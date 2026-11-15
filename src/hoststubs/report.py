"""Count how many return values and parameters each evidence source resolved."""
from __future__ import annotations

from pathlib import Path
from collections import Counter

from hoststubs import ir
from hoststubs.host import HOSTS, load_host
from hoststubs.names import Names
from hoststubs.infer import inference_dir
from hoststubs.resolve import Resolver, Signature, resolve_functions
from hoststubs.overrides import load_overrides
from hoststubs.inference import load_inference
from hoststubs.docstrings import VAR_KEYWORD, VAR_POSITIONAL

PYTHON_FUNCTION = 'builtins.function'


def resolve_dump(
    dump_path: Path, use_overrides: bool = True,
) -> tuple[ir.Dump, dict[str, tuple[Signature, ...]]]:
    dump = ir.load(dump_path)
    names = Names(dump)
    host = load_host(dump.host)
    inferred = load_inference(inference_dir(dump), names)
    resolver = Resolver(dump, names, host.type_names, inferred)

    if not use_overrides:
        return dump, resolve_functions(resolver, dump, {}, set())

    overrides = load_overrides(HOSTS / dump.host / 'overrides', dump, names)
    overridden = {path: override.signatures for path, override in overrides.functions.items()}
    return dump, resolve_functions(resolver, dump, overridden, set(overrides.deleted))


def _groups(dump: ir.Dump) -> dict[str, str]:
    """Map each function path to a group such as 'nuke C' or 'hiero Python'."""
    groups: dict[str, str] = {}

    def visit(members: dict[str, ir.Member], prefix: str) -> None:
        for name, member in members.items():
            path = f'{prefix}.{name}'
            if isinstance(member, ir.Class):
                visit(member.members, path)
                continue

            function = member.getter if isinstance(member, ir.Property) else member
            if not isinstance(function, ir.Function):
                continue

            if function.descriptor == PYTHON_FUNCTION:
                kind = 'Python'
            elif name.startswith('__') and name.endswith('__'):
                kind = 'C dunder'
            else:
                kind = 'C'
            groups[path] = f'{path.split(".")[0]} {kind}'

    for module_name, module in dump.modules.items():
        visit(module.members, module_name)
    return groups


def _shares(counter: Counter[str]) -> str:
    total = sum(counter.values())
    parts = [f'{source} {count} ({count / total:.0%})' for source, count in counter.most_common()]
    return f'{total}: ' + ', '.join(parts)


def report(dump_path: Path) -> str:
    dump, resolved = resolve_dump(dump_path)
    groups = _groups(dump)

    returns: dict[str, Counter[str]] = {}
    params: dict[str, Counter[str]] = {}

    for path, signatures in resolved.items():
        # A function that an override adds has no dump entry to classify.
        group = groups.get(path, f'{path.split(".")[0]} added')
        signature = signatures[0]
        returns.setdefault(group, Counter())[signature.returns_source] += 1

        for index, param in enumerate(signature.params):
            is_receiver = index == 0 and param.name in ('self', 'cls')
            if not is_receiver and param.kind not in (VAR_POSITIONAL, VAR_KEYWORD):
                params.setdefault(group, Counter())[param.source] += 1

    lines = [f'{dump.host} {dump.host_version}: share resolved per source']
    for group in sorted(returns):
        lines.append(f'{group}')
        lines.append(f'  returns {_shares(returns[group])}')
        if group in params:
            lines.append(f'  params  {_shares(params[group])}')
    return '\n'.join(lines)
