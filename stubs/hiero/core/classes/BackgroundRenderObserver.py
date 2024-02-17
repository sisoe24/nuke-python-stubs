"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import ui
import core
import hiero
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class BackgroundRenderObserver:
    """
    Observer of background renders.
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def __bool__(self, ) -> None:
        """
        True if self else False
        """
        ...

    def isNull(self) -> bool:
        """

        """
        ...

    def onFrameRenderCancelled(self, path: str, frame: int, nodeName: str) -> None:
        """

        """
        ...

    def onFrameRenderError(self, path: str, frame: int, nodeName: str, error: str) -> None:
        """

        """
        ...

    def onFrameRenderInProgress(self, path: str, frame: int, nodeName: str) -> None:
        """

        """
        ...

    def onFrameRenderQueued(self, path: str, frame: int, nodeName: str) -> None:
        """

        """
        ...

    def onFrameRendered(self, path: str, frame: int, nodeName: str) -> None:
        """

        """
        ...

    def onRenderQueued(self, path: str, frameRanges: str, nodeName: str, views: str) -> None:
        """

        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...
