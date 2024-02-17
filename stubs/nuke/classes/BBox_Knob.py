"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class BBox_Knob(Array_Knob):
    """
    A knob which holds a bounding box.
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

    def names(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return name for dimension 'i'
        """
        ...

    def value(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return value for dimension 'i'
        """
        ...

    def x(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return value for X position.
        """
        ...

    def setX(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Set value for X position.
        """
        ...

    def y(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return value for Y position.
        """
        ...

    def setY(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Set value for Y position.
        """
        ...

    def r(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return value for R extent.
        """
        ...

    def setR(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Set value for R extent.
        """
        ...

    def t(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return value for T extent.
        """
        ...

    def setT(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Set value for T extent.
        """
        ...

    def toDict(self,) -> dict:
        """
        self.toDict() -> dict.

        Returns the bounding box as a dict with x, y, r, and t keys.
        @return: dict with x, y, r and t keys
        """
        ...

    def fromDict(self, box: dict) -> None:
        """
        self.fromDict(box) -> None

        Set the bounding box from the given box.
        @param box: Dictionary containing the x, y, r and t keys.
        @return: None
        """
        ...
