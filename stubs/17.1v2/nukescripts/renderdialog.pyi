# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import nukescripts.panels as _nukescripts_panels
import threading as _threading
from nuke_internal.executeInMain import executeInMainThreadWithResult as executeInMainThreadWithResult
from nukescripts import captureViewer as captureViewer
from nukescripts import flipbooking as flipbooking
from nukescripts.fnFlipbookRenderer import getFlipbookRenderer as getFlipbookRenderer
from nukescripts.panels import PythonPanel as PythonPanel

class DialogState:
    def __init__(self) -> None: ...
    def get(self, knob: Any, defaultValue: Any = ...) -> None:
        """Return the given knob's stored last state value.
        If none exists, defaultValue is returned.
        Values are stored in a dict referenced by knob name, so names must be unique!
        """
    def getValue(self, id: Any, defaultValue: Any = ...) -> None:
        """Recalls the value. If it was not set before, it will return the defaultValue."""
    def save(self, knob: Any) -> None:
        """Store the knob's current value as the 'last state' for the next time the dialog is opened.
        Values are stored in a dict referenced by knob name, so names must be unique!
        """
    def saveValue(self, id: Any, value: Any) -> None:
        """Stores the value with the given id."""
    def setKnob(self, knob: Any, defaultValue: Any = ...) -> None:
        """Convenience method for setting a value straight on a knob."""

class ExecuteDialog(_nukescripts_panels.PythonPanel):
    def __init__(self, dialogState: Any, groupContext: Any, nodeSelection: Any = ..., exceptOnError: bool = ...) -> None: ...
    def addKnob(self, knob: Any) -> None:
        """Add the knob and make sure it cannot be animated."""
    def addToPane(self) -> None: ...
    def knobChanged(self, knob: Any) -> None: ...
    def run(self) -> None: ...

class RenderDialog(ExecuteDialog):
    ShowWarning: bool
    deprecatedWarningShown: bool
    shouldShowBGRender: bool
    def __init__(self, dialogState: Any, groupContext: Any, nodeSelection: Any = ..., exceptOnError: bool = ..., allowFrameServer: bool = ...) -> None: ...
    def backgroundRenderAvailable(self) -> bool:
        """Return whether background rendering should be allowed for this render"""
    def extractContainerNodes(self, nodeSelection: Any) -> tuple[list[Any], list[Any]]: ...
    def frameserverRenderAvailable(self) -> bool: ...
    def getNodeSelection(self) -> Any: ...
    def isBackgrounded(self) -> bool:
        """Return whether the background rendering option is enabled."""
    def isFrameserverEnabled(self) -> bool:
        """Return whether the frame server option is enabled."""
    def isTimelineWrite(self) -> bool: ...
    def knobChanged(self, knob: Any) -> None: ...
    def renderContainsContainers(self) -> bool: ...
    def renderToFrameServer(self, frame_ranges: Any, views: Any) -> None: ...
    def run(self) -> None: ...
    def saveFileToRender(self, prefix: Any, forceSaveNew: Any) -> tuple[Any, bool]: ...

class FlipbookDialog(RenderDialog):
    def __init__(self, dialogState: Any, groupContext: Any, node: Any, takeNodeSettings: Any) -> None: ...
    def flipbookKnobs(self) -> None: ...
    def knobChanged(self, knob: Any) -> None: ...
    def run(self) -> None: ...

class ViewerCaptureDialog(FlipbookDialog):
    def __init__(self, dialogState: Any, groupContext: Any, node: Any) -> None: ...
    def captureViewer(self) -> Any:
        """Return an instance of a CaptureViewer class, which when executed captures the viewer.
        
        """
    def knobChanged(self, knob: Any) -> None: ...

class ViewerCaptureDialogThread(_threading.Thread):
    def __init__(self, captureViewer: Any) -> None: ...
    def run(self) -> None: ...

def bboxToTopLeft(height: Any, roi: Any) -> dict[str, Any]:
    """Convert the roi passed from a origin at the bottom left to the top left.
    Also replaces the r and t keys with w and h keys.
    @param height: the height used to determine the top.
    @param roi: the roi with a bottom left origin, must have x, y, r & t keys.
    @result dict with x, y, w & h keys
    """

def setFlipbookDefaultOption(name: Any, value: Any) -> None:
    """Set a particular option to the given value. The type of the value differs per option, giving the wrong value may result in exceptions. The options are read every time the dialog is opened, though not every knob in the dialog has it's value stored."""

def setRenderDialogDefaultOption(name: Any, value: Any) -> None:
    """Set a particular option to the given value. The type of the value differs per option, giving the wrong value may result in exceptions. The options are read every time the dialog is opened, though not every knob in the dialog has it's value stored."""

def showExecuteDialog(nodesToExecute: Any, exceptOnError: bool = ...) -> None:
    """Present a dialog that executes the given list of nodes."""

def showFlipbookDialog(node: Any, takeNodeSettings: bool = ...) -> None:
    """Present a dialog that flipbooks the given node."""

def showFlipbookDialogForSelected() -> None:
    """Present a dialog that flipbooks the currently selected node."""

def showRenderDialog(nodesToRender: Any, exceptOnError: bool = ..., allowFrameServer: bool = ...) -> None:
    """Present a dialog that renders the given list of nodes."""

def showViewerCaptureDialog(node: Any) -> None: ...
