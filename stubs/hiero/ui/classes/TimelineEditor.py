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


class TimelineEditor:
    """
    Object representing the Timeline Editor.
    """

    def __new__(cls, *args, **kwargs) -> TimelineEditor:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def beginSelectionUpdate(self) -> None:
        """
        self.beginSelectionUpdate() -> Call beginSelectionUpdate before, and endSelectionUpdate after, making multiple setSelection.
        """
        ...

    def endSelectionUpdate(self) -> None:
        """
        self.endSelectionUpdate() -> Call beginSelectionUpdate before, and endSelectionUpdate after, making multiple setSelection.
        """
        ...

    def getSelection(self) -> tuple[TrackItem, Transition]:
        """
        Deprecated; please use the selection method instead.

        @return: tuple of TrackItem and Transition objects
        """
        ...

    def selectAll(self) -> None:
        """
        self.selectAll( )

        Select All TrackItems within current sequence.
        """
        ...

    def selectNone(self) -> None:
        """
        self.selectNone( )

        Unselect all TrackItems and Tracks.
        """
        ...

    def selection(self) -> tuple[TrackItem, Transition]:
        """
        self.selection() -> returns a tuple with the currently selected items.

        @return: tuple of TrackItem and Transition objects
        """
        ...

    def sequence(self) -> Sequence:
        """
        self.sequence() -> returns the Sequence currently being edited in the timeline editor.

        @return: Sequence object
        """
        ...

    def setSelection(self, selection: typing.Union[TrackItem, list[TrackItem]]) -> None:
        """
        self.setSelection( hiero.core.TrackItem )
        self.setSelection( [hiero.core.TrackItem] )
        Will throw exception if selection is not subset of current sequence.

        @param selection: track item(s) to be selected.
        """
        ...

    def setTrackSelection(self, selection: typing.Union[TrackBase, list[TrackBase]]) -> None:
        """
        self.setTrackSelection( hiero.core.TrackBase )
        self.setTrackSelection( [hiero.core.TrackBase] )
        Will throw exception if selection is not subset of current sequence.

        @param selection: Tracks to be selected.
        """
        ...

    def window(self) -> PySide2.QtWidgets.QWidget:
        """
        self.window() -> Return the timeline editor window
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...
