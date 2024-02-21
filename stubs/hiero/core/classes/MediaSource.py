"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import ui
import core
import nuke
import hiero
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class MediaSource:
    """
    Represents a media source.
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

    def associatedFilePaths(self) -> typing.List[str]:
        """
        self.associatedFilePaths() -> Return a list of file paths associated with the 'main' file, this is used with r3d clips where there are multiple r3ds in sequence, or rmd files.

        @return: list of path strings
        """
        ...

    def createOfflineVideoMediaSource(self, path: str, start: int, duration: int, frameRate: hiero.core.TimeBase, startTimecode: int = 0) -> hiero.core.MediaSource:
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

    def duration(self) -> int:
        """
        self.duration() -> returns the duration, in frames.

        @return: frames
        """
        ...

    def fileinfos(self) -> typing.List[core.MediaFileInfo]:
        """
        self.fileinfos() -> returns a tuple of hiero.core.MediaFileInfo objects, which can be used to retrieve all of the file fragments that are used by this MediaSource.

        @return: tuple of hiero.core.MediaFileInfo objects
        """
        ...

    def filename(self) -> str:
        """
        self.filename() -> returns the file name (and just the file name) of the first file used for the MediaSource.

        Deprecated; Please use the fileinfos() method instead.

        @return: string
        """
        ...

    def filenameHead(self) -> str:
        """
        self.filenameHead() -> returns the portion of filename before the frame index for an image sequence.

        @return: string
        """
        ...

    def filenamePadding(self) -> int:
        """
        self.filenameHead() -> returns the number characters used for frame index. -1 if not an image sequence.

        @return: int
        """
        ...

    def firstpath(self) -> str:
        """
        self.firstpath() -> returns the full path of the first file used for the MediaSource.
        Deprecated; Please use the fileinfos() method instead.

        @return: string
        """
        ...

    def fragmentFilename(self, index: int) -> str:
        """
        self.fragmentFilename(fragmentIndex) -> returns the file name (and just the file name) for the fragment of the MediaSource, specified by the fragmentIndex.
        Deprecated; Please use the fileinfos() method instead

        @param fragmentIndex: index of the fragment to retrieve
        @return: string
        """
        ...

    def fragmentPath(self, index: int) -> str:
        """
        self.fragmentPath(fragmentIndex) -> returns the full path for the fragment of the MediaSource, specified by the fragmentIndex.
        Deprecated; Please use the fileinfos() method instead.

        @param fragmentIndex: index of the fragment to retrieve
        @return: string
        """
        ...

    def hasAudio(self) -> bool:
        """
        self.hasAudio() -> True if the source has audio.

        @return: True or False
        """
        ...

    def hasVideo(self) -> bool:
        """
        self.hasVideo() -> True if the source has video.

        @return: True or False
        """
        ...

    def height(self) -> int:
        """
        self.height() -> returns the height of the media.

        @return: int
        """
        ...

    def isMediaPresent(self) -> bool:
        """
        self.isMediaPresent() -> returns True if the media is present.

        @return: True or False
        """
        ...

    def isNull(self) -> bool:
        """
        self.isNull() -> True if the object points to an invalid source, False otherwise.

        @return: True or False
        """
        ...

    def isOffline(self) -> bool:
        """
        self.isOffline() -> returns True if the media is missing or unavailable for any reason.

        @return: True or False
        """
        ...

    def metadata(self) -> hiero.core.DataCollection:
        """
        self.metadata() -> returns a hiero.core.Metadata object with metadata for the MediaSource.

        @return: hiero.core.Metadata object
        """
        ...

    def numChannels(self, mediaType: hiero.core.MediaSource.MediaType) -> int:
        """

        """
        ...

    def numFragments(self) -> int:
        """
        self.numFragments() -> returns the number of files used by this MediaSource, or -1 for invalid media. For instance, for mov files, this will return 1; for exr sequences this method will return the number of exr files in the sequence.
        Deprecated; Please use the fileinfos() method instead.

        @return: int
        """
        ...

    def pixelAspect(self) -> float:
        """
        self.pixelAspect() -> returns the pixel aspect ratio of the media.

        @return: float
        """
        ...

    def refresh(self) -> None:
        """
        self.refresh() -> updates source info for latest changes in underlying files but doesn't update the frame range
        """
        ...

    def singleFile(self) -> bool:
        """
        self.singleFile() -> returns True if this MediaSource is comprised of only a single file regardless of how many frames it contains (like a .mov or .r3d).

        @return: True or False
        """
        ...

    def startTime(self) -> int:
        """
        self.startTime() -> returns the start time of the media.

        @return: int
        """
        ...

    def timecodeStart(self) -> int:
        """

        """
        ...

    def toString(self) -> str:
        """
        self.toString(includeMetadata=False) -> returns a string with info for the MediaSource. str(object) is equivalent to object.toString().

        @param includeMetadata: True adds metadata to the string, False does not
        @return: string
        """
        ...

    def width(self) -> int:
        """
        self.width() -> returns the width of the media.

        @return: int
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...

    MediaType: Any = None
    kVideo: Any = None
    kAudio: Any = None
