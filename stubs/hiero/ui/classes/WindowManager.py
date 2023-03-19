import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class WindowManager(Object):
    """
    Global object to handle window management in Hiero. Use hiero.ui.windowManager() to get the single instance of this object to use.
    """

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def addWindow(self, *args, **kwargs):
        """
        self.addWindow(window, section, shortcut) -> adds a window to the window manager and insert a menu item for it into the Window menu. This will also make the window dockable with Hiero's other windows.

        @param window: QWidget object for the window
        @param section: section (either an int, or a WindowManager.WindowMenuSection) to insert the menu item into
        @param shortcut: shortcut to apply to the menu item. See the documentation on QKeySequence for more info
        """
        return Any

    def popupWindow(self, w: PySide2.QtWidgets.QWidget) -> None:
        """
        self.popupWindow(window) -> Opens the window in a floating dock panel.

        @param window: QWidget object for the window
        """
        return None

    def showWindow(self, w: PySide2.QtWidgets.QWidget) -> None:
        """
        self.showWindow(window) -> Opens the window in its layout position or if as a floating dock panel

        @param window: QWidget object for the window
        """
        return None

    def windows(self) -> typing.List*args:
        """
        self.windows() -> Returns a list with the available widgets in WindowManager

        @return: list of the available widgets in WindowManager
        """
        return list()

    def __copy__(self,) -> None:
        """

        """
        return None

    WindowMenuSection: Any = None
    kQAToolsSection: Any = None
    kApplicationSection: Any = None
    kDocumentSection: Any = None
    kNumGroups: Any = None

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None
