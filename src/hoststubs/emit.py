"""Write one `.pyi` file per module from the dump and the resolved signatures."""
from __future__ import annotations

import re
import json
import shutil
import textwrap
from pathlib import Path
from dataclasses import dataclass

from hoststubs import ir
from hoststubs.host import HostConfig
from hoststubs.names import TYPED_QT_BINDINGS, Names
from hoststubs.resolve import Param, Signature
from hoststubs.overrides import Overrides
from hoststubs.docstrings import VAR_KEYWORD, VAR_POSITIONAL
from hoststubs.annotations import NONE

INDENT = '    '
PYTHON_FUNCTION = 'builtins.function'
TYPE_NAME = re.compile(r'[A-Za-z_][\w.]*')

POSITIONAL_ONLY = 'POSITIONAL_ONLY'
KEYWORD_ONLY = 'KEYWORD_ONLY'
DECORATORS = {'static': '@staticmethod', 'class': '@classmethod'}

# Slots every C class reports. In a stub, `__getattribute__` and `__setattr__`
# would make any attribute access valid and hide misspelled names.
SKIPPED_DUNDERS = frozenset({
    '__getattribute__', '__setattr__', '__delattr__', '__init_subclass__', '__subclasshook__',
    '__reduce__', '__reduce_ex__', '__sizeof__', '__dir__', '__format__', '__new__',
    '__class_getitem__',
})


@dataclass(frozen=True)
class Context:
    dump: ir.Dump
    names: Names
    resolved: dict[str, tuple[Signature, ...]]
    overrides: Overrides


def _is_dunder(name: str) -> bool:
    return name.startswith('__') and name.endswith('__')


def _is_private(name: str) -> bool:
    return name.startswith('_') and not _is_dunder(name)


def docstring(doc: str | None, indent: str) -> list[str]:
    """Render `doc` as an indented docstring literal that evaluates back to the same text."""
    if not doc or not doc.strip():
        return []

    text = doc.replace('\\', '\\\\').replace('"""', '\\"\\"\\"')
    if text.endswith('"'):
        text = text[:-1] + '\\"'

    lines = text.split('\n')
    if len(lines) == 1:
        return [f'{indent}"""{text}"""']

    # Indented like the code around it; inspect.cleandoc removes it again.
    rest = textwrap.indent('\n'.join(lines[1:]), indent).split('\n')
    return [f'{indent}"""{lines[0]}', *rest, f'{indent}"""']


class ModuleEmitter:
    """Builds the text of one stub file."""

    def __init__(self, name: str, module: ir.Module, context: Context) -> None:
        self._name = name
        self._module = module
        self._context = context
        self._names = context.names

        self._imports: set[str] = set()

    # === PRIVATE === #

    def _import_module(self, module: str) -> str:
        """Import `module` under a private alias, so it cannot collide with a member name."""
        alias = '_' + module.replace('.', '_')
        self._imports.add(f'import {module} as {alias}')
        return alias

    def _short(self, module: str, name: str, shadowed: frozenset[str]) -> str:
        """Use `name` from `module` by its short name, unless something else has that name."""
        if name in self._module.members or name in shadowed:
            return f'{self._import_module(module)}.{name}'
        if module != 'builtins':
            self._imports.add(f'from {module} import {name}')
        return name

    def _type_name(self, qualified: str, shadowed: frozenset[str]) -> str:
        if qualified == NONE:
            return NONE

        module, rest = self._names.split_module(qualified)
        if module == 'typing':
            source = 'typing_extensions' if rest == 'Self' else 'typing'
            return self._short(source, rest, shadowed)
        if module == 'builtins':
            return self._short('builtins', rest, shadowed)

        if module == self._name:
            if rest.split('.')[0] in shadowed:
                # A class attribute hides the module-level class of the same name.
                return f'{self._import_module(module)}.{rest}'
            return rest
        return f'{self._import_module(module)}.{rest}'

    def _type(self, type_: str, shadowed: frozenset[str] = frozenset()) -> str:
        return TYPE_NAME.sub(lambda match: self._type_name(match.group(0), shadowed), type_)

    def _value_type(self, value: ir.Value, shadowed: frozenset[str]) -> str:
        accepted = self._names.accept(value.type)
        return self._type(accepted or 'typing.Any', shadowed)

    def _params(
        self, params: tuple[Param, ...], has_receiver: bool, shadowed: frozenset[str],
    ) -> str:
        parts: list[str] = []
        keyword_only_open = False

        for index, param in enumerate(params):
            if param.kind == KEYWORD_ONLY and not keyword_only_open:
                parts.append('*')
            keyword_only_open = keyword_only_open or param.kind in (KEYWORD_ONLY, VAR_POSITIONAL)

            prefix = {VAR_POSITIONAL: '*', VAR_KEYWORD: '**'}.get(param.kind, '')
            text = f'{prefix}{param.name}'
            if not (has_receiver and index == 0):
                text += f': {self._type(param.type, shadowed)}'
            if param.has_default:
                text += ' = ...'
            parts.append(text)

            is_last_positional_only = param.kind == POSITIONAL_ONLY and (
                index + 1 == len(params) or params[index + 1].kind != POSITIONAL_ONLY
            )
            if is_last_positional_only:
                parts.append('/')

        return ', '.join(parts)

    def _function(
        self,
        name: str,
        path: str,
        doc: str | None,
        binding: str | None,
        indent: str,
        shadowed: frozenset[str],
    ) -> list[str]:
        signatures = self._context.resolved[path]
        override = self._context.overrides.functions.get(path)
        if override:
            binding = override.binding
            doc = override.doc or doc

        # A method stored without `self` cannot be called on an instance as written.
        if binding == 'instance' and not signatures[0].params:
            binding = 'static'

        lines: list[str] = []
        for signature in signatures:
            if len(signatures) > 1:
                self._imports.add('from typing import overload')
                lines.append(f'{indent}@overload')
            if binding in DECORATORS:
                lines.append(f'{indent}{DECORATORS[binding]}')

            has_receiver = binding in ('instance', 'class', 'new')
            params = self._params(signature.params, has_receiver, shadowed)
            returns = self._type(signature.returns, shadowed)
            header = f'{indent}def {name}({params}) -> {returns}:'

            body = docstring(doc, indent + INDENT)
            lines += [header, *body] if body else [f'{header} ...']
        return lines

    def _property(
        self, name: str, path: str, prop: ir.Property, indent: str, shadowed: frozenset[str],
    ) -> list[str]:
        returns = self._type(self._context.resolved[path][0].returns, shadowed)
        if prop.getter is None:
            # A C descriptor: nothing says whether it can be assigned.
            return [f'{indent}{name}: {returns}']

        doc = prop.doc or prop.getter.doc
        body = docstring(doc, indent + INDENT)
        header = f'{indent}def {name}(self) -> {returns}:'
        lines = [f'{indent}@property', *([header, *body] if body else [f'{header} ...'])]

        if prop.settable:
            lines += [
                f'{indent}@{name}.setter',
                f'{indent}def {name}(self, value: {returns}) -> None: ...',
            ]
        return lines

    def _bases(self, cls: ir.Class) -> list[str]:
        bases = []
        for raw in cls.bases:
            accepted = self._names.accept(raw)
            if accepted and accepted != 'builtins.object':
                bases.append(self._type(accepted))
        return bases

    def _class(self, name: str, cls: ir.Class, path: str, indent: str) -> list[str]:
        inner = indent + INDENT
        shadowed = frozenset(cls.members)

        bases = self._bases(cls)
        header = f'{indent}class {name}({", ".join(bases)}):' if bases else f'{indent}class {name}:'
        # C code can derive from a type that refuses Python subclasses, so the
        # flag alone is not enough: no class in the dump may derive from it.
        if cls.final and not self._names.has_subclass(path):
            header = f'{indent}@{self._short("typing", "final", frozenset())}\n{header}'
        body = docstring(cls.doc, inner)

        nested: list[str] = []
        values: list[str] = []
        functions: list[str] = []
        deleted = self._context.overrides.deleted

        members = dict(cls.members)
        for added in self._added(path):
            members.setdefault(added, None)

        for member_name, member in sorted(members.items()):
            member_path = f'{path}.{member_name}'
            if member_path in deleted or _is_private(member_name):
                continue

            if member is None:
                functions += self._function(
                    member_name, member_path, None, 'instance', inner, shadowed,
                )
            elif isinstance(member, ir.Class):
                nested += self._class(member_name, member, member_path, inner)
            elif isinstance(member, ir.Function):
                is_overridden = member_path in self._context.overrides.functions
                is_python_new = member_name == '__new__' and member.descriptor == PYTHON_FUNCTION
                if member_name in SKIPPED_DUNDERS and not (is_overridden or is_python_new):
                    continue
                # `__new__` takes the class first and needs no decorator.
                binding = 'new' if member_name == '__new__' else member.binding
                functions += self._function(
                    member_name, member_path, member.doc, binding, inner, shadowed,
                )
            elif isinstance(member, ir.Property):
                functions += self._property(member_name, member_path, member, inner, shadowed)
            elif isinstance(member, ir.Value) and not _is_dunder(member_name):
                values.append(f'{inner}{member_name}: {self._value_type(member, shadowed)}')

        new = cls.members.get('__new__')
        is_c_new = isinstance(new, ir.Function) and new.descriptor != PYTHON_FUNCTION
        if is_c_new and '__init__' not in cls.members:
            # The C constructor says nothing about its arguments; without this
            # line a checker would allow none at all.
            any_ = self._type('typing.Any', shadowed)
            arguments = f'cls, *args: {any_}, **kwargs: {any_}'
            # Not `Self`: mypy rejects it as the return of `__new__` in a final class.
            returns = self._type(path, shadowed)
            functions.append(f'{inner}def __new__({arguments}) -> {returns}: ...')

        content = body + nested + values + functions
        if not content:
            return [f'{header} ...']
        return [header, *content]

    def _added(self, container: str) -> list[str]:
        """Names that overrides add to `container` and the dump does not have."""
        prefix = f'{container}.'
        return sorted(
            path[len(prefix):] for path in self._context.overrides.functions
            if path.startswith(prefix) and '.' not in path[len(prefix):]
            and self._names.find(path)[1] is None
        )

    def _classes_in_order(self) -> list[tuple[str, ir.Class]]:
        """Classes sorted by name, each after the local classes it derives from."""
        classes = {
            name: member for name, member in self._module.members.items()
            if isinstance(member, ir.Class)
        }
        ordered: list[tuple[str, ir.Class]] = []
        placed: set[str] = set()

        def place(name: str) -> None:
            if name in placed:
                return
            placed.add(name)
            for raw in classes[name].bases:
                public = self._names.accept(raw) or ''
                module, _, base = public.rpartition('.')
                if module == self._name and base in classes:
                    place(base)
            ordered.append((name, classes[name]))

        for name in sorted(classes):
            place(name)
        return ordered

    def _reexport(self, name: str, alias: ir.Alias) -> str | None:
        """A line that makes an object defined elsewhere visible under `name`, if it can be."""
        if alias.is_module:
            # Only `x as x` re-exports from a stub. A module imported under another
            # name (`import nuke_internal as nuke`) is the module's own business.
            parent, _, last = alias.target.rpartition('.')
            if alias.target not in self._context.dump.modules or last != name:
                return None
            if parent == self._name:
                return f'from . import {name} as {name}'
            if parent:
                return f'from {parent} import {name} as {name}'
            return f'import {name} as {name}'

        path, member = self._names.find(alias.target)
        if member is None:
            return None

        module, rest = self._names.split_module(path)
        if module == self._name:
            return f'{name} = {rest}'
        if rest == name:
            return f'from {module} import {name} as {name}'
        # Only `x as x` re-exports from a stub, so another name needs an assignment.
        return f'{name} = {self._import_module(module)}.{rest}'

    # === PUBLIC === #

    def emit(self, header: str) -> str:
        deleted = self._context.overrides.deleted
        reexports: list[str] = []
        local_aliases: list[str] = []
        values: list[str] = []
        functions: list[str] = []

        members: dict[str, ir.Member | None] = dict(self._module.members)
        for added in self._added(self._name):
            members.setdefault(added, None)

        for name, member in sorted(members.items()):
            path = f'{self._name}.{name}'
            if path in deleted or _is_private(name):
                continue

            if member is None:
                functions += self._function(name, path, None, None, '', frozenset()) + ['']
            elif isinstance(member, ir.Alias):
                line = self._reexport(name, member)
                if line and ' = ' in line:
                    local_aliases.append(line)
                elif line:
                    reexports.append(line)
            elif isinstance(member, ir.Function):
                functions += self._function(name, path, member.doc, None, '', frozenset()) + ['']
            elif isinstance(member, ir.Value) and not member.type.startswith('__future__.'):
                # `from __future__ import annotations` leaves a module attribute behind.
                values.append(f'{name}: {self._value_type(member, frozenset())}')

        classes: list[str] = []
        for name, cls in self._classes_in_order():
            path = f'{self._name}.{name}'
            if path not in deleted:
                classes += self._class(name, cls, path, '') + ['']

        sections = [
            [header],
            docstring(self._module.doc, ''),
            sorted(self._imports) + sorted(reexports),
            values,
            classes,
            functions,
            local_aliases,
        ]
        text = '\n\n'.join('\n'.join(section).rstrip() for section in sections if section)
        return text + '\n'


def module_file(name: str, modules: dict[str, ir.Module]) -> Path:
    """Stub path for module `name`. A top-level module or one with submodules is a package."""
    parts = name.split('.')
    has_children = any(other.startswith(f'{name}.') for other in modules)
    if has_children or len(parts) == 1:
        return Path(*parts) / '__init__.pyi'
    return Path(*parts).with_suffix('.pyi')


def normalize_version(raw: str) -> str:
    """Make a host version valid for PEP 440: `15.2v9` becomes `15.2.9`."""
    return '.'.join(re.findall(r'\d+', raw))


def package(context: Context, host: HostConfig, stubs: Path, out: Path) -> Path:
    """Lay the stub tree out as a PEP 561 stub-only distribution under `out`."""
    dump = context.dump
    if dump.host_version not in host.stub_revisions:
        raise KeyError(f'No stub revision for {dump.host} {dump.host_version} in the host config')

    packages = []
    for top in sorted(path for path in stubs.iterdir() if path.is_dir()):
        target = out / f'{top.name}-stubs'
        shutil.copytree(top, target)
        (target / 'py.typed').write_text('', encoding='utf-8')
        packages.append(target.name)

    qt = dump.qt
    dependencies = [qt.binding] if qt and qt.binding in TYPED_QT_BINDINGS else []
    revision = host.stub_revisions[dump.host_version]
    python = '.'.join(dump.python.split('.')[:2])

    (out / 'pyproject.toml').write_text(f'''[project]
name = "{host.package_name}"
version = "{normalize_version(dump.host_version)}.{revision}"
description = "Type stubs for {dump.host} {dump.host_version}"
license = "MIT"
requires-python = ">={python}"
dependencies = {json.dumps(dependencies)}
classifiers = ["Typing :: Stubs Only"]

[tool.hoststubs]
host = "{dump.host}"
host-version = "{dump.host_version}"
stub-revision = {revision}

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = {json.dumps(packages)}
''', encoding='utf-8')
    return out


def emit(context: Context, out: Path) -> list[Path]:
    """Write every module of the dump under `out` and return the files written."""
    dump = context.dump
    header = f'# Type stubs for {dump.host} {dump.host_version}. Generated; do not edit.'

    written = []
    for name, module in sorted(dump.modules.items()):
        path = out / module_file(name, dump.modules)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(ModuleEmitter(name, module, context).emit(header), encoding='utf-8')
        written.append(path)
    return written
