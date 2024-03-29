"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class Enumeration_Knob(Unsigned_Knob):
    """
    Stores a single value between 0 and some maximum, and manages a
    set of keywords visible to the user. The words themselves are
    displayed on a pulldown list in the user interface, and are written
    to the saved scripts (so that the numerical values can change).
    self.__init__(name, label, items) -> None
    @param name: Name.
    @param label: Label.
    @param items: List of strings.
    Example:
    k = nuke.Enumeration_Knob('MyEnumKnobName', 'MyEnumKnobLabel', ['label1', 'label2'])
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
        self.numValues() -> int

        Return number of values. Deprecated.
        """
        ...

    def enumName(self, n) -> str:
        """
        self.enumName(n) -> string

        Return name of enumeration n. The argument n is an integer and in the range of 0 and numValues. Deprecated.
        """
        ...

    def values(self,) -> list:
        """
        self.values() -> List of strings.
        Return list of items.
        @return: List of strings.
        Example:
        w = nuke.nodes.Write()
        k = w['file_type']
        k.values()
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

    def setValue(self, item: Union[int, str]) -> None:
        """
        self.setValue(item) -> None.
        Set the current value. item will first be converted into a string and matched against the enum values.
        If this fails, it will attempt to be used as an index into the enum.
        @param item: String or Integer.
        @return: None.
        Example:
        w = nuke.nodes.Write()
        k = w['file_type']
        k.setValue('exr')
        """
        ...

    def setValues(self, items: list) -> None:
        """
        self.setValues(items) -> None.
        (Re)initialise knob to the supplied list of items.
        @param items: The new list of values.
        @return: None.
        Example:
        w = nuke.nodes.Write()
        k = w['file_type']
        k.setValues(['exr'])
        """
        ...

    def getDisplayStrFromID(self, ) -> str:
        """
        self.getDisplayStrFromID()
        returns the display text for the associated id
        @param id: the id you want to retrieve the display text for
        @return: String containing the display text, example scene_linear (linear)
        Example:
        displayStr = knob.getDisplayStrFromID('scene_linear')
        """
        ...
