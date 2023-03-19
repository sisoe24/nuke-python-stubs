import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class ColorButton(QPushButton):
    """
    QPushButton(self, icon: PySide2.QtGui.QIcon, text: str, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QPushButton(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
    QPushButton(self, text: str, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
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

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def canBeInvalid(self) -> bool:
        """

        """
        return bool()

    def color(self) -> PySide2.QtGui.QColor:
        """

        """
        return Any

    def dragEnterEvent(self, event: PySide2.QtGui.QDragEnterEvent) -> None:
        """
        dragEnterEvent(self, event: PySide2.QtGui.QDragEnterEvent) -> None
        """
        return None

    def dropEvent(self, event: PySide2.QtGui.QDropEvent) -> None:
        """
        dropEvent(self, event: PySide2.QtGui.QDropEvent) -> None
        """
        return None

    def mouseMoveEvent(self, event: PySide2.QtGui.QMouseEvent) -> None:
        """
        mouseMoveEvent(self, e: PySide2.QtGui.QMouseEvent) -> None
        """
        return None

    def mousePressEvent(self, event: PySide2.QtGui.QMouseEvent) -> None:
        """
        mousePressEvent(self, e: PySide2.QtGui.QMouseEvent) -> None
        """
        return None

    def paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None:
        """
        paintEvent(self, arg__1: PySide2.QtGui.QPaintEvent) -> None
        """
        return None

    def setCanBeInvalid(self, v: bool) -> None:
        """

        """
        return None

    def setColor(self, color: PySide2.QtGui.QColor) -> None:
        """

        """
        return None

    def setValidColor(self, validColor: bool) -> None:
        """

        """
        return None

    def sizeHint(self) -> PySide2.QtCore.QSize:
        """
        sizeHint(self) -> PySide2.QtCore.QSize
        """
        return Any

    def validColor(self) -> bool:
        """

        """
        return bool()

    colorChanged = Signal()
    staticMetaObject: Any = None
