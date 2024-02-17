# Copyright (c) 2011 The Foundry Visionmongers Ltd.  All Rights Reserved.

import os
import typing
import threading
from typing import *

import ui
import core
import _nuke
import hiero
import PySide2
# the following are Hiero/Studio only things, check if the exports feature is enabled
import hiero.core
from ui import *
from PySide2 import QtGui, QtCore, QtWidgets
from _fnpython import (TimelineEditorCreationFlag, menuBar, activeView,
                       mainWindow, setWorkspace, saveWorkspace, activeSequence,
                       registerAction, currentWorkspace, getTimelineEditor,
                       registeredActions, findRegisteredAction,
                       findRegisteredActions, resetCurrentWorkspace)

from . import (CopyCuts, TagsMenu, SendToNuke, FnPosterFrameUI,
               ScanForVersions, FnReExportAction, LocalisationMenu,
               RenameTimelineShots, BuildExternalMediaTrack, nuke, nuke_bridge)
from .classes import *

if 'exports' in hiero.core.env['Features']:
    from .FnExporterBaseUI import TaskUIBase, RenderTaskUIBase
    from .FnProcessorUI import ProcessorUIBase
    from .FnExportUIRegistry import TaskUIRegistry, taskUIRegistry
    from .FnExporterBaseUI import InvalidOutputResolutionMessage

from foundry.ui import openFileBrowser

from . import FnViewerMethods
from .FnVersionWidget import VersionWidget

# Constants used to determine menu actions' visibilty
kContextProperty = 'ActiveContext'
kContextNone = 0
kContextStudio = 1
kContextTimeline = 2
kContextComp = 3

# Menus


def _addMenuActionR(path, action, menu, before=None):
    # Find first path element in menu
    name = path[0]
    for a in menu.actions():
        if name == a.objectName() or name == a.text():
            if len(path) <= 1:
                if before != None:
                    for b in a.menu().actions():
                        if before == b.objectName() or before == b.text():
                            a.menu().insertAction(b, action)
                            return True
                else:
                    a.menu().addAction(action)
                return True
            else:
                _addMenuActionR(path[1:], action, a.menu())
                return True
    # We didn't find the menu
    return False


def addMenuAction(path, action, before=None):
    """
    Add a QAction to the main menubar. The 'path' parameter specifies the menu to which to add the action as a '/'-separated string.
    The path may contain either internal action names or display names. e.g. 'View/Transform', or (better) 'foundry.menu.view/foundry.view.transform'."
    The optional 'before' parameter specifies the name of an item the action should be inserted before. If this is not specified, the action is appended to the menu.
    """
    return _addMenuActionR(path.split('/'), action, menuBar(), before)


def createMenuAction(name, method, icon=None, path=None):
    """
    Creates a menu action (QAction) for use in context menus or Main menubar.
    The 'name' parameter specifies the title of the action.

    @param: name - the title of the menu action
    @param: method - the Python method which this action triggers
    @param: icon (optional) - provides an icon for the action. This can be an absolute path ('/var/tmp/myIcon.png'), or relative path ('icons:myIcon.png')
    @param: path (optional) - the path to the menu action. The action objects name will be set to this value
    """

    action = QtWidgets.QAction(name, None)
    if icon:
        action.setIcon(QtGui.QIcon(icon))

    if path:
        action.setObjectName(path)

    action.triggered.connect(method)
    return action


def insertMenuAction(action, menu, before=None, after=None):
    """
    Insert a QAction into the given QMenu. If strings 'before' or 'after' are specified, the action is inserted before or after the action with that name.
    If no such action is found or 'before/after' are not given, the action is appended to the menu.
    """
    insert = False
    for a in menu.actions():
        if insert:
            menu.insertAction(a, action)
            return
        if before != None:
            if before == a.objectName() or before == a.text():
                menu.insertAction(a, action)
                return
        if after != None:
            if after == a.objectName() or after == a.text():
                insert = True
    menu.addAction(action)


def _findMenuActionR(name, menu):
    for a in menu.actions():
        if name == a.objectName() or name == a.text():
            return a
        if a.menu() != None:
            result = _findMenuActionR(name, a.menu())
            if result != None:
                return result
    return None


def findMenuAction(name):
    """
      Find a QAction in the main menubar. The 'name' parameter specifies the name of the action.
      The name may be either an internal action name or a display name. e.g. 'Cut', or (better) 'foundry.application.cut'."
      """
    return _findMenuActionR(name, menuBar())


def trackNameValidator():
    namepatternrx = QtCore.QRegExp('[a-z A-Z 0-9 . _ -]*')
    nameval = QtGui.QRegExpValidator(namepatternrx)
    return nameval


# Panels
_panels = dict()


def registerPanel(id, command):
    _panels[id] = command


def unregisterPanel(id, command):
    del _panels[id]


def restorePanel(id):
    try:
        return _panels[id]()
    except:
        log.debug("Can't restore panel '" + str(id) +
                  "' because it hasn't been registered.")
        return None


def getProjectRootInteractive(project):
    """ Try to get a valid root path from the project.  If the existing exportRootDirectory()
        is not set or doesn't exist, the user will be prompted to select one.  If no path
        is selected, returns None. """
    projectRoot = project.exportRootDirectory()

    # If the project root is not set or the directory doesn't exist, ask the user to select a path
    if not projectRoot or not hiero.core.util.filesystem.exists(projectRoot):
        fileList = openFileBrowser(
            caption='Please select a valid path for the Export Root', pattern='*/', mode=2, initialPath='/')
        if (fileList != None and len(fileList) > 0):
            projectRoot = fileList[0]
            project.setUseCustomExportDirectory(True)
            project.setCustomExportDirectory(projectRoot)
        else:
            projectRoot = None

    return projectRoot


# Python Menus and Actions
'''Stubs generated automatically from Nuke's internal interpreter.'''


# Constants

# Built-in methods

def Initialise() -> None:
    """

    """
    ...


def activeSequence() -> hiero.core.Sequence:
    """
    hiero.ui.activeSequence() -> gets the currently active sequence.

    @return: a hiero.core.Sequence of the last activated hiero.ui.TimelineEditor, hiero.ui.SpreadsheetView object or hiero.ui.Viewer object
    """
    ...


def activeView() -> int | float:
    """
    hiero.ui.activeView() -> gets the currently active view object.

    @return: depending on the active view, a hiero.ui.TimelineEditor, a hiero.ui.SpreadsheetView object, a hiero.ui.Viewer object or a hiero.ui.BinView object
    """
    ...


def browseForApplication(*args: typing.Any, **kwargs: typing.Any) -> str:
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


def getTimelineEditor(sequence: hiero.core.Sequence, creationFlag: Optional[hiero.ui.TimelineEditorCreationFlag] = None) -> hiero.ui.TimelineEditor:
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


def openFileBrowser(caption='', mode=1, pattern='', initialPath='', forSave=False, canChooseMultiple=False, sequencesEnabled=False, mayNotExist=False, showAllFileTypes=False, confirmOverwrite=True, requiredExtension='') -> list:
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


def openInNewViewer(*args: typing.Any, **kwargs: typing.Any) -> Viewer:
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


def openInTimeline(*args: typing.Any, **kwargs: typing.Any) -> int | float:
    """
    hiero.ui.openInTimeline( hiero.core.BinItem ) -> Opens a BinItem's activeItem (Clip/Sequence) in a Timeline View.
    hiero.ui.openInTimeline( hiero.core.Sequence ) -> Opens a Sequence in a Timeline View.
    hiero.ui.openInTimeline( hiero.core.Clip ) -> Opens a Clip in a Timeline View.
    @return: hiero.ui.TimelineEditor object
    hiero.ui.openInTimeline( [hiero.core.BinItem] ) -> Opens a list of BinItems' activeItems (Clips/Sequences) in a Timeline View.
    @return: tuple of hiero.ui.TimelineEditor objects
    """
    ...


def openInViewer(*args: typing.Any, **kwargs: typing.Any) -> Viewer:
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


def sendToViewerA(*args: typing.Any, **kwargs: typing.Any) -> Iterable:
    """
    hiero.ui.sendToViewerA( hiero.core.BinItem ) -> Sends a BinItem's activeItem (Clip/Sequence) to the Viewer A.
    hiero.ui.sendToViewerA( hiero.core.Sequence ) -> Sends a Sequence to the Viewer A.
    hiero.ui.sendToViewerA( hiero.core.Clip ) -> Sends a Clip to the Viewer A.
    """
    ...


def sendToViewerB(*args: typing.Any, **kwargs: typing.Any) -> Iterable:
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
