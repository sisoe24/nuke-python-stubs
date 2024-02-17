"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class Info(object):
    """
    An info object stores x, y, w and h values.
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

    def x(self,) -> float:
        """
        x() -> float

        Return left edge.
        """
        ...

    def y(self,) -> float:
        """
        self.y() -> float

        Return the bottom edge.
        """
        ...

    def w(self,) -> float:
        """
        self.w() -> float

        Return width.
        """
        ...

    def h(self,) -> float:
        """
        self.h() -> float

        Return height.
        """
        ...
