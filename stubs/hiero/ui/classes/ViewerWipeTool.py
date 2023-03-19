import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class ViewerWipeTool(ViewerTool):
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

    def setWipeToolState(self, wipeToolState: ui.WipeToolState) -> None:
        """

        """
        return None

    def wipeToolState(self) -> ui.WipeToolState:
        """

        """
        return ui.WipeToolState()

    wipeToolStateChanged = Signal()
    staticMetaObject: Any = None

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None
