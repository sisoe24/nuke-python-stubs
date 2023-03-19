import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class FormatChooser(QComboBox):
    """
    QComboBox(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None) -> None
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

    def currentFormat(self) -> object:
        """

        """
        return object()

    def setCurrentFormat(self, arg__1: core.Format) -> None:
        """

        """
        return None

    def setProject(self, arg__1: core.Project) -> None:
        """

        """
        return None

    formatChanged = Signal()
    staticMetaObject: Any = None
