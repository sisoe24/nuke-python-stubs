import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class UndoGroup(Object):
    """
    Helper class for beginning and ending undo on a project. Recommended usage is to create with hiero.core.Project.beginUndo(name), using a with block for exception safety to ensure Project.endUndo() is called.

    For example:
        with project.beginUndo('My Undo'):
        // Undoable edits
    """

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

    def __enter__(self) -> None:
        """
        self.__enter__() -> Allows usage in a with block to automatically end the undo.
        """
        return None

    def __exit__(self, arg__1: object, arg__2: object, arg__3: object) -> None:
        """
        self.__exit__() -> Calls self.endUndo().  This allows usage in a with block to automatically end the undo.
        """
        return Any

    def beginUndo(self) -> None:
        """
        self.beginUndo() -> starts a new undo action on the project with the initialised name.  See hiero.core.Project.beginUndo()
        """
        return None

    def endUndo(self) -> None:
        """
        self.endUndo() -> ends the undo action on the project
        """
        return None

    def isNull(self) -> bool:
        """

        """
        return bool()

    def __copy__(self,) -> None:
        """

        """
        return None
