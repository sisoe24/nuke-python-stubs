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


class TrackItemBase:
    """
    Base class for objects which can exist on a timeline track which provides some common methods.  Not to be used directly.
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __repr__(self) -> object:
        """
        Return repr(self).
        """
        ...

    def __hash__(self, ) -> None:
        """
        Return hash(self).
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

    def __lt__(self, value, ) -> None:
        """
        Return self<value.
        """
        ...

    def __le__(self, value, ) -> None:
        """
        Return self<=value.
        """
        ...

    def __eq__(self, value, ) -> None:
        """
        Return self==value.
        """
        ...

    def __ne__(self, value, ) -> None:
        """
        Return self!=value.
        """
        ...

    def __gt__(self, value, ) -> None:
        """
        Return self>value.
        """
        ...

    def __ge__(self, value, ) -> None:
        """
        Return self>=value.
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

    def clone(self, *args, **kwargs) -> None:
        """
        self.clone() -> returns a deep copy of this object.



        WARNING - DEPRECATED ( clone ): This method is deprecated and will not be present in future versions of the Python API.
        This method has been replaced by copy().
        """
        ...

    def copy(self) -> object:
        """
        self.copy() -> returns a deep copy of this object.
        """
        ...

    def duration(self) -> int:
        """
        self.duration() -> returns the timeline duration value for the item.

        @return: frames
        """
        ...

    def guid(self) -> object:
        """

        """
        ...

    def isEnabled(self) -> bool:
        """
        self.isEnabled() -> returns True if the track item is enabled.

        @return: True or False
        """
        ...

    def isNull(self) -> bool:
        """
        self.isNull() -> returns True if the track item is invalid.

        @return: True or False
        """
        ...

    def linkedItems(self) -> object:
        """
        self.linkedItems() -> returns a tuple of track item objects linked to this one.

        @return: tuple of linked items
        """
        ...

    def move(self, frames: int) -> None:
        """
        self.move(time) -> moves the item in the sequence. This will keep the duration.

        @param time: frame value. If positive, the item moves right. If negative, the item moves left.
        """
        ...

    def moveTrackItems(self, trackItems: typing.List[core.TrackItemBase], frames: int) -> None:
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, ...):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
        ...

    def parent(self) -> object:
        """
        self.parent() -> returns the AudioTrack or VideoTrack that contains this item.

        @return: hiero.core.AudioTrack or hiero.core.VideoTrack object
        """
        ...

    def parentSequence(self) -> object:
        """

        """
        ...

    def parentTrack(self) -> object:
        """

        """
        ...

    def project(self) -> hiero.core.Project:
        """
        self.project() -> returns the Project object that this is attached to, or None if the object is not attached to a project.

        @return: hiero.core.Project object
        """
        ...

    def sequence(self) -> core.Sequence:
        """
        self.sequence() -> returns the Sequence object that this is attached to, or None if the object is not attached to a project.

        @return: hiero.core.Project object
        """
        ...

    def setEnabled(self, enable: bool) -> None:
        """
        self.setEnabled(enabled) -> enables or disables the track item.

        @return: True or False
        """
        ...

    def setTimelineIn(self, time: int) -> None:
        """
        self.setTimelineIn(inTime) -> sets the timeline in value. Shrinks or grows the timeline duration, as appropriate.

        @param inTime: frame value
        """
        ...

    def setTimelineOut(self, time: int) -> None:
        """
        self.setTimelineOut(outTime) -> sets the timeline out value. Shrinks or grows the timeline duration, as appropriate.

        @param outTime: frame value
        """
        ...

    def timelineIn(self) -> int:
        """
        self.timelineIn() -> returns the timeline in value for the track item.

        @return: frames
        """
        ...

    def timelineOut(self) -> int:
        """
        self.timelineOut() -> returns the timeline in value for the track item.

        @return: frames
        """
        ...

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        ...

    def trimIn(self, t: int) -> None:
        """
        self.trimIn(time) -> trims the left end of the item. This will grow or shrink the duration and the sourceDuration, but keep the playback speed.

        @param time: frame value. If positive, the item duration shrinks. If negative, the item duration grows.
        """
        ...

    def trimOut(self, t: int) -> None:
        """
        self.trimOut(time) -> trims the right end of the item. This will grow or shrink the duration and the sourceDuration, but keep the playback speed.

        @param time: frame value. If positive, the item duration shrinks. If negative, the item duration grows.
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...
