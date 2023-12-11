import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class ViewerCursorTool(QObject):
    """
    QObject(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __setattr__(self, name, value, ) -> None:
        """
        Implement setattr(self, name, value).
        """
        ...

    def __delattr__(self, name, ) -> None:
        """
        Implement delattr(self, name).
        """
        ...

    def setCursors(self, cursors: typing.List[ui.ViewerCursor]) -> None:
        """

        """
        ...

    cursorPositionChanged = Signal()
    cursorLeave = Signal()
    staticMetaObject: Any = None

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
