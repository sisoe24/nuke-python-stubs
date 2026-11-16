# Type stubs for nuke 17.1v2. Generated; do not edit.

"""Functions used by the ModelBuilder node"""

from typing import Any
from nukescripts.autobackdrop import autoBackdrop as autoBackdrop

assist: bool

def bakeApplyTexture(mb: Any) -> None: ...

def bakeProjection(mb: Any) -> None:
    """Create a projection setup for the current frame."""

def bakeSceneSelection(mb: Any) -> None:
    """Create a ModelBuilderGeo node containing a copy of the currently selected geometry."""

def clearNodeSelection() -> None: ...

def copyCamera(srcCam: Any) -> Any: ...

def modelbuilderCreateCallback() -> None: ...

def populateBakeMenu(mb: Any) -> None:
    """Populate the bake menu on a ModelBuilder node."""
