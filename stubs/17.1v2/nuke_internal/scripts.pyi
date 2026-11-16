# Type stubs for nuke 17.1v2. Generated; do not edit.

"""This module define the scriptSaveAndClear method for Nuke API.
nuke.scriptSaveAndClear will call nuke.scriptSave() if any changes were made and then calls nuke.scriptClear()
"""

from typing import Any

def scriptSaveAndClear(filename: Any = ..., ignoreUnsavedChanges: bool = ...) -> None:
    """scriptSaveAndClear(filename=None, ignoreUnsavedChanges=False) -> None
    Calls nuke.scriptSave and nuke.scriptClear
    @param filename: Save to this file name without changing the script name in the
     project.
    @param ignoreUnsavedChanges: Optional. If set to True scripSave will be called,
     ignoring any unsaved changes
    @return: True when sucessful. False if the user cancels the operation. In this
     case nuke.scripClear will not be called
 
    """
