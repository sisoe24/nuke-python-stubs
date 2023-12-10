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
        self != 0
        """
        ...

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
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