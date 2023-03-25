import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class RenderProgressObserver(Object):
    """
    Observer for tracking the progress of renders on the frame server.
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

    def updateProgress(self, progressList: typing.Sequence[typing.Any]) -> None:
        """
        RenderProgressObserver.updateProgress() -> called on progress of frame renders
        @param progressList: list of lists containing [filePath, frame, progress]
        """
        return None

    def __copy__(self,) -> None:
        """

        """
        return None
