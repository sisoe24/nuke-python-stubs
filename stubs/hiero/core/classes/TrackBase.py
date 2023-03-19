import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class TrackBase(Object):
    """
    Base class for VideoTrack and AudioTrack objects. This class should never be used directly.

    Flags for controlling behavior when removing items, these can be combined with bitwise or:
     TrackBase.eRemoveLinkedItems: removing an item will also remove any items it is linked to
     TrackBase.eDontRemoveLinkedItems: removing an item will not remove linked items
     TrackBase.eDontCollapseSubTracks: removing a sub-track item will not cause empty sub-tracks to be removed
    """

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

    def addItem(self, trackItem: core.TrackItem) -> core.TrackItem:
        """
        self.addItem(item) -> deprecated; use addTrackItem instead. Adds a track item to this track. Throws an exception if the item overlaps any existing items on the track.

        @param item: the hiero.core.TrackItem to add to this track
        @return: hiero.core.TrackItem object
        """
        return core.TrackItem()

    def addTag(self, tag: core.Tag) -> core.Tag:
        """
        self.addTag(tag) -> adds the specified tag to the Track.

        @param tag: Tag object to apply to the track
        @return: a hiero.core.Tag object
        """
        return core.Tag()

    def addTransition(self, transition: core.Transition) -> core.Transition:
        """
        self.addTransition(transition) -> adds a transition to the timeline for the track.  Can only be called when the track has been added to a Sequence.

        Note that a transition can only be added to a single track. Calling this function with a Transition object which already belongs to a Track will result in an error.
        Transition items can be reomoved from a track using the removeTransition function.

        @param transition: the hiero.core.Transition to add to this track
        @return: a hiero.core.Transition object
        """
        return core.Transition()

    def clearRange(self, start: int, end: int, ripple: bool) -> None:
        """
        self.clearRange(start, end, ripple) -> Clears a time range out of the track; effectively a razor on any clips straddling the start and end, and a delete of everything else.

        @param start: the start of the range to clear
        @param end: the end of the range to clear
        @param ripple: set to True to shift the remaining track items to the left
        """
        return None

    def guid(self) -> object:
        """

        """
        return object()

    def isEnabled(self) -> bool:
        """
        self.isEnabled() -> returns True if the Track object is enabled.

        @return: True or False
        """
        return bool()

    def isLocked(self) -> bool:
        """
        self.isLocked() -> returns True if the Track object is locked.

        @return: True or False
        """
        return bool()

    def isNull(self) -> bool:
        """
        self.isNull() -> returns True if the Track object is invalid.

        @return: True or False
        """
        return bool()

    def metadata(self) -> core.DataCollection:
        """
        self.metadata() -> returns the metadata for this Track.

        @return: hiero.core.DataCollection object
        """
        return core.DataCollection()

    def name(self) -> str:
        """
        self.name() -> returns the name of the track. Identical to calling trackName().

        @return: string
        """
        return str()

    def numItems(self) -> int:
        """
        self.numItems() -> returns the number of items in this track.

        @return: int
        """
        return int()

    def numTransitions(self) -> int:
        """
        self.numTransitions() -> returns the number of transitions in this track.

        @return: int
        """
        return int()

    def project(self) -> object:
        """
        self.project() -> returns the Project object that this item is attached to or None if the object is not attached to a project.

        @return: hiero.core.Project object
        """
        return object()

    def razorAt(self, *args, **kwargs):
        """
        self.razorAt(time) -> Creates razor cuts on a track for the parameter time(s).

        @param time: if a single (integer) value, indicates the razor cut time; if a tuple or list of integer values, then the times to create multiple cuts at
        """
        return Number()

    def removeItem(self, trackItem: core.TrackItem, option: int = 'eRemoveLinkedItems') -> None:
        """
        self.removeItem(trackItem, option=eRemoveLinkedItems) -> removes a track item from this track.

        @param trackItem: the hiero.core.TrackItem to remove from this track
        @param option: options controlling the remove behavior. By default linked items are also removed. Note that if linked effects are not removed, this will put them in an invalid state.
        """
        return None

    def removeTag(self, tag: core.Tag) -> None:
        """
        self.removeTag(tag) -> removes the tag from the track.

        @param tag: tag object
        """
        return None

    def removeTransition(self, transition: core.Transition) -> None:
        """
        self.removeTransition(transition) -> removes a transition from the timeline of this track.

        @param transition: the hiero.core.Transition to remove from this track's timeline
        """
        return None

    def setEnabled(self, enabled: bool) -> None:
        """
        self.setEnabled() -> enables or disables the Track.
        """
        return None

    def setLocked(self, locked: bool) -> None:
        """
        self.setLocked() -> locks or unlocks the Track.

        @return: True or False
        """
        return None

    def setName(self, name: str) -> None:
        """
        self.setName() -> Sets the name of a track.

        @param: string
        """
        return None

    def tags(self) -> object:
        """
        self.tags() -> returns a tuple of all of the tags applied to this object.

        @return: tuple of hiero.core.Tag objects
        """
        return object()

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        return str()

    def trackIndex(self) -> int:
        """

        """
        return int()

    def trackName(self) -> str:
        """
        self.trackName() -> returns the name of the track. Identical to calling name().

        @return: string
        """
        return str()

    def transitions(self) -> object:
        """
        self.transitions() -> returns a tuple of all of the transitions applied to this track object.

        @return: tuple of hiero.core.Transition objects
        """
        return object()

    def __copy__(self,) -> None:
        """

        """
        return None

    RemoveItemOptions: Any = None
    eRemoveLinkedItems: Any = None
    eDontRemoveLinkedItems: Any = None
    eDontCollapseSubTracks: Any = None
