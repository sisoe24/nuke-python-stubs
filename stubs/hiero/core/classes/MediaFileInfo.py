import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class MediaFileInfo(object):
    """
    Object representing a single set of media files on disk.
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def endFrame(self) -> int:
        """
        self.endFrame() -> returns the last frame of the media source contained by this object. Note that for video formats (mov, r3d), this will always be the media's (duration - 1).

        @return: integer frame
        """
        ...

    def filename(self) -> str:
        """
        self.filename() -> returns a path to a media source on disk. May represent multiple files, as with image sequences. The form will be one of the following, depending on the file extension of the media:
        * /somepath/file.mov
        * /somepath/imagesequence.######.dpx (1-40)

        In the case of the image sequence above, the numbers between the brackets represent the first and last frame of the sequence.

        @return: string
        """
        ...

    def startFrame(self) -> int:
        """
        self.startFrame() -> returns the first frame of the media source contained by this object. Note that for video formats (mov, r3d), this will always be 0.

        @return: integer frame
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...
