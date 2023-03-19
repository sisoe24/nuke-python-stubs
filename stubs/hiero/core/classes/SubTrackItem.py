import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class SubTrackItem(TrackItemBase):
    """
    Base class for items that exist in sub-tracks, e.g. Annotation objects. This class should never be used directly.
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

    def descString(self) -> str:
        """

        """
        return str()

    def setTimelineIn(self, time: int) -> None:
        """
        self.setTimelineIn(inTime) -> sets the in point for this SubTrackItem. Note that this trims the duration of the SubTrackItem.

        @param inTime: frame for the new in point
        """
        return None

    def setTimelineOut(self, time: int) -> None:
        """
        self.setTimelineOut(outTime) -> sets the out point for this SubTrackItem. Note that this trims the duration of the SubTrackItem.

        @param outTime: frame for the new out point
        """
        return None

    def subTrackIndex(self) -> int:
        """
        self.subTrackIndex() -> get the index of the item's parent sub-track.

        @return: int index, -1 if the item has not been added to a track
        """
        return int()

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        return str()

    def __copy__(self,) -> None:
        """

        """
        return None
