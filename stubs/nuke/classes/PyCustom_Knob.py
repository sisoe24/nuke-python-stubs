"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class PyCustom_Knob(Script_Knob):
    """
    PyCustom_Knob
    """

    def __new__(cls, *args, **kwargs) -> PyCustom_Knob:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __hash__(self) -> int:
        """
        Return hash(self).
        """
        ...

    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def getObject(self, *args: typing.Any, **kwargs: typing.Any) -> PyCustom_Knob:
        """
        Returns the custom knob object as created in the by the 'command' argument to the PyCuston_Knob constructor.
        """
        ...
