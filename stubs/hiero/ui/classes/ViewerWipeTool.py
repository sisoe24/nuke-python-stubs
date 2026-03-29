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


class ViewerWipeTool(ViewerTool):
    """
    Python interface for the viewer tools
    """

    def __new__(cls, *args, **kwargs) -> 'ViewerWipeTool':
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

    def setWipeToolState(self, wipeToolState: hiero.ui.WipeToolState) -> None:
        """

        """
        ...

    def wipeToolState(self) -> hiero.ui.WipeToolState:
        """

        """
        ...

    wipeToolStateChanged = Signal()
    staticMetaObject: Any = None

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
