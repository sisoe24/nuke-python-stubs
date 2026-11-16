from __future__ import annotations

from pathlib import Path

import pytest

from hoststubs import ir
from hoststubs.host import HOSTS, data_dir
from hoststubs.names import Names
from hoststubs.resolve import ANY, Signature
from hoststubs.overrides import OverrideError, Overrides, load_overrides

FIXTURE_DUMP = Path(__file__).parent / 'fixtures' / 'dump.golden.json'
Resolved = dict[str, tuple[Signature, ...]]


def _load(tmp_path: Path, module: str, text: str, names: Names) -> Overrides:
    (tmp_path / f'{module}.pyi').write_text(text, encoding='utf-8')
    return load_overrides(tmp_path, ir.load(FIXTURE_DUMP), names)


def test_def_replaces_a_function(tmp_path: Path, fixture_names: Names) -> None:
    """A def replaces the symbol outright, with every type from the override."""
    text = '# src: manual\ndef toNode(s: str) -> Node | None: ...\n'
    override = _load(tmp_path, 'fxhost', text, fixture_names).functions['fxhost.toNode']

    [signature] = override.signatures
    assert signature.returns == 'fxhost.Node | None'
    assert [(param.name, param.type, param.source) for param in signature.params] == [
        ('s', 'builtins.str', 'override'),
    ]
    assert override.provenance == 'manual'
    assert override.location.endswith('fxhost.pyi:2')


def test_method_and_review_provenance(tmp_path: Path, fixture_names: Names) -> None:
    """A def inside a class block overrides a method; `# src: review` is recorded."""
    text = (
        'class Node:\n'
        '    # src: review\n'
        '    def knob(self, p: str | int, follow_link: bool = ...) -> Knob | None: ...\n'
    )
    override = _load(tmp_path, 'fxhost', text, fixture_names).functions['fxhost.Node.knob']

    assert override.provenance == 'review'
    assert override.binding == 'instance'
    assert [param.has_default for param in override.signatures[0].params] == [False, False, True]


def test_overload_run_replaces_the_set(tmp_path: Path, fixture_names: Names) -> None:
    """Consecutive @overload defs become one overload set; one comment covers the run."""
    text = (
        '# src: manual\n'
        '@overload\n'
        'def root() -> Node: ...\n'
        '@overload\n'
        'def root(name: str) -> Node | None: ...\n'
    )
    override = _load(tmp_path, 'fxhost', text, fixture_names).functions['fxhost.root']
    assert [signature.returns for signature in override.signatures] == [
        'fxhost.Node', 'fxhost.Node | None',
    ]


def test_def_for_unknown_name_adds_it(tmp_path: Path, fixture_names: Names) -> None:
    """A def for a name that is not in the dump adds the symbol."""
    text = '# src: manual\ndef brandNew(count: int) -> list[Node]: ...\n'
    functions = _load(tmp_path, 'fxhost', text, fixture_names).functions
    assert functions['fxhost.brandNew'].signatures[0].returns == 'builtins.list[fxhost.Node]'


def test_delete(tmp_path: Path, fixture_names: Names) -> None:
    """`# delete:` on its own line removes a symbol."""
    text = '# src: manual\n# delete: fxhost.Node.name\n'
    deleted = _load(tmp_path, 'fxhost', text, fixture_names).deleted
    assert list(deleted) == ['fxhost.Node.name']


def test_reexport_is_keyed_by_recorded_path(tmp_path: Path, fixture_names: Names) -> None:
    """An override written against a re-export lands on the path the dump records."""
    text = '# src: manual\ndef frame_range(first: int, last: int, step: int = ...) -> list[int]: ...\n'
    functions = _load(tmp_path, 'fxhost', text, fixture_names).functions
    assert list(functions) == ['fxhost.utils.frame_range']


def test_explicit_any_is_allowed(tmp_path: Path, fixture_names: Names) -> None:
    """`Any` is a valid hand-written answer, also inside a container."""
    text = '# src: manual\ndef root(options: dict[str, Any] = ...) -> Any: ...\n'
    [signature] = _load(tmp_path, 'fxhost', text, fixture_names).functions['fxhost.root'].signatures
    assert signature.returns == ANY
    assert signature.params[0].type == 'builtins.dict[builtins.str, typing.Any]'


def test_qt_type_without_typed_binding_is_any(tmp_path: Path, fixture_names: Names) -> None:
    """`QtGui.QImage` means the host's binding. The fixture host uses PySide2, so it is Any."""
    text = '# src: manual\ndef root() -> QtGui.QImage: ...\n'
    [signature] = _load(tmp_path, 'fxhost', text, fixture_names).functions['fxhost.root'].signatures
    assert signature.returns == ANY


@pytest.mark.parametrize(('text', 'message'), [
    ('def root() -> Node: ...\n', r'fxhost\.pyi:1: missing "# src: manual"'),
    ('# src: manual\ndef root() -> Nod: ...\n', r"fxhost\.pyi:2: type 'Nod' does not resolve"),
    # A typo inside a container must not turn into Any.
    ('# src: manual\ndef root() -> list[Nod]: ...\n', r"fxhost\.pyi:2: type 'list\[Nod\]'"),
    ('# src: manual\ndef root(): ...\n', r'fxhost\.pyi:2: root has no return annotation'),
    ('import os\n', r'fxhost\.pyi:1: Import is not supported'),
    ('# src: manual\n# delete: fxhost.Nope\n', r'fxhost\.pyi:2: cannot delete fxhost\.Nope'),
    (
        '# src: manual\ndef root() -> Node: ...\ndef root() -> Node: ...\n',
        r'fxhost\.pyi:2: fxhost\.root is defined 2 times without @overload',
    ),
    (
        'class Nope:\n    # src: manual\n    def run(self) -> None: ...\n',
        r'fxhost\.pyi:3: fxhost\.Nope is not a module or class',
    ),
    ('def root(:\n', r'fxhost\.pyi:1: not valid Python'),
])
def test_wrong_override_is_a_build_error(
    tmp_path: Path, fixture_names: Names, text: str, message: str,
) -> None:
    """A mistake in an override stops the build and names the file and line."""
    with pytest.raises(OverrideError, match=message):
        _load(tmp_path, 'fxhost', text, fixture_names)


def test_parameters_must_match_a_python_function(tmp_path: Path, fixture_names: Names) -> None:
    """A Python function reports its parameters, so a misspelled one is caught."""
    text = '# src: manual\ndef node_names(node=..., upper=..., prefix=...) -> list[str]: ...\n'
    with pytest.raises(OverrideError, match=r"takes \['nodes', 'upper', 'prefix'\]"):
        _load(tmp_path, 'fxscripts.misc', text, fixture_names)


def test_file_must_name_a_dumped_module(tmp_path: Path, fixture_names: Names) -> None:
    """The file name is the module; an unknown module is a typo."""
    with pytest.raises(OverrideError, match='nope is not a module in the dump'):
        _load(tmp_path, 'nope', '', fixture_names)


@pytest.mark.parametrize('names', ['nuke15_names', 'nuke17_names'])
def test_nuke_overrides_load_on_every_version(names: str, request: pytest.FixtureRequest) -> None:
    """The shipped overrides resolve against each dumped version and add no symbol."""
    version = {'nuke15_names': '15.2v9', 'nuke17_names': '17.1v2'}[names]
    dump = ir.load(data_dir('nuke', version) / 'dump.json')
    resolved_names = request.getfixturevalue(names)

    overrides = load_overrides(HOSTS / 'nuke' / 'overrides', dump, resolved_names)
    assert len(overrides.functions) == 39
    for path in overrides.functions:
        assert resolved_names.find(path)[1] is not None, path


def test_qt_override_follows_the_binding(nuke15_names: Names, nuke17_names: Names) -> None:
    """TrackItem.thumbnail returns a QImage: Any on PySide2, the class on PySide6."""
    returns = []
    for version, names in (('15.2v9', nuke15_names), ('17.1v2', nuke17_names)):
        dump = ir.load(data_dir('nuke', version) / 'dump.json')
        overrides = load_overrides(HOSTS / 'nuke' / 'overrides', dump, names)
        returns.append(overrides.functions['hiero.core.TrackItem.thumbnail'].signatures[0].returns)
    assert returns == [ANY, 'PySide6.QtGui.QImage']


# One row per ported post-fix that changes the result. Verified in Nuke 15.2v9
# unless the override file says otherwise.
@pytest.mark.parametrize(('path', 'returns'), [
    ('nuke.root', 'nuke.Root'),
    ('nuke.toNode', 'nuke.Node | None'),
    ('nuke.allNodes', 'builtins.list[nuke.Node]'),
    ('nuke.tprint', 'None'),
    ('nuke.executeBackgroundNuke', 'builtins.int'),
    ('nuke.executeMultiple', 'None'),
    ('nuke.Node.knob', 'nuke.Knob | None'),
    ('nuke.Node.__getitem__', 'nuke.Knob'),
    ('nuke.Node.dependent', 'builtins.list[nuke.Node]'),
    ('nuke.Menu.addCommand', ANY),
    ('nuke.MenuBar.addCommand', ANY),
    ('hiero.core.project', 'hiero.core.Project | None'),
    ('hiero.core.Project.sequences', 'builtins.list[hiero.core.Sequence]'),
    ('hiero.core.Project.clips', 'builtins.list[hiero.core.Clip]'),
    ('hiero.core.Project.bins', 'builtins.list[hiero.core.Bin]'),
    ('hiero.core.Project.tracks', 'builtins.list[hiero.core.VideoTrack | hiero.core.AudioTrack]'),
    ('hiero.core.Project.videoTracks', 'builtins.list[hiero.core.VideoTrack]'),
    ('hiero.core.Project.audioTracks', 'builtins.list[hiero.core.AudioTrack]'),
    ('hiero.core.Project.trackItems', 'builtins.list[hiero.core.TrackItem]'),
    ('hiero.core.Project.videoTrackItems', 'builtins.list[hiero.core.TrackItem]'),
    ('hiero.core.Project.audioTrackItems', 'builtins.list[hiero.core.TrackItem]'),
    ('hiero.core.Project.extractSettings', 'builtins.dict[builtins.str, builtins.str | builtins.bool]'),
    ('hiero.core.Sequence.videoTracks', 'builtins.tuple[hiero.core.VideoTrack, ...]'),
    ('hiero.core.Sequence.items', 'builtins.tuple[hiero.core.VideoTrack | hiero.core.AudioTrack, ...]'),
    ('hiero.core.Sequence.addClip', 'builtins.list[hiero.core.TrackItem]'),
    ('hiero.core.VideoTrack.items', 'builtins.tuple[hiero.core.TrackItem, ...]'),
    ('hiero.core.EffectTrackItem.isRetimeEffect', 'builtins.bool'),
    ('hiero.core.EffectTrackItem.setName', 'None'),
    (
        'hiero.core.TrackItem.source',
        'hiero.core.Clip | hiero.core.Sequence | hiero.core.MediaSource',
    ),
    ('hiero.core.Bin.importSequence', 'hiero.core.Sequence'),
    ('hiero.FnRedirect.activeSequence', 'hiero.core.Sequence | None'),
    ('hiero.FnRedirect.getTimelineEditor', 'hiero.ui.TimelineEditor | None'),
])
def test_ported_post_fix(nuke15_resolved: Resolved, path: str, returns: str) -> None:
    """Each override reaches the resolved result."""
    [signature] = nuke15_resolved[path]
    assert (signature.returns, signature.returns_source) == (returns, 'override')


@pytest.mark.parametrize(('path', 'count', 'returns'), [
    ('nuke.execute', 2, 'None'),
    ('hiero.core.projects', 2, 'builtins.tuple[hiero.core.Project, ...]'),
    ('hiero.core.Project.setOutputFormat', 2, 'None'),
    ('hiero.core.VideoTrack.addTrackItem', 2, 'hiero.core.TrackItem'),
])
def test_ported_overloads(nuke15_resolved: Resolved, path: str, count: int, returns: str) -> None:
    """NUKE_POST_INJECT and the other overload sets."""
    signatures = nuke15_resolved[path]
    assert len(signatures) == count
    assert {signature.returns for signature in signatures} == {returns}


# Old post-fixes the pipeline now derives without an override.
@pytest.mark.parametrize(('path', 'returns', 'source'), [
    ('nuke.createNode', 'nuke.Node', 'doc_signature'),
    ('hiero.core.conformer', 'hiero.core.Conformer', 'doc_field'),
    ('hiero.core.Clip.readNode', 'nuke.Node', 'doc_field'),
    ('hiero.core.EffectTrackItem.name', 'builtins.str', 'doc_field'),
    ('hiero.core.TrackItemBase.project', 'hiero.core.Project', 'doc_field'),
])
def test_post_fix_no_longer_needed(
    nuke15_derived: Resolved, path: str, returns: str, source: str,
) -> None:
    """These old corrections are evidence the resolver finds itself."""
    [signature] = nuke15_derived[path]
    assert (signature.returns, signature.returns_source) == (returns, source)


@pytest.mark.parametrize('path', [
    'hiero.core.Clip.addToNukeScript',
    'hiero.core.Clip.addAnnotationsToNukeScript',
    'hiero.core.Clip.getReadInfo',
    'hiero.core.TrackItem.unlinkAll',
    'hiero.core.EffectTrackItem.setName',
    'hiero.core.Sequence.addClip',
])
def test_renaming_post_fix_no_longer_needed(nuke15_resolved: Resolved, path: str) -> None:
    """The old generator needed a rename (`_Clip_addToNukeScript`); the dump has the public name."""
    assert path in nuke15_resolved


def test_default_instance_types_the_parameter(nuke15_derived: Resolved) -> None:
    """`script=ScriptWriter()`: the old post-fix typed `script` by hand."""
    [signature] = nuke15_derived['hiero.core.TrackItem.addToNukeScript']
    script = signature.params[1]
    assert (script.type, script.source) == ('hiero.core.nuke.Script.ScriptWriter', 'default')


# Overrides that were removed once the probes found the same signature.
@pytest.mark.parametrize(('path', 'returns'), [
    ('nuke.selectedNodes', 'builtins.list[nuke.Node]'),
    ('nuke.formats', 'builtins.list[nuke.Format]'),
    ('nuke.layers', 'builtins.list[builtins.str]'),
    ('nuke.recentFile', 'builtins.str'),
    ('nuke.stripFrameRange', 'builtins.str'),
    ('nuke.Node.knobs', 'builtins.dict[builtins.str, nuke.Knob]'),
    ('nuke.Node.allKnobs', 'builtins.list[nuke.Knob]'),
    ('nuke.Node.dependencies', 'builtins.list[nuke.Node]'),
    ('nuke.Node.rootNode', 'nuke.Node'),
])
def test_override_no_longer_needed(nuke15_resolved: Resolved, path: str, returns: str) -> None:
    """The pipeline derives these on its own; a regression here would bring back Any."""
    [signature] = nuke15_resolved[path]
    assert signature.returns == returns
    assert signature.returns_source != 'override'
