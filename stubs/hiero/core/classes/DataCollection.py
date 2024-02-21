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


class DataCollection:
    """
    Storage objects for key/value pairs. Generally used to store metadata.
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

    def __getitem__(self, key, ) -> None:
        """
        Return self[key].
        """
        ...

    def __contains__(self, key, ) -> None:
        """
        Return key in self.
        """
        ...

    def dict(self) -> object:
        """
        self.dict() -> returns a dictionary of key/value pairs. Can be used to iterate over the items in this collection.

        @return: dict
        """
        ...

    def hasKey(self, key: str) -> bool:
        """
        self.hasKey(key) -> returns True if the collection has a value for the key.

        @param key: the key to look up
        @return: True or False
        """
        ...

    def keys(self) -> typing.List[str]:
        """
        self.keys() -> returns keys in the collection.

        @return: list of strings which are keys in the collection
        """
        ...

    def readOnly(self) -> bool:
        """
        self.readOnly(key) -> returns True if the collection can be modified.

        @return: True or False
        """
        ...

    def setValue(self, key: str, value: str) -> None:
        """
        self.setValue(key) -> sets the value of the key stored in this collection.

        @param key: the key to look up
        @param value: value to assign to key
        """
        ...

    def toString(self) -> str:
        """
        self.toString() -> returns a formatted list of the key/value pairs currently set on this object. Equivalent to str(object).

        @return: string
        """
        ...

    def value(self, key: str) -> str:
        """
        self.value(key) -> returns the value of the key stored in this collection. Throws an exception if the key does not exist.

        @param key: the key to look up
        @return: string
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...
