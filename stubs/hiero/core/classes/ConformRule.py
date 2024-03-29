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


class ConformRule:
    """
    Represents a conform rule used by Hiero to make decisions when conforming. Can be derived from in order to make new conform rules.
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

    def activate(self) -> None:
        """
        self.activate() -> adds this conform rule to the list of conform rules. Conform operations done after this call will use the rule.
        """
        ...

    def appliesToTrackItems(self) -> bool:
        """
        self.appliesToTrackItems() -> should return True if this conform rule applies to track items.

        @return: True or False; default implementation returns True
        """
        ...

    def compare(self, media: hiero.core.DataCollection, candidateMedia: hiero.core.DataCollection) -> bool:
        """
        self.compare(media, candidateMedia) -> should compare media against candidateMedia, and return True if they match, according to this conform rule.

        The metadata contains the following keys which can be used for creating matching rules:
          Conformer.kUmid == 'umid'
          Conformer.kName == 'name'
          Conformer.kTapeName == 'tapeName'
          Conformer.kUrl == 'url'
          Conformer.kAudioChannels == 'audioChannels'
          Conformer.kDuration == 'duration'
          Conformer.kFramerate == 'framerate'
          Conformer.kFramerateIsNtsc == 'framerateIsNtsc'
          Conformer.kSamplerate == 'samplerate'
          Conformer.kMediaType == 'mediaType'
          Conformer.kMasterMediaType == 'masterMediaType'
          Conformer.kStartTime == 'startTime'
          Conformer.kTimecode == 'timecode'
          Conformer.kWidth == 'width'
          Conformer.kHeight == 'height'

        @return: True for a match, False otherwise; default implementation returns False
        """
        ...

    def conformType(self) -> int:
        """
        self.conformType() -> Get the conform types for which this rule can be used.  The default is kConform.

        @return: one of the constants kConform, kReconnect, kConformAndReconnect
        """
        ...

    def deactivate(self) -> None:
        """
        self.deactivate() -> removes this conform rule from the list of conform rules. Conform operations done after this call will not use the rule.
        """
        ...

    def isNull(self) -> bool:
        """
        self.name() -> should return True if the conform rule is invalid.

        @return: True for invalid, False otherwise
        """
        ...

    def name(self) -> str:
        """
        self.name() -> returns the name of the conform rule (which was passed to the object in it's initializer).

        @return: string
        """
        ...

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...

    Type: Any = None
    kConform: Any = None
    kReconnect: Any = None
    kConformAndReconnect: Any = None
