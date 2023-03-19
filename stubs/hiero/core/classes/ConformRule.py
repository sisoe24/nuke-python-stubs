import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class ConformRule(Object):
    """
    Represents a conform rule used by Hiero to make decisions when conforming. Can be derived from in order to make new conform rules.
    """

    def __repr__(self) -> object:
        """
        Return repr(self).
        """
        return object()

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

    def activate(self) -> None:
        """
        self.activate() -> adds this conform rule to the list of conform rules. Conform operations done after this call will use the rule.
        """
        return None

    def appliesToTrackItems(self) -> bool:
        """
        self.appliesToTrackItems() -> should return True if this conform rule applies to track items.

        @return: True or False; default implementation returns True
        """
        return bool()

    def compare(self, media: core.DataCollection, candidateMedia: core.DataCollection) -> bool:
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
        return bool()

    def conformType(self) -> int:
        """
        self.conformType() -> Get the conform types for which this rule can be used.  The default is kConform.

        @return: one of the constants kConform, kReconnect, kConformAndReconnect
        """
        return int()

    def deactivate(self) -> None:
        """
        self.deactivate() -> removes this conform rule from the list of conform rules. Conform operations done after this call will not use the rule.
        """
        return None

    def isNull(self) -> bool:
        """
        self.name() -> should return True if the conform rule is invalid.

        @return: True for invalid, False otherwise
        """
        return bool()

    def name(self) -> str:
        """
        self.name() -> returns the name of the conform rule (which was passed to the object in it's initializer).

        @return: string
        """
        return str()

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        return str()

    def __copy__(self,) -> None:
        """

        """
        return None

    Type: Any = None
    kConform: Any = None
    kReconnect: Any = None
    kConformAndReconnect: Any = None
