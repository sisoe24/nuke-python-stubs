from typing import *
from numbers import Number

import nuke

from . import *


class Layer(object):
    """
    A layer is a set of channels.
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def visible(self,) -> bool:
        """
        self.visible() -> bool
        Check whether the layer is visible.

        @return: True if visible, False if not.
        """
        ...

    def name(self,) -> str:
        """
        self.name() -> str
        Get the layer name.

        @return: The layer name, as a string.
        """
        ...

    def setName(self, newName: str) -> None:
        """
        self.setName(newName) -> None
        Set the name of this layer.

        @param newName: The new name for this layer.
        """
        ...

    def channels(self,) -> list:
        """
        self.channels() -> [string, ...]
        Get a list of the channels in this layer.

        @return: A list of strings, where each string is the name of a channel in this layer.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
