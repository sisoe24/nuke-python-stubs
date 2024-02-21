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


class FormatChooser(QComboBox):
    """
    QComboBox(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
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

    def currentFormat(self) -> object:
        """

        """
        ...

    def setCurrentFormat(self, arg__1: core.Format) -> None:
        """

        """
        ...

    def setProject(self, arg__1: core.Project) -> None:
        """

        """
        ...

    formatChanged = Signal()
    staticMetaObject: Any = None
