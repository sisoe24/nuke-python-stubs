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

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def setPadding(self, padding):
        """

        """
        return None

    def padding(self):
        """

        """
        return None

    def sizeHint(self):
        """
        sizeHint(self) -> PySide2.QtCore.QSize
        """
        return None

    def textFromValue(self, value):
        """
        textFromValue(self, val: int) -> str
        """
        return None

    def valueFromText(self, text):
        """
        valueFromText(self, text: str) -> int
        """
        return None

    staticMetaObject: Any = None
