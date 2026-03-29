"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import ui
import core
import nuke
import hiero
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class ViewerCursorTool(QObject):
    """
    QObject(self, parent: typing.Optional[PySide2.QtCore.QObject] = None) -> None
    """

    def __new__(self, *args: object, **kwargs: object) -> 'ViewerCursorTool':
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __setattr__(self, name: str, value: object) -> None:
        """
        Implement setattr(self, name, value).
        """
        ...

    def __delattr__(self, name: str) -> None:
        """
        Implement delattr(self, name).
        """
        ...

    def setCursors(self, cursors: typing.List[ui.ViewerCursor]) -> None:
        """

        """
        ...

    cursorLeave = Signal()
    cursorPositionChanged = Signal()
    staticMetaObject: Any = None

    def __init__(self, *args: object, **kwargs: object) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
