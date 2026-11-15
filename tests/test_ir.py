from __future__ import annotations

import json
from pathlib import Path

import pytest

from hoststubs import ir

GOLDEN = Path(__file__).parent / 'fixtures' / 'dump.golden.json'


@pytest.fixture(scope='module')
def dump() -> ir.Dump:
    return ir.load(GOLDEN)


def test_header(dump: ir.Dump) -> None:
    """Host, Qt binding, import errors and outside references are loaded."""
    assert (dump.host, dump.host_version) == ('fxhost', '1.0v1')
    assert dump.qt == ir.Qt(binding='PySide2', version='5.15.2')
    assert [error['where'] for error in dump.errors] == ['fxscripts.broken']
    assert dump.foreign == {'PySide2': 3}


def test_skipped_module_is_absent(dump: ir.Dump) -> None:
    """A skipped module is neither dumped nor reported as an error."""
    assert 'fxscripts.examples' not in dump.modules


def test_c_function_has_doc_but_no_signature(dump: ir.Dump) -> None:
    """A C function without a signature keeps its docstring as the only evidence."""
    knob = dump.modules['fxhost'].members['Node'].members['knob']
    assert knob.signature is None
    assert knob.doc.startswith('self.knob(p[, follow_link]) -> The knob named p')
    assert knob.binding == 'instance'


def test_text_signature(dump: ir.Dump) -> None:
    """__text_signature__ is recorded verbatim."""
    function = dump.modules['fxhost'].members['withTextSignature']
    assert function.text_signature == '($module, name, index=0, /)'


def test_private_origin_is_owned_by_public_module(dump: ir.Dump) -> None:
    """A class from a private or unimportable module is recorded where it is exposed."""
    members = dump.modules['fxhost'].members
    assert members['Node'].origin == '_fxhost'
    assert members['Sequence'].origin == 'core'


def test_reexport_is_an_alias(dump: ir.Dump) -> None:
    """A re-exported object points to its defining module instead of being copied."""
    host = dump.modules['fxhost'].members
    scripts = dump.modules['fxscripts'].members

    assert host['frame_range'] == ir.Alias('fxhost.utils.frame_range', False)
    assert scripts['QObject'] == ir.Alias('PySide2.QtCore.QObject', False)
    assert scripts['os'] == ir.Alias('os', True)


def test_constants(dump: ir.Dump) -> None:
    """Numbers keep their value; strings do not, because they can hold local paths."""
    members = dump.modules['fxhost'].members
    assert members['ADD_VIEWS'] == ir.Value('builtins.int', '1')
    assert members['EXE_PATH'] == ir.Value('builtins.str', None)


def test_signal_is_a_value(dump: ir.Dump) -> None:
    """A Qt signal in a class body is an attribute, not a method."""
    signal = dump.modules['fxhost'].members['TimelineEditor'].members['selectionChanged']
    assert signal == ir.Value('PySide2.QtCore.Signal', None)


def test_python_signature(dump: ir.Dump) -> None:
    """A Python function keeps parameter kinds, annotations and default types."""
    signature = dump.modules['fxscripts.misc'].members['node_names'].signature
    assert [param.name for param in signature.params] == ['nodes', 'upper', 'prefix']
    assert signature.params[0].default == ir.Value('builtins.NoneType', 'None')
    assert signature.params[1].default == ir.Value('builtins.bool', 'False')
    assert signature.params[2].default == ir.Value('builtins.str', "''")

    annotated = dump.modules['fxhost.utils'].members['frame_range'].signature
    assert annotated.params[0].annotation == 'int'
    assert annotated.returns == 'list[int]'


def test_class_members(dump: ir.Dump) -> None:
    """Properties, static and class methods, slots and nested classes are told apart."""
    panel = dump.modules['fxscripts.misc'].members['Panel']
    assert panel.bases == ('PySide2.QtCore.QObject',)
    assert panel.members['name'].getter.signature.returns == 'str'
    assert panel.members['name'].settable is False
    assert panel.members['size'].settable is True
    assert panel.members['default_size'].binding == 'static'
    assert panel.members['create'].binding == 'class'
    assert isinstance(panel.members['Options'], ir.Class)

    width = dump.modules['fxhost'].members['Format'].members['width']
    assert width == ir.Property('builtins.member_descriptor', None, None, None)


def test_wrong_schema_is_rejected(tmp_path: Path) -> None:
    """A dump with another schema version stops the load."""
    path = tmp_path / 'dump.json'
    path.write_text(json.dumps({'schema': 0}), encoding='utf-8')

    with pytest.raises(ValueError, match='schema 0, expected 1'):
        ir.load(path)
