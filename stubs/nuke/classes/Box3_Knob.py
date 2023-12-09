from typing import *
from numbers import Number

import nuke

from . import *


class Box3_Knob(Array_Knob):
    """
    A 3-dimensional box.
    """

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

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def names(self, *args, **kwargs) -> None:
        """
        Return name for dimension 'i'
        """
        ...

    def value(self, *args, **kwargs) -> None:
        """
        Return value for dimension 'i'
        """
        ...

    def x(self, *args, **kwargs) -> None:
        """
        Return value for X position. X is the minimum horizontal extent of the box.
        """
        ...

    def setX(self, *args, **kwargs) -> None:
        """
        Set value for X position. X is the minimum horizontal extent of the box.
        """
        ...

    def y(self, *args, **kwargs) -> None:
        """
        Return value for Y position. Y is the minimum vertical extent of the box.
        """
        ...

    def setY(self, *args, **kwargs) -> None:
        """
        Set value for Y position. Y is the minimum vertical extent of the box.
        """
        ...

    def n(self, *args, **kwargs) -> None:
        """
        Return value for N position. N (near) is the minimum Z extent of the box.
        """
        ...

    def setN(self, *args, **kwargs) -> None:
        """
        Set value for N position. N (near) is the minimum Z extent of the box.
        """
        ...

    def r(self, *args, **kwargs) -> None:
        """
        Return value for R extent. R (right) is the right extent of the box.
        """
        ...

    def setR(self, *args, **kwargs) -> None:
        """
        Set value for R extent. R (right) is the right extent of the box.
        """
        ...

    def t(self, *args, **kwargs) -> None:
        """
        Return value for T extent. T (top) is the maximum vertical extent of the box.
        """
        ...

    def setT(self, *args, **kwargs) -> None:
        """
        Set value for T extent. T (top) is the maximum vertical extent of the box.
        """
        ...

    def f(self, *args, **kwargs) -> None:
        """
        Return value for F extent. F (far) is the maximum Z extent of the box.
        """
        ...

    def setF(self, *args, **kwargs) -> None:
        """
        Set value for F extent. F (far) is the maximum Z extent of the box.
        """
        ...
