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


class FlipbookManager:
    """
    Object for Flipbook manager
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

    def createClip(self, filepath: str) -> hiero.core.Clip:
        """
        self.createClip(filepath) -> creates and return a flipbook clip for the defined filepath.

        @return: hiero.core.Clip
        """
        ...

    def createEffectItem(self, effectType: bytes, timelineIn: int, timelineOut: int) -> hiero.core.EffectTrackItem:
        """
        self.createEffectItem(effectType, timelineIn, timelineOut) -> creates and return a flipbook Soft Effect with defiend effectType,
        covering the specified timeline in and out range.

        @return: hiero.core.EffectTrackItem
        """
        ...

    def createSequence(self, frameRate: hiero.core.TimeBase, outputFormat: hiero.core.Format, views: typing.List[str]) -> hiero.core.Sequence:
        """
        self.createSequence(framerate, outputformat) -> creates and returns a flipbook sequence with the defined framerate and ouput formar.

        @return: hiero.core.Sequence
        """
        ...

    def setWorkingSpace(self, workingSpace: str) -> None:
        """
        self.setWorkingSpace(workingSpace) -> sets the colorspace to use as the working space.

        @return: None
        """
        ...

    def updateOCIOConfig(self, ocioConfigPath: str) -> None:
        """
        self.updateOCIOConfig(ocioConfigPath) -> updates the flipbook OCIO setting with the defined ocio config filename.

        @return: None
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...
