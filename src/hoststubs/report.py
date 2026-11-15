"""Count how many return values and parameters each evidence source resolved."""
from __future__ import annotations

from pathlib import Path
from collections import Counter

from hoststubs import ir
from hoststubs.host import HOSTS, load_host
from hoststubs.names import Names
from hoststubs.infer import inference_dir
from hoststubs.params import load_params
from hoststubs.resolve import (Observed, ProbedParams, Resolver, Signature,
                               resolve_functions)
from hoststubs.emit import Context
from hoststubs.overrides import Overrides, load_overrides
from hoststubs.observations import load_observations
from hoststubs.inference import load_inference
from hoststubs.docstrings import VAR_KEYWORD, VAR_POSITIONAL

PYTHON_FUNCTION = 'builtins.function'
PROBES = HOSTS.parent / 'probes'


def load_context(
    dump_path: Path, use_overrides: bool = True, use_probe: bool = True,
) -> Context:
    """Load every input for one host version and resolve all signatures."""
    dump = ir.load(dump_path)
    names = Names(dump)
    host = load_host(dump.host)
    inferred = load_inference(inference_dir(dump), names)
    # One file per session kind: `nuke-15.2v9.json`, `nuke-15.2v9.hiero.json`.
    observed: dict[str, Observed] = {}
    probed: dict[str, ProbedParams] = {}
    probes = sorted(PROBES.glob(f'{dump.host}-{dump.host_version}*.json')) if use_probe else []
    for probe in probes:
        if probe.name.endswith('.params.json'):
            probed.update(load_params(probe, names, host.probe_messages))
        else:
            observed.update(load_observations(probe, names))
    resolver = Resolver(dump, names, host.type_names, inferred, observed, probed)

    overrides = Overrides({}, {})
    if use_overrides:
        overrides = load_overrides(HOSTS / dump.host / 'overrides', dump, names)

    overridden = {path: override.signatures for path, override in overrides.functions.items()}
    resolved = resolve_functions(resolver, dump, overridden, set(overrides.deleted))
    return Context(dump, names, resolved, overrides)


def resolve_dump(
    dump_path: Path, use_overrides: bool = True, use_probe: bool = True,
) -> tuple[ir.Dump, dict[str, tuple[Signature, ...]]]:
    context = load_context(dump_path, use_overrides, use_probe)
    return context.dump, context.resolved


def _groups(dump: ir.Dump) -> dict[str, str]:
    """Map each function path to a group such as 'nuke C' or 'hiero Python'."""
    groups: dict[str, str] = {}

    def visit(members: dict[str, ir.Member], prefix: str) -> None:
        for name, member in members.items():
            path = f'{prefix}.{name}'
            if isinstance(member, ir.Class):
                visit(member.members, path)
                continue

            if isinstance(member, ir.Property) and member.getter is None:
                groups[path] = f'{path.split(".")[0]} C property'
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
