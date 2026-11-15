from __future__ import annotations

import pytest

from hoststubs import ir
from hoststubs.host import load_host
from hoststubs.resolve import Signature
from hoststubs.targets import is_skipped, name_words, probe_targets

Resolved = dict[str, tuple[Signature, ...]]


@pytest.mark.parametrize(('name', 'words'), [
    ('scriptSaveAs', {'script', 'save', 'as'}),
    ('clearRAMCache', {'clear', 'ram', 'cache'}),
    ('nodeDelete', {'node', 'delete'}),
    ('autoplace_snap_all', {'autoplace', 'snap', 'all'}),
    ('isLoaded', {'is', 'loaded'}),
])
def test_name_words(name: str, words: set[str]) -> None:
    """Names split on case changes and underscores."""
    assert name_words(name) == words


@pytest.mark.parametrize('path', [
    'nuke.scriptSaveAs',        # save
    'nuke.scriptClear',         # clear
    'nuke.nodeDelete',          # delete
    'nuke.Node.writeKnobs',     # write
    'nuke.fork',                # fork
    'nuke.hotkeys',             # found by running: ends the session
    'nuke.Foo.__del__',
])
def test_skipped(path: str) -> None:
    """A risky word anywhere in the name, or a listed path, keeps the probe away."""
    assert is_skipped(path, path.rsplit('.', 1)[-1], load_host('nuke'))


@pytest.mark.parametrize('path', ['nuke.root', 'nuke.Node.name', 'nuke.Node.isLoaded'])
def test_not_skipped(path: str) -> None:
    """A word that only contains a risky word is not a match."""
    assert not is_skipped(path, path.rsplit('.', 1)[-1], load_host('nuke'))


def test_targets(nuke15_dump: ir.Dump, nuke15_derived: Resolved) -> None:
    """Only C functions callable without arguments and C properties; methods before functions."""
    targets = probe_targets(nuke15_dump, nuke15_derived, load_host('nuke'))
    by_path = {target['path']: target for target in targets}

    assert by_path['nuke.root']['on'] == 'owner'
    assert by_path['nuke.Node.name']['on'] == 'instance'
    assert by_path['nuke.allNodes']['kind'] == 'function'

    assert 'nuke.Node.knob' not in by_path            # needs an argument
    assert 'nuke.scriptClear' not in by_path          # skipped word
    assert 'nukescripts.misc.declone' not in by_path  # Python function

    kinds = [target['on'] for target in targets]
    assert kinds == sorted(kinds, key=lambda on: on == 'owner')
