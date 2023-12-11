from typing import *
from numbers import Number

import nuke

from . import *


class Knob(object):
    """
    A modifiable control that appears (unless hidden) in the panel for a node.
    This is a base class that specific knob types inherit from.

    Knobs can be animated, have expressions, be disabled or hidden and more.
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def Class(self,) -> str:
        """
        self.Class() -> Class name.
        @return: Class name.
        """
        ...

    def ClassID(self,) -> str:
        """
        self.ClassID() -> Class ID.
        @return: Class ID.
        """
        ...

    def node(self,) -> Node:
        """
        self.node() -> nuke.Node
        Return the node that this knob belongs to. If the node has been cloned, we'll always return a reference to the original.
        @return: The node which owns this knob, or None if the knob has no owner yet.
        """
        ...

    def name(self,) -> str:
        """
        self.name() -> name.
        @return: name.
        """
        ...

    def setName(self, s: str) -> None:
        """
        self.setName(s) -> None.
        @param s: New name.
        @return: None.
        """
        ...

    def error(self, message: str) -> None:
        """
        self.error(message) -> None.
        @param message: message to put the knob in error.
        @return: None.
        """
        ...

    def critical(self, message: str) -> None:
        """
        self.critical(message) -> None.
        @param message: message to put the knob in error, and do a popup.
        @return: None.
        """
        ...

    def warning(self, message: str) -> None:
        """
        self.warning(message) -> None.
        @param message: message to put a warning on the knob.
        @return: None.
        """
        ...

    def debug(self, message: str) -> None:
        """
        self.debug(message) -> None.
        @param message: message to put out to the error console, attached to the knob, if the verbosity level is set high enough.
        @return: None.
        """
        ...

    def label(self,) -> str:
        """
        self.label() -> label.
        @return: label.
        """
        ...

    def setLabel(self, s: str) -> None:
        """
        self.setLabel(s) -> None.
        @param s: New label.
        @return: None.
        """
        ...

    def tooltip(self,) -> str:
        """
        self.tooltip() -> tooltip.
        @return: tooltip.
        """
        ...

    def setTooltip(self, s: str) -> None:
        """
        self.setTooltip(s) -> None.
        @param s: New tooltip.
        @return: None.
        """
        ...

    def setFlag(self, f) -> None:
        """
        self.setFlag(f) -> None.
        Logical OR of the argument and existing knob flags.
        @param f: Flag.
        @return: None.
        """
        ...

    def getFlag(self, f) -> bool:
        """
        self.getFlag(f) -> Bool.
        Returns whether the input flag is set.
        @param f: Flag.
        @return: True if set, False otherwise.
        """
        ...

    def clearFlag(self, f) -> None:
        """
        self.clearFlag(f) -> None.
        Clear flag.
        @param f: Flag.
        @return: None.
        """
        ...

    def setValue(self, val, chan) -> bool:
        """
        self.setValue(val, chan) -> bool

        Sets the value 'val' at channel 'chan'.
        @return: True if successful, False if not.
        """
        ...

    def setValueAt(self, val, time, chan) -> bool:
        """
        self.setValueAt(val, time, chan) -> bool

        Sets the value 'val' at channel 'chan' for time 'time'.
        @return: True if successful, False if not.
        """
        ...

    def getValue(self, *args, **kwargs) -> None:
        """
        Return value at the current frame for channel 'c'.
        """
        ...

    def value(self, *args, **kwargs) -> None:
        """
        Return value at the current frame for channel 'c'.
        """
        ...

    def getValueAt(self, *args, **kwargs) -> None:
        """
        Return value at time 't' for channel 'c'.
        """
        ...

    def getKeyList(self, *args, **kwargs) -> None:
        """
        Get all unique keys on the knob.  Returns list.
        """
        ...

    def removeKey(self, *args, **kwargs) -> None:
        """
        Remove key for channel 'c'. Return True if successful.
        """
        ...

    def removeKeyAt(self, *args, **kwargs) -> None:
        """
        Remove key at time 't' for channel 'c'. Return True if successful.
        """
        ...

    def isKey(self, *args, **kwargs) -> None:
        """
        Return True if there is a keyframe at the current frame for channel 'c'.
        """
        ...

    def isKeyAt(self, *args, **kwargs) -> None:
        """
        Return True if there is a keyframe at time 't' for channel 'c'.
        """
        ...

    def getNumKeys(self, *args, **kwargs) -> None:
        """
        Return number of keyframes for channel 'c'.
        """
        ...

    def getKeyIndex(self, *args, **kwargs) -> None:
        """
        Return keyframe index at time 't' for channel 'c'.
        """
        ...

    def getKeyTime(self, *args, **kwargs) -> None:
        """
        Return index of the keyframe at time 't' for channel 'c'.
        """
        ...

    def getDerivative(self, *args, **kwargs) -> None:
        """
        Return derivative at time 't' for channel 'c'.
        """
        ...

    def getNthDerivative(self, *args, **kwargs) -> None:
        """
        Return nth derivative at time 't' for channel 'c'.
        """
        ...

    def getIntegral(self, *args, **kwargs) -> None:
        """
        Return integral at the interval [t1, t2] for channel 'c'.
        """
        ...

    def setAnimated(self, *args, **kwargs) -> None:
        """
        Set channel 'c' to be animated.
        """
        ...

    def isAnimated(self, *args, **kwargs) -> None:
        """
        Return True if channel 'c' is animated.
        """
        ...

    def clearAnimated(self, *args, **kwargs) -> None:
        """
        Clear animation for channel 'c'. Return True if successful.
        """
        ...

    def hasExpression(self, index=-1) -> bool:
        """
        self.hasExpression(index=-1) -> bool
        Return True if animation at index 'index' has an expression.
        @param index: Optional index parameter. Defaults to -1 if not specified. This can be specified as a keyword parameter if desired.
        @return: True if has expression, False otherwise.
        """
        ...

    def setExpression(self, expression: str, channel=-1, view=None) -> bool:
        """
        self.setExpression(expression, channel=-1, view=None) -> bool
        Set the expression for a knob. You can optionally specify a channel to set the expression for.

        @param expression: The new expression for the knob. This should be a string.
        @param channel: Optional parameter, specifying the channel to set the expression for. This should be an integer.
        @param view: Optional view parameter. Without, this command will set the expression for the current view theinterface is displaying. Can be the name of the view or the index.
        @return: True if successful, False if not.
        """
        ...

    def toScript(self, quote, context=None) -> str:
        """
        toScript(quote, context=current) -> string.

        Return the value of the knob in script syntax.
        Pass True for quote to return results quoted in {}.
        Pass None for context to get results for all views and key times (as stored in a .nk file).
        """
        ...

    def fromScript(self, *args, **kwargs) -> None:
        """
        Initialise from script.
        """
        ...

    def fullyQualifiedName(self, channel=-1) -> str:
        """
        self.fullyQualifiedName(channel=-1) -> string
        Returns the fully-qualified name of the knob within the node. This can be useful for expression linking.

        @param channel: Optional parameter, specifies the channel number of the sub-knob (for example, channels of  0 and 1 would refer to the x and y of a XY_Knob respectively), leave blank or set to -1 to get the  qualified name of the knob only.
        @return: The string of the qualified knob or sub-knob, which can be used directly in expression links.
        """
        ...

    def setEnabled(self, enabled: bool) -> None:
        """
        self.setEnabled(enabled) -> None.

        Enable or disable the knob.
        @param enabled: True to enable the knob, False to disable it.
        """
        ...

    def enabled(self,) -> bool:
        """
        self.enabled() -> Boolean.

        @return: True if the knob is enabled, False if it's disabled.
        """
        ...

    def setVisible(self, visible: bool) -> None:
        """
        self.setVisible(visible) -> None.

        Show or hide the knob.
        @param visible: True to show the knob, False to hide it.
        """
        ...

    def visible(self,) -> bool:
        """
        self.visible() -> Boolean.

        @return: True if the knob is visible, False if it's hidden.
        """
        ...

    def getAuthorModes(self,) -> list:
        """
        self.getAuthorModes() -> List.
        Returns the names of the authoring modes of the knob if the knob is an authoring knob, otherwise an empty list.
        @return: The names of the authoring modes of the knob if the knob is an authoring knob, otherwise an empty list. This is a list of strings.
        """
        ...

    def getAuthorMode(self,) -> str:
        """
        self.getAuthorMode() -> Integer.
        Returns the authoring mode currently set on the knob. This is a unique string identifier of the option, which is also used for serialisation and deserialisation. It is not meant to change,thus one can rely on it.
        @return: The string identifier of the current authoring mode set.
        """
        ...

    def setAuthorMode(self, authorMode: int) -> None:
        """
        self.setAuthorMode(authorMode) -> None.
        Sets the authoring mode on the knob. This accepts both the unique string identifier, which is also used for serialisation and deserialisation, or index of the option for convenience. These values are not meant to change, thus one can rely on them.
        @param authorMode: The string identifier or index of the authoring mode.
        @return: None.
        """
        ...

    def makeWidget(self,) -> Any:
        """
        self.makeWidget() -> PySide2.QtWidgets.QWidget.
        Returns an instance of the QWidget subclass used to edit the knob's value.
        The widget will update the knob's value when its value changes and should
        update its displayed value(s) when they change on the knob.
        Can return null if no widget should be created for the knob.
        @return: PySide2.QtWidgets.QWidget.
        """
        ...
