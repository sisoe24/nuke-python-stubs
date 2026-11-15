from __future__ import annotations

from pathlib import Path

import pytest

from hoststubs.gate import check_corpus, check_names, check_syntax, write_snapshot
from hoststubs.host import REPO
from hoststubs.build import build


def test_syntax_error_is_a_finding(tmp_path: Path) -> None:
    """A stub that does not parse is reported with its file and line."""
    (tmp_path / 'broken.pyi').write_text('def f(:\n')
    [finding] = check_syntax(tmp_path)
    assert finding.startswith(f'{tmp_path / "broken.pyi"}:1:')


def test_undefined_name_is_a_finding(tmp_path: Path) -> None:
    """A stub that names a type it does not define or import is reported."""
    (tmp_path / 'module.pyi').write_text('def f() -> Node: ...\n')
    [finding] = check_names(tmp_path)
    assert 'F821' in finding


def test_clean_stub_has_no_findings(tmp_path: Path) -> None:
    """A valid stub passes both checks."""
    (tmp_path / 'module.pyi').write_text('class Node: ...\ndef f() -> Node: ...\n')
    assert check_syntax(tmp_path) == []
    assert check_names(tmp_path) == []


def test_corpus_change_is_a_finding(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """A revealed type that differs from the snapshot, or falls back to Any, fails."""
    monkeypatch.setattr('hoststubs.gate.SNAPSHOTS', tmp_path)
    write_snapshot({'use.py': {'revealed': {'nuke.root()': 'Root'}, 'errors': {}}}, 'nuke', '1')

    same = {'use.py': {'revealed': {'nuke.root()': 'Root'}, 'errors': {}}}
    fallen_back = {'use.py': {'revealed': {'nuke.root()': 'Any'}, 'errors': {}}}
    assert check_corpus(same, 'nuke', '1') == []

    [finding] = check_corpus(fallen_back, 'nuke', '1')
    assert 'expected Root' in finding
    assert 'got      Any' in finding


def test_missing_error_is_a_finding(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """A line that is wrong on purpose must keep being reported."""
    monkeypatch.setattr('hoststubs.gate.SNAPSHOTS', tmp_path)
    expected = {'use.py': {'revealed': {}, 'errors': {'node.nope()': 'reportAttributeAccessIssue'}}}
    write_snapshot(expected, 'nuke', '1')

    [finding] = check_corpus({'use.py': {'revealed': {}, 'errors': {}}}, 'nuke', '1')
    assert 'node.nope()' in finding


@pytest.mark.parametrize('dump', sorted((REPO / 'dumps').glob('*.json')), ids=lambda path: path.stem)
def test_build_passes_the_gate(dump: Path, tmp_path: Path) -> None:
    """Every dumped version builds: stubs parse, names resolve, the corpus matches its snapshot."""
    assert build(dump, tmp_path / 'build') == []
