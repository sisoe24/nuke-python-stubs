"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class SceneGraph_Knob(Unsigned_Knob):
    """
    Displays a list of items as a hierarchy.
    The hierarchy is specified using back or forward slashes within the item names
    to specify their level in the tree. Handles multiple selection of items within the tree.
    """

    def __new__(cls, *args, **kwargs) -> SceneGraph_Knob:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __hash__(self) -> int:
        """
        Return hash(self).
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def getItems(self) -> tuple[tuple[str, str], ...]:
        """
        self.getItems() -> tuple of strings (name, type)

        Returns a tuple of string tuples (name, type).
        """
        ...

    def setItems(self, items: list[tuple[str, str]], autoSelect: bool = False) -> None:
        """
        self.setItems([(name1, type1), (name2, type2), ...], autoSelect=false) -> None

        Sets the list of items that can be selected on the knob.

        :param items: sequence of string tuples (name, type) .
        :param autoSelect: If True, all items are automatically set as imported and selected.
        :return: None.
        """
        ...

    def addItems(self, items: list[tuple[str, str]], autoSelect: bool = False) -> None:
        """
        self.addItems([(name1, type1), (name2, type2), ...], autoSelect=false) -> None\n

        Adds to the existing list of items that can be selected on the knob.

        :param items: sequence of string tuples (name, type) .
        :param autoSelect: If True, all items are automatically set as selected.
        :return: None.
        """
        ...

    def removeItems(self, names: list[str]) -> None:
        """
        self.removeItems([name1, name2, ...]) -> None

        Removes a list of string names from the knob.
        """
        ...

    def getSelectedItems(self) -> list[str]:
        """
        self.getSelectedItems() -> list

        :return: list of strings containing all currently selected items in the knob.
        """
        ...

    def setSelectedItems(self, items: list[str]) -> None:
        """
        self.setSelectedItems([name1, name2, ...]) -> None

        :param items: sequence of strings - names of the items in the list .
        :return: None.
        """
        ...
