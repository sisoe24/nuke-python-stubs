import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class ViewerTool(QObject):
    """
    Python interface for the viewer tools
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

    def isActive(self) -> bool:
        """
        self.isActive() -> get the tool's active state
        """
        return bool()

    def setActive(self, active: bool) -> None:
        """
        self.setActive(active) -> set the tool's active state
        """
        return None

    activeChanged = Signal()
    staticMetaObject: Any = None

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None
