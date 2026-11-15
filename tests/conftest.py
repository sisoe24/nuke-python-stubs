from __future__ import annotations

from pathlib import Path

import pytest

from hoststubs import ir
from hoststubs.names import Names
from hoststubs.resolve import Signature
from hoststubs.report import resolve_dump

REPO = Path(__file__).parents[1]
FIXTURES = REPO / 'tests' / 'fixtures'


@pytest.fixture(scope='session')
def fixture_names() -> Names:
    return Names(ir.load(FIXTURES / 'dump.golden.json'))


@pytest.fixture(scope='session')
def nuke15_names() -> Names:
    """Nuke 15 uses PySide2, which ships no type information."""
    return Names(ir.load(REPO / 'dumps' / 'nuke-15.2v9.json'))


@pytest.fixture(scope='session')
def nuke17_names() -> Names:
    """Nuke 17 uses PySide6, which does."""
    return Names(ir.load(REPO / 'dumps' / 'nuke-17.1v2.json'))


@pytest.fixture(scope='session')
def nuke15_dump() -> ir.Dump:
    return ir.load(REPO / 'dumps' / 'nuke-15.2v9.json')


@pytest.fixture(scope='session')
def nuke15_resolved() -> dict[str, tuple[Signature, ...]]:
    return resolve_dump(REPO / 'dumps' / 'nuke-15.2v9.json')[1]


@pytest.fixture(scope='session')
def nuke15_derived() -> dict[str, tuple[Signature, ...]]:
    """What the evidence gives before any override is applied."""
    path = REPO / 'dumps' / 'nuke-15.2v9.json'
    return resolve_dump(path, use_overrides=False, use_probe=False)[1]


@pytest.fixture(scope='session')
def nuke15_probed() -> dict[str, tuple[Signature, ...]]:
    """Derived results with both probes, without overrides."""
    return resolve_dump(REPO / 'dumps' / 'nuke-15.2v9.json', use_overrides=False)[1]
