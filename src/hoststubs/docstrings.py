"""Read the machine-readable parts of a C-extension docstring.

Two parts: the signature line (`self.knob(p[, follow_link]) -> Knob`) and
the epydoc or reST fields (`@param p:`, `:return:`, `@rtype:`). This module
only extracts text. Deciding whether a text is a type is `annotations`' job.
"""
from __future__ import annotations

import re
import keyword
from dataclasses import dataclass

POSITIONAL = 'POSITIONAL_OR_KEYWORD'
VAR_POSITIONAL = 'VAR_POSITIONAL'
VAR_KEYWORD = 'VAR_KEYWORD'

# pybind11 lists overloads as numbered lines under this marker.
OVERLOAD_MARKER = 'Overloaded function.'

FIELD = re.compile(
    r'^\s*[@:](?P<field>param|parm|type|returns?|rtype)\b[ \t]*(?P<name>\*{0,2}\w+)?[ \t]*:'
    r'[ \t]*(?P<text>.*)$',
    re.MULTILINE,
)

OPENERS = '([{<'
CLOSERS = ')]}>'


@dataclass(frozen=True)
class DocParam:
    name: str
    kind: str
    annotation: str | None
    default: str | None
    optional: bool


@dataclass(frozen=True)
class DocSignature:
    # None when the line has no parameter list or it cannot be a Python signature.
    params: tuple[DocParam, ...] | None
    returns: str | None


@dataclass(frozen=True)
class DocFields:
    params: dict[str, str]
    param_types: dict[str, str]
    returns: str | None
    return_type: str | None


def _split_params(text: str) -> list[tuple[str, bool]]:
    """Split `p[, follow_link]` into (piece, is_optional), dropping the optional brackets."""
    pieces: list[tuple[str, bool]] = []
    current = ''
    current_optional = False
    rest_optional = False
    optional_depth = 0
    depth = 0

    for char in text:
        is_default_value = current.rstrip().endswith('=')

        if char == '[' and depth == 0 and not is_default_value:
            optional_depth += 1
            rest_optional = True
            if not current.strip():
                current_optional = True
            continue
        if char == ']' and depth == 0 and optional_depth:
            optional_depth -= 1
            continue

        if char in OPENERS:
            depth += 1
        elif char in CLOSERS:
            depth = max(depth - 1, 0)

        if char == ',' and depth == 0:
            pieces.append((current.strip(), current_optional))
            current = ''
            current_optional = rest_optional
        else:
            current += char

    pieces.append((current.strip(), current_optional))
    return [(piece, optional) for piece, optional in pieces if piece]


def _parse_param(piece: str, optional: bool) -> DocParam | None:
    if piece in ('/', '*'):
        return None
    if piece == '...':
        return DocParam('args', VAR_POSITIONAL, None, None, False)
    if piece.startswith('**'):
        return DocParam(piece[2:].strip(), VAR_KEYWORD, None, None, False)
    if piece.startswith('*'):
        return DocParam(piece[1:].strip(), VAR_POSITIONAL, None, None, False)

    declaration, equals, default = (part.strip() for part in piece.partition('='))
    name, colon, annotation = (part.strip() for part in declaration.partition(':'))

    return DocParam(
        name=name,
        kind=POSITIONAL,
        annotation=annotation if colon else None,
        default=default if equals else None,
        optional=optional or bool(equals),
    )


def parse_params(text: str) -> tuple[DocParam, ...] | None:
    """Parse the text between the parentheses, or return None if it is not a signature."""
    params: list[DocParam] = []
    seen_optional = False

    for piece, optional in _split_params(text):
        param = _parse_param(piece, optional)
        if param is None:
            continue

        if not param.name.isidentifier() or keyword.iskeyword(param.name):
            return None
        if any(param.name == other.name for other in params):
            return None
        is_variadic = param.kind in (VAR_POSITIONAL, VAR_KEYWORD)
        if is_variadic and any(param.kind == other.kind for other in params):
            return None

        if param.kind == POSITIONAL:
            # Python allows no required parameter after an optional one.
            if seen_optional and not param.optional:
                param = DocParam(param.name, param.kind, param.annotation, param.default, True)
            seen_optional = seen_optional or param.optional

        params.append(param)

    return tuple(params)


def _closing_paren(text: str, opening: int) -> int | None:
    depth = 0
    for index in range(opening, len(text)):
        if text[index] == '(':
            depth += 1
        elif text[index] == ')':
            depth -= 1
            if depth == 0:
                return index
    return None


def _parse_line(line: str, name: str) -> DocSignature | None:
    """Parse `[1. ][owner.]name(params) [-> returns]` or `[owner.]name -> returns`."""
    head = re.match(r'^\s*(?:\d+\.\s*)?(?:[\w.]+\.)?' + re.escape(name) + r'\s*(?=\(|->)', line)
    if head is None:
        return None

    params = None
    rest = line[head.end():]
    if rest.startswith('('):
        closing = _closing_paren(rest, 0)
        if closing is None:
            return None
        params = parse_params(rest[1:closing])
        rest = rest[closing + 1:]

    rest = rest.strip()
    if rest and not rest.startswith('->'):
        # Prose that happens to start with a call, such as an example.
        return None

    returns = rest[2:].strip() or None
    return DocSignature(params=params, returns=returns)


def signature_lines(doc: str, name: str) -> list[DocSignature]:
    """Return the signatures a docstring declares for `name`. More than one means overloads."""
    lines = doc.splitlines()

    if OVERLOAD_MARKER in doc:
        numbered = [line for line in lines if re.match(r'^\s*\d+\.\s', line)]
        return [found for line in numbered if (found := _parse_line(line, name))]

    # Only the leading lines: a matching line further down is usually an example.
    signatures = []
    for line in lines:
        if not line.strip():
            if signatures:
                break
            continue

        found = _parse_line(line, name)
        if found is None:
            break
        signatures.append(found)
    return signatures


def fields(doc: str) -> DocFields:
    params: dict[str, str] = {}
    param_types: dict[str, str] = {}
    returns = None
    return_type = None

    for match in FIELD.finditer(doc):
        field = match.group('field')
        name = (match.group('name') or '').lstrip('*')
        text = match.group('text').strip()

        if field in ('param', 'parm') and name:
            params.setdefault(name, text)
        elif field == 'type' and name:
            param_types.setdefault(name, text)
        elif field in ('return', 'returns') and returns is None:
            # `@return name: text` is not a form; the "name" is the first word of the text.
            returns = f'{name}: {text}' if name else text
        elif field == 'rtype' and return_type is None:
            return_type = text

    return DocFields(params, param_types, returns, return_type)


def is_documented_optional(doc: str, doc_fields: DocFields, name: str) -> bool:
    """True when the docstring says in words that parameter `name` can be left out.

    Signature lines often list optional parameters as if required
    (`allNodes(filter, group)` with ':param filter: Optional.'). Treating
    those as required would report errors on correct calls.
    """
    described = f'{doc_fields.params.get(name, "")} {doc_fields.param_types.get(name, "")}'
    if re.search(r'\boptional\b|\bdefaults? (?:is|to)\b', described, re.IGNORECASE):
        return True

    escaped = re.escape(name)
    sentence = (
        rf'\boptional (?:parameter |argument )?{escaped}\b'
        rf'|\b{escaped}(?: and \w+)? (?:is|are) optional\b'
        rf'|\b\w+ and {escaped} are optional\b'
    )
    return re.search(sentence, doc, re.IGNORECASE) is not None
