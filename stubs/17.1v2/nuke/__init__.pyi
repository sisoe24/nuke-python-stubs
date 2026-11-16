# Type stubs for nuke 17.1v2. Generated; do not edit.

"""Set up the 'nuke' module

This initializes Nuke's internal modules and brings the symbols into this namespace
"""

from typing import Any
from typing import Callable
from typing import Sequence
from typing import SupportsFloat
from typing import final
from typing import overload
import PySide6.QtWidgets as _PySide6_QtWidgets
import hiero.core.nuke.NukeFunctionReplacement as _hiero_core_nuke_NukeFunctionReplacement
import nuke_internal.geo as _nuke_internal_geo
import nuke_internal.scripts as _nuke_internal_scripts
from nuke_internal import callbacks as callbacks
from nuke_internal import colorspaces as colorspaces
from nuke_internal import executeInMain as executeInMain
from nuke_internal import geo as geo
from nuke_internal import localization as localization
from nuke_internal import memory2 as memory2
from nuke_internal import overrides as overrides
from nuke_internal import rotopaint as rotopaint
from nuke_internal import scripts as scripts
from nuke_internal import splinewarp as splinewarp
from nuke_internal import utils as utils
from nuke_internal.callbacks import addAfterBackgroundFrameRender as addAfterBackgroundFrameRender
from nuke_internal.callbacks import addAfterBackgroundRender as addAfterBackgroundRender
from nuke_internal.callbacks import addAfterFrameRender as addAfterFrameRender
from nuke_internal.callbacks import addAfterRecording as addAfterRecording
from nuke_internal.callbacks import addAfterRender as addAfterRender
from nuke_internal.callbacks import addAfterReplay as addAfterReplay
from nuke_internal.callbacks import addAfterUserAddGsv as addAfterUserAddGsv
from nuke_internal.callbacks import addAfterUserAddGsvSet as addAfterUserAddGsvSet
from nuke_internal.callbacks import addAfterUserRemoveGsv as addAfterUserRemoveGsv
from nuke_internal.callbacks import addAfterUserRemoveGsvSet as addAfterUserRemoveGsvSet
from nuke_internal.callbacks import addAfterUserRenameGsv as addAfterUserRenameGsv
from nuke_internal.callbacks import addAfterUserRenameGsvSet as addAfterUserRenameGsvSet
from nuke_internal.callbacks import addAfterUserSetGsvValue as addAfterUserSetGsvValue
from nuke_internal.callbacks import addAutoSaveDeleteFilter as addAutoSaveDeleteFilter
from nuke_internal.callbacks import addAutoSaveFilter as addAutoSaveFilter
from nuke_internal.callbacks import addAutoSaveRestoreFilter as addAutoSaveRestoreFilter
from nuke_internal.callbacks import addAutolabel as addAutolabel
from nuke_internal.callbacks import addBeforeBackgroundRender as addBeforeBackgroundRender
from nuke_internal.callbacks import addBeforeFrameRender as addBeforeFrameRender
from nuke_internal.callbacks import addBeforeRecording as addBeforeRecording
from nuke_internal.callbacks import addBeforeRender as addBeforeRender
from nuke_internal.callbacks import addBeforeReplay as addBeforeReplay
from nuke_internal.callbacks import addBeforeUserAddGsv as addBeforeUserAddGsv
from nuke_internal.callbacks import addBeforeUserAddGsvSet as addBeforeUserAddGsvSet
from nuke_internal.callbacks import addBeforeUserRemoveGsv as addBeforeUserRemoveGsv
from nuke_internal.callbacks import addBeforeUserRemoveGsvSet as addBeforeUserRemoveGsvSet
from nuke_internal.callbacks import addBeforeUserRenameGsv as addBeforeUserRenameGsv
from nuke_internal.callbacks import addBeforeUserRenameGsvSet as addBeforeUserRenameGsvSet
from nuke_internal.callbacks import addBeforeUserSetGsvValue as addBeforeUserSetGsvValue
from nuke_internal.callbacks import addFilenameFilter as addFilenameFilter
from nuke_internal.callbacks import addKnobChanged as addKnobChanged
from nuke_internal.callbacks import addOnCreate as addOnCreate
from nuke_internal.callbacks import addOnDestroy as addOnDestroy
from nuke_internal.callbacks import addOnScriptClose as addOnScriptClose
from nuke_internal.callbacks import addOnScriptLoad as addOnScriptLoad
from nuke_internal.callbacks import addOnScriptSave as addOnScriptSave
from nuke_internal.callbacks import addOnUserCreate as addOnUserCreate
from nuke_internal.callbacks import addRenderProgress as addRenderProgress
from nuke_internal.callbacks import addUpdateUI as addUpdateUI
from nuke_internal.callbacks import addValidateFilename as addValidateFilename
from nuke_internal.callbacks import afterBackgroundFrameRender as afterBackgroundFrameRender
from nuke_internal.callbacks import afterBackgroundRender as afterBackgroundRender
from nuke_internal.callbacks import afterFrameRender as afterFrameRender
from nuke_internal.callbacks import afterRecording as afterRecording
from nuke_internal.callbacks import afterRender as afterRender
from nuke_internal.callbacks import afterReplay as afterReplay
from nuke_internal.callbacks import afterUserAddGsv as afterUserAddGsv
from nuke_internal.callbacks import afterUserAddGsvSet as afterUserAddGsvSet
from nuke_internal.callbacks import afterUserRemoveGsv as afterUserRemoveGsv
from nuke_internal.callbacks import afterUserRemoveGsvSet as afterUserRemoveGsvSet
from nuke_internal.callbacks import afterUserRenameGsv as afterUserRenameGsv
from nuke_internal.callbacks import afterUserRenameGsvSet as afterUserRenameGsvSet
from nuke_internal.callbacks import afterUserSetGsvValue as afterUserSetGsvValue
from nuke_internal.callbacks import autoSaveDeleteFilter as autoSaveDeleteFilter
from nuke_internal.callbacks import autoSaveFilter as autoSaveFilter
from nuke_internal.callbacks import autoSaveRestoreFilter as autoSaveRestoreFilter
from nuke_internal.callbacks import autolabel as autolabel
from nuke_internal.callbacks import beforeBackgroundRender as beforeBackgroundRender
from nuke_internal.callbacks import beforeFrameRender as beforeFrameRender
from nuke_internal.callbacks import beforeRecording as beforeRecording
from nuke_internal.callbacks import beforeRender as beforeRender
from nuke_internal.callbacks import beforeReplay as beforeReplay
from nuke_internal.callbacks import beforeUserAddGsv as beforeUserAddGsv
from nuke_internal.callbacks import beforeUserAddGsvSet as beforeUserAddGsvSet
from nuke_internal.callbacks import beforeUserRemoveGsv as beforeUserRemoveGsv
from nuke_internal.callbacks import beforeUserRemoveGsvSet as beforeUserRemoveGsvSet
from nuke_internal.callbacks import beforeUserRenameGsv as beforeUserRenameGsv
from nuke_internal.callbacks import beforeUserRenameGsvSet as beforeUserRenameGsvSet
from nuke_internal.callbacks import beforeUserSetGsvValue as beforeUserSetGsvValue
from nuke_internal.callbacks import filenameFilter as filenameFilter
from nuke_internal.callbacks import knobChanged as knobChanged
from nuke_internal.callbacks import onCreate as onCreate
from nuke_internal.callbacks import onDestroy as onDestroy
from nuke_internal.callbacks import onScriptClose as onScriptClose
from nuke_internal.callbacks import onScriptLoad as onScriptLoad
from nuke_internal.callbacks import onScriptSave as onScriptSave
from nuke_internal.callbacks import onUserCreate as onUserCreate
from nuke_internal.callbacks import removeAfterBackgroundFrameRender as removeAfterBackgroundFrameRender
from nuke_internal.callbacks import removeAfterBackgroundRender as removeAfterBackgroundRender
from nuke_internal.callbacks import removeAfterFrameRender as removeAfterFrameRender
from nuke_internal.callbacks import removeAfterRecording as removeAfterRecording
from nuke_internal.callbacks import removeAfterRender as removeAfterRender
from nuke_internal.callbacks import removeAfterReplay as removeAfterReplay
from nuke_internal.callbacks import removeAfterUserAddGsv as removeAfterUserAddGsv
from nuke_internal.callbacks import removeAfterUserAddGsvSet as removeAfterUserAddGsvSet
from nuke_internal.callbacks import removeAfterUserRemoveGsv as removeAfterUserRemoveGsv
from nuke_internal.callbacks import removeAfterUserRemoveGsvSet as removeAfterUserRemoveGsvSet
from nuke_internal.callbacks import removeAfterUserRenameGsv as removeAfterUserRenameGsv
from nuke_internal.callbacks import removeAfterUserRenameGsvSet as removeAfterUserRenameGsvSet
from nuke_internal.callbacks import removeAfterUserSetGsvValue as removeAfterUserSetGsvValue
from nuke_internal.callbacks import removeAutoSaveDeleteFilter as removeAutoSaveDeleteFilter
from nuke_internal.callbacks import removeAutoSaveFilter as removeAutoSaveFilter
from nuke_internal.callbacks import removeAutoSaveRestoreFilter as removeAutoSaveRestoreFilter
from nuke_internal.callbacks import removeAutolabel as removeAutolabel
from nuke_internal.callbacks import removeBeforeBackgroundRender as removeBeforeBackgroundRender
from nuke_internal.callbacks import removeBeforeFrameRender as removeBeforeFrameRender
from nuke_internal.callbacks import removeBeforeRecording as removeBeforeRecording
from nuke_internal.callbacks import removeBeforeRender as removeBeforeRender
from nuke_internal.callbacks import removeBeforeReplay as removeBeforeReplay
from nuke_internal.callbacks import removeBeforeUserAddGsv as removeBeforeUserAddGsv
from nuke_internal.callbacks import removeBeforeUserAddGsvSet as removeBeforeUserAddGsvSet
from nuke_internal.callbacks import removeBeforeUserRemoveGsv as removeBeforeUserRemoveGsv
from nuke_internal.callbacks import removeBeforeUserRemoveGsvSet as removeBeforeUserRemoveGsvSet
from nuke_internal.callbacks import removeBeforeUserRenameGsv as removeBeforeUserRenameGsv
from nuke_internal.callbacks import removeBeforeUserRenameGsvSet as removeBeforeUserRenameGsvSet
from nuke_internal.callbacks import removeBeforeUserSetGsvValue as removeBeforeUserSetGsvValue
from nuke_internal.callbacks import removeFilenameFilter as removeFilenameFilter
from nuke_internal.callbacks import removeFilenameValidate as removeFilenameValidate
from nuke_internal.callbacks import removeKnobChanged as removeKnobChanged
from nuke_internal.callbacks import removeOnCreate as removeOnCreate
from nuke_internal.callbacks import removeOnDestroy as removeOnDestroy
from nuke_internal.callbacks import removeOnScriptClose as removeOnScriptClose
from nuke_internal.callbacks import removeOnScriptLoad as removeOnScriptLoad
from nuke_internal.callbacks import removeOnScriptSave as removeOnScriptSave
from nuke_internal.callbacks import removeOnUserCreate as removeOnUserCreate
from nuke_internal.callbacks import removeRenderProgress as removeRenderProgress
from nuke_internal.callbacks import removeUpdateUI as removeUpdateUI
from nuke_internal.callbacks import renderProgress as renderProgress
from nuke_internal.callbacks import updateUI as updateUI
from nuke_internal.callbacks import validateFilename as validateFilename
from nuke_internal.colorspaces import ColorspaceLookupError as ColorspaceLookupError
from nuke_internal.colorspaces import addDefaultColorspaceMapper as addDefaultColorspaceMapper
from nuke_internal.colorspaces import defaultColorspaceMapper as defaultColorspaceMapper
from nuke_internal.colorspaces import getColorspaceList as getColorspaceList
from nuke_internal.colorspaces import removeDefaultColorspaceMapper as removeDefaultColorspaceMapper
from nuke_internal.executeInMain import executeInMainThread as executeInMainThread
from nuke_internal.executeInMain import executeInMainThreadWithResult as executeInMainThreadWithResult
from nuke_internal.overrides import dependencies as dependencies
from nuke_internal.overrides import dependentNodes as dependentNodes
from nuke_internal.overrides import pluginAddPath as pluginAddPath
from nuke_internal.overrides import pluginAppendPath as pluginAppendPath
from nuke_internal.overrides import selectConnectedNodes as selectConnectedNodes
from nuke_internal.scripts import scriptSaveAndClear as scriptSaveAndClear
from nuke_internal.utils import FnPySingleton as FnPySingleton
from nuke_internal.utils import loadModuleFromPath as loadModuleFromPath
from nuke_internal.utils import script_directory as script_directory

ADD_VIEWS: int
AFTER_CONST: int
AFTER_LINEAR: int
ALL: int
ALWAYS_SAVE: int
BEFORE_CONST: int
BEFORE_LINEAR: int
BREAK: int
CATMULL_ROM: int
CONSTANT: int
CUBIC: int
DISABLED: int
DONT_CREATE_VIEWS: int
DONT_SAVE_TO_NODEPRESET: int
DO_NOT_READ: int
DO_NOT_WRITE: int
ENDLINE: int
EXE_PATH: str
EXPAND_TO_WIDTH: int
EXPRESSIONS: int
FLAGS_LOCKED: int
FLOAT: int
FONT: int
GEO: int
GUI: bool
HIDDEN_INPUTS: int
HORIZONTAL: int
IMAGE: int
INPUTS: int
INT16: int
INT8: int
INTERACTIVE: bool
INVALIDHINT: int
INVISIBLE: int
KNOB_CHANGED_ALWAYS: int
KNOB_CHANGED_RECURSIVE: int
KNOB_CHANGED_RIGHTCONTEXT: int
LINEAR: int
LINKINPUTS: int
LINKNODE_INPUTS: int
LIVEGROUP_CALLBACK_CAN_MAKE_EDITABLE: str
LIVEGROUP_CALLBACK_CAN_PUBLISH: str
LIVEGROUP_CALLBACK_MADE_EDITABLE: str
LIVEGROUP_CALLBACK_PUBLISHED: str
LIVEGROUP_CALLBACK_RELOADED: str
LOG: int
MATCH_CLASS: int
MATCH_COLOR: int
MATCH_LABEL: int
MONITOR: int
NODIR: int
NOREADERWRITER: int
NO_ANIMATION: int
NO_CHECKMARKS: int
NO_MULTIVIEW: int
NO_POSTAGESTAMPS: bool
NO_UNDO: int
NUKE_VERSION_DATE: str
NUKE_VERSION_MAJOR: int
NUKE_VERSION_MINOR: int
NUKE_VERSION_PHASE: str
NUKE_VERSION_PHASENUMBER: int
NUKE_VERSION_RELEASE: int
NUKE_VERSION_STRING: str
NUM_CPUS: int
NUM_INTERPOLATIONS: int
PLUGIN_EXT: str
PRECOMP_CALLBACK_OPENED: str
PREPEND: int
PROFILE_ENGINE: int
PROFILE_REQUEST: int
PROFILE_STORE: int
PROFILE_VALIDATE: int
PYTHON: int
READ_ONLY: int
READ_ONLY_IN_SCRIPTS: int
REGISTERED: int
REPLACE: int
REPLACE_VIEWS: int
SAVE_MENU: int
SCRIPT: int
SINGLE_SELECTION_ONLY: int
SMOOTH: int
STARTLINE: int
STORE_INTEGER: int
STRING_EXPAND_FILENAME: int
STRING_EXPAND_FILENUMBER: int
STRIP_CASCADE_PREFIX: int
TABBEGINCLOSEDGROUP: int
TABBEGINGROUP: int
TABENDGROUP: int
TABKNOB: int
THREADS: int
TO_SCRIPT: int
TO_VALUE: int
USER_SET_SLOPE: int
VIEWER: int
VIEW_NAMES: str
WRITE_ALL: int
WRITE_NON_DEFAULT_ONLY: int
WRITE_USER_KNOB_DEFS: int
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
defaultLUTMappers: dict
env: GlobalsEnvironment
filenameFilters: dict
importName: str
knobChangeds: dict
nodes: Nodes
nukeName: str
onCreates: dict
onDestroys: dict
onScriptCloses: dict
onScriptLoads: dict
onScriptSaves: dict
onUserCreates: dict
rawArgs: list
renderProgresses: dict
untitled: str
updateUIs: dict
validateFilenames: dict

class Knob:
    """A modifiable control that appears (unless hidden) in the panel for a node.
    This is a base class that specific knob types inherit from.

    Knobs can be animated, have expressions, be disabled or hidden and more.
    """
    def Class(self) -> str:
        """self.Class() -> Class name.
        @return: Class name.
        """
    def ClassID(self) -> int:
        """self.ClassID() -> Class ID.
        @return: Class ID.
        """
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def clearAnimated(self, *args: Any, **kwargs: Any) -> Any:
        """Clear animation for channel 'c'. Return True if successful."""
    def clearFlag(self, f: Any) -> None:
        """self.clearFlag(f) -> None.
        Clear flag.
        @param f: Flag.
        @return: None.
        """
    def critical(self, message: str) -> None:
        """self.critical(message) -> None.
        @param message: message to put the knob in error, and do a popup.
        @return: None.
        """
    def debug(self, message: str) -> None:
        """self.debug(message) -> None.
        @param message: message to put out to the error console, attached to the knob, if the verbosity level is set high enough.
        @return: None.
        """
    def enabled(self) -> bool:
        """self.enabled() -> Boolean.

        @return: True if the knob is enabled, False if it's disabled.
        """
    def error(self, message: str) -> None:
        """self.error(message) -> None.
        @param message: message to put the knob in error.
        @return: None.
        """
    def fromScript(self, arg1: str, /) -> Any:
        """Initialise from script."""
    def fullyQualifiedName(self, channel: int = ...) -> str:
        """self.fullyQualifiedName(channel=-1) -> string
        Returns the fully-qualified name of the knob within the node. This can be useful for expression linking.

        @param channel: Optional parameter, specifies the channel number of the sub-knob (for example, channels of  0 and 1 would refer to the x and y of a XY_Knob respectively), leave blank or set to -1 to get the  qualified name of the knob only.
        @return: The string of the qualified knob or sub-knob, which can be used directly in expression links.
        """
    def getAuthorMode(self) -> int:
        """self.getAuthorMode() -> Integer.
        Returns the authoring mode currently set on the knob. This is a unique string identifier of the option, which is also used for serialisation and deserialisation. It is not meant to change,thus one can rely on it.
        @return: The string identifier of the current authoring mode set.
        """
    def getAuthorModes(self) -> list:
        """self.getAuthorModes() -> List.
        Returns the names of the authoring modes of the knob if the knob is an authoring knob, otherwise an empty list.
        @return: The names of the authoring modes of the knob if the knob is an authoring knob, otherwise an empty list. This is a list of strings.
        """
    def getDerivative(self, arg1: float, arg2: int = ..., /) -> Any:
        """Return derivative at time 't' for channel 'c'."""
    def getFlag(self, f: int) -> bool:
        """self.getFlag(f) -> Bool.
        Returns whether the input flag is set.
        @param f: Flag.
        @return: True if set, False otherwise.
        """
    def getIntegral(self, arg1: float, arg2: float, arg3: int = ..., /) -> Any:
        """Return integral at the interval [t1, t2] for channel 'c'."""
    def getKeyIndex(self, arg1: float, arg2: int = ..., /) -> Any:
        """Return keyframe index at time 't' for channel 'c'."""
    def getKeyList(self) -> list:
        """Get all unique keys on the knob.  Returns list."""
    def getKeyTime(self, arg1: int, arg2: int = ..., /) -> Any:
        """Return index of the keyframe at time 't' for channel 'c'."""
    def getNthDerivative(self, arg1: int, arg2: float, arg3: int = ..., /) -> Any:
        """Return nth derivative at time 't' for channel 'c'."""
    def getNumKeys(self, arg1: int = ..., /) -> int:
        """Return number of keyframes for channel 'c'."""
    def getValue(self, arg1: int = ..., arg2: Any = ..., arg3: Any = ..., /) -> Any:
        """Return value at the current frame for channel 'c'."""
    def getValueAt(self, arg1: float, arg2: int = ..., arg3: Any = ..., /) -> Any:
        """Return value at time 't' for channel 'c'."""
    def hasExpression(self, index: int = ...) -> bool:
        """self.hasExpression(index=-1) -> bool
        Return True if animation at index 'index' has an expression.
        @param index: Optional index parameter. Defaults to -1 if not specified. This can be specified as a keyword parameter if desired.
        @return: True if has expression, False otherwise.
        """
    def isAnimated(self, arg1: int = ..., arg2: Any = ..., /) -> bool:
        """Return True if channel 'c' is animated."""
    def isKey(self, arg1: int = ..., arg2: Any = ..., /) -> bool:
        """Return True if there is a keyframe at the current frame for channel 'c'."""
    def isKeyAt(self, arg1: float, arg2: int = ..., arg3: Any = ..., /) -> Any:
        """Return True if there is a keyframe at time 't' for channel 'c'."""
    def label(self) -> str:
        """self.label() -> label.
        @return: label.
        """
    def makeWidget(self) -> _PySide6_QtWidgets.QWidget:
        """self.makeWidget() -> PySide6.QtWidgets.QWidget.
        Returns an instance of the QWidget subclass used to edit the knob's value.
        The widget will update the knob's value when its value changes and should
        update its displayed value(s) when they change on the knob.
        Can return null if no widget should be created for the knob.
        @return: PySide6.QtWidgets.QWidget.
        """
    def name(self) -> str:
        """self.name() -> name.
        @return: name.
        """
    def node(self) -> Node:
        """self.node() -> nuke.Node
        Return the node that this knob belongs to. If the node has been cloned, we'll always return a reference to the original.
        @return: The node which owns this knob, or None if the knob has no owner yet.
        """
    def notDefault(self) -> bool:
        """self.notDefault() -> True if any of the values is not set to the default, False otherwise.
        @return: True if any of the values is not set to the default, False otherwise.
        """
    def removeKey(self, *args: Any, **kwargs: Any) -> Any:
        """Remove key for channel 'c'. Return True if successful."""
    def removeKeyAt(self, *args: Any, **kwargs: Any) -> Any:
        """Remove key at time 't' for channel 'c'. Return True if successful."""
    def resetToDefault(self, *args: Any, **kwargs: Any) -> Any:
        """self.resetToDefault() set the knob value back to its default, removing all animations."""
    def setAnimated(self, arg1: int = ..., arg2: Any = ..., /) -> bool:
        """Set channel 'c' to be animated."""
    def setAuthorMode(self, authorMode: Any) -> None:
        """self.setAuthorMode(authorMode) -> None.
        Sets the authoring mode on the knob. This accepts both the unique string identifier, which is also used for serialisation and deserialisation, or index of the option for convenience. These values are not meant to change, thus one can rely on them.
        @param authorMode: The string identifier or index of the authoring mode.
        @return: None.
        """
    def setEnabled(self, enabled: bool) -> None:
        """self.setEnabled(enabled) -> None.

        Enable or disable the knob.
        @param enabled: True to enable the knob, False to disable it.
        """
    def setExpression(self, expression: str, channel: int = ..., view: str | int | View = ...) -> bool:
        """self.setExpression(expression, channel=-1, view=None) -> bool
        Set the expression for a knob. You can optionally specify a channel to set the expression for.

        @param expression: The new expression for the knob. This should be a string.
        @param channel: Optional parameter, specifying the channel to set the expression for. This should be an integer.
        @param view: Optional view parameter. Without, this command will set the expression for the current view theinterface is displaying. Can be the name of the view or the index.
        @return: True if successful, False if not.
        """
    def setFlag(self, f: int) -> None:
        """self.setFlag(f) -> None.
        Logical OR of the argument and existing knob flags.
        @param f: Flag.
        @return: None.
        """
    def setLabel(self, s: str | None) -> None:
        """self.setLabel(s) -> None.
        @param s: New label.
        @return: None.
        """
    def setName(self, s: str) -> None:
        """self.setName(s) -> None.
        @param s: New name.
        @return: None.
        """
    def setTooltip(self, s: str) -> None:
        """self.setTooltip(s) -> None.
        @param s: New tooltip.
        @return: None.
        """
    def setValue(self, val: Any, chan: Any = ..., arg3: Any = ...) -> bool:
        """self.setValue(val, chan) -> bool

        Sets the value 'val' at channel 'chan'.
        @return: True if successful, False if not.
        """
    def setValueAt(self, val: float, time: float, chan: int = ..., arg4: Any = ...) -> bool:
        """self.setValueAt(val, time, chan) -> bool

        Sets the value 'val' at channel 'chan' for time 'time'.
        @return: True if successful, False if not.
        """
    def setVisible(self, visible: bool) -> None:
        """self.setVisible(visible) -> None.

        Show or hide the knob.
        @param visible: True to show the knob, False to hide it.
        """
    def toScript(self, quote: Any = ..., context: OutputContext | None = ...) -> str:
        """toScript(quote, context=current) -> string.

        Return the value of the knob in script syntax.
        Pass True for quote to return results quoted in {}.
        Pass None for context to get results for all views and key times (as stored in a .nk file).
        """
    def toScriptPrefix(self) -> str:
        """self.toScriptPrefix() -> string
        Write commands that must be executed before the to_script() value can be parsed. This is used to write commands to declare Layers and Formats and other objects that are shared by knobs.
        """
    def tooltip(self) -> str:
        """self.tooltip() -> tooltip.
        @return: tooltip.
        """
    def value(self, *args: Any, **kwargs: Any) -> Any:
        """Return value at the current frame for channel 'c'."""
    def visible(self) -> bool:
        """self.visible() -> Boolean.

        @return: True if the knob is visible, False if it's hidden.
        """
    def warning(self, message: str) -> None:
        """self.warning(message) -> None.
        @param message: message to put a warning on the knob.
        @return: None.
        """

class Array_Knob(Knob):
    """A knob which holds an array of values."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def animation(self, chan: int, view: str | int | View = ...) -> AnimationCurve | None:
        """self.animation(chan, view) -> AnimationCurve or None.
        Return the AnimationCurve for the  channel 'chan' and view 'view'. The view argument is optional.
        @param channel: The channel index.
        @param view: Optional view.
        @return: AnimationCurve or None.
        """
    def animations(self, view: str | int | View = ...) -> list:
        """self.animations(view) -> AnimationCurve list.
        @param view: Optional view.
        @return: AnimationCurve list.
        Example:
        b = nuke.nodes.Blur()
        k = b['size']
        k.setAnimated(0)
        a = k.animations()
        a[0].setKey(0, 11)
        a[0].setKey(10, 20)
        """
    def array(self, arg1: str | int | View = ...) -> list[float]:
        """self.array() -> List of knob values.
        @return: List of knob values.
        Should only be used for knobs that are neither animated
        nor get their values from a ValueProvider.
        For knobs like that, use Array_Knob.getValue, instead
        """
    def arraySize(self) -> int:
        """self.arraySize() -> Number of elements in array.
        @return: Number of elements in array.
        """
    def clearAnimated(self, index: Any = ..., view: Any = ...) -> bool:
        """self.clearAnimated(index, view) -> True if succeeded, False otherwise.
        Delete animation.
        @param index: Optional index.
        @param view: Optional view.
        @return: True if succeeded, False otherwise.
        """
    def copyAnimation(self, channel: Any, curve: AnimationCurve, view: Any = ...) -> None:
        """self.copyAnimation(channel, curve, view) -> None.
        Copies the i'th channel of the AnimationCurve curve to this object. The view is optional and defaults to the current view.
        @param channel: The channel index.
        @param curve: AnimationCurve.
        @param view: Optional view. Defaults to current.
        @return: None.
        """
    def copyAnimations(self, curves: Any, view: Any = ...) -> None:
        """self.copyAnimations(curves, view) -> None.
        Copies the AnimationCurves from curves to this object. The view is optional and defaults to the current view.
        @param curves: AnimationCurve list.
        @param view: Optional view. Defaults to current.
        @return: None.
        """
    def defaultValue(self) -> float:
        """self.defaultValue() -> Default value.
        @return: Default value.
        """
    def deleteAnimation(self, curve: Any) -> None:
        """self.deleteAnimation(curve) -> None. Raises ValueError if not found.
        Deletes the AnimationCurve.
        @param curve: An AnimationCurve instance which belongs to this Knob.
        @return: None. Raises ValueError if not found.
        """
    def dimensions(self) -> int:
        """self.dimensions() -> Dimensions in array.
        @return: Dimensions in array.
        """
    def frame(self) -> float:
        """self.frame() -> Frame number.
        @return: Frame number.
        """
    def fromScript(self, s: str) -> bool:
        """self.fromScript(s) -> True if successful, False otherwise.
        Set value of the knob to a user defined script (TCL syntax, as in .nk file). Return True if successful.
        @param s: Nuke script to be set on knob.
        @return: True if successful, False otherwise.
        """
    def getDerivative(self, arg1: float, arg2: int = ..., /) -> Any:
        """Return derivative at time 't' and index 'i'."""
    def getIntegral(self, arg1: float, arg2: float, arg3: int = ..., /) -> Any:
        """Return integral at time interval [t1, t2] and index 'i'."""
    def getKeyIndex(self, arg1: float, arg2: int = ..., /) -> Any:
        """Return index of the keyframe at time 't' and channel 'c'."""
    def getKeyTime(self, arg1: int, arg2: int = ..., /) -> Any:
        """Return time of the keyframe at time 't' and channel 'c'."""
    def getNthDerivative(self, arg1: int, arg2: float, arg3: int = ..., /) -> Any:
        """Return n'th derivative at time 't' and index 'i'."""
    def getNumKeys(self, arg1: int = ..., /) -> int:
        """Return number of keys at channel 'c'."""
    def getValue(self, arg1: int = ..., arg2: str | int | View = ..., arg3: float = ..., /) -> Any:
        """self.value(index, view, time) -> Floating point or List of floating point values (in case some are different).
        @param index: Optional index. Default is 0.
        @param view: Optional view.
        @param time: Optional time.
        @return: Floating point or List of floating point values (in case some are different).
        """
    def getValueAt(self, arg1: float = ..., arg2: int = ..., arg3: str | int | View = ..., /) -> Any:
        """self.valueAt(time, index, view) -> Floating point or List of floating point values (in case some are different).
        Return value for this knob at specified time, optional index and view.
        @param time: Time.
        @param index: Optional index. Default is 0.
        @param view: Optional view.
        @return: Floating point or List of floating point values (in case some are different).
        """
    def hasExpression(self, index: int = ...) -> bool:
        """self.hasExpression(index) -> True if has expression, False otherwise.
        @param index: Optional index.
        @return: True if has expression, False otherwise.
        """
    def height(self) -> int:
        """self.height() -> Height of array of values.
        @return: Height of array of values.
        """
    def isAnimated(self, index: int = ..., view: str | int | View = ...) -> bool:
        """self.isAnimated(index, view) -> True if animated, False otherwise.
        @param index: Optional index.
        @param view: Optional view.
        @return: True if animated, False otherwise.
        """
    def isKey(self, index: int = ..., view: str | int | View = ...) -> bool:
        """self.isKey(index, view) -> True if succeeded, False otherwise.
        @param index: Optional index.
        @param view: Optional view.
        @return: True if succeeded, False otherwise.
        """
    def isKeyAt(self, time: float, index: int = ..., view: str | int | View = ...) -> bool:
        """self.isKeyAt(time, index, view) -> True if succeeded, False otherwise.
        Returns True if there is a keyframe at specified time, optional index and view, otherwise returns False.
        @param time: Time.
        @param index: Optional index.
        @param view: Optional view.
        @return: True if succeeded, False otherwise.
        """
    def max(self) -> float:
        """self.max() -> Maximum value.
        @return: Maximum value.
        """
    def maximum(self) -> float:
        """self.max() -> Maximum value.
        @return: Maximum value.
        """
    def min(self) -> float:
        """self.min() -> Minimum value.
        @return: Minimum value.
        """
    def minimum(self) -> float:
        """self.min() -> Minimum value.
        @return: Minimum value.
        """
    def removeKey(self, index: Any = ..., view: Any = ...) -> bool:
        """self.removeKey(index, view) -> True if succeeded, False otherwise.
        Remove key.
        @param index: Optional index.
        @param view: Optional view.
        @return: True if succeeded, False otherwise.
        """
    def removeKeyAt(self, time: Any, index: Any = ..., view: Any = ...) -> bool:
        """self.removeKeyAt(time, index, view) -> True if succeeded, False otherwise.
        Remove keyframe at specified time, optional index and view. Return True if successful.
        @param time: Time.
        @param index: Optional index.
        @param view: Optional view.
        @return: True if succeeded, False otherwise.
        """
    def resize(self, w: int, h: int = ...) -> bool:
        """self.resize(w, h) -> True if successful, False otherwise.
        Resize the array.
        @param w: New width
        @param h: Optional new height
        @return: True if successful, False otherwise.
        """
    def setAnimated(self, index: int = ..., view: str | int | View = ...) -> bool:
        """self.setAnimated(index, view) -> True if succeeded, False otherwise.
        Create an Animation object. Return True if successful, in which case caller must initialise it by calling setValue() or setValueAt().
        @param index: Optional index.
        @param view: Optional view.
        @return: True if succeeded, False otherwise.
        """
    def setDefaultValue(self, s: Sequence[Any]) -> None:
        """self.setDefaultValue(s) -> None.
        @param s: Sequence of floating-point values.
        @return: None.
        """
    def setExpression(self, expression: str, channel: int = ..., view: str | int | View = ...) -> bool:
        """self.setExpression(expression, channel=-1, view=None) -> bool
        Set the expression for a knob. You can optionally specify a channel to set the expression for.

        @param expression: The new expression for the knob. This should be a string.
        @param channel: Optional parameter, specifying the channel to set the expression for. This should be an integer.
        @param view: Optional view parameter. Without, this command will set the expression for the current view theinterface is displaying. Can be the name of the view or the index.
        @return: True if successful, False if not.
        """
    def setKeyAt(self, time: float, index: int = ..., view: str | int | View = ...) -> None:
        """self.setKeyAt(time, index, view) -> None.
        Set a key on element 'index', at time and view.
        @param time: Time.
        @param index: Optional index.
        @param view: Optional view.
        @return: None.
        """
    def setRange(self, f1: float, f2: float) -> None:
        """self.setRange(f1, f2) -> None.
        Set range of values.
        @param f1 Min value.
        @param f2 Max value.
        @return: None.
        """
    def setSingleValue(self, b: bool, view: str | int | View = ...) -> None:
        """self.setSingleValue(b, view) -> None.
        Set to just hold a single value or not.
        @param b: Boolean object.
        @param view: Optional view. Default is current view.
        @return: None.
        """
    def setValue(self, value: Any, index: Any = ..., time: Any = ..., view: Any = ...) -> bool:
        """self.setValue(value, index, time, view) -> True if value changed, False otherwise. Safe to ignore.
        Set index to value at time and view.
        @param value: Floating point value.
        @param index: Optional index.
        @param time: Optional time.
        @param view: Optional view.
        @return: True if value changed, False otherwise. Safe to ignore.
        """
    def setValueAt(self, value: float, time: float, index: int = ..., view: str | int | View = ...) -> bool:
        """self.setValueAt(value, time, index, view) -> bool.
        Set value of element 'index' at time for view. If the knob is animated, it will set a new keyframe or change an existing one. Index and view are optional. Return True if successful.
        @param value: Floating point value.
        @param time: Time.
        @param index: Optional index.
        @param view: Optional view.
        @return: True if value changed, False otherwise. Safe to ignore.
        """
    def singleValue(self, view: str | int | View = ...) -> bool:
        """self.singleValue(view) -> True if holds a single value.
        @param view: Optional view. Default is current view.
        @return: True if holds a single value.
        """
    def splitView(self, view: str | int | View = ...) -> None:
        """self.splitView(view) -> None.
        Split the view away from the current knob value.
        @param view: Optional view. Default is current view.
        @return: None.
        """
    def toScript(self, quote: Any = ..., context: OutputContext | None = ...) -> str:
        """self.toScript(quote, context) -> String.
        Return the value of the knob in script syntax.
        @param quote: Optional, default is False. Specify True to return the knob value quoted in {}.
        @param context: Optional context, default is current, None will be "contextless" (all views, all keys) as in a .nk file.
        @return: String.
        """
    def unsplitView(self, view: str | int | View = ...) -> None:
        """self.unsplitView(view) -> None.
        Unsplit the view so that it shares a value with other views.
        @param view: Optional view. Default is current view.
        @return: None.
        """
    def value(self, index: Any = ..., view: Any = ..., time: Any = ...) -> Any:
        """self.value(index, view, time) -> Floating point or List of floating point values (in case some are different).
        @param index: Optional index. Default is 0.
        @param view: Optional view.
        @param time: Optional time.
        @return: Floating point or List of floating point values (in case some are different).
        """
    def valueAt(self, time: float, index: int = ..., view: str | int | View = ...) -> Any:
        """self.valueAt(time, index, view) -> Floating point or List of floating point values (in case some are different).
        Return value for this knob at specified time, optional index and view.
        @param time: Time.
        @param index: Optional index. Default is 0.
        @param view: Optional view.
        @return: Floating point or List of floating point values (in case some are different).
        """
    def vect(self, arg1: str | int | View = ...) -> list[float]:
        """self.vect() -> List of knob values.
        @return: List of knob values.
        Should only be used for knobs that are neither animated
        nor get their values from a ValueProvider.
        For knobs like that, use Array_Knob.getValue, instead
        """
    def width(self) -> int:
        """self.width() -> Width of array of values.
        @return: Width of array of values.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> Array_Knob: ...

class Color_Knob(Array_Knob):
    """A knob which holds a color. Provides a UI for picking colours as well as editing the values directly."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def inputNumber(self) -> int:
        """inputNumber() -> int

        Return input number.
        """
    def names(self, n: int) -> str:
        """names(n) -> string

        Return name for dimension n. The argument n is an integer.
        """

class AColor_Knob(Color_Knob):
    """AColor_Knob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class AnimationCurve:
    """AnimationCurve"""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """AnimationCurve(knob, index, name, view) -> AnimationCurve

        Construct a new AnimationCurve.
        @param knob: The knob this animation belongs to.
        @param index: The slot number in the knob.
        @param name: Field name.
        @param view: Optional view name.
        """
    def addKey(self, keys: Any) -> None:
        """self.addKey(keys) -> None.
        Insert a sequence of keys.
        @param keys: Sequence of AnimationKey.
        @return: None.
        """
    def changeInterpolation(self, keys: Any, type: Any) -> None:
        """self.changeInterpolation(keys, type) -> None.
        Change interpolation (and extrapolation) type for the keys.
        @param keys: Sequence of keys.
        @param type: Interpolation type.
        @return: None.
        """
    def clear(self) -> None:
        """self.clear() -> None.
        Delete all keys.
        @return: None.
        """
    def constant(self) -> bool:
        """self.constant() -> bool
        @return: True if the animation appears to be a horizontal line, is a simple
        number, or it is the default and all the points are at the same y value and
        have 0 slopes. False otherwise.
        """
    def derivative(self, t: Any, n: Any = ...) -> float:
        """self.derivative(t, n) -> Float.
        The n'th derivative at time 't'. If n is less than 1 it returns evaluate(t).
        @param t: Time.
        @param n: Optional. Default is 1.
        @return: The value of the derivative.
        """
    def evaluate(self, t: Any) -> float:
        """self.evaluate(t) -> float
        Value at time 't'.
        @param t: Time.
        @return: The value of the animation at time 't'.
        """
    def expression(self) -> str:
        """self.expression() -> String.
        Get the expression.
        @return: String.
        """
    def fixSlopes(self) -> None:
        """self.fixSlopes() -> None.
        @return: None.
        """
    def fromScript(self, s: str) -> None:
        """self.fromScript(s) -> None.
        @param s: String.
        @return: None.
        """
    def identity(self) -> bool:
        """self.identity() -> bool
        @return: True if the animation appears to be such that y == x everywhere.
        """
    def integrate(self, t1: Any, t2: Any) -> float:
        """self.integrate(t1, t2) -> Float.
        Calculate the area underneath the curve from t1 to t2.
        @param t1 The start of the integration range.
        @param t2 The end of the integration range.
        @return: The result of the integration.
        """
    def inverse(self, y: Any) -> float:
        """self.inverse(y) -> Float.
        The inverse function at value y.
        @param y: The value of the function to get the inverse for.
        @return: Float.
        """
    def keys(self) -> list[AnimationKey]:
        """self.keys() -> List of keys.
        @return: List of keys.
        """
    def knob(self) -> Knob:
        """self.knob() -> Knob.
        Return knob this animation belongs to.
        @return: Knob.
        """
    def knobAndFieldName(self) -> str:
        """self.knobAndFieldName() -> string.
        Knob and field name combined (e.g. 'translate.x').
        @return: string.
        """
    def knobIndex(self) -> int:
        """self.knobIndex() -> Int.
        Return the knob index this animation belongs to.
        @return: Int.
        """
    def noExpression(self) -> bool:
        """self.noExpression() -> bool
        @return: True if the expression is the default expression (i.e. the keys
        control the curve), False otherwise.
        """
    def removeKey(self, keys: Any) -> None:
        """self.removeKey(keys) -> None.
        Remove some keys from the curve.
        @param keys: The sequence of keys to be removed.
        @return: None.
        """
    def selected(self) -> bool:
        """self.selected() -> bool
        @return: True if selected, False otherwise.
        """
    def setExpression(self, s: Any) -> None:
        """self.setExpression(s) -> None.
        Set expression.
        @param s: A string containing the expression.
        @return: None.
        """
    def setKey(self, t: Any, y: Any) -> Any:
        """self.setKey(t, y) -> Key.
        Set a key at time t and value y.
        @param t: The time to set the key at.
        @param y: The value for the key.
        @return: The new key.
        """
    def size(self) -> int:
        """self.size() -> Number of keys.
        @return: Number of keys.
        """
    def toScript(self, selected: Any = ...) -> str:
        """self.toScript(selected) -> str
        @param selected: Optional parameter. If True, only process selected curves.
        @return: A string containing the curves.
        """
    def view(self) -> str:
        """self.view() -> String.
        The view this AnimationCurve object is associated with.
        @return: String.
        """

class AnimationKey:
    """A control point for an animation curve.
    @var x
    The horizontal position of the point
    @var y
    The vertical position of the point
    @var lslope
    The derivative to the left of the point. If interpolation does not have
    USER_SET_SLOPE then this may not be correct until after evaluate() has been
    called.
    @var rslope
    The derivative to the right of the point. If interpolation does not have
    USER_SET_SLOPE then this may not be correct until after evaluate() has been
    called.
    @var la
    The left 'bicubic' value. This represents the horizontal
    position of the left bezier handle end, where 1.0 means 1/3 of the
    distance to the previous point. If both handles for a span are 1.0
    then the horizontal interpolation is linear and thus the vertical
    interpolation a cubic function.  The legal values are 0 to
    3. Setting outside of this range will produce undefined results.
    @var ra
    The right 'bicubic' value, again the legal range is 0 to 3.
    @var interpolation
    Used to calculate all the slopes except for the left slope of the first key
    and the right slope of the last key.
    Legal values are:
    - USER_SET_SLOPE: If this bit is on, the slopes are fixed by
                      the user and interpolation and extrapolation are ignored.
    - CONSTANT: The value of the curve is equal to the y of the
                point to the left.
    - LINEAR: slopes point directly at the next key.
    - SMOOTH: same as CATMULL_ROM but the slopes are clamped so that the
              convex-hull property is preserved (meaning no part of the curve
              extends vertically outside the range of the keys on each side of
              it). This is the default.
    - CATMULL_ROM: the slope at key n is set to the slope between the control
                   points n-1 and n+1. This is used by lots of software.
    - cubic: the slope is calculated to the only cubic interpolation which makes
             the first and second derivatives continuous. This type of
             interpolation was very popular in older animation software.  A
             different cubic interpolation is figured out for each set of adjacent
             points with the CUBIC type.
    - for the smooth, CATMULL_ROM, and CUBIC interpolations, the first and last
      key have slopes calculated so that the second derivative is zero at them.
    @var extrapolation
    controls how to set the left slope of the first point and the right slope of
    the last point. Notice that this can be set differently on the first and last
    points, and is also remembered on all internal points so if end points are
    deleted old behavior is restored).
    - constant: the left slope of the first point, and the right slope of the last
                point, are set to zero.
    - linear: (and all other values): The left slope of the first point is set
              equal to it's right slope (calculated by the interpolation).
    the right slope of the last point is set equal to it's left slope.
    if there is only one point both slopes are set to zero.
    @var selected
    True if the point is selected in the curve editor.
    """
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """AnimationKey(x, y, interpolation=nuke.SMOOTH, extrapolation=nuke.CONSTANT) -> AnimationKey

        Construct a new AnimationKey at position (x, y) with the given interpolation and extrapolation.
        """
    @property
    def extrapolation(self) -> Any:
        """Controls how to set the left slope of the first point and the right slope of the last point"""
    @extrapolation.setter
    def extrapolation(self, value: Any) -> None: ...
    @property
    def interpolation(self) -> Any:
        """Used to calculate all the slopes except for the left slope of the first key and the right slope of the last key"""
    @interpolation.setter
    def interpolation(self, value: Any) -> None: ...
    @property
    def la(self) -> Any:
        """The left 'bicubic' value"""
    @la.setter
    def la(self, value: Any) -> None: ...
    @property
    def lslope(self) -> Any:
        """The derivative to the left of the point"""
    @lslope.setter
    def lslope(self, value: Any) -> None: ...
    @property
    def ra(self) -> Any:
        """The right 'bicubic' value"""
    @ra.setter
    def ra(self, value: Any) -> None: ...
    @property
    def rslope(self) -> Any:
        """The derivative to the right of the point"""
    @rslope.setter
    def rslope(self, value: Any) -> None: ...
    @property
    def selected(self) -> Any:
        """True if the point is selected in the curve editor"""
    @selected.setter
    def selected(self, value: Any) -> None: ...
    @property
    def x(self) -> Any:
        """The horizontal position of the point"""
    @x.setter
    def x(self, value: Any) -> None: ...
    @property
    def y(self) -> Any:
        """The vertical position of the point"""
    @y.setter
    def y(self, value: Any) -> None: ...

class Axis_Knob(Knob):
    """A knob which descibes a 3D affine transformation, by combining rotations around each principal axis, scaling, translation, skew and a pivot point."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def pivot(self) -> XYZ_Knob:
        """self.pivot() -> XYZ_Knob

        Return pivot knob.
        """
    def rotate(self) -> XYZ_Knob:
        """self.rotate() -> XYZ_Knob

        Return rotation knob.
        """
    def scale(self) -> Scale_Knob:
        """self.scale() -> Scale_Knob

        Return scale knob.
        """
    def skew(self) -> XYZ_Knob:
        """self.skew() -> XYZ_Knob

        Return skew knob.
        """
    def translate(self) -> XYZ_Knob:
        """self.translate() -> XYZ_Knob

        Return translation knob.
        """
    def uniformScale(self) -> Double_Knob:
        """self.uniformScale() -> Double_Knob

        Return uniform scale knob.
        """
    def value(self, arg1: OutputContext = ...) -> Any:
        """self.value() -> _nukemath.Matrix4
        Return the transform matrix formed by combining the input knob values for translate, rotate, scale, skew and pivot.
        """

class BBox_Knob(Array_Knob):
    """A knob which holds a bounding box."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def fromDict(self, box: dict) -> None:
        """self.fromDict(box) -> None

        Set the bounding box from the given box.
        @param box: Dictionary containing the x, y, r and t keys.
        @return: None
        """
    def names(self, arg1: int, /) -> Any:
        """Return name for dimension 'i'"""
    def r(self, arg1: OutputContext = ..., /) -> float:
        """Return value for R extent."""
    def setR(self, arg1: float, /) -> Any:
        """Set value for R extent."""
    def setT(self, arg1: float, /) -> Any:
        """Set value for T extent."""
    def setX(self, arg1: float, /) -> Any:
        """Set value for X position."""
    def setY(self, arg1: float, /) -> Any:
        """Set value for Y position."""
    def t(self, arg1: OutputContext = ..., /) -> float:
        """Return value for T extent."""
    def toDict(self) -> dict[str, float]:
        """self.toDict() -> dict.

        Returns the bounding box as a dict with x, y, r, and t keys.
        @return: dict with x, y, r and t keys
        """
    def value(self, arg1: int = ..., arg2: OutputContext = ..., /) -> tuple[float, ...]:
        """Return value for dimension 'i'"""
    def x(self, arg1: OutputContext = ..., /) -> float:
        """Return value for X position."""
    def y(self, arg1: OutputContext = ..., /) -> float:
        """Return value for Y position."""

class Node:
    def Class(self) -> str:
        """self.Class() -> Class of node.
        @return: Class of node.
        """
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __getitem__(self, key: str, /) -> Knob:
        """Return self[key]."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __str__(self, /) -> str:
        """Return str(self)."""
    def addCallback(self, string: Any, Callable: Any) -> None:
        """self.addCallback(string, Callable) -> None
        Add a callback to a specific event id.
        Specific event ids can be found in the documentation of the related type or function.
        The LiveGroupNode has some examples of these event ids such as nuke.LIVEGROUP_CALLBACK_PUBLISHED.
        It is possible to use your own event id string and then execute the callback using self.executeCallback(string).
        Note that this is not related to the standard Nuke callback mechanism.
        @param string: the string event id to add the callback on.
        @param callable: callable to execute when the event is triggered. The callable should take the node as a parameter e.g. def callback(node):
        @return: None
  
        """
    def addKnob(self, k: Knob) -> None:
        """self.addKnob(k) -> None.
        Add knob k to this node or panel.
        @param k: Knob.
        @return: None.
        """
    def allKnobs(self) -> list[Knob]:
        """self.allKnobs() -> list

        Get a list of all knobs in this node, including nameless knobs.

        For example:

           >>> b = nuke.nodes.Blur()
           >>> b.allKnobs()

        @return: List of all knobs.

        Note that this doesn't follow the links for Link_Knobs/Obsolete_Knobs
        """
    def autoplace(self) -> None:
        """self.autoplace() -> None.
        Automatically place nodes, so they do not overlap.
        @return: None.
        """
    def baseNode(self) -> Node:
        """self.baseNode() -> Return the 'original'(base) node if this is a clone, or this node if not cloned.
        @return: A node.
        """
    def bbox(self) -> Info:
        """self.bbox() -> List of x, y, w, h.
        Bounding box of the node.
        @return: List of x, y, w, h.
        """
    def canSetInput(self, i: Any, node: Any) -> bool:
        """self.canSetInput(i, node) -> bool
        Check whether the output of 'node' can be connected to input i. 
        @param i: Input number.
        @param node: The node to be connected to input i.
        @return: True if node can be connected, False otherwise.
        """
    def channels(self) -> list[str]:
        """self.channels() -> String list.
        List channels output by this node.
        @return: String list.
        """
    def clearCallbacks(self) -> None:
        """self.clearCallbacks() -> None
        Remove all callbacks on the node that were previously added using self.addCallback(string, Callable).
        Note that this is not related to the standard Nuke callback mechanism.
        @return: None
        """
    def clearCustomIcon(self) -> None:
        """self.clearCustomIcon() -> None.
        Clear the custom icon set for the node.
        @return: None.
        """
    def cloneInstanceIndex(self) -> int:
        """self.cloneInstanceIndex() -> The instance index of this node where 0 is the base node, and clones begin at index 1.
        The instance index is not guaranteed to be the same between Nuke sessions.
        @return: Index of clone instance, or -1 if node is not cloned.
        """
    def cloneInstanceNode(self) -> Any:
        """self.cloneInstanceNode() -> The node for a valid clone instance index. If index is 0 this node(the base) is returned.
        @param i: Instance index.
        @return: An instance node, or None if index is invalid for this node.
        """
    def cloneInstances(self) -> list:
        """self.cloneInstances() -> Return a list of all instances for this node.
        @return: List of nodes.
        """
    def clones(self) -> int:
        """self.clones() -> Number of clones.
        @return: Number of clones.
        """
    def connectInput(self, i: Any, node: Any) -> bool:
        """self.connectInput(i, node) -> bool
        Connect the output of 'node' to the i'th input or the next available unconnected input. The requested input is tried first, but if it is already set then subsequent inputs are tried until an unconnected one is found, as when you drop a connection arrow onto a node in the GUI.
        @param i: Input number to try first.
        @param node: The node to connect to input i.
        @return: True if a connection is made, False otherwise.
        """
    def deepSample(self, c: str | float, x: int, y: int, n: int) -> Any:
        """self.deepSample(c, x, y, n) -> Floating point value.
        Return pixel values from a deep image.
        This requires the image to be calculated, so performance may be very bad if this is placed into an expression in
        a control panel.
        @param c: Channel name.
        @param x: Position to sample (X coordinate).
        @param y: Position to sample (Y coordinate).
        @param n: Sample index (between 0 and the number returned by deepSampleCount() for this pixel, or -1 for the frontmost).
        @return: Floating point value.
        """
    def deepSampleCount(self, x: int, y: int) -> Any:
        """self.deepSampleCount(x, y) -> Integer value.
        Return number of samples for a pixel on a deep image.
        This requires the image to be calculated, so performance may be very bad if this is placed into an expression in
        a control panel.
        @param x: Position to sample (X coordinate).
        @param y: Position to sample (Y coordinate).
        @return: Integer value.
        """
    def dependencies(self, what: int = ...) -> list[Node]:
        """self.dependencies(what) -> List of nodes.

        List all nodes referred to by this node. 'what' is an optional integer (see below).
        You can use the following constants or'ed together to select what types of dependencies are looked for:
                 nuke.EXPRESSIONS = expressions
                 nuke.LINKINPUTS = link knobs
                 nuke.LINKNODE_INPUTS = link nodes
                 nuke.INPUTS = visible input pipes
                 nuke.HIDDEN_INPUTS = hidden input pipes.
        The default is to look for all types of connections.

        Example:
        nuke.toNode('Blur1').dependencies( nuke.INPUTS | nuke.EXPRESSIONS )
        @param what: Or'ed constant of nuke.EXPRESSIONS, nuke.INPUTS and nuke.HIDDEN_INPUTS to select the types of dependencies. The default is to look for all types of connections.
        @return: List of nodes.
        """
    def dependent(self, what: int = ..., forceEvaluate: bool = ...) -> list[Node]:
        """self.dependent(what, forceEvaluate) -> List of nodes.

        List all nodes that read information from this node.  'what' is an optional integer:
                 You can use any combination of the following constants or'ed together to select what types of dependent nodes to look for:
                         nuke.EXPRESSIONS = expressions
                         nuke.LINKINPUTS = link knobs
                         nuke.LINKNODE_INPUTS = link nodes
                         nuke.INPUTS = visible input pipes
                         nuke.HIDDEN_INPUTS = hidden input pipes.
        The default is to look for all types of connections.

        forceEvaluate is an optional boolean defaulting to True. When this parameter is true, it forces a re-evaluation of the entire tree. 
        This can be expensive, but otherwise could give incorrect results if nodes are expression-linked. 

        Example:
        nuke.toNode('Blur1').dependent( nuke.INPUTS | nuke.EXPRESSIONS )
        @param what: Or'ed constant of nuke.EXPRESSIONS, nuke.INPUTS and nuke.HIDDEN_INPUTS to select the types of dependent nodes. The default is to look for all types of connections.
        @param forceEvaluate: Specifies whether a full tree evaluation will take place. Defaults to True.
        @return: List of nodes.
        """
    def error(self) -> bool:
        """error() -> bool
        True if the node or any in its input tree have an error, or False otherwise.

        Error state of the node and its input tree.  Deprecated; use hasError or treeHasError instead.
        Note that this will always return false for viewers, which cannot generate their input trees.  Instead, choose an input of the viewer (e.g. the active one), and call treeHasError() on that.
        """
    def executePythonCallback(self, string: Any) -> None:
        """self.executePythonCallback(string) -> None
        Executes the callback if one was added for the given event id string using self.addCallback(string, Callable).
        Specific event ids can be found in the documentation of the related type or function. 
        The LiveGroupNode has some examples of these event ids such as nuke.LIVEGROUP_CALLBACK_PUBLISHED.
        It is possible to use your own event id string by adding a callback for it using self.addCallback(string, Callable).
        Note that this is not related to the standard Nuke callback mechanism.
        @param string: the string event id with the callback to execute.
        @return: None
        """
    def fileDependencies(self, start: int, end: int) -> Any:
        """self.fileDependencies(start, end) -> List of nodes and filenames.

        @param start: first frame
        @param end: last frame
        Returns the list of input file dependencies for this node and all nodes upstream from this node for the given frame range.
        The file dependencies are calcuated by searching for Read ops or ops with a File knob.
        All views are considered and current proxy mode is used to decide on whether full format or proxy files are returned.
        Note that Write nodes files are also included but precomps, gizmos and external plugins are not.
        Any time shifting operation such as frameholds, timeblurs, motionblur etc are taken into consideration.
        @return The return list is a list of nodes and files they require.
        Eg.  [Read1, ['file1.dpx, file2.dpx'] ], [Read2, ['file3.dpx', 'file4.dpx'] ] ]
        """
    def firstFrame(self) -> int:
        """self.firstFrame() -> int.
        First frame in frame range for this node.
        @return: int.
        """
    def forceUpdateLocalization(self) -> None:
        """self.forceUpdateLocalization() -> Force Updates the localized files for this node.
        @return: None
        """
    def forceValidate(self) -> None:
        """self.forceValidate() -> None

        Force the node to validate itself, updating its hash.
        """
    def format(self) -> Format:
        """self.format() -> Format.
        Format of the node.
        @return: Format.
        """
    def frameRange(self) -> FrameRange:
        """self.frameRange() -> FrameRange.
        Frame range for this node.
        @return: FrameRange.
        """
    def fullName(self) -> str:
        """self.fullName() -> str
        Get the name of this node and any groups enclosing it in 'group.group.name' form.
        @return: The fully-qualified name of this node, as a string.
        """
    def getLink(self) -> Node:
        """self.getLink() -> Node

        Returns the node that this node is linked against.

        @raise TypeError: If the node is not a linkable node.
        @return: Node this node is linked against, returns None if not linked.
        """
    def getNumKnobs(self) -> int:
        """self.numKnobs() -> The number of knobs.
        @return: The number of knobs.
        """
    def getStage(self, arg1: OutputContext = ..., arg2: Any = ..., /) -> Any:
        """self.getStage([OutputContext], [list of additional times]) -> Runs the graph and returns the composed stage for geometry, Viewer or ScanlineRender nodes (if the latter two have geometry nodes connected, else None). Returns None for other node types."""
    def getTab(self) -> Any:
        """self.getTab() -> Integer value.
        @return: The index for the current active tab, or None if the node is not open in a panel.
        """
    def hasError(self) -> bool:
        """hasError() -> bool
        True if the node itself has an error, regardless of the state of the ops in its input tree, or False otherwise.

        Error state of the node itself, regardless of the state of the ops in its input tree.
        Note that an error on a node may not appear if there is an error somewhere in its input tree, because it may not be possible to validate the node itself correctly in that case.
        """
    def height(self) -> int:
        """self.height() -> int.
        Height of the node.
        @return: int.
        """
    def help(self) -> str:
        """self.help() -> str
        @return: Help for the node.
        """
    def helpUrl(self, *args: Any, **kwargs: Any) -> str:
        """@return The current documentation help URL for the node"""
    def hideControlPanel(self) -> None:
        """self.hideControlPanel() -> None
        @return: None
        """
    def input(self, i: int) -> Any:
        """self.input(i) -> The i'th input.
        @param i: Input number.
        @return: The i'th input.
        """
    def inputs(self) -> int:
        """self.inputs() -> Gets the maximum number of connected inputs.
        @return: Number of the highest connected input + 1. If inputs 0, 1, and 3 are connected, this will return 4.
        """
    def isClone(self) -> bool:
        """self.isClone() -> Is this node a clone? If so use baseNode() to retrieve the 'original' node.
        @return: True if the node is a clone, False otherwise.
        """
    def isCloneable(self) -> bool:
        """self.isCloneable() -> If the node permits cloning.
        @return: True if the node allows cloning, False otherwise.
        """
    def isLinked(self) -> bool:
        """self.isLinked() -> bool

        Return True if the node is currently linked to a node.

        @raise TypeError: If the node is not a linkable node.
        @return: True if linked.
        """
    def isLocalizationOutdated(self) -> bool:
        """self.isLocalizationOutdated() -> Returns if there are changes detected in the source file.
        @return: true if the Localization source file has changed
        """
    def isLocalized(self) -> bool:
        """self.isLocalized() -> returns True/False whether the node is completely localized.
        @return: bool
        """
    def isSelected(self) -> bool:
        """self.isSelected() -> bool

        Returns the current selection state of the node.  This is the same as checking the 'selected' knob.
        @return: True if selected, or False if not.
        """
    def knob(self, p: str | int, follow_link: bool = ...) -> Knob | None:
        """self.knob(p[, follow_link]) -> The knob named p or the pth knob.
        @param p: A string or an integer.
        @param follow_link: Should it follow links to Link_Knob until resolution. Default is True.
        @return: The knob named p or the pth knob.
        """
    def knobs(self) -> dict[str, Knob]:
        """self.knobs() -> dict

        Get a dictionary of (name, knob) pairs for all knobs in this node.

        For example:

           >>> b = nuke.nodes.Blur()
           >>> b.knobs()

        @return: Dictionary of all knobs.

        Note that this doesn't follow the links for Link_Knobs/Obsolete_Knobs
        """
    def lastFrame(self) -> int:
        """self.lastFrame() -> int.
        Last frame in frame range for this node.
        @return: int.
        """
    def linkableKnobs(self, knobType: Any = ...) -> list:
        """self.linkableKnobs(knobType) -> List

        Returns a list of any knobs that may be linked to from the node as well as some meta information about the knob. This may include whether the knob is enabled and whether it should be used for absolute or relative values. Not all of these variables may make sense for all knobs..
        @param knobType A KnobType describing the type of knobs you want.@return: A list of LinkableKnobInfo that may be empty .
        """
    def localizationProgress(self) -> float:
        """self.localizationProgress() -> Checks and reports on progress of localization of the current node.
        @return: float, between 0.0 (not localized) and 1.0 (localized)
        """
    def lock(self) -> Any:
        """self.lock() -> Sets the node to a locked state where knobs cannot be edited."""
    def locked(self) -> bool:
        """self.locked() -> Returns True if the node is locked, False otherwise."""
    def maxInputs(self) -> int:
        """self.maximumInputs() -> Maximum number of inputs this node can have.
        @return: Maximum number of inputs this node can have.
        """
    def maxOutputs(self) -> int:
        """self.maximumOutputs() -> Maximum number of outputs this node can have.
        @return: Maximum number of outputs this node can have.
        """
    def maximumInputs(self) -> int:
        """self.maximumInputs() -> Maximum number of inputs this node can have.
        @return: Maximum number of inputs this node can have.
        """
    def maximumOutputs(self) -> int:
        """self.maximumOutputs() -> Maximum number of outputs this node can have.
        @return: Maximum number of outputs this node can have.
        """
    def metadata(self, key: str = ..., time: float = ..., view: str | int | View = ...) -> dict:
        """self.metadata(key, time, view) -> value or dict
        Return the metadata item for key on this node at current output context, or at optional time and view.
        If key is not specified a dictionary containing all key/value pairs is returned.
        None is returned if key does not exist on this node.
        @param key: Optional name of the metadata key to retrieve.
        @param time: Optional time to evaluate at (default is taken from node's current output context).
        @param view: Optional view to evaluate at (default is taken from node's current output context).
        @return: The requested metadata value, a dictionary containing all keys if a key name is not provided, or None if the specified key is not matched.
        """
    def minInputs(self) -> int:
        """self.minimumInputs() -> Minimum number of inputs this node can have.
        @return: Minimum number of inputs this node can have.
        """
    def minimumInputs(self) -> int:
        """self.minimumInputs() -> Minimum number of inputs this node can have.
        @return: Minimum number of inputs this node can have.
        """
    def name(self) -> str:
        """self.name() -> str
        @return: Name of node.
        """
    def numKnobs(self) -> int:
        """self.numKnobs() -> The number of knobs.
        @return: The number of knobs.
        """
    def opHashes(self) -> list[int]:
        """self.opHashes() -> list of int

        Returns a list of hash values, one for each op in this node.
        """
    def optionalInput(self) -> int:
        """self.optionalInput() -> Number of first optional input.
        @return: Number of first optional input.
        """
    def overrideKnob(self, k: Any) -> bool:
        """self.overrideKnob(k) -> bool

        Override knob k on this link node.

        @param k: Knob to override.
        @raise TypeError: If the node is not a linkable node.
        @raise RuntimeError: If not linked.
        @return: True if knob successfully overridden.
        """
    def parent(self) -> Node:
        """self.parent() -> Return the parent group node for this node."""
    def performanceInfo(self, category: Any) -> Any:
        """self.performanceInfo( category ) -> Returns performance information for this node. Performance timing must be enabled.
        @category: performance category ( optional ).A performance category, must be either nuke.PROFILE_STORE, nuke.PROFILE_VALIDATE, nuke.PROFILE_REQUEST or nuke.PROFILE_ENGINE The default is nuke.PROFILE_ENGINE which gives the performance info of the render engine.
        @return: A dictionary containing the cumulative performance info for this category, where:
        callCount = the number of calls made
        timeTakenCPU =  the CPU time spent in microseconds
        timeTakenWall = the actual time ( wall time ) spent in microseconds
        """
    def pixelAspect(self) -> float:
        """self.pixelAspect() -> int.
        Pixel Aspect ratio of the node.
        @return: float.
        """
    def proxy(self) -> bool:
        """self.proxy() -> bool
        @return: True if proxy is enabled, False otherwise.
        """
    def readKnobs(self, s: str) -> None:
        """self.readKnobs(s) -> None.
        Read the knobs from a string (TCL syntax).
        @param s: A string.
        @return: None.
        """
    def redraw(self) -> None:
        """self.redraw() -> None.
        Force a redraw of the node.
        @return: None.
        """
    def removeCallback(self, string: Any) -> None:
        """self.removeCallback(string) -> None
        Remove a callback for a specific event id string that was previously added using self.addCallback(string, Callable).
        Note that this is not related to the standard Nuke callback mechanism.
        @param string: the string event id with the callback to remove.
        @return: None
        """
    def removeKnob(self, k: Knob) -> None:
        """self.removeKnob(k) -> None.
        Remove knob k from this node or panel. Throws a ValueError exception if k is not found on the node.
        @param k: Knob.
        @return: None.
        """
    def removeOverrideKnob(self, k: Any) -> bool:
        """self.removeOverrideKnob(k) -> bool

        Remove override from knob k on this link node.

        @param k: Knob to remove override from.
        @raise TypeError: If the node is not a linkable node.
        @raise RuntimeError: If not linked.
        @return: True if override removed successfully.
        """
    def resetKnobsToDefault(self) -> None:
        """self.resetKnobsToDefault() -> None

        Reset all the knobs to their default values.
        """
    def rootNode(self) -> Node:
        """self.rootNode() -> Returns this node's root node. This may differ from nuke.root() for example if the read node was created importing footage to the timeline."""
    @classmethod
    def running(cls) -> Any:
        """self.running() -> Node rendering when paralled threads are running or None.
        Class method.
        @return: Node rendering when paralled threads are running or None.
        """
    def sample(self, c: str | float, x: float, y: float, dx: float = ..., dy: float = ..., arg6: float = ...) -> Any:
        """self.sample(c, x, y, dx, dy) -> Floating point value.
        Return pixel values from an image.
        This requires the image to be calculated, so performance may be very bad if this is placed into an expression in
        a control panel. Produces a cubic filtered result. Any sizes less than 1, including 0, produce the same filtered result,
        this is correct based on sampling theory. Note that integers are at the corners of pixels, to center on a pixel add .5 to both coordinates.
        If the optional dx,dy are not given then the exact value of the square pixel that x,y lands in is returned. This is also called 'impulse filtering'.
        @param c: Channel name.
        @param x: Centre of the area to sample (X coordinate).
        @param y: Centre of the area to sample (Y coordinate).
        @param dx: Optional size of the area to sample (X coordinate).
        @param dy: Optional size of the area to sample (Y coordinate).
        @param frame: Optional frame to sample the node at.
        @return: Floating point value.
        """
    def screenHeight(self) -> int:
        """self.screenHeight() -> int.
        Height of the node when displayed on screen in the DAG, at 1:1 zoom, in pixels.
        @return: int.
        """
    def screenWidth(self) -> int:
        """self.screenWidth() -> int.
        Width of the node when displayed on screen in the DAG, at 1:1 zoom, in pixels.
        @return: int.
        """
    def selectOnly(self) -> None:
        """self.selectOnly() -> None.
        Set this node to be the only selection, as if it had been clicked in the DAG.
        @return: None.
        """
    def setCustomIcon(self, image: str, scale: float = ..., offsetX: int = ..., offsetY: int = ...) -> bool:
        """self.setCustomIcon(image, scale, offsetX, offsetY) -> bool.
        Set a custom icon for the node.
        @param image: filepath to image to be used as an icon.
        @param scale: Optional. scale factor for the icon.
        @param offsetX: Optional. offset the icon in the x axis from the top left corner of the node.
        @param offsetY: Optional. offset the icon in the y axis from the top left corner of the node.
        @return: True if icon has been set, else false.
        """
    def setInput(self, i: Any, node: Any) -> bool:
        """self.setInput(i, node) -> bool
        Connect input i to node if canSetInput() returns true.
        @param i: Input number.
        @param node: The node to connect to input i.
        @return: True if canSetInput() returns true, or if the input is already correct.
        """
    def setName(self, name: str, uncollide: bool = ..., updateExpressions: bool = ...) -> None:
        """self.setName(name, uncollide=True, updateExpressions=False) -> None
        Set name of the node and resolve name collisions if optional named argument 'uncollide' is True.
        @param name: A string.
        @param uncollide: Optional boolean to resolve name collisions. Defaults to True.
        @param updateExpressions: Optional boolean to update expressions in other nodes to point at the new name. Defaults to False.
        @return: None
        """
    def setSelected(self, selected: Any) -> None:
        """self.setSelected(selected) -> None.
        Set the selection state of the node.  This is the same as changing the 'selected' knob.
        @param selected: New selection state - True or False.
        @return: None.
        """
    def setTab(self, tabIndex: Any = ...) -> None:
        """self.setTab(tabIndex) -> None
        @param tabIndex: The tab to show (first is 0).
        @return: None
        """
    def setXYpos(self, x: int, y: int) -> None:
        """self.setXYpos(x, y) -> None.
        Set the (x, y) position of node in node graph.
        @param x: The x position of node in node graph.
        @param y: The y position of node in node graph.
        @return: None.
        """
    def setXpos(self, x: int) -> None:
        """self.setXpos(x) -> None.
        Set the x position of node in node graph.
        @param x: The x position of node in node graph.
        @return: None.
        """
    def setYpos(self, y: int) -> None:
        """self.setYpos(y) -> None.
        Set the y position of node in node graph.
        @param y: The y position of node in node graph.
        @return: None.
        """
    def showControlPanel(self, forceFloat: Any = ...) -> None:
        """self.showControlPanel(forceFloat = false) -> None
        @param forceFloat: Optional python object. If it evaluates to True the control panel will always open as a floating panel. Default is False.
        @return: None
        """
    def showInfo(self, s: Any) -> None:
        """self.showInfo(s) -> None.
        Creates a dialog box showing the result of script s.
        @param s: A string.
        @return: None.
        """
    def shown(self) -> bool:
        """self.shown() -> true if the properties panel is open. This can be used to skip updates that are not visible to the user.
        @return: true if the properties panel is open. This can be used to skip updates that are not visible to the user.
        """
    def treeHasError(self) -> bool:
        """treeHasError() -> bool
        True if the node or any in its input tree have an error, or False otherwise.

        Error state of the node and its input tree.
        Note that this will always return false for viewers, which cannot generate their input trees.  Instead, choose an input of the viewer (e.g. the active one), and call treeHasError() on that.
        """
    def unlink(self) -> None:
        """self.unlink() -> None

        Unlink the node without possibility to resolve.

        @raise TypeError: If the node is not a linkable node.
        """
    def unlock(self) -> Any:
        """self.unlock() -> Unlocks the node and makes knobs editable."""
    def upstreamFrameRange(self, i: int) -> FrameRange:
        """self.upstreamFrameRange(i) -> FrameRange
        Frame range for the i'th input of this node.
        @param i: Input number.
        @return: FrameRange. Returns None when querying an invalid input.
        """
    def width(self) -> int:
        """self.width() -> int.
        Width of the node.
        @return: int.
        """
    def writeKnobs(self, i: Any = ...) -> Any:
        """self.writeKnobs(i) -> String in .nk form.
        Return a tcl list. If TO_SCRIPT | TO_VALUE is not on, this is a simple list
        of knob names. If it is on, it is an alternating list of knob names
        and the output of to_script().

        Flags can be any of these or'd together:
        - nuke.TO_SCRIPT produces to_script(0) values
        - nuke.TO_VALUE produces to_script(context) values
        - nuke.WRITE_NON_DEFAULT_ONLY skips knobs with not_default() false
        - nuke.WRITE_USER_KNOB_DEFS writes addUserKnob commands for user knobs
        - nuke.WRITE_ALL writes normally invisible knobs like name, xpos, ypos

        @param i: The set of flags or'd together. Default is TO_SCRIPT | TO_VALUE.
        @return: String in .nk form.
        """
    def xpos(self) -> int:
        """self.xpos() -> X position of node in node graph.
        @return: X position of node in node graph.
        """
    def ypos(self) -> int:
        """self.ypos() -> Y position of node in node graph.
        @return: Y position of node in node graph.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> Node: ...

class BackdropNode(Node):
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __str__(self, /) -> str:
        """Return str(self)."""
    def getNodes(self) -> Any:
        """self.getNodes() -> a list of nodes contained inside the backdrop
        Get the nodes contained inside a backdrop node
        Example:
        backdrop = nuke.toNode("BackdropNode1")
        nodesInBackdrop = backdrop.getNodes()

        @return: a list of nodes contained inside the backdrop.
        """
    def selectNodes(self, selectNodes: Any = ...) -> None:
        """self.selectNodes(selectNodes) -> None
        Select or deselect all nodes in backdrop node
        Example:
        backdrop = nuke.toNode("BackdropNode1")
        backdrop.selectNodes(True)

        @return: None.
        """

class BeginTabGroup_Knob(Knob):
    """Begin a group of tabs. Subsequent knobs will all be part of the same tab group, until a matching EndTabGroup knob is found."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __new__(cls, *args: Any, **kwargs: Any) -> BeginTabGroup_Knob: ...

class Unsigned_Knob(Array_Knob):
    """A knob which holds one or more unsigned integer values."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def setValue(self, val: Any) -> bool:
        """self.setValue(val) -> bool
        Set the unsigned integer value of this knob.
        @param val: The new value for the knob. Must be an integer >= 0.
        @return: True if succeeded, False otherwise.
        """
    def value(self) -> int:
        """self.value() -> int
        Get the value of this knob as an integer.
        @return: int
        """

class Enumeration_Knob(Unsigned_Knob):
    """Stores a single value between 0 and some maximum, and manages a
    set of keywords visible to the user. The words themselves are
    displayed on a pulldown list in the user interface, and are written
    to the saved scripts (so that the numerical values can change).
    self.__init__(name, label, items) -> None
    @param name: Name.
    @param label: Label.
    @param items: List of strings.
    Example:
    k = nuke.Enumeration_Knob('MyEnumKnobName', 'MyEnumKnobLabel', ['label1', 'label2'])
    """
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def enumName(self, n: int) -> str:
        """self.enumName(n) -> string

        Return name of enumeration n. The argument n is an integer and in the range of 0 and numValues. Deprecated.
        """
    def getDisplayStrFromID(self) -> Any:
        """self.getDisplayStrFromID()
        returns the display text for the associated id
        @param id: the id you want to retrieve the display text for
        @return: String containing the display text, example scene_linear (linear)
        Example:
        displayStr = knob.getDisplayStrFromID('scene_linear')
        """
    def numValues(self) -> int:
        """self.numValues() -> int

        Return number of values. Deprecated.
        """
    def setValue(self, item: str | float) -> None:
        """self.setValue(item) -> None.
        Set the current value. item will first be converted into a string and matched against the enum values.
        If this fails, it will attempt to be used as an index into the enum.
        @param item: String or Integer.
        @return: None.
        Example:
        w = nuke.nodes.Write()
        k = w['file_type']
        k.setValue('exr')
        """
    def setValues(self, items: Sequence[Any]) -> None:
        """self.setValues(items) -> None.
        (Re)initialise knob to the supplied list of items.
        @param items: The new list of values.
        @return: None.
        Example:
        w = nuke.nodes.Write()
        k = w['file_type']
        k.setValues(['exr'])
        """
    def value(self) -> str:
        """self.value() -> String.
        Current value.
        @return: String.
        Example:
        w = nuke.nodes.Write()
        k = w['file_type']
        k.value()
        """
    def values(self) -> list[str]:
        """self.values() -> List of strings.
        Return list of items.
        @return: List of strings.
        Example:
        w = nuke.nodes.Write()
        k = w['file_type']
        k.values()
        """

class Bitmask_Knob(Enumeration_Knob):
    """Bitmask_Knob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __new__(cls, *args: Any, **kwargs: Any) -> Bitmask_Knob: ...

class String_Knob(Knob):
    """A knob which holds a string value. Appears as a text entry field in a Node panel."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getText(self, oc: OutputContext = ...) -> str:
        """self.getText(oc) -> string

        Get the non-evaluated value of this knob - also see `value()`
        @param oc: Optional parameter specifying the output context.
        Return text associated with knob.
        """
    def getValue(self, arg1: OutputContext = ..., /) -> str:
        """self.value(oc) -> str

        Get the evaluated value of this knob as a string - also see `getText()`.
        @param oc: Optional parameter specifying the output context.
        @return: String value.
        """
    def setText(self, arg1: str | None, arg2: str | None = ..., /) -> None:
        """self.setValue(val, view='default') -> None

        Set value of knob.
        @param val: The new value.
        @param view: Optional parameter specifying which view to set the value for. If omitted, the value will be set for the default view.
        @return: None
        """
    def setValue(self, val: str | None, view: str | None = ...) -> None:
        """self.setValue(val, view='default') -> None

        Set value of knob.
        @param val: The new value.
        @param view: Optional parameter specifying which view to set the value for. If omitted, the value will be set for the default view.
        @return: None
        """
    def splitView(self, view: str | int | View = ...) -> None:
        """self.splitView(view) -> None.
        Split the view away from the current knob value.
        @param view: Optional view. Default is current view.
        @return: None.
        """
    def unsplitView(self, view: str | int | View = ...) -> None:
        """self.unsplitView(view) -> None.
        Unsplit the view so that it shares a value with other views.
        @param view: Optional view. Default is current view.
        @return: None.
        """
    def value(self, oc: OutputContext = ...) -> str:
        """self.value(oc) -> str

        Get the evaluated value of this knob as a string - also see `getText()`.
        @param oc: Optional parameter specifying the output context.
        @return: String value.
        """

class Script_Knob(String_Knob):
    """A button which executes a TCL script."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def command(self) -> str:
        """self.command() -> str

        Get the current command.
        @return: The current command as a string, or None if there is no current command.
        """
    def execute(self) -> None:
        """self.execute() -> None
        Execute the command.
        @return: None.
        """
    def setCommand(self, cmd: str) -> None:
        """self.setCommand(cmd) -> None
        Set the new command for this knob.
        @param cmd: String containing a TCL command.
        @return: None.
        """
    def setValue(self, cmd: str) -> None:
        """self.setValue(cmd) -> None
        Set the new command for this knob.
        @param cmd: String containing a TCL command.
        @return: None.
        """
    def value(self) -> str:
        """self.value() -> str

        Get the current command.
        @return: The current command as a string, or None if there is no current command.
        """

class BlinkEditorKnob(Script_Knob):
    """BlinkEditorKnob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getFilename(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the filename of the script that was used to create the custom knob."""
    def getObject(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the custom knob object as created in the by the 'command' argument to the BlinkEditorKnob constructor."""
    def setNeedsRecompile(self, *args: Any, **kwargs: Any) -> Any:
        """Triggers the knob to recompile the script."""

class Boolean_Knob(Array_Knob):
    """A knob which holds a boolean value. This appears in a Node panel as a check box."""
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def setValue(self, b: Any) -> bool:
        """self.setValue(b) -> bool
        Set the boolean value of this knob.
        @param b: Boolean convertible object.
        @return: True if modified, False otherwise.
        """
    def value(self) -> bool:
        """self.value() -> bool
        Get the boolean value for this knob.
        @return: True or False.
        """

class Box:
    """A 2-dimensional rectangle. Described by left, right, top and bottom coords (width and height are calculated as necessary)."""
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def centerX(self) -> float:
        """self.centerX() -> float

        Return center in X.
        """
    def centerY(self) -> float:
        """self.centerY() -> float

        Return height in Y.
        """
    def clampX(self, x: Any) -> int:
        """self.clampX(x) -> int.

        Return x restricted to pointing at a pixel in the box.
        """
    def clampY(self, y: Any) -> int:
        """self.clampY(y) -> int.

        Return y restricted to pointing at a pixel in the box.
        """
    def clear(self) -> None:
        """self.clear() -> None.

        Set to is_constant().
        """
    def h(self) -> int:
        """self.h() -> int

        Return height.
        """
    def intersect(self, x: Any, y: Any, r: Any, t: Any) -> None:
        """self.intersect(x, y, r, t) -> None.

        Intersect with the given edges.
        self.intersect(box) -> None.

        Intersect with the given edges.
        """
    def isConstant(self) -> bool:
        """self.isConstant() -> True if box is 1x1 in both directions, False otherwise."""
    def merge(self, x: Any, y: Any, r: Any, t: Any) -> None:
        """self.merge(x, y, r, t) -> None.

        Merge with the given edges.
        self.merge(box) -> None.

        Merge with the given edges.
        """
    def move(self, dx: Any, dy: Any) -> None:
        """self.move(dx, dy) -> None.

        Move all the sides and thus the entire box by the given deltas.
        """
    def pad(self, *args: Any, **kwargs: Any) -> Any:
        """Expand the box by (dx, dy) on each side.
        self.pad(dx, dy, dr, dt) -> None.

        Move all the sides and thus the entire box by the given deltas.
        """
    def r(self) -> int:
        """self.r() -> int

        Return the right edge of the box.
        """
    def set(self, x: Any, y: Any, r: Any, t: Any) -> None:
        """self.set(x, y, r, t) -> None

        Set all values at once.
        """
    def setH(self, n: Any) -> None:
        """self.setH(n) -> None

        Set height by moving top edge.
        """
    def setR(self, n: Any) -> None:
        """self.setR(n) -> None

        Set the right edge. The parameter n is an integer.
        """
    def setT(self, n: Any) -> None:
        """self.setT(n) -> None

        Set top edge.
        """
    def setW(self, n: Any) -> None:
        """self.setW(n) -> None

        Set width by moving right edge.
        """
    def setX(self, n: Any) -> None:
        """self.setX(n) -> None

        Set the left edge. The parameter n is an integer.
        """
    def setY(self, n: Any) -> None:
        """self.setY(n) -> None

        Set the bottom edge. The parameter n is an integer.
        """
    def t(self) -> int:
        """self.t() -> int

        Return top edge.
        """
    def w(self) -> int:
        """self.w() -> int

        Return width.
        """
    def x(self) -> int:
        """self.x() -> int

        The left edge of the box.
        """
    def y(self) -> int:
        """self.y() -> int

        Return the bottom edge.
        """

class Box3_Knob(Array_Knob):
    """A 3-dimensional box."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def f(self, arg1: OutputContext = ..., /) -> float:
        """Return value for F extent. F (far) is the maximum Z extent of the box."""
    def n(self, arg1: OutputContext = ..., /) -> float:
        """Return value for N position. N (near) is the minimum Z extent of the box."""
    def names(self, arg1: int, /) -> Any:
        """Return name for dimension 'i'"""
    def r(self, arg1: OutputContext = ..., /) -> float:
        """Return value for R extent. R (right) is the right extent of the box."""
    def setF(self, arg1: float, /) -> Any:
        """Set value for F extent. F (far) is the maximum Z extent of the box."""
    def setN(self, arg1: float, /) -> Any:
        """Set value for N position. N (near) is the minimum Z extent of the box."""
    def setR(self, arg1: float, /) -> Any:
        """Set value for R extent. R (right) is the right extent of the box."""
    def setT(self, arg1: float, /) -> Any:
        """Set value for T extent. T (top) is the maximum vertical extent of the box."""
    def setX(self, arg1: float, /) -> Any:
        """Set value for X position. X is the minimum horizontal extent of the box."""
    def setY(self, arg1: float, /) -> Any:
        """Set value for Y position. Y is the minimum vertical extent of the box."""
    def t(self, arg1: OutputContext = ..., /) -> float:
        """Return value for T extent. T (top) is the maximum vertical extent of the box."""
    def value(self, arg1: int = ..., arg2: OutputContext = ..., /) -> tuple[float, ...]:
        """Return value for dimension 'i'"""
    def x(self, arg1: OutputContext = ..., /) -> float:
        """Return value for X position. X is the minimum horizontal extent of the box."""
    def y(self, arg1: OutputContext = ..., /) -> float:
        """Return value for Y position. Y is the minimum vertical extent of the box."""

class CancelledError(Exception): ...

class CascadingEnumeration_Knob(Enumeration_Knob):
    """Stores a single value between 0 and some maximum, and manages a
    set of keywords visible to the user. The words themselves are
    displayed on a pulldown list in the user interface, and are written
    to the saved scripts (so that the numerical values can change). To 
    create cascading submenus simply use the forward slash ( '/' ) 
    e.g. menu/item1self.__init__(name, label, items) -> None
    @param name: Name.
    @param label: Label.
    @param items: List of strings.
    Example:
    k = nuke.Enumeration_Knob('MyEnumKnobName', 'MyEnumKnobLabel', ['menu1/label1', 'label2'])
    """
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class Channel_Knob(Knob):
    """A knob which lets you select a layer and enable or disable individual channels.
    self.__init__(s, label, depth) -> None
    Constructor.
    @param s: name.
    @param label: Optional name to appear in GUI. Defaults to the knob's name.
    @param depth: Optional number of channels with zero being the Nuke default number of channels. Defaults to 0.
    """
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def channelSelector(self) -> bool:
        """self.channelSelector() -> bool"""
    def checkMarks(self) -> bool:
        """self.checkMarks() -> bool"""
    def depth(self) -> int:
        """self.depth() -> int

        Get the channel depth.
        @return: The depth of the channel as an int.
        """
    def enableChannel(self, name: int, b: Any = ...) -> None:
        """self.enableChannel(name, b) -> None

        Enable or disable a channel.
        @param name: The name of the channel.
        @param b: True to enable the channel, False to disable it.
        @return: None
        """
    def inputKnob(self) -> bool:
        """self.inputKnob() -> bool"""
    def inputNumber(self) -> int:
        """self.inputNumber() -> int"""
    def isChannelEnabled(self, name: int) -> bool:
        """self.isChannelEnabled(name) -> bool

        Test if a channel is enabled.
        @param name: The name of the channel.@return: True if the channel is enabled, False otherwise.
        """
    def layerSelector(self) -> bool:
        """self.layerSelector() -> bool"""
    def setEnable(self, name: int) -> None:
        """self.setEnable(name) -> None

        Enable a channel.
        @param name: The name of the channel to enable.
        @return: None
        """
    def setInput(self, num: int) -> None:
        """self.setInput(num) -> None
        Set the input number for this knob.@param num: The number of the new input.
        @return: None
        """
    def setValue(self, name: str) -> None:
        """self.setValue(name) -> None
        Set the selected channel using the channel name.
        @param name: The name of the new channel as a string.
        @return: None
        @raise ValueError exception if the channel doesn't exist.
        """
    def value(self) -> str:
        """self.value() -> str
        Get the name of the selected channel.
        @return: The name of the channel as a string.
        """

class ChannelMask_Knob(Channel_Knob):
    """ChannelMask_Knob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class ColorChip_Knob(Unsigned_Knob):
    """A knob which holds a single unsigned int that describes a user interface colour. The color format is 0xRRGGBB00."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class Disable_Knob(Boolean_Knob):
    """A knob which holds a boolean value representing the disabled state of a node. This appears in a Node panel as a check box."""
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def setValue(self, b: Any) -> bool:
        """self.setValue(b) -> bool
        Set the boolean value of this knob.
        @param b: Boolean convertible object.
        @return: True if modified, False otherwise.
        """
    def value(self) -> bool:
        """self.value() -> bool
        Get the boolean value for this knob.
        @return: True or False.
        """

class Double_Knob(Array_Knob):
    """A knob which holds one or more double-precision floating point values."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class EditableEnumeration_Knob(Enumeration_Knob):
    """Stores a single value between 0 and some maximum, and manages a
    set of Radio Buttons visible to the user. This is essentially an
    Enumeration_Knob with a different widget.
    """
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def enumName(self, n: Any) -> str:
        """self.enumName(n) -> string

        Return name of enumeration n. The argument n is an integer and in the range of 0 and numValues. Deprecated.
        """
    def getDisplayStrFromID(self) -> Any:
        """self.getDisplayStrFromID()
        returns the display text for the associated id
        @param id: the id you want to retrieve the display text for
        @return: String containing the display text, example scene_linear (linear)
        Example:
        displayStr = knob.getDisplayStrFromID('scene_linear')
        """
    def numValues(self) -> int:
        """self.numValues() -> int

        Return number of values. Deprecated.
        """
    def setValue(self, item: str | int) -> None:
        """self.setValue(item) -> None.
        Set the current value. item will first be converted into a string and matched against the enum values.
        If this fails, it will attempt to be used as an index into the enum.
        @param item: String or Integer.
        @return: None.
        Example:
        w = nuke.nodes.Write()
        k = w['file_type']
        k.setValue('exr')
        """
    def setValues(self, items: Any) -> None:
        """self.setValues(items) -> None.
        (Re)initialise knob to the supplied list of items.
        @param items: The new list of values.
        @return: None.
        Example:
        w = nuke.nodes.Write()
        k = w['file_type']
        k.setValues(['exr'])
        """
    def value(self) -> str:
        """self.value() -> String.
        Current value.
        @return: String.
        Example:
        w = nuke.nodes.Write()
        k = w['file_type']
        k.value()
        """
    def values(self) -> Any:
        """self.values() -> List of strings.
        Return list of items.
        @return: List of strings.
        Example:
        w = nuke.nodes.Write()
        k = w['file_type']
        k.values()
        """

class EndTabGroup_Knob(Knob):
    """End a group of tabs. This is only valid when a BeginTabGroup knob has already been used."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __new__(cls, *args: Any, **kwargs: Any) -> EndTabGroup_Knob: ...

class EvalString_Knob(String_Knob):
    """A string-valued knob which evaluates its value as a TCL expression."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def evaluate(self, arg1: float = ..., arg2: str | int | View = ...) -> str:
        """self.evaluate() -> String.
        Evaluate the string, performing substitutions.
        @return: String.
        """

class Eyedropper_Knob(AColor_Knob):
    """Eyedropper_Knob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class File_Knob(EvalString_Knob):
    """A knob which holds a filename. When it appears in a Node panel it provides a text field to show the filename and a button which opens the file chooser dialog."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def fromScript(self, s: str) -> None:
        """self.fromScript(s) -> None.
        Assign string to knob.
        @param s: String to assign.
        @return: None.
        """
    def fromUserText(self, s: str) -> None:
        """self.fromUserText(s) -> None.
        Assign string to knob, parses frame range off the end and opens file to get set the format.
        @param s: String to assign.
        @return: None.
        """
    def getEvaluatedValue(self, oc: OutputContext = ...) -> str:
        """self.getEvaluatedValue(oc) -> String.
        Returns the string on this knob, will be normalized to technical notation if sequence (%4d). Will also evaluate the string for any tcl and gsv expressions
        @parm oc: the output context to use, if None the knob uiContext will be used.
        @return: String.
        """
    def getValue(self) -> str:
        """self.getValue() -> String.
        Returns the string on this knob, will be normalized to technical notation if sequence (%4d). This will not evaluate any tcl or gsv expressions.
        @return: String.
        """
    def setValue(self, arg1: str, /) -> None:
        """self.fromScript(s) -> None.
        Assign string to knob.
        @param s: String to assign.
        @return: None.
        """
    def value(self, *args: Any, **kwargs: Any) -> str:
        """self.getValue() -> String.
        Returns the string on this knob, will be normalized to technical notation if sequence (%4d). This will not evaluate any tcl or gsv expressions.
        @return: String.
        """

class Font_Knob(Knob):
    """A knob for choosing a font."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def setValue(self, arg1: str, /) -> Any: ...
    def value(self) -> str: ...

class Format:
    """A Format."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Construct an empty format.
        Construct a format with width, height, x, y, r, t and optional pixel aspect ratio.
        """
    def add(self, name: Any) -> None:
        """self.add(name) -> None

        Add this instance to a list of "named" formats. The name parameter is the name of the list to add the format to.
        """
    def fromUV(self, u: Any, v: Any) -> Any:
        """self.fromUV(u, v) -> [x, y]

        Transform a UV coordinate in the range 0-1 into the format's XY range. Returns a list containing the x and y coordinates.

        @param u: The U coordinate.
        @param v: The V coordinate.
        @return: [x, y]
        """
    def height(self) -> int:
        """self.height() -> int

        Return the height of image file in pixels.
        """
    def name(self) -> str:
        """self.name() -> string

        Returns the user-visible name of the format.
        """
    def pixelAspect(self) -> float:
        """self.pixelAspect() -> float

        Returns the pixel aspect ratio (pixel width divided by pixel height) for this format.
        """
    def r(self) -> int:
        """self.r() -> int

        Return the right edge of image file in pixels.
        """
    def scaled(self, sx: Any = ..., sy: Any = ..., tx: Any = ..., ty: Any = ...) -> Format:
        """scaled(sx, sy, tx, ty) -> Format

        Scale and translate this format by sx, sy, tx and ty.

        @param sx: Scale factor in X.
        @param sy: Scale factor in Y.
        @param tx: Offset factor in X.
        @param ty: Offset factor in Y.
        @return: Format.
        """
    def setHeight(self, newHeight: Any) -> None:
        """self.setHeight(newHeight) -> None

        Set the height of image file in pixels. newHeight is the new height for the image; it should be a positive integer.
        """
    def setName(self, name: Any) -> None:
        """self.setName(name) -> None

        Set name of this format. The name parameter is the new name for the format.
        """
    def setPixelAspect(self, aspectRatio: Any) -> None:
        """self.setPixelAspect(aspectRatio) -> None

        Set a new pixel aspect ratio for this format. The aspectRatio parameter is the new ratio, found by dividing the desired pixel width by the desired pixel height.
        """
    def setR(self, newR: Any) -> None:
        """self.setR(newR) -> None

        Set the right edge of image file in pixels. newR is the new right edge for the image; it should be a positive integer.
        """
    def setT(self, newT: Any) -> None:
        """self.setT(newT) -> None

        Set the top edge of image file in pixels. newY is the new top edge for the image; it should be a positive integer.
        """
    def setWidth(self, newWidth: Any) -> None:
        """self.setWidth(newWidth) -> None

        Set the width of image file in pixels.newWidth is the new width for the image; it should be a positive integer.
        """
    def setX(self, newX: Any) -> None:
        """self.setX(newX) -> None

        Set the left edge of image file in pixels. newX is the new left edge for the  image; it should be a positive integer.
        """
    def setY(self, newY: Any) -> None:
        """self.setY(newY) -> None

        Set the bottom edge of image file in pixels. newY is the new bottom edge for the image; it should be a positive integer.
        """
    def t(self) -> int:
        """self.t() -> int

        Return the top edge of image file in pixels.
        """
    def toUV(self, x: Any, y: Any) -> Any:
        """self.toUV(x, y) -> (u, v)

        Back-transform an XY coordinate in the format's space into UV space.

        @param x: The X coordinate.
        @param y: The Y coordinate.
        @return: [u, v].
        """
    def width(self) -> int:
        """self.width() -> int

        Return the width of image file in pixels.
        """
    def x(self) -> int:
        """self.x() -> int

        Return the left edge of image file in pixels.
        """
    def y(self) -> int:
        """self.y() -> int

        Return the bottom edge of image file in pixels.
        """

class Format_Knob(Knob):
    """Format_Knob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def actualValue(self) -> Format:
        """actualValue() -> Format.

        Return value of knob.
        """
    def fromScript(self, s: str) -> bool:
        """fromScript(s) -> True if succeeded, False otherwise.

        Initialise from script s.
        """
    def name(self) -> str:
        """name() -> string.

        Return name of knob.
        """
    def setValue(self, format: str | None) -> bool:
        """setValue(format) -> True if succeeded, False otherwise.

        Set value of knob to format (either a Format object or a name of a format, e.g. "NTSC").
        """
    def toScript(self, quote: Any = ..., context: OutputContext | None = ...) -> str:
        """toScript(quote, context=current) -> string.

        Return the value of the knob in script syntax.
        Pass True for quote to return results quoted in {}.
        Pass None for context to get results for all views and key times (as stored in a .nk file).
        """
    def value(self) -> Format:
        """value() -> Format.

        Return value of knob.
        """

class FrameRange:
    """A frame range, with an upper and lower bound and an increment."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Construct from a frame range string, e.g. '1-10x2'."""
    def __iter__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __len__(self, *args: Any, **kwargs: Any) -> int: ...
    def __repr__(self, *args: Any, **kwargs: Any) -> str: ...
    def __str__(self, *args: Any, **kwargs: Any) -> str: ...
    def first(self) -> int:
        """self.first() -> int

        return the first frame of the range.
        """
    def frames(self) -> int:
        """self.frames() -> int

        return the numbers of frames defined in the range.
        """
    def getFrame(self, n: Any) -> int:
        """self.getFrame(n) -> int

        return the frame according to the index, parameter n must be between 0 and frames().
        """
    def increment(self) -> int:
        """self.increment() -> int

        return the increment between two frames.
        """
    def isInRange(self, n: Any) -> int:
        """self.isInRange(n) -> int

        return if the frame is inside the range.
        """
    def last(self) -> int:
        """self.last() -> int

        return the last frame of the range.
        """
    def maxFrame(self) -> int:
        """self.maxFrame() -> int

        return the maximum frame define in the range.
        """
    def minFrame(self) -> int:
        """self.minFrame() -> int

        return the minimum frame define in the range.
        """
    def setFirst(self, n: Any) -> None:
        """self.setFirst(n) -> None

        set the first frame of the range.
        """
    def setIncrement(self, n: Any) -> None:
        """self.setIncrement(n) -> None

        set the increment between two frames.
        """
    def setLast(self, n: Any) -> None:
        """self.setLast(n) -> None

        set the last frame of the range.
        """
    def stepFrame(self) -> int:
        """self.stepFrame() -> int

        return the absolute increment between two frames.
        """

class FrameRanges:
    """A sequence of FrameRange objects with convenience functions for iterating over all frames in all ranges."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Construct from a list of integers, FrameRange objects, or strings."""
    def __iter__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __len__(self, *args: Any, **kwargs: Any) -> int: ...
    def __str__(self, *args: Any, **kwargs: Any) -> str: ...
    def add(self, r: Any) -> None:
        """add(r) -> None

        add a new frame range.
        """
    def clear(self) -> None:
        """clear() -> None

        reset all store frame ranges.
        """
    def compact(self) -> None:
        """compact() -> None

        compact all the frame ranges.
        """
    def getRange(self) -> FrameRange:
        """getRange()-> FrameRange

        return a range from the list
        """
    def maxFrame(self) -> int:
        """maxFrame() -> int

        get maximum frame of all ranges.
        """
    def minFrame(self) -> int:
        """minFrame() -> int

        get minimum frame of all ranges.
        """
    def size(self) -> int:
        """size() -> int

        return the ranges number.
        """
    def toFrameList(self) -> list[int]:
        """toFrameList() -> [int]

        return a list of frames in a vector
        """

class FreeType_Knob(Knob):
    """A knob which holds a font family and style name."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getValue(self) -> list[str]:
        """self.getValue() -> [String, String]

        Returns the font family/style on this knob.

        :return: [String, String].
        """
    def setValue(self, family: str, style: int) -> None:
        """self.setValue(family,style) -> None.

        Change font family/style with a new one.

        :param family: String of the font family name.
        :param style: String of the font style name.
        :param filename: Font filename.
        :param index: Face index.
        :raises: It raises an exception if the font is not available.
        :return: None.
        """

@final
class GeoSelect_Knob(Knob):
    """A knob which allows selection of parts of a 3D object."""
    def getFaceWeights(self) -> tuple[list, ...]:
        """self.getFaceWeights() -> list of lists of floats
        Returns the selection weight for each face as a float. If you access the result as selection[obj][fc], then obj is the index of the object in the input geometry and fc is the index of the face in that object.
        """
    def getGeometry(self) -> _nuke_internal_geo.GeometryList:
        """self.getGeometry() -> _geo.GeometryList
        Get the geometry which this knob can select from.
        """
    def getSelectedFaces(self) -> tuple[list, ...]:
        """self.getSelectedFaces() -> list of lists of floats
        Returns the selection for each face as a float. If you access the result as selection[obj][fc], then obj is the index of the object in the input geometry and fc is the index of the face in that object.
        """
    def getSelection(self) -> tuple[list, ...]:
        """self.getSelection() -> list of lists of floats
        Returns the selection for each vertex as a float. If you access the result as selection[obj][pt], then obj is the index of the object in the input geometry and pt is the index of the point in that object.
        """
    def getSelectionWeights(self) -> tuple[list, ...]:
        """self.getSelectionWeights() -> list of lists of floats
        Returns the selection weights for each vertex as a float. If you access the result as selection[obj][pt], then obj is the index of the object in the input geometry and pt is the index of the point in that object. LALA
        """

class GeoSelection:
    def __getitem__(self, arg0: str) -> Any:
        """__getitem__(self: _nuke.GeoSelection, arg0: str) -> Foundry::Python::GeoSelectionItem"""
    def __init__(self) -> None:
        """__init__(self: _nuke.GeoSelection) -> None"""
    def __iter__(self) -> Any:
        """__iter__(self: _nuke.GeoSelection) -> collections.abc.Iterator[Foundry::Python::GeoSelectionItem]"""
    def __len__(self) -> int:
        """__len__(self: _nuke.GeoSelection) -> int"""
    def selectFaces(self, primPath: str, faces: Any, faceWeights: Any = ...) -> None:
        """selectFaces(self: _nuke.GeoSelection, primPath: str, faces: collections.abc.Sequence[typing.SupportsFloat], faceWeights: collections.abc.Sequence[typing.SupportsFloat] = []) -> None

        Select faces, also sets face weights if given
        """
    def selectObject(self, arg0: str) -> None:
        """selectObject(self: _nuke.GeoSelection, arg0: str) -> None"""
    def selectVertices(self, primPath: str, vertices: Any, vertexWeights: Any = ...) -> None:
        """selectVertices(self: _nuke.GeoSelection, primPath: str, vertices: collections.abc.Sequence[typing.SupportsFloat], vertexWeights: collections.abc.Sequence[typing.SupportsFloat] = []) -> None

        Select vertices, also sets vertex weights if given
        """

class GeoSelectionItem:
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getFaceWeights(self) -> list[float]:
        """getFaceWeights(self: _nuke.GeoSelectionItem) -> list[float]"""
    def getFaces(self) -> list[float]:
        """getFaces(self: _nuke.GeoSelectionItem) -> list[float]"""
    def getObject(self) -> bool:
        """getObject(self: _nuke.GeoSelectionItem) -> bool"""
    def getPath(self) -> Any:
        """getPath(self: _nuke.GeoSelectionItem) -> object"""
    def getVertexWeights(self) -> list[float]:
        """getVertexWeights(self: _nuke.GeoSelectionItem) -> list[float]"""
    def getVertices(self) -> list[float]:
        """getVertices(self: _nuke.GeoSelectionItem) -> list[float]"""
    def getWorldNormals(self, arg0: object, time: SupportsFloat = ...) -> list[Any]:
        """getWorldNormals(self: _nuke.GeoSelectionItem, arg0: object, time: typing.SupportsFloat = nan) -> list[_nukemath.Vector3]"""
    def getWorldPoints(self, arg0: object, time: SupportsFloat = ...) -> list[Any]:
        """getWorldPoints(self: _nuke.GeoSelectionItem, arg0: object, time: typing.SupportsFloat = nan) -> list[_nukemath.Vector3]"""

class Group(Node):
    def __enter__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __exit__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __str__(self, /) -> str:
        """Return str(self)."""
    def begin(self) -> Group:
        """self.begin() -> Group.
        All python code that follows will be executed in the context of node. All names are evaluated relative to this object. Must be paired with end.
        @return: Group.
        """
    def connectSelectedNodes(self, backward: Any, inputA: Any) -> None:
        """self.connectSelectedNodes(backward, inputA) -> None.
        Connect the selected nodes.
        @param backward.
        @param inputA.
        @return: None.
        """
    def end(self) -> None:
        """self.end() -> None.
        All python code that follows will no longer be executed in the context of node. Must be paired with begin.
        @return: None.
        """
    def expand(self) -> None:
        """self.expand() -> None.
        Moves all nodes from the group node into its parent group, maintaining node input
        and output connections, and deletes the group.
        Returns the nodes that were moved, which will also be selected.
        @return: None.
        """
    def findNode(self, name: Any) -> Node:
        """self.findNode(name) -> Node
        Find the first node who's local name matches string 'name', including any clones.
        Assumes the string contains only the node's local name, not the full path of the node which may contain parents or expressions.@param s: A string.
        @return: Node with local name matching string 'name', or None if not found.
        """
    def node(self, s: str) -> Any:
        """self.node(s) -> Node with name s or None.
        Locate a node by name.
        @param s: A string.
        @return: Node with name s or None.
        """
    def nodes(self) -> list[Node]:
        """self.nodes() -> List of nodes
        List of nodes in group.
        @return: List of nodes
        """
    def numNodes(self) -> int:
        """self.numNodes() -> Number of nodes
        Number of nodes in group.
        @return: Number of nodes
        """
    def output(self) -> Node | None:
        """self.output() -> Node or None.
        Return output node of group.
        @return: Node or None.
        """
    def run(self, callable: Callable[..., Any], arg2: tuple = ..., arg3: dict = ...) -> Any:
        """self.run(callable) -> Result of callable.
        Execute in the context of node. All names are evaluated relative to this object.
        @param callable: callable to execute.
        @return: Result of callable.
        """
    def selectedNode(self) -> Node | None:
        """self.selectedNode() -> Node or None.
        Returns the node the user is most likely thinking about. This is the last node the user clicked on, if it is selected.  Otherwise it is an 'output' (one with no selected outputs) of the set of selected nodes. If no nodes are selected then None is returned.
        @return: Node or None.
        """
    def selectedNodes(self) -> list[Node]:
        """self.selectedNodes() -> Node or None.
        Selected nodes.
        @return: Node or None.
        """
    def splaySelectedNodes(self, backward: bool, inputA: bool) -> None:
        """self.splaySelectedNodes(backward, inputA) -> None.
        Splay the selected nodes.
        @param backward.
        @param inputA.
        @return: None.
        """
    def subgraphLocked(self) -> bool: ...

class Gizmo(Group):
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __str__(self, /) -> str:
        """Return str(self)."""
    def command(self) -> str:
        """self.command() -> String.
        Gizmo command.
        @return: String.
        """
    def filename(self) -> str:
        """self.filename() -> String.
        Gizmo filename.
        @return: String.
        """
    def makeGroup(self) -> Group:
        """self.makeGroup() -> Group
        Creates a Group node copy of the Gizmo node.
        @return: Group.
        """

@final
class GlobalsEnvironment:
    """Dictionary-style object holding global Nuke state.
    Example:
    nuke.env['threads'] = 4
    """
    def __contains__(self, *args: Any, **kwargs: Any) -> bool: ...
    def __delitem__(self, key: Any, /) -> None:
        """Delete self[key]."""
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __setitem__(self, key: Any, value: Any, /) -> None:
        """Set self[key] to value."""
    def get(self, *args: Any, **kwargs: Any) -> Any: ...
    def has_key(self, *args: Any, **kwargs: Any) -> Any: ...
    def items(self, *args: Any, **kwargs: Any) -> Any: ...
    def keys(self, *args: Any, **kwargs: Any) -> Any: ...
    def values(self, *args: Any, **kwargs: Any) -> Any: ...
    def __new__(cls, *args: Any, **kwargs: Any) -> GlobalsEnvironment: ...

class Gsv_Knob(Knob):
    """A knob which holds the Graph Variables created within the scope of this group.

    GSV knobs show variables inherited from parent groups.  If these are modified
    then the inherited variables are overridden once they reach the scope of this
    group. In addition, the root group node shows the variables introduced by all
    groups in the script.  This allows the root node to update GSVs within all
    VariableGroups.  Note that VariableGroup scoped variables are still held by
    their respective groups; renaming or removing the VariableGroups will rename
    or remove all the GSV within the VariableGroup scope.
    """
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addGsv(self, path: str, value: str, dataType: Any = ..., listOptions: list = ...) -> bool:
        """addGsv(path, value, dataType, listOptions) -> bool

        Add the Graph Scope Variable.

        @param path:
          The path to the GSV.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @param value: The value of the Graph Scope Variable.
        @type value: str
        @param dataType: The type of data to store in the GSV (string/integer/list).
        @type dataType: nuke.gsv.DataType, optional
        @param listOptions: The available options for a list variable.
        @type listOptions: list, optional
        @raise RuntimeError: If the knob is locked.
        @raise ValueError: If the knob is read only.
        @return: True if the GSV was added successfully.
        @rtype: bool

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.Variable_01'
          value = 'Clip1234'
          knob.addGsv(path, value)
        """
    def addGsvSet(self, path: str) -> bool:
        """addGsvSet(path) -> bool

        Add a GSV set to the containing group.

        @param path:
          The path to the GSV set.
          The path format is ``[GroupName.][GroupName...]SetName``.
        @type path: str
        @raise RuntimeError: If the knob is locked.
        @raise ValueError: If the knob is read only.
        @return: True if the GSV set was successfully added.
        @rtype: bool

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01'
          knob.addGsvSet(path)
        """
    def contains(self, path: str) -> bool:
        """contains(path) -> bool

        Return True if the path exist relative to the GSV knob.

        This function does not make distinction between the element types for
        the given path i.e. the path must include the GSV set name when checking
        for a variable in the `__default__` variable set.

        @param path:
          The path to test.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @raise RuntimeError: If the knob is locked.
        @raise ValueError: If the knob is read only.
        @return: Return True if the path exist relative to the GSV knob.
        @rtype: bool

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.Variable_01'
          knob.contains(path)
        """
    def containsGsv(self, path: str) -> bool:
        """containsGsv(path) -> bool

        Return True if the path exist relative to the GSV knob.

        This function does not make distinction between the element types for
        the given path i.e. the path must include the GSV set name when checking
        for a variable in the `__default__` variable set.

        @param path:
          The path to test.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @raise RuntimeError: If the knob is locked.
        @raise ValueError: If the knob is read only.
        @return: Return True if the path exist relative to the GSV knob.
        @rtype: bool

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.Variable_01'
          knob.containsGsv(path)
        """
    def containsGsvSet(self, path: str) -> bool:
        """containsGsvSet(path) -> bool

        Return True if the path to the GSV set exists relative to the GSV knob.

        @param path:
          The path to test.
          The path format is ``[GroupName.][GroupName...]SetName``.
        @type path: str
        @raise RuntimeError: If the knob is locked.
        @raise ValueError: If the knob is read only.
        @return: Return True if the path exist relative to the GSV knob.
        @rtype: bool

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01'
          knob.containsGsvSet(path)
        """
    def getDataType(self, path: str) -> Any:
        """getDataType(path) -> nuke.gsv.DataType

        Return the data type of the GSV.

        @param path:
          The path to the GSV.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @return: The type of data stored in the GSV (string/integer/list).
        @rtype: nuke.gsv.DataType

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.Variable_01'
          dataType = knob.getDataType(path)
        """
    def getGsvValue(self, path: str) -> str:
        """getGsvValue(path) -> str

        Return the value of the Graph Scope Variable.

        @param path:
          The path to the GSV.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @return: Return the value of the Graph Scope Variable.
        @rtype: str

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.Variable_01'
          value = knob.getGsvValue(path)
        """
    def getLabel(self) -> str:
        """getLabel() -> str

        Return the label for the GSV.

        @param path:
          The path to the GSV.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @return: Return the label for the GSV.
        @rtype: str

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.Variable_01'
          label = knob.getLabel(path)
        """
    def getListOptions(self, path: str) -> list:
        """getListOptions(path) -> list

        Return the value options for a list GSV.

        @param path:
          The path to the GSV.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @raise ValueError: If the path does not point to a list GSV.
        @return: Return the value options for a list GSV.
        @rtype: list

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.Variable_01'
          listOptions = knob.getListOptions(path)
        """
    def getTooltip(self) -> str:
        """getTooltip() -> str

        Return the tooltip for the GSV.

        @param path:
          The path to the GSV.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @return: Return the tooltip for the GSV.
        @rtype: str

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.Variable_01'
          tooltip = knob.getTooltip(path)
        """
    def getValue(self) -> dict:
        """getValue() -> dict

        Return the GSV sets.

        @return:
          GSV sets as a dictionary of dictionaries.
          Keys are the set names (including `__default__`).
          Values are dictionaries of the variables.
          Variables are returned as ``{variable_name: variable_value}``.
        @rtype: dict

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          sets = knob.getValue()
        """
    def isFavorite(self, path: str) -> bool:
        """isFavorite(path) -> bool

        Return True if the GSV under this path is marked as a favorite.

        Favorite variables are shown in Nuke's Variables Panel.

        @param path:
          The path to the GSV.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @return: Return True if the GSV under this path is marked as a favorite.
        @rtype: bool

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.Variable_01'
          knob.isFavorite(path)
        """
    def label(self) -> str:
        """label() -> str

        Return the label for the GSV.

        @param path:
          The path to the GSV.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @return: Return the label for the GSV.
        @rtype: str

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.Variable_01'
          label = knob.label(path)
        """
    def removeGsv(self, path: str) -> bool:
        """removeGsv(path) -> bool

        Remove a GSV from the containing variable set.

        @param path:
          The path to the GSV.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @raise RuntimeError: If the knob is locked.
        @raise ValueError: If the knob is read only.
        @return: True if the GSV was successfully removed.
        @rtype: bool

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.Variable_01'
          knob.removeGsv(path)
        """
    def removeGsvSet(self, path: str) -> bool:
        """removeGsvSet(path) -> bool

        Remove a GSV set from the containing group.

        @param path:
          The path to the GSV set.
          The path format is ``[GroupName.][GroupName...]SetName``.
        @type path: str
        @raise RuntimeError: If the knob is locked.
        @raise ValueError: If the knob is read only.
        @return: True if the GSV set was successfully added.
        @rtype: bool

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01'
          knob.removeGsvSet(path)
        """
    def renameGsv(self, path: str, name: str) -> bool:
        """renameGsv(path, name) -> bool

        Rename a GSV.

        @param path:
          The path to the GSV.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @param name: The new variable name.
        @type name: str
        @raise RuntimeError: If the knob is locked.
        @raise ValueError: If the knob is read only.
        @return: True if the GSV was successfully renamed.
        @rtype: bool

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.OldVariableName'
          knob.renameGsv(path, 'NewVariableName')
        """
    def renameGsvSet(self, path: str, name: str) -> bool:
        """renameGsvSet(path, name) -> bool

        Rename a GSV set.

        @param path:
          The path to the GSV set.
          The path format is ``[GroupName.][GroupName...]SetName``.
        @type path: str
        @param name: The new variable set name.
        @type name: str
        @raise RuntimeError: If the knob is locked.
        @raise ValueError: If the knob is read only.
        @return: True if the GSV set was successfully renamed.
        @rtype: bool

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.OldVariableSet'
          knob.renameGsvSet(path, 'NewVariableSet')
        """
    def setDataType(self, path: str, value: Any) -> bool:
        """setDataType(path, value) -> bool

        Set the data type of the GSV.

        @param path:
          The path to the GSV.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @param value: The type of data stored in the GSV (string/integer/list).
        @type value: nuke.gsv.DataType
        @raise RuntimeError: If the knob is locked.
        @raise ValueError: If the knob is read only.
        @return: True if the data type was set successfully.
        @rtype: bool

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.Variable_01'
          knob.setDataType(path, nuke.gsv.DataType.List)
        """
    def setFavorite(self, path: str, value: bool) -> bool:
        """setFavorite(path, value) -> bool

        Set the favorite property of a GSV.

        @param path:
          The path to the GSV.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @param value:
          True to add to favorites.
          False to remove from favorites.
        @type value: bool
        @raise RuntimeError: If the knob is locked.
        @raise ValueError: If the knob is read only.
        @return: True if the favorite property was successfully updated.
        @rtype: bool

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.Variable_01'
          knob.setFavorite(path, True)
        """
    def setGsvValue(self, path: str, value: str, dataType: Any = ..., listOptions: list = ...) -> bool:
        """setGsvValue(path, value, dataType, listOptions) -> bool

        Set the value of the Graph Scope Variable.

        @param path:
          The path to the GSV.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @param value: The value of the Graph Scope Variable.
        @type value: str
        @param dataType: The type of data to store in the GSV (string/integer/list).
        @type dataType: nuke.gsv.DataType, optional
        @param listOptions: The available options for a list variable.
        @type listOptions: list, optional
        @raise RuntimeError: If the knob is locked.
        @raise ValueError: If the knob is read only.
        @return: True if the GSV was set successfully.
        @rtype: bool

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.Variable_01'
          value = 'Clip1234'
          knob.setGsvValue(path, value)
        """
    def setLabel(self, path: str, value: str) -> bool:
        """setLabel(path, value) -> bool

        Set the label for the GSV.

        @param path:
          The path to the GSV.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @param value: The label text.
        @type value: str
        @raise RuntimeError: If the knob is locked.
        @raise ValueError: If the knob is read only.
        @return: True if the label was set successfully.
        @rtype: bool

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.Variable_01'
          knob.setLabel(path, 'Custom Label')
        """
    def setListOptions(self, path: str, list: list) -> bool:
        """setListOptions(path, list) -> bool

        Set the value options for a list GSV.

        @param path:
          The path to the GSV.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @param list: List of value options
        @type list: list
        @raise RuntimeError: If the knob is locked.
        @raise ValueError: If the knob is read only.
        @return: True if the value options were set successfully.
        @rtype: bool

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.Variable_01'
          knob.setListOptions(path, ['shot01', 'shot02'])
        """
    def setTooltip(self, path: str, value: str) -> bool:
        """setTooltip(path, value) -> bool

        Set the tooltip for the GSV.

        @param path:
          The path to the GSV.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @param value: The tooltip text.
        @type value: str
        @raise RuntimeError: If the knob is locked.
        @raise ValueError: If the knob is read only.
        @return: True if the label was set successfully.
        @rtype: bool

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.Variable_01'
          knob.setTooltip(path, 'Custom Tooltip')
        """
    def setValue(self, value: dict) -> None:
        """self.setValue(value) -> None

        Set the GSV sets as a dictionary of dictionaries.

        @param value:
          GSV sets as a dictionary of dictionaries.
          Keys are the set names (including `__default__`).
          Values are dictionaries of the variables.
          Variable are set as ``{variable_name: variable_value}``.
        @type value: dict
        @raise RuntimeError: If the knob is locked.
        @raise ValueError: If the knob is read only.

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          knob.setValue(
            {
              '__default__': {'dk1': 'dv1', 'dk2': 'dv2'},
              'Custom': {'ck1': 'cv1', 'ck2': 'cv2'}
            }
          )
        """
    def tooltip(self) -> str:
        """tooltip() -> str

        Return the tooltip for the GSV.

        @param path:
          The path to the GSV.
          The path format is ``[GroupName.][GroupName...]SetName.VariableName``.
        @type path: str
        @return: Return the tooltip for the GSV.
        @rtype: str

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          path = 'VariableGroup1.VariableSet_01.Variable_01'
          tooltip = knob.tooltip(path)
        """
    def value(self) -> dict:
        """value() -> dict

        Return the GSV sets.

        @return:
          GSV sets as a dictionary of dictionaries.
          Keys are the set names (including `__default__`).
          Values are dictionaries of the variables.
          Variables are returned as ``{variable_name: variable_value}``.
        @rtype: dict

        *Example*::

          root = nuke.root()
          knob = root['gsv']
          sets = knob.value()
        """

@final
class Hash:
    """A hash value for any number of objects.

    The append() method is used to add objects to the hash; the value will be recomputed efficiently as each new object is added.
    """
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def append(self, arg1: Any, /) -> Any:
        """Add another value to the hash."""
    def getHash(self) -> int:
        """Get the current value of the hash."""
    def reset(self, *args: Any, **kwargs: Any) -> Any:
        """Reset the hash."""
    def setHash(self, arg1: int, /) -> Any:
        """Set the current value of the hash."""
    def __new__(cls, *args: Any, **kwargs: Any) -> Hash: ...

class Help_Knob(Knob):
    """Help_Knob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class Histogram_Knob(Knob):
    """Histogram_Knob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class IArray_Knob(Array_Knob):
    """IArray_Knob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def dimensions(self) -> int:
        """Return number of dimensions."""
    def height(self) -> int:
        """Return height of the array."""
    def value(self, arg1: int = ..., arg2: int = ..., /) -> float:
        """Return value of the array at position (x, y)."""
    def width(self) -> int:
        """Return width of the array."""

class Info:
    """An info object stores x, y, w and h values."""
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def h(self) -> float:
        """self.h() -> float

        Return height.
        """
    def w(self) -> float:
        """self.w() -> float

        Return width.
        """
    def x(self) -> float:
        """x() -> float

        Return left edge.
        """
    def y(self) -> float:
        """self.y() -> float

        Return the bottom edge.
        """

class Int_Knob(Array_Knob):
    """A knob which holds one or more integer values."""
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def setValue(self, val: int) -> bool:
        """self.setValue(val) -> bool
        Set the integer value of this knob.
        @param val: The new value. Must be an integer.
        @return: True if succeeded, False otherwise.
        """
    def value(self) -> int:
        """self.value() -> int
        Get the integer value of this knob.
        @return: The value of this knob as an int.
        """

class Keyer_Knob(Array_Knob):
    """Keyer_Knob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def highSoft(self, arg1: OutputContext = ..., /) -> float: ...
    def highTol(self, arg1: OutputContext = ..., /) -> float: ...
    def lowSoft(self, arg1: OutputContext = ..., /) -> float: ...
    def lowTol(self, arg1: OutputContext = ..., /) -> float: ...
    def names(self, n: int) -> str:
        """self.names(n) -> string

        @param n: The index of the name to return.
        @return: The name at position n.
        """
    def value(self, outputCtx: int = ..., n: OutputContext = ...) -> float:
        """self.value(outputCtx, n) -> float

        Get the value of argument n.
        @param outputCtx: The OutputContext to evaluate the argument in.
        @param n: The index of the argument to get the value of.
        @return: The value of argument n.
        """

@final
class KnobType:
    """Constants for use in parameters which require a knob type."""
    eAColorKnob: int
    eArrayKnob: int
    eAxisKnob: int
    eBBoxKnob: int
    eBitMaskKnob: int
    eBoolKnob: int
    eBox3Knob: int
    eCachedFileKnob: int
    eCancelExecutionKnob: int
    eCascadingEnumerationKnob: int
    eChannelKnob: int
    eChannelMaskKnob: int
    eColorChipKnob: int
    eColorKnob: int
    eColorspaceKnob: int
    eControlPointCollectionKnob: int
    eCpKnob: int
    eCustomKnob: int
    eDisableKnob: int
    eDoubleKnob: int
    eDynamicBitmaskKnob: int
    eEditableEnumerationKnob: int
    eEnumKnob: int
    eExoGroupKnob: int
    eEyeDropperKnob: int
    eFileKnob: int
    eFloatKnob: int
    eFormatKnob: int
    eFrameExtentKnob: int
    eFreeTypeKnob: int
    eGeoSelectKnob: int
    eHelpKnob: int
    eHistogramKnob: int
    eIconKnob: int
    eInputOnlyChannelKnob: int
    eInputOnlyChannelMaskKnob: int
    eIntKnob: int
    eKeyerKnob: int
    eLinkKnob: int
    eListKnob: int
    eLookupCurvesKnob: int
    eMenuKnob: int
    eMetaDataKnob: int
    eMetaKeyFrameKnob: int
    eMultiArrayKnob: int
    eMultiViewKnob: int
    eMultilineEvalStringKnob: int
    eMultilineStringKnob: int
    eObsoleteKnob: int
    eOneViewKnob: int
    eParticleChannelsKnob: int
    ePasswordKnob: int
    ePathExpressionKnob: int
    ePathKnob: int
    ePixelAspectKnob: int
    ePluginPythonKnob: int
    ePositionVectorKnob: int
    ePulldownKnob: int
    ePyPulldownKnob: int
    ePyScriptKnob: int
    ePythonKnob: int
    eRadioKnob: int
    eRangeKnob: int
    eResizableArrayKnob: int
    eRippleKnob: int
    eScaleKnob: int
    eSceneGraphKnob: int
    eSceneViewKnob: int
    eScriptKnob: int
    eSimpleArrayKnob: int
    eSizeKnob: int
    eSpacerKnob: int
    eStringKnob: int
    eTabGroupKnob: int
    eTabKnob: int
    eTableKnob: int
    eTextEditorKnob: int
    eTextKnob: int
    eToolbarKnob: int
    eToolboxKnob: int
    eTooltipKnob: int
    eTransform2DKnob: int
    eTransformJackKnob: int
    eUSDSceneGraphKnob: int
    eUVKnob: int
    eVSpacerKnob: int
    eVec2Knob: int
    eVec3Knob: int
    eVec4Knob: int
    eViewPairKnob: int
    eViewViewKnob: int
    eWHKnob: int
    eXYKnob: int
    eXYZKnob: int

class Layer:
    """A layer is a set of channels."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Construct a layer with a name and optional list of channel names."""
    def channels(self) -> list[str]:
        """self.channels() -> [string, ...]
        Get a list of the channels in this layer.

        @return: A list of strings, where each string is the name of a channel in this layer.
        """
    def name(self) -> str:
        """self.name() -> str
        Get the layer name.

        @return: The layer name, as a string.
        """
    def setName(self, newName: Any) -> None:
        """self.setName(newName) -> None
        Set the name of this layer.

        @param newName: The new name for this layer.
        """
    def visible(self) -> bool:
        """self.visible() -> bool
        Check whether the layer is visible.

        @return: True if visible, False if not.
        """

class Link_Knob(Knob):
    """Link_Knob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def applyOverride(self) -> bool:
        """applyOverride() -> bool
        This function only affects link knobs that are placed on a LiveGroup node. It replaces the value of the linked knob in the live group with the value set in the LiveGroup node.
        """
    def getLink(self) -> Any:
        """getLink() -> s"""
    def getLinkedKnob(self) -> Any:
        """getLinkedKnob() -> knob"""
    def makeLink(self, s: str, t: str) -> None:
        """makeLink(s, t) -> None"""
    def revertOverride(self) -> bool:
        """revertOverride() -> bool
        This function only affects link knobs that are placed on a LiveGroup node. When called the LinkKnob will revert to the linked knob value and will follow it after reloads.
        """
    def setLink(self, s: str) -> None:
        """setLink(s) -> None"""
    def setValue(self) -> None:
        """setValue() -> None

        Set value of knob.
        """
    def value(self, arg1: OutputContext = ...) -> str:
        """value() -> string

        Return value of knob.
        """

@final
class LinkableKnobInfo:
    """A linkable knob description. Holds a reference to a knob that may be linked to, as well as an indication whether this knob should be used as part of an absolute or relative expression and whether it is enabled."""
    def absolute(self) -> bool:
        """self.absolute() -> Boolean
        Returns whether the values of this knob should be treated as absolute or relative. This may be useful for positions.
        """
    def displayName(self) -> str:
        """self.displayName() -> String
        Returns the custom display name that will appear in Link-to menus.
        """
    def enabled(self) -> bool:
        """self.enabled() -> Boolean
        Returns whether the knob is currently enabled or not.
        """
    def indices(self) -> list:
        """self.indices() -> List
        Returns a list of the knob channels that should be used with this linkable knob.
        """
    def knob(self) -> Knob:
        """self.knob() -> Knob
        Returns the knob that may be linked to.
        """

class Precomp(Group):
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __str__(self, /) -> str:
        """Return str(self)."""
    def reload(self) -> None:
        """self.reload() -> None
        Precomp Node reload()
        @return: None
        """

class LiveGroup(Precomp):
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __str__(self, /) -> str:
        """Return str(self)."""
    def anyOverrides(self) -> bool:
        """anyOverrides() -> bool
        If any of the exposed link knobs are overridden it returns with True.
        """
    def applyOverrides(self, *args: Any, **kwargs: Any) -> Any:
        """applyOverride() -> bool
        This function only affects link knobs that are placed on a LiveGroup type node. It replaces the value of the linked knob in the live group with the value set in the LiveGroup node.
        """
    def isLocal(self) -> bool:
        """isLocal() -> bool
        Checks if the LiveGroup is local.WARNING: This function is deprecated. Use published() instead.
        """
    def makeEditable(self) -> None:
        """makeEditable() -> None
        Puts the LiveGroup into "editable" state.
        """
    def makeLocal(self) -> None:
        """makeLocal() -> None
        Puts the LiveGroup into "local" state.
        WARNING: This function is deprecated. Use makeEditable() instead.
        """
    def modified(self) -> bool:
        """modified() -> bool
        Returns True if the anything within the livegroup has changed.
        """
    def publish(self, *args: Any, **kwargs: Any) -> bool:
        """publishLiveGroup(file) -> bool

        Writes a LiveGroup to a file.

        :param file: (optional) The path to which we want to publish this LiveGroup. If None then write to the path currently defined by the file knob. If the file specified by this param already exists, Nuke will attempt to over write it without a warning. Otherwise a new file will be created.

        :return: bool. True if successful, else, False.
        """
    def published(self) -> bool:
        """published() -> bool
        Returns True if the LiveGroup is published.
        """
    def reload(self) -> None:
        """reload() -> None
        Reloads the livegroup from the livegroups source file. 
        """
    def revertOverrides(self, *args: Any, **kwargs: Any) -> Any:
        """revertOverride() -> bool
        This function only affects link knobs that are placed on a LiveGroup type node. When called the LinkKnob will revert to the linked knob value and will follow it after reloads.
        """

class LookupCurves_Knob(Knob):
    """Provide a set of user-editable lookup curves."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addCurve(self, curve: str, expr: str = ...) -> None:
        """self.addCurve(curve, expr=None) -> None
        Adds a curve.
        @param curve: The name of an animation curve, or an AnimationCurve instance.
        @param expr: Optional parameter giving an expression for the curve.
        @return: None
        """
    def delCurve(self, curve: str) -> None:
        """self.delCurve(curve) -> None
        Deletes a curve.
        @param curve: The name of the animation curve.
        @return: None
        """
    def editCurve(self, curve: str, expr: str = ...) -> None:
        """self.editCurve(curve, expr=None) -> None
        Edits an existing curve.
        @param curve: The name of an animation curve.
        @param expr: The new expression for the curve.
        @return: None
        """

class Lut:
    """Lut"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def fromByte(self, float: Any) -> float:
        """self.fromByte(float) -> float.

        Converts byte values in the range 0-255 to floating point.
        """
    def fromByteSingle(self, *args: Any, **kwargs: Any) -> Any:
        """self.fromByte(float) -> float.

        Converts byte values in the range 0-255 to floating point.
        """
    def fromFloat(self, src: Any, alpha: Any) -> Any:
        """fromFloat(src, alpha) -> float list.

        Convert a sequence of floating-point values to from_byte(x*255).
        Alpha is an optional argument and if present unpremultiply by alpha, convert, and then multiply back.
        """
    def isLinear(self) -> bool:
        """self.isLinear() -> True if toByte(x) appears to return x*255, False otherwise."""
    def isZero(self) -> bool:
        """self.isZero() -> True if toByte(0) returns a value <= 0, False otherwise."""
    def toByte(self, float: Any) -> float:
        """self.toByte(float) -> float.

        Converts floating point values to byte values in the range 0-255.
        """
    def toByteSingle(self, *args: Any, **kwargs: Any) -> Any:
        """self.toByte(float) -> float.

        Converts floating point values to byte values in the range 0-255.
        """
    def toFloat(self, src: Any, alpha: Any) -> Any:
        """toFloat(src, alpha) -> float list.

        Convert a sequence of floating-point values to to_byte(x)/255.
        Alpha is an optional argument and if present unpremultiply by alpha, convert, and then multiply back.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> Lut: ...

class MenuItem:
    """MenuItem"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def action(self) -> None:
        """self.action() -> None
        Get the action associated with this menu item.
        """
    def icon(self) -> str:
        """self.icon() -> String
        Returns the name of the icon on this menu item as path of the icon.
        """
    def invoke(self) -> None:
        """self.invoke() -> None
        Perform the action associated with this menu item.
        """
    def name(self) -> str:
        """self.name() -> String
        Returns the name of the menu item.
        """
    def script(self) -> str:
        """self.script() -> String
        Returns the script that gets executed for this menu item.
        """
    def setEnabled(self, enabled: Any, recursive: Any) -> None:
        """self.setEnabled(enabled, recursive) -> None
        Enable or disable the item.
        @param enabled: True to enable the object; False to disable it.
        @param recursive: True to also setEnabled on submenu actions.
        """
    def setIcon(self, icon: Any) -> None:
        """self.setIcon(icon) -> None
        Set the icon on this menu item.
        @param icon: the new icon as a path
        """
    def setScript(self, script: Any) -> None:
        """self.setScript(script) -> None
        Set the script to be executed for this menu item.
        Note: To call a python script file, you can use the execfile() function. i.e:
        menu.setScript("execfile('script.py')")
        """
    def setShortcut(self, keySequence: Any) -> None:
        """self.setShortcut(keySequence) -> None
        Set the keyboard shortcut on this menu item.
        @param keySequence: the new shortcut in PortableText format, e.g. "Ctrl+Shift+P\"
        """
    def setVisible(self, visible: Any) -> None:
        """self.setVisible(visible) -> None
        Show or hide the item.
        @param visible: True to show the object; False to hide it.
        """
    def shortcut(self) -> str:
        """self.shortcut() -> String
        Returns the keyboard shortcut on this menu item. The format of this is the PortableText format. It will return a string such as "Ctrl+Shift+P". Note that on Mac OS X the Command key is equivalent to Ctrl.
        """

@final
class Menu(MenuItem):
    """Menu"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def addAction(self, action: Any) -> bool:
        """self.addAction(action) -> bool
        Adds the QAction to the menu.
        """
    def addCommand(self, name: str, command: str | Callable[..., Any] = ..., shortcut: str = ..., icon: str = ..., tooltip: str = ..., index: int = ..., readonly: bool = ..., shortcutContext: int = ..., tag: Any = ..., tagTarget: Any = ..., node: str = ...) -> Any:
        """self.addCommand(name, command, shortcut, icon, tooltip, index, readonly, shortcutContext, tag, tagTarget, node) -> The menu/toolbar item that was added to hold the command.
        Add a new command to this menu/toolbar. Note that when invoked, the command is automatically enclosed in an undo group, so that undo/redo functionality works. Optional arguments can be specified by name.
        Note that if the command argument is not specified, then the command will be auto-created as a "nuke.createNode()" using the name argument as the node to create.
        Note: During startup this command can cause slowdown when using the custom toolset menu. To speedup the process include "icon='/'" as an argument, however, it'll show an empty spot next to each menu where icons are shown.

        Example:
        menubar = nuke.menu('Nuke')
        fileMenu = menubar.findItem('File')
        fileMenu.addCommand('NewCommand', 'print 10', shortcut='t')

        @param name: The name for the menu/toolbar item. The name may contain submenu names delimited by '/' or '', and submenus are created as needed.
        @param command: Optional. The command to add to the menu/toolbar. This can be a string to evaluate or a Python Callable (function, method, etc) to run.
        @param shortcut: Optional. The keyboard shortcut for the command, such as 'R', 'F5' or 'Ctrl-H'. Note that this overrides pre-existing other uses for the shortcut.
        @param icon: Optional. An icon for the command. This should be a path to an icon in the nuke.pluginPath() directory. If the icon is not specified, Nuke will automatically try to find an icon with the name argument and .png appended to it.
        @param tooltip: Optional. The tooltip text, displayed on mouseover for toolbar buttons.
        @param index: Optional. The position to insert the new item in, in the menu/toolbar. This defaults to last in the menu/toolbar.
        @param readonly: Optional. True/False for whether the item should be available when the menu is invoked in a read-only context.
        @param shortcutContext: Optional. Sets the shortcut context (0==Window, 1=Application, 2=DAG).
        @param tag: Optional. Sets the tag icon that is displayed on the menu/toolbar item (0==None, 1=Beta, 2=Classic).
        @param tagTarget: Optional. Determines which type of the menu/toolbar should display the specified tag (0==Unknown, 1=Beta, 2=TabMenu, 3=ContextMenu, 7=All).
        @param nodeClass: The NodeClass the tag should apply to.@return: The menu/toolbar item that was added to hold the command.
        """
    def addMenu(self, **kwargs: Any) -> Any:
        """self.addMenu(**kwargs) -> The submenu that was added.
        Add a new submenu.
        @param **kwargs The following keyword arguments are accepted:
                        name      The name for the menu/toolbar item
                        icon      An icon for the menu. Loaded from the nuke search path.
                        tooltip   The tooltip text.
                        index     The position to insert the menu in. Use -1 to add to the end of the menu.
                        tag       Optional. Sets the tag icon that is displayed on the menu/toolbar item (0==None, 1=Beta, 2=Classic).
        @return: The submenu that was added.
        """
    def addSeparator(self, **kwargs: Any) -> Any:
        """self.addSeparator(**kwargs) -> The separator that was created.
        Add a separator to this menu/toolbar.
        @param **kwargs The following keyword arguments are accepted:
        index     The position to insert the new separator in, in the menu/toolbar.
        @return: The separator that was created.
        """
    def clearMenu(self) -> bool:
        """self.clearMenu() 
        Clears a menu.
        @param **kwargs The following keyword arguments are accepted:
                        name      The name for the menu/toolbar item
        @return: true if cleared, false if menu not found 
        """
    def findItem(self, name: Any) -> Menu | None:
        """self.findItem(name) -> Menu or None
        Finds a submenu or command with a particular name.
        @param name: The name to search for.
        @return: The submenu or command we found, or None if we could not find anything.
        """
    def items(self) -> None:
        """self.items() -> None
        Returns a list of sub menu items.
        """
    def menu(self, name: Any) -> Menu | None:
        """self.menu(name) -> Menu or None
        Finds a submenu or command with a particular name.
        @param name: The name to search for.
        @return: The submenu or command we found, or None if we could not find anything.
        """
    def name(self) -> str:
        """self.name() -> String
        Returns the name of the menu item.
        """
    def removeItem(self, name: Any) -> None:
        """self.removeItem(name) -> None
        Removes a submenu or command with a particular name. If the containing menu becomes empty, it will be removed too.
        @param name: The name to remove for.
        @return: true if removed, false if menu not found 
        """
    def updateMenuItems(self) -> None:
        """updateMenuItems() -> None
        Updates menu items' states. Call on about to show menu.
        """

@final
class MenuBar:
    """MenuBar"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def addAction(self, action: Any) -> bool:
        """self.addAction(action) -> bool
        Adds the QAction to the menu.
        """
    def addCommand(self, name: str, command: str | Callable[..., Any] = ..., shortcut: str = ..., icon: str = ..., tooltip: str = ..., index: int = ..., readonly: bool = ..., shortcutContext: int = ..., tag: Any = ..., tagTarget: Any = ..., node: str = ...) -> Any:
        """self.addCommand(name, command, shortcut, icon, tooltip, index, readonly, shortcutContext, tag, tagTarget, node) -> The menu/toolbar item that was added to hold the command.
        Add a new command to this menu/toolbar. Note that when invoked, the command is automatically enclosed in an undo group, so that undo/redo functionality works. Optional arguments can be specified by name.
        Note that if the command argument is not specified, then the command will be auto-created as a "nuke.createNode()" using the name argument as the node to create.
        Note: During startup this command can cause slowdown when using the custom toolset menu. To speedup the process include "icon='/'" as an argument, however, it'll show an empty spot next to each menu where icons are shown.

        Example:
        menubar = nuke.menu('Nuke')
        fileMenu = menubar.findItem('File')
        fileMenu.addCommand('NewCommand', 'print 10', shortcut='t')

        @param name: The name for the menu/toolbar item. The name may contain submenu names delimited by '/' or '', and submenus are created as needed.
        @param command: Optional. The command to add to the menu/toolbar. This can be a string to evaluate or a Python Callable (function, method, etc) to run.
        @param shortcut: Optional. The keyboard shortcut for the command, such as 'R', 'F5' or 'Ctrl-H'. Note that this overrides pre-existing other uses for the shortcut.
        @param icon: Optional. An icon for the command. This should be a path to an icon in the nuke.pluginPath() directory. If the icon is not specified, Nuke will automatically try to find an icon with the name argument and .png appended to it.
        @param tooltip: Optional. The tooltip text, displayed on mouseover for toolbar buttons.
        @param index: Optional. The position to insert the new item in, in the menu/toolbar. This defaults to last in the menu/toolbar.
        @param readonly: Optional. True/False for whether the item should be available when the menu is invoked in a read-only context.
        @param shortcutContext: Optional. Sets the shortcut context (0==Window, 1=Application, 2=DAG).
        @param tag: Optional. Sets the tag icon that is displayed on the menu/toolbar item (0==None, 1=Beta, 2=Classic).
        @param tagTarget: Optional. Determines which type of the menu/toolbar should display the specified tag (0==Unknown, 1=Beta, 2=TabMenu, 3=ContextMenu, 7=All).
        @param nodeClass: The NodeClass the tag should apply to.@return: The menu/toolbar item that was added to hold the command.
        """
    def addMenu(self, **kwargs: Any) -> Any:
        """self.addMenu(**kwargs) -> The submenu that was added.
        Add a new submenu.
        @param **kwargs The following keyword arguments are accepted:
                        name      The name for the menu/toolbar item
                        icon      An icon for the menu. Loaded from the nuke search path.
                        tooltip   The tooltip text.
                        index     The position to insert the menu in. Use -1 to add to the end of the menu.
                        tag       Optional. Sets the tag icon that is displayed on the menu/toolbar item (0==None, 1=Beta, 2=Classic).
        @return: The submenu that was added.
        """
    def addSeparator(self, **kwargs: Any) -> Any:
        """self.addSeparator(**kwargs) -> The separator that was created.
        Add a separator to this menu/toolbar.
        @param **kwargs The following keyword arguments are accepted:
        index     The position to insert the new separator in, in the menu/toolbar.
        @return: The separator that was created.
        """
    def clearMenu(self) -> bool:
        """self.clearMenu() 
        Clears a menu.
        @param **kwargs The following keyword arguments are accepted:
                        name      The name for the menu/toolbar item
        @return: true if cleared, false if menu not found 
        """
    def findItem(self, name: Any) -> Menu | None:
        """self.findItem(name) -> Menu or None
        Finds a submenu or command with a particular name.
        @param name: The name to search for.
        @return: The submenu or command we found, or None if we could not find anything.
        """
    def items(self) -> None:
        """self.items() -> None
        Returns a list of sub menu items.
        """
    def menu(self, name: Any) -> Menu | None:
        """self.menu(name) -> Menu or None
        Finds a submenu or command with a particular name.
        @param name: The name to search for.
        @return: The submenu or command we found, or None if we could not find anything.
        """
    def name(self) -> str:
        """self.name() -> String
        Returns the name of the menu item.
        """
    def removeItem(self, name: Any) -> None:
        """self.removeItem(name) -> None
        Removes a submenu or command with a particular name. If the containing menu becomes empty, it will be removed too.
        @param name: The name to remove for.
        @return: true if removed, false if menu not found 
        """
    def updateMenuItems(self) -> None:
        """updateMenuItems() -> None
        Updates menu items' states. Call on about to show menu.
        """

class MultiView_Knob(Knob):
    """MultiView_Knob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def fromScript(self, s: str) -> bool:
        """fromScript(s) -> True if succeeded, False otherwise.

        Initialise from script s.
        """
    def setValue(self, arg1: str, /) -> Any:
        """fromScript(s) -> True if succeeded, False otherwise.

        Initialise from script s.
        """
    def toScript(self, quote: Any = ..., context: OutputContext | None = ...) -> str:
        """toScript(quote, context=current) -> string.

        Return the value of the knob in script syntax.
        Pass True for quote to return results quoted in {}.
        Pass None for context to get results for all views and key times (as stored in a .nk file).
        """
    def toScriptPrefixUserKnob(self) -> str: ...
    def value(self, arg1: Any = ..., arg2: OutputContext | None = ..., /) -> str:
        """toScript(quote, context=current) -> string.

        Return the value of the knob in script syntax.
        Pass True for quote to return results quoted in {}.
        Pass None for context to get results for all views and key times (as stored in a .nk file).
        """

class Multiline_Eval_String_Knob(EvalString_Knob):
    """A knob which evaluates it's string value as a TCL expression. It provides a multiline text area when it appears in a Node panel."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def maxScrollValue(self) -> int:
        """self.maxScrollValue() -> int.
        Return the maximum value for the vertical scrollbar.
        @return: int with maximum value, or 0 if scrollbar not present.
        """
    def scrollTo(self, value: int) -> None:
        """self.scrollTo(value) -> None.
        Set the vertical scrollbar value.
        @param value: The new scrollbar value.
        @return: None.
        """

class NodeConstructor:
    """NodeConstructor"""
    def __call__(self, /, *args: Any, **kwargs: Any) -> Any:
        """Call self as a function."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __new__(cls, *args: Any, **kwargs: Any) -> NodeConstructor: ...

class Nodes:
    """Nodes"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __new__(cls, *args: Any, **kwargs: Any) -> Nodes: ...

class Obsolete_Knob(Knob):
    """For internal use only."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def setValue(self, *args: Any, **kwargs: Any) -> Any: ...
    def value(self, *args: Any, **kwargs: Any) -> Any: ...

class OneView_Knob(Enumeration_Knob):
    """OneView_Knob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __new__(cls, *args: Any, **kwargs: Any) -> OneView_Knob: ...

class OutputContext:
    """Describes a context in which expressions can be evaluated."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Construct with a frame number.
        Construct with a frame number and view.
        """
    def frame(self) -> float:
        """frame() -> float

        Return frame value.
        """
    def setFrame(self, f: Any) -> bool:
        """setFrame(f) -> True

        Set frame value. The f argument is a float.
        """
    def setView(self, n: Any) -> bool:
        """setView(n) -> True

        Set view number. The n argument is an integer in the range of 0 to number of views.
        """
    def view(self) -> int:
        """view() -> int

        Return view number.
        """
    def viewFromName(self, name: Any) -> int:
        """viewFromName(name) -> int

        Returns the index of the view with name matching the argument name or -1 if there is no match.
        """
    def viewcount(self) -> int:
        """viewcount() -> int

        Return number of views.
        """
    def viewname(self, n: Any) -> str:
        """viewname(n) -> string

        Return name of the view. The n argument is an integer in the range of 0 to number of views.
        """
    def viewshort(self, n: Any) -> str:
        """viewshort(n) -> string

        Return short name of the view. The n argument is an integer in the range of 0 to number of views.
        """

@final
class Panel:
    """Panel"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def addBooleanCheckBox(self, name: Any, value: Any) -> bool:
        """self.addBooleanCheckBox(name, value) -> True if successful.
        Add a boolean check box knob to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
    def addButton(self, name: Any, value: Any) -> bool:
        """self.addButton(name, value) -> True if successful.
        Add a button to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
    def addClipnameSearch(self, name: Any, value: Any) -> bool:
        """self.addClipnameSearch(name, value) -> True if successful.
        Add a clipname search knob to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
    def addEnumerationPulldown(self, name: Any, value: Any) -> bool:
        """self.addEnumerationPulldown(name, value) -> True if successful.
        Add a pulldown menu to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
    def addExpressionInput(self, name: Any, value: Any) -> bool:
        """self.addExpressionInput(name, value) -> True if successful.
        Add an expression evaluator to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
    def addFilenameSearch(self, name: Any, value: Any) -> bool:
        """self.addFilenameSearch(name, value) -> True if successful.
        Add a filename search knob to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
    def addMultilineTextInput(self, name: Any, value: Any) -> bool:
        """self.addMultilineTextInput(name, value) -> True if successful.
        Add a multi-line text knob to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
    def addNotepad(self, name: Any, value: Any) -> bool:
        """self.addNotepad(name, value) -> True if successful.
        Add a text edit widget to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
    def addPasswordInput(self, name: Any, value: Any) -> bool:
        """self.addPasswordInput(name, value) -> True if successful.
        Add a password input knob to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
    def addRGBColorChip(self, name: Any, value: Any) -> bool:
        """self.addRGBColorChip(name, value) -> True if successful.
        Add a color chooser to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
    def addScriptCommand(self, name: Any, value: Any) -> bool:
        """self.addScriptCommand(name, value) -> True if successful.
        Add a script command evaluator to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
    def addSingleLineInput(self, name: Any, value: Any) -> bool:
        """self.addSingleLineInput(name, value) -> True if successful.
        Add a single-line input knob to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
    def addTextFontPulldown(self, name: Any, value: Any) -> bool:
        """self.addTextFontPulldown(name, value) -> True if successful.
        Add a font chooser to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
    def clear(self) -> None:
        """self.clear() -> None
        Clear all panel attributes.
        """
    def execute(self, name: Any) -> Any:
        """self.execute(name) -> The result of the script as a string, or None if it fails.
        Execute the script command associated with a particular label and return the result as a string.
        @param name: The name of the script field to execute.
        @return: The result of the script as a string, or None if it fails.
        """
    def setTitle(self, val: Any) -> bool:
        """self.setTitle(val) -> True if successful.
        Set the current title for the panel.
        @param val: The title as a string.
        @return: True if successful.
        """
    def setWidth(self, val: Any) -> bool:
        """self.setWidth(val) -> True if successful.
        Set the width of the panel.
        @param val: The width as an int.
        @return: True if successful.
        """
    def show(self) -> Any:
        """self.show() -> An int value indicating how the dialog was closed (normally, or cancelled).
        Display the panel.
        @return: An int value indicating how the dialog was closed (normally, or cancelled).
        """
    def title(self) -> Any:
        """self.title() -> The title as a string.
        Get the current title for the panel.
        @return: The title as a string.
        """
    def value(self, name: Any) -> Any:
        """self.value(name) -> The value for the field if any, otherwise None.
        Get the value of a particular control in the panel.
        @param name: The name of the knob to get a value from.
        @return: The value for the field if any, otherwise None.
        """
    def width(self) -> Any:
        """self.width() -> The width as an int.
        Get the width of the panel.
        @return: The width as an int.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> Panel: ...

class PanelNode:
    """PanelNode"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __str__(self, /) -> str:
        """Return str(self)."""
    def addKnob(self, k: Knob) -> None:
        """self.addKnob(k) -> None.
        Add knob k to this node or panel.
        @param k: Knob.
        @return: None.
        """
    def createWidget(self, *args: Any, **kwargs: Any) -> Any:
        """Create the widget for the panel"""
    def knobs(self) -> dict:
        """self.knobs() -> dict

        Get a dictionary of (name, knob) pairs for all knobs in this node.

        For example:

           >>> b = nuke.nodes.Blur()
           >>> b.knobs()

        @return: Dictionary of all knobs.

        Note that this doesn't follow the links for Link_Knobs/Obsolete_Knobs
        """
    def readKnobs(self, s: Any) -> None:
        """self.readKnobs(s) -> None.
        Read the knobs from a string (TCL syntax).
        @param s: A string.
        @return: None.
        """
    def removeKnob(self, k: Knob) -> None:
        """self.removeKnob(k) -> None.
        Remove knob k from this node or panel. Throws a ValueError exception if k is not found on the node.
        @param k: Knob.
        @return: None.
        """
    def writeKnobs(self, i: Any = ...) -> Any:
        """self.writeKnobs(i) -> String in .nk form.
        Return a tcl list. If TO_SCRIPT | TO_VALUE is not on, this is a simple list
        of knob names. If it is on, it is an alternating list of knob names
        and the output of to_script().

        Flags can be any of these or'd together:
        - nuke.TO_SCRIPT produces to_script(0) values
        - nuke.TO_VALUE produces to_script(context) values
        - nuke.WRITE_NON_DEFAULT_ONLY skips knobs with not_default() false
        - nuke.WRITE_USER_KNOB_DEFS writes addUserKnob commands for user knobs
        - nuke.WRITE_ALL writes normally invisible knobs like name, xpos, ypos

        @param i: The set of flags or'd together. Default is TO_SCRIPT | TO_VALUE.
        @return: String in .nk form.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> PanelNode: ...

class ParticleChannels_Knob(Knob):
    """ParticleChannels_Knob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def setValue(self, v: int) -> bool:
        """self.setValue(v) -> bool
        Set the ParticleChannels value of this knob.
        @param v: int convertible object.
        @return: True if modified, False otherwise.
        """
    def value(self) -> int:
        """self.value() -> int
        Get the ParticleChannels value for this knob.
        @return: Particle channels as integer.
        """

class Password_Knob(Knob):
    """A knob which holds a password string value. Appears as a password entry field in a Node panel."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getText(self) -> str:
        """self.getText() -> string

        Return text associated with knob.
        """
    def setValue(self, val: str | None, view: str | None = ...) -> None:
        """self.setValue(val, view='default') -> None

        Set value of knob.
        @param val: The new value.
        @param view: Optional parameter specifying which view to set the value for. If omitted, the value will be set for the default view.
        @return: None
        """
    def value(self, arg1: OutputContext = ...) -> str:
        """self.value() -> str

        Get the value of this knob as a string.
        @return: String value.
        """

class Path_Knob(EvalString_Knob):
    """Stores a Prim path."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def inWarning(self) -> bool:
        """self.inWarning() -> bool

        Returns True if the knob currently has a warning set on it, False otherwise.
        """
    def stagePaths(self) -> list:
        """self.stagePaths() -> list

        Returns a list of paths (strings) in the stage.
        """

class PathExpression_Knob(Path_Knob):
    """Stores a Prim path expression."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def match(self, pattern: str) -> list:
        """self.match(pattern: str) -> list

        Returns a list of paths (strings) that match the given stage using the pattern expression.
        """

class ProgressTask:
    """Progress Task."""
    kDefaultFlags: int
    kDelayedPopup: int
    kDisable: int
    kKeepWhenFinished: int
    kModal: int
    kShowTimeToGo: int
    kUseCallback: int
    kUserCanCancel: int
    kUserCanPause: int
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """ProgressTask.

        @param name: The title of the progress task.
        @param maximum: The maximum progress value (default 100).
        @param flags: Bitwise combination of flag constants (default kUserCanCancel | kShowTimeToGo).
        """
    def isCancelled(self) -> bool:
        """self.isCancelled() -> True if the user has requested the task to be cancelled."""
    def setMessage(self, s: Any) -> None:
        """self.setMessage(s) -> None.

        set the message for the progress task
        """
    def setProgress(self, i: Any) -> None:
        """self.setProgress(i) -> None.

        i is an integer representing the current progress
        """

class Pulldown_Knob(Enumeration_Knob):
    """Pulldown_Knob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def commands(self, n: int) -> str:
        """commands(n) -> string

        Return command n. The argument n is an integer and in the range of 0 and numValues.
        """
    def itemName(self, n: int) -> str:
        """itemName(n) -> string

        Return name of item n. The argument n is an integer and in the range of 0 and numValues.
        """
    def numValues(self) -> int:
        """numValues() -> int

        Return number of values.
        """
    def setValues(self, items: Any = ...) -> None:
        """self.setValues(items) -> None.
        (Re)initialise knob to the list of items.
        @param items: Dictionary of name/value pairs.
        @param sort: Optional parameter as to whether to sort the names.
        @return: None.
        Example:
        w = nuke.nodes.NoOp()
        k = nuke.Pulldown_Knob('kname', 'klabel')
        k.setValues({'label/command' : 'eval("3*2")'})
        w.addKnob(k)
        k = w['kname']
        """
    def value(self, arg1: int = ..., /) -> tuple[str, ...]: ...

class PyCustom_Knob(Script_Knob):
    """PyCustom_Knob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getObject(self) -> Any:
        """Returns the custom knob object as created in the by the 'command' argument to the PyCuston_Knob constructor."""

class PyScript_Knob(Script_Knob):
    """PyScript_Knob(name, label=None, command=None)
    A button that executes a Python script.
    """
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class PythonCustomKnob(Script_Knob):
    """PythonCustomKnob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getObject(self, *args: Any, **kwargs: Any) -> Any:
        """Returns the custom knob object as created in the by the 'command' argument to the PyCuston_Knob constructor."""

class PythonKnob(String_Knob):
    """A string-valued knob which evaluates its value as a Python expression."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class Radio_Knob(Enumeration_Knob):
    """Stores a single value between 0 and some maximum, and manages a
    set of Radio Buttons visible to the user. This is essentially an
    Enumeration_Knob with a different widget.
    """
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def enumName(self, n: int) -> str:
        """self.enumName(n) -> string

        Return name of enumeration n. The argument n is an integer and in the range of 0 and numValues. Deprecated.
        """
    def getDisplayStrFromID(self) -> Any:
        """self.getDisplayStrFromID()
        returns the display text for the associated id
        @param id: the id you want to retrieve the display text for
        @return: String containing the display text, example scene_linear (linear)
        Example:
        displayStr = knob.getDisplayStrFromID('scene_linear')
        """
    def numValues(self) -> int:
        """self.numValues() -> int

        Return number of values. Deprecated.
        """
    def setValue(self, item: str | float) -> None:
        """self.setValue(item) -> None.
        Set the current value. item will first be converted into a string and matched against the enum values.
        If this fails, it will attempt to be used as an index into the enum.
        @param item: String or Integer.
        @return: None.
        Example:
        w = nuke.nodes.Write()
        k = w['file_type']
        k.setValue('exr')
        """
    def setValues(self, items: Sequence[Any]) -> None:
        """self.setValues(items) -> None.
        (Re)initialise knob to the supplied list of items.
        @param items: The new list of values.
        @return: None.
        Example:
        w = nuke.nodes.Write()
        k = w['file_type']
        k.setValues(['exr'])
        """
    def value(self) -> str:
        """self.value() -> String.
        Current value.
        @return: String.
        Example:
        w = nuke.nodes.Write()
        k = w['file_type']
        k.value()
        """
    def values(self) -> list[str]:
        """self.values() -> List of strings.
        Return list of items.
        @return: List of strings.
        Example:
        w = nuke.nodes.Write()
        k = w['file_type']
        k.values()
        """

class Range_Knob(Array_Knob):
    """A knob which the minimum and maximum for a range of values."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class Root(Group):
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __str__(self, /) -> str:
        """Return str(self)."""
    def addView(self, name: str | int | View, color: str = ...) -> None:
        """self.addView(name, color) -> None.
        Add view.
        @param name: String - name of view.
        @param color: Optional. String in the format #RGB, #RRGGBB, #RRRGGGBBB, #RRRRGGGGBBBB or a name from the list of colors defined in the list of SVG color keyword names.
        @return: None.
        """
    def canSetInput(self, *args: Any, **kwargs: Any) -> Any: ...
    @classmethod
    def channels(cls) -> list[str]:
        """nuke.Root.channels() -> Channel list.
        Class method.
        @return: Channel list.
        """
    def clones(self, *args: Any, **kwargs: Any) -> Any: ...
    def connectInput(self, *args: Any, **kwargs: Any) -> Any: ...
    def deleteView(self, s: Any) -> None:
        """self.deleteView(s) -> None.
        Delete view.
        @param s: Name of view.
        @return: None.
        """
    def firstFrame(self) -> int:
        """self.firstFrame() -> Integer.
        First frame.
        @return: Integer.
        """
    def fps(self) -> int:
        """self.fps() -> integer
        Return the FPS rounded to an int. This is deprecated. Please use real_fps().
        """
    def getOCIOColorspaceFamily(self, colorspace: Any) -> Any:
        """nuke.root.getOCIOColorspaceFamily(colorspace) -> Family of colorspace
        Gets the name of the family to which the specified colorspace belongs,
        for the root node's current OCIO config.
        @param colorspace: Colorspace name.
        @return: Family name, may be an empty string.
        """
    def getOCIOColorspaceFromViewTransform(self, display: Any, view: Any) -> Any:
        """nuke.root.getOCIOColorspaceFromViewTransform(display, view) -> Colorspace name
        Gets the name of the colorspace to which the specified display and view names are mapped
        for the root node's current OCIO config.
        @param display: Display name.
        @param view: View name.
        @return: The corresponding colorspace name.
        """
    def input(self, *args: Any, **kwargs: Any) -> Any: ...
    def inputs(self, *args: Any, **kwargs: Any) -> Any: ...
    def lastFrame(self) -> int:
        """self.lastFrame() -> Integer.
        Last frame.
        @return: Integer.
        """
    @classmethod
    def layers(cls) -> list[Layer]:
        """nuke.Root.layers() -> Layer list.
        Class method.
        @return: Layer list.
        """
    def maximumInputs(self, *args: Any, **kwargs: Any) -> Any: ...
    def maximumOutputs(self, *args: Any, **kwargs: Any) -> Any: ...
    def mergeFrameRange(self, a: int, b: int) -> None:
        """self.mergeFrameRange(a, b) -> None.
        Merge frame range.
        @param a: Low-end of interval range.
        @param b: High-end of interval range.
        @return: None.
        """
    def minimumInputs(self, *args: Any, **kwargs: Any) -> Any: ...
    def modified(self) -> bool:
        """self.modified() -> True if modified, False otherwise.
        Get or set the 'modified' flag in a script
        @return: True if modified, False otherwise.
        """
    def optionalInput(self, *args: Any, **kwargs: Any) -> Any: ...
    def proxy(self) -> bool:
        """self.proxy() -> True if proxy is set, False otherwise.
        @return: True if proxy is set, False otherwise.
        """
    def realFps(self) -> float:
        """self.realFps() -> float
        The global frames per second setting.
        """
    def setFrame(self, n: float) -> None:
        """self.setFrame(n) -> None.
        Set frame.
        @param n: Frame number.
        @return: None.
        """
    def setInput(self, *args: Any, **kwargs: Any) -> Any: ...
    def setModified(self, b: Any) -> None:
        """self.setModified(b) -> None.
        Set the 'modified' flag in a script.
        Setting the value will turn the indicator in the title bar on/off and will start or stop the autosave timeout.
        @param b: Boolean convertible object.
        @return: None.
        """
    def setProxy(self, b: Any) -> None:
        """self.setProxy(b) -> None.
        Set proxy.
        @param b: Boolean convertible object.
        @return: None.
        """
    def setView(self, s: str | int | View) -> None:
        """self.setView(s) -> None.
        Set view.
        @param s: Name of view.
        @return: None.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> Root: ...

@final
class RunInMainThread:
    """RunInMainThread"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    @classmethod
    def request(cls, arg1: Callable[..., Any] = ..., arg2: tuple = ..., arg3: dict = ..., arg4: Any = ..., /) -> Any: ...
    @classmethod
    def result(cls, arg1: int, /) -> Any: ...

class Scale_Knob(Array_Knob):
    """Scale_Knob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def names(self, n: int) -> str:
        """names(n) -> string

        Return name for dimension n. The argument n is an integer.
        """
    def value(self, n: int = ..., oc: OutputContext = ...) -> float:
        """value(n, oc) -> float

        Return value for dimension n. The optional argument oc is an OutputContext.
        """
    def x(self, oc: OutputContext = ...) -> float:
        """x(oc) -> float

        Return value for x. The optional oc argument is an OutputContext
        """
    def y(self, oc: OutputContext = ...) -> float:
        """y(oc) -> float

        Return value for y. The optional oc argument is an OutputContext
        """
    def z(self, oc: OutputContext = ...) -> float:
        """z(oc) -> float

        Return value for z. The optional oc argument is an OutputContext
        """

class SceneGraph_Knob(Unsigned_Knob):
    """Displays a list of items as a hierarchy.
    The hierarchy is specified using back or forward slashes within the item names
    to specify their level in the tree. Handles multiple selection of items within the tree.
    """
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addItems(self, *args: Any, **kwargs: Any) -> None:
        """self.addItems([(name1, type1), (name2, type2), ...], autoSelect=false) -> None\\n

        Adds to the existing list of items that can be selected on the knob.

        :param items: sequence of string tuples (name, type) .
        :param autoSelect: If True, all items are automatically set as selected.
        :return: None.
        """
    def getItems(self) -> Any:
        """self.getItems() -> tuple of strings (name, type) 

        Returns a tuple of string tuples (name, type).
        """
    def getSelectedItems(self) -> list:
        """self.getSelectedItems() -> list

        :return: list of strings containing all currently selected items in the knob.
        """
    def removeItems(self, name1: Any = ..., name2: Any = ..., *args: Any) -> None:
        """self.removeItems([name1, name2, ...]) -> None

        Removes a list of string names from the knob.
        """
    def setItems(self, *args: Any, **kwargs: Any) -> None:
        """self.setItems([(name1, type1), (name2, type2), ...], autoSelect=false) -> None

        Sets the list of items that can be selected on the knob.

        :param items: sequence of string tuples (name, type) .
        :param autoSelect: If True, all items are automatically set as imported and selected.
        :return: None.
        """
    def setSelectedItems(self, name1: Any = ..., name2: Any = ..., *args: Any) -> None:
        """self.setSelectedItems([name1, name2, ...]) -> None

        :param items: sequence of strings - names of the items in the list .
        :return: None.
        """

class SceneView_Knob(Unsigned_Knob):
    """Displays a list of items as a hierarchy.
    The hierarchy is specified using back or forward slashes within the item names
    to specify their level in the tree. Handles multiple selection of items within the tree.
    """
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addItems(self) -> None:
        """self.addItems() -> None

        Adds a list of string items to the knob. New items are automatically set as imported and selected.
        """
    def getAllItems(self) -> list:
        """self.getAllItems() -> list

        Returns a list of strings containing all items that the knob can import.
        """
    def getHighlightedItem(self) -> str:
        """self.getHighlightedItem() -> string

        Returns a string containing the item which is currently highlighted.
        """
    def getImportedItems(self) -> list:
        """self.getImportedItems() -> list

        Returns a list of strings containing all items imported into the knob.
        """
    def getSelectedItems(self) -> list:
        """self.getSelectedItems() -> list

        Returns a list of strings containing all currently selected items in the knob.
        """
    def removeItems(self) -> None:
        """self.removeItems() -> None

        Removes a list of string items from the knob.
        """
    def setAllItems(self, items: Any, autoSelect: Any) -> None:
        """self.setAllItems(items, autoSelect) -> None

        Sets a list of strings containing all items that the knob can import.
        After calling this function, only items from this list can be imported into the nosde.

        :param items: List of imported items.
        :param autoSelect: If True, all items are automatically set as imported and selected.
        :return: None.
        """
    def setImportedItems(self, items: Any) -> None:
        """self.setImportedItems(items) -> None\\n

        Sets a list of strings containing all items imported into the knob. This will overwrite the current imported items list.

        :param items: List of imported items.
        :return: None.
        """
    def setSelectedItems(self) -> None:
        """self.setSelectedItems() -> None

        Takes a list of strings of items contained in the knob and sets them as selected.
        """

class Tab_Knob(Knob):
    """Groups subsequent knobs onto a tab."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def setValue(self, arg1: bool, /) -> Any: ...
    def value(self) -> bool: ...
    def __new__(cls, *args: Any, **kwargs: Any) -> Tab_Knob: ...

class Text_Knob(Knob):
    """A knob which holds a string value."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def setValue(self, arg1: str, /) -> Any: ...
    def value(self) -> str: ...

@final
class ToolBar:
    """ToolBar"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def addAction(self, action: Any) -> bool:
        """self.addAction(action) -> bool
        Adds the QAction to the menu.
        """
    def addCommand(self, name: Any, command: Any = ..., shortcut: Any = ..., icon: Any = ..., tooltip: Any = ..., index: Any = ..., readonly: Any = ..., shortcutContext: Any = ..., tag: Any = ..., tagTarget: Any = ..., node: Any = ...) -> Any:
        """self.addCommand(name, command, shortcut, icon, tooltip, index, readonly, shortcutContext, tag, tagTarget, node) -> The menu/toolbar item that was added to hold the command.
        Add a new command to this menu/toolbar. Note that when invoked, the command is automatically enclosed in an undo group, so that undo/redo functionality works. Optional arguments can be specified by name.
        Note that if the command argument is not specified, then the command will be auto-created as a "nuke.createNode()" using the name argument as the node to create.
        Note: During startup this command can cause slowdown when using the custom toolset menu. To speedup the process include "icon='/'" as an argument, however, it'll show an empty spot next to each menu where icons are shown.

        Example:
        menubar = nuke.menu('Nuke')
        fileMenu = menubar.findItem('File')
        fileMenu.addCommand('NewCommand', 'print 10', shortcut='t')

        @param name: The name for the menu/toolbar item. The name may contain submenu names delimited by '/' or '', and submenus are created as needed.
        @param command: Optional. The command to add to the menu/toolbar. This can be a string to evaluate or a Python Callable (function, method, etc) to run.
        @param shortcut: Optional. The keyboard shortcut for the command, such as 'R', 'F5' or 'Ctrl-H'. Note that this overrides pre-existing other uses for the shortcut.
        @param icon: Optional. An icon for the command. This should be a path to an icon in the nuke.pluginPath() directory. If the icon is not specified, Nuke will automatically try to find an icon with the name argument and .png appended to it.
        @param tooltip: Optional. The tooltip text, displayed on mouseover for toolbar buttons.
        @param index: Optional. The position to insert the new item in, in the menu/toolbar. This defaults to last in the menu/toolbar.
        @param readonly: Optional. True/False for whether the item should be available when the menu is invoked in a read-only context.
        @param shortcutContext: Optional. Sets the shortcut context (0==Window, 1=Application, 2=DAG).
        @param tag: Optional. Sets the tag icon that is displayed on the menu/toolbar item (0==None, 1=Beta, 2=Classic).
        @param tagTarget: Optional. Determines which type of the menu/toolbar should display the specified tag (0==Unknown, 1=Beta, 2=TabMenu, 3=ContextMenu, 7=All).
        @param nodeClass: The NodeClass the tag should apply to.@return: The menu/toolbar item that was added to hold the command.
        """
    def addMenu(self, **kwargs: Any) -> Any:
        """self.addMenu(**kwargs) -> The submenu that was added.
        Add a new submenu.
        @param **kwargs The following keyword arguments are accepted:
                        name      The name for the menu/toolbar item
                        icon      An icon for the menu. Loaded from the nuke search path.
                        tooltip   The tooltip text.
                        index     The position to insert the menu in. Use -1 to add to the end of the menu.
                        tag       Optional. Sets the tag icon that is displayed on the menu/toolbar item (0==None, 1=Beta, 2=Classic).
        @return: The submenu that was added.
        """
    def addSeparator(self, **kwargs: Any) -> Any:
        """self.addSeparator(**kwargs) -> The separator that was created.
        Add a separator to this menu/toolbar.
        @param **kwargs The following keyword arguments are accepted:
        index     The position to insert the new separator in, in the menu/toolbar.
        @return: The separator that was created.
        """
    def clearMenu(self) -> bool:
        """self.clearMenu() 
        Clears a menu.
        @param **kwargs The following keyword arguments are accepted:
                        name      The name for the menu/toolbar item
        @return: true if cleared, false if menu not found 
        """
    def findItem(self, name: Any) -> Menu | None:
        """self.findItem(name) -> Menu or None
        Finds a submenu or command with a particular name.
        @param name: The name to search for.
        @return: The submenu or command we found, or None if we could not find anything.
        """
    def items(self) -> None:
        """self.items() -> None
        Returns a list of sub menu items.
        """
    def menu(self, name: Any) -> Menu | None:
        """self.menu(name) -> Menu or None
        Finds a submenu or command with a particular name.
        @param name: The name to search for.
        @return: The submenu or command we found, or None if we could not find anything.
        """
    def name(self) -> str:
        """self.name() -> String
        Returns the name of the menu item.
        """
    def removeItem(self, name: Any) -> None:
        """self.removeItem(name) -> None
        Removes a submenu or command with a particular name. If the containing menu becomes empty, it will be removed too.
        @param name: The name to remove for.
        @return: true if removed, false if menu not found 
        """
    def updateMenuItems(self) -> None:
        """updateMenuItems() -> None
        Updates menu items' states. Call on about to show menu.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> ToolBar: ...

class Transform2d_Knob(Knob):
    """Transform2d_Knob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def value(self, oc: OutputContext = ...) -> Any:
        """value(oc) -> matrix

        Return transformation matrix. The argument oc is an OutputContext. Both arguments are optional.
        """

class USDSceneGraphKnob(Knob):
    """A knob which allows selection of a USD prim from a USD file."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def showPopup(self) -> Any:
        """showPopup(self) -> void

        Show the popup to customise the USD stage.
        """

class Vec2_Knob(Array_Knob):
    """A knob that stores 2 numbers with custom labels."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def names(self, n: int) -> str:
        """names(n) -> string

        Return name for dimension n. The argument n is an integer.
        """
    def x(self, oc: OutputContext = ...) -> float:
        """x(oc) -> float

        Return value for x. The optional oc argument is an OutputContext
        """
    def x_at(self, t: float = ...) -> float:
        """x_at(t) -> float

        Return value for x at a time t. The optional t is a float.
        """
    def y(self, oc: OutputContext = ...) -> float:
        """y(oc) -> float

        Return value for y. The optional oc argument is an OutputContext
        """
    def y_at(self, t: float = ...) -> float:
        """y_at(t) -> float

        Return value for y at a time t. The optional t is a float.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> Vec2_Knob: ...

class UV_Knob(Vec2_Knob):
    """A knob which describes a texture coordinate."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class Undo:
    """Manages Nuke's undo/redo system.

    All methods are class-level and can be called on the type directly (e.g. ``nuke.Undo.begin()``) or on an instance.  An ``Undo`` instance can also be used as a context manager: the ``with`` block opens an undo group on entry and closes it on exit.

    Example::

        with nuke.Undo():
            nuke.Undo.name('My Operation')
            # ... make changes ...
    """
    def __enter__(self, *args: Any, **kwargs: Any) -> Any:
        """Open an undo group.  Accepts an optional string label (same as begin()).
        The ``as`` target will be None.
        """
    def __exit__(self, *args: Any, **kwargs: Any) -> Any:
        """Close the undo group opened by __enter__."""
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    @staticmethod
    def begin(name: Any = ...) -> None:
        """begin(name=None) -> None

        Begin a new user-visible group of undo actions.

        @param name: Optional label shown in the Edit menu.  Can be set or
                     overridden later with name().
        """
    @staticmethod
    def cancel() -> None:
        """cancel() -> None

        Undo every action recorded in the current group and discard it.

        No entry is added to the undo stack.  Safe to call when no group is open (no-op in that case).
        """
    @staticmethod
    def disable() -> None:
        """disable() -> None

        Increment the disable counter, suppressing undo recording.

        Each call must be matched by a corresponding enable().  The counter
        is clamped at zero by enable() so it can never go negative.
        """
    @staticmethod
    def disabled() -> bool:
        """disabled() -> bool

        Return True if the undo system is currently suppressed.
        """
    @staticmethod
    def enable() -> None:
        """enable() -> None

        Decrement the disable counter (clamped at zero).

        Undo recording resumes once the counter reaches zero.
        """
    @staticmethod
    def end() -> None:
        """end() -> None

        Complete the current undo group and add it to the undo stack.

        Empty groups (no recorded actions) are discarded silently.
        """
    @staticmethod
    def name(name: Any) -> None:
        """name(name) -> None

        Set or override the label of the current undo group.

        Unlike the C++ API, the Python binding always applies the name (forceSetName=true), so this will override a label set by begin().

        @param name: New label string.
        """
    @staticmethod
    def new() -> None:
        """new() -> None

        Same as end();begin().

        Commits the current group to the undo stack and immediately opens a
        fresh unnamed group, producing two separate undo entries for actions
        recorded before and after the call.
        """
    @staticmethod
    def redo() -> None:
        """redo() -> None

        Redo the most recently undone operation.
        """
    @staticmethod
    def redoDescribe(n: Any) -> str:
        """redoDescribe(n) -> str

        Return a short description of the nth redo entry (0 = most recent).
        Returns an empty string if n is out of range.
        """
    @staticmethod
    def redoDescribeFully(n: Any) -> str:
        """redoDescribeFully(n) -> str

        Return a long description of the nth redo entry (0 = most recent).
        Returns an empty string if n is out of range.
        """
    @staticmethod
    def redoSize() -> int:
        """redoSize() -> int

        Number of redo operations available.
        """
    @staticmethod
    def redoTruncate(n: Any = ...) -> None:
        """redoTruncate(n=0) -> None

        Destroy all redo entries at index >= n.
        """
    @staticmethod
    def undo() -> None:
        """undo() -> None

        Undo the most recent operation.
        """
    @staticmethod
    def undoDescribe(n: Any) -> str:
        """undoDescribe(n) -> str

        Return a short description of the nth undo entry (0 = most recent).
        Returns an empty string if n is out of range.
        """
    @staticmethod
    def undoDescribeFully(n: Any) -> str:
        """undoDescribeFully(n) -> str

        Return a long description of the nth undo entry (0 = most recent).
        Returns an empty string if n is out of range.
        """
    @staticmethod
    def undoSize() -> int:
        """undoSize() -> int

        Number of undo operations available.
        """
    @staticmethod
    def undoTruncate(n: Any = ...) -> None:
        """undoTruncate(n=0) -> None

        Destroy all undo entries at index >= n.
        """

class Vec3_Knob(Array_Knob):
    """A knob that stores 3 numbers with custom labels."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def names(self, n: int) -> str:
        """names(n) -> string

        Return name for dimension n. The argument n is an integer.
        """
    def x(self, oc: OutputContext = ...) -> float:
        """x(oc) -> float

        Return value for x. The optional oc argument is an OutputContext
        """
    def x_at(self, t: float = ...) -> float:
        """x_at(t) -> float

        Return value for x at a time t. The optional t is a float.
        """
    def y(self, oc: OutputContext = ...) -> float:
        """y(oc) -> float

        Return value for y. The optional oc argument is an OutputContext
        """
    def y_at(self, t: float = ...) -> float:
        """y_at(t) -> float

        Return value for y at a time t. The optional t is a float.
        """
    def z(self, oc: OutputContext = ...) -> float:
        """z(oc) -> float

        Return value for z. The optional oc argument is an OutputContext
        """
    def z_at(self, t: float = ...) -> float:
        """z_at(t) -> float

        Return value for z at a time t. The optional t is a float.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> Vec3_Knob: ...

class Vec4_Knob(Array_Knob):
    """A knob that stores 4 numbers with custom labels."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def names(self, n: int) -> str:
        """names(n) -> string

        Return name for dimension n. The argument n is an integer.
        """
    def w(self, oc: OutputContext = ...) -> float:
        """w(oc) -> float

        Return value for w. The optional oc argument is an OutputContext
        """
    def w_at(self, t: float = ...) -> float:
        """w_at(t) -> float

        Return value for w at a time t. The optional t is a float.
        """
    def x(self, oc: OutputContext = ...) -> float:
        """x(oc) -> float

        Return value for x. The optional oc argument is an OutputContext
        """
    def x_at(self, t: float = ...) -> float:
        """x_at(t) -> float

        Return value for x at a time t. The optional t is a float.
        """
    def y(self, oc: OutputContext = ...) -> float:
        """y(oc) -> float

        Return value for y. The optional oc argument is an OutputContext
        """
    def y_at(self, t: float = ...) -> float:
        """y_at(t) -> float

        Return value for y at a time t. The optional t is a float.
        """
    def z(self, oc: OutputContext = ...) -> float:
        """z(oc) -> float

        Return value for z. The optional oc argument is an OutputContext
        """
    def z_at(self, t: float = ...) -> float:
        """z_at(t) -> float

        Return value for z at a time t. The optional t is a float.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> Vec4_Knob: ...

class View:
    """A named view."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Construct a view from its name.
        Construct a view from its index.
        Construct the default view.
        Construct a view by copying another view.
        """
    def __repr__(self, *args: Any, **kwargs: Any) -> str: ...
    def __str__(self, *args: Any, **kwargs: Any) -> str: ...
    def string(self) -> Any:
        """self.string() -> Name of view.
        @return: Name of view.
        """
    def value(self) -> Any:
        """self.value() -> Value of view.
        @return: Value of view.
        """

class ViewView_Knob(Knob):
    """ViewView_Knob"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class Viewer(Node):
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __str__(self, /) -> str:
        """Return str(self)."""
    def capture(self, file: str) -> None:
        """capture(file) -> None

        Capture the viewer image to a file.  Only jpg files are supported at present.  The image is captured immediately even if the viewer is mid-render.To capture a fully rendered image at a frame or frame range use nuke.render passing in the viewer node you want to capture.When using nuke.render the filename is specified by the 'file' knob on the viewer node.
        """
    def frameCached(self, f: Any = ...) -> bool:
        """frameCached(f) -> Bool

        Determine whether frame /f/ is known to be in the memory cache.
        """
    def getZoomLevel(self) -> float:
        """self.getZoomLevel() -> float
        Get viewer zoom level.
        @return: float.
        """
    def isPlayingOrRecording(self) -> bool:
        """isPlayingOrRecording() -> Bool 

        @return: Is a recording being made or played?
        """
    def pauseUpdates(self, value: Any) -> bool:
        """self.pauseUpdates(value) -> Bool

        Sets the viewer pauseUpdates state to value.
        """
    def playbackRange(self) -> FrameRange:
        """self.playbackRange() -> FrameRange.
        Return the frame range that's currently set to be played back in the viewer.@return: FrameRange.
        """
    def recordMouse(self) -> bool:
        """recordMouse() -> Bool

        Start viewer window mouse recording.@return: Recording started?
        """
    def recordMouseStop(self) -> Any:
        """recordMouseStop()

        Stop viewer window mouse recording.
        """
    def replayMouseAsync(self, xmlRecordingFilename: Any = ...) -> bool:
        """replayMouseAsync(xmlRecordingFilename) -> Bool

        Start timer based (asynchronous) playback of a viewer window mouse recording.@param: Name of recording xml file to play@return: Replay started?
        """
    def replayMouseSync(self, xmlRecordingFilename: Any) -> bool:
        """replayMouseSync(xmlRecordingFilename) -> Bool

        Start direct (synchronous) playback of a viewer window mouse recording.@param: Name of recording xml file to play@return: Replay succeeded?
        """
    def roi(self) -> dict:
        """self.roi() -> dict
        Region of interest set in the viewer in pixel space coordinates.
        Returns None if the Viewer has no window yet.
        @return: Dict with keys x, y, r and t or None.
        """
    def roiEnabled(self) -> bool:
        """self.roiEnabled() -> bool
        Whether the viewing of just a region of interest is enabled.
        Returns None if the Viewer has no window yet.
        @return: Boolean or None.
        """
    def sendMouseEvent(self) -> bool:
        """sendMouseEvent() -> Bool

        Temporary:
        Post a mouse event to the viewer window.
        """
    def setRoi(self, box: Any = ...) -> None:
        """self.setRoi(box) -> None.
        Set the region of interest in pixel space.
        @param box: A dictionary with the x, y, r and t keys.@return: None.
        """
    def setZoomLevel(self, zoomLevel: Any = ..., center: bool = ...) -> None:
        """self.setZoomLevel(zoomLevel, center=True) -> None
        Set viewer zoom level. Includes an optional argument to center the view.
        @param zoomLevel: float representing zoom level as a percentage (e.g. 100.0 = 100%).
        @param center: Specifies whether to center the view alongside the zoom. Defaults to True.
        @return: None.
        """
    def toggleMouseTrails(self) -> bool:
        """toggleMouseTrails() -> Bool 

        Toggle mouse trails in the viewer window on/off.@return: Trails now showing?
        """
    def toggleWaitOnReplayEvents(self, *args: Any, **kwargs: Any) -> Any:
        """toggleWaitOnEvents() -> Bool 

        Toggle whether asynchronous playback waits on each event.
        Otherwise events will be handled by the next nuke update.@return: Now waiting?
        """
    def visibleRange(self) -> FrameRange:
        """self.visibleRange() -> FrameRange.
        Return the frame range that is currently visible in the viewer.@return: FrameRange.
        """

@final
class ViewerProcess:
    """ViewerProcess"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    @classmethod
    def node(cls, name: str | None = ..., viewer: str = ...) -> Node:
        """nuke.ViewerProcess.node(name, viewer) -> Node.

        Returns a ViewerProcess node. Default is to return the current selected one. This is a class method.

        :param name: Optional ViewerProcess name.
        :param viewer: Optional viewer name.
        :return: Node.
        """
    @classmethod
    def nodeMonitorOut(cls, name: str | None = ..., viewer: str = ...) -> Node:
        """nuke.ViewerProcess.nodeMonitorOut(name, viewer) -> Node.

        Returns a ViewerProcess node for Monitor Out. If a viewer has not been specified, returns the current selected one. This is a class method.

        :param name: Optional ViewerProcess name.
        :param viewer: Optional viewer name.
        :return: Node.
        """
    @classmethod
    def register(cls, name: Any, call: Any, args: Any, kwargs: Any = ...) -> None:
        """nuke.ViewerProcess.register(name, call, args, kwargs) -> None.

        Register a ViewerProcess. This is a class method.

        :param name: Menu name.
        :param call: Python callable. Must return a Node.
        :param args: Arguments to call.
        :param kwargs: Optional named arguments.
        :return: None.
        """
    @classmethod
    def registeredNames(cls) -> list[str]:
        """nuke.ViewerProcess.registeredNames() -> List.

        Returns a list containing the names of all currently regisered ViewerProcesses.

        :return: List.
        """
    @classmethod
    def restoreSelectionAfterReload(cls) -> None:
        """nuke.ViewerProcess.restoreSelectionAfterReload() -> None.

        Restores the viewer process selection after an OCIO or Nuke Config has been reloaded
        this is normally called after nuke.ViewerProcess.storeSelectionBeforeReload()

        :return: None.
        """
    @classmethod
    def storeSelectionBeforeReload(cls) -> None:
        """nuke.ViewerProcess.storeSelectionBeforeReload() -> None.

        When the user reloads an OCIO or Nuke config the viewer process selection is stored in the the viewer process object
        Following the reload you can call nuke.ViewerProcess.restoreSelectionAfterReload() which will then restore the selection instead of the default.

        :return: None.
        """
    @classmethod
    def unregister(cls, name: Any) -> None:
        """nuke.ViewerProcess.unregister(name) -> None.

        Unregister a ViewerProcess. This is a class method.

        :param name: Menu name.
        :return: None.
        """

@final
class ViewerWindow:
    """ViewerWindow"""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def activateInput(self, input: Any, secondary: bool = ...) -> None:
        """self.activateInput(input, secondary=False) -> None
        Set the given viewer input to be active - i. e. show its image in the output window.
        @param input: The viewer input number, starting with 0 for the first.  If the input is not
        connected, a ValueError exception is raised.
        @param secondary: True if the input should be connected as the secondary (wipe) input, or
        False to connect it as the primary input (the default).
        @return: None
        """
    def activeInput(self, secondary: bool = ...) -> int:
        """self.activeInput(secondary=False) -> int
        Returns the currently active input of the viewer - i. e. the one with its image in the output window.
        @param secondary: True to return the index of the active secondary (wipe) input, or False (the default)
        to return the primary input.
        @return: int: The currently active input of the viewer, starting with 0 for the first, or None if no input is active.
        """
    def frameControl(self, i: Any) -> bool:
        """self.frameControl(i) -> True.

        i is an integer indicating viewer frame control 'button' to execute:

           -6 go to start
           -5 play reverse
           -4 go to previous keyframe
           -3 step back by increment
           -2 go back previous keyframe or increment, whichever is closer
           -1 step back one frame

            0 stop

           +1 step forward one frame
           +2 go to next keyframe or increment, whichever is closer
           +3 step forward by increment
           +4 go to next keyframe
           +5 play forward
           +6 go to end
        """
    def getCurrentErrorMessage(self) -> Any:
        """self.getCurrentErrorMessage() -> Error.
        Returns the error currently displayed in this viewer.
        @return: Error string if an error is present, otherwise None.
        """
    def getGLCameraMatrix(self) -> Any:
        """self.getGLCameraMatrix() -> Matrix4
        Return the world transformations of the current GL viewer camera.
        @return: Matrix4: GL camera world transformation.
        """
    def getGeometryNodes(self, *args: Any, **kwargs: Any) -> Nodes:
        """self.getGeometry() -> None
        Returns the a list of geometry nodes attached with this viewer
        @return: Nodes: a list of the geometry nodes.
        """
    def getStatusMessage(self) -> str:
        """self.getStatusMessage() -> str.
        @return: The status message in the viewer.
        """
    def hideStatusMessage(self) -> None:
        """self.hideStatusMessage() -> None.
        Hides the status message in the viewer.
        @return: None.
        """
    def isOverlayShown(self) -> bool:
        """self.isOverlayShown() -> Bool.
        @return: True if the overlay is visible, False otherwise.
        """
    def nextView(self) -> Any:
        """self.nextView() -> switch to next view in settings Views list."""
    def node(self) -> Node:
        """self.node() -> Node.
        Returns the Viewer node currently associated with this window.
        @return: Node.
        """
    def play(self, *args: Any, **kwargs: Any) -> Any:
        """Play forward (1) or reverse (0)."""
    def previousView(self) -> Any:
        """self.previousView() -> switch to previous view in settings Views list."""
    def setView(self, s: Any) -> Any:
        """self.setView(s) -> set 'current' multi-view view to 's'."""
    def showOverlay(self, show: Any) -> bool:
        """self.showOverlay(show) -> Bool.
        Activates or deactivates the overlay in the viewer.
        @param show: True to activate the overlay, False to deactivate the overlay.
        @return: True if the overlay was activated or deactivated, False otherwise.
        """
    def showStatusMessage(self) -> None:
        """self.showStatusMessage() -> None.
        Shows the status message in the viewer.
        @return: None.
        """
    def stop(self, *args: Any, **kwargs: Any) -> Any:
        """Stop playing."""
    def view(self) -> Any:
        """self.view() -> string name of 'current' multi-view view."""

class WH_Knob(Vec2_Knob):
    """A knob which holds width and height values."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class XYZ_Knob(Vec3_Knob):
    """A knob which holds a 3D coordinate."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def parent(self) -> XYZ_Knob:
        """parent() -> XYZ_Knob

        Return parent.
        """
    def value(self, n: int = ..., oc: OutputContext = ...) -> float:
        """value(n, oc) -> float

        Return value for dimension n. The optional argument oc is an OutputContext.
        """

class XY_Knob(Vec2_Knob):
    """A knob which describes a 2D position."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def value(self, n: int = ..., oc: OutputContext = ...) -> float:
        """value(n, oc) -> float

        Return value for dimension n. The optional argument oc is an OutputContext.
        """

def activeGroup() -> Group:
    """activeGroup() -> Group

    Returns the group of the DAG window in focus. Returns the root group if none in focus.

    :return: The group node.
    """

def activeViewer() -> ViewerWindow:
    """activeViewer() -> ViewerWindow

    Return an object representing the active Viewer panel. This
    is not the same as the Viewer node, this is the viewer UI element.

    :return: Object representing the active ViewerWindow
    """

def addFavoriteDir(name: str, directory: str, type: int = ..., icon: str = ..., tooltip: str = ..., key: str = ...) -> None:
    """addFavoriteDir(name, directory, type, icon, tooltip, key) -> None.

    Add a path to the file choosers favorite directory list. The path name can contain environment variables which will be expanded when the user clicks the favourites button

    :param name: Favourite path entry ('Home', 'Desktop', etc.).
    :param directory: FileChooser will change to this directory path.
    :param type: Optional bitwise OR combination of nuke.IMAGE, nuke.SCRIPT, nuke.FONT or nuke.GEO.
    :param icon: Optional filename of an image to use as an icon.
    :param tooltip: Optional short text to explain the path and the meaning of the name.
    :param key: Optional shortcut key.
    :return: None.
    """

def addFormat(s: str) -> Format | None:
    """addFormat(s) -> Format or None.

    Create a new image format, which will show up on the pull-down menus for image formats.
    You must give a width and height and name. The xyrt rectangle describes the image area, if
    it is smaller than the width and height (for Academy aperture, for example). The
    pixel aspect is the ratio of the width of a pixel to the height.

    :param s: String in TCL format \\w h ?x y r t? ?pa? name\\.
    :return: Format or None.
    """

def addNodePresetExcludePaths(paths: Any = ...) -> None:
    """addNodePresetExcludePaths( paths ) -> None

    Adds a list of paths that will be excluded from Node preset search paths.

    :param: paths Sequence of paths to exclude
    :return: None.
    """

def addSequenceFileExtension(fileExtension: Any) -> Any:
    """addSequenceFileExtension( fileExtension )

    Adds the input file extension to the list of extensions that will get displayed as sequences in the file browser.

    :param fileExtension: the new file extension. Valid examples are: 'exr', '.jpg'; invalid examples are: 'somefile.ext'
    """

def addToolsetExcludePaths(paths: Any = ...) -> None:
    """addToolsetExcludePaths( paths ) -> None

    :param paths Sequence of paths to exclude. Adds a list of paths that will be excluded from Toolset search paths.
    :return: None.
    """

def addView(s: str) -> None:
    """addView(s) -> None

    Deprecated. Use the Root node.

    Adds a new view to the list of views.

    :param s: View name.
    :return: None
    """

def alert(prompt: Any = ...) -> None:
    """alert(prompt) -> None

    Show a warning dialog box. Pops up a warning box
    and waits for the user to hit the OK button.

    :param prompt: Present user with this message.
    :return: None
    """

def allNodes(filter: str = ..., group: Node = ..., recurseGroups: bool = ...) -> list[Node]:
    """allNodes(filter, group, recurseGroups) -> list

    List of all nodes in a group. If you need to get all the nodes in the script
    from a context which has no child nodes, for instance a control panel, use
    nuke.root().nodes().

    :param filter: Optional. Only return nodes of the specified class.
    :param group: Optional. If the group is omitted the current group (ie the group the user picked a menu item from the toolbar of) is used.
    :param recurseGroups: Optional. If True, will also return all child nodes within any group nodes. This is done recursively and defaults to False.
    :return: list
    """

def animation(object: Any, *commands: Any) -> None:
    """animation(object, *commands) -> None

    Does operations on an animation curve.

    The following commands are supported:
      - B{clear} deletes all the keys from the animation.
      - B{erase} C{index I{last_index}} removes all keyframes between index and last_index
      - B{expression} C{I{newvalue}} returns or sets the expression for
        the animation. The default is 'curve' or 'y' which returns the interpolation of the keys.
      - B{generate} C{start end increment field expression I{field expression} ...}
        generates an animation with start, end, and increment. Multiple field/expression pairs
        generate a keyframe. Possible field commands are:
          - B{x} sets the frame number for the next keyframe
          - B{y} sets the keyframe value
          - B{dy} sets the left slope
          - B{ldy} sets left and right slope to the same value
          - B{la} and B{ra} are the length of the slope handle in x direction. A value of 1
            generates a handle that is one third of the distance to the next keyframe.
      - B{index} C{x} returns the index of the last key with x <= t, return -1 for none.
      - B{is_key} return non-zero if there is a key with x == t. The actual return value is the index+1.
      - B{move} C{field expression I{field expression}} replaces all selected keys
        in an animation with new ones as explained above in B{generate}
      - B{name} returns a user-friendly name for this animation. This will eliminate
        any common prefix between this animation and all other selected ones,
        and also replaces mangled names returned by animations with nice ones.
      - B{size} returns the number of keys in the animation.
      - B{test} errors if no points in the animation are selected
      - B{y} index C{I{newvalue}} gets or sets the value of an animation.
      - B{x} index C{I{newvalue}} gets or sets the horizontal postion of a key.
        If the animation contains an expression or keyframes, the new value will be overridden.

    See also: animations

    :param object: The animation curve.
    :param commands: a varargs-style list of commands, where each command is one of those defined above.
    :return: None
    """

def animationEnd() -> float:
    """animationEnd() -> float.

    Returns the last frame (or x value) for the currently selected animations.

    :return: The end frame.
    """

def animationIncrement() -> float:
    """animationIncrement() -> float

    Returns a recommended interval between samples of the currently selected animation.

    :return: The recommended interval.
    """

def animationStart() -> float:
    """animationStart() -> float

    Returns the starting frame (or x value) for the currently selected animations.

    :return: The start frame.
    """

def animations() -> tuple:
    """animations() -> tuple

    Returns a list of animatable things the user wants to work on.

    If this is a command being executed from a menu item in a curve editor, a list of the names of all selected curves is returned. If this list is empty a "No curves selected" error is produced.

    If this is a command being executed from the pop-up list in a knob then a list of all the fields in the knob is returned.

    If this is a command being executed from the right-mouse-button pop-up list in a field of a knob, the name of that field is returned.

    Otherwise this produces an error indicating that the command requries a knob context. You can get such a context by doing "in <knob> {command}"

    Also see the 'selected' argument to the animation command.

    See also: animation, animationStart, animationEnd, animationIncrement

    :return: A tuple of animatable things.
    """

def applyPreset(nodeName: Any, presetName: Any) -> None:
    """applyPreset(nodeName, presetName) -> None

    Applies a given preset to the current node.

    :param nodeName: Name of the node to apply the preset to.
    :param presetName: Name of the preset to use.
    :param node: (optional) a Node object to apply the preset to. If this is provided, the nodeName parameter is ignored.
    :return: bool.
    """

def applyUserPreset(nodeName: Any, presetName: Any) -> None:
    """applyUserPreset(nodeName, presetName) -> None

    Applies a given user preset to the current node.

    :param nodeName: Name of the node to apply the preset to.
    :param presetName: Name of the preset to use.
    :param node: (optional) a Node object to apply the preset to. If this is provided, the nodeName parameter is ignored.
    :return: bool.
    """

def ask(prompt: Any) -> bool:
    """ask(prompt) -> bool

    Show a Yes/No dialog.

    :param prompt: Present the user with this message.
    :return: True if Yes, False otherwise.
    """

def askWithCancel(prompt: Any) -> bool:
    """askWithCancel(prompt) -> bool

    Show a Yes/No/Cancel dialog.

    :param prompt: Present the user with this question.
    :return: True if Yes, False if No, an exception is thrown if Cancel.
    """

def autoplace(n: Node = ...) -> None:
    """autoplace(n) -> None.

    Deprecated. Use Node.autoplace.

    Automatically place nodes, so they do not overlap.

    :param n: Node.
    :return: None
    """

def autoplaceSnap(n: Node = ...) -> None:
    """autoplaceSnap(n) -> None

    Move node to the closest grid position.

    :param n: Node.
    :return: None
    """

def autoplace_all() -> None:
    """autoplace_all() -> None.

    Performs autoplace of all nodes in current context group.

    :return: None. May return exception it top context group has subgraph locked.
    """

def autoplace_snap_all() -> None:
    """autoplace_snap_all() -> None.

    Performs autoplace snap of all nodes in current context group.

    :return: None. May return exception it top context group has subgraph locked.
    """

def autoplace_snap_selected() -> None:
    """autoplace_snap_selected() -> None.

    Performs autoplace snap of all selected nodes in current context group.

    :return: None. May return exception it top context group has subgraph locked.
    """

def cacheUsage() -> int:
    """cacheUsage() -> int

    Get the total amount of memory currently used by the cache.

    :return: Current memory usage in bytes.
    """

def canCreateNode(name: str) -> bool:
    """canCreateNode(name) -> True if the node can be created, or False if not.

    This function can be used to determine whether it is possible to create a node with the specified node class.

    :param name: Node name.
    :return: True if the node can be created, or False if not.
    """

def cancel() -> None:
    """cancel() -> None

    Cancel an in-progress operation. This has the same effect as hitting cancel on the progress panel.

    :return: None
    """

def center() -> Any:
    """center() -> array with x, then y

    Return the center values of a group's display, these values are suitable to be passed to nuke.zoom as the DAG center point.  Like so:

    .. code-block:: python

        center = nuke.center()
        zoom = nuke.zoom()
        print center[0]
        print center[1]
        ## move DAG back to center point without changing zoom.
        nuke.zoom( zoom, center )

    :return: Array of x, y.
    """

def channels(n: Node = ...) -> list[str]:
    """channels(n=None) -> (string)

    Deprecated. Use Node.channels.

    List channels. The n argument is a Nuke node and if given only the channels
    output by this node are listed. If not given or None, all channels known about
    are listed.

    :param n: Optional node parameter.
    :return: A list of channel names.
    """

def choice(title: Any = ..., prompt: Any = ..., options: Any = ..., default: Any = ...) -> Any:
    """choice(title, prompt, options, default = 0) -> index

    Shows a dialog box with the given title and prompt text, and a combo box containing the given options.

    :param title: Text to put in the dialog's title bar.
    :param prompt: Text to display at the top of the dialog.
    :param options: A list of strings for the user to choose from.
    :param default: The index (starting from zero) of the option to select first.
    :return: An integer index (starting from zero) of the choice the user selected, or None if the dialog was cancelled.
    """

def clearAssetCache() -> None:
    """clearAssetCache() -> None

    Clear the Asset cache.
    """

def clearBlinkCache() -> None:
    """clearBlinkCache() -> None

    Clear the Blink cache for all devices.
    """

def clearDiskCache() -> None:
    """clearDiskCache() -> None

    Clear the disk cache of all files.
    """

def clearGeoSelection() -> None:
    """clearGeoSelection() -> None

    Clear currently selected geometry.

    :return: None.
    """

def clearRAMCache() -> None:
    """clearRAMCache() -> None

    Clear the RAM cache of all files.
    """

def clearTabMenuFavorites() -> None:
    """clearTabMenuFavorites() -> None

    Uncheck every favourite node in tab search menu.
    """

def clearTabMenuWeighting() -> None:
    """clearTabMenuWeighting() -> None

    Set the weight of each node to 0 in tab search menu.
    """

def clone(n: Node, args: str = ..., inpanel: bool = ...) -> Node:
    """clone(n, args, inpanel) -> Node

    Create a clone node that behaves identical to the original. The node argument is the node to be cloned, args and inpanel are optional arguments similar to createNode.
    A cloned node shares the exact same properties with its original. Clones share the same set of knobs and the same control panel. However they can
    have different positions and connections in the render tree. Any clone, including the original, can be deleted at any time without harming any of its clones.

    :param n: Node.
    :param args: Optional number of inputs requested.
    :param inpanel: Optional boolean.
    :return: Node
    """

def cloneSelected(action: str = ...) -> bool:
    """cloneSelected(action) -> bool

    This makes a clone of all selected nodes, preserving connections between them, and makes only the clones be selected.

    :param action: Optional and if 'copy' it cuts the resulting clones to the clipboard.
    :return: True if succeeded, False otherwise.
    """

def collapseToGroup(show: bool = ...) -> Group:
    """collapseToGroup(show=True) -> Group

    Moves the currently selected nodes to a new group, maintaining their previous connections.

    :param show: If show is True, the node graph for the new group is shown in the background.
    :return: The new Group node.
    """

def collapseToLiveGroup(show: bool = ...) -> Group:
    """collapseToLiveGroup(show=True) -> Group

    Moves the currently selected nodes to a new group, maintaining their previous connections.

    :param show: If show is True, the node graph for the new group is shown in the background.
    :return: The new Group node.
    """

def collapseToVariableGroup(show: bool = ...) -> Group:
    """collapseToVariableGroup(show=True) -> Group

    Moves the currently selected nodes to a new group, maintaining their previous connections.

    :param show: If show is True, the node graph for the new group is shown in the background.
    :return: The new Group node.
    """

def connectNodes() -> None:
    """connectNodes() -> None

    Deprecated. Use Group.connectSelectedNodes.

    :return: None
    """

def connectViewer(inputNum: Any, node: Any) -> None:
    """connectViewer(inputNum, node) -> None

    Connect a viewer input to a node. The argument i is the input number and n is either a Nuke node or None.
    Some viewer in the current group is found, if there are no viewers one is created. The
    viewer is then altered to have at least n+1 inputs and then input n is connected to the given node.
    This function is used by the numeric shortcuts in the DAG view menu.

    :param inputNum: Input number.
    :param node: The Node to connect to the input.
    :return: None
    """

def createLiveInput() -> Node:
    """createLiveInput() -> Node

    Creates a new LiveInput and populates the \\file\\ and \\liveGroup\\ knobs according to the
    filename and LiveGroup name of the parent group

    :return: The new LiveInput_Node.
    """

def createNode(node: str, knobs: str = ..., inpanel: bool = ...) -> Node:
    """createNode(node, knobs, inpanel) -> Node

    Creates a node of the specified type and adds it to the DAG.

    :param node: Name of node class to create (e.g. 'Blur').
    :type node: str
    :param knobs: TCL list of knob name value pairs.
    :type knobs: str, optional
    :param inpanel: Open the control bin (only applies when the GUI is running), defaults to True.
    :type inpanel: bool, optional
    :return: The node created.
    :rtype: nuke.Node
    """

def createScenefileBrowser(fileName: str, nodeName: str) -> None:
    """createScenefileBrowser( fileName, nodeName ) -> None

    Pops up a scene browser dialog box.
    Receives the path to an Alembic (abc) or Universal Scene Description (usd/usda/usdc/usdz) file,
    and displays a hierarchical tree of the nodes within the file.
    The user can select which nodes they are interested in, and nodes of the appropriate type will automatically.
    be created.
    If a valid scene file nodeName is specified, this node will be populated with the selected tree.

    :param fileName: Path and filename for an alembic or usd/usda/usdc/usdz file.
    :param nodeName: name of a valid scene file node to populate. If the node is invalid, new nodes will be automatically created
    """

def createToolset(filename: Any = ..., overwrite: Any = ..., rootPath: Any = ...) -> None:
    """createToolset(filename=None, overwrite=-1, rootPath = None) -> None

    Creates a tool preset based on the currently selected nodes.

    :param filename: Saves the preset as a script with the given file name.
    :param overwrite: If 1 (true) always overwrite; if 0 (false) never overwrite;
    :param rootPath: If specified, use this as the root path to save the Toolset to. If not specified, save to the user's .nuke/Toolsets folder.
     otherwise, in GUI mode ask the user, in terminal do same as False. Default
     is -1, meaning 'ask the user'.
    """

def critical(message: str) -> None:
    """critical(message)-> None

    Puts the message into the error console, treating it like an error. Also pops up an alert dialog to the user, immediately.

    :param message: String parameter.
    :return: None.
    """

def deassetize(arg1: Sequence[Any], /) -> Any:
    """Finds all assetized File_Knobs in nodes and replaces their entity reference
    by their respective resolved file path.

    :param nodes : A list of nodes to be deassetized

    : return : A tuple.The first element is a boolean that is True if all assetized
    knobs were successfully deassetized and the second is a list of
    unresolved knobs that are assetized but failed to be resolved.

    If OpenAssetIO isn't correctly configured, (False, []) is returned.
    """

def debug(message: str) -> None:
    """debug(message)-> None

    Puts the message into the error console, treating it like a debug message, which only shows up when the verbosity level is high enough.

    :param message: String parameter.
    :return: None.
    """

def defaultFontPathname() -> str:
    """defaultFontPathname() -> str

    Get the path to Nukes default font.

    :return: Path to the font.
    """

def defaultNodeColor(s: str) -> int:
    """defaultNodeColor(s) -> int

    Get the default node colour.

    :param s: Node class.
    :return: The color as a packed integer (0xRRGGBB00).
    """

def delete(n: Node) -> None:
    """delete(n) -> None

    The named node is deleted. It can be recovered with an undo.

    :param n: Node.
    :return: None
    """

def deletePreset(nodeClassName: Any, presetName: Any) -> None:
    """deletePreset(nodeClassName, presetName) -> None

    Deletes a pre-created node preset

    :param nodeClassName: Name of the node class to create a preset for.
    :param presetName: Name of the preset to create.
    :return: bool.
    """

def deleteUserPreset(nodeClassName: Any, presetName: Any) -> None:
    """deleteUserPreset(nodeClassName, presetName) -> None

    Deletes a pre-created user node preset

    :param nodeClassName: Name of the node class to create a preset for.
    :param presetName: Name of the preset to create.
    :return: bool.
    """

def deleteView(s: Any) -> None:
    """deleteView(s) -> None

    Deprecated. Use the Root node.

    Deletes a view from the list of views.

    :param s: View name.
    :return: None
    """

def display(s: Any = ..., node: Node = ..., title: Any = ..., width: Any = ...) -> None:
    """display(s, node, title, width) -> None.

    Creates a window showing the result of a python script. The script is
    executed in the context of the given node, so this and a knob
    name in expressions refer to that node.

    The window will have an 'update' button to run the script again.

    :param s: Python script.
    :param node: Node.
    :param title: Optional title of window.
    :param width: Optional width of window.
    :return: None.
    """

def duplicateSelectedNodes() -> None:
    """duplicateSelectedNodes() -> None.

    Creates a duplicate of all selected nodes in the current script context group

    :return: None. May return exception it top context group has subgraph locked.
    """

def endGroup() -> None:
    """endGroup() -> None

    **Deprecated**. Use Group.run, Group.begin/Group.end pairs or (preferably) the with statement.

    Changes the current group to the parent of the current group. Does nothing if the current group is a Root (the main window of a script).

    :return: None.
    """

def error(message: str) -> None:
    """error(message)-> None

    Puts the message into the error console, treating it like an error.

    :param message: String parameter.
    :return: None.
    """

def evaluateGsv(*args: Any, **kwargs: Any) -> Any:
    """Finds all of the gsv terms within a given expression and replaces these
     terms with the evaluated result.

    :param expression: The expression string to be evaluated.
    :param node: Optional node to use as a gsv context. If not supplied the current
     thisNode will be used.
    :return: A copy of the input expression string with all valid gsv evaluated.
    """

def evaluateString(arg1: str = ..., arg2: Any = ..., arg3: Any = ..., arg4: Any = ..., /) -> Any:
    """"expand" the string by replacing tcl portions of the string
    with the final text.

    Expansion can be controlled with optional flags:
    - STRING_EXPAND_FILENAME a leading "~/" is replaced by the
    value of $env(HOME), and a leading "~foo" is replaced by a guess
    of the user foo's home directory done by replacing the end of
    $env(HOME) (nuke does not bother with the passwd file). And the
    result is passed through filename_fix, if the command is defined.
    - STRING_EXPAND_FILENUMBER %nd and ### sequences are replaced
    by the frame number from the context parameter, and %V and %v
    are replaced with the name and initial of the view.

    :param expression: The expression string to be evaluated.
    :param node: Optional node to use as the context for expansion. If not supplied the current thisNode will be used.
    :param context: Optional OutputContext to use for expansion.
    :param flags: Optional flags to control expansion.
    :return: The expanded string.
    """

@overload
def execute(nameOrNode: Node | str, start: int = ..., end: int = ..., incr: int = ..., views: list[str] = ..., continueOnError: bool = ...) -> None:
    """execute(nameOrNode, start, end, incr, views, continueOnError = False) -> None.
    execute(nameOrNode, frameRangeSet, views, continueOnError = False) -> None.

    Execute the named Write node over the specified frames.

    There are two variants of this function. The first allows you to specify the
    frames to write range by giving the start frame number, the end frame number
    and the frame increment. The second allows you to specify more complicated
    sets of frames by providing a sequence of FrameRange objects.

    If Nuke is run with the GUI up, this will pop up a progress meter. If the user hits
    the cancel button this command will return 'cancelled' error.
    If Nuke is run from the nuke command line (ie nuke was started with the -t switch)
    execute() prints a text percentage as it progresses.
    If the user types ^C it will aborting the execute() and return a 'cancelled' error.

    :param nameOrNode: A node name or a node object.
    :param start: Optional start frame. Default is root.first_frame.
    :param end: Optional end frame. Default is root.last_frame.
    :param incr: Optional increment. Default is 1.
    :param views: Optional list of views. Default is None, meaning \\all views\\.
    :return: None
    """
@overload
def execute(nameOrNode: Node | str, frameRangeSet: FrameRanges | list[FrameRange], views: list[str] = ..., continueOnError: bool = ...) -> None:
    """execute(nameOrNode, start, end, incr, views, continueOnError = False) -> None.
    execute(nameOrNode, frameRangeSet, views, continueOnError = False) -> None.

    Execute the named Write node over the specified frames.

    There are two variants of this function. The first allows you to specify the
    frames to write range by giving the start frame number, the end frame number
    and the frame increment. The second allows you to specify more complicated
    sets of frames by providing a sequence of FrameRange objects.

    If Nuke is run with the GUI up, this will pop up a progress meter. If the user hits
    the cancel button this command will return 'cancelled' error.
    If Nuke is run from the nuke command line (ie nuke was started with the -t switch)
    execute() prints a text percentage as it progresses.
    If the user types ^C it will aborting the execute() and return a 'cancelled' error.

    :param nameOrNode: A node name or a node object.
    :param start: Optional start frame. Default is root.first_frame.
    :param end: Optional end frame. Default is root.last_frame.
    :param incr: Optional increment. Default is 1.
    :param views: Optional list of views. Default is None, meaning \\all views\\.
    :return: None
    """

def executeBackgroundNuke(exe_path: str, nodes: list[Node], frameRange: list[Any], views: list[str], limits: dict[str, Any], continueOnError: bool = ..., flipbookToRun: str = ..., flipbookOptions: dict[str, Any] = ...) -> int:
    """executeBackgroundNuke(exe_path, nodes, frameRange, views, limits, continueOnError = False, flipbookToRun = ", flipbookOptions = {}) -> None

    Run an instance of Nuke as a monitored sub process. Returns an integer that's used as unique id for the started task. If it failed to launch this will be -1.

    :param: exe_path: Path to Nuke or a script that can take Nuke arguments. You probably want to supply nuke.EXE_PATH.
    :param: nodes: A list of nodes to execute.
    :param: frameRanges: List of frame ranges to execute.
    :param: views: A list of view names to execute.
    :param: limits: A dictionary with system limits, currently uses keys maxThreads and maxCache.
    :param: flipbookToRun: The name of the flipbook application to run after the render, or an empty string if not desired.
    :param: flipbookOptions: A dictionary with options to pass to the flipbook. These should include roi and pixelAspect.
    :return: Int.
    """

def executeMultiple(nodes: Sequence[Node], ranges: Sequence[Sequence[int]] = ..., views: list[str] = ..., continueOnError: bool = ...) -> None:
    """executeMultiple(nodes, ranges, views, continueOnError=False) -> None

    Execute the current script for a specified frame range. The argument nodes is
    a sequence of Nuke nodes and ranges is a sequence of range lists. A Nuke range
    list is a sequence of 3 integers - first, last and incr ( e.g. nuke.execute((w,), ((1,100,1),)) ).
    The named nodes must all be Write or other executable operators. If no nodes
    are given then all executable nodes in the current group are executed.
    Note that DiskCache and Precomp nodes do not get executed with this call, unless explicitly specified.

    If Nuke is run with the GUI up, this will pop up a progress meter. If the
    user hits the cancel button this command will raise a 'cancelled' error. If
    Nuke is run in terminal mode (with the -t switch) this prints a text
    percentage as it progresses.

    If the user types ^C it will abort the execute() and raise a 'cancelled' error.

    :param nodes: Node list.
    :param ranges: Optional start frame. Default is root.first_frame.
    :param views: Optional list of views. Default is None. Execute for all.
    :return: None
    """

def executing() -> bool:
    """executing() -> Bool.

    Returns whether an Executable Node is currently active or not.

    :param f: Optional frame number.
    :return: Current bool.
    """

def exists(s: str) -> bool:
    """exists(s) -> bool

    Check for the existence of a named item.
    Function for backwards-compatibility with TCL.

    :param s: Name of item.
    :return: True if exists, False otherwise.
    """

def expandSelectedGroup() -> None:
    """expandSelectedGroup() -> None

    Moves all nodes from the currently selected group node into its parent group,
    maintaining node input and output connections, and deletes the group.
    Returns the nodes that were moved, which will also be selected.

    :return: None
    """

def expr(arg1: str, /) -> Any:
    """expression(s) -> float

    Parse a Nuke expression. Runs the same expression parser as is used by animations. This is not the same as the tcl expr parser. The main differences are:

    - Only floating point numbers are calculated. There are no strings, boolean, or integer values.
    - You can name any knob that returns a floating point value, with a dot-separated name, see knob for details on these names. You may follow the knob name with a time in parenthesis (like a function call) and if it is animated it will be evaluated at that time. If it is animated and no time is given, 'frame' is used.
    - The words 'frame', 't', and 'x' evaluate to the frame number of the context node, or the frame number this animation is being evaluated at.
    - The word 'y' in an animation expression evaluates to the value the animation would have if the control points were used and there was no expression. Outside an animation expression y returns zero.

    :param s: The expression, as a string.
    :return: The result.
    """

def expression(s: str) -> float:
    """expression(s) -> float

    Parse a Nuke expression. Runs the same expression parser as is used by animations. This is not the same as the tcl expr parser. The main differences are:

    - Only floating point numbers are calculated. There are no strings, boolean, or integer values.
    - You can name any knob that returns a floating point value, with a dot-separated name, see knob for details on these names. You may follow the knob name with a time in parenthesis (like a function call) and if it is animated it will be evaluated at that time. If it is animated and no time is given, 'frame' is used.
    - The words 'frame', 't', and 'x' evaluate to the frame number of the context node, or the frame number this animation is being evaluated at.
    - The word 'y' in an animation expression evaluates to the value the animation would have if the control points were used and there was no expression. Outside an animation expression y returns zero.

    :param s: The expression, as a string.
    :return: The result.
    """

def extractSelected() -> None:
    """extractSelected() -> None

    Disconnects the selected nodes in the group from the tree, and shifts them to the side.

    :return: None
    """

def filename(node: Node = ..., i: int = ...) -> str:
    """filename(node, i) -> str

    Return the filename(s) this node or group is working with.

    For a Read or Write operator (or anything else with a filename
    knob) this will return the current filename, based on the
    root.proxy settings and which of the fullsize/proxy filenames are
    filled in. All expansion of commands and variables is
    done. However by default it will still have %%04d sequences in it,
    use REPLACE to get the actual filename with the current frame number.

    If the node is a group, a search is done for executable (i.e. Write)
    operators and the value from each of them is returned. This will duplicate
    the result of calling execute() on the group.

    :param node: Optional node.
    :param i: Optional nuke.REPLACE. Will replace %%04d style sequences with the current frame number.
    :return: Filename, or None if no filenames are found.
    """

def forceClone() -> bool:
    """forceClone() -> bool

    :return: True if succeeded, False otherwise.
    """

def forceLoad(n: Any = ...) -> None:
    """forceLoad(n) -> None

    Force the plugin to be fully instantiated.

    :param n: Optional node argument. Default is the current node.
    :return: None
    """

def fork(*args: Any, **kwargs: Any) -> Any:
    """Forks a new instance of Nuke optionally with the contents of the named file."""

def formats() -> list[Format]:
    """formats() -> list

    :return: List of all available formats.
    """

def frame(f: float = ...) -> int:
    """frame(f) -> Current frame.

    Return or set the current frame number. Deprecated. Use Root.frame.

    Returns the current frame. Normally this is the frame number set in the root
    node, typically by the user moving the frame slider in a viewer. If a number is
    given, it sets the current frame number to that number. If the current context
    is the root this changes the root frame.

    :param f: Optional frame number.
    :return: Current frame.
    """

def fromNode(n: Any) -> str:
    """fromNode(n) -> String.

    Return the Node n as a string.
    This function is most useful when combining Python and TCL scripts for backwards compatibility reasons.

    :param n: A Node.
    :return: String.
    """

def getAllUserPresets() -> None:
    """getAllUserPresets() -> None

    Gets a list of all current user presets

    :return: a list of tuples containing all nodename/presetname pairs.
    """

def getClipname(prompt: Any = ..., pattern: Any = ..., default: Any = ..., multiple: bool = ...) -> Any:
    """getClipname(prompt, pattern=None, default=None, multiple=False) -> list of strings or string

    Pops up a file chooser dialog box. You can use the pattern to restrict the displayed choices to matching filenames,
    normal Unix glob rules are used here. getClipname compresses lists of filenames that only differ by an index number
    into a single entry called a 'clip'.

    :param prompt: Present the user with this message.
    :param pattern: Optional file selection pattern.
    :param default: Optional default filename and path.
    :param multiple: Optional boolean convertible object to allow for multiple
     selection.
    :return: If multiple is True, the user input is returned as a list of
     strings, otherwise as a single string. If the dialog is cancelled, the
     return value is None.
    """

def getColor(initial: Any = ...) -> int:
    """getColor(initial) -> int

    Show a color chooser dialog and return the selected color as an int.

    The format of the color values is packed 8bit rgb multiplied by 256 (ie in hex: 0xRRGGBB00).

    :param initial: Optional initial color. Integer with components packed as above.
    :return: The selected color.
    """

def getDeletedPresets() -> None:
    """getDeletedPresets() -> None

    Gets a list of all currently deleted presets

    :return: a pyDict containing all nodename/presetname pairs.
    """

def getFileNameList(dir: Any, splitSequences: bool = ..., extraInformation: bool = ..., returnDirs: bool = ..., returnHidden: bool = ...) -> str:
    """getFileNameList( dir, splitSequences = False, extraInformation = False, returnDirs=True, returnHidden=False ) -> str

    Retrieves the filename list.

    :param: dir the directory to get sequences from
    :param: splitSequences whether to split sequences or not
    :param: extraInformation whether or not there should be extra sequence information on the sequence name
    :param: returnDirs whether to return a list of directories as well as sequences
    :param: returnHidden whether to return hidden files and directories.
    :return: Array of files.
    """

def getFilename(message: str, pattern: str = ..., default: str = ..., favorites: str = ..., type: str = ..., multiple: bool = ..., arg7: str = ...) -> Any:
    """getFilename(message, pattern=None, default=None, favorites=None, type=None, multiple=False) -> list of strings or single string

    Pops up a file chooser dialog box. You can use the pattern to restrict the
    displayed choices to matching filenames, normal Unix glob rules are used
    here.

    :param message: Present the user with this message.
    :param pattern: Optional file selection pattern.
    :param default: Optional default filename and path.
    :param favorites: Optional. Restrict favorites to this set. Must be one of 'image', 'script', or 'font'.
    :param type: Optional the type of browser, to define task-specific behaviors; currently only 'save' is recognised.
    :param multiple: Optional boolean convertible object to allow for multiple
     selection. If this is True, the return value will be a list of strings; if
     not, it will be a single string. The default is
    :return: If multiple is True, the user input is returned as a list of
     strings, otherwise as a single string. If the dialog was cancelled, the
     return value will be None.
    """

def getFonts() -> list[list]:
    """getFonts() -> list of font  families and styl.

    Return a list of all available font families and styles

    :return: List of font families and style.
    """

def getFramesAndViews(label: Any = ..., default: Any = ..., maxviews: Any = ...) -> Any:
    """getFramesAndViews(label, default=None, maxviews=0) -> (ranges, views)

    Pops up a dialog with fields for a frame range and view selection.

    :param label: User message.
    :param default: Optional value for the input field.
    :param maxviews: Optional max number of views.
    :return: List of ranges and views.
    """

def getGeoSelection() -> GeoSelection:
    """getGeoSelection() -> Returns the selection as a dictionary

    :return: Currently selected geometry
    """

def getInput(prompt: Any = ..., default: Any = ...) -> str:
    """getInput(prompt, default) -> str

    Pops up a dialog box with a text field for an arbitrary string.

    :param prompt: Present the user with this message.
    :param default: Default value for the input text field.
    :return: String from text field or None if dialog is cancelled.
    """

def getNodeClassName() -> str:
    """getNodeClassName() -> None

    Gets the class name for the currently selected node

    :return: a string containing the name.
    """

def getNodePresetExcludePaths() -> list:
    """getNodePresetExcludePaths() -> string list

    Gets a list of all paths that are excluded from the search for node presets.

    :return: List of paths.
    """

def getNodePresetID() -> str:
    """getNodePresetID() -> None

    Gets the node preset identifier for the currently selected node

    :return: a string containing the ID.
    """

def getOcioColorSpaces() -> list[str]:
    """getOcioColorSpaces() -> returns the list of OCIO colorspaces.

    :return: list of strings
    """

def getPaneFor(panelName: Any) -> Any:
    """getPaneFor( panelName ) -> Dock

    Returns the first pane that contains the named panel or None if it can't be found.
    Note that the panelName must be exact as described in the layout.xml file or the panel ID.
    For example, 'Properties.1' or 'Viewer.1 or 'co.uk.thefoundry.WebBrowser'

    :return: The pane or None.
    """

def getPresetKnobValues() -> None:
    """getPresetKnobValues() -> None

    Gets a list of knob values for a given preset

    :param nodeClassName: Name of the node class to get values for.
    :param presetName: Name of the preset to get values for.
    :return: a pyDict containing all knob name/value pairs.
    """

def getPresets() -> None:
    """getPresets() -> None

    Gets a list of all presets for the currently selected node's class

    :return: a pyList containing all nodename/presetname pairs.
    """

def getPresetsMenu(Node: Node) -> Menu | None:
    """getPresetsMenu(Node) -> Menu or None

    Gets the presets menu for the currently selected node.

    :return: The menu, or None if it doesn't exist.
    """

def getReadFileKnob(node: Node) -> Any:
    """getReadFileKnob(node) -> knob

    Gets the read knob for a node (if it exists).

    :param node: The node to get the knob for.

    :return: A PyObject containing the read knob if it exists, NULL otherwise
    """

def getRenderProgress() -> Any:
    """getRenderProgress() -> Returns the progress of the render of a frame from 0 - 100 % complete.

    :return: The progress of the render.  Can be 0 if there is no progress to report.
    """

def getToolsetExcludePaths() -> list:
    """getToolsetExcludePaths() -> string list

    Gets a list of all paths that are excluded from the search for node presets.

    :return: List of paths.
    """

def getUserPresetKnobValues() -> None:
    """getUserPresetKnobValues() -> None

    Gets a list of knob values for a given preset

    :param nodeClassName: Name of the node class to get values for.
    :param presetName: Name of the preset to get values for.
    :return: a pyDict containing all knob name/value pairs.
    """

def getUserPresets(Node: Node) -> None:
    """getUserPresets(Node) -> None

    Gets a list of all user presets for the currently selected node's class

    :return: a pyList containing all nodename/presetname pairs.
    """

def hotkeys() -> str:
    """hotkeys() -> str

    Returns the Nuke key assignments as a string formatted for use in nuke.display().

    :return: A formatted string.
    """

def inputs(n: Node, i: int = ...) -> int:
    """inputs(n, i) -> int

    Deprecated. Use Node.inputs.

    Get how many inputs the node has. Normally this is a constant but some nodes have a variable number, the user can keep connecting them and the count will increase.
    Attempting to set the number will just disconnect all inputs greater or equal to number. For a variable input node this may decrease
    inputs to the new value. For most nodes this will have no effect on the value of inputs.

    :param n: Node.
    :param i: Optional number of inputs requested.
    :return: Number of inputs.
    """

def invertSelection() -> None:
    """invertSelection() -> None

    Selects all unselected nodes, and deselects all selected ones.

    :return: None.
    """

def knob(name: str, value: str = ..., getType: bool = ..., getClass: bool = ...) -> None:
    """knob(name, value, getType, getClass) -> None

    Returns or sets the entire state of a knob.

    Each individual control on a control panel is called a 'knob'. A
    knob's name is a dot-separated list. An example of a fully-expanded
    name of a knob is 'root.Group1.Blur1.size.w'. 'root' is the node
    name of the outermost group, 'Group1' is a group inside that
    containing the blur operator, 'Blur1' is the name of a blur
    operator, 'size' is the name of the actual knob, and 'w' is the
    name of the 'field' (there are two fields in a blur size, 'w' and
    'h').

    You can omit a lot of this because all knob names are figured out
    relative to a 'current knob' and 'current node'. These are set
    depending on the context of where the scripting is invoked. For
    menu items the current node is the group that contained the menu,
    and there is no current knob. For expressions typed into knob
    fields the current knob is that knob and the current node is the
    node the knob belongs to.

    If a name does not start with 'root' then a search upwards is done
    for the first word in the name, first against the fields in the
    current knob, then against the knobs in the current node, then
    against the nodes in the group containing the current node (or in
    it if it is a group), on up to the root.

    The word 'this' means the current knob or the current node.

    The word 'input' means the first (0 or B) input of a node. Ie
    'Blur1.input' returns the node connected to the input of Blur1,
    while 'Blur1.input.input' returns the input of that node.

    If you are getting the value for reporting to the user, you probably
    want to use the value or expression commands.

    If the getType argument is specified and is True, it will print out the type of the
    knob rather than getting or setting the value. The type is an integer,
    using the same list as addUserKnob.

    If the getClass argument is specified and is True, it will print out the type of the knob as a string, e.g. 'Int_Knob',
    'Enumeration_Knob', 'XY_Knob'.

    If both the getType and getClass arguments are present and are True, getType takes precedence.

    :param name: The name of the knob.
    :param value: Optional argument. If this is present, the value will be stored into the knob.
    :param getType: Optional boolean argument. If True, return the class ID for the knob instead of the knob itself. The class ID is an int.
    :param getClass: Optional boolean argument. If True, return the class name for the knob instead of the knob itself. The class name is a string.
    """

def knobDefault(classknob: str, value: str = ...) -> str:
    """knobDefault(classknob, value) -> str

    Set a default value for knobs in nodes that belong to the
    same class. All knobs with matching names, that are created after this
    command was issued, will default to the new value. If class. is missing
    or is \\*.\\ then this default applies to all nodes with such a knob.
    If several values are supplied, the first value which is valid will be
    used as the default.
    knobDefault can be used to specify file format specific knobs.
    These are knobs that are added to Read, Write and other file format
    dependent nodes when the file name changes. To specify defaults, use
    the class name, followed by the file format extension, followed by the knob name,
    all separated by periods. An example is shown below.

    Example:
      nuke.knobDefault(Blur.size, 20)

    Example:
      nuke.knobDefault(Read.exr.compression, 2)

    :param classknob: String in the form `class.knob` where `class` is the class of Node, i.e. Blur, and \\knob\\ is the name of the knob. This can also include a file extension, as in \\class.extension.knob\\
    :param value: Optional string to convert to the default value.
    :return: None or String with the default value.
    """

def knobTooltip(classknob: str, value: str) -> None:
    """knobTooltip(classknob, value) -> None

    Set an override for a tooltip on a knob.

    Example:

       nuke.knobTooltip('Blur.size', '[some text]')

    :param classknob: String in the form `class.knob` where `class` is the class of Node, i.e. Blur, and \\knob\\ is the name of the knob.
    :param value: String to use as the tooltip
    :return: None)
    """

def lastHitGroup() -> Group:
    """lastHitGroup() -> Group

    Returns the Group node of the last clicked group view.

    :return:
      - The Group node of the last clicked group view;
        applies to the DAG window of the current context group.
      - If no Group node of the last clicked group view exists,
        return the current context group.
    :rtype: nuke.Group
    """

def layers(node: Node = ...) -> list[str]:
    """layers(node=None) -> string list.

    Lists the layers in a node. If no node is provided this will list all known
    layer names in this script.

    :param node: Optional node parameter.
    :return: A list of layer names.
    """

def licenseInfo() -> None:
    """licenseInfo() -> Shows information about licenses used by nuke.

    :return: None
    """

def link(n: Node, args: str = ..., inpanel: bool = ...) -> Node:
    """link(n, args, inpanel) -> Node

    Create a link node that behaves identically to the original. The node argument
    is the node to be linked, args and inpanel are optional arguments similar to
    createNode. A link node shares the knob values with its original until
    overridden. link nodes share the same set of knobs. They can have different
    positions and connections in the render tree. Any link node, including the
    original, should be able to be deleted at any time without harming any of its
    link nodes.

    :param n: Node.
    :param args: Optional number of inputs requested.
    :param inpanel: Optional boolean.
    :return: Node
    """

def linkSelected(action: Any = ...) -> bool:
    """linkSelected(action) -> bool

    This makes a link node of all selected nodes, preserving connections between
    them, and makes only the link nodes be selected.

    :param action: Optional and if 'copy' it cuts the resulting link nodes to the
                   clipboard.
    :return: True if succeeded, False otherwise.
    """

def load(s: Any) -> None:
    """load(s) -> None

    Load a plugin. You can force a certain plugin to load with this function. If the plugin has already been loaded nothing happens.
    If there is no slash in the name then the pluginPath() is searched for it. If there is a slash then the name is used directly as a
    filename, if it does not start with a slash the name is relative to the directory containing any plugin being currently loaded.
    If no filename extension is provided, it will try appending '.so' (or whatever your OS dynamic library extension is) and finding
    nothing will also try to append '.tcl' and '.py'.

    :param s: Plugin name or filename.
    :return: None
    :raise RuntimeError: if the plugin couldn't be loaded for any reason.
    """

def loadToolset(filename: Any = ..., overwrite: Any = ...) -> None:
    """loadToolset(filename=None, overwrite=-1) -> None

    Loads the tool preset with the given file name.

    :param filename: name of preset script file to load
    """

def localiseFiles(readKnobs: Any) -> None:
    """localiseFiles(readKnobs)

    **This functionality has been removed, please check the documentation**

    @return: None.
    """

def localizationEnabled(knob: Any) -> bool:
    """localizationEnabled(knob) -> bool

    Checks if localization is enabled on a given Read_File_Knob.

    :param knob: The Read_File_Knob to check.
    :return: true if enabled, false otherwise
    """

def makeGroup(show: bool = ...) -> Group:
    """makeGroup(show=True) -> Group

    Creates a new group containing copies of all the currently selected nodes.
    Note that this creates duplicates of the selected nodes, rather than moving
    them.

    :param show: If show is True, the node graph for the new group is shown.
    :return: The new Group node.
    """

def maxPerformanceInfo(*args: Any, **kwargs: Any) -> Any:
    """maxPerformanceInfo -> Get the max performance info for this session.

    :return: a struct containing the max performance info if performance timers are in use, otherwise returns None.
    """

def menu(name: Any) -> Menu:
    """menu(name) -> Menu

    Find and return the Menu object with the given name.

    :param name: The name of the menu to get. Must be on the following values:
      - 'Nuke': The application menu
      - 'Pane': The UI Panes & Panels menu
      - 'Nodes': The Nodes toolbar (and Nodegraph right mouse menu)
      - 'Properties': The Properties panel right mouse menu
      - 'Animation': The knob Animation menu and Curve Editor right mouse menu
      - 'Viewer': The Viewer right mouse menu
      - 'Node Graph': The Node Graph right mouse menu
      - 'Axis': Functions which appear in menus on all Axis_Knobs.

    :return: The menu.
    :raises: RuntimeError: if Nuke isn't in GUI mode.
    """

def message(prompt: Any) -> None:
    """message(prompt) -> None

    Show an info dialog box. Pops up an info box (with a 'i' and the text
    message) and waits for the user to hit the OK button.

    :param prompt: Present user with this message.
    :return: None
    """

def modified(status: bool = ...) -> bool:
    """modified(status) -> True if modified, False otherwise.

    Deprecated. Use Root.modified and Root.setModified.

    Get or set the 'modified' flag in a script. Setting the value will turn the
    indicator in the title bar on/off and will start or stop the autosave timeout.

    :param status: Optional boolean value. If this is present the status will be set to this value; otherwise it will be retrieved instead.
    :return: True if modified, False otherwise.
    """

def nodeAtPath(path: str, instanceIndex: int = ...) -> Node:
    """nodeAtPath(path, instanceIndex) -> Node

    Find the node at the given full path, if it exists, and return it as a Python object.
    If the 'instanceIndex' provided is >= 0 then a specific clone instance (index 1+), or
    the 'original'(base) instance (index 0) is returned. If 'instanceIndex' value is not
    valid for the retrieved Node's context then null is returned.

    'path' is -always- an absolute path and periods '.' are assumed as the node hierarchy
    separator, conforming to the standard Nuke node path convention. However unlike 'toNode()'
    embedded expressions are -NOT- supported in the path string. For example you cannot
    retrieve a node using the path string 'Group1.FooNode.parent' as the trailing '.parent'
    is an expression, while 'Group1.FooNode' will work since it ends in an explicit node name.

    :param path: Absolute node path ending in a node name. No expression support provided.
    :param instanceIndex: Optional. If >= 0 return a specific clone instance where index 0 is the
    base node and index 1+ are clones. If instanceIndex is specified but the node is not cloned
    or the value is out of range then None is returned.
    :return: Node or None if it does not exist.
    """

def nodeCopy(s: Any) -> bool:
    """nodeCopy(s) -> bool

    Copy all selected nodes into a file or the clipboard.

    :param s: The name of a clipboard to copy into. If s is the string '%clipboard%' this will copy into the operating systems clipboard.
    :return: True if any nodes were selected, False otherwise.
    """

def nodeDelete(s: Any) -> bool:
    """nodeDelete(s) -> True if any nodes were deleted, False otherwise.

    Removes all selected nodes from the DAG.

    :return: True if all nodes were deleted, False if at least one wasn't.
    """

def nodePaste(s: Any) -> Node:
    """nodePaste(s) -> Node

    Paste nodes from a script file or the clipboard.
    This function executes the script stored in a file. It is assumed the script is the result of
    a nodeCopy command. The 's' argument can be '%clipboard%' to paste the operating system's clipboard contents.

    :param s: The 's' argument can be '%clipboard%' to paste the operating system's clipboard contents.
    :return: Node
    """

def nodeTypes(force_plugin_load: int = ...) -> list[str]:
    """nodeTypes(force_plugin_load=False) -> List

    :param force_plugin_load bool True to force loading all plugins on the path before querying node types, defaults to False
    :return list of all loaded node types
    """

def nodesSelected() -> None:
    """nodesSelected() -> None

    :return: true if any nodes are currently selected
    """

def numvalue(knob: str, default: float = ...) -> float:
    """numvalue(knob, default=infinity) -> float

    The numvalue function returns the current value of a knob.

    This is the same as the value() command except it will always return a
    number. For enumerations this returns the index into the menu, starting at
    zero. For checkmarks this returns 0 for false and 1 for true.

    :param knob: A knob.
    :param default: Optional default value to return if the knob's value cannot
     be converted to a number.
    :return: A numeric value for the knob, or the default value (if any).
    """

def oculaPresent() -> bool:
    """oculaPresent() -> bool

    Check whether Ocula is present.

    :return: True if Ocula is present, False if not.
    """

def ofxAddPluginAliasExclusion(fullOfxEffectName: Any) -> None:
    """ofxAddPluginAliasExclusion(fullOfxEffectName) -> None

    Adds the ofx effect name to a list of exclusions that will not get tcl aliases automatically created for them.

    For example, if there is an ofx plugin with a fully qualified name of: 'OFXuk.co.thefoundry.noisetools.denoise_v100'.

    Nuke by default would automatically alias that so that nuke.createNode('Denoise') will create that node type.

    By calling nuke.ofxAddPluginAliasExclusion('OFXuk.co.thefoundry.noisetools.denoise_v100'), you'd be changing
    that such that the only way to create a node of that type would be to call nuke.createNode('OFXuk.co.thefoundry.noisetools.denoise_v100')
    This does not change saving or loading of Nuke scripts with that plugin used in any way.

    :param fullOfxEffectName: The fully qualified name of the ofx plugin to add to the exclusion list.
    :return: None.
    """

def ofxMenu(arg1: str = ...) -> bool:
    """ofxMenu() -> bool

    Find all the OFX plugins (by searching all the directories below $OFX_PLUGIN_PATH,
    or by reading a cache file stored in $NUKE_TEMP_DIR), then add a menu item for each
    of them to the main menu.

    :return: True if succeeded, False otherwise.
    """

def ofxPluginPath() -> list[str]:
    """nuke.ofxPluginPath() -> String list

    List of all the directories Nuke searched for OFX plugins in.

    :return: String list
    """

def ofxRemovePluginAliasExclusion(fullOfxEffectName: Any) -> None:
    """ofxRemovePluginAliasExclusion(fullOfxEffectName) -> None

    Remove an ofx plugin alias exclusion that was previously added with .
    Example: nuke.ofxRemovePluginAliasExclusion('OFXuk.co.thefoundry.noisetools.denoise_v100')

    :param fullOfxEffectName: The fully qualified name of the ofx plugin to remove from the exclusion list.
    :return: None.
    """

def openPanels(*args: Any, **kwargs: Any) -> Any:
    """nodesSelected() -> List

    :return: a list of Nodes which have panels open. The last item in the list is the currently active Node panel.
    """

def pan() -> Any:
    """pan() -> array with x, then y

    Return the pan values of a group's display.
    This function is deprecated and will be removed in a future version.  You probably want to use nuke.center().\\n
    n = nuke.pan()
    print n[0]
    print n[1]

    :return: Array of x, y.
    """

def performanceProfileFilename() -> Any:
    """performanceProfileFilename() -> File to write performance profile to for this session.

    :return: the profile filename if performance timers are in use, otherwise returns None.
    """

def pluginExists(name: str) -> bool:
    """pluginExists(name) -> True if found, or False if not.

    This function is the same as load(), but only checks for the existence of a plugin rather than loading it.
    If there is no slash in the name then the pluginPath() is searched for it. If there is a slash then the name is used directly as a
    filename, if it does not start with a slash the name is relative to the directory containing any plugin being currently loaded.
    If no filename extension is provided, it will try appending '.so' (or whatever your OS dynamic library extension is) and finding
    nothing will also try to append '.tcl' and '.py'.

    :param name: Plugin name or filename.
    :return: True if found, or False if not.
    """

def pluginInstallLocation() -> Any:
    """pluginInstallLocation() -> string list

    The system-specific locations that Nuke will look in for third-party plugins.

    :return: List of paths.
    """

def pluginPath() -> list[str]:
    """pluginPath() -> string list

    List all the directories Nuke will search in for plugins.

    The built-in default is ~/.nuke and the 'plugins' directory from the
    same location the NUKE executable file is in. Setting the environment
    variable $NUKE_PATH to a colon-separated list of directories will
    replace the ~/.nuke with your own set of directories, but the plugins
    directory is always on the end.

    :return: List of paths.
    """

def plugins(switches: Any = ..., *pattern: Any) -> list[str]:
    """plugins(switches=0, *pattern)-> list of str

    Returns a list of every loaded plugin or every plugin available. By
    default each plugin is returned as the full pathname of the plugin
    file.

    You can give a glob-style matching pattern and only the plugins
    whose filenames (not path) match the pattern will be returned. You can
    give more than one glob pattern if desired.

    You can also put options before the glob patterns. Currently supported:

      ALL    Return all plugins in each of the plugin_path() directories,
             rather than only the currently loaded plugins.

      NODIR  Just put the filenames in the list, not the full path. There
             may be duplicates.

      REGISTERED  Include Ops which have been registered by the loaded plugins.
                  This is useful for plugin bundles where there are registered Ops
                  which do not have their own plugin file.
                  Please note that these Ops will not have a directory path or
                  file extension.  They are not filtered by the pattern.

      NOREADERWRITER  Do not include Reader or Writer plugins.  These cannot be used
                      as stand-alone plugins.

    If you don't specify any switches, the default behaviour is to return a list
    with the full paths of all loaded plugins.

    :param switches: Optional parameter. Bitwise OR of nuke.ALL, nuke.NODIR,
                     nuke.REGISTERED, nuke.NOREADERWRITER.
    :param pattern: Zero or more glob patterns.
    :return: List of plugins.
    """

def recentFile(index: int) -> str:
    """recentFile(index) -> str

    Returns a filename from the recent-files list.

    :param index: A position in the recent files list. This must be a non-negative number.
    :return: A file path.
    :raise ValueError: if the index is negative.
    :raise RuntimeError: if there is no entry in the recent files list for the specified index.
    """

def redo() -> None:
    """redo() -> None

    Perform the most recent redo.

    :return: None
    """

def registerFlipbook(s: Any) -> None:
    """registerFlipbook(s) -> None

    Register a flipbook application name into Nuke.

    :param s: Name of the flipbook application to be registered.
    :return: None
    """

def removeFavoriteDir(name: Any, type: Any = ...) -> None:
    """removeFavoriteDir(name, type) -> None.

    Remove a directory path from the favorites list.

    :param name: Favourite path entry ('Home', 'Desktop', etc.).
    :param type: Optional bitwise OR combination of nuke.IMAGE, nuke.SCRIPT, nuke.FONT or nuke.GEO.
    :return: None
    """

def render(*args: Any, **kwargs: Any) -> None:
    """execute(nameOrNode, start, end, incr, views, continueOnError = False) -> None.
    execute(nameOrNode, frameRangeSet, views, continueOnError = False) -> None.

    Execute the named Write node over the specified frames.

    There are two variants of this function. The first allows you to specify the
    frames to write range by giving the start frame number, the end frame number
    and the frame increment. The second allows you to specify more complicated
    sets of frames by providing a sequence of FrameRange objects.

    If Nuke is run with the GUI up, this will pop up a progress meter. If the user hits
    the cancel button this command will return 'cancelled' error.
    If Nuke is run from the nuke command line (ie nuke was started with the -t switch)
    execute() prints a text percentage as it progresses.
    If the user types ^C it will aborting the execute() and return a 'cancelled' error.

    :param nameOrNode: A node name or a node object.
    :param start: Optional start frame. Default is root.first_frame.
    :param end: Optional end frame. Default is root.last_frame.
    :param incr: Optional increment. Default is 1.
    :param views: Optional list of views. Default is None, meaning \\all views\\.
    :return: None
    """

def rescanFontFolders() -> None:
    """rescanFontFolders() -> None

    Rebuild the font cache scanning all available font directories.

    :return: None.
    """

def resetPerformanceTimers() -> None:
    """resetPerformanceTimers() -> None

    Clears the accumulated time on the performance timers.
    """

def restoreWindowLayout(i: Any) -> None:
    """restoreWindowLayout(i) -> None.

    Restores a saved window layout.

    :param i: Layout number
    :return: None

    WARNING - DEPRECATED ( nuke.restoreWindowLayout ): 
    This method is deprecated. The Restore action in the Workspace Menu corresponding to the input argument will be triggered.
    hiero.ui.setWorkspace(name) should be called with the desired workspace name.
    """

def resumePathProcessing() -> None:
    """resumePathProcessing() -> None

    Resume path processing.
    Use prior to performingmultiple node graph modifications, to avoid repeated path processing.

    :return: None.
    """

def root() -> Root:
    """root() -> node

    Get the DAG's root node. Always succeeds.

    :return: The root node. This will never be None.
    """

def runIn(object: str, cmd: str) -> bool:
    """runIn(object, cmd) -> bool

    Execute commands with a given node/knob/field as the 'context'.
    This means that all names are evaluated relative to this object, and commands that modify 'this' node will modify the given one.

    :param object: Name of object.
    :param cmd: Command to run.
    :return: True if succeeded, False otherwise.
    """

def sample(n: Node, c: str | float, x: float, y: float, dx: float = ..., dy: float = ...) -> float:
    """sample(n, c, x, y, dx, dy) -> float.

    Get pixel values from an image. Deprecated, use Node.sample instead.

    This requires the image to be calculated, so performance may be very bad if this is placed into an expression in
    a control panel. Produces a cubic filtered result. Any sizes less than 1, including 0, produce the same filtered result,
    this is correct based on sampling theory. Note that integers are at the corners of pixels, to center on a pixel add .5 to both coordinates.
    If the optional dx,dy are not given then the exact value of the square pixel that x,y lands in is returned. This is also called 'impulse filtering'.

    :param n: Node.
    :param c: Channel name.
    :param x: Centre of the area to sample (X coordinate).
    :param y: Centre of the area to sample (Y coordinate).
    :param dx: Optional size of the area to sample (X coordinate).
    :param dy: Optional size of the area to sample (Y coordinate).
    :return: Floating point value.
    """

def saveEventGraphTimers(filePath: Any) -> None:
    """saveEventGraphTimers(filePath) -> None

    Save events in the event graph.

    :param filePath: specify the file path where the event graph profiling data should be saved to.
    """

def saveToScript(filename: Any, fileContent: Any) -> None:
    """saveToScript(filename, fileContent) -> None

    Saves the fileContent with the given filename.
    """

def saveUserPreset(node: Any, presetName: Any) -> None:
    """saveUserPreset(node, presetName) -> None

    Saves a node's current knob values as a user preset.

    :param presetName: Name of the preset to create.
    :return: bool.
    """

def saveWindowLayout(i: Any = ...) -> None:
    """saveWindowLayout(i=-1) -> None

    Saves the current window layout.

    :param i: Optional layout index. If this is omitted or set to a negative value, save as the default layout.
    :return: None.

    WARNING - DEPRECATED ( nuke.saveWindowLayout ): 
    This method is deprecared. The Save action in the Workspace Menu corresponding to the input argument will be triggered.
    hiero.ui.saveWorkspace(name) should be called with the new workspace name.
    """

def scriptClear(*args: Any, **kwargs: Any) -> Any:
    """Clears a Nuke script and resets all the root knobs to user defined knob defaults. To reset to compiled in defaults only pass in resetToCompiledDefaults=True. To clear the user knobs, pass in clearUserKnobs=True."""

def scriptName() -> str:
    """scriptName() -> String

    Return the current script's file name
    """

def scriptNew(*args: Any, **kwargs: Any) -> Any:
    """Start a new script. Returns True if successful."""

def scriptReadFile(arg1: str, /) -> Any:
    """Read nodes from a file."""

def scriptReadText(arg1: str, /) -> Any:
    """Read nodes from a string."""

def scriptSave(filename: Any = ...) -> bool:
    """scriptSave(filename=None) -> bool

    Saves the current script to the current file name. If there is no current
    file name and Nuke is running in GUI mode, the user is asked for a name using
    the file chooser.

    :param filename: Save to this file name without changing the script name in the project (use scriptSaveAs() if you want it to change).
    :return: True if the file was saved, False if the user cancelled the operation.
      A RuntimeError is raised on other failures.)
    """

def scriptSaveAs(filename: Any = ..., overwrite: Any = ...) -> None:
    """scriptSaveAs(filename=None, overwrite=-1) -> None

    Saves the current script with the given file name if supplied, or (in GUI
    mode) asks the user for one using the file chooser. If Nuke is not running
    in GUI mode, you must supply a filename.

    :param filename: Saves the current script with the given file name if
     supplied, or (in GUI mode) asks the user for one using the file chooser.
    :param overwrite: If 1 (true) always overwrite; if 0 (false) never overwrite;
     otherwise, in GUI mode ask the user, in terminal do same as False. Default
     is -1, meaning 'ask the user'.
    """

def scriptSaveToTemp(string: Any) -> str:
    """scriptSaveToTemp(string) -> string

    Saves the script to a file without modifying the root information or the original script

    :param overwrite: Optional boolean to overwrite an existing file. If not specified, the behaviour defaults to False.
    :return: string
    """

def scriptSource(arg1: str, /) -> Any:
    """Same as scriptReadFile()."""

def selectAll() -> None:
    """selectAll() -> None

    Select all nodes in the DAG.

    :return: None
    """

def selectPattern() -> None:
    """selectPattern() -> None

    Selects nodes according to a regular expression matching pattern, entered
    through an input dialog. The pattern can include wildcards ('?' and '*') as
    well as regular expressions. The expressions are checked against the node
    name, label, class, and associated file names.

    :return: None
    """

def selectSimilar(matchType: int) -> None:
    """selectSimilar(matchType) -> None

    Selects nodes that match a node in the current selection based on matchType criteria.

    :param matchType: One of nuke.MATCH_CLASS, nuke.MATCH_LABEL, nuke.MATCH_COLOR.
    :return: None.
    """

def selectedNode() -> Node:
    """selectedNode() -> Node.

    Returns the selected node. This will recursively search for a selected node.
    If several nodes are selected, a selected node at the highest level will be returned.
    If none are selected, this produces a 'No node selected' error.

    :return: Node.
    """

def selectedNodes(filter: str = ..., recursive: bool = ...) -> list[Node]:
    """selectedNodes(filter, recursive) -> list

    Returns a list of all selected nodes in the current group by default.

    If recursive=True is specified, the algorithm will search recursively for selected nodes.
    An attempt is made to return them in 'useful' order where inputs are done before the final node,
    so commands applied to this list go from top-down.

    :param filter: Only return nodes of the specified node class.
    :type filter: str, optional
    :param recursive: If True, the algorithm will search recursively for selected nodes.
    :type recursive: bool, optional
    :return: The list of selected nodes.
    :rtype: list
    """

def setGeoSelection(GeoSelection: Any) -> None:
    """setGeoSelection(GeoSelection) -> None

    Set the currently selected geometry
    """

def setPreset(nodeClassName: Any, presetName: Any, knobValues: Any) -> None:
    """setPreset(nodeClassName, presetName, knobValues) -> None

    Create a node preset for the given node using the supplied knob values

    :param nodeClassName: Name of the node class to create a preset for.
    :param presetName: Name of the preset to create.
    :param knobValues: A dictionary containing a set of knob names and preset values.
    :return: bool.
    """

def setReadOnlyPresets(readOnly: bool) -> None:
    """setReadOnlyPresets(readOnly) -> None

    Sets whether newly created presets should be added in read-only mode.
    Read-only presets can be applied to a node, but can't be overwritten or deleted.
    """

def setUserPreset(nodeClassName: Any, presetName: Any, knobValues: Any) -> None:
    """setUserPreset(nodeClassName, presetName, knobValues) -> None

    Create a node preset for the given node using the supplied knob values

    :param nodeClassName: Name of the node class to create a preset for.
    :param presetName: Name of the preset to create.
    :param knobValues: A dictionary containing a set of knob names and preset values.
    :return: bool.
    """

def show(n: Any = ..., forceFloat: Any = ...) -> None:
    """show(n, forceFloat) -> None

    Opens a window for each named node, as though the user double-clicked on them.  For normal operators this opens the
    control panel, for viewers it opens the viewer, for groups it opens the control panel.

    :param n: Optional node argument. Default is the current node.
    :param forceFloat: Optional python object. If it evaluates to True it will open the window as a floating panel. Default is False.
    :return: None
    """

def showBookmarkChooser(n: Any) -> None:
    """showBookmarkChooser(n) -> None

    Show bookmark chooser search box.

    :return: None
    """

def showCreateViewsDialog(*args: Any, **kwargs: Any) -> Any:
    """pluginPath() -> string list

    List all the directories Nuke will search in for plugins.

    The built-in default is ~/.nuke and the 'plugins' directory from the
    same location the NUKE executable file is in. Setting the environment
    variable $NUKE_PATH to a colon-separated list of directories will
    replace the ~/.nuke with your own set of directories, but the plugins
    directory is always on the end.

    :return: List of paths.
    """

def showDag(n: Any = ...) -> None:
    """showDag(n) -> None

    Show the tree view of a group node or opens a node control panel.

    :param n: Optional Group.
    :return: None
    """

def showInfo(n: Any = ...) -> str:
    """showInfo(n) -> str

    Returns a long string of debugging information about each node and
    the operators it is currently managing. You should not rely on its
    contents or format being the same in different versions of Nuke.

    :param n: Optional node argument.
    :return: String.
    """

def showSettings() -> None:
    """showSettings() -> None

    Show the settings of the current group.

    :return: None
    """

def splayNodes() -> None:
    """splayNodes() -> None

    Deprecated. Use Group.splaySelectedNodes.

    :return: None
    """

def startEventGraphTimers() -> None:
    """startEventGraphTimers() -> None

    Start keeping track of events in the event graph.
    """

def startPerformanceTimers() -> None:
    """startPerformanceTimers() -> None

    Start keeping track of accumulated time on the performance timers, and display the accumulated time in the DAG.
    """

def stopEventGraphTimers() -> None:
    """stopEventGraphTimers() -> None

    Stop keeping track of events in the event graph.
    """

def stopPerformanceTimers() -> None:
    """stopPerformanceTimers() -> None

    Stop keeping track of accumulated time on the performance timers, and cease displaying the accumulated time in the DAG.
    """

def stripFrameRange(clipname: str) -> str:
    """stripFrameRange(clipname) -> string

    Strip out the frame range from a clipname, leaving a file path (still possibly with variables).

    :param clipname: The clipname.
    :return: The name without the frame range.
    """

def suspendPathProcessing() -> None:
    """suspendPathProcessing() -> None

    Suspend path processing.
    Use prior to performing multiple node graph modifications, to avoid repeated path processing.

    :return: None.
    """

def tabClose(*args: Any, **kwargs: Any) -> Any:
    """Close the active dock tab. Returns True if successful."""

def tabNext() -> bool:
    """Make the next tab in this dock active. Returns True if successful."""

def tcl(s: Any, *args: Any) -> str:
    """tcl(s, *args) -> str.

    Run a tcl command. The arguments must be strings and passed to
    the command. If no arguments are given and the command has whitespace in it
    then it is instead interpreted as a tcl program (this is deprecated).

    :param s: TCL code.
    :param args: The arguments to pass in to the TCL code.
    :return: Result of TCL command as string.
    """

def thisClass() -> str:
    """thisClass() -> None

    Get the class name of the current node. This equivalent to calling
    nuke.thisNode().Class(), only faster.

    :return: The class name for the current node.
    """

def thisGroup() -> Group:
    """thisGroup() -> Group

    Returns the current context Group node.

    :return: The group node.
    """

def thisKnob() -> Knob:
    """thisKnob() -> Knob

    Returns the current context knob if any.

    :return: Knob or None
    """

def thisNode() -> Node:
    """thisNode() -> Node.

    Return the current context node.

    :return: The node.
    """

def thisPane() -> Any:
    """thisPane() -> the active pane.

    Returns the active pane. This is only valid during a pane menu callback or window layout restoration.

    :return: The active pane.
    """

def thisParent() -> Node:
    """thisParent() -> Node

    Returns the current context Node parent.

    :return: A node.
    """

def thisRoot() -> Root:
    """thisRoot() -> Root

    Returns the current context Root node.

    :return: The root node.
    """

def thisView() -> str:
    """thisView() -> str

    Get the name of the current view.

    :return: The current view name as a string.
    """

def toNode(s: str) -> Node | None:
    """toNode(s) -> Node

    Search for a node in the DAG by name and return it as a Python object.

    :param s: Node name.
    :return: Node or None if it does not exist.
    """

def toggleFullscreen() -> None:
    """toggleFullscreen() -> None

    Toggles between windowed and fullscreen mode.

    :return: None
    """

def toggleViewers() -> None:
    """toggleViewers() -> None

    Toggles all the viewers on and off.

    :return: None
    """

def toolbar(name: Any, create: bool = ...) -> ToolBar:
    """toolbar(name, create=True)-> ToolBar

    Find and return the ToolBar object with the given name. The name of the
    built-in nodes toolbar is 'Nodes'.

    :param name: The name of the toolbar to find or create.
    :param create: Optional parameter. True (the default value) will mean that a new
     toolbar gets created if one with the given name couldn't be found; False will
     mean that no new toolbar will be created.
    :raises: A RuntimeException is thrown if not in GUI mode.
    :return: The toolbar, or None if no toolbar was found and 'create' was False.
    """

def tprint(*value: Any, sep: str = ..., end: str = ..., file: Any = ...) -> None:
    """tprint(value, ..., sep=' ', end='\\', file=sys.stdout) -> None

    Prints the values to a stream, or to stdout by default.

    :param value: A python object
    :param file: a file-like object (stream); defaults to stdout.
    :param sep: string inserted between values, default a space.
    :param end: string appended after the last value, default a newline.
    :return: None
    """

def undo() -> None:
    """undo() -> None

    Perform the most recent undo.

    :return: None
    """

def unlinkSelected() -> None:
    """unlinkSelected() -> None.

    Unlink all selected link nodes.

    :return: None
    """

def usingOcio() -> bool:
    """usingOCIO() -> returns true if using OCIO instead of Nuke LUTs.

    :return: bool
    """

def usingPerformanceTimers() -> bool:
    """usingPerformanceTimers() -> True if on, False if off

    :return: true if performance timers are in use.
    """

def value(knob: str, default: str | None = ...) -> str:
    """value(knob, default) -> string.

    The value function returns the current value of a knob. The knob argument is a string referring to a knob and default
    is an optional default value to be returned in case of an error. Unlike knob(), this will evaluate animation at the
    current frame, and expand brackets and dollar signs in string knobs.
    """

def views() -> list[str]:
    """views() -> List.

    List of all the globally existing views.

    :return: List
    """

def waitForThreadsToFinish() -> str:
    """waitForThreadsToFinish() -> str

    Returns true if Nuke should wait for any Python threads to finish before exitting.

    :return: True or False.
    """

def warning(message: str) -> None:
    """warning(message)-> None

    Puts the message into the error console, treating it like a warning.

    :param message: String parameter.
    :return: None.
    """

def zoom(scale: Any = ..., center: Any = ..., group: Any = ...) -> float:
    """zoom(scale, center, group) -> float

    Change the zoom and pan of a group's display. The scale argument is the new zoom factor.
    //If the group name is omitted then the current group is used. (Not yet implemented.)
    If the scale is given, but not the center, the zoom is set to that factor and the view is
    positioned so the cursor is pointing at the same place it was before zooming. A zero or negative
    scale value will cause a zoom-to-fit.

    If both scale and center arguments are given, the view is zoomed and then centered on the
    specified point.

    The new scale factor will be returned, or None if the function is run in a non-GUI context.

    :param scale: New zoom factor.
    :param center: Optional 2-item tuple specifying the center coordinates.
    :param group: Optional Group. This is ignored at present.
    :return: Current zoom factor or None if not in a GUI context.
    """

def zoomToFitSelected() -> None:
    """zoomToFitSelected() -> None

    Does a zoom to fit on the selected nodes in the DAG

    :return: None.
    """

scriptClose = _nuke_internal_scripts.scriptSaveAndClear
scriptExit = _hiero_core_nuke_NukeFunctionReplacement.scriptExitReplacementFunc
scriptOpen = _hiero_core_nuke_NukeFunctionReplacement.scriptOpenReplacementFunc
