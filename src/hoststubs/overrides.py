"""Hand-authored corrections. They are the only manual input and always win.

One `.pyi` file per module in the host's `overrides` directory, named after
the module (`nuke.pyi`, `hiero.core.pyi`). Supported, and nothing else:

    # src: manual
    def root() -> Root: ...               replaces nuke.root, or adds it

    class Node:
        # src: manual
        def knob(self, p: str | int, follow_link: bool = ...) -> Knob | None: ...

    # src: manual
    @overload
    def execute(...) -> None: ...         a run of @overload replaces the whole set
    @overload
    def execute(...) -> None: ...

    # src: manual
    # delete: nuke.Foo.bar                removes a symbol

Every entry needs `# src: manual` or `# src: review` on the line above it.
Types are written as in a stub of that module. `QtGui.QImage` means the
host's Qt binding. A type that does not resolve is a build error.
"""
from __future__ import annotations

import re
import ast
from pathlib import Path
from dataclasses import dataclass

from hoststubs import ir
from hoststubs.names import TYPED_QT_BINDINGS, Names
from hoststubs.resolve import Param, Signature, is_informative
from hoststubs.docstrings import POSITIONAL, VAR_KEYWORD, VAR_POSITIONAL
from hoststubs.annotations import ANY, normalize_strict, resolve_documented

SOURCE = 'override'
PROVENANCE = re.compile(r'^\s*# src: (manual|review)\s*$')
DELETE = re.compile(r'^# delete: ([\w.]+)\s*$')

POSITIONAL_ONLY = 'POSITIONAL_ONLY'
KEYWORD_ONLY = 'KEYWORD_ONLY'
BINDINGS = {'staticmethod': 'static', 'classmethod': 'class'}

FunctionDef = ast.FunctionDef | ast.AsyncFunctionDef


class OverrideError(ValueError):
    """An override file is wrong. The message starts with `file:line`."""


@dataclass(frozen=True)
class Override:
    signatures: tuple[Signature, ...]
    doc: str | None
    # 'static', 'class', 'instance', or None for a module-level function.
    binding: str | None
    provenance: str
    location: str


@dataclass(frozen=True)
class Overrides:
    functions: dict[str, Override]
    # Path of each removed symbol -> where the removal is written.
    deleted: dict[str, str]


def _decorator_names(function: FunctionDef) -> list[str]:
    return [ast.unparse(decorator).rsplit('.', 1)[-1] for decorator in function.decorator_list]


def _first_line(function: FunctionDef) -> int:
    lines = [function.lineno] + [decorator.lineno for decorator in function.decorator_list]
    return min(lines)


class _ModuleLoader:
    def __init__(self, path: Path, dump: ir.Dump, names: Names) -> None:
        self._path = path
        self._module = path.stem
        self._dump = dump
        self._names = names

        self._lines = path.read_text(encoding='utf-8').splitlines()
        self.functions: dict[str, Override] = {}
        self.deleted: dict[str, str] = {}

    # === PRIVATE === #

    def _error(self, line: int, message: str) -> OverrideError:
        return OverrideError(f'{self._path}:{line}: {message}')

    def _provenance(self, line: int) -> str:
        """Read the `# src:` comment on the line above `line` (1-based)."""
        match = PROVENANCE.match(self._lines[line - 2]) if line >= 2 else None
        if match is None:
            raise self._error(line, 'missing "# src: manual" or "# src: review" on the line above')
        return match.group(1)

    def _resolve_name(self, dotted: str) -> str | None:
        if dotted.split('.')[0].startswith('Qt'):
            qt = self._dump.qt
            if qt is None or qt.binding not in TYPED_QT_BINDINGS:
                # The binding ships no types, so no consumer could resolve the name.
                return ANY
            return self._names.accept(f'{qt.binding}.{dotted}')
        return resolve_documented(dotted, self._names, self._module)

    def _type(self, annotation: ast.expr | None, line: int) -> str:
        if annotation is None:
            return ANY

        text = ast.unparse(annotation)
        found = normalize_strict(text, self._resolve_name)
        if found is None:
            raise self._error(line, f'type {text!r} does not resolve to a known class')
        return found

    def _signature(self, function: FunctionDef) -> Signature:
        if function.returns is None:
            raise self._error(function.lineno, f'{function.name} has no return annotation')

        arguments = function.args
        positional = arguments.posonlyargs + arguments.args
        first_default = len(positional) - len(arguments.defaults)

        params = []
        for index, argument in enumerate(positional):
            kind = POSITIONAL_ONLY if index < len(arguments.posonlyargs) else POSITIONAL
            type_ = self._type(argument.annotation, function.lineno)
            params.append(Param(argument.arg, kind, index >= first_default, type_, SOURCE))

        if arguments.vararg:
            type_ = self._type(arguments.vararg.annotation, function.lineno)
            params.append(Param(arguments.vararg.arg, VAR_POSITIONAL, False, type_, SOURCE))

        for argument, default in zip(arguments.kwonlyargs, arguments.kw_defaults):
            type_ = self._type(argument.annotation, function.lineno)
            params.append(Param(argument.arg, KEYWORD_ONLY, default is not None, type_, SOURCE))

        if arguments.kwarg:
            type_ = self._type(arguments.kwarg.annotation, function.lineno)
            params.append(Param(arguments.kwarg.arg, VAR_KEYWORD, False, type_, SOURCE))

        returns = self._type(function.returns, function.lineno)
        return Signature(tuple(params), returns, SOURCE, SOURCE)

    def _check_against_runtime(self, path: str, signature: Signature, line: int) -> None:
        """A Python function reports its real parameters; the override must name the same ones."""
        _, member = self._names.find(path)
        runtime = member.signature if isinstance(member, ir.Function) else None
        if runtime is None or not is_informative(runtime):
            return

        expected = [param.name for param in runtime.params]
        written = [param.name for param in signature.params]
        if written != expected:
            raise self._error(line, f'{path} takes {expected}, the override names {written}')

    def _recorded_path(self, prefix: str, name: str, line: int) -> str:
        """Path under which the dump records `prefix.name`, following re-exports."""
        container = prefix
        if prefix not in self._dump.modules:
            container, member = self._names.find(prefix)
            if not isinstance(member, ir.Class):
                raise self._error(line, f'{prefix} is not a module or class in the dump')

        path, member = self._names.find(f'{container}.{name}')
        return path if member is not None else f'{container}.{name}'

    def _add(self, prefix: str, run: list[FunctionDef], in_class: bool) -> None:
        first = run[0]
        line = _first_line(first)
        path = self._recorded_path(prefix, first.name, line)

        is_overload = ['overload' in _decorator_names(function) for function in run]
        if len(run) > 1 and not all(is_overload):
            raise self._error(line, f'{path} is defined {len(run)} times without @overload')
        if path in self.functions:
            other = self.functions[path].location
            raise self._error(line, f'{path} is already overridden at {other}')

        signatures = tuple(self._signature(function) for function in run)
        for signature in signatures:
            self._check_against_runtime(path, signature, line)

        decorators = _decorator_names(first)
        binding = next((BINDINGS[name] for name in decorators if name in BINDINGS), None)
        self.functions[path] = Override(
            signatures=signatures,
            doc=ast.get_docstring(first),
            binding=binding or ('instance' if in_class else None),
            provenance=self._provenance(line),
            location=f'{self._path}:{line}',
        )

    def _visit(self, body: list[ast.stmt], prefix: str, in_class: bool) -> None:
        run: list[FunctionDef] = []

        def flush() -> None:
            if run:
                self._add(prefix, list(run), in_class)
                run.clear()

        for node in body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if run and run[0].name != node.name:
                    flush()
                run.append(node)
                continue

            flush()
            is_docstring = isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant)
            if isinstance(node, ast.ClassDef):
                self._visit(node.body, f'{prefix}.{node.name}', in_class=True)
            elif not is_docstring and not isinstance(node, ast.Pass):
                kind = type(node).__name__
                raise self._error(node.lineno, f'{kind} is not supported, only def and class')
        flush()

    def _load_deletions(self) -> None:
        for index, text in enumerate(self._lines, start=1):
            match = DELETE.match(text)
            if match is None:
                continue

            path = match.group(1)
            self._provenance(index)
            if self._names.find(path)[1] is None:
                raise self._error(index, f'cannot delete {path}: not in the dump')
            self.deleted[path] = f'{self._path}:{index}'

    # === PUBLIC === #

    def load(self) -> None:
        if self._module not in self._dump.modules:
            raise self._error(1, f'{self._module} is not a module in the dump')

        try:
            tree = ast.parse('\n'.join(self._lines))
        except SyntaxError as error:
            raise self._error(error.lineno or 1, f'not valid Python: {error.msg}') from error

        self._visit(tree.body, self._module, in_class=False)
        self._load_deletions()


def load_overrides(directory: Path, dump: ir.Dump, names: Names) -> Overrides:
    functions: dict[str, Override] = {}
    deleted: dict[str, str] = {}

    for path in sorted(directory.glob('*.pyi')):
        loader = _ModuleLoader(path, dump, names)
        loader.load()
        functions.update(loader.functions)
        deleted.update(loader.deleted)

    return Overrides(functions, deleted)
