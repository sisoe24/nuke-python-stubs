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

    def dimensions(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return number of dimensions.
        """
        ...

    def width(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return width of the array.
        """
        ...

    def height(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return height of the array.
        """
        ...

    def value(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return value of the array at position (x, y).
        """
        ...
