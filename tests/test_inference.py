from __future__ import annotations

from pathlib import Path

import pytest

from hoststubs.names import Names
from hoststubs.inference import Inferred, load_inference
from hoststubs.annotations import normalize

# Regenerate with: python -m hoststubs infer tests/fixtures/dump.golden.json tests/fixtures/host
# then move inference/fxhost-1.0v1 to tests/fixtures/inference.
INFERENCE = Path(__file__).parent / 'fixtures' / 'inference'


@pytest.fixture(scope='module')
def inferred(fixture_names: Names) -> dict[str, Inferred]:
    return load_inference(INFERENCE, fixture_names)


def test_inferred_return_comment(inferred: dict[str, Inferred]) -> None:
    """Pyright's `# -> list[Any]:` comment becomes the return type."""
    assert inferred['fxscripts.misc.node_names'].returns == 'builtins.list[typing.Any]'


def test_source_annotations(inferred: dict[str, Inferred]) -> None:
    """Annotations written in the source are kept for the return and the parameters."""
    function = inferred['fxscripts.misc.script_directory']
    assert function.returns == 'builtins.str'
    assert function.params == {'path': 'builtins.str | None'}


def test_class_in_scope(inferred: dict[str, Inferred]) -> None:
    """A class of the same module resolves to its qualified name."""
    assert inferred['fxscripts.misc.find_panel'].returns == 'fxscripts.misc.Panel | None'


def test_short_name_out_of_scope_is_not_guessed(inferred: dict[str, Inferred]) -> None:
    """Pyright prints `Node`, but the module only imports `fxhost`, so there is no evidence."""
    assert inferred['fxscripts.misc.make_node'].returns is None


def test_literals_widen(inferred: dict[str, Inferred]) -> None:
    """`Literal[True]` is one observed value; the type is `bool`."""
    assert inferred['fxscripts.misc.Panel.show'].returns == 'builtins.bool'
    assert inferred['fxscripts.misc.Panel.default_size'].returns == (
        'builtins.tuple[builtins.int, builtins.int]'
    )


def test_empty_body_is_not_none(inferred: dict[str, Inferred]) -> None:
    """A hook with an empty body is overridden by subclasses, so `None` is not evidence."""
    assert inferred['fxscripts.misc.Panel.on_close'].returns is None
    assert inferred['fxscripts.misc.Panel.__init__'].returns == 'None'


def test_property_setter_does_not_replace_getter(inferred: dict[str, Inferred]) -> None:
    """`size` has a setter that returns None; the entry is the getter, which is unknown."""
    assert inferred['fxscripts.misc.Panel.size'].returns is None
    assert inferred['fxscripts.misc.Panel.name'].returns == 'builtins.str'


def test_self(inferred: dict[str, Inferred]) -> None:
    """A classmethod constructor returns `Self`."""
    assert inferred['fxscripts.misc.Panel.create'].returns == 'typing.Self'


def test_private_functions_are_absent(inferred: dict[str, Inferred]) -> None:
    """Pyright leaves private functions out of a draft stub."""
    assert 'fxscripts.misc._panels' not in inferred


# Annotations as pyright wrote them for Nuke 15.2v9, with the module that holds them.
@pytest.mark.parametrize(('annotation', 'module', 'expected'), [
    ('Literal[False] | None', 'nukescripts.toolsets', 'builtins.bool | None'),
    ('LiteralString', 'nukescripts.hardwareinfo', 'builtins.str'),
    (
        'Generator[Any, Any, None]',
        'nukescripts.snap3d',
        'typing.Generator[typing.Any, typing.Any, None]',
    ),
    ('ResolveTable', 'hiero.core.FnResolveTable', 'hiero.core.FnResolveTable.ResolveTable'),
    (
        'ReformatNode | None',
        'hiero.core.FnNukeHelpersV2',
        'hiero.core.nuke.Node.ReformatNode | None',
    ),
    (
        'tuple[Literal[0], Literal[0], None, None, Literal[0]]',
        'hiero.ui.BuildExternalMediaTrack',
        'builtins.tuple[builtins.int, builtins.int, None, None, builtins.int]',
    ),
    # A union with Any says nothing more than Any.
    ('Any | None', 'hiero.ui.FnExportUIRegistry', None),
    ('Any', 'nukescripts.misc', None),
    (
        'tuple[Literal[0], Literal[0], Any, Any] | tuple[int, int, int, int]',
        'hiero.core.FnEffectHelpers',
        'builtins.tuple[builtins.int, builtins.int, typing.Any, typing.Any]'
        ' | builtins.tuple[builtins.int, builtins.int, builtins.int, builtins.int]',
    ),
    # Pyright prints callable types in a form that is not Python.
    ('(x) -> None', 'nukescripts.misc', None),
])
def test_normalize_real_annotations(
    nuke15_names: Names, annotation: str, module: str, expected: str | None,
) -> None:
    """Each widening and rejection rule, on an annotation from the real output."""
    assert normalize(annotation, nuke15_names, module) == expected
