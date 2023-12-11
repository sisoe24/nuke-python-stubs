import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class SubTrackItem(TrackItemBase):
    """
    Base class for items that exist in sub-tracks, e.g. Annotation objects. This class should never be used directly.
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

    def descString(self) -> str:
        """

        """
        ...

    def setTimelineIn(self, time: int) -> None:
        """
        self.setTimelineIn(inTime) -> sets the in point for this SubTrackItem. Note that this trims the duration of the SubTrackItem.

        @param inTime: frame for the new in point
        """
        ...

    def setTimelineOut(self, time: int) -> None:
        """
        self.setTimelineOut(outTime) -> sets the out point for this SubTrackItem. Note that this trims the duration of the SubTrackItem.

        @param outTime: frame for the new out point
        """
        ...

    def subTrackIndex(self) -> int:
        """
        self.subTrackIndex() -> get the index of the item's parent sub-track.

        @return: int index, -1 if the item has not been added to a track
        """
        ...

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...
