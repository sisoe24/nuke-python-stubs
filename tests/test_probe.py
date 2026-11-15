from __future__ import annotations

import os
import ast
import sys
import json
import subprocess
from pathlib import Path

import pytest

from hoststubs.host import REPO

PROBE_SCRIPT = REPO / 'inhost' / 'probe.py'
FIXTURES = Path(__file__).parent / 'fixtures'


def _target(path: str, kind: str = 'function', on: str = 'owner') -> dict[str, str]:
    owner, _, name = path.rpartition('.')
    return {'path': path, 'owner': owner, 'name': name, 'kind': kind, 'on': on}


TARGETS = [
    _target('fxhost.Node.name', on='instance'),
    _target('fxhost.Node.knob', on='instance'),
    _target('fxhost.Format.width', kind='property', on='instance'),
    _target('fxhost.Format.height', kind='property', on='instance'),
    _target('fxhost.Knob.missing', on='instance'),
    _target('fxhost.allNodes'),
    _target('fxhost.root'),
    _target('fxhost.toNode'),
]


def _run(tmp_path: Path, *extra: str) -> dict:
    targets = tmp_path / 'targets.json'
    targets.write_text(json.dumps({'targets': TARGETS}), encoding='utf-8')

    out = tmp_path / 'probe.json'
    command = [
        sys.executable, str(PROBE_SCRIPT), str(out),
        f'targets={targets}', f'scene={FIXTURES / "probe_scene.py"}', *extra,
    ]
    env = {**os.environ, 'PYTHONPATH': str(FIXTURES / 'host')}
    subprocess.run(command, env=env, check=True)
    return json.loads(out.read_text(encoding='utf-8'))


@pytest.fixture(scope='module')
def probe(tmp_path_factory: pytest.TempPathFactory) -> dict:
    return _run(tmp_path_factory.mktemp('probe'))


def test_method_is_called_on_each_instance(probe: dict) -> None:
    """A method is called on every scene instance of its class."""
    observations = probe['observations']['fxhost.Node.name']
    assert [observation['type'] for observation in observations] == ['builtins.str'] * 2
    assert observations[0]['receiver'] == '_fxhost.Node'


def test_container_records_element_types(probe: dict) -> None:
    """A list is recorded with the types of its elements and its length."""
    [observation] = probe['observations']['fxhost.allNodes']
    assert observation == {
        'type': 'builtins.list', 'elements': ['_fxhost.Node'], 'length': 2,
        'receiver': 'builtins.module',
    }


def test_none_is_recorded_as_its_type(probe: dict) -> None:
    """A None result is kept as NoneType; the offline loader decides to discard it."""
    [observation] = probe['observations']['fxhost.toNode']
    assert observation['type'] == 'builtins.NoneType'


def test_call_that_needs_arguments_is_an_error(probe: dict) -> None:
    """A function that cannot be called without arguments is recorded as an error."""
    [first, _] = probe['observations']['fxhost.Node.knob']
    assert first['error'] == 'TypeError'


def test_property_is_read(probe: dict) -> None:
    """A property is read, not called. An unset slot raises and is recorded."""
    [width] = probe['observations']['fxhost.Format.width']
    [height] = probe['observations']['fxhost.Format.height']
    assert width['type'] == 'builtins.int'
    assert height['error'] == 'AttributeError'


def test_class_without_instance_has_no_observation(probe: dict) -> None:
    """The scene holds no Knob, so its method is listed with nothing observed."""
    assert probe['observations']['fxhost.Knob.missing'] == []


def test_scene_is_recorded(probe: dict) -> None:
    """The scene the observations come from is part of the output."""
    assert probe['scene'] == ['two nodes, one format with width set']
    assert probe['crashed'] == []


def test_journal_is_written_before_each_call(tmp_path: Path) -> None:
    """Each target has a start line before its result line, in call order."""
    _run(tmp_path)
    lines = (tmp_path / 'probe.json.journal').read_text(encoding='utf-8').splitlines()
    assert lines[0] == '> fxhost.Node.name'
    assert lines[1].startswith('< fxhost.Node.name [')
    assert [line.split()[1] for line in lines[::2]] == [target['path'] for target in TARGETS]


def test_resume_skips_journalled_calls_and_reports_the_crash(tmp_path: Path) -> None:
    """After a crash in fxhost.root, a resumed run does not call it again and names it."""
    (tmp_path / 'probe.json.journal').write_text('> fxhost.root\n', encoding='utf-8')

    probe = _run(tmp_path, 'resume')
    assert probe['crashed'] == ['fxhost.root']
    assert 'fxhost.root' not in probe['observations']
    assert 'fxhost.allNodes' in probe['observations']


@pytest.mark.parametrize('script', sorted((REPO / 'inhost').glob('*.py')), ids=lambda path: path.name)
def test_in_host_script_is_python37_and_stdlib_only(script: Path) -> None:
    """Scripts that run inside the host use Python 3.7 syntax and no extra package."""
    source = script.read_text(encoding='utf-8')
    tree = ast.parse(source, feature_version=(3, 7))

    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split('.')[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.add(node.module.split('.')[0])

    # param_probe.py imports its sibling probe.py.
    assert imported - {'probe'} <= sys.stdlib_module_names
