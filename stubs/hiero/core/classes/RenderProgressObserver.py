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


class RenderProgressObserver:
    """
    Observer for tracking the progress of renders on the frame server.
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

    def __bool__(self, ) -> None:
        """
        True if self else False
        """
        ...

    def isNull(self) -> bool:
        """

        """
        ...

    def updateProgress(self, progressList: typing.Sequence[typing.Any]) -> None:
        """
        RenderProgressObserver.updateProgress() -> called on progress of frame renders
        @param progressList: list of lists containing [filePath, frame, progress]
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...
