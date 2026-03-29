"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class Hash(object):
    """
    A hash value for any number of objects.

    The append() method is used to add objects to the hash; the value will be recomputed efficiently as each new object is added.
    """

    def __new__(cls, *args, **kwargs) -> Hash:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __hash__(self) -> int:
        """
        Return hash(self).
        """
        ...

    def __getattribute__(self, name: str) -> typing.Any:
        """
        Return getattr(self, name).
        """
        ...

    def __setattr__(self, name: str, value: typing.Any) -> None:
        """
        Implement setattr(self, name, value).
        """
        ...

    def __delattr__(self, name: str) -> None:
        """
        Implement delattr(self, name).
        """
        ...

    def __lt__(self, value: typing.Any) -> bool:
        """
        Return self<value.
        """
        ...

    def __le__(self, value: typing.Any) -> bool:
        """
        Return self<=value.
        """
        ...

    def __eq__(self, value: typing.Any) -> bool:
        """
        Return self==value.
        """
        ...

    def __ne__(self, value: typing.Any) -> bool:
        """
        Return self!=value.
        """
        ...

    def __gt__(self, value: typing.Any) -> bool:
        """
        Return self>value.
        """
        ...

    def __ge__(self, value: typing.Any) -> bool:
        """
        Return self>=value.
        """
        ...

    def getHash(self, *args: typing.Any, **kwargs: typing.Any) -> int:
        """
        Get the current value of the hash.
        """
        ...

    def setHash(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Set the current value of the hash.
        """
        ...

    def reset(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Reset the hash.
        """
        ...

    def append(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Add another value to the hash.
        """
        ...

    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
