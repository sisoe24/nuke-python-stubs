from typing import *
from numbers import Number

import nuke

from . import *


class Array_Knob(Knob):
    """
    A knob which holds an array of values.
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

    def vect(self,) -> list:
        """
        self.vect() -> List of knob values.
        @return: List of knob values.
        Should only be used for knobs that are neither animated
        nor get their values from a ValueProvider.
        For knobs like that, use Array_Knob.getValue, instead
        """
        ...

    def array(self,) -> list:
        """
        self.array() -> List of knob values.
        @return: List of knob values.
        Should only be used for knobs that are neither animated
        nor get their values from a ValueProvider.
        For knobs like that, use Array_Knob.getValue, instead
        """
        ...

    def width(self,) -> list:
        """
        self.width() -> Width of array of values.
        @return: Width of array of values.
        """
        ...

    def height(self,) -> list:
        """
        self.height() -> Height of array of values.
        @return: Height of array of values.
        """
        ...

    def arraySize(self,) -> list:
        """
        self.arraySize() -> Number of elements in array.
        @return: Number of elements in array.
        """
        ...

    def dimensions(self,) -> list:
        """
        self.dimensions() -> Dimensions in array.
        @return: Dimensions in array.
        """
        ...

    def resize(self, w: Number, h: Optional[Number] = None) -> bool:
        """
        self.resize(w, h) -> True if successful, False otherwise.
        Resize the array.
        @param w: New width
        @param h: Optional new height
        @return: True if successful, False otherwise.
        """
        ...

    def fromScript(self, s: str) -> bool:
        """
        self.fromScript(s) -> True if successful, False otherwise.
        Set value of the knob to a user defined script (TCL syntax, as in .nk file). Return True if successful.
        @param s: Nuke script to be set on knob.
        @return: True if successful, False otherwise.
        """
        ...

    def toScript(self, quote: Optional[bool] = None, context: Optional[str] = None) -> str:
        """
        self.toScript(quote, context) -> String.
        Return the value of the knob in script syntax.
        @param quote: Optional, default is False. Specify True to return the knob value quoted in {}.
        @param context: Optional context, default is current, None will be "contextless" (all views, all keys) as in a .nk file.
        @return: String.
        """
        ...

    def notDefault(self,) -> bool:
        """
        self.notDefault() -> True if any of the values is not set to the default, False otherwise.
        @return: True if any of the values is not set to the default, False otherwise.
        """
        ...

    def defaultValue(self,) -> Any:
        """
        self.defaultValue() -> Default value.
        @return: Default value.
        """
        ...

    def setDefaultValue(self, s: Iterable) -> None:
        """
        self.setDefaultValue(s) -> None.
        @param s: Sequence of floating-point values.
        @return: None.
        """
        ...

    def min(self,) -> Number:
        """
        self.min() -> Minimum value.
        @return: Minimum value.
        """
        ...

    def min(self,) -> Number:
        """
        self.min() -> Minimum value.
        @return: Minimum value.
        """
        ...

    def max(self,) -> Number:
        """
        self.max() -> Maximum value.
        @return: Maximum value.
        """
        ...

    def max(self,) -> Number:
        """
        self.max() -> Maximum value.
        @return: Maximum value.
        """
        ...

    def setRange(self, f1: Number, f2: Number) -> None:
        """
        self.setRange(f1, f2) -> None.
        Set range of values.
        @param f1 Min value.
        @param f2 Max value.
        @return: None.
        """
        ...

    def singleValue(self, view=None) -> bool:
        """
        self.singleValue(view) -> True if holds a single value.
        @param view: Optional view. Default is current view.
        @return: True if holds a single value.
        """
        ...

    def setSingleValue(self, b: bool, view=None) -> None:
        """
        self.setSingleValue(b, view) -> None.
        Set to just hold a single value or not.
        @param b: Boolean object.
        @param view: Optional view. Default is current view.
        @return: None.
        """
        ...

    def frame(self,) -> int:
        """
        self.frame() -> Frame number.
        @return: Frame number.
        """
        ...

    def setValue(self, value: float, index: Optional[int] = None, time: Optional[Number] = None, view=None) -> bool:
        """
        self.setValue(value, index, time, view) -> True if value changed, False otherwise. Safe to ignore.
        Set index to value at time and view.
        @param value: Floating point value.
        @param index: Optional index.
        @param time: Optional time.
        @param view: Optional view.
        @return: True if value changed, False otherwise. Safe to ignore.
        """
        ...

    def setValueAt(self, value: float, time: Number, index: Optional[int] = None, view=None) -> bool:
        """
        self.setValueAt(value, time, index, view) -> bool.
        Set value of element 'index' at time for view. If the knob is animated, it will set a new keyframe or change an existing one. Index and view are optional. Return True if successful.
        @param value: Floating point value.
        @param time: Time.
        @param index: Optional index.
        @param view: Optional view.
        @return: True if value changed, False otherwise. Safe to ignore.
        """
        ...

    def value(self, index: Optional[int] = None, view=None, time: Optional[Number] = None) -> list:
        """
        self.value(index, view, time) -> Floating point or List of floating point values (in case some are different).
        @param index: Optional index. Default is 0.
        @param view: Optional view.
        @param time: Optional time.
        @return: Floating point or List of floating point values (in case some are different).
        """
        ...

    def value(self, index: Optional[int] = None, view=None, time: Optional[Number] = None) -> list:
        """
        self.value(index, view, time) -> Floating point or List of floating point values (in case some are different).
        @param index: Optional index. Default is 0.
        @param view: Optional view.
        @param time: Optional time.
        @return: Floating point or List of floating point values (in case some are different).
        """
        ...

    def valueAt(self, time: Number, index: Optional[int] = None, view=None) -> list:
        """
        self.valueAt(time, index, view) -> Floating point or List of floating point values (in case some are different).
        Return value for this knob at specified time, optional index and view.
        @param time: Time.
        @param index: Optional index. Default is 0.
        @param view: Optional view.
        @return: Floating point or List of floating point values (in case some are different).
        """
        ...

    def valueAt(self, time: Number, index: Optional[int] = None, view=None) -> list:
        """
        self.valueAt(time, index, view) -> Floating point or List of floating point values (in case some are different).
        Return value for this knob at specified time, optional index and view.
        @param time: Time.
        @param index: Optional index. Default is 0.
        @param view: Optional view.
        @return: Floating point or List of floating point values (in case some are different).
        """
        ...

    def setKeyAt(self, time: Number, index: Optional[int] = None, view=None) -> None:
        """
        self.setKeyAt(time, index, view) -> None.
        Set a key on element 'index', at time and view.
        @param time: Time.
        @param index: Optional index.
        @param view: Optional view.
        @return: None.
        """
        ...

    def removeKey(self, index: Optional[int] = None, view=None) -> bool:
        """
        self.removeKey(index, view) -> True if succeeded, False otherwise.
        Remove key.
        @param index: Optional index.
        @param view: Optional view.
        @return: True if succeeded, False otherwise.
        """
        ...

    def removeKeyAt(self, time: Number, index: Optional[int] = None, view=None) -> bool:
        """
        self.removeKeyAt(time, index, view) -> True if succeeded, False otherwise.
        Remove keyframe at specified time, optional index and view. Return True if successful.
        @param time: Time.
        @param index: Optional index.
        @param view: Optional view.
        @return: True if succeeded, False otherwise.
        """
        ...

    def isKey(self, index: Optional[int] = None, view=None) -> bool:
        """
        self.isKey(index, view) -> True if succeeded, False otherwise.
        @param index: Optional index.
        @param view: Optional view.
        @return: True if succeeded, False otherwise.
        """
        ...

    def isKeyAt(self, time: Number, index: Optional[int] = None, view=None) -> bool:
        """
        self.isKeyAt(time, index, view) -> True if succeeded, False otherwise.
        Returns True if there is a keyframe at specified time, optional index and view, otherwise returns False.
        @param time: Time.
        @param index: Optional index.
        @param view: Optional view.
        @return: True if succeeded, False otherwise.
        """
        ...

    def getNumKeys(self, *args, **kwargs) -> None:
        """
        Return number of keys at channel 'c'.
        """
        ...

    def getKeyIndex(self, *args, **kwargs) -> None:
        """
        Return index of the keyframe at time 't' and channel 'c'.
        """
        ...

    def getKeyTime(self, *args, **kwargs) -> None:
        """
        Return time of the keyframe at time 't' and channel 'c'.
        """
        ...

    def getDerivative(self, *args, **kwargs) -> None:
        """
        Return derivative at time 't' and index 'i'.
        """
        ...

    def getNthDerivative(self, *args, **kwargs) -> None:
        """
        Return n'th derivative at time 't' and index 'i'.
        """
        ...

    def getIntegral(self, *args, **kwargs) -> None:
        """
        Return integral at time interval [t1, t2] and index 'i'.
        """
        ...

    def setAnimated(self, index: Optional[int] = None, view=None) -> bool:
        """
        self.setAnimated(index, view) -> True if succeeded, False otherwise.
        Create an Animation object. Return True if successful, in which case caller must initialise it by calling setValue() or setValueAt().
        @param index: Optional index.
        @param view: Optional view.
        @return: True if succeeded, False otherwise.
        """
        ...

    def isAnimated(self, index: Optional[int] = None, view=None) -> bool:
        """
        self.isAnimated(index, view) -> True if animated, False otherwise.
        @param index: Optional index.
        @param view: Optional view.
        @return: True if animated, False otherwise.
        """
        ...

    def clearAnimated(self, index: Optional[int] = None, view=None) -> bool:
        """
        self.clearAnimated(index, view) -> True if succeeded, False otherwise.
        Delete animation.
        @param index: Optional index.
        @param view: Optional view.
        @return: True if succeeded, False otherwise.
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

    def hasExpression(self, index: Optional[int] = None) -> bool:
        """
        self.hasExpression(index) -> True if has expression, False otherwise.
        @param index: Optional index.
        @return: True if has expression, False otherwise.
        """
        ...

    def splitView(self, view=None) -> None:
        """
        self.splitView(view) -> None.
        Split the view away from the current knob value.
        @param view: Optional view. Default is current view.
        @return: None.
        """
        ...

    def unsplitView(self, view=None) -> None:
        """
        self.unsplitView(view) -> None.
        Unsplit the view so that it shares a value with other views.
        @param view: Optional view. Default is current view.
        @return: None.
        """
        ...

    def animations(self, view=None) -> list:
        """
        self.animations(view) -> AnimationCurve list.
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
        ...

    def animation(self, chan, view=None) -> Union[AnimationCurve, None]:
        """
        self.animation(chan, view) -> AnimationCurve or None.
        Return the AnimationCurve for the  channel 'chan' and view 'view'. The view argument is optional.
        @param channel: The channel index.
        @param view: Optional view.
        @return: AnimationCurve or None.
        """
        ...

    def deleteAnimation(self, curve: AnimationCurve) -> None:
        """
        self.deleteAnimation(curve) -> None. Raises ValueError if not found.
        Deletes the AnimationCurve.
        @param curve: An AnimationCurve instance which belongs to this Knob.
        @return: None. Raises ValueError if not found.
        """
        ...

    def copyAnimation(self, channel: int, curve: AnimationCurve, view=None) -> None:
        """
        self.copyAnimation(channel, curve, view) -> None.
        Copies the i'th channel of the AnimationCurve curve to this object. The view is optional and defaults to the current view.
        @param channel: The channel index.
        @param curve: AnimationCurve.
        @param view: Optional view. Defaults to current.
        @return: None.
        """
        ...

    def copyAnimations(self, curves: list, view=None) -> None:
        """
        self.copyAnimations(curves, view) -> None.
        Copies the AnimationCurves from curves to this object. The view is optional and defaults to the current view.
        @param curves: AnimationCurve list.
        @param view: Optional view. Defaults to current.
        @return: None.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
