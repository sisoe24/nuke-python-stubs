# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import PySide6.QtWidgets as _PySide6_QtWidgets
from hiero.core import Project as Project
from hiero.core.events import EventType as EventType
import hiero as hiero

ClipPosterFrameFuncs: dict
eventFlags: tuple

class PosterFrameDialog(_PySide6_QtWidgets.QDialog):
    """Dialog for setting custom poster frames on selected clips. """
    kAbsolute: int
    kRelative: int
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, clips: Any, parent: Any) -> None: ...
    def accept(self) -> None: ...
    def onComboBoxIndexChanged(self, index: Any) -> None: ...

class PosterFrameSelectionWidgets:
    """Not a widget itself, creates and manages the label and input widget for
    selecting poster frame numbers.
    """
    def __init__(self, label: Any) -> None: ...
    def inputWidget(self) -> _PySide6_QtWidgets.QLineEdit: ...
    def labelWidget(self) -> _PySide6_QtWidgets.QLabel: ...
    def setEnabled(self, enabled: Any) -> None: ...
    def setRange(self, minFrame: Any, maxFrame: Any, startFrame: Any) -> None: ...
    def value(self) -> int: ...

def binContextMenuEvent(event: Any) -> None:
    """Callback when context menu is shown in the project panel. """

def findClipsInBinSelection(selection: Any) -> list[Any]:
    """Find selected clips, recursing through the bin hierarchy. """

def findIntersectingFrameRange(ranges: Any) -> tuple[Any, Any]:
    """Try to find the intersection of a sequence of frame range tuples. Raises a
    RuntimeError if the ranges did not all intersect.
    """

def isValidClipForPosterFrames(clip: Any) -> Any:
    """Check if poster frames can be set on a clip. """

def onClipAddedToProject(event: Any) -> None:
    """Callback when a clip is added to a project. Sets the poster frame according
    to the project settings.
    """

def setPosterFrames(clips: Any, func: Any) -> None:
    """For each clip, set the poster frame, calling func to get the value """

def showPosterFrameDialog(clips: Any) -> None: ...

def viewerContextMenuEvent(event: Any) -> None:
    """Callback when context menu is shown in a viewer. """
