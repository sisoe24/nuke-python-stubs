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

    # Importable C modules that users reach only through a root.
    private: tuple[str, ...]

    # Type spellings in the host's docstrings that are not Python names.
    type_names: dict[str, str]

    # The probe calls nothing whose name contains one of these words
    # (`scriptSaveAs` contains `save`), and none of the listed paths.
    probe_skip_words: frozenset[str]
    probe_skip: frozenset[str]

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


def dump_arguments(host: HostConfig, out: str) -> list[str]:
    """Arguments for inhost/dump.py, after the script path."""
    return [
        out,
        f'host={host.name}',
        f'version={host.version_attribute}',
        *(f'skip={module}' for module in host.skip),
        *(f'private={module}' for module in host.private),
        *host.roots,
    ]
