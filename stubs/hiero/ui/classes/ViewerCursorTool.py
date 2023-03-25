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

    def __setattr__(self, name, value, ):
        """
        Implement setattr(self, name, value).
        """
        return None

    def __delattr__(self, name, ):
        """
        Implement delattr(self, name).
        """
        return None

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def setCursors(self, cursors: typing.List[ui.ViewerCursor]) -> None:
        """

        """
        return None

    cursorLeave = Signal()
    cursorPositionChanged = Signal()
    staticMetaObject: Any = None

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None
