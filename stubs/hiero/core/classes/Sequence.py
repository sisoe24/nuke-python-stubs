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


class Sequence(SequenceBase):
    """
    Object for Sequences.
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

    def __len__(self, ) -> None:
        """
        Return len(self).
        """
        ...

    def __getitem__(self, key, ) -> None:
        """
        Return self[key].
        """
        ...

    def activePlayhead(self) -> int:
        """
        activePlayhead() -> Returns the index of the active playhead.
        """
        ...

    def addTrack(self, *args: typing.Any, **kwargs: typing.Any) -> Iterable:
        """
        self.addTrack(track) -> adds a video or audio track to the Sequence.

        @param track: video or audio track to add
        """
        ...

    def audioTrack(self, index: int) -> core.AudioTrack:
        """
        self.audioTrack(index) -> returns the audio track for the specified index.

        @param index: index of the audio track to return
        @return: hiero.core.AudioTrack
        """
        ...

    def audioTracks(self) -> object:
        """
        self.audioTracks() -> returns a tuple with all of the audio tracks.

        @return: tuple of hiero.core.AudioTrack objects
        """
        ...

    def changeFramerateKeepFrames(self, toTimebase: core.TimeBase) -> None:
        """
        self.changeFramerateKeepFrames(toTimebase) -> changes the timebase of the sequence, keeping frames of track items the same

        @param toTimebase: timebase to change to
        """
        ...

    def changeFramerateKeepTimecodes(self, toTimebase: core.TimeBase, roundingMode: core.TimeBase.RoundingMode) -> None:
        """
        self.changeFramerateKeepTimecodes(toTimebase, roundingMode) -> changes the timebase of the sequence, keeping timecodes of track items the same, according to the specified rounding mode

        @param toTimebase: timebase to change to
        @param roundingMode: rounding mode to use when converting timebases (hiero.core.TimeBase.kRoundNearest, hiero.core.TimeBase.kRound32Pulldown)
        """
        ...

    def clone(self, *args, **kwargs) -> Iterable:
        """
        self.clone() -> returns a deep copy of this object.

        @return: hiero.core.Sequence object

        WARNING - DEPRECATED ( clone ): This method is deprecated and will not be present in future versions of the Python API.
        This method has been replaced by copy().
        """
        ...

    def copy(self) -> object:
        """
        self.copy() -> returns a deep copy of this object.

        @return: hiero.core.Sequence object
        """
        ...

    def deserialize(self, data: str, rangeMin: int, rangeMax: int) -> None:
        """
        self.deserialize() -> restore the sequence state from XML data

        @param rangeMin: The beginning of the timeline range effected by this change
        @param rangeMax: The end of the timeline range effected by this change
        """
        ...

    def guid(self) -> object:
        """

        """
        ...

    def importTracks(self, path: str) -> typing.List[core.TrackBase]:
        """
        self.importTracks(filePath) -> imports all of the tracks from the file specified by the filePath argument.

        @param filePath: path to the file to import tracks from
        @return tracks: tuple of created tracks
        """
        ...

    def importTracksFromTimeBaseKeepFrames(self, path: str, toTimebase: core.TimeBase) -> typing.List[core.TrackBase]:
        """
        self.importTracksFromTimeBaseKeepFrames(filePath, srcTimebase) -> imports all of the tracks from the file specified by the filePath argument using the specified timebase.

        @param filePath: path to the file to import tracks from
        @param srcTimebase: timebase to use when reading the source file
        @return tracks: tuple of created tracks
        """
        ...

    def importTracksFromTimeBaseKeepTimecodes(self, path: str, toTimebase: core.TimeBase, roundingMode: core.TimeBase.RoundingMode) -> typing.List[core.TrackBase]:
        """
        self.importTracksFromTimeBaseKeepTimecodes(filePath, srcTimebase, roundingMode) -> imports all of the tracks from the file specified by the filePath argument using the specified timebase.

        @param filePath: path to the file to import tracks from
        @param srcTimebase: timebase to use when reading the source file
        @param roundingMode: rounding mode to use when converting timebases (hiero.core.TimeBase.kRoundNearest, hiero.core.TimeBase.kRound32Pulldown)
        @return tracks: tuple of created tracks
        """
        ...

    def items(self) -> tuple[hiero.core.VideoTrack, hiero.core.AudioTrack]:
        """
        self.items() -> returns a tuple with all of the video tracks concatenated with all of the audio tracks. Can iterate over the video tracks first by using self.numVideoTracks. The audio tracks follow the video tracks in the tuple returned from this method.

        @return: tuple of hiero.core.VideoTrack and hiero.core.AudioTrack objects
        """
        ...

    def matchMedia(self, path: str) -> None:
        """
        self.matchMedia(path) -> match media using the current rule configuration in hiero.core.conformer().

        @param path: path to the folder with the media to connect
        """
        ...

    def numAudioTracks(self) -> int:
        """
        self.numAudioTracks() -> returns number of audio tracks contained by this sequence.

        @return: int
        """
        ...

    def numVideoTracks(self) -> int:
        """
        self.numVideoTracks() -> returns number of video tracks contained by this sequence.

        @return: int
        """
        ...

    def playheadCount(self) -> int:
        """
        playheadCount(index) -> Returns the number of playheads in the sequence.
        """
        ...

    def playheadState(self, index: int) -> core.Sequence.PlayheadState:
        """
        playheadState(index) -> The state of the given playhead index.
        The available states are:  ePlayheadActive : is the active playhead
          ePlayheadEnabled : is not the active playhead but is editable
          ePlayheadDisabled : has been removed.
          ePlayheadInvalid : index does not reference a valid playhead.@param index: The index of the playhead to be queried.
        """
        ...

    def playheadTime(self, index: int) -> int:
        """
        playheadTime(index) -> Returns the time position of the playhead in the sequence.
        @param index: The index of the playhead.
        """
        ...

    def reconnectMedia(self, path: str) -> None:
        """
        self.reconnectMedia(path) -> For each of the Clips used by this Sequence, reconnects media found in the specified path.

        @param path: path containing media to reconnect to
        """
        ...

    def removeTrack(self, *args: typing.Any, **kwargs: typing.Any) -> Iterable:
        """
        self.removeTrack(track) -> removes the track from the Sequence.

        @param track: track to remove (hiero.core.AudioTrack or VideoTrack object)
        """
        ...

    def replaceClips(self, path: str) -> None:
        """
        self.replaceClips(path) -> For each of the TrackItems in this sequence, replace it's Clip with media found in the specified path.

        @param path: path containing media to replace with
        """
        ...

    def serialize(self) -> str:
        """
        self.serialize() -> serialize the sequence object to XML
        """
        ...

    def setActivePlayhead(self, index: int) -> None:
        """
        setActivePlayhead(index) -> The given playhead index is made active.
        There can only be one active playhead, the previous playhead will be made inactive.
        @param index: The index of the playhead to be made active.
        """
        ...

    def setPlayheadEnabled(self, index: int, enabled: bool) -> None:
        """
        setPlayheadEnabled(index, enabled) -> Put the given playhead into the enabled state. The playheadis not active but is visible and editable in the UI. Otherwise the playhead will be disabled, which means thatit will not be visible in the UI.
        The current active playhead cannot be changed by this function.
        @param index: The index of the playhead to be changed.
        @param enabled: True if the playhead is enabled.
        """
        ...

    def setPlayheadTime(self, index: int, time: int) -> None:
        """
        setPlayheadTime(index, time) -> Set the time position for the given playhead index.
        @param index: The index of the playhead to be changed.
        @param time: The new time position to be set.
        """
        ...

    def trackItemAt(self, t: int) -> core.TrackItem:
        """
        self.trackItemAt(time) -> returns the top-most video track item for the specified time that is enabled and has media.

        @param time: frame to get the trackitem for
        @return: hiero.core.TrackItem
        """
        ...

    def trackItemsAt(self, *args: typing.Any, **kwargs: typing.Any) -> tuple:
        """
        self.trackItemsAt(time, mediaType) -> finds enabled track items for the specified time, ordered from top-track to bottom-track (or for audio, min channel to max channel).

        @param time: frame to get the trackitems for
        @param mediaType: TrackItem.MediaType value specifying the media type of the track items to look for (defaults to kVideo)
        @return: tuple of hiero.core.TrackItem objects
        """
        ...

    def videoTrack(self, index: int) -> core.VideoTrack:
        """
        self.videoTrack(index) -> returns the video track for the specified index.

        @param index: index of the video track to return
        @return: hiero.core.VideoTrack
        """
        ...

    def videoTracks(self) -> Tuple[core.VideoTrack, ...]:
        """
        self.videoTracks() -> returns a tuple with all of the video tracks.

        @return: tuple of hiero.core.VideoTrack objects
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...

    PlayheadState: Any = None
    ePlayheadActive: Any = None
    ePlayheadEnabled: Any = None
    ePlayheadDisabled: Any = None
    ePlayheadInvalid: Any = None

    def addClip(self, clip: Clip, time: int | float, videoTrackIndex=0, audioTrackIndex=-1) -> list[core.TrackItem]:
        """
        Add a clip to a sequence, creating a TrackItem for each video/audio channel in the clip,
        adding them to the appropriate tracks and linking them together.  This has the same effect
        as dragging a clip from the Bin View to the Timeline View in the Hiero UI.

        @param clip: the clip to add
        @param time: the in time for created track items
        @param videoTrackIndex: index of the video track to add items to if the clip has video
        @param audioTrackIndex: index of the audio track to start adding items to if the clip has audio
        @return: list of created hiero.core.TrackItems
        """
        ...

    def addToNukeScript(self, script: hiero.core.nuke.ScriptWriter, additionalNodes=list, disconnected=False, masterTrackItem=None, includeAnnotations=False, includeEffects=True, outputToFormat=None):
        """
        addToNukeScript(self, script)
        @param script: Nuke script object to add nodes to.
        @param includeRetimes: True/False include retimes
        @param retimeMethod: "Motion", "Blend", "Frame" - Knob setting for OFlow retime method
        @param additionalNodesCallback: callback to allow custom additional node per item function([Clip|TrackItem|Track|Sequence])
        @param offset: Optional, Global frame offset applied across whole script
        @param skipOffline: If True, offline clips are not included in the export
        @param mediaToSkip: List of MediaSources which should be excluded from the export
        @param disconnected: If True, tracks other than that containing the masterTrackItem are not connected to any inputs
        @param masterTrackItem: Used for controlling the script output if disconnected is specified
        @param includeAnnotations: If True, annotations are included in the exported script
        @param includeEffects: If True, soft effects are included in the exported script
        @param outputToFormat: Format to use for output.  If not specified, the sequence's own format is used.
        @return: None

        Add nodes representing this Sequence to the specified script.
        If there are no clips in the Sequence, nothing is added.
        """
        ...
