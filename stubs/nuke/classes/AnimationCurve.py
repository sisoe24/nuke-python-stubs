from typing import *
from numbers import Number

import nuke

from . import *


class AnimationCurve(object):
    """
    AnimationCurve
    """

    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def size(self,) -> Number:
        """
        self.size() -> Number of keys.
        @return: Number of keys.
        """
        ...

    def keys(self,) -> list:
        """
        self.keys() -> List of keys.
        @return: List of keys.
        """
        ...

    def knobAndFieldName(self,) -> str:
        """
        self.knobAndFieldName() -> string.
        Knob and field name combined (e.g. 'translate.x').
        @return: string.
        """
        ...

    def knob(self,) -> Knob:
        """
        self.knob() -> Knob.
        Return knob this animation belongs to.@return: Knob.
        """
        ...

    def knobIndex(self,) -> int:
        """
        self.knobIndex() -> Int.
        Return the knob index this animation belongs to.@return: Int.
        """
        ...

    def noExpression(self,) -> bool:
        """
        self.noExpression() -> bool
        @return: True if the expression is the default expression (i.e. the keys
        control the curve), False otherwise.
        """
        ...

    def constant(self,) -> bool:
        """
        self.constant() -> bool
        @return: True if the animation appears to be a horizontal line, is a simple
        number, or it is the default and all the points are at the same y value and
        have 0 slopes. False otherwise.
        """
        ...

    def identity(self,) -> bool:
        """
        self.identity() -> bool
        @return: True if the animation appears to be such that y == x everywhere. This
        is True only for an expression of 'x' or the default expression and all points
        having y == x and slope == 1. Extrapolation is ignored.
        """
        ...

    def selected(self,) -> bool:
        """
        self.selected() -> bool
        @return: True if selected, False otherwise.
        """
        ...

    def evaluate(self, t: Number) -> Number:
        """
        self.evaluate(t) -> float
        Value at time 't'.
        @param t: Time.
        @return: The value of the animation at time 't'.
        """
        ...

    def derivative(self, t: Number, n: Optional[int] = None) -> float:
        """
        self.derivative(t, n) -> Float.
        The n'th derivative at time 't'. If n is less than 1 it returns evaluate(t).
        @param t: Time.
        @param n: Optional. Default is 1.
        @return: The value of the derivative.
        """
        ...

    def inverse(self, y) -> float:
        """
        self.inverse(y) -> Float.
        The inverse function at value y. This is the value of x such that evaluate(x)
        returns y.
        This is designed to invert color lookup tables. It only works if the
        derivative is zero or positive everywhere.
        @param y: The value of the function to get the inverse for.
        @return: Float.
        """
        ...

    def integrate(self, t1: Number, t2: Number) -> float:
        """
        self.integrate(t1, t2) -> Float.
        Calculate the area underneath the curve from t1 to t2.
        @param t1 The start of the integration range.
        @param t2 The end of the integration range.
        @return: The result of the integration.
        """
        ...

    def setKey(self, t: Number, y) -> Any:
        """
        self.setKey(t, y) -> Key.
        Set a key at time t and value y. If there is no key
        there one is created. If there is a key there it is moved
        vertically to be at y.  If a new key is inserted the
        interpolation and extrapolation are copied from a neighboring key, if
        there were no keys then it is set to nuke.SMOOTH interpolation and
        nuke.CONSTANT extrapolation.
        @param t: The time to set the key at.
        @param y: The value for the key.
        @return: The new key.
        """
        ...

    def addKey(self, keys: Iterable) -> None:
        """
        self.addKey(keys) -> None.
        Insert a sequence of keys.
        @param keys: Sequence of AnimationKey.
        @return: None.
        """
        ...

    def clear(self,) -> None:
        """
        self.clear() -> None.
        Delete all keys.
        @return: None.
        """
        ...

    def setExpression(self, s: str) -> None:
        """
        self.setExpression(s) -> None.
        Set expression.
        @param s: A string containing the expression.
        @return: None.
        """
        ...

    def expression(self,) -> str:
        """
        self.expression() -> String.
        Get the expression.@return: String.
        """
        ...

    def changeInterpolation(self, keys: Iterable, type) -> None:
        """
        self.changeInterpolation(keys, type) -> None.
        Change interpolation (and extrapolation) type for the keys.
        @param keys: Sequence of keys.
        @param type: Interpolation type. One of:
               nuke.HORIZONTAL
               nuke.BREAK
               nuke.BEFORE_CONST
               nuke.BEFORE_LINEAR
               nuke.AFTER_CONST
               nuke.AFTER_LINEAR.
        @return: None.
        """
        ...

    def fromScript(self, s: str) -> None:
        """
        self.fromScript(s) -> None.
        @param s: String.
        @return: None.
        """
        ...

    def toScript(self, selected: Optional[bool] = None) -> str:
        """
        self.toScript(selected) -> str
        @param selected: Optional parameter. If this is given and is True, then only
        process the selected curves; otherwise convert all.
        @return: A string containing the curves.
        """
        ...

    def fixSlopes(self,) -> None:
        """
        self.fixSlopes() -> None.
        @return: None.
        """
        ...

    def view(self,) -> str:
        """
        self.view() -> String.
        The view this AnimationCurve object is associated with.
        @return: String.
        """
        ...

    def removeKey(self, keys: Iterable) -> None:
        """
        self.removeKey(keys) -> None.
        Remove some keys from the curve.
        @param keys: The sequence of keys to be removed.
        @return: None.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
