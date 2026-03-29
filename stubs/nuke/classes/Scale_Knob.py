"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class Scale_Knob(Array_Knob):
    """
    Scale_Knob
    """

    def __new__(cls, *args, **kwargs) -> Scale_Knob:
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

    def value(self, n: int, oc: OutputContext | None = None) -> float:
        """
        value(n, oc) -> float

        Return value for dimension n. The optional argument oc is an OutputContext.
        """
        ...

    def x(self, oc: OutputContext | None = None) -> float:
        """
        x(oc) -> float

        Return value for x. The optional oc argument is an OutputContext
        """
        ...

    def y(self, oc: OutputContext | None = None) -> float:
        """
        y(oc) -> float

        Return value for y. The optional oc argument is an OutputContext
        """
        ...

    def z(self, oc: OutputContext | None = None) -> float:
        """
        z(oc) -> float

        Return value for z. The optional oc argument is an OutputContext
        """
        ...
