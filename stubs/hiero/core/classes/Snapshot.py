import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class Snapshot(Object):
    """
    Object representing a snapshot of a sequence or clip. Can be created with a Clip or a Sequence object.
    """

    def __repr__(self) -> object:
        """
        Return repr(self).
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

    def comment(self) -> str:
        """
        self.comment() -> returns the comment set on this snapshot object.

        @return: string
        """
        return str()

    def isNull(self) -> bool:
        """
        self.isNull() -> returns True if the object is invalid, False otherwise.

        @return: True or False
        """
        return Union[True, False]

    def item(self) -> None:
        """
        self.item() -> returns the clip or sequence stored with this snapshot.

        @return: hiero.core.Clip or hiero.core.Sequence object
        """
        return Iterable()

    def name(self) -> str:
        """
        self.name() -> returns the name of this snapshot.

        @return: string
        """
        return str()

    def setComment(self, comment: str) -> None:
        """
        self.setComment(comment) -> sets the comment on this snapshot object.

        @param comment: string to set the comment to
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
