import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class Version(Object):
    """
    Object representing a version of a clip or sequence. Can be created with a Clip or Sequence object.
    """

    def __repr__(self) -> object:
        """
        Return repr(self).
        """
        return None

    def __hash__(self, ):
        """
        Return hash(self).
        """
        return None

    def __lt__(self, value, ):
        """
        Return self<value.
        """
        return None

    def __le__(self, value, ):
        """
        Return self<=value.
        """
        return None

    def __eq__(self, value, ):
        """
        Return self==value.
        """
        return None

    def __ne__(self, value, ):
        """
        Return self!=value.
        """
        return None

    def __gt__(self, value, ):
        """
        Return self>value.
        """
        return None

    def __ge__(self, value, ):
        """
        Return self>=value.
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

    def guid(self) -> object:
        """

        """
        return None

    def isHidden(self) -> bool:
        """

        """
        return bool()

    def isNull(self) -> bool:
        """
        self.isNull() -> returns True if the object is invalid, False otherwise.

        @return: True or False
        """
        return Union[True, False]

    def item(self) -> None:
        """
        self.item() -> returns the clip or sequence stored with this version.

        @return: hiero.core.Clip or hiero.core.Sequence object
        """
        return Iterable()

    def name(self) -> str:
        """
        self.name() -> returns the name of this version.

        @return: string
        """
        return str()

    def parent(self) -> core.BinItem:
        """
        self.parent() -> returns the bin item that contains this version.

        @return: hiero.core.BinItem object
        """
        return BinItem()

    def serialize(self) -> str:
        """

        """
        return str()

    def setHidden(self, hidden: bool) -> None:
        """

        """
        return None

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        return str()

    def versionIndex(self, *args, **kwargs):
        """
        self.versionIndex() -> returns a string containing the version's index.

        @return: string

        WARNING - DEPRECATED ( versionIndex ): This method is deprecated and will not be present in future versions of the Python API.
        Version indices are no longer unique identifiers and should not be used as such.
        """
        return str()

    def __copy__(self,) -> None:
        """

        """
        return None
