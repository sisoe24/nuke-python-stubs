# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from typing import Callable
from typing import final
from typing_extensions import Self
import enum as _enum
import hiero.core as _hiero_core
import hiero.ui as _hiero_ui

class FnPySingleton:
    def __new__(type, *args: Any, **kwargs: Any) -> Self: ...

@final
class RunInMainThread:
    """RunInMainThread"""
    @classmethod
    def request(cls, arg1: Callable[..., Any] = ..., arg2: tuple = ..., arg3: dict = ..., arg4: Any = ..., /) -> Any: ...
    @classmethod
    def result(cls, *args: Any, **kwargs: Any) -> Any: ...

class SERedirector:
    def __init__(self, stream: Any) -> None: ...
    def close(self) -> None: ...
    def stream(self) -> Any: ...

class SESysStdErr(SERedirector, FnPySingleton):
    def write(self, out: Any) -> None: ...

class SESysStdIn(SERedirector, FnPySingleton):
    def readline(self) -> str: ...

class SESysStdOut(SERedirector, FnPySingleton):
    def write(self, out: Any) -> None: ...

class TimelineEditorCreationFlag(_enum.IntEnum):
    """An enumeration."""
    kDontCreate: TimelineEditorCreationFlag
    kForceCreation: TimelineEditorCreationFlag
    kRecycleOrCreate: TimelineEditorCreationFlag
    def __new__(cls, value: Any) -> Self: ...

def activeSequence() -> _hiero_core.Sequence | None:
    """hiero.ui.activeSequence() -> gets the currently active sequence.

    @return: a hiero.core.Sequence of the last activated hiero.ui.TimelineEditor, hiero.ui.SpreadsheetView object or hiero.ui.Viewer object
    """

def activeView() -> Any:
    """hiero.ui.activeView() -> gets the currently active view object.

    @return: depending on the active view, a hiero.ui.TimelineEditor, a hiero.ui.SpreadsheetView object, a hiero.ui.Viewer object or a hiero.ui.BinView object
    """

def application() -> Any:
    """Internal. Not for public use."""

def currentWorkspace() -> str:
    """hiero.ui.currentWorkspace() -> Returns the name of the current Workspace.

    @return: name of current Workspace as a string
    """

def findRegisteredAction(name: Any) -> Any:
    """hiero.ui.findRegisteredAction(name) -> Find the action with the given name.

    @return: a QAction, or None if not found.
    """

def findRegisteredActions(pattern: Any) -> Any:
    """hiero.ui.findRegisteredActions(pattern) -> Find the action that starts with the given pattern.

    @return: a QAction list or None on an error.
    """

def getActiveView() -> Any:
    """hiero.ui.activeView() -> gets the currently active view object.

    @return: depending on the active view, a hiero.ui.TimelineEditor, a hiero.ui.SpreadsheetView object, a hiero.ui.Viewer object or a hiero.ui.BinView object
    """

def getApplication() -> Any:
    """Internal. Not for public use."""

def getMainWindow() -> Any:
    """hiero.ui.getMainWindow() -> deprecated; please use hiero.ui.mainWindow() instead."""

def getMonitorOutStats() -> tuple[int, ...]: ...

def getPluginPath() -> tuple[str, ...]:
    """hiero.core.getPluginPath() -> deprecated; please use hiero.core.pluginPath instead."""

def getTimelineEditor(sequence: _hiero_core.Sequence, creationFlag: TimelineEditorCreationFlag = ...) -> _hiero_ui.TimelineEditor | None:
    """hiero.ui.getTimelineEditor(sequence, creationFlag) -> Find the TimelineEditor for the given Sequence. A new TimelineEditor may be created or an existing one may be recycled depending on the creationFlag parameter, see hiero.ui.TimelineEditorCreationFlag. If the optional creationFlag is not specified, the default behavior will recycle an existing TimelineEditor or create one i.e. hiero.ui.TimelineEditorCreationFlag.kRecycleOrCreate.

    @param sequence: A hiero.core.Sequence object
    @param creationFlag (Optional): Enum flag of type hiero.ui.TimelineEditorCreationFlag. This flag determines the behavior when a TimelineEditor is not found for the given Sequence.
    @return: a hiero.ui.TimelineEditor if one exist or is successfully created/recycled.
    """

def mainWindow() -> Any:
    """hiero.ui.mainWindow() -> used to get Hiero's main window object.

    @return: a PySide2.QtGui.QMainWindow object
    """

def menuBar() -> Any:
    """hiero.ui.menuBar() -> used to get Hiero's global menu bar.

    @return: a PySide2.QtGui.QMenuBar object
    """

def nonInteractiveHelp(object: Any = ...) -> None:
    """Non-interactive version of the built-in help function. This prevents the Nuke UI from freezing when Nuke is launched
    from an interactive terminal and help is used in the Script Editor.
    :param object: Show help for this object.
    """

def outputRedirector(arg1: str, /) -> Any:
    """Internal. Not for public use."""

def pluginPath() -> tuple[str, ...]:
    """hiero.core.pluginPath() -> Returns a tuple of the search paths used by Hiero to load Python scripts.

    @return: tuple of strings
    """

def registerAction(action: Any) -> Any:
    """hiero.ui.registerAction(action) -> Register an action."""

def registerWindow(*args: Any, **kwargs: Any) -> Any:
    """Internal. Not for public use."""

def registeredActions() -> list:
    """hiero.ui.registeredActions() -> Returns a list of all registered actions.

    @return: a tuple of QActions
    """

def resetCurrentWorkspace() -> None:
    """hiero.ui.resetCurrentWorkspace() -> Resets the current Workspace to its default state.

    @return: None
    """

def saveWorkspace(name: Any) -> None:
    """hiero.ui.saveWorkspace(name) -> Save the current Workspace with name.

    @return: None

    Example: hiero.ui.saveWorkspace('NewWorkspaceName')
    """

def setWorkspace(name: Any) -> None:
    """hiero.ui.setWorkspace(name) -> Sets the Workspace with name, as per the name in the Workspace menu.

    @return: None

    Example: hiero.ui.setWorkspace('Reviewing')
    """

def showCreateCompSpecialDialog(*args: Any, **kwargs: Any) -> Any:
    """Internal.  Not for public use."""

def stderrRedirector(arg1: str, /) -> Any:
    """Internal. Not for public use."""

def viewIconForTrack(arg1: Any, /) -> Any: ...
