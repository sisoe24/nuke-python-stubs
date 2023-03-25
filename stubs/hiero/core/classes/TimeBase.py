import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class TimeBase(Object):
    """
    Helper object that wraps up time bases (or frame rates). Stores values internally as integer ratios, as opposed to floating point values.

    Can be initialised with an int, float, or str.  In addition, you can construct a TimeBase using TimeBase.fromRational(numerator, denominator), or use the predefined TimeBase values, for example TimeBase.k30NTSC.
    """

    def __repr__(self) -> object:
        """
        Return repr(self).
        """
        return None

    def __lt__(self, value, ):
        """
        Return self<value.
        """
        return None

    def __le__(self, value, ):
        """
        Return self<=value.
        """
        return None

    def __eq__(self, value, ):
        """
        Return self==value.
        """
        return None

    def __ne__(self, value, ):
        """
        Return self!=value.
        """
        return None

    def __gt__(self, value, ):
        """
        Return self>value.
        """
        return None

    def __ge__(self, value, ):
        """
        Return self>=value.
        """
        return None

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def convert(self, *args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, ...):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
        return Any

    def convertTime(self, t: int, toRate: core.TimeBase) -> int:
        """
        self.convertTime(t, toRate) -> returns the time specified by the first parameter converted from this object's time base into the second parameter's time base.
        If either of the time bases is invalid, this method returns the t parameter unchanged.

        @param t: the time (frame) to convert from one rate to another
        @param toRate: the new time time to convert to
        @return: integer
        """
        return int()

    def denominator(self) -> int:
        """
        self.denominator() -> gets the denominator of the time base.
        @return: int
        """
        return int()

    def fromRational(self, *args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, ...):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
        return Any

    def fromString(self, *args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, ...):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
        return Any

    def isNTSC(self) -> bool:
        """
        self.isNTSC() -> returns True if the time base is NTSC (24*1000/1001, 30*1000/1001, or 60*1000/1001).

        @return: True or False
        """
        return Union[True, False]

    def isValid(self) -> bool:
        """
        self.isValid() -> returns True if the denominator of the time base is non-zero.

        @return: True or False
        """
        return Union[True, False]

    def numerator(self) -> int:
        """
        self.numerator() -> gets the numerator of the time base.
        @return: int
        """
        return int()

    def supportsDropFrames(self) -> bool:
        """
        self.supportsDropFrames() -> returns True if the time base supports drop frames (only true for 30 or 60 fps NTSC currently).

        @return: True or False
        """
        return Union[True, False]

    def toFloat(self) -> float:
        """
        self.toFloat() -> returns the time base value expressed as a floating point value.

        @return: float
        """
        return float()

    def toInt(self) -> int:
        """
        self.toInt() -> returns the time base value, rounded to the nearest integer.

        @return: int
        """
        return int()

    def toRational(self) -> typing.Tuple[int, int]:
        """
        self.toRational() -> returns a tuple of the numerator and the denominator of the time base.

        @return: tuple of integers
        """
        return tuple()

    def toRationalString(self) -> str:
        """
        self.toRationalString() -> returns a string containing the time base expressed as a ratio, for example '30000/1001'.

        @return: string
        """
        return str()

    def toString(self) -> str:
        """
        self.toString() -> returns a string containing the time base as a floating point number. Equivalent to str(object).

        @return: string
        """
        return str()

    def __copy__(self,) -> None:
        """

        """
        return None

    __hash__: Any = None
    RoundingMode: Any = None
    kRoundNearest: Any = None
    kRound32Pulldown: Any = None
    k24: Any = None
    k25: Any = None
    k30: Any = None
    k50: Any = None
    k60: Any = None
    k24NTSC: Any = None
    k30NTSC: Any = None
    k60NTSC: Any = None
