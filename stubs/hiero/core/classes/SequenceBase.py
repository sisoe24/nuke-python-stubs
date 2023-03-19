import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class SequenceBase(Object):
    """
    Base class for Sequence and Clip objects. Has some methods common to both of those objects. Most likely never used directly.
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

    def addTag(self, tag: core.Tag) -> core.Tag:
        """
        self.addTag(tag) -> adds a hiero.core.Tag object to the Clip or Sequence.

        @param tag: the tag object to add
        @return: hiero.core.Tag object
        """
        return core.Tag()

    def addTagToRange(self, tag: core.Tag, inTime: int, outTime: int) -> core.Tag:
        """
        self.addTagToRange(tag, inTime, outTime) -> adds a hiero.core.Tag object to the specified range of the Clip or Sequence.

        @param tag: the tag object to add
        @param inTime: the first time at which the tag is valid
        @param outTime: the last time at which the tag is valid
        @return: hiero.core.Tag object
        """
        return core.Tag()

    def binItem(self) -> core.BinItem:
        """
        self.binItem() -> returns the parent BinItem this Sequence or Clip belongs to, if any.

        @return: BinItem
        """
        return core.BinItem()

    def clearInTime(self) -> None:
        """
        self.clearInTime(t) -> clear the 'in' point for the clip to Time t.

        @return: None
        """
        return None

    def clearOutTime(self) -> None:
        """
        self.clearInTime(t) -> clear the 'out' point for the clip to Time t.

        @return: None
        """
        return None

    def clearRange(self, start: int, end: int, ripple: bool) -> None:
        """
        self.clearRange(start, end, ripple) -> Clears a time range out of the sequence; effectively a razor on any clips straddling the start and end, and a delete of everything else.

        @param start: the start of the range to clear
        @param end: the end of the range to clear
        @param ripple: set to True to shift the remaining track items to the left
        """
        return None

    def disableSoftTrims(self) -> None:
        """
        self.disableSoftTrims() -> disables soft trims on the object.
        """
        return None

    def dropFrame(self) -> bool:
        """
        self.dropFrame() -> get whether sequence timecode is displayed in drop frame format
        """
        return bool()

    def duration(self) -> int:
        """
        self.duration() -> returns the duration of the Clip or Sequence.

        @return: int time value
        """
        return int()

    def editFinished(self, *args, **kwargs):
        """
        self.editFinished(trackItems) -> this should be called after finishing editing the sequence to ensure that its internal state is updated properly and to send a signal to all objects listening to changes in this object (e.g. UI views).This function optionally takes a list of track items that is used to selectively rebuild only those sections of the timeline.This allows a faster update when the edited track items are known.

        @param trackItems: optional, the track items to be updated
        """
        return list()

    def enableSoftTrims(self, inTime: int, outTime: int) -> None:
        """
        self.enableSoftTrims(inTime, outTime) -> enables soft trims on the object.

        @param inTime: Time - soft trim in time
        @param outTime: Time - soft trim out time
        """
        return None

    def format(self) -> core.Format:
        """
        self.format() -> returns the output Format object for this Sequence or Clip.

        @return: hiero.core.Format object
        """
        return core.Format()

    def framerate(self) -> core.TimeBase:
        """
        self.framerate() -> returns the framerate of the Sequence or Clip.

        @return: hiero.core.TimeBase object
        """
        return core.TimeBase()

    def getAnnotationsTrack(self) -> core.VideoTrack:
        """
        self.getAnnotationsTrack() -> Returns the annotations track for the Clip or Sequence. If one does not already exist, it will be created.
        """
        return core.VideoTrack()

    def inOutEnabled(self) -> bool:
        """
        self.inOutEnabled() -> Checks if the 'in' and 'out' points are enabled in the Sequence or Clip.

        @return: bool
        """
        return bool()

    def inTime(self) -> int:
        """
        self.inTime() -> returns the 'in' point set on the clip.

        @return: frame
        """
        return int()

    def isNull(self) -> bool:
        """
        self.isNull() -> returns False if this is a valid Sequence or Clip object, True otherwise.

        @return: True or False
        """
        return bool()

    def metadata(self) -> core.DataCollection:
        """
        self.metadata() -> returns a collection of metadata for the object.

        @return: hiero.core.DataCollection object
        """
        return core.DataCollection()

    def name(self) -> str:
        """
        self.name() -> returns the name of the object.

        @return: string
        """
        return str()

    def outTime(self) -> int:
        """
        self.outTime() -> returns the 'out' point set on the clip.

        @return: frame
        """
        return int()

    def posterFrame(self) -> int:
        """
        self.posterFrame() -> get the frame in the sequence used for thumbnails
        """
        return int()

    def project(self) -> object:
        """
        self.project() -> returns the Project object that this is attached to, or None if the object is not attached to a project.

        @return: hiero.core.Project object
        """
        return object()

    def rawView(self) -> str:
        """
        self.rawView() -> returns a string representing the raw view of this sequence or clip.

        @return: string
        """
        return str()

    def razorAt(self, *args, **kwargs):
        """
        self.razorAt(time) -> Creates razor cuts on all of the unlocked tracks for the parameter time(s).

        @param time: if a single (integer) value, indicates the razor cut time; if a tuple or list of integer values, then the times to create multiple cuts at
        """
        return Number()

    def refreshInOutEnabled(self) -> None:
        """
        self.refreshInOutEnabled() -> Automatically set the sequence in/out enabled based on the current in/out values.

        @return: None
        """
        return None

    def removeTag(self, tag: core.Tag) -> None:
        """
        self.removeTag(tag) -> removes the tag from the track.

        @param tag: hiero.core.Tag object
        """
        return None

    def setDropFrame(self, drop: bool) -> None:
        """
        self.setDropFrame(drop) -> set whether sequence timecode is displayed in drop frame format
        """
        return None

    def setFormat(self, format: core.Format) -> None:
        """
        self.setFormat(format) -> set the format of the Sequence or Clip.

        @param format: a hiero.core.Format object to set for the Clip or Sequence.

        Example: myClipSequence.setFormat( hiero.core.Format(2048, 400, 2.37, 'MyFormat') )
        """
        return None

    def setFramerate(self, timeBase: core.TimeBase) -> None:
        """
        self.setFramerate(framerate) -> set the framerate of the Sequence or Clip.

        @param framerate: framerate value to set
        """
        return None

    def setInOutEnabled(self, enable: bool) -> None:
        """
        self.setInOutEnabled(enable) -> Enable/Disable the 'in' and 'out' points.

        @return: None
        """
        return None

    def setInTime(self, t: int) -> None:
        """
        self.setInTime(t) -> set the 'in' point for the clip to Time t.
        This will also enable the In/Out lock.

        @return: None
        """
        return None

    def setName(self, name: str) -> None:
        """
        self.setName() -> set the name of the object.

        @param: string new name
        """
        return None

    def setOutTime(self, t: int) -> None:
        """
        self.setOutTime(t) -> set the 'out' point for the clip to Time t.
        This will also enable the In/Out lock.

        @return: None
        """
        return None

    def setPosterFrame(self, frame: int) -> None:
        """
        self.setPosterFrame(frame) -> set the frame in the sequence used for thumbnails
        """
        return None

    def setSoftTrimsInTime(self, value: int) -> None:
        """
        self.setSoftTrimsInTime(inTime) -> sets the in time for the soft trims. Note: this method does not enable soft trims if they are disabled.

        @param inTime: in frame value for the soft trims
        """
        return None

    def setSoftTrimsOutTime(self, value: int) -> None:
        """
        self.setSoftTrimsOutTime(outTime) -> sets the out time for the soft trims. Note: this method does not enable soft trims if they are disabled.

        @param outTime: out frame value for the soft trims
        """
        return None

    def setTimecodeStart(self, *args, **kwargs):
        """
        self.setTimecodeStart(time) -> sets the value of the start timecode by frame. To convert times to frame values, use TimeCode.HMSFToFrames or TimeCode.stringToTime.
        self.setTimecodeStart(timecodeValue, hasDropFrames) -> sets the value of the start timecode by formatted string, using the framerate of the Sequence or Clip as the time base. If just passing in a framerate, pass it in as an integer.

        @param time: frame value to set the time code to
        @param timecodeValue: string of the format "hh:mm:ss:ff"
        @param hasDropFrames: True if the timecode includes drop frames, False otherwise
        """
        return Number()

    def softTrimsEnabled(self) -> bool:
        """
        self.softTrimsEnabled() -> returns True if soft trims are enabled, False otherwise.

        @return: True or False
        """
        return bool()

    def softTrimsInTime(self) -> int:
        """
        self.softTrimsInTime() -> returns the in time set for the soft trims.

        @return: frame
        """
        return int()

    def softTrimsOutTime(self) -> int:
        """
        self.softTrimsOutTime() -> returns the out time set for the soft trims.

        @return: frame
        """
        return int()

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

    def timecodeStart(self) -> int:
        """
        self.timecodeStart() -> returns the frame value of the start timecode. To convert this to a time code string, use TimeCode.timeToString.

        @return: frame
        """
        return int()

    def timelineOffset(self) -> int:
        """
        self.timelineOffset() -> returns the timeline offset value.

        @return: frame
        """
        return int()

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        return str()

    def writeAudioToFile(self, *args, **kwargs):
        """
        self.writeAudioToFile() -> Bounce down audio tracks and write to wav file at specified location. File will be created or overwritten.

        @param filepath: the filepath of file to be written
        @param inTime: in point of the timeline to write
        @param outTime: out point of the timeline to write
        @param numChannels: number of audio channels
        @param sampleRate: the sample rate to export to
        @param bitDepth: sample bit depth (PCM only)
        @param bitRate: audio bitrate in bits (compressed formats only)
        """
        return str()

    def __copy__(self,) -> None:
        """

        """
        return None
