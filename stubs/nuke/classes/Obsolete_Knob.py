"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class Obsolete_Knob(Knob):
    """
    For internal use only.
    """

    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def value(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return value at the current frame for channel 'c'.
        """
        ...

    def setValue(self, val, chan) -> bool:
        """
        self.setValue(val, chan) -> bool

        Sets the value 'val' at channel 'chan'.
        @return: True if successful, False if not.
        """
        ...
