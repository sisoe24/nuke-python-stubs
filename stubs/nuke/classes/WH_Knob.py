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
        Return name for dimension 'i'.
        """
        ...

    def x(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return value for X position.
        """
        ...

    def y(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return value for Y position.
        """
        ...

    def x_at(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return value for X position at time 't'.
        """
        ...

    def y_at(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return value for Y position at time 't'.
        """
        ...
