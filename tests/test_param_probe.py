from __future__ import annotations

import os
import sys
import json
import subprocess
from pathlib import Path

import pytest

from hoststubs.host import REPO, data_dir, load_host
from hoststubs.names import Names
from hoststubs.params import load_params
from hoststubs.resolve import ANY, ProbedParams, Signature

SCRIPT = REPO / 'src' / 'hoststubs' / 'inhost' / 'param_probe.py'
FIXTURES = Path(__file__).parent / 'fixtures'
Resolved = dict[str, tuple[Signature, ...]]

# Real C functions with standard argument parsing, so the test needs no host.
TARGETS = [
    {'path': 'math.pow', 'owner': 'math', 'name': 'pow', 'kind': 'function', 'on': 'owner', 'count': None},
    {'path': 'os.getcwd', 'owner': 'os', 'name': 'getcwd', 'kind': 'function', 'on': 'owner', 'count': None},
]


@pytest.fixture(scope='module')
def probe_file(tmp_path_factory: pytest.TempPathFactory) -> Path:
    tmp_path = tmp_path_factory.mktemp('params')
    targets = tmp_path / 'targets.json'
    targets.write_text(json.dumps({'targets': TARGETS}), encoding='utf-8')

    out = tmp_path / 'params.json'
    command = [
        sys.executable, str(SCRIPT), str(out),
        f'targets={targets}', f'scene={FIXTURES / "probe_scene.py"}',
    ]
    env = {**os.environ, 'PYTHONPATH': str(FIXTURES / 'host')}
    subprocess.run(command, env=env, check=True)
    return out


@pytest.fixture(scope='module')
def raw(probe_file: Path) -> dict:
    return json.loads(probe_file.read_text(encoding='utf-8'))['functions']


def test_counts_from_errors(raw: dict) -> None:
    """'expected 2 arguments, got 0' and 'takes no arguments' give the argument counts."""
    [power] = raw['math.pow']
    [getcwd] = raw['os.getcwd']
    assert (power['minimum'], power['maximum']) == (2, 2)
    assert (getcwd['minimum'], getcwd['maximum']) == (0, 0)


def test_candidate_passes_when_the_error_blames_the_poison(raw: dict) -> None:
    """math.pow(1, POISON): the error is about the poison, so position 1 accepts int."""
    outcomes = raw['math.pow'][0]['positions'][0]['candidates']
    assert 'HostStubsPoison' in outcomes['builtins.int']['message']
    assert 'HostStubsPoison' in outcomes['builtins.float']['message']
    assert 'HostStubsPoison' not in outcomes['builtins.str']['message']


def test_last_position_gets_only_the_poison(raw: dict) -> None:
    """Nothing can follow the last argument, so no candidate is tried there."""
    last = raw['math.pow'][0]['positions'][1]
    assert last['candidates'] == {}
    assert 'must be real number, not HostStubsPoison' in last['poison']['message']


def test_function_body_does_not_run(raw: dict) -> None:
    """Every call on math.pow ends in a TypeError; none returns a value."""
    record = raw['math.pow'][0]
    outcomes = [record['none'], record['many']]
    for position in record['positions']:
        outcomes += [position['poison'], *position['candidates'].values()]
    assert {outcome.get('error') for outcome in outcomes} == {'TypeError'}


def test_reader_types_each_position(probe_file: Path, fixture_names: Names) -> None:
    """Error text and accepted candidates give float for both positions of pow."""
    probed = load_params(probe_file, fixture_names, ())
    assert probed['math.pow'] == ProbedParams(2, 2, ('builtins.float', 'builtins.float'))
    assert probed['os.getcwd'] == ProbedParams(0, 0, ())


@pytest.fixture(scope='module')
def nuke_params(nuke15_names: Names) -> dict[str, ProbedParams]:
    host = load_host('nuke')
    return load_params(data_dir('nuke', '15.2v9') / 'params-nuke.json', nuke15_names, host.probe_messages)


# Read from the errors Nuke 15.2v9 gave.
@pytest.mark.parametrize(('path', 'expected'), [
    # "toNode() argument 1 must be str, not HostStubsPoison"
    ('nuke.toNode', ProbedParams(1, 1, ('builtins.str',))),
    # "'HostStubsPoison' object cannot be interpreted as an integer"
    ('nuke.Node.setXYpos', ProbedParams(2, 2, ('builtins.int', 'builtins.int'))),
    # "takes no arguments (12 given)"
    ('nuke.root', ProbedParams(0, 0, ())),
    # "expecting a Nuke node type": a host message from the config
    ('nuke.layers', ProbedParams(0, 1, ('nuke.Node',))),
])
def test_nuke_messages(nuke_params: dict[str, ProbedParams], path: str, expected: ProbedParams) -> None:
    """Counts and types as Nuke's own argument checks state them."""
    assert nuke_params[path] == expected


def test_str_or_none_message(nuke_params: dict[str, ProbedParams]) -> None:
    """'must be str or None' keeps the None."""
    assert 'builtins.str | None' in nuke_params['nuke.Knob.setLabel'].types


def test_receiver_that_refuses_the_call_is_ignored(nuke_params: dict[str, ProbedParams]) -> None:
    """Root answers 'invalid' to setInput; the reading comes from the plain Node."""
    assert (nuke_params['nuke.Node.setInput'].minimum, nuke_params['nuke.Node.setInput'].maximum) == (2, 2)


def test_subclasses_that_differ_merge_permissively(nuke_params: dict[str, ProbedParams]) -> None:
    """Knob.setValue needs one argument on one knob class and takes three on another."""
    assert nuke_params['nuke.Knob.setValue'] == ProbedParams(1, 3, (None,))


def test_base_method_accepts_the_common_call(probed: Resolved) -> None:
    """`knob.setValue(10)` is the most common Nuke call; `chan` must not be required."""
    assert _params(probed['nuke.Knob.setValue'][0])[:2] == [('val', ANY, False), ('chan', ANY, True)]


@pytest.fixture(scope='module')
def probed(nuke15_probed: Resolved) -> Resolved:
    return nuke15_probed


def _params(signature: Signature) -> list[tuple[str, str, bool]]:
    return [(param.name, param.type, param.has_default) for param in signature.params[1:]]


def test_types_replace_untyped_documented_params(probed: Resolved) -> None:
    """setXYpos(x, y): names from the docstring, types from the parser."""
    assert _params(probed['nuke.Node.setXYpos'][0]) == [
        ('x', 'builtins.int', False), ('y', 'builtins.int', False),
    ]
    assert probed['nuke.Node.setXYpos'][0].params[1].source == 'probe'


def test_documented_required_params_are_relaxed(probed: Resolved) -> None:
    """Format.scaled(sx, sy, tx, ty) is documented as four required; a call with none works."""
    assert [optional for _, _, optional in _params(probed['nuke.Format.scaled'][0])] == [True] * 4


def test_parser_never_makes_a_param_required(probed: Resolved) -> None:
    """Node.knob's parser claims two required arguments, but knob('size') works."""
    assert _params(probed['nuke.Node.knob'][0]) == [('p', ANY, False), ('follow_link', ANY, True)]


def test_shape_from_parser_when_docstring_has_none(probed: Resolved) -> None:
    """No signature line in the docstring: positional-only parameters from the counts."""
    signature = probed['hiero.core.TimeBase.convert'][0]
    assert signature.shape_source == 'probe'
    assert [(param.name, param.kind) for param in signature.params] == [
        ('arg1', 'POSITIONAL_ONLY'), ('arg2', 'POSITIONAL_ONLY'), ('arg3', 'POSITIONAL_ONLY'),
    ]
