"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class Pulldown_Knob(Enumeration_Knob):
    """
    Pulldown_Knob
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

    def numValues(self,) -> int:
        """
        numValues() -> int

        Return number of values.
        """
        ...

    def itemName(self, n) -> str:
        """
        itemName(n) -> string

        Return name of item n. The argument n is an integer and in the range of 0 and numValues.
        """
        ...

    def commands(self, n) -> str:
        """
        commands(n) -> string

        Return command n. The argument n is an integer and in the range of 0 and numValues.
        """
        ...

    def value(self,) -> str:
        """
        self.value() -> String.
        Current value.
        @return: String.
        Example:
        w = nuke.nodes.Write()
        k = w['file_type']
        k.value()
        """
        ...

    def setValues(self, items: str) -> None:
        """
        self.setValues(items) -> None.
        (Re)initialise knob to the list of items.
        @param items: Dictionary of name/value pairs.
        @param sort: Optional parameter as to whether to sort the names.
        @return: None.
        Example:
        w = nuke.nodes.NoOp()
        k = nuke.Pulldown_Knob('kname', 'klabel')
        k.setValues({'label/command' : 'eval("3*2")'})
        w.addKnob(k)
        k = w['kname']
        """
        ...
