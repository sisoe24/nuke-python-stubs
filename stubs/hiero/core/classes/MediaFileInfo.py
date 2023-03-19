import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class MediaFileInfo(Object):
    """
    Object representing a single set of media files on disk.
    """

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def endFrame(self) -> int:
        """
        self.endFrame() -> returns the last frame of the media source contained by this object. Note that for video formats (mov, r3d), this will always be the media's (duration - 1).

        @return: integer frame
        """
        return int()

    def filename(self) -> str:
        """
        self.filename() -> returns a path to a media source on disk. May represent multiple files, as with image sequences. The form will be one of the following, depending on the file extension of the media:
        * /somepath/file.mov
        * /somepath/imagesequence.######.dpx (1-40)

        In the case of the image sequence above, the numbers between the brackets represent the first and last frame of the sequence.

        @return: string
        """
        return str()

    def startFrame(self) -> int:
        """
        self.startFrame() -> returns the first frame of the media source contained by this object. Note that for video formats (mov, r3d), this will always be 0.

        @return: integer frame
        """
        return int()

    def __copy__(self,) -> None:
        """

        """
        return None
