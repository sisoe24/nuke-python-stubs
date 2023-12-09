import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class ViewerCursor(Object):
    """

    """

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

    def __copy__(self,) -> None:
        """

        """
        ...

    @property
    def pos(self) -> Any:
        """

        """
        ...

    @property
    def color(self) -> Any:
        """

        """
        ...

    @property
    def label(self) -> Any:
        """

        """
        ...
