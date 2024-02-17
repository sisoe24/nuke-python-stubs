"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class FrameRange(object):
    """
    A frame range, with an upper and lower bound and an increment.
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def __str__(self, ) -> None:
        """
        Return str(self).
        """
        ...

    def __iter__(self, ) -> None:
        """
        Implement iter(self).
        """
        ...

    def __next__(self, ) -> None:
        """
        Implement next(self).
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def first(self,) -> int:
        """
        self.first() -> int

        return the first frame of the range.
        """
        ...

    def last(self,) -> int:
        """
        self.last() -> int

        return the last frame of the range.
        """
        ...

    def increment(self,) -> int:
        """
        self.increment() -> int

        return the increment between two frames.
        """
        ...

    def setFirst(self, n) -> None:
        """
        self.setFirst(n) -> None

        set the first frame of the range.
        """
        ...

    def setLast(self, n) -> None:
        """
        self.setLast(n) -> None

        set the last frame of the range.
        """
        ...

    def setIncrement(self, n) -> None:
        """
        self.setIncrement(n) -> None

        set the increment between two frames.
        """
        ...

    def frames(self,) -> int:
        """
        self.frames() -> int

        return the numbers of frames defined in the range.
        """
        ...

    def getFrame(self, n) -> int:
        """
        self.getFrame(n) -> int

        return the frame according to the index, parameter n must be between 0 and frames().
        """
        ...

    def isInRange(self, n) -> int:
        """
        self.isInRange(n) -> int

        return if the frame is inside the range.
        """
        ...

    def minFrame(self,) -> int:
        """
        self.minFrame() -> int

        return the minimun frame define in the range.
        """
        ...

    def maxFrame(self,) -> int:
        """
        self.maxFrame() -> int

        return the maximun frame define in the range.
        """
        ...

    def stepFrame(self,) -> int:
        """
        self.stepFrame() -> int

        return the absolute increment between two frames.
        """
        ...
