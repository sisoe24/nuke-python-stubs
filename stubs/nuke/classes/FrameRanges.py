"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class FrameRanges(object):
    """
    A sequence of FrameRange objects with convenience functions for iterating over all frames in all ranges.
    """

    def __new__(cls, *args, **kwargs) -> FrameRanges:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __hash__(self) -> int:
        """
        Return hash(self).
        """
        ...

    def __str__(self) -> str:
        """
        Return str(self).
        """
        ...

    def __iter__(self) -> Iterator[int]:
        """
        Implement iter(self).
        """
        ...

    def __next__(self) -> int:
        """
        Implement next(self).
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def size(self) -> int:
        """
        size() -> int

        return the ranges number.
        """
        ...

    def add(self, r: FrameRange) -> None:
        """
        add(r) -> None

        add a new frame range.
        """
        ...

    def minFrame(self) -> int:
        """
        minFrame() -> int

        get minimun frame of all ranges.
        """
        ...

    def maxFrame(self) -> int:
        """
        maxFrame() -> int

        get maximun frame of all ranges.
        """
        ...

    def clear(self) -> None:
        """
        clear() -> None

        reset all store frame ranges.
        """
        ...

    def compact(self) -> None:
        """
        compact() -> None

        compact all the frame ranges.
        """
        ...

    def toFrameList(self) -> List[int]:
        """
        toFrameList() -> [int]

        return a list of frames in a vector
        """
        ...

    def getRange(self) -> FrameRange:
        """
        getRange()-> FrameRange

        return a range from the list
        """
        ...
