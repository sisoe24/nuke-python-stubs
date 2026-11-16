# Type stubs for nuke 15.2v9. Generated; do not edit.

"""This module defines new behavior (methods) for the Nuke Python API:
nuke.scriptNew, nuke.scriptClose and nuke.scriptExit
nuke.restoreWindowLayout and nuke.saveWindowLayout
"""

from typing import Any
import nuke_internal as _nuke_internal
from hiero.core.deprecated import deprecated as deprecated
import hiero as hiero
import nuke as nuke

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
