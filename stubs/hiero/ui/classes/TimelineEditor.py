import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class TimelineEditor(Object):
    """
    Object representing the Timeline Editor.
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

    def beginSelectionUpdate(self) -> None:
        """
        self.beginSelectionUpdate() -> Call beginSelectionUpdate before, and endSelectionUpdate after, making multiple setSelection.
        """
        return None

    def endSelectionUpdate(self) -> None:
        """
        self.endSelectionUpdate() -> Call beginSelectionUpdate before, and endSelectionUpdate after, making multiple setSelection.
        """
        return None

    def getSelection(self) -> object:
        """
        Deprecated; please use the selection method instead.

        @return: tuple of TrackItem and Transition objects
        """
        return object()

    def selectAll(self) -> None:
        """
        self.selectAll( )

        Select All TrackItems within current sequence.
        """
        return None

    def selectNone(self) -> None:
        """
        self.selectNone( )

        Unselect all TrackItems and Tracks.
        """
        return None

    def selection(self) -> object:
        """
        self.selection() -> returns a tuple with the currently selected items.

        @return: tuple of TrackItem and Transition objects
        """
        return object()

    def sequence(self) -> object:
        """
        self.sequence() -> returns the Sequence currently being edited in the timeline editor.

        @return: Sequence object
        """
        return object()

    def setSelection(self, *args, **kwargs):
        """
        self.setSelection( hiero.core.TrackItem )
        self.setSelection( [hiero.core.TrackItem] )
        Will throw exception if selection is not subset of current sequence.

        @param selection: track item(s) to be selected.
        """
        return None

    def setTrackSelection(self, *args, **kwargs):
        """
        self.setTrackSelection( hiero.core.TrackBase )
        self.setTrackSelection( [hiero.core.TrackBase] )
        Will throw exception if selection is not subset of current sequence.

        @param selection: Tracks to be selected.
        """
        return None

    def window(self) -> PySide2.QtWidgets.QWidget:
        """
        self.window() -> Return the timeline editor window
        """
        return Any

    def __copy__(self,) -> None:
        """

        """
        return None
