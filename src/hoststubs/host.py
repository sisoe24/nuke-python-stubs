"""Host configuration: everything that differs between host applications."""
from __future__ import annotations

import importlib.util
from pathlib import Path
from dataclasses import dataclass

REPO = Path(__file__).parents[2]
HOSTS = REPO / 'hosts'
DUMP_SCRIPT = REPO / 'inhost' / 'dump.py'


@dataclass(frozen=True)
class HostConfig:
    name: str

    # Dotted path to the host version string, read inside the host.
    version_attribute: str

    # Modules to dump, with their submodules. The first root that shows an
    # object from a private C module owns it, so order matters.
    roots: tuple[str, ...]
    skip: tuple[str, ...]

    # Command prefix that runs a Python script inside the host, by label.
    launchers: dict[str, tuple[str, ...]]

    # Raw host version -> stub revision. Bumped by hand when a package is published.
    stub_revisions: dict[str, int]


def load_host(name: str) -> HostConfig:
    path = HOSTS / name / 'config.py'
    if not path.is_file():
        raise FileNotFoundError(f'No host config at {path}')

    spec = importlib.util.spec_from_file_location(f'hosts.{name}.config', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.HOST


def dump_command(host: HostConfig, launcher: str, out: str) -> list[str]:
    return [
        *host.launchers[launcher],
        str(DUMP_SCRIPT),
        out,
        f'host={host.name}',
        f'version={host.version_attribute}',
        *(f'skip={module}' for module in host.skip),
        *host.roots,
    ]
