import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class SpreadsheetView(Object):
    """

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

    def selectAll(self) -> None:
        """
        self.selectAll( )

        Select All TrackItems within current sequence.
        """
        return None

    def selectNone(self) -> None:
        """
        self.selectNone( )

        Unselect all TrackItems.
        """
        return None

    def selection(self) -> object:
        """

        """
        return object()

    def sequence(self) -> object:
        """

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

    def window(self) -> PySide2.QtWidgets.QWidget:
        """
        self.window() -> Return the spreadsheet view window
        """
        return Any

    def __copy__(self,) -> None:
        """

        """
        return None
