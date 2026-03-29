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


class TracksMask:
    """

    """

    def __new__(cls, *args, **kwargs) -> 'TracksMask':
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __lt__(self, value: 'TracksMask') -> bool:
        """
        Return self<value.
        """
        ...

    def __le__(self, value: 'TracksMask') -> bool:
        """
        Return self<=value.
        """
        ...

    def __eq__(self, value: 'TracksMask') -> bool:
        """
        Return self==value.
        """
        ...

    def __ne__(self, value: 'TracksMask') -> bool:
        """
        Return self!=value.
        """
        ...

    def __gt__(self, value: 'TracksMask') -> bool:
        """
        Return self>value.
        """
        ...

    def __ge__(self, value: 'TracksMask') -> bool:
        """
        Return self>=value.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def setTracks(self, tracks: typing.List[core.VideoTrack]) -> None:
        """

        """
        ...

    def setVisibleByDefault(self, visibleByDefault: bool) -> None:
        """

        """
        ...

    def tracks(self) -> typing.List[core.VideoTrack]:
        """

        """
        ...

    def visibleByDefault(self) -> bool:
        """

        """
        ...

    __hash__: Any = None
