from __future__ import annotations

import json
from pathlib import Path

import pytest

from hoststubs.names import Names
from hoststubs.resolve import ANY, Candidate, Signature
from hoststubs.host import data_dir
from hoststubs.report import resolve_dump
from hoststubs.observations import load_observations

Resolved = dict[str, tuple[Signature, ...]]


def _candidate(tmp_path: Path, names: Names, *observations: dict) -> Candidate | None:
    path = tmp_path / 'probe.json'
    path.write_text(json.dumps({'schema': 1, 'observations': {'target': list(observations)}}))
    observed = load_observations(path, names).get('target')
    return observed.candidate if observed else None


def _seen(type_: str, **details: object) -> dict:
    return {'type': type_, **details}


def test_none_is_discarded(tmp_path: Path, nuke15_names: Names) -> None:
    """None means nothing was set here, not that the function returns None."""
    assert _candidate(tmp_path, nuke15_names, _seen('builtins.NoneType')) is None

    mixed = _candidate(tmp_path, nuke15_names, _seen('builtins.NoneType'), _seen('builtins.str'))
    assert mixed == Candidate('builtins.str', 'probe')


def test_uniform_list_qualifies(tmp_path: Path, nuke15_names: Names) -> None:
    """Every element has one type: `list[Node]`. Runtime names resolve to public ones."""
    seen = _seen('builtins.list', elements=['builtins.Node'], length=3)
    assert _candidate(tmp_path, nuke15_names, seen) == Candidate('builtins.list[nuke.Node]', 'probe')


def test_empty_list_is_weak(tmp_path: Path, nuke15_names: Names) -> None:
    """An empty list says only that it is a list."""
    seen = _seen('builtins.list', elements=[], length=0)
    assert _candidate(tmp_path, nuke15_names, seen) == Candidate('builtins.list', 'probe_weak')


def test_mixed_elements_without_common_class_are_weak(tmp_path: Path, nuke15_names: Names) -> None:
    """`[1, 'a']` has no single element type."""
    seen = _seen('builtins.list', elements=['builtins.int', 'builtins.str'], length=2)
    assert _candidate(tmp_path, nuke15_names, seen) == Candidate('builtins.list', 'probe_weak')


def test_mixed_elements_with_common_base(tmp_path: Path, nuke15_names: Names) -> None:
    """Knob subclasses in one list share the base class Knob."""
    seen = _seen('builtins.list', elements=['builtins.WH_Knob', 'builtins.String_Knob'], length=2)
    assert _candidate(tmp_path, nuke15_names, seen) == Candidate('builtins.list[nuke.Knob]', 'probe')


def test_empty_observation_does_not_contradict(tmp_path: Path, nuke15_names: Names) -> None:
    """One receiver returned an empty list, another a list of nodes."""
    empty = _seen('builtins.list', elements=[], length=0)
    full = _seen('builtins.list', elements=['builtins.Node'], length=1)
    assert _candidate(tmp_path, nuke15_names, empty, full).type == 'builtins.list[nuke.Node]'


def test_tuple_and_dict(tmp_path: Path, nuke15_names: Names) -> None:
    """A tuple is variable-length; a dict needs uniform keys and values."""
    pair = _seen('builtins.tuple', elements=['builtins.float'], length=2)
    assert _candidate(tmp_path, nuke15_names, pair).type == 'builtins.tuple[builtins.float, ...]'

    knobs = _seen('builtins.dict', keys=['builtins.str'], values=['builtins.WH_Knob'], length=1)
    assert _candidate(tmp_path, nuke15_names, knobs).type == 'builtins.dict[builtins.str, nuke.WH_Knob]'


def test_receivers_that_disagree_give_nothing(tmp_path: Path, nuke15_names: Names) -> None:
    """float on one receiver and str on another: no candidate."""
    seen = [_seen('builtins.float'), _seen('builtins.str')]
    assert _candidate(tmp_path, nuke15_names, *seen) is None


def test_errors_are_ignored(tmp_path: Path, nuke15_names: Names) -> None:
    """A call that raised says nothing about the return type."""
    error = {'error': 'TypeError', 'message': 'needs an argument'}
    assert _candidate(tmp_path, nuke15_names, error) is None


def test_unknown_runtime_type_gives_nothing(tmp_path: Path, nuke15_names: Names) -> None:
    """A type the dump does not hold is not emitted."""
    assert _candidate(tmp_path, nuke15_names, _seen('_secret.Thing')) is None


def test_real_probe_knob_value_disagrees(nuke15_names: Names) -> None:
    """Knob.value() returns float, str, bool or a list by knob class: the base method stays Any."""
    observed = load_observations(data_dir('nuke', '15.2v9') / 'probe-nuke.json', nuke15_names)
    assert 'nuke.Knob.value' not in observed
    assert observed['nuke.Knob.name'].candidate == Candidate('builtins.str', 'probe')


@pytest.fixture(scope='module')
def probed() -> Resolved:
    """Derived results with the probe, without overrides."""
    path = data_dir('nuke', '15.2v9') / 'dump.json'
    return resolve_dump(path, use_overrides=False)[1]


@pytest.mark.parametrize(('path', 'returns', 'source'), [
    # The docstring says Node. The probe saw Root, which is a Node: the docstring stands.
    ('nuke.thisNode', 'nuke.Node', 'doc_signature'),
    ('nuke.activeGroup', 'nuke.Group', 'doc_signature'),
    # The docstring knows about None; the probe saw one Node.
    ('nuke.Group.selectedNode', 'nuke.Node | None', 'doc_signature'),
    # The docstring is wrong or vague; the probe contradicts or refines it.
    ('nuke.Node.pixelAspect', 'builtins.float', 'probe'),
    ('nuke.getNodeClassName', 'builtins.str', 'probe'),
    ('nuke.views', 'builtins.list[builtins.str]', 'probe'),
    ('nuke.allNodes', 'builtins.list[nuke.Node]', 'probe'),
    ('nuke.Node.knobs', 'builtins.dict[builtins.str, nuke.Knob]', 'probe'),
    # The docstring lists both classes the probe saw: it stays, unmerged.
    ('hiero.core.BinItem.activeItem', 'hiero.core.Clip | hiero.core.Sequence', 'doc_field'),
    # Docstring says Bin; a top-level bin returned the Project. Both are real.
    ('hiero.core.Bin.parentBin', 'hiero.core.Bin | hiero.core.Project', 'probe'),
    # The docstring names a builtin and the probe saw a host class: the docstring is wrong.
    ('hiero.core.AudioTrack.channel', 'hiero.core.AudioTrack.Channel', 'probe'),
    ('hiero.core.Bin.name', 'builtins.str', 'probe'),
])
def test_probe_against_docstring(probed: Resolved, path: str, returns: str, source: str) -> None:
    """The probe replaces a docstring type only where the observation contradicts or refines it."""
    [signature] = probed[path]
    assert (signature.returns, signature.returns_source) == (returns, source)


def test_observed_subclass_is_widened(probed: Resolved, nuke15_derived: Resolved) -> None:
    """Without a docstring type, an observed Root is emitted as Node: true in every scene."""
    assert nuke15_derived['nuke.root'][0].returns == ANY
    assert (probed['nuke.root'][0].returns, probed['nuke.root'][0].returns_source) == (
        'nuke.Node', 'probe',
    )
