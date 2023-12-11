import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class Transition(TrackItemBase):
    """
    Object representing a transition between two clips.
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

    def alignment(self) -> core.Transition.Alignments:
        """
        self.alignment() -> returns the alignment mode of this transition. Either kFadeIn, kDissolve, kFadeOut or kUnknown.

        @return: alignment type (hiero.core.Transition.Alignments)
        """
        ...

    def createAudioCrossfadeTransition(self, item1: core.TrackItem, item2: core.TrackItem, duration1: int, duration2: int) -> core.Transition:
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

    def createAudioFadeInTransition(self, item: core.TrackItem, duration: int) -> core.Transition:
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

    def createAudioFadeOutTransition(self, item: core.TrackItem, duration: int) -> core.Transition:
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

    def createDissolveTransition(self, item1: core.TrackItem, item2: core.TrackItem, duration1: int, duration2: int) -> core.Transition:
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

    def createFadeInTransition(self, item: core.TrackItem, duration: int) -> core.Transition:
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

    def createFadeOutTransition(self, item: core.TrackItem, duration: int) -> core.Transition:
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

    def dissolveNode(self) -> object:
        """
        self.dissolveNode() -> Returns the Dissolve node which controls the transition curve.

        @return: nuke.Node
        """
        ...

    def guid(self) -> object:
        """

        """
        ...

    def inTrackItem(self) -> core.TrackItem:
        """
        self.inTrackItem() -> Get the in track item for this transition.

        return: hiero.core.TrackItem
        """
        ...

    def outTrackItem(self) -> core.TrackItem:
        """
        self.outTrackItem() -> Get the out track item for this transition.

        return: hiero.core.TrackItem
        """
        ...

    def parent(self) -> object:
        """
        self.parent() -> returns the AudioTrack or VideoTrack that contains this transition.

        @return: hiero.core.AudioTrack or hiero.core.VideoTrack object
        """
        ...

    def project(self) -> object:
        """
        self.project() -> returns the Project object that this is attached to, or None if the object is not attached to a project.

        @return: hiero.core.Project object
        """
        ...

    def setAlignment(self, alignment: core.Transition.Alignments) -> None:
        """
        self.setAlignment(alignment) -> sets the alignment mode on this transition.

        @param alignment: alignment type (hiero.core.Transition.Alignments), either kFadeIn, kDissolve, or kFadeOut
        """
        ...

    def setTimelineIn(self, arg__1: int) -> None:
        """
        self.setTimelineIn(inTime) -> sets the in point for this transition. Note that this trims the duration of the transition.

        @param inTime: frame for the new in point
        """
        ...

    def setTimelineOut(self, arg__1: int) -> None:
        """
        self.setTimelineOut(outTime) -> sets the out point for this transition. Note that this trims the duration of the transition.

        @param outTime: frame for the new out point
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

    Alignments: Any = None
    kFadeIn: Any = None
    kDissolve: Any = None
    kFadeOut: Any = None
    kUnknown: Any = None
