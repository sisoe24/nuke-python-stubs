"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class Password_Knob(Knob):
    """
    A knob which holds a password string value. Appears as a password entry field in a Node panel.
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

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def getText(self,) -> str:
        """
        self.getText() -> string

        Return text associated with knob.
        """
        ...

    def value(self,) -> str:
        """
        self.value() -> str

        Get the value of this knob as a string.
        @return: String value.
        """
        ...

    def setValue(self, val, view='default') -> None:
        """
        self.setValue(val, view='default') -> None

        Set value of knob.
        @param val: The new value.
        @param view: Optional parameter specifying which view to set the value for. If omitted, the value will be set for the default view.
        @return: None
        """
        ...
