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


class BinView:
    """
    Object representing the Bin View. Passed as the sender object to the event handler callbacks registered for hiero.core.events.EventType.kShowContextMenu type events. Can also be retrieved using hiero.ui.currentContextMenuView when active during the context menu events.
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

    def getSelection(self) -> object:
        """
        Deprecated; please use the selection method instead.

        @return: tuple of hiero.core.BinItem objects
        """
        ...

    def selection(self) -> object:
        """
        self.selection() -> returns a tuple with the currently selected items.

        @return: tuple of hiero.core.BinItem objects
        """
        ...

    def window(self) -> PySide2.QtWidgets.QWidget:
        """
        self.window() -> Return the bin view window
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...
