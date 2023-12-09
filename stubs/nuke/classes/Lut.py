from typing import *
from numbers import Number

import nuke

from . import *


class Lut(object):
    """
    Lut
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

    def isLinear(self,) -> bool:
        """
        self.isLinear() -> True if toByte(x) appears to return x*255, False otherwise.
        """
        ...

    def isZero(self,) -> int:
        """
        self.isZero() -> True if toByte(0) returns a value <= 0, False otherwise.
        """
        ...

    def toByte(self, float) -> float:
        """
        self.toByte(float) -> float.

        Converts floating point values to byte values in the range 0-255.
        """
        ...

    def fromByte(self, float) -> float:
        """
        self.fromByte(float) -> float.

        Converts byte values in the range 0-255 to floating point.
        """
        ...

    def toByte(self, float) -> float:
        """
        self.toByte(float) -> float.

        Converts floating point values to byte values in the range 0-255.
        """
        ...

    def fromByte(self, float) -> float:
        """
        self.fromByte(float) -> float.

        Converts byte values in the range 0-255 to floating point.
        """
        ...

    def toFloat(self, src, alpha) -> list:
        """
        toFloat(src, alpha) -> float list.

        Convert a sequence of floating-point values to to_byte(x)/255.
        Alpha is an optional argument and if present unpremultiply by alpha, convert, and then multiply back.
        """
        ...

    def fromFloat(self, src, alpha) -> list:
        """
        fromFloat(src, alpha) -> float list.

        Convert a sequence of floating-point values to from_byte(x*255).
        Alpha is an optional argument and if present unpremultiply by alpha, convert, and then multiply back.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
