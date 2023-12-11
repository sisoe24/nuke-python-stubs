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

    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def __lt__(self, value, ) -> None:
        """
        Return self<value.
        """
        ...

    def __le__(self, value, ) -> None:
        """
        Return self<=value.
        """
        ...

    def __eq__(self, value, ) -> None:
        """
        Return self==value.
        """
        ...

    def __ne__(self, value, ) -> None:
        """
        Return self!=value.
        """
        ...

    def __gt__(self, value, ) -> None:
        """
        Return self>value.
        """
        ...

    def __ge__(self, value, ) -> None:
        """
        Return self>=value.
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

    def guid(self) -> object:
        """

        """
        ...

    def isHidden(self) -> bool:
        """

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
        self.item() -> returns the clip or sequence stored with this version.

        @return: hiero.core.Clip or hiero.core.Sequence object
        """
        ...

    def name(self) -> str:
        """
        self.name() -> returns the name of this version.

        @return: string
        """
        ...

    def parent(self) -> core.BinItem:
        """
        self.parent() -> returns the bin item that contains this version.

        @return: hiero.core.BinItem object
        """
        ...

    def serialize(self) -> str:
        """

        """
        ...

    def setHidden(self, hidden: bool) -> None:
        """

        """
        ...

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        ...

    def versionIndex(self, *args, **kwargs) -> str:
        """
        self.versionIndex() -> returns a string containing the version's index.

        @return: string

        WARNING - DEPRECATED ( versionIndex ): This method is deprecated and will not be present in future versions of the Python API.
        Version indices are no longer unique identifiers and should not be used as such.
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...
