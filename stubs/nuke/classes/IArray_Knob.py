"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class IArray_Knob(Array_Knob):
    """
    IArray_Knob
    """

    def __new__(cls, *args, **kwargs) -> 'IArray_Knob':
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

    def dimensions(self) -> int:
        """
        Return number of dimensions.
        """
        ...

    def width(self) -> int:
        """
        Return width of the array.
        """
        ...

    def height(self) -> int:
        """
        Return height of the array.
        """
        ...

    def value(self, x: int, y: int) -> typing.Any:
        """
        Return value of the array at position (x, y).
        """
        ...
