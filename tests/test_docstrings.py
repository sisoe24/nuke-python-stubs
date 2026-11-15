from __future__ import annotations

import pytest

from hoststubs import ir
from hoststubs.docstrings import (VAR_POSITIONAL, fields, parse_params, signature_lines,
                                  is_documented_optional)


def _doc(dump: ir.Dump, module: str, *path: str) -> str:
    member = dump.modules[module].members[path[0]]
    for name in path[1:]:
        member = member.members[name]
    return member.doc


def test_optional_brackets() -> None:
    """`p[, follow_link]` from Node.knob: the bracket marks what can be left out."""
    params = parse_params('p[, follow_link]')
    optional = [(param.name, param.optional) for param in params]
    assert optional == [('p', False), ('follow_link', True)]


def test_default_value() -> None:
    """A default from nuke.execute's line is kept as text and makes the parameter optional."""
    params = parse_params('nameOrNode, start, end, incr, views, continueOnError = False')
    assert [param.name for param in params][-1] == 'continueOnError'
    assert params[-1].default == 'False'
    assert params[-1].optional
    assert not params[0].optional


def test_pybind_annotations_with_cpp_types() -> None:
    """pybind11 writes C++ types with `::` and templates; they are kept as text."""
    params = parse_params('self: _nuke.GeoSelectionItem, stage: usg::Stage, time: float = nan')
    assert [(param.name, param.annotation) for param in params] == [
        ('self', '_nuke.GeoSelectionItem'), ('stage', 'usg::Stage'), ('time', 'float'),
    ]


def test_ellipsis_and_brackets_in_defaults() -> None:
    """`...` means more arguments; `[]` after `=` is a default, not an optional marker."""
    params = parse_params('name, items=[], ...')
    assert params[1].default == '[]'
    assert params[2].kind == VAR_POSITIONAL


@pytest.mark.parametrize('text', ['from, to', 'x, x', "'name'", 'a b'])
def test_not_a_signature(text: str) -> None:
    """A keyword, a duplicate or a non-identifier cannot be a Python parameter list."""
    assert parse_params(text) is None


def test_signature_line(nuke15_dump: ir.Dump) -> None:
    """The first line of Node.knob declares parameters and a return text."""
    [signature] = signature_lines(_doc(nuke15_dump, 'nuke', 'Node', 'knob'), 'knob')
    assert [param.name for param in signature.params] == ['p', 'follow_link']
    assert signature.returns == 'The knob named p or the pth knob.'


def test_overloads_are_leading_lines(nuke15_dump: ir.Dump) -> None:
    """nuke.execute starts with two signature lines: two overloads."""
    signatures = signature_lines(_doc(nuke15_dump, 'nuke', 'execute'), 'execute')
    assert [len(signature.params) for signature in signatures] == [6, 4]
    assert signatures[0].returns == 'None.'


def test_example_further_down_is_not_a_signature() -> None:
    """Project.sequences ends with a usage example that also looks like a call."""
    doc = (
        'self.sequences(partialName) -> returns all sequences in a project.\n'
        '@return: an array of hiero.core.Sequence objects.\n\n'
        'Example: finds all sequences in a project with 30Sec in the name:\n\n'
        "sequences = myProject.sequences('30Sec')"
    )
    assert len(signature_lines(doc, 'sequences')) == 1


def test_line_without_parentheses(nuke15_dump: ir.Dump) -> None:
    """hiero writes some methods as `self.rotation -> float`: a return, no parameter list."""
    doc = _doc(nuke15_dump, 'hiero.core', 'AnnotationText', 'rotation')
    [signature] = signature_lines(doc, 'rotation')
    assert signature.params is None
    assert signature.returns == 'float'


def test_rest_fields(nuke15_dump: ir.Dump) -> None:
    """nuke.createNode uses reST fields with `:type:` and `:rtype:`."""
    found = fields(_doc(nuke15_dump, 'nuke', 'createNode'))
    assert found.param_types == {
        'node': 'str', 'knobs': 'str, optional', 'inpanel': 'bool, optional',
    }
    assert found.returns == 'The node created.'
    assert found.return_type == 'nuke.Node'


def test_epydoc_fields(nuke15_dump: ir.Dump) -> None:
    """Node.knob uses epydoc fields."""
    found = fields(_doc(nuke15_dump, 'nuke', 'Node', 'knob'))
    assert found.params['p'] == 'A string or an integer.'
    assert found.returns == 'The knob named p or the pth knob.'


def test_documented_optional(nuke15_dump: ir.Dump) -> None:
    """allNodes lists `filter` as if required, but its field says 'Optional.'"""
    doc = _doc(nuke15_dump, 'nuke', 'allNodes')
    assert is_documented_optional(doc, fields(doc), 'filter')

    doc = _doc(nuke15_dump, 'nuke', 'Node', 'knob')
    assert not is_documented_optional(doc, fields(doc), 'p')
