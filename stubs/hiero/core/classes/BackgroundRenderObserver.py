import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class BackgroundRenderObserver(Object):
    """
    Observer of background renders.
    """

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def __bool__(self, ):
        """
        self != 0
        """
        return None

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def isNull(self) -> bool:
        """

        """
        return bool()

    def onFrameRenderCancelled(self, path: str, frame: int, nodeName: str) -> None:
        """

        """
        return None

    def onFrameRenderError(self, path: str, frame: int, nodeName: str, error: str) -> None:
        """

        """
        return None

    def onFrameRenderInProgress(self, path: str, frame: int, nodeName: str) -> None:
        """

        """
        return None

    def onFrameRenderQueued(self, path: str, frame: int, nodeName: str) -> None:
        """

        """
        return None

    def onFrameRendered(self, path: str, frame: int, nodeName: str) -> None:
        """

        """
        return None

    def onRenderQueued(self, path: str, frameRanges: str, nodeName: str, views: str) -> None:
        """

        """
        return None

    def __copy__(self,) -> None:
        """

        """
        return None
