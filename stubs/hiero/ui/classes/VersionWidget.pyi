import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *

class VersionWidget(QSpinBox):
    """
    Widget for editing version indices and padding. This extends QSpinbox to
    allow the user to add leading zeroes to specify padding.
    """
    paddingChanged = Signal()
    def __init__(self) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def setPadding(self, padding) -> None:
        """

        """
        ...

    def padding(self) -> None:
        """

        """
        ...

    def sizeHint(self) -> None:
        """
        sizeHint(self) -> PySide2.QtCore.QSize
        """
        ...

    def textFromValue(self, value) -> None:
        """
        textFromValue(self, val: int) -> str
        """
        ...

    def valueFromText(self, text) -> None:
        """
        valueFromText(self, text: str) -> int
        """
        ...

    staticMetaObject: Any = None
