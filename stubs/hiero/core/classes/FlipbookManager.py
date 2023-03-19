import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class FlipbookManager(Object):
    """
    Object for Flipbook manager
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

    def createClip(self, filepath: str) -> core.Clip:
        """
        self.createClip(filepath) -> creates and return a flipbook clip for the defined filepath.

        @return: hiero.core.Clip
        """
        return core.Clip()

    def createEffectItem(self, effectType: bytes, timelineIn: int, timelineOut: int) -> core.EffectTrackItem:
        """
        self.createEffectItem(effectType, timelineIn, timelineOut) -> creates and return a flipbook Soft Effect with defiend effectType,
        covering the specified timeline in and out range.

        @return: hiero.core.EffectTrackItem
        """
        return core.EffectTrackItem()

    def createSequence(self, frameRate: core.TimeBase, outputFormat: core.Format, views: typing.List*args) -> core.Sequence:
        """
        self.createSequence(framerate, outputformat) -> creates and returns a flipbook sequence with the defined framerate and ouput formar.

        @return: hiero.core.Sequence
        """
        return core.Sequence()

    def setWorkingSpace(self, workingSpace: str) -> None:
        """
        self.setWorkingSpace(workingSpace) -> sets the colorspace to use as the working space.

        @return: None
        """
        return None

    def updateOCIOConfig(self, ocioConfigPath: str) -> None:
        """
        self.updateOCIOConfig(ocioConfigPath) -> updates the flipbook OCIO setting with the defined ocio config filename.

        @return: None
        """
        return None

    def __copy__(self,) -> None:
        """

        """
        return None
