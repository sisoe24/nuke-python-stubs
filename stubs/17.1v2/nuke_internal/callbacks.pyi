# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
from typing import Callable

afterBackgroundFrameRenders: list
afterBackgroundRenders: list
afterFrameRenders: dict
afterRenders: dict
afterUserAddGsvSets: list
afterUserAddGsvs: list
afterUserRemoveGsvSets: list
afterUserRemoveGsvs: list
afterUserRenameGsvSets: list
afterUserRenameGsvs: list
afterUserSetGsvValues: list
autoSaveDeleteFilters: dict
autoSaveFilters: dict
autoSaveRestoreFilters: dict
autolabels: dict
beforeBackgroundRenders: list
beforeFrameRenders: dict
beforeRenders: dict
beforeUserAddGsvSets: list
beforeUserAddGsvs: list
beforeUserRemoveGsvSets: list
beforeUserRemoveGsvs: list
beforeUserRenameGsvSets: list
beforeUserRenameGsvs: list
beforeUserSetGsvValues: list
filenameFilters: dict
knobChangeds: dict
onCreates: dict
onDestroys: dict
onScriptCloses: dict
onScriptLoads: dict
onScriptSaves: dict
onUserCreates: dict
renderProgresses: dict
updateUIs: dict
validateFilenames: dict

def addAfterBackgroundFrameRender(call: Any, args: Any = ..., kwargs: Any = ...) -> None:
    """Add code to execute after each frame of a background render.
    The call must be in the form of:
    def foo(context):
      pass

    The context object that will be passed in is a dictionary containing the following elements:
    id => The identifier for the task that's making progress
    frame => the current frame number being rendered
    numFrames => the total number of frames that is being rendered
    frameProgress => the number of frames rendered so far.

    Please be aware that the current Nuke context will not make sense in the callback (e.g. nuke.thisNode will return a random node).
    """

def addAfterBackgroundRender(call: Any, args: Any = ..., kwargs: Any = ...) -> None:
    """Add code to execute after any background renders.
    The call must be in the form of:
    def foo(context):
      pass

    The context object that will be passed in is a dictionary containing the following elements:
    id => The identifier for the task that's ended

    Please be aware that the current Nuke context will not make sense in the callback (e.g. nuke.thisNode will return a random node).
    """

def addAfterFrameRender(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add code to execute after each frame of a render"""

def addAfterRecording(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add code to execute after viewer recording"""

def addAfterRender(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add code to execute after any renders"""

def addAfterReplay(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add code to execute after viewer replay"""

def addAfterUserAddGsv(function: Callable[[Any], None]) -> bool:
    """addAfterUserAddGsv(function) -> bool

    Add a callback to be called after the user has added a GSV via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path.
    @type function: Callable[[path], None]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was added successfully.
    @rtype: bool
    """

def addAfterUserAddGsvSet(function: Callable[[Any], None]) -> bool:
    """addAfterUserAddGsvSet(function) -> bool

    Add a callback to be called after the user has added a GSV set via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path.
    @type function: Callable[[path], None]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was added successfully.
    @rtype: bool
    """

def addAfterUserRemoveGsv(function: Callable[[Any], None]) -> bool:
    """addAfterUserRemoveGsv(function) -> bool

    Add a callback to be called after the user removes a GSV via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path.
    @type function: Callable[[path], None]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was added successfully.
    @rtype: bool
    """

def addAfterUserRemoveGsvSet(function: Callable[[Any], None]) -> bool:
    """addAfterUserRemoveGsvSet(function) -> bool

    Add a callback to be called before the user removes a GSV set via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path.
    @type function: Callable[[path], None]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was added successfully.
    @rtype: bool
    """

def addAfterUserRenameGsv(function: Callable[[Any, Any], None]) -> bool:
    """addAfterUserRenameGsv(function) -> bool

    Add a callback to be called after the user renames a GSV via the UI or the
    python API.

    @param function:
      A callable function which takes parameters for the GSV path and new name.
    @type function: Callable[[path, name], None]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was added successfully.
    @rtype: bool
    """

def addAfterUserRenameGsvSet(function: Callable[[Any, Any], None]) -> bool:
    """addAfterUserRenameGsvSet(function) -> bool

    Add a callback to be called after the user renames a GSV set via the UI or the
    python API.

    @param function:
      A callable function which takes parameters for the GSV path and new name.
    @type function: Callable[[path, name], None]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was added successfully.
    @rtype: bool
    """

def addAfterUserSetGsvValue(function: Callable[[Any], None]) -> bool:
    """addAfterUserSetGsvValue(function) -> bool

    Add a callback to be called after the user has set a GSV value via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path.
    @type function: Callable[[path], None]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was added successfully.
    @rtype: bool
    """

def addAutoSaveDeleteFilter(filter: Any) -> None:
    """addAutoSaveDeleteFilter(filter) -> None

    Add a function to modify the autosave filename before Nuke attempts delete the autosave file.

    Look at rollingAutoSave.py in the nukescripts directory for an example of using the auto save filters.

    @param filter: A filter function.  The first argument to the filter is the current autosave filename.
    This function should return the filename to delete or return None if no file should be deleted.
    """

def addAutoSaveFilter(filter: Any) -> None:
    """addAutoSaveFilter(filter) -> None

    Add a function to modify the autosave filename before Nuke saves the current script on an autosave timeout.

    Look at rollingAutoSave.py in the nukescripts directory for an example of using the auto save filters.

    @param filter: A filter function.  The first argument to the filter is the current autosave filename.
    The filter should return the filename to save the autosave to.
    """

def addAutoSaveRestoreFilter(filter: Any) -> None:
    """addAutoSaveRestoreFilter(filter) -> None

    Add a function to modify the autosave restore file before Nuke attempts to restores the autosave file.

    Look at rollingAutoSave.py in the nukescripts directory for an example of using the auto save filters.

    @param filter: A filter function.  The first argument to the filter is the current autosave filename.
    This function should return the filename to load autosave from or it should return None if the autosave file should be ignored.
    """

def addAutolabel(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add code to execute on every node to produce the text to draw on it
    in the DAG. Any value other than None is converted to a string and used
    as the text. None indicates that previously-added functions should
    be tried
    """

def addBeforeBackgroundRender(call: Any, args: Any = ..., kwargs: Any = ...) -> None:
    """Add code to execute before starting any background renders.
    The call must be in the form of:
    def foo(context):
      pass

    The context object that will be passed in is a dictionary containing the following elements:
    id => The identifier for the task that's about to begin

    Please be aware that the current Nuke context will not make sense in the callback (e.g. nuke.thisNode will return a random node).
    """

def addBeforeFrameRender(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add code to execute before each frame of a render"""

def addBeforeRecording(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add code to execute before viewer recording"""

def addBeforeRender(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add code to execute before starting any renders"""

def addBeforeReplay(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add code to execute before viewer replay"""

def addBeforeUserAddGsv(function: Callable[[Any], bool]) -> bool:
    """addBeforeUserAddGsv(function) -> bool

    Add a callback to be called before the user has added a GSV via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path. If
      this function returns false, the gsv addition will be aborted.
    @type function: Callable[[path], bool]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was added successfully.
    @rtype: bool
    """

def addBeforeUserAddGsvSet(function: Callable[[Any], bool]) -> bool:
    """addBeforeUserAddGsvSet(function) -> bool

    Add a callback to be called after the user has added a GSV set via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path. If
      this function returns false, the gsv set addition will be aborted.
    @type function: Callable[[path], bool]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was added successfully.
    @rtype: bool
    """

def addBeforeUserRemoveGsv(function: Callable[[Any], bool]) -> bool:
    """addBeforeUserRemoveGsv(function) -> bool

    Add a callback to be called before the user removes a GSV via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path. If
      this function returns false, the gsv removal will be aborted.
    @type function: Callable[[path], bool]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was added successfully.
    @rtype: bool
    """

def addBeforeUserRemoveGsvSet(function: Callable[[Any], bool]) -> bool:
    """addBeforeUserRemoveGsvSet(function) -> bool

    Add a callback to be called before the user removes a GSV set via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path. If
      this function returns false, the gsv set removal will be aborted.
    @type function: Callable[[path], bool]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was added successfully.
    @rtype: bool
    """

def addBeforeUserRenameGsv(function: Callable[[Any, Any], bool]) -> bool:
    """addBeforeUserRenameGsv(function) -> bool

    Add a callback to be called before the user renames a GSV via the UI or the
    python API.

    @param function:
      A callable function which takes parameters for the GSV path and new name. If
      this function returns false, the gsv rename will be aborted.
    @type function: Callable[[path, name], bool]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was added successfully.
    @rtype: bool
    """

def addBeforeUserRenameGsvSet(function: Callable[[Any, Any], bool]) -> bool:
    """addBeforeUserRenameGsvSet(function) -> bool

    Add a callback to be called before the user renames a GSV set via the UI or the
    python API.

    @param function:
      A callable function which takes parameters for the GSV path and new name. If
      this function returns false, the gsv set rename will be aborted.
    @type function: Callable[[path, name], bool]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was added successfully.
    @rtype: bool
    """

def addBeforeUserSetGsvValue(function: Callable[[Any, Any], bool]) -> bool:
    """addBeforeUserSetGsvValue(function) -> bool

    Add a callback to be called before the user has set a GSV value via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path. If
      this function returns false, the gsv value modification will be aborted.
    @type function: Callable[[path, value], bool]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was added successfully.
    @rtype: bool
    """

def addFilenameFilter(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add a function to modify filenames before Nuke passes them to
    the operating system. The first argument to the function is the
    filename, and it should return the new filename. None is the same as
    returning the string unchanged. All added functions are called
    in backwards order.
    """

def addKnobChanged(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ..., node: Any = ...) -> None:
    """Add code to execute when any knob value changes
    The knob is available in nuke.thisKnob() and the node in nuke.thisNode().
    This callback is triggered for any knob change, including changes made
    programmatically and changes that occur even when the Properties panel
    is closed (such as node position changes in the DAG).
    This is also called with dummy knobs when the control panel is opened
    or when the inputs to the node changes.
    Use addUpdateUI() for periodic updates during idle time.
    """

def addOnCreate(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add code to execute when a node is created or undeleted"""

def addOnDestroy(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add code to execute when a node is destroyed"""

def addOnScriptClose(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add code to execute before a script is closed"""

def addOnScriptLoad(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add code to execute when a script is loaded"""

def addOnScriptSave(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add code to execute before a script is saved"""

def addOnUserCreate(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add code to execute when user creates a node"""

def addRenderProgress(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add code to execute when the progress bar updates during any renders"""

def addUpdateUI(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add code to execute on every node when things change. This is done
    during idle, you cannot rely on it being done before it starts updating
    the viewer
    """

def addValidateFilename(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add a function to validate a filename in Write nodes. The first argument
    is the filename and it should return a Boolean as to whether the filename is valid
    or not. If a callback is provided, it will control whether the Render button of Write nodes
    and the Execute button of WriteGeo nodes is enabled or not.
    """

def afterBackgroundFrameRender(context: Any) -> None: ...

def afterBackgroundRender(context: Any) -> None: ...

def afterFrameRender() -> None: ...

def afterRecording() -> None: ...

def afterRender() -> None: ...

def afterReplay() -> None: ...

def afterUserAddGsv(path: Any) -> None: ...

def afterUserAddGsvSet(path: Any) -> None: ...

def afterUserRemoveGsv(path: Any) -> None: ...

def afterUserRemoveGsvSet(path: Any) -> None: ...

def afterUserRenameGsv(path: Any, name: Any) -> None: ...

def afterUserRenameGsvSet(path: Any, name: Any) -> bool: ...

def afterUserSetGsvValue(path: Any) -> None: ...

def autoSaveDeleteFilter(filename: Any) -> Any:
    """Internal function.  Use addAutoSaveDeleteFilter to add a callback"""

def autoSaveFilter(filename: Any) -> Any:
    """Internal function.  Use addAutoSaveFilter to add a callback"""

def autoSaveRestoreFilter(filename: Any) -> Any:
    """Internal function.  Use addAutoSaveRestoreFilter to add a callback"""

def autolabel() -> None: ...

def beforeBackgroundRender(context: Any) -> None: ...

def beforeFrameRender() -> None: ...

def beforeRecording() -> None: ...

def beforeRender() -> None: ...

def beforeReplay() -> None: ...

def beforeUserAddGsv(path: Any) -> bool: ...

def beforeUserAddGsvSet(path: Any) -> None: ...

def beforeUserRemoveGsv(path: Any) -> bool: ...

def beforeUserRemoveGsvSet(path: Any) -> bool: ...

def beforeUserRenameGsv(path: Any, name: Any) -> bool: ...

def beforeUserRenameGsvSet(path: Any, name: Any) -> bool: ...

def beforeUserSetGsvValue(path: Any, value: Any) -> bool: ...

def filenameFilter(filename: Any) -> Any: ...

def knobChanged() -> None: ...

def onCreate() -> None: ...

def onDestroy() -> None: ...

def onScriptClose() -> None: ...

def onScriptLoad() -> None: ...

def onScriptSave() -> None: ...

def onUserCreate() -> None: ...

def removeAfterBackgroundFrameRender(call: Any, args: Any = ..., kwargs: Any = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeAfterBackgroundRender(call: Any, args: Any = ..., kwargs: Any = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeAfterFrameRender(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeAfterRecording(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeAfterRender(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeAfterReplay(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeAfterUserAddGsv(function: Callable[[Any], None]) -> bool:
    """removeAfterUserAddGsv(function) -> bool

    Remove a callback called after the user has added a GSV via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path.
    @type function: Callable[[path], None]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was removed successfully.
    @rtype: bool
    """

def removeAfterUserAddGsvSet(function: Callable[[Any], None]) -> bool:
    """removeAfterUserAddGsvSet(function) -> bool

    Remove a callback called after the user has added a GSV set via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path.
    @type function: Callable[[path], None]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was removed successfully.
    @rtype: bool
    """

def removeAfterUserRemoveGsv(function: Callable[[Any], None]) -> bool:
    """removeAfterUserRemoveGsv(function) -> bool

    Remove a callback called after the user removes a GSV via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path.
    @type function: Callable[[path], None]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was removed successfully.
    @rtype: bool
    """

def removeAfterUserRemoveGsvSet(function: Callable[[Any], None]) -> bool:
    """removeAfterUserRemoveGsvSet(function) -> bool

    Remove a callback called before the user removes a GSV set via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path.
    @type function: Callable[[path], None]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was removed successfully.
    @rtype: bool
    """

def removeAfterUserRenameGsv(function: Callable[[Any, Any], None]) -> bool:
    """removeAfterUserRenameGsv(function) -> bool

    Remove a callback called after the user renames a GSV via the UI or the
    python API.

    @param function:
      A callable function which takes parameters for the GSV path and new name.
    @type function: Callable[[path, name], None]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was removed successfully.
    @rtype: bool
    """

def removeAfterUserRenameGsvSet(function: Callable[[Any, Any], None]) -> bool:
    """removeAfterUserRenameGsvSet(function) -> bool

    Remove a callback called after the user renames a GSV set via the UI or the
    python API.

    @param function:
      A callable function which takes parameters for the GSV path and new name.
    @type function: Callable[[path, name], None]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was removed successfully.
    @rtype: bool
    """

def removeAfterUserSetGsvValue(function: Callable[[Any], None]) -> bool:
    """removeAfterUserSetGsvValue(function) -> bool

    Remove a callback called after the user has set a GSV value via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path.
    @type function: Callable[[path], None]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was removed successfully.
    @rtype: bool
    """

def removeAutoSaveDeleteFilter(filter: Any) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeAutoSaveFilter(filter: Any) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeAutoSaveRestoreFilter(filter: Any) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeAutolabel(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeBeforeBackgroundRender(call: Any, args: Any = ..., kwargs: Any = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeBeforeFrameRender(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeBeforeRecording(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeBeforeRender(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeBeforeReplay(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeBeforeUserAddGsv(function: Callable[[Any], bool]) -> bool:
    """removeBeforeUserAddGsv(function) -> bool

    Remove a callback called before the user has added a GSV via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path.
    @type function: Callable[[path], bool]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was removed successfully.
    @rtype: bool
    """

def removeBeforeUserAddGsvSet(function: Callable[[Any], bool]) -> bool:
    """removeBeforeUserAddGsvSet(function) -> bool

    Remove a callback called after the user has added a GSV set via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path.
    @type function: Callable[[path], bool]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was removed successfully.
    @rtype: bool
    """

def removeBeforeUserRemoveGsv(function: Callable[[Any], bool]) -> bool:
    """removeBeforeUserRemoveGsv(function) -> bool

    Remove a callback called before the user removes a GSV via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path.
    @type function: Callable[[path], bool]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was removed successfully.
    @rtype: bool
    """

def removeBeforeUserRemoveGsvSet(function: Callable[[Any], bool]) -> bool:
    """removeBeforeUserRemoveGsvSet(function) -> bool

    Remove a callback called before the user removes a GSV set via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path.
    @type function: Callable[[path], bool]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was removed successfully.
    @rtype: bool
    """

def removeBeforeUserRenameGsv(function: Callable[[Any, Any], bool]) -> bool:
    """removeBeforeUserRenameGsv(function) -> bool

    Remove a callback called before the user renames a GSV via the UI or the
    python API.

    @param function:
      A callable function which takes parameters for the GSV path and new name.
    @type function: Callable[[path, name], bool]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was removed successfully.
    @rtype: bool
    """

def removeBeforeUserRenameGsvSet(function: Callable[[Any, Any], bool]) -> bool:
    """removeBeforeUserRenameGsvSet(function) -> bool

    Remove a callback called before the user renames a GSV set via the UI or the
    python API.

    @param function:
      A callable function which takes parameters for the GSV path and new name.
    @type function: Callable[[path, name], bool]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was removed successfully.
    @rtype: bool
    """

def removeBeforeUserSetGsvValue(function: Callable[[Any, Any], bool]) -> bool:
    """removeBeforeUserSetGsvValue(function) -> bool

    Remove a callback called after the user has set a GSV value via the UI or the
    python API.

    @param function:
      A callable function which takes a single parameter for the GSV path.
    @type function: Callable[[path, value], bool]
    @raise TypeError: If a single callable parameter is not provided.
    @return: True if the callback was removed successfully.
    @rtype: bool
    """

def removeFilenameFilter(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeFilenameValidate(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback."""

def removeKnobChanged(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ..., node: Any = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeOnCreate(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeOnDestroy(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeOnScriptClose(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeOnScriptLoad(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeOnScriptSave(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeOnUserCreate(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeRenderProgress(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def removeUpdateUI(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""

def renderProgress() -> None: ...

def updateUI() -> None: ...

def validateFilename(filename: Any) -> bool: ...
