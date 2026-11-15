from __future__ import annotations

import pytest

from hoststubs.names import Names
from hoststubs.annotations import type_from_text

TYPE_NAMES = {'String': 'builtins.str', 'List': 'builtins.list'}


# Return texts from Nuke 15.2v9 docstrings.
@pytest.mark.parametrize(('text', 'module', 'expected'), [
    ('Node', 'nuke', 'nuke.Node'),
    ('Node or None if it does not exist.', 'nuke', 'nuke.Node | None'),
    ('Menu or None', 'nuke', 'nuke.Menu | None'),
    ('True if successful, False otherwise.', 'nuke', 'builtins.bool'),
    ('bool.', 'nuke', 'builtins.bool'),
    ('None', 'nuke', 'None'),
    ('String', 'nuke', 'builtins.str'),
    ('List.', 'nuke', 'builtins.list'),
    ('Format object.', 'nuke', 'nuke.Format'),
    ('hiero.core.Version object', 'hiero.core', 'hiero.core.Version'),
    # A dotted name in a docstring is a public path, not hiero.core's own `nuke` module.
    ('nuke.Node', 'hiero.core', 'nuke.Node'),
    ('str, optional', 'nuke', 'builtins.str'),
])
def test_text_that_states_a_type(
    nuke15_names: Names, text: str, module: str, expected: str,
) -> None:
    """The text is a type, possibly followed by a clause that cannot change it."""
    assert type_from_text(text, nuke15_names, module, TYPE_NAMES) == expected


@pytest.mark.parametrize(('text', 'module'), [
    ('The root node. This will never be None.', 'nuke'),
    ('The knob named p or the pth knob.', 'nuke'),
    ('node', 'nuke'),
    ('list of nodes', 'nuke'),
    ('Number of first optional input.', 'nuke'),
    ('Name of node.', 'nuke'),
    # `Layer` is a class, but the next word changes the meaning.
    ('Layer name.', 'nuke'),
    # Plural: a collection of unknown kind.
    ('hiero.core.TrackItem objects', 'hiero.core'),
    ('an array of hiero.core.Sequence objects.', 'hiero.core'),
    ('returns all sequences in a project.', 'hiero.core'),
    # `set` is a builtin and an English verb.
    ('set', 'nuke'),
    ('Knob or node to use', 'nuke'),
    ('usg::Array<fdk::Vec3<float> >', 'nuke'),
])
def test_prose_is_not_a_type(nuke15_names: Names, text: str, module: str) -> None:
    """A word inside a sentence is not evidence, even when a class has that name."""
    assert type_from_text(text, nuke15_names, module, TYPE_NAMES) is None
