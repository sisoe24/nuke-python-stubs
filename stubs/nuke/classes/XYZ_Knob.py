"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class XYZ_Knob(Array_Knob):
    """
    A knob which holds a 3D coordinate.
    """

    def __new__(cls, *args, **kwargs) -> 'XYZ_Knob':
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __hash__(self) -> int:
        """
        Return hash(self).
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def names(self, n: int) -> str:
        """
        names(n) -> string

        Return name for dimension n. The argument n is an integer.
        """
        ...

    def value(self, n: int, oc: Optional['OutputContext'] = None) -> float:
        """
        value(n, oc) -> float

        Return value for dimension n. The optional argument oc is an OutputContext.
        """
        ...

    def parent(self) -> Optional[XYZ_Knob]:
        """
        parent() -> XYZ_Knob

        Return parent.
        """
        ...

    def x(self, oc: Optional['OutputContext'] = None) -> float:
        """
        x(oc) -> float

        Return value for x. The optional oc argument is an OutputContext
        """
        ...

    def y(self, oc: Optional['OutputContext'] = None) -> float:
        """
        y(oc) -> float

        Return value for y. The optional oc argument is an OutputContext
        """
        ...

    def z(self, oc: Optional['OutputContext'] = None) -> float:
        """
        z(oc) -> float

        Return value for z. The optional oc argument is an OutputContext
        """
        ...
