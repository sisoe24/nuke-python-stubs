'''Stubs generated automatically from Nuke's internal interpreter.'''
from typing import *
from numbers import Number

import ui
import core

from . import nuke
from .classes import *

# Constants

# Built-in methods
def Initialise() -> None:
    """

    """
    ...

def activeSequence() -> Iterable:
    """
    hiero.ui.activeSequence() -> gets the currently active sequence.

    @return: a hiero.core.Sequence of the last activated hiero.ui.TimelineEditor, hiero.ui.SpreadsheetView object or hiero.ui.Viewer object
    """
    ...

def activeView() -> Number:
    """
    hiero.ui.activeView() -> gets the currently active view object.

    @return: depending on the active view, a hiero.ui.TimelineEditor, a hiero.ui.SpreadsheetView object, a hiero.ui.Viewer object or a hiero.ui.BinView object
    """
    ...

def browseForApplication(*args, **kwargs) -> str:
    """
    hiero.ui.browseForApplication (message, initialPath, parentWidget) -> brings up the file browser to allow the user to select an application. Allows the user to select an executable file on Windows and Linux, and to select an application bundle (\*.app) directory on OSX.

    @param message: prompt to display to the user in the file browser
    @param initialPath: initial path to set the file browser to. Can be a zero length string
    @param parentWidget: QWidget to set as the parent of the file browser. Can be None.
    @return: string
    """
    ...

def currentContextMenuView() -> object:
    """
    hiero.ui.currentContextMenuView() -> returns the current view for the context menu. Only valid during a kShowContextMenu event callback.

    @return: hiero.ui.Viewer, hiero.ui.TimelineEditor, hiero.ui.BinView, depending on which window had the context menu created for it
    """
    ...

def currentViewer() -> ui.Viewer:
    """
    hiero.ui.currentViewer() -> returns the current viewer window.

    @return: hiero.ui.Viewer
    """
    ...

def currentWorkspace() -> str:
    """
    hiero.ui.currentWorkspace() -> Returns the name of the current Workspace.

    @return: name of current Workspace as a string
    """
    ...

def findRegisteredAction(name) -> None:
    """
    hiero.ui.findRegisteredAction(name) -> Find the action with the given name.

    @return: a QAction, or None if not found.
    """
    ...

def findRegisteredActions(pattern) -> list:
    """
    hiero.ui.findRegisteredActions(pattern) -> Find the action that starts with the given pattern.

    @return: a QAction list or None on an error.
    """
    ...

def flushAllViewersCache() -> None:
    """
    self.flushAllViewersCache() -> flush the cache of all viewers and pause caching
    """
    ...

def getFlipbook() -> ui.Viewer:
    """

    """
    ...

def getTimelineEditor(sequence:Iterable, creationFlag:Optional[Iterable] = None) -> Number:
    """
    hiero.ui.getTimelineEditor(sequence, creationFlag) -> Find the TimelineEditor for the given Sequence. A new TimelineEditor may be created or an existing one may be recycled depending on the creationFlag parameter, see hiero.ui.TimelineEditorCreationFlag. If the optional creationFlag is not specified, the default behavior will recycle an existing TimelineEditor or create one i.e. hiero.ui.TimelineEditorCreationFlag.kRecycleOrCreate.

    @param sequence: A hiero.core.Sequence object
    @param creationFlag (Optional): Enum flag of type hiero.ui.TimelineEditorCreationFlag. This flag determines the behavior when a TimelineEditor is not found for the given Sequence.
    @return: a hiero.ui.TimelineEditor if one exist or is successfully created/recycled.
    """
    ...

def isInAnyProject(arg__1: str) -> object:
    """

    """
    ...

def isInAnyTimeline(arg__1: str) -> object:
    """

    """
    ...

def mainWindow() -> Any:
    """
    hiero.ui.mainWindow() -> used to get Hiero's main window object.

    @return: a PySide2.QtGui.QMainWindow object
    """
    ...

def menuBar() -> Any:
    """
    hiero.ui.menuBar() -> used to get Hiero's global menu bar.

    @return: a PySide2.QtGui.QMenuBar object
    """
    ...

def monitorOutNode() -> object:
    """

    """
    ...

def openFileBrowser(caption="", mode=1, pattern="", initialPath="", forSave=False, canChooseMultiple=False, sequencesEnabled=False, mayNotExist=False, showAllFileTypes=False, confirmOverwrite=True, requiredExtension="") -> list:
    """
    openFileBrowser(caption="", mode=1, pattern="", initialPath="", forSave=False, canChooseMultiple=False, sequencesEnabled=False, mayNotExist=False, showAllFileTypes=False, confirmOverwrite=True, requiredExtension="") -> string list.

    Displays a modal foundry file browser dialog.

    @param caption: Optional. Message to display in the dialog.
    @param mode: Optional. Selection mode (1=Files Only, 2=Directories Only, 3=Files and Directories)
    @param pattern: Optional. File filter pattern.
    @param initialPath: Optional. The selected path on dialog creation.
    @param forSave: Optional. Configure dialog for saving a file.
    @param multipleSelection: Optional. Allow selection of multiple files.
    @param sequencesEnabled: Optional. Configure file browser for showing sequences.
    @param mayNotExist: Optional. Allow return of paths that don't exist e.g. for saving.
    @param showAllFileTypes: Optional. Show all files regardless of the filter.
    @param confirmOverwrite: Optional. If file exists will ask user to confirm overwrite. If canceled the file will not be in the returned list of paths.
    @param requiredExtension: Optional. Enforce a certain file extension.
    @return: The selected files as a list of strings
    """
    ...

def openInNewViewer(*args, **kwargs) -> Viewer:
    """
    hiero.ui.openInNewViewer( hiero.core.BinItem ) -> Opens a BinItem's activeItem (Clip/Sequence) in a new Viewer.
    hiero.ui.openInNewViewer( hiero.core.Sequence ) -> Opens a Sequence in a new Viewer.
    hiero.ui.openInNewViewer( hiero.core.Clip ) -> Opens a Clip in a new Viewer.
    @return: hiero.ui.Viewer object
    """
    ...

def openInOSShell(arg__1: str) -> object:
    """

    """
    ...

def openInSpreadsheet(sequence: core.Sequence) -> ui.SpreadsheetView:
    """
    hiero.ui.openInSpreadsheet( hiero.core.Sequence ) -> Opens a Sequence in a Spreadsheet.
    @return: hiero.ui.SpreadsheetView object
    """
    ...

def openInTimeline(*args, **kwargs) -> Number:
    """
    hiero.ui.openInTimeline( hiero.core.BinItem ) -> Opens a BinItem's activeItem (Clip/Sequence) in a Timeline View.
    hiero.ui.openInTimeline( hiero.core.Sequence ) -> Opens a Sequence in a Timeline View.
    hiero.ui.openInTimeline( hiero.core.Clip ) -> Opens a Clip in a Timeline View.
    @return: hiero.ui.TimelineEditor object
    hiero.ui.openInTimeline( [hiero.core.BinItem] ) -> Opens a list of BinItems' activeItems (Clips/Sequences) in a Timeline View.
    @return: tuple of hiero.ui.TimelineEditor objects
    """
    ...

def openInViewer(*args, **kwargs) -> Viewer:
    """
    hiero.ui.openInViewer( hiero.core.BinItem ) -> Opens a BinItem's activeItem (Clip/Sequence) in the Viewer.
    hiero.ui.openInViewer( hiero.core.Sequence ) -> Opens a Sequence in the Viewer.
    hiero.ui.openInViewer( hiero.core.Clip ) -> Opens a Clip in the Viewer.
    @return: hiero.ui.Viewer object
    """
    ...

def openProject(path: str, flags: int = 'Hiero.Python.Project.kProjectOpenNoFlags') -> core.Project:
    """

    """
    ...

def registerAction(action) -> Any:
    """
    hiero.ui.registerAction(action) -> Register an action.
    """
    ...

def registerBinViewCustomMimeDataType(arg__1: str) -> object:
    """
    hiero.ui.registerBinViewCustomMimeDataType(customMimeType) -> registers a custom mime type so that Hiero passes on drag and drop events through the event system. For an example of how to use this method, see the bin_drop.py example.
    """
    ...

def registeredActions() -> tuple:
    """
    hiero.ui.registeredActions() -> Returns a list of all registered actions.

    @return: a tuple of QActions
    """
    ...

def resetCurrentWorkspace() -> None:
    """
    hiero.ui.resetCurrentWorkspace() -> Resets the current Workspace to its default state.

    @return: None
    """
    ...

def saveWorkspace(name) -> None:
    """
    hiero.ui.saveWorkspace(name) -> Save the current Workspace with name.

    @return: None

    Example: hiero.ui.saveWorkspace('NewWorkspaceName')
    """
    ...

def sendToViewerA(*args, **kwargs) -> Iterable:
    """
    hiero.ui.sendToViewerA( hiero.core.BinItem ) -> Sends a BinItem's activeItem (Clip/Sequence) to the Viewer A.
    hiero.ui.sendToViewerA( hiero.core.Sequence ) -> Sends a Sequence to the Viewer A.
    hiero.ui.sendToViewerA( hiero.core.Clip ) -> Sends a Clip to the Viewer A.
    """
    ...

def sendToViewerB(*args, **kwargs) -> Iterable:
    """
    hiero.ui.sendToViewerB( hiero.core.BinItem ) -> Sends a BinItem's activeItem (Clip/Sequence) to the Viewer B.
    hiero.ui.sendToViewerB( hiero.core.Sequence ) -> Sends a Sequence to the Viewer B.
    hiero.ui.sendToViewerB( hiero.core.Clip ) -> Sends a Clip to the Viewer B.
    """
    ...

def setWorkspace(name) -> None:
    """
    hiero.ui.setWorkspace(name) -> Sets the Workspace with name, as per the name in the Workspace menu.

    @return: None

    Example: hiero.ui.setWorkspace('Reviewing')
    """
    ...

def unregisterBinViewCustomMimeDataType(arg__1: str) -> object:
    """
    hiero.ui.unregisterBinViewCustomMimeDataType(customMimeType) -> unregisters a custom mime type that was previously registered using hiero.ui.registerBinViewCustomMimeDataType().
    """
    ...

def updateViewer(oldClip: core.Clip, newClip: core.Clip) -> None:
    """

    """
    ...

def windowManager() -> object:
    """
    hiero.ui.windowManager() -> returns the single WindowManager object.

    @return: hiero.ui.WindowManager
    """
    ...
