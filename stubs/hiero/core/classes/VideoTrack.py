import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class VideoTrack(TrackBase):
    """
    Object for manipulating video tracks.
    """

    def __repr__(self) -> object:
        """
        Return repr(self).
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

    def __len__(self, ):
        """
        Return len(self).
        """
        return None

    def __getitem__(self, key, ):
        """
        Return self[key].
        """
        return None

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def addSubTrackItem(self, subTrackItem: core.SubTrackItem, subTrackIndex: int) -> core.SubTrackItem:
        """
        self.addSubTrackItem(subTrackItem, subTrackIndex) -> Add a subtrack item to the track on the given sub-track index.
        This method will cut or delete sub-track items that overlap with the one being added.

        @param subTrackItem: a hiero.core.SubTrackItem object to add.
        @param subTrackIndex: the index of the sub-track to add to.
        @return: the added item
        """
        return core.SubTrackItem()

    def addTag(self, tag: core.Tag) -> core.Tag:
        """
        self.addTag(tag) -> adds a tag to the video track item.

        @param tag: the hiero.core.Tag to add to the video track.
        """
        return core.Tag()

    def addTrackItem(self, *args, **kwargs):
        """
        self.addTrackItem(clip, position) -> if the first parameter is a Clip object, the second parameter must be specified and this method creates a new track item and adds it to this video track at the given position.
        If the first parameter is a TrackItem, then this method just adds the track item specified.
        This method will cut or delete track items that overlap with the one being added.
        This method can only be called if the track has already been added to a Sequence.

        @param clip: a hiero.core.Clip object or a hiero.core.TrackItem object, to add to this video track.
        @param position: int; insert position. Do not specify if clip is a TrackItem.
        @return: hiero.core.TrackItem object
        """
        return TrackItem()

    def blendMode(self) -> str:
        """
        self.blendMode() -> returns a string representing the blend-mode as it appears in the Nuke Merge Node, if the VideoTrack object has blending enabled.

        @return: String containing the blend-mode
        """
        return str()

    def clone(self, *args, **kwargs):
        """
        self.clone() -> returns a deep copy of this object.

        @return: hiero.core.VideoTrack object

        WARNING - DEPRECATED ( clone ): This method is deprecated and will not be present in future versions of the Python API.
        This method has been replaced by copy().
        """
        return VideoTrack()

    def copy(self) -> object:
        """
        self.copy() -> returns a deep copy of this object.

        @return: hiero.core.VideoTrack object
        """
        return VideoTrack()

    def createTrackItem(self, name: str) -> core.TrackItem:
        """
        self.createTrackItem(name) -> creates a new track item.

        @param name: the name of the new track item
        @return: hiero.core.TrackItem object
        """
        return TrackItem()

    def isBlendEnabled(self) -> bool:
        """
        self.isEnabled() -> returns True if the VideoTrack object has blending enabled.

        @return: True or False
        """
        return Union[True, False]

    def isBlendMaskEnabled(self) -> bool:
        """
        self.isBlendMaskEnabled() -> returns True if the VideoTrack object has blend-masking enabled.

        @return: True or False
        """
        return Union[True, False]

    def items(self) -> object:
        """
        self.items() -> returns a tuple with all of the track items contained by this track.

        @return: tuple of hiero.core.TrackItem objects
        """
        return tuple()

    def parent(self) -> object:
        """
        self.parent() -> returns the sequence that contains this track.

        @return: hiero.core.Sequence object
        """
        return Iterable()

    def removeSubTrackItem(self, subTrackItem: core.SubTrackItem, option: int = 'eRemoveLinkedItems') -> None:
        """
        self.removeSubTrackItem(subTrackItem, option=eRemoveLinkedItems) -> removes a sub-track item from this track.

        @param subTrackItem: the hiero.core.SubTrackItem to remove from this track
        @param option: options controlling the remove behavior. By default linked items are also removed.
        """
        return None

    def removeTag(self, tag: core.Tag) -> None:
        """
        self.removeTag(tag) -> removes the tag from the video track.

        @param tag: hiero.core.Tag object
        """
        return None

    def setAllViews(self) -> None:
        """
        self.setAllViews() -> assigns all views to a VideoTrack in the form of an empty string since that represents all views.
        An error is raised if the track doesn't have a project with multiple views.
        """
        return None

    def setBlendEnabled(self, blendEnabled: bool) -> None:
        """
        self.setEnabled() -> enables or disables blending on the VideoTrack, if it is not locked or restricted.
        An error is raised if the track is locked or restricted.
        """
        return None

    def setBlendMaskEnabled(self, enabled: bool) -> None:
        """
        self.setBlendMaskEnabled() -> sets whether blend-masking is enabled or not, if it is not locked or restricted.
        An error is raised if the track is locked or restricted.
        """
        return None

    def setBlendMode(self, blendMode: str) -> None:
        """
        self.setBlendMode() -> sets the blend mode to be used, if it is not locked or restricted. Expected strings are NUKE Merge Node operations.
        An error is raised if the track is locked or restricted.
        """
        return None

    def setView(self, view: str) -> None:
        """
        self.setView() -> assigns a view on a VideoTrack.
        An error is raised if the track doesn't have a project with multiple views, or the specified view is invalid.
        """
        return None

    def splitViewsToTracks(self) -> None:
        """
        self.splitViewsToTracks() -> split the views to separate tracks on the Timeline.
        An error is raised if the track doesn't have a project with multiple views.
        """
        return None

    def subTrackItems(self) -> object:
        """
        self.subTrackItems() -> returns a tuple with an entry for each sub track in this track, each entry being a tuple of items
        on the corresponding sub track.

        @return: tuple of hiero.core.SubTrackItem sub-class objects
        """
        return tuple()

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

    def view(self) -> str:
        """
        self.view() -> returns a string representing the view assigned to the VideoTrack. An empty string is returned if the track has multiple views assigned.

        @return: String containing the view name
        """
        return str()

    def __copy__(self,) -> None:
        """

        """
        return None

    def _VideoTrack_addToNukeScript(self, script=None, additionalNodes=*args, disconnected=False, includeAnnotations=False, includeEffects=True):
        """
        Add a Read node for each track item to the script with Merge or Dissolve nodes
        to join them in a sequence. TimeClip nodes are added to pad any gaps between clips.

        @param script: Nuke script object to add nodes to.
        @param additionalNodes: List of nodes to be added post read, passed on to track items
        @param additionalNodesCallback: callback to allow custom additional node per item function([Clip|TrackItem|Track|Sequence])
        @param includeRetimes: True/False include retimes
        @param retimeMethod: "Motion", "Blend", "Frame" - Knob setting for OFlow retime method
        @param offset: Optional, Global frame offset applied across whole script
        @param skipOffline: If True, offline clips are not included in the export
        @param mediaToSkip: List of MediaSources which should be excluded from the export
        @param disconnected: If True, items on the track are not connected and no constant nodes are added to fill gaps
        @param includeAnnotations: If True, clip-level annotations will be included in the output
        @param includeEffects: If True, clip-level soft effects will be included in the output
        """
        return None

    def createEffect(self, effectType=None, cloneFrom=None, copyFrom=None, trackItem=None, timelineIn=None, timelineOut=None, subTrackIndex=None):
        """
        self.createEffect(trackItem=None, timelineIn=None, timelineOut=None, subTrackIndex=None) -> Create an effect item and add it to the track.

        The effect's node will be of type effectType or if cloneFrom is given, will be a clone of that.  It will use timing either based on trackItem if given or timelineIn and timelineOut.  If none of these are specified,
        the effect will cover the full duration of the track's parent sequence.

        @param effectType: the node type to create a soft effect for

        @param cloneFrom: if given, the new effect item will be cloned from this

        @param copyFrom: if given, the new effect item will be copied from this

        @param trackItem: if specified, the effect will be linked to the track item and use the same timing

        @param timelineIn: the effect start time

        @param timelineOut: the effect end time

        @param subTrackIndex: if specified, will be placed on the appropriate sub-track, otherwise will be placed on a new sub-track

        @return: the created EffectTrackItem object
        """
        return EffectTrackItem()
