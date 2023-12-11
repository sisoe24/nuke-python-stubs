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

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def canBeInvalid(self) -> bool:
        """

        """
        ...

    def color(self) -> PySide2.QtGui.QColor:
        """

        """
        ...

    def dragEnterEvent(self, event: PySide2.QtGui.QDragEnterEvent) -> None:
        """
        dragEnterEvent(self, event: PySide2.QtGui.QDragEnterEvent) -> None
        """
        ...

    def dropEvent(self, event: PySide2.QtGui.QDropEvent) -> None:
        """
        dropEvent(self, event: PySide2.QtGui.QDropEvent) -> None
        """
        ...

    def mouseMoveEvent(self, event: PySide2.QtGui.QMouseEvent) -> None:
        """
        mouseMoveEvent(self, e: PySide2.QtGui.QMouseEvent) -> None
        """
        ...

    def mousePressEvent(self, event: PySide2.QtGui.QMouseEvent) -> None:
        """
        mousePressEvent(self, e: PySide2.QtGui.QMouseEvent) -> None
        """
        ...

    def paintEvent(self, event: PySide2.QtGui.QPaintEvent) -> None:
        """
        paintEvent(self, arg__1: PySide2.QtGui.QPaintEvent) -> None
        """
        ...

    def setCanBeInvalid(self, v: bool) -> None:
        """

        """
        ...

    def setColor(self, color: PySide2.QtGui.QColor) -> None:
        """

        """
        ...

    def setValidColor(self, validColor: bool) -> None:
        """

        """
        ...

    def sizeHint(self) -> PySide2.QtCore.QSize:
        """
        sizeHint(self) -> PySide2.QtCore.QSize
        """
        ...

    def validColor(self) -> bool:
        """

        """
        ...

    colorChanged = Signal()
    staticMetaObject: Any = None
