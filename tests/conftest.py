from __future__ import annotations

from pathlib import Path

import pytest

from hoststubs import ir
from hoststubs.names import Names

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
