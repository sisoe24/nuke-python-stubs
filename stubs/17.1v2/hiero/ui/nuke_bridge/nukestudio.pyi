# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import PySide6.QtGui as _PySide6_QtGui
import PySide6.QtWidgets as _PySide6_QtWidgets
import hiero.core as _hiero_core
import hiero.ui.nuke_bridge.add_effect as _hiero_ui_nuke_bridge_add_effect
import hiero.ui.nuke_bridge.hiero_state as _hiero_ui_nuke_bridge_hiero_state
import nuke as _nuke
from hiero.FnRedirect import currentWorkspace as currentWorkspace
from hiero.FnRedirect import menuBar as menuBar
from hiero.core import util as util
from hiero.core.FnCompSourceInfo import isNukeScript as isNukeScript
from hiero.core.nuke.NukeFunctionReplacement import nodeGraphExists as nodeGraphExists
from hiero.exporters import FnFrameServerRender as FnFrameServerRender
from hiero.ui import findMenuAction as findMenuAction
from hiero.ui import insertMenuAction as insertMenuAction
from hiero.ui.nuke_bridge import add_effect as add_effect
from hiero.ui.nuke_bridge import hiero_state as hiero_state
from hiero.ui.nuke_bridge.FnNsFrameServer import cancelFrames as cancelFrames
from hiero.ui.nuke_bridge.FnNsFrameServer import configureFrameServerFromCommandArgs as configureFrameServerFromCommandArgs
from hiero.ui.nuke_bridge.FnNsFrameServer import isServerRunning as isServerRunning
from hiero.ui.nuke_bridge.FnNsFrameServer import onFatalError as onFatalError
from hiero.ui.nuke_bridge.FnNsFrameServer import promptFrameServerKill as promptFrameServerKill
from hiero.ui.nuke_bridge.FnNsFrameServer import renderFrames as renderFrames
from hiero.ui.nuke_bridge.FnNsFrameServer import renderScript as renderScript
from hiero.ui.nuke_bridge.FnNsFrameServer import setBackgroundRenderer as setBackgroundRenderer
from hiero.ui.nuke_bridge.FnNsFrameServer import startServer as startServer
from hiero.ui.nuke_bridge.FnNsFrameServer import stopServer as stopServer
from hiero.ui.nuke_bridge.FnNsFrameServer import workerCount as workerCount
import hiero as hiero
import nukescripts as nukescripts

addEffectHandler: _hiero_ui_nuke_bridge_add_effect.AddEffectHandler
app: _PySide6_QtWidgets.QApplication
backgroundRenderObserver: _hiero_core.BackgroundRenderObserver
backgroundRenderer: Any
eventHandler: NukeStudioEventHandler
frameServer: Any
hieroRedoItem: _PySide6_QtGui.QAction
hieroState: _hiero_ui_nuke_bridge_hiero_state.HieroState
hieroUndoItem: _PySide6_QtGui.QAction
kAutoBackgroundRenderNeverValue: int
kAutoBackgroundRenderOnSaveCreateOrVersionValue: int
kAutoBackgroundRenderOnSaveValue: int
kAutoBackgroundRenderPrefKey: str
nukeCloseItem: _nuke.MenuItem
nukeMenuBar: _nuke.Menu
nukeOpenItem: _nuke.MenuItem
nukeRedoItem: _nuke.MenuItem
nukeSaveAsItem: _nuke.MenuItem
nukeSaveItem: _nuke.MenuItem
nukeUndoItem: _nuke.MenuItem
recentNukeActions: list
renderProgressObserver: _hiero_core.RenderProgressObserver
runningInGui: bool
saveAndReRenderAction: _PySide6_QtGui.QAction

class NukeStudioEventHandler:
    def __init__(self) -> None: ...
    def getNukeScriptPathFromItem(self, item: Any) -> Any:
        """Extract the path from the given item, and check if it points to a Nuke script.
        Returns None if no path was found or if it wasn't a Nuke script. 
        """
    def onContextChanged(self, event: Any) -> None: ...
    def onDoubleClick(self, event: Any) -> None: ...
    def openDAG(self, filePath: Any, fork: bool = ...) -> None:
        """Open a script in the DAG, or in a new Nuke process if fork is true.
        The caller should make sure the filePath is actually a valid Nuke script. 
        """

class OpenInNodeGraphAction(_PySide6_QtGui.QAction):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, studioEventHandler: Any, fork: Any) -> None: ...
    def doOpen(self) -> None: ...
    def eventHandler(self, event: Any) -> None: ...

def aboutToShowMenu() -> None: ...

def addNewScriptVersionToBin(previousFileName: Any, newFileName: Any) -> None: ...

def addNewScriptVersionToBinRec(bin: Any, previousFileName: Any, newFileName: Any) -> bool: ...

def appendNukeUserMenus() -> None:
    """Get nuke user created menus and add them so they appear at the end of the menu bar
    
    """

def autoBackgroundRenderOnScriptSave() -> bool:
    """Check if a script should be automatically re-rendered when the user saves normally. """

def hideAction(action: Any) -> None: ...

def hideNukeMenus() -> None: ...

def initDuplicateMenus(timelineMenuName: Any, nukeMenuName: Any) -> None: ...

def insertAction(action: Any, menu: Any, before: Any = ..., after: Any = ..., context: Any = ...) -> None: ...

def insertNukeAction(item: Any, menu: Any, before: Any = ..., after: Any = ..., context: Any = ...) -> None: ...

def makeScriptSaveAndReRenderAction() -> Any: ...

def mergeMenus() -> None: ...

def scriptSaveAndReRender() -> None:
    """Save the current nk script and queue background re-render of its frames. """

def setContext(action: Any, context: Any, recursive: Any) -> None: ...

def setMenuVisibility(focusInNuke: Any) -> None: ...

def setup() -> Any: ...

def setupMenus() -> Any: ...

def showViewer() -> None:
    """Show Viewer Window of the first Viewer Node from nuke.allNodes("Viewer") """

def updateMenuActionVisibility(action: Any, focusInNuke: Any) -> None:
    """Recursively set the visibility of menu actions based on their context,
    and whether keyboard focus is in a Nuke widget.
    """
