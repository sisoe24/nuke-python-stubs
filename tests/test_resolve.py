from __future__ import annotations

import pytest

from hoststubs.resolve import ANY, SOURCES, Candidate, Signature, pick

Resolved = dict[str, tuple[Signature, ...]]


def _types(signature: Signature) -> dict[str, str]:
    return {param.name: param.type for param in signature.params}


def _optional(signature: Signature) -> list[str]:
    return [param.name for param in signature.params if param.has_default]


def test_priority_order() -> None:
    """The source order is fixed: override first, Any last."""
    assert SOURCES == (
        'override', 'probe', 'signature', 'doc_signature', 'doc_field', 'inference',
        'default', 'dunder', 'probe_weak', 'any',
    )


@pytest.mark.parametrize(('winner', 'loser'), [
    ('override', 'probe'),
    ('probe', 'doc_signature'),
    ('doc_signature', 'doc_field'),
    ('doc_field', 'inference'),
    ('dunder', 'probe_weak'),
])
def test_pick_takes_the_higher_source(winner: str, loser: str) -> None:
    """A candidate from an earlier source wins, whatever the order of arrival."""
    candidates = [Candidate('builtins.int', loser), Candidate('builtins.str', winner)]
    assert pick(candidates).source == winner
    assert pick(candidates[::-1]).source == winner


def test_pick_without_evidence_is_any() -> None:
    """No candidate, or only Any, resolves to Any."""
    assert pick([]) == Candidate(ANY, 'any')
    assert pick([Candidate(ANY, 'inference')]) == Candidate(ANY, 'any')


def test_signature_line_with_prose_return(nuke15_resolved: Resolved) -> None:
    """Node.knob: parameters come from the line; the prose return gives no type."""
    [signature] = nuke15_resolved['nuke.Node.knob']
    assert [param.name for param in signature.params] == ['self', 'p', 'follow_link']
    assert _optional(signature) == ['follow_link']
    assert signature.returns == ANY
    assert signature.shape_source == 'doc_signature'


def test_prose_return_is_any_not_none(nuke15_resolved: Resolved) -> None:
    """'root() -> node': unknown stays Any. The old generator wrote None here."""
    [signature] = nuke15_resolved['nuke.root']
    assert signature.returns == ANY


def test_signature_line_outranks_field(nuke15_resolved: Resolved) -> None:
    """toNode: the line says 'Node', the field 'Node or None'. The line has priority."""
    [signature] = nuke15_resolved['nuke.toNode']
    assert (signature.returns, signature.returns_source) == ('nuke.Node', 'doc_signature')


def test_typed_fields(nuke15_resolved: Resolved) -> None:
    """createNode: `:type:` fields give parameter types and mark optional ones."""
    [signature] = nuke15_resolved['nuke.createNode']
    assert _types(signature) == {
        'node': 'builtins.str', 'knobs': 'builtins.str', 'inpanel': 'builtins.bool',
    }
    assert _optional(signature) == ['knobs', 'inpanel']
    assert signature.returns == 'nuke.Node'


def test_documented_optional_params(nuke15_resolved: Resolved) -> None:
    """allNodes(filter, group): the fields say 'Optional', so `nuke.allNodes()` must be valid."""
    [signature] = nuke15_resolved['nuke.allNodes']
    assert _optional(signature) == ['filter', 'group', 'recurseGroups']
    assert signature.returns == 'builtins.list'


def test_overloads(nuke15_resolved: Resolved) -> None:
    """nuke.execute declares two signature lines."""
    first, second = nuke15_resolved['nuke.execute']
    assert 'start' in _types(first)
    assert 'frameRangeSet' in _types(second)
    assert first.returns == second.returns == 'None'
    assert _types(first)['continueOnError'] == 'builtins.bool'


def test_dunder_table(nuke15_resolved: Resolved) -> None:
    """Dunders without documentation get their return type from the rule table."""
    assert nuke15_resolved['nuke.Node.__len__'][0].returns == 'builtins.int'
    assert nuke15_resolved['nuke.Node.__len__'][0].returns_source == 'dunder'
    assert nuke15_resolved['nuke.Node.__getitem__'][0].returns == ANY


def test_cpp_types_are_rejected(nuke15_resolved: Resolved) -> None:
    """A pybind11 line: C++ types become Any, Python ones are kept."""
    [signature] = nuke15_resolved['nuke.GeoSelectionItem.getWorldPoints']
    assert signature.returns == ANY
    assert _types(signature)['time'] == 'builtins.float'


def test_docstring_name_is_a_public_path(nuke15_resolved: Resolved) -> None:
    """'@return: nuke.Node' in hiero.core is Nuke's Node, not hiero.core.nuke.Node."""
    [signature] = nuke15_resolved['hiero.core.Transition.dissolveNode']
    assert signature.returns == 'nuke.Node'


def test_inference_fills_python_functions(nuke15_resolved: Resolved) -> None:
    """A Python function without annotations gets pyright's inferred return."""
    [signature] = nuke15_resolved['nukescripts.toolsets.addToolsetsPanel']
    assert (signature.returns, signature.returns_source) == ('builtins.bool | None', 'inference')


def test_default_types(nuke15_resolved: Resolved) -> None:
    """A bool default types the parameter; an int default does not."""
    [signature] = nuke15_resolved['hiero.core.Clip.addToNukeScript']
    by_name = {param.name: param for param in signature.params}
    assert (by_name['trimmed'].type, by_name['trimmed'].source) == ('builtins.bool', 'default')

    [signature] = nuke15_resolved['hiero.core.EffectTrackItem.addToNukeScript']
    assert _types(signature)['offset'] == ANY
