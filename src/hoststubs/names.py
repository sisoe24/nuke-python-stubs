"""Resolve a type name to the fully qualified name the stubs may use.

Every track writes types as fully qualified names (`list[nuke.Node]`,
`typing.Any`); the emitter turns them into imports. A name is accepted only
if it resolves to a class in the dump, a builtin, a `typing` construct, a
standard-library type, or a Qt binding that ships type information.
Everything else is rejected, and the caller falls back to `Any`.
"""
from __future__ import annotations

import sys
import types
import typing
import builtins
import importlib

from hoststubs import ir

# Qt bindings whose installed package carries type information.
TYPED_QT_BINDINGS = frozenset({'PySide6'})
QT_BINDINGS = frozenset({'PySide6', 'PySide2', 'PyQt6', 'PyQt5'})

# Names pyright prints without an import.
BARE_TYPING_NAMES = frozenset({
    'Any', 'Callable', 'Generator', 'Iterator', 'Iterable', 'Self', 'NoReturn', 'Never',
    'Sequence', 'Mapping', 'Coroutine', 'Awaitable', 'AsyncGenerator', 'Literal',
})

MAX_ALIAS_HOPS = 10

INTERPRETER_TYPES = frozenset(
    value.__name__ for module in (builtins, types) for value in vars(module).values()
    if isinstance(value, type)
)


def _stdlib_type(qualified: str) -> bool:
    parts = qualified.split('.')
    for split in range(len(parts) - 1, 0, -1):
        try:
            found = importlib.import_module('.'.join(parts[:split]))
        except ImportError:
            continue
        for attribute in parts[split:]:
            found = getattr(found, attribute, None)
        return isinstance(found, type)
    return False


class Names:
    def __init__(self, dump: ir.Dump) -> None:
        self._dump = dump

        # Public path of every class, also reachable by its runtime `__module__.__qualname__`.
        self._classes: dict[str, str] = {}
        # Public path of a class -> its bases as the runtime names them.
        self._bases: dict[str, tuple[str, ...]] = {}
        for name, module in dump.modules.items():
            self._index(module.members, name)

    # === PRIVATE === #

    def _index(self, members: dict[str, ir.Member], prefix: str) -> None:
        for name, member in members.items():
            if not isinstance(member, ir.Class):
                continue

            path = f'{prefix}.{name}'
            self._classes[path] = path
            self._bases[path] = member.bases

            # Host classes can report `builtins` as their module. A real interpreter
            # type (`NoneType`, re-exported by `from types import *`) must not be
            # found under that name, or every None value would get that class.
            is_host_class = member.origin != 'builtins' or member.qualname not in INTERPRETER_TYPES
            if is_host_class:
                self._classes.setdefault(f'{member.origin}.{member.qualname}', path)
            self._index(member.members, path)

    def _follow_alias(self, qualified: str) -> str | None:
        """Rewrite `module.name.rest` to `target.rest` when `name` is an alias in `module`."""
        parts = qualified.split('.')
        for split in range(len(parts) - 1, 0, -1):
            module = self._dump.modules.get('.'.join(parts[:split]))
            if module is None:
                continue

            member = module.members.get(parts[split])
            if isinstance(member, ir.Alias):
                return '.'.join([member.target, *parts[split + 1:]])
            return None
        return None

    def _member(self, path: str) -> ir.Member | None:
        parts = path.split('.')
        for split in range(len(parts) - 1, 0, -1):
            module = self._dump.modules.get('.'.join(parts[:split]))
            if module is None:
                continue

            member = module.members.get(parts[split])
            for name in parts[split + 1:]:
                member = member.members.get(name) if isinstance(member, ir.Class) else None
            return member
        return None

    def _in_scope(self, head: str, module: str) -> str | None:
        """Qualified name that `head` means inside `module`, from the runtime namespace."""
        scope = self._dump.modules.get(module)
        member = scope.members.get(head) if scope else None

        if isinstance(member, ir.Class):
            return f'{module}.{head}'
        if isinstance(member, ir.Alias):
            return member.target
        if member is not None:
            return None

        if isinstance(getattr(builtins, head, None), type):
            return f'builtins.{head}'
        if head in BARE_TYPING_NAMES:
            return f'typing.{head}'
        return None

    # === PUBLIC === #

    def find(self, path: str) -> tuple[str, ir.Member | None]:
        """Follow aliases from `path` to the place where the object is recorded."""
        for _ in range(MAX_ALIAS_HOPS):
            member = self._member(path)
            if not isinstance(member, ir.Alias) or member.is_module:
                return path, member
            path = member.target
        return path, None

    def split_module(self, qualified: str) -> tuple[str, str]:
        """Split an accepted type name into the module to import and the name inside it."""
        parts = qualified.split('.')
        if parts[0] in ('builtins', 'typing'):
            return parts[0], '.'.join(parts[1:])

        for split in range(len(parts) - 1, 0, -1):
            if '.'.join(parts[:split]) in self._dump.modules:
                return '.'.join(parts[:split]), '.'.join(parts[split:])

        if parts[0] in QT_BINDINGS:
            return '.'.join(parts[:2]), '.'.join(parts[2:])

        for split in range(len(parts) - 1, 0, -1):
            try:
                importlib.import_module('.'.join(parts[:split]))
            except ImportError:
                continue
            return '.'.join(parts[:split]), '.'.join(parts[split:])
        raise ValueError(f'{qualified} is not in a known module')

    def is_class(self, path: str) -> bool:
        return self._classes.get(path) == path

    def has_subclass(self, path: str) -> bool:
        """True when a class in the dump derives from the class at public `path`."""
        return any(
            self._classes.get(base) == path
            for bases in self._bases.values() for base in bases
        )

    def ancestors(self, path: str) -> list[str]:
        """The class at public `path`, then its base classes in the dump, nearest first."""
        found = [path]
        for current in found:
            for base in self._bases.get(current, ()):
                public = self._classes.get(base)
                if public and public not in found:
                    found.append(public)
        return found

    def common_base(self, paths: list[str]) -> str | None:
        """Nearest dump class that every class in `paths` is or derives from."""
        others = [set(self.ancestors(path)) for path in paths[1:]]
        for candidate in self.ancestors(paths[0]):
            if all(candidate in ancestors for ancestors in others):
                return candidate
        return None

    def accept(self, qualified: str) -> str | None:
        """Return the name to emit for a fully qualified type name, or None to reject it."""
        for _ in range(MAX_ALIAS_HOPS):
            if qualified in self._classes:
                return self._classes[qualified]

            target = self._follow_alias(qualified)
            if target is None:
                break
            qualified = target

        top, _, rest = qualified.partition('.')
        if top == 'builtins':
            return qualified if isinstance(getattr(builtins, rest, None), type) else None
        if top == 'typing':
            # The fixed set keeps the answer independent of the Python that runs the build.
            is_public = not rest.startswith('_') and hasattr(typing, rest)
            return qualified if rest in BARE_TYPING_NAMES or is_public else None
        if top in QT_BINDINGS:
            qt = self._dump.qt
            is_typed = qt is not None and qt.binding == top and top in TYPED_QT_BINDINGS
            return qualified if is_typed else None
        if top in sys.stdlib_module_names:
            return qualified if _stdlib_type(qualified) else None
        return None

    def resolve(self, dotted: str, module: str) -> str | None:
        """Return the name to emit for `dotted` as written inside `module`, or None."""
        head, _, rest = dotted.partition('.')

        base = self._in_scope(head, module)
        if base is None:
            return None
        return self.accept(f'{base}.{rest}' if rest else base)
