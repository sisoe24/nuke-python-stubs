from __future__ import annotations

import pytest

from hoststubs.names import Names


@pytest.mark.parametrize(('qualified', 'expected'), [
    ('nuke.Node', 'nuke.Node'),
    # Nuke C classes report `builtins` as their module.
    ('builtins.Node', 'nuke.Node'),
    # hiero C classes report `core`; users import them from `hiero.core`.
    ('core.Sequence', 'hiero.core.Sequence'),
    # A re-export resolves to the module that defines the class.
    ('nukescripts.PythonPanel', 'nukescripts.panels.PythonPanel'),
    ('builtins.int', 'builtins.int'),
    ('logging.Logger', 'logging.Logger'),
])
def test_accepted_names(nuke15_names: Names, qualified: str, expected: str) -> None:
    """A dump class, a builtin and a standard-library type are accepted."""
    assert nuke15_names.accept(qualified) == expected


@pytest.mark.parametrize('qualified', [
    'nuke.addOnCreate',      # a function, not a class
    'os.nothing',            # no such attribute
    'foundry.ui.Thing',      # a package outside the dump
    'builtins.print',        # a builtin that is not a type
])
def test_rejected_names(nuke15_names: Names, qualified: str) -> None:
    """A name that is not a known class is rejected."""
    assert nuke15_names.accept(qualified) is None


def test_qt_needs_a_typed_binding(nuke15_names: Names, nuke17_names: Names) -> None:
    """Qt names are accepted for PySide6 only; PySide2 has no types to resolve them."""
    assert nuke15_names.accept('PySide2.QtCore.QRect') is None
    assert nuke17_names.accept('PySide6.QtCore.QRect') == 'PySide6.QtCore.QRect'
    assert nuke17_names.accept('PySide2.QtCore.QRect') is None


def test_resolve_uses_the_module_namespace(nuke15_names: Names) -> None:
    """A name means what the module's runtime namespace says it means."""
    assert nuke15_names.resolve('nuke.Node', 'nukescripts.misc') == 'nuke.Node'
    assert nuke15_names.resolve('Knob', 'nuke') == 'nuke.Knob'
    assert nuke15_names.resolve('Self', 'nuke') == 'typing.Self'


@pytest.mark.parametrize('word', ['List', 'node', 'Number', 'string'])
def test_prose_words_are_not_types(nuke15_names: Names, word: str) -> None:
    """A word from a docstring such as 'allNodes(filter, group) -> List.' is never a type."""
    assert nuke15_names.resolve(word, 'nuke') is None
