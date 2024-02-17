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


class TrackBase:
    """
    Base class for VideoTrack and AudioTrack objects. This class should never be used directly.

    Flags for controlling behavior when removing items, these can be combined with bitwise or:
     TrackBase.eRemoveLinkedItems: removing an item will also remove any items it is linked to
     TrackBase.eDontRemoveLinkedItems: removing an item will not remove linked items
     TrackBase.eDontCollapseSubTracks: removing a sub-track item will not cause empty sub-tracks to be removed
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

    def addItem(self, trackItem: core.TrackItem) -> core.TrackItem:
        """
        self.addItem(item) -> deprecated; use addTrackItem instead. Adds a track item to this track. Throws an exception if the item overlaps any existing items on the track.

        @param item: the hiero.core.TrackItem to add to this track
        @return: hiero.core.TrackItem object
        """
        ...

    def addTag(self, tag: core.Tag) -> core.Tag:
        """
        self.addTag(tag) -> adds the specified tag to the Track.

        @param tag: Tag object to apply to the track
        @return: a hiero.core.Tag object
        """
        ...

    def addTransition(self, transition: core.Transition) -> core.Transition:
        """
        self.addTransition(transition) -> adds a transition to the timeline for the track.  Can only be called when the track has been added to a Sequence.

        Note that a transition can only be added to a single track. Calling this function with a Transition object which already belongs to a Track will result in an error.
        Transition items can be reomoved from a track using the removeTransition function.

        @param transition: the hiero.core.Transition to add to this track
        @return: a hiero.core.Transition object
        """
        ...

    def clearRange(self, start: int, end: int, ripple: bool) -> None:
        """
        self.clearRange(start, end, ripple) -> Clears a time range out of the track; effectively a razor on any clips straddling the start and end, and a delete of everything else.

        @param start: the start of the range to clear
        @param end: the end of the range to clear
        @param ripple: set to True to shift the remaining track items to the left
        """
        ...

    def guid(self) -> object:
        """

        """
        ...

    def isEnabled(self) -> bool:
        """
        self.isEnabled() -> returns True if the Track object is enabled.

        @return: True or False
        """
        ...

    def isLocked(self) -> bool:
        """
        self.isLocked() -> returns True if the Track object is locked.

        @return: True or False
        """
        ...

    def isNull(self) -> bool:
        """
        self.isNull() -> returns True if the Track object is invalid.

        @return: True or False
        """
        ...

    def metadata(self) -> core.DataCollection:
        """
        self.metadata() -> returns the metadata for this Track.

        @return: hiero.core.DataCollection object
        """
        ...

    def name(self) -> str:
        """
        self.name() -> returns the name of the track. Identical to calling trackName().

        @return: string
        """
        ...

    def numItems(self) -> int:
        """
        self.numItems() -> returns the number of items in this track.

        @return: int
        """
        ...

    def numTransitions(self) -> int:
        """
        self.numTransitions() -> returns the number of transitions in this track.

        @return: int
        """
        ...

    def project(self) -> object:
        """
        self.project() -> returns the Project object that this item is attached to or None if the object is not attached to a project.

        @return: hiero.core.Project object
        """
        ...

    def razorAt(self, *args: typing.Any, **kwargs: typing.Any) -> int | float:
        """
        self.razorAt(time) -> Creates razor cuts on a track for the parameter time(s).

        @param time: if a single (integer) value, indicates the razor cut time; if a tuple or list of integer values, then the times to create multiple cuts at
        """
        ...

    def removeItem(self, trackItem: core.TrackItem, option: int = 'eRemoveLinkedItems') -> None:
        """
        self.removeItem(trackItem, option=eRemoveLinkedItems) -> removes a track item from this track.

        @param trackItem: the hiero.core.TrackItem to remove from this track
        @param option: options controlling the remove behavior. By default linked items are also removed. Note that if linked effects are not removed, this will put them in an invalid state.
        """
        ...

    def removeTag(self, tag: core.Tag) -> None:
        """
        self.removeTag(tag) -> removes the tag from the track.

        @param tag: tag object
        """
        ...

    def removeTransition(self, transition: core.Transition) -> None:
        """
        self.removeTransition(transition) -> removes a transition from the timeline of this track.

        @param transition: the hiero.core.Transition to remove from this track's timeline
        """
        ...

    def setEnabled(self, enabled: bool) -> None:
        """
        self.setEnabled() -> enables or disables the Track.
        """
        ...

    def setLocked(self, locked: bool) -> None:
        """
        self.setLocked() -> locks or unlocks the Track.

        @return: True or False
        """
        ...

    def setName(self, name: str) -> None:
        """
        self.setName() -> Sets the name of a track.

        @param: string
        """
        ...

    def tags(self) -> object:
        """
        self.tags() -> returns a tuple of all of the tags applied to this object.

        @return: tuple of hiero.core.Tag objects
        """
        ...

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        ...

    def trackIndex(self) -> int:
        """

        """
        ...

    def trackName(self) -> str:
        """
        self.trackName() -> returns the name of the track. Identical to calling name().

        @return: string
        """
        ...

    def transitions(self) -> object:
        """
        self.transitions() -> returns a tuple of all of the transitions applied to this track object.

        @return: tuple of hiero.core.Transition objects
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...

    RemoveItemOptions: Any = None
    eRemoveLinkedItems: Any = None
    eDontRemoveLinkedItems: Any = None
    eDontCollapseSubTracks: Any = None
