"""Host configuration: everything that differs between host applications."""
from __future__ import annotations

import importlib
from pathlib import Path
from dataclasses import dataclass

REPO = Path(__file__).parents[2]
HOSTS = Path(__file__).parent / 'hosts'
DUMP_SCRIPT = Path(__file__).parent / 'inhost' / 'dump.py'


def data_dir(host: str, version: str) -> Path:
    return REPO / 'data' / host / version


@dataclass(frozen=True)
class HostConfig:
    name: str

    # Name of the stub distribution on PyPI.
    package_name: str

    # Dotted path to the host version string, read inside the host.
    version_attribute: str

    # Modules to dump, with their submodules. The first root that shows an
    # object from a private C module owns it, so order matters.
    roots: tuple[str, ...]
    skip: tuple[str, ...]

    # Private C module -> the public module that owns its objects.
    private: dict[str, str]

    # Type spellings in the host's docstrings that are not Python names.
    type_names: dict[str, str]

    # Error texts of the host's own argument checks, as (regex, type).
    probe_messages: tuple[tuple[str, str], ...]

    # The probe calls nothing whose name contains one of these words
    # (`scriptSaveAs` contains `save`), and nothing at or under the listed paths.
    probe_skip_words: frozenset[str]
    probe_skip: frozenset[str]

    # Raw host version -> stub revision. Bumped by hand when a package is published.
    stub_revisions: dict[str, int]

    # Host version whose stubs are committed in `stubs/`, for editors that read that directory.
    stub_tree_version: str


def load_host(name: str) -> HostConfig:
    if not (HOSTS / name / 'config.py').is_file():
        raise FileNotFoundError(f'No host config at {HOSTS / name / "config.py"}')

    return importlib.import_module(f'hoststubs.hosts.{name}.config').HOST


def dump_arguments(host: HostConfig, out: str) -> list[str]:
    """Arguments for hoststubs/inhost/dump.py, after the script path."""
    return [
        out,
        f'host={host.name}',
        f'version={host.version_attribute}',
        *(f'skip={module}' for module in host.skip),
        *(f'private={module}:{owner}' for module, owner in host.private.items()),
        *host.roots,
    ]
