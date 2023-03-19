import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class TrackItem(TrackItemBase):
    """
    Represents a specific item on a Track. Can also be created using the createTrackItem method on VideoTrack and AudioTrack objects. Can be converted to a MediaSource object if isSource() returns True, or a Sequence object if isSequence() returns True.
    Note that the version functions don't cause a scan of any directories for other versions of media and will only skip to versions that have already been discovered. For an example of how to do that, see Plugins/site-packages/hiero/ui/ScanForVersions.py.
    For an example of how to implement custom versioning scheme, see Plugins/site-packages/hiero/core/versioning_example.py.
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

    def addTag(self, tag: core.Tag) -> core.Tag:
        """
        self.addTag(tag) -> adds a new tag to the track item.

        @param tag: tag object
        @return: a hiero.core.Tag object
        """
        return core.Tag()

    def currentVersion(self) -> core.Version:
        """
        self.currentVersion() -> returns a version object for the current version set on this track item.

        @return: hiero.core.Version object
        """
        return core.Version()

    def eventNumber(self) -> int:
        """
        self.eventNumber() -> Get the event number of this track item on it's Sequence.

        @return: integer event number
        """
        return int()

    def getAvailableOcioColourTransforms(self) -> typing.List*args:
        """
        self.    getAvailableOcioColourTransforms() -> returns colour transform for the media source.

        @return: string
        """
        return list()

    def handleInLength(self) -> int:
        """
        self.handleInLength() -> returns the length of the track item's in handle.

        @return: frames
        """
        return int()

    def handleInTime(self) -> int:
        """
        self.handleInTime() -> returns the track item's in handle time.

        @return: frames
        """
        return int()

    def handleOutLength(self) -> int:
        """
        self.handleOutLength() -> returns the length of the track item's out handle.

        @return: frames
        """
        return int()

    def handleOutTime(self) -> int:
        """
        self.handleOutTime() -> returns the track item's out handle time.

        @return: frames
        """
        return int()

    def inTransition(self) -> core.Transition:
        """
        self.inTransition() -> returns the in transition for this track item.

        @return: hiero.core.Transition object
        """
        return core.Transition()

    def isMediaPresent(self) -> bool:
        """
        self.isMediaPreset() -> returns True if the track item represent a media source and if the media source is currently available in Hiero (and not offline). Returns False otherwise.

        @return: True or False
        """
        return bool()

    def link(self, trackItem: core.TrackItem) -> None:
        """
        self.link(trackItem) -> Links track item with another track item. Both track items must point to the same source.

        @param trackItem: track item to link to
        """
        return None

    def mapSourceToTimeline(self, time: float) -> float:
        """
        self.mapTimelineToSource(time) -> Map from the track item's source time to timeline time.

        @param time: time to map
        @return: mapped time
        """
        return float()

    def mapTimelineToSource(self, time: float) -> float:
        """
        self.mapTimelineToSource(time) -> Map from timeline time to the track item's source time.

        @param time: time to map
        @return: mapped time
        """
        return float()

    def maxVersion(self) -> core.Version:
        """
        self.maxVersion() -> sets the highest available version on this TrackItem. If versionLinkedToBin() is set, changes the version on all linked objects.

        @return: hiero.core.Version object
        """
        return core.Version()

    def mediaType(self) -> core.TrackItem.MediaType:
        """
        self.mediaType() -> returns media type for the track item.

        @return: MediaType object
        """
        return core.TrackItem.MediaType()

    def metadata(self) -> core.DataCollection:
        """
        self.metadata() -> returns the metadata for the track item.

        @return: hiero.core.DataCollection object
        """
        return core.DataCollection()

    def minVersion(self) -> core.Version:
        """
        self.minVersion() -> sets the lowest available version on this TrackItem. If versionLinkedToBin() is set, changes the version on all linked objects.

        @return: hiero.core.Version object
        """
        return core.Version()

    def name(self) -> str:
        """
        self.name() -> returns the track item's name.

        @return: string
        """
        return str()

    def nextVersion(self) -> core.Version:
        """
        self.nextVersion() -> sets the next available version on this TrackItem. If versionLinkedToBin() is set, changes the version on all linked objects.

        @return: hiero.core.Version object
        """
        return core.Version()

    def numVersions(self) -> int:
        """
        self.numVersions() -> returns the total number of versions on this track item currently (nothing to do with the maximum or minimum version number).

        @return: int
        """
        return int()

    def outTransition(self) -> core.Transition:
        """
        self.outTransition() -> returns the out transition for this track item.

        @return: hiero.core.Transition object
        """
        return core.Transition()

    def playbackSpeed(self) -> float:
        """
        self.playbackSpeed() -> returns the playback speed of this track item.

        @return: double
        """
        return float()

    def prevVersion(self) -> core.Version:
        """
        self.prevVersion() -> sets the next available version on this TrackItem. If versionLinkedToBin() is set, changes the version on all linked objects.

        @return: hiero.core.Version object
        """
        return core.Version()

    def reconnectMedia(self, path: str) -> None:
        """
        self.reconnectMedia(path) -> Reconnects media for the Clip used by the TrackItem, using the specified path.

        @param path: path containing media to reconnect to
        """
        return None

    def reformatState(self) -> core.ReformatState:
        """
        self.reformatState() -> returns the reformat state for the track item.

        @return: hiero.core.ReformatState object
        """
        return core.ReformatState()

    def removeTag(self, tag: core.Tag) -> None:
        """
        self.removeTag(tag) -> removes the tag from the track item.

        @param tag: hiero.core.Tag object
        """
        return None

    def replaceClips(self, path: str) -> None:
        """
        self.replaceClips(path) -> Find a new Clip from the specified path, and replace the TrackItem's existing Clip with it.

        @param path: path containing media to replace with
        """
        return None

    def setCameraColourTransform(self, arg__1: str) -> None:
        """
        self.setCameraColourTransform(colourTransform) -> sets the camera colour transform for the source media.

        @param colourTransform: Colour transform name
        """
        return None

    def setCurrentVersion(self, version: core.Version) -> None:
        """
        self.setCurrentVersion(version) -> sets the current version (by object) on this track item. Note that this method doesn't check that the versioned media source exists on disk.

        @param version: hiero.core.Version object
        """
        return None

    def setCurrentVersionIndex(self, *args, **kwargs):
        """
        self.setCurrentVersionIndex(index) -> sets the current version on this track item and returns the new version object. Creates a new version if there wasn't one before, but doesn't check that the versioned media source exists on disk.

        @param index: the integer index to set the current version on this track item to
        @return: hiero.core.Version object

        WARNING - DEPRECATED ( setCurrentVersionIndex ): This method is deprecated and will not be present in future versions of the Python API.
        Version indices are no longer unique identifiers and should not be used as such. Please use TrackItem.setActiveVersion() instead.
        """
        return Version()

    def setName(self, name: str) -> None:
        """
        self.setName(name) -> sets the name of the track item.

        @param name: the value to set the track name to
        """
        return None

    def setPlaybackSpeed(self, speed: float) -> None:
        """
        self.setPlaybackSpeed(newSpeed) -> sets the playback speed of this track item.

        @param newSpeed: double
        """
        return None

    def setSource(self, *args, **kwargs):
        """
        self.setSource(clip, trackIndex=0) -> sets the source Clip for this TrackItem.
        If the TrackItem is not already in a Track, the duration will be set to the Clip's duration.

        @param clip: the hiero.core.Clip object to set as the source for this track item
        @param trackIndex: optional track index, for instance if you are adding an audio Clip and want to use its second audio track
        @return: the hiero.core.Clip object passed in
        """
        return TrackItem()

    def setSourceIn(self, arg__1: float) -> None:
        """
        self.setSourceIn(time) -> sets the source in for the track item. This will shrink or grow the duration.

        @param time: frame value
        """
        return None

    def setSourceMediaColourTransform(self, arg__1: str) -> None:
        """
        self.setSourceMediaColourTransform(colourTransform) -> sets the input colour transform for the source media.

        @param colourTransform: Colour transform name
        """
        return None

    def setSourceOut(self, arg__1: float) -> None:
        """
        self.setSourceOut(time) -> sets the source out for the track item. This will shrink or grow the duration.

        Note that this value depends on speed. For exact editing, edit speed instead in order to avoid rounding errors.

        @param time: frame value
        """
        return None

    def setTimelineIn(self, arg__1: int) -> None:
        """
        self.setTimelineIn(inTime) -> sets the timeline in value. Shrinks or grows the timeline duration, as appropriate.

        @param inTime: frame value
        """
        return None

    def setTimelineOut(self, arg__1: int) -> None:
        """
        self.setTimelineOut(outTime) -> sets the timeline out value. Shrinks or grows the timeline duration, as appropriate.

        @param outTime: frame value
        """
        return None

    def setTimes(self, timelineIn: int, timelineOut: int, sourceIn: float, sourceOut: float) -> None:
        """
        self.setTimes(timelineIn, timelineOut, sourceIn, sourceOut) -> sets the timeline and source times for the track item.

        @param timelineIn: timeline in frame
        @param timelineOut: timeline out frame
        @param sourceIn: source in frame
        @param sourceOut: source out frame
        """
        return None

    def setVersionLinkedToBin(self, linked: bool, updateVersion: bool = False) -> None:
        """
        self.setVersionLinkedToBin(linked) -> link the TrackItem's version to that of it's associated BinItem. If updateVersion is false, the TrackItem's version will not be updated immediately, this will happen next time a version is set on the BinItem or any linked TrackItems.

        @param linked: The linked state to be set on the TrackItem
        @param updatedVersion: Whether or not the TrackItems version will be updated
        """
        return None

    def source(self) -> object:
        """
        self.source() -> depending on the underlying type of the track item, returns a hiero.core.Clip object, a hiero.core.Sequence object or a hiero.core.MediaSource object.

        @return: a hiero.core.Clip object, a hiero.core.Sequence object or a hiero.core.MediaSource object
        """
        return object()

    def sourceDuration(self) -> float:
        """
        self.sourceDuration() -> returns the source duration value for the track item.

        Note that this value depends on speed, and may not be an integer value.

        @return: frames
        """
        return float()

    def sourceIn(self) -> float:
        """
        self.sourceIn() -> returns the source in value for the track item.

        Note that after a combination of a retime and editing, this value may not be an integer.

        @return: frame
        """
        return float()

    def sourceMediaColourTransform(self) -> str:
        """
        self.setSourceMediaColourTransform() -> returns colour transform for the media source.

        @return: string
        """
        return str()

    def sourceOut(self) -> float:
        """
        self.sourceOut() -> returns the source out value for the track item.

        Note that this value depends on speed, and may not be an integer value.

        @return: frame
        """
        return float()

    def tags(self) -> object:
        """
        self.tags() -> returns a tuple of all of the tags applied to this object.

        @return: tuple of hiero.core.Tag objects
        """
        return object()

    def thumbnail(self, index: int = 0, layer: str = Default(self, Hiero.Python.String)) -> PySide2.QtGui.QImage:
        """
        self.thumbnail(frame, layer) -> returns a thumbnail of the frame specified as a QImage object.

        @param frame: the frame to get the thumbnail for (defaults to 0)
        @param layer: the layer to get the thumbnail for (defaults to colour)
        @return: QImage object
        """
        return Any

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        return str()

    def unlink(self, trackItem: core.TrackItem) -> None:
        """
        self.unlink(trackItem) -> Unlinks this track item from given track item.

        @param trackItem: track item from which this track item is being unlinked
        """
        return None

    def versionDown(self, *args, **kwargs):
        """
        self.versionDown() -> decrements the current version on this track item and returns the new version object. Creates a new version if there wasn't one before, but doesn't check that the versioned media source exists on disk.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionDown ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from TrackItem. To find new versions, please use hiero.core.VersionScanner. To obtain the next version, please use TrackItem.prevVersion().
        """
        return Version()

    def versionLinkedToBin(self) -> bool:
        """
        self.versionLinkedToBin() -> get if the TrackItem's version is linked to the associated BinItem

        @return: bool
        """
        return bool()

    def versionMaxAvailable(self, *args, **kwargs):
        """
        self.versionMaxAvailable() -> returns the highest discovered version on this track item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionMaxAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from TrackItem. This method has been replaced by TrackItem.maxVersion().
        """
        return Version()

    def versionMinAvailable(self, *args, **kwargs):
        """
        self.versionMinAvailable() -> returns the lowest discovered version on this track item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionMinAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from TrackItem. This method has been replaced by TrackItem.minVersion().
        """
        return Version()

    def versionNextAvailable(self, *args, **kwargs):
        """
        self.versionNextAvailable() -> returns the next highest available version on this track item that the application has discovered.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionNextAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from TrackItem. This method has been replaced by TrackItem.nextVersion().
        """
        return Version()

    def versionPrevAvailable(self, *args, **kwargs):
        """
        self.versionPrevAvailable() -> returns the next lowest version on this track item that the application has discovered.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionPrevAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from TrackItem. This method has been replaced by TrackItem.prevVersion().
        """
        return Version()

    def versionUp(self, *args, **kwargs):
        """
        self.versionUp() -> increments the current version on this track item and returns the new version object. Creates a new version if there wasn't one before, but doesn't check that the versioned media source exists on disk.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionUp ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from TrackItem. To find new versions, please use hiero.core.VersionScanner. To obtain the next version, please use TrackItem.nextVersion().
        """
        return Version()

    def __copy__(self,) -> None:
        """

        """
        return None

    MediaType: Any = None
    kVideo: Any = None
    kAudio: Any = None
    kUnknown: Any = None

    def _TrackItem_addToNukeScript(self, script=None, firstFrame=None, additionalNodes=[], additionalNodesCallback=None, includeRetimes=False, retimeMethod=None, startHandle=None, endHandle=None, colourTransform=None, offset=0, nodeLabel=None, includeAnnotations=False, includeEffects=True, outputToSequenceFormat=False):
        """
        This is a variation on the Clip.addToNukeScript() method that remaps the
        Read frame range to the range of the this TrackItem rather than the Clip's
        range. TrackItem retimes and reverses are applied via Retime and OFlow nodes
        if needed. The additionalNodes parameter takes a list of nodes to add before
        the source material is shifted to the TrackItem timeline time and trimmed to
        black outside of the cut. This means timing can be set in the original
        source range and adding channels, etc won't affect frames outside the cut
        length.

        @param retimeMethod: "Motion", "Blend", "Frame" - Knob setting for OFlow retime method
        @param offset: Optional, Global frame offset applied across whole script
        """
        return None

    def __TrackItem_unlinkAll(self):
        """
        self.unlinkAll() -> Unlink all track items that are linked to this one.
        """
        return None