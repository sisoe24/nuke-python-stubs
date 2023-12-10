from typing import *
from numbers import Number

import nuke

from . import *


class XYZ_Knob(Array_Knob):
    """
    A knob which holds a 3D coordinate.
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

    def names(self, n) -> str:
        """
        names(n) -> string

        Return name for dimension n. The argument n is an integer.
        """
        ...

    def value(self, n, oc) -> float:
        """
        value(n, oc) -> float

        Return value for dimension n. The optional argument oc is an OutputContext.
        """
        ...

    def parent(self,) -> XYZ_Knob:
        """
        parent() -> XYZ_Knob

        Return parent.
        """
        ...

    def x(self, oc) -> float:
        """
        x(oc) -> float

        Return value for x. The optional oc argument is an OutputContext
        """
        ...

    def y(self, oc) -> float:
        """
        y(oc) -> float

        Return value for y. The optional oc argument is an OutputContext
        """
        ...

    def z(self, oc) -> float:
        """
        z(oc) -> float

        Return value for z. The optional oc argument is an OutputContext
        """
        ...
