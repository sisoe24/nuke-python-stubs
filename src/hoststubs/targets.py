"""Choose what the in-host probe may call."""
from __future__ import annotations

import re

from hoststubs import ir
from hoststubs.host import HostConfig
from hoststubs.resolve import Signature
from hoststubs.docstrings import VAR_KEYWORD, VAR_POSITIONAL

PYTHON_FUNCTION = 'builtins.function'
WORDS = re.compile(r'[A-Z]+(?![a-z])|[A-Z]?[a-z]+|\d+')


def name_words(name: str) -> set[str]:
    """Split `scriptSaveAs` or `clear_cache` into lowercase words."""
    return {word.lower() for word in WORDS.findall(name)}


def is_skipped(path: str, name: str, host: HostConfig) -> bool:
    if name == '__del__':
        return True
    if any(path == skipped or path.startswith(f'{skipped}.') for skipped in host.probe_skip):
        return True
    return bool(name_words(name) & host.probe_skip_words)


def _takes_no_arguments(signature: Signature) -> bool:
    """True when the function can be called with no arguments, or when nothing is known."""
    required = [
        param for index, param in enumerate(signature.params)
        if not param.has_default
        and param.kind not in (VAR_POSITIONAL, VAR_KEYWORD)
        and not (index == 0 and param.name in ('self', 'cls'))
    ]
    return not required


def _target(path: str, owner: str, name: str, kind: str, on: str) -> dict[str, str]:
    return {'path': path, 'owner': owner, 'name': name, 'kind': kind, 'on': on}


def probe_targets(
    dump: ir.Dump, resolved: dict[str, tuple[Signature, ...]], host: HostConfig,
) -> list[dict[str, str]]:
    """List C functions callable without arguments and C properties, methods first.

    Python functions are left out: pyright reads their source, and calling
    them has more side effects than calling a C getter.
    """
    targets: list[dict[str, str]] = []

    def visit(members: dict[str, ir.Member], owner: str, in_class: bool) -> None:
        for name, member in sorted(members.items()):
            path = f'{owner}.{name}'
            if isinstance(member, ir.Class):
                visit(member.members, path, in_class=True)
                continue

            is_dunder = name.startswith('__') and name.endswith('__')
            if is_dunder or is_skipped(path, name, host):
                continue

            if isinstance(member, ir.Property) and member.getter is None and in_class:
                targets.append(_target(path, owner, name, 'property', 'instance'))
            elif isinstance(member, ir.Function) and member.descriptor != PYTHON_FUNCTION:
                if not any(_takes_no_arguments(signature) for signature in resolved[path]):
                    continue
                on = 'instance' if in_class and member.binding == 'instance' else 'owner'
                targets.append(_target(path, owner, name, 'function', on))

    for module_name, module in dump.modules.items():
        visit(module.members, module_name, in_class=False)

    # Methods run on the scene as built; module functions may change it.
    return sorted(targets, key=lambda target: (target['on'] == 'owner', target['path']))
