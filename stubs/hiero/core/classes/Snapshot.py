import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class Snapshot(object):
    """
    Object representing a snapshot of a sequence or clip. Can be created with a Clip or a Sequence object.
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

    def comment(self) -> str:
        """
        self.comment() -> returns the comment set on this snapshot object.

        @return: string
        """
        ...

    def isNull(self) -> bool:
        """
        self.isNull() -> returns True if the object is invalid, False otherwise.

        @return: True or False
        """
        ...

    def item(self) -> None:
        """
        self.item() -> returns the clip or sequence stored with this snapshot.

        @return: hiero.core.Clip or hiero.core.Sequence object
        """
        ...

    def name(self) -> str:
        """
        self.name() -> returns the name of this snapshot.

        @return: string
        """
        ...

    def setComment(self, comment: str) -> None:
        """
        self.setComment(comment) -> sets the comment on this snapshot object.

        @param comment: string to set the comment to
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
