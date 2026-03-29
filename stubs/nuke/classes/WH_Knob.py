"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class WH_Knob(Array_Knob):
    """
    A knob which holds width and height values.
    """

    def __new__(cls, *args, **kwargs) -> 'WH_Knob':
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

    def names(self, i: int) -> str:
        """
        Return name for dimension 'i'.
        """
        ...

    def x(self) -> float:
        """
        Return value for X position.
        """
        ...

    def y(self) -> float:
        """
        Return value for Y position.
        """
        ...

    def x_at(self, t: float) -> float:
        """
        Return value for X position at time 't'.
        """
        ...

    def y_at(self, t: float) -> float:
        """
        Return value for Y position at time 't'.
        """
        ...
