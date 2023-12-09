from typing import *
from numbers import Number

import nuke

from . import *


class FrameRanges(object):
    """
    A sequence of FrameRange objects with convenience functions for iterating over all frames in all ranges.
    """

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

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def size(self,) -> int:
        """
        size() -> int

        return the ranges number.
        """
        ...

    def add(self, r) -> None:
        """
        add(r) -> None

        add a new frame range.
        """
        ...

    def minFrame(self,) -> int:
        """
        minFrame() -> int

        get minimun frame of all ranges.
        """
        ...

    def maxFrame(self,) -> int:
        """
        maxFrame() -> int

        get maximun frame of all ranges.
        """
        ...

    def clear(self,) -> None:
        """
        clear() -> None

        reset all store frame ranges.
        """
        ...

    def compact(self,) -> None:
        """
        compact() -> None

        compact all the frame ranges.
        """
        ...

    def toFrameList(self,) -> [int]:
        """
        toFrameList() -> [int]

        return a list of frames in a vector
        """
        ...

    def getRange(self,) -> FrameRange:
        """
        getRange()-> FrameRange

        return a range from the list
        """
        ...
