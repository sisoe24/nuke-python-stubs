import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class TrackItemBase(Object):
    """
    Base class for objects which can exist on a timeline track which provides some common methods.  Not to be used directly.
    """

    def __repr__(self) -> object:
        """
        Return repr(self).
        """
        return object()

    def __hash__(self, ):
        """
        Return hash(self).
        """
        return None

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

    def __lt__(self, value, ):
        """
        Return self<value.
        """
        return None

    def __le__(self, value, ):
        """
        Return self<=value.
        """
        return None

    def __eq__(self, value, ):
        """
        Return self==value.
        """
        return None

    def __ne__(self, value, ):
        """
        Return self!=value.
        """
        return None

    def __gt__(self, value, ):
        """
        Return self>value.
        """
        return None

    def __ge__(self, value, ):
        """
        Return self>=value.
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

    def clone(self, *args, **kwargs):
        """
        self.clone() -> returns a deep copy of this object.



        WARNING - DEPRECATED ( clone ): This method is deprecated and will not be present in future versions of the Python API.
        This method has been replaced by copy().
        """
        return None

    def copy(self) -> object:
        """
        self.copy() -> returns a deep copy of this object.
        """
        return object()

    def duration(self) -> int:
        """
        self.duration() -> returns the timeline duration value for the item.

        @return: frames
        """
        return int()

    def guid(self) -> object:
        """

        """
        return object()

    def isEnabled(self) -> bool:
        """
        self.isEnabled() -> returns True if the track item is enabled.

        @return: True or False
        """
        return bool()

    def isNull(self) -> bool:
        """
        self.isNull() -> returns True if the track item is invalid.

        @return: True or False
        """
        return bool()

    def linkedItems(self) -> object:
        """
        self.linkedItems() -> returns a tuple of track item objects linked to this one.

        @return: tuple of linked items
        """
        return object()

    def move(self, frames: int) -> None:
        """
        self.move(time) -> moves the item in the sequence. This will keep the duration.

        @param time: frame value. If positive, the item moves right. If negative, the item moves left.
        """
        return None

    def moveTrackItems(self, *args, **kwargs):
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
        return Any

    def parent(self) -> object:
        """
        self.parent() -> returns the AudioTrack or VideoTrack that contains this item.

        @return: hiero.core.AudioTrack or hiero.core.VideoTrack object
        """
        return object()

    def parentSequence(self) -> object:
        """

        """
        return object()

    def parentTrack(self) -> object:
        """

        """
        return object()

    def project(self) -> object:
        """
        self.project() -> returns the Project object that this is attached to, or None if the object is not attached to a project.

        @return: hiero.core.Project object
        """
        return object()

    def sequence(self) -> core.Sequence:
        """
        self.sequence() -> returns the Sequence object that this is attached to, or None if the object is not attached to a project.

        @return: hiero.core.Project object
        """
        return core.Sequence()

    def setEnabled(self, enable: bool) -> None:
        """
        self.setEnabled(enabled) -> enables or disables the track item.

        @return: True or False
        """
        return None

    def setTimelineIn(self, time: int) -> None:
        """
        self.setTimelineIn(inTime) -> sets the timeline in value. Shrinks or grows the timeline duration, as appropriate.

        @param inTime: frame value
        """
        return None

    def setTimelineOut(self, time: int) -> None:
        """
        self.setTimelineOut(outTime) -> sets the timeline out value. Shrinks or grows the timeline duration, as appropriate.

        @param outTime: frame value
        """
        return None

    def timelineIn(self) -> int:
        """
        self.timelineIn() -> returns the timeline in value for the track item.

        @return: frames
        """
        return int()

    def timelineOut(self) -> int:
        """
        self.timelineOut() -> returns the timeline in value for the track item.

        @return: frames
        """
        return int()

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        return str()

    def trimIn(self, t: int) -> None:
        """
        self.trimIn(time) -> trims the left end of the item. This will grow or shrink the duration and the sourceDuration, but keep the playback speed.

        @param time: frame value. If positive, the item duration shrinks. If negative, the item duration grows.
        """
        return None

    def trimOut(self, t: int) -> None:
        """
        self.trimOut(time) -> trims the right end of the item. This will grow or shrink the duration and the sourceDuration, but keep the playback speed.

        @param time: frame value. If positive, the item duration shrinks. If negative, the item duration grows.
        """
        return None

    def __copy__(self,) -> None:
        """

        """
        return None
