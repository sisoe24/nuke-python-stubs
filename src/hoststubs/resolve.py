"""Pick one type for every parameter and return value, by a fixed source priority."""
from __future__ import annotations

import re
from dataclasses import dataclass

from hoststubs import ir
from hoststubs.names import Names
from hoststubs.inference import Inferred
from hoststubs.docstrings import (POSITIONAL, VAR_KEYWORD, VAR_POSITIONAL, DocParam, DocFields,
                                  DocSignature, fields, signature_lines, is_documented_optional)
from hoststubs.annotations import (ANY, NONE, normalize, split_generic, split_top_level,
                                   type_from_text)

# Highest priority first. A candidate from an earlier source always wins.
SOURCES = (
    'override',
    'probe',
    'signature',
    'doc_signature',
    'doc_field',
    'inference',
    'default',
    'dunder',
    'probe_weak',
    'any',
)

BOOL = 'builtins.bool'
INT = 'builtins.int'
STR = 'builtins.str'

DUNDER_RETURNS = {
    **dict.fromkeys(('__eq__', '__ne__', '__lt__', '__le__', '__gt__', '__ge__'), BOOL),
    **dict.fromkeys(('__bool__', '__contains__'), BOOL),
    **dict.fromkeys(('__len__', '__hash__', '__int__', '__index__', '__sizeof__'), INT),
    **dict.fromkeys(('__repr__', '__str__', '__format__'), STR),
    **dict.fromkeys(('__init__', '__setattr__', '__delattr__', '__setitem__', '__delitem__'), NONE),
    '__float__': 'builtins.float',
    '__new__': 'typing.Self',
}

# A default of these types says what the parameter accepts. `int` does not:
# `scale=1` usually takes a float too, and a wrong type is worse than Any.
DEFAULT_TYPES = frozenset({BOOL, STR, 'builtins.float'})
QUOTED = re.compile(r'''^(['"]).*\1$''')
FLOAT_LITERAL = re.compile(r'^-?\d+\.\d*$')

RECEIVERS = {'instance': 'self', 'class': 'cls'}


@dataclass(frozen=True)
class Candidate:
    type: str
    source: str


@dataclass(frozen=True)
class Observed:
    """What the probe saw for one function."""
    candidate: Candidate
    # Each distinct type seen, before they were merged into a common base.
    seen: tuple[str, ...]


@dataclass(frozen=True)
class Param:
    name: str
    kind: str
    has_default: bool
    type: str
    source: str


@dataclass(frozen=True)
class Signature:
    params: tuple[Param, ...]
    returns: str
    returns_source: str
    # Where the parameter list came from: 'signature', 'doc_signature' or 'any'.
    shape_source: str


def pick(candidates: list[Candidate]) -> Candidate:
    known = [candidate for candidate in candidates if candidate.type != ANY]
    if not known:
        return Candidate(ANY, 'any')
    return min(known, key=lambda candidate: SOURCES.index(candidate.source))


def _is_dunder(name: str) -> bool:
    return name.startswith('__') and name.endswith('__')


def is_informative(signature: ir.Signature) -> bool:
    """False for `(self, /, *args, **kwargs)`, which C slots report and which says nothing."""
    named = [
        param for param in signature.params[1:]
        if param.kind not in (VAR_POSITIONAL, VAR_KEYWORD)
    ]
    has_variadic = any(param.kind in (VAR_POSITIONAL, VAR_KEYWORD) for param in signature.params)
    return bool(named) or not has_variadic


def _default_type(default: ir.Value | None, doc_default: str | None) -> str | None:
    if default is not None:
        return default.type if default.type in DEFAULT_TYPES else None
    if doc_default is None:
        return None
    if doc_default in ('True', 'False'):
        return BOOL
    if QUOTED.match(doc_default):
        return STR
    if FLOAT_LITERAL.match(doc_default):
        return 'builtins.float'
    return None


class Resolver:
    def __init__(
        self,
        dump: ir.Dump,
        names: Names,
        type_names: dict[str, str],
        inferred: dict[str, Inferred],
        observed: dict[str, Observed],
    ) -> None:
        self._dump = dump
        self._names = names
        self._type_names = type_names
        self._inferred = inferred
        self._observed = observed

    # === PRIVATE === #

    def _from_text(self, text: str | None, source: str, scope: str) -> list[Candidate]:
        if not text:
            return []
        found = type_from_text(text, self._names, scope, self._type_names)
        return [Candidate(found, source)] if found else []

    def _from_annotation(self, annotation: str | None, source: str, scope: str) -> list[Candidate]:
        if not annotation:
            return []
        # pybind11 writes the runtime module (`_nuke.Node`), which only `accept` knows.
        found = normalize(annotation, self._names, scope) or self._names.accept(annotation)
        return [Candidate(found, source)] if found else []

    def _param(
        self,
        name: str,
        kind: str,
        candidates: list[Candidate],
        default: ir.Value | None = None,
        doc_default: str | None = None,
        has_default: bool = False,
    ) -> Param:
        default_type = _default_type(default, doc_default)
        is_instance = default is not None and not default.type.startswith('builtins.')
        if default_type is None and is_instance:
            # `script=ScriptWriter()`: an instance of a host class as the default.
            default_type = self._names.accept(default.type)
        if default_type:
            candidates = candidates + [Candidate(default_type, 'default')]

        chosen = pick(candidates)
        type_ = chosen.type

        is_none_default = (default is not None and default.repr == 'None') or doc_default == 'None'
        if is_none_default and type_ != ANY and NONE not in type_.split(' | '):
            type_ = f'{type_} | {NONE}'

        return Param(name, kind, has_default, type_, chosen.source)

    def _runtime_params(
        self, signature: ir.Signature, scope: str, doc: DocSignature | None,
        doc_fields: DocFields, inferred: Inferred | None,
    ) -> tuple[Param, ...]:
        doc_params = {param.name: param for param in (doc.params or ())} if doc else {}

        params = []
        for param in signature.params:
            documented = doc_params.get(param.name)
            doc_annotation = documented.annotation if documented else None
            candidates = (
                self._from_annotation(param.annotation, 'signature', scope)
                + self._from_annotation(doc_annotation, 'doc_signature', scope)
                + self._field_candidates(param.name, doc_fields, scope)
            )
            if inferred and param.name in inferred.params:
                candidates.append(Candidate(inferred.params[param.name], 'inference'))

            params.append(self._param(
                param.name, param.kind, candidates,
                default=param.default, has_default=param.default is not None,
            ))
        return tuple(params)

    def _doc_params(
        self, documented: tuple[DocParam, ...], receiver: str | None, scope: str,
        doc: str, doc_fields: DocFields,
    ) -> tuple[Param, ...]:
        params = []
        if receiver and (not documented or documented[0].name != receiver):
            params.append(Param(receiver, POSITIONAL, False, ANY, 'any'))

        seen_optional = False
        for param in documented:
            # Python allows no required parameter after an optional one.
            is_positional = param.kind == POSITIONAL
            documented_optional = is_documented_optional(doc, doc_fields, param.name)
            optional = is_positional and (seen_optional or param.optional or documented_optional)
            seen_optional = seen_optional or optional

            candidates = (
                self._from_annotation(param.annotation, 'doc_signature', scope)
                + self._field_candidates(param.name, doc_fields, scope)
            )
            params.append(self._param(
                param.name, param.kind, candidates,
                doc_default=param.default, has_default=optional,
            ))
        return tuple(params)

    def _field_candidates(self, name: str, doc_fields: DocFields, scope: str) -> list[Candidate]:
        return (
            self._from_text(doc_fields.param_types.get(name), 'doc_field', scope)
            + self._from_text(doc_fields.params.get(name), 'doc_field', scope)
        )

    def _unknown_params(self, receiver: str | None) -> tuple[Param, ...]:
        params = [Param(receiver, POSITIONAL, False, ANY, 'any')] if receiver else []
        params.append(Param('args', VAR_POSITIONAL, False, ANY, 'any'))
        params.append(Param('kwargs', VAR_KEYWORD, False, ANY, 'any'))
        return tuple(params)

    # === PUBLIC === #

    def _widen(self, observed: str) -> str:
        """Replace each observed class by its topmost base in the dump.

        The probe saw `Root` where a function may return any `Node`. The
        base is always true; the subclass is true for this scene only.
        """
        base, arguments = split_generic(observed)
        if arguments:
            return f'{base}[{", ".join(self._widen(argument) for argument in arguments)}]'
        return self._names.ancestors(observed)[-1]

    def _agrees(self, observed: str, documented: str) -> bool:
        """True when the observed type is one the documented type allows."""
        observed_base, observed_arguments = split_generic(observed)

        for member in split_top_level(documented, ' | '):
            base, arguments = split_generic(member)
            if not arguments and not observed_arguments:
                if member in self._names.ancestors(observed):
                    return True
            elif base == observed_base and len(arguments) == len(observed_arguments):
                # A bare `list` has no arguments, so `list[str]` refines it instead.
                if all(map(self._agrees, observed_arguments, arguments)):
                    return True
        return False

    def _with_probe(self, documented: Candidate, path: str) -> Candidate:
        """Combine the best non-probe candidate with what the probe observed.

        The probe outranks a docstring only where they contradict. Where the
        observation fits the documented type, the docstring is the wider and
        safer statement: it knows `Node | None`, the probe saw one `Node`.
        """
        observed = self._observed.get(path)
        if observed is None:
            return documented

        candidate = observed.candidate
        if candidate.source != 'probe':
            return pick([documented, candidate])

        widened = self._widen(candidate.type)
        if documented.source == 'any':
            return Candidate(widened, 'probe')
        if all(self._agrees(seen, documented.type) for seen in observed.seen):
            return documented

        if self._is_class_type(documented.type) and self._is_class_type(widened):
            # Two host classes: the function returns one or the other by state
            # (`Bin.parentBin()` is a Bin, or the Project for a top-level bin).
            members = split_top_level(documented.type, ' | ') + [widened]
            return Candidate(' | '.join(dict.fromkeys(members)), 'probe')
        return Candidate(widened, 'probe')

    def _is_class_type(self, type_: str) -> bool:
        members = [member for member in split_top_level(type_, ' | ') if member != NONE]
        return bool(members) and all(self._names.is_class(member) for member in members)

    def property(self, path: str) -> Signature:
        """Resolve a C property. It has no docstring evidence, only what the probe read."""
        returns = self._with_probe(Candidate(ANY, 'any'), path)
        return Signature((), returns.type, returns.source, 'property')

    def function(
        self, function: ir.Function, name: str, module: str, path: str,
    ) -> tuple[Signature, ...]:
        """Resolve the function recorded at `path`. Several results are overloads."""
        # A Python function reads names from its own module; a C function has none,
        # so its docstring is read in the public module that shows it.
        scope = function.origin if function.origin in self._dump.modules else module
        doc = function.doc or ''

        doc_lines = signature_lines(doc, name)
        if not doc_lines and function.qualname:
            doc_lines = signature_lines(doc, function.qualname.rsplit('.', 1)[-1])
        doc_fields = fields(doc)

        inferred = self._inferred.get(f'{function.origin}.{function.qualname}')
        receiver = RECEIVERS.get(function.binding)

        shared = (
            self._from_text(doc_fields.return_type, 'doc_field', scope)
            + self._from_text(doc_fields.returns, 'doc_field', scope)
        )
        if function.signature:
            shared += self._from_annotation(function.signature.returns, 'signature', scope)
        if inferred and inferred.returns:
            shared.append(Candidate(inferred.returns, 'inference'))
        if name in DUNDER_RETURNS:
            shared.append(Candidate(DUNDER_RETURNS[name], 'dunder'))

        runtime = function.signature
        if runtime and (is_informative(runtime) or not any(line.params for line in doc_lines)):
            first = doc_lines[0] if doc_lines else None
            params = self._runtime_params(runtime, scope, first, doc_fields, inferred)
            variants = [(params, first.returns if first else None, 'signature')]
        elif any(line.params is not None for line in doc_lines):
            variants = [
                (
                    self._doc_params(line.params, receiver, scope, doc, doc_fields),
                    line.returns,
                    'doc_signature',
                )
                for line in doc_lines if line.params is not None
            ]
        else:
            first = doc_lines[0] if doc_lines else None
            variants = [(self._unknown_params(receiver), first.returns if first else None, 'any')]

        signatures = []
        for params, returns_text, shape_source in variants:
            documented = pick(shared + self._from_text(returns_text, 'doc_signature', scope))
            returns = self._with_probe(documented, path)
            signatures.append(Signature(params, returns.type, returns.source, shape_source))
        return tuple(signatures)


def resolve_functions(
    resolver: Resolver,
    dump: ir.Dump,
    overridden: dict[str, tuple[Signature, ...]],
    deleted: set[str],
) -> dict[str, tuple[Signature, ...]]:
    """Resolve every function, keyed by the path where the dump records it.

    `overridden` replaces or adds whole functions; `deleted` paths are removed.
    """
    resolved: dict[str, tuple[Signature, ...]] = {}

    def visit(members: dict[str, ir.Member], prefix: str, module: str) -> None:
        for name, member in members.items():
            path = f'{prefix}.{name}'
            if isinstance(member, ir.Class):
                visit(member.members, path, module)
            elif isinstance(member, ir.Function):
                resolved[path] = resolver.function(member, name, module, path)
            elif isinstance(member, ir.Property) and member.getter:
                resolved[path] = resolver.function(member.getter, name, module, path)
            elif isinstance(member, ir.Property):
                resolved[path] = (resolver.property(path),)

    for module_name, module in dump.modules.items():
        visit(module.members, module_name, module_name)

    resolved.update(overridden)
    return {path: signatures for path, signatures in resolved.items() if path not in deleted}
