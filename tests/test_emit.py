from __future__ import annotations

import ast
import inspect
from pathlib import Path

import pytest

from hoststubs import ir
from hoststubs.emit import Context, docstring, emit, module_file, normalize_version
from hoststubs.names import Names
from hoststubs.resolve import Resolver, resolve_functions
from hoststubs.inference import load_inference
from hoststubs.overrides import Overrides, load_overrides

FIXTURES = Path(__file__).parent / 'fixtures'
GOLDEN = FIXTURES / 'stubs'


def _fixture_context(overrides_dir: Path | None = None) -> Context:
    dump = ir.load(FIXTURES / 'dump.golden.json')
    names = Names(dump)
    inferred = load_inference(FIXTURES / 'inference', names)
    resolver = Resolver(dump, names, {}, inferred, {}, {})

    overrides = Overrides({}, {})
    if overrides_dir:
        overrides = load_overrides(overrides_dir, dump, names)
    overridden = {path: override.signatures for path, override in overrides.functions.items()}
    resolved = resolve_functions(resolver, dump, overridden, set(overrides.deleted))
    return Context(dump, names, resolved, overrides)


def _emitted(tmp_path: Path, overrides_dir: Path | None = None) -> dict[str, str]:
    written = emit(_fixture_context(overrides_dir), tmp_path)
    return {path.relative_to(tmp_path).as_posix(): path.read_text() for path in written}


def test_fixture_stubs_match_golden(tmp_path: Path) -> None:
    """The stubs for the fixture host are byte-identical to the committed ones.

    Regenerate by emitting `_fixture_context()` into tests/fixtures/stubs.
    """
    emitted = _emitted(tmp_path)
    golden = {path.relative_to(GOLDEN).as_posix(): path.read_text() for path in GOLDEN.rglob('*.pyi')}
    assert emitted == golden


def test_every_fixture_stub_parses(tmp_path: Path) -> None:
    """Each emitted file is valid Python."""
    for text in _emitted(tmp_path).values():
        ast.parse(text)


def test_docstrings_survive(tmp_path: Path) -> None:
    """A docstring read back from the stub is the docstring in the dump."""
    dump = ir.load(FIXTURES / 'dump.golden.json')
    tree = ast.parse(_emitted(tmp_path)['fxhost/__init__.pyi'])

    functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
    original = dump.modules['fxhost'].members['allNodes'].doc
    assert inspect.cleandoc(ast.get_docstring(functions['allNodes'])) == original


@pytest.mark.parametrize('doc', [
    'One line.',
    'First line.\n\nSecond paragraph.\n    indented code',
    'A path: C:\\temp\\new and a regex \\d+',
    'Contains """triple quotes""" inside',
    'Ends with a quote"',
])
def test_docstring_literal_evaluates_back(doc: str) -> None:
    """Backslashes and quotes in a docstring do not change or break it."""
    source = 'def function():\n' + '\n'.join(docstring(doc, '    '))
    function = ast.parse(source).body[0]
    assert ast.get_docstring(function) == inspect.cleandoc(doc)


def test_types_use_short_local_names_and_imports(tmp_path: Path) -> None:
    """A class of the same file is named directly; typing names are imported."""
    text = _emitted(tmp_path)['fxscripts/misc.pyi']
    assert 'def find_panel(name: Any) -> Panel | None: ...' in text
    assert 'from typing import Any' in text


def test_no_star_or_bare_relative_imports(tmp_path: Path) -> None:
    """Imports are explicit: no star import, and re-exports use the `x as x` form."""
    for text in _emitted(tmp_path).values():
        assert 'import *' not in text
    assert 'from fxscripts.misc import Panel as Panel' in _emitted(tmp_path)['fxscripts/__init__.pyi']


def test_private_members_are_left_out(tmp_path: Path) -> None:
    """A private module-level function is not part of the stub."""
    assert '_panels' not in _emitted(tmp_path)['fxscripts/misc.pyi']


def test_property_staticmethod_classmethod(tmp_path: Path) -> None:
    """Each kind of class member keeps its decorator; a settable property gets a setter."""
    text = _emitted(tmp_path)['fxscripts/misc.pyi']
    assert '    @property\n    def name(self) -> str:' in text
    assert '    @size.setter\n    def size(self, value: Any) -> None: ...' in text
    assert '    @staticmethod\n    def default_size() -> tuple[int, int]: ...' in text
    assert '    @classmethod\n    def create(cls, name: Any) -> Self: ...' in text


def test_slots_that_hide_typos_are_left_out(nuke15_emitted: dict[str, str]) -> None:
    """`__getattribute__` in a stub would make every attribute access valid."""
    text = nuke15_emitted['nuke/__init__.pyi']
    assert '__getattribute__' not in text
    assert '__setattr__' not in text


def test_shadowed_name_is_qualified(nuke15_emitted: dict[str, str]) -> None:
    """hiero.core has its own `nuke` submodule, so Nuke's Node is imported under an alias."""
    text = nuke15_emitted['hiero/core/__init__.pyi']
    assert 'import nuke as _nuke' in text
    assert 'def dissolveNode(self) -> _nuke.Node:' in text


def test_override_adds_and_deletes(tmp_path: Path) -> None:
    """An override for an unknown name adds a function; `# delete:` removes one."""
    overrides = tmp_path / 'overrides'
    overrides.mkdir()
    (overrides / 'fxhost.pyi').write_text(
        '# src: manual\n'
        'def brandNew(count: int) -> list[Node]:\n'
        '    """Added by hand."""\n'
        '\n'
        '# src: manual\n'
        '# delete: fxhost.toNode\n',
    )
    text = _emitted(tmp_path / 'out', overrides)['fxhost/__init__.pyi']
    assert 'def brandNew(count: int) -> list[Node]:\n    """Added by hand."""' in text
    assert 'def toNode' not in text


@pytest.mark.parametrize(('raw', 'expected'), [('15.2v9', '15.2.9'), ('17.1v2', '17.1.2'), ('20.5.332', '20.5.332')])
def test_normalize_version(raw: str, expected: str) -> None:
    """A host version becomes a PEP 440 release."""
    assert normalize_version(raw) == expected


def test_module_file() -> None:
    """A top-level module or one with submodules is a package; a leaf is a file."""
    modules = dict.fromkeys(['nuke', 'hiero', 'hiero.core', 'hiero.core.nuke', 'hiero.ui'])
    assert module_file('nuke', modules) == Path('nuke/__init__.pyi')
    assert module_file('hiero.core', modules) == Path('hiero/core/__init__.pyi')
    assert module_file('hiero.ui', modules) == Path('hiero/ui.pyi')
