"""Turn type text into fully qualified, accepted type names.

Two inputs: an annotation in Python syntax (`normalize`), and the text of a
docstring return or parameter description (`type_from_text`).
"""
from __future__ import annotations

import re
import ast
from typing import Callable

from hoststubs.names import Names

ANY = 'typing.Any'
NONE = 'None'

# Builtins a docstring may name as a type. Others (`set`, `filter`, `range`,
# `type`) are also English words, so they are not read from prose.
PROSE_BUILTINS = frozenset({'int', 'float', 'str', 'bool', 'list', 'tuple', 'dict', 'bytes'})
PROSE_LITERALS = {'None': NONE, 'True': 'builtins.bool', 'False': 'builtins.bool'}

# `T`, `T or U`, `a T object`, then the end or a clause that cannot change the type.
# "Layer name." must not match: the word after the type decides what the text means.
PROSE_TYPE = re.compile(
    r'^(?:an? |the )?(?P<first>[\w.]*\w)'
    r'(?P<rest>(?:,? or (?:an? )?[\w.]*\w)*)'
    r'(?: object)?'
    r'(?=$|[.,;:]|\s+(?:if|when|on|otherwise|-)\s)',
)


class _Normalizer:
    """Turn an annotation as written in one module into fully qualified, accepted names."""

    def __init__(self, resolve: Callable[[str], str | None], strict: bool = False) -> None:
        self._resolve = resolve
        # Strict: an unknown name inside a container rejects the whole type
        # instead of becoming Any. For hand-written types, where it is a typo.
        self._strict = strict

    # === PRIVATE === #

    def _literal(self, node: ast.expr) -> str | None:
        """Widen one `Literal[...]` element to its type."""
        if isinstance(node, ast.Constant):
            return 'None' if node.value is None else f'builtins.{type(node.value).__name__}'
        if isinstance(node, ast.UnaryOp) and isinstance(node.operand, ast.Constant):
            return f'builtins.{type(node.operand.value).__name__}'
        if isinstance(node, ast.Attribute):
            # An enum member: the type is the enum class.
            return self._resolve(ast.unparse(node.value))
        return None

    def _union(self, members: list[str | None]) -> str | None:
        if None in members or (ANY in members and not self._strict):
            return None
        return ' | '.join(dict.fromkeys(members))

    def _argument(self, node: ast.expr) -> str | None:
        if isinstance(node, ast.Constant) and node.value is Ellipsis:
            return '...'
        if isinstance(node, ast.List):
            items = [self._argument(item) for item in node.elts]
            return None if None in items else '[' + ', '.join(items) + ']'

        found = self.normalize(node)
        if found is None and not self._strict:
            return ANY
        return found

    def _subscript(self, node: ast.Subscript) -> str | None:
        arguments = node.slice.elts if isinstance(node.slice, ast.Tuple) else [node.slice]

        if ast.unparse(node.value) == 'Literal':
            return self._union([self._literal(argument) for argument in arguments])

        container = self.normalize(node.value)
        normalized = [self._argument(argument) for argument in arguments]
        if container is None or None in normalized:
            return None
        return f'{container}[{", ".join(normalized)}]'

    def _union_members(self, node: ast.expr) -> list[ast.expr]:
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
            return self._union_members(node.left) + self._union_members(node.right)
        return [node]

    # === PUBLIC === #

    def normalize(self, node: ast.expr) -> str | None:
        if isinstance(node, ast.Constant) and node.value is None:
            return 'None'
        if isinstance(node, (ast.Name, ast.Attribute)):
            dotted = ast.unparse(node)
            if dotted == 'LiteralString':
                return 'builtins.str'
            return self._resolve(dotted)
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
            return self._union([self.normalize(member) for member in self._union_members(node)])
        if isinstance(node, ast.Subscript):
            return self._subscript(node)
        return None


def _normalize(annotation: str, resolve: Callable[[str], str | None]) -> str | None:
    try:
        tree = ast.parse(annotation.strip(), mode='eval')
    except SyntaxError:
        # Pyright prints some types that are not Python, such as `(x) -> None`.
        return None

    result = _Normalizer(resolve).normalize(tree.body)
    return None if result == ANY else result


def normalize(annotation: str, names: Names, module: str) -> str | None:
    """Return the accepted, fully qualified form of a Python annotation, or None.

    Names mean what they mean in `module`, as in source code.
    """
    return _normalize(annotation, lambda dotted: names.resolve(dotted, module))


def normalize_strict(annotation: str, resolve: Callable[[str], str | None]) -> str | None:
    """Normalize a hand-written annotation. Any unknown name rejects it; `Any` is a valid answer."""
    try:
        tree = ast.parse(annotation.strip(), mode='eval')
    except SyntaxError:
        return None
    return _Normalizer(resolve, strict=True).normalize(tree.body)


def resolve_documented(dotted: str, names: Names, module: str) -> str | None:
    """Resolve a name written in a docstring.

    A docstring addresses the user, so a dotted name is a public path first:
    `nuke.Node` in a hiero.core docstring is Nuke's node, although inside
    hiero.core the name `nuke` is the module hiero.core.nuke.
    """
    qualified = names.accept(dotted) if '.' in dotted else None
    return qualified or names.resolve(dotted, module)


def _prose_token(token: str, names: Names, module: str, type_names: dict[str, str]) -> str | None:
    if token in PROSE_LITERALS:
        return PROSE_LITERALS[token]
    if token in type_names:
        return type_names[token]
    if token in PROSE_BUILTINS:
        return f'builtins.{token}'
    if token[0].islower() and '.' not in token:
        # A lowercase word is prose even when a class has that name.
        return None
    return resolve_documented(token, names, module)


def type_from_text(
    text: str, names: Names, module: str, type_names: dict[str, str],
) -> str | None:
    """Read a type from docstring text, only when the text states one outright.

    'Node or None if it does not exist.' gives `Node | None`. 'The root node.'
    and 'List of nodes' give nothing: a word inside a sentence is not evidence.
    `type_names` maps host spellings such as 'String' to a type.
    """
    text = text.strip()
    if not text:
        return None

    if '[' in text or '|' in text:
        return _normalize(
            text.rstrip('.'), lambda dotted: resolve_documented(dotted, names, module),
        )

    match = PROSE_TYPE.match(text)
    if match is None:
        return None

    tokens = [match.group('first')]
    tokens += re.findall(r'or (?:an? )?([\w.]*\w)', match.group('rest'))

    types = [_prose_token(token, names, module, type_names) for token in tokens]
    if None in types:
        return None
    return ' | '.join(dict.fromkeys(types))


def split_top_level(text: str, separator: str) -> list[str]:
    """Split a type on `separator`, ignoring separators inside brackets."""
    pieces = ['']
    depth = 0
    index = 0
    while index < len(text):
        char = text[index]
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1

        if depth == 0 and text.startswith(separator, index):
            pieces.append('')
            index += len(separator)
        else:
            pieces[-1] += char
            index += 1
    return pieces


def split_generic(type_: str) -> tuple[str, list[str]]:
    """Split `list[nuke.Node]` into ('list', ['nuke.Node']); a plain name has no arguments."""
    base, bracket, rest = type_.partition('[')
    if not bracket:
        return type_, []
    return base, split_top_level(rest[:-1], ', ')
