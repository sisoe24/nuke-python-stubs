# Type stubs for nuke 17.1v2. Generated; do not edit.

"""This module defines new behavior (methods) for the Nuke Python API:
nuke.scriptNew, nuke.scriptClose and nuke.scriptExit
nuke.restoreWindowLayout and nuke.saveWindowLayout
"""

from typing import Any
import nuke_internal as _nuke_internal
from hiero.core.deprecated import deprecated as deprecated
import hiero as hiero
import nuke as nuke

def nodeGraphExists() -> bool:
    """Returns True if a Node Graph (DAG) panel is present in the current workspace,
    False otherwise. Two cases are excluded:
    - Widgets stashed in the hidden parent during a workspace switch
      (fn_hiddenByWorkspace property set).
    - Floating Node Graph panels (w.window() != mainWindow, because DockWindow
      inherits QMainWindow so w.window() returns the DockWindow itself).
    A panel present as a background (non-active) tab is still counted — callers
    can use nuke.showDag() to bring it to the front.
    """

def restoreWorkspaceFunc(workspaceIndex: Any) -> None:
    """restoreWindowLayout(i) -> None.

    Restores a saved window layout.

    :param i: Layout number
    :return: None
    """

def saveWorkspaceFunc(workspaceIndex: Any = ...) -> None:
    """saveWindowLayout(i=-1) -> None

    Saves the current window layout.

    :param i: Optional layout index. If this is omitted or set to a negative value, save as the default layout.
    :return: None.
    """

def scriptExitReplacementFunc(*args: Any, **kwargs: Any) -> None:
    """Exit the Application if 'forceExit' is True, otherwise 'nuke.scriptSaveAndClear' will be called
    @param forceExit: Optional parameter. Forces the Application to close.
    @return: None.
    """

def scriptOpenReplacementFunc(filePath: Any) -> Any:
    """Opens a new script containing the contents of the named file."""

nukeScriptOpenOldMethod = _nuke_internal.scriptOpen
