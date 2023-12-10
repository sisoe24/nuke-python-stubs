from typing import *
from numbers import Number

import nuke

from . import *

class SceneView_Knob(Unsigned_Knob):
    """
    Displays a list of items as a hierarchy.
    The hierarchy is specified using back or forward slashes within the item names
    to specify their level in the tree. Handles multiple selection of items within the tree.
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

    def __new__(self,*args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def getImportedItems(self,) -> list:
        """
        self.getImportedItems() -> list

        Returns a list of strings containing all items imported into the knob.
        """
        ...

    def setImportedItems(self, items:list) -> None:
        """
        self.setImportedItems(items) -> None\n

        Sets a list of strings containing all items imported into the knob. This will overwrite the current imported items list.

        :param items: List of imported items.
        :return: None.
        """
        ...

    def getAllItems(self,) -> list:
        """
        self.getAllItems() -> list

        Returns a list of strings containing all items that the knob can import.
        """
        ...

    def setAllItems(self, items:list, autoSelect:bool) -> None:
        """
        self.setAllItems(items, autoSelect) -> None

        Sets a list of strings containing all items that the knob can import.
        After calling this function, only items from this list can be imported into the nosde.

        :param items: List of imported items.
        :param autoSelect: If True, all items are automatically set as imported and selected.
        :return: None.
        """
        ...

    def addItems(self,) -> None:
        """
        self.addItems() -> None

        Adds a list of string items to the knob. New items are automatically set as imported and selected.
        """
        ...

    def removeItems(self,) -> None:
        """
        self.removeItems() -> None

        Removes a list of string items from the knob.
        """
        ...

    def getSelectedItems(self,) -> list:
        """
        self.getSelectedItems() -> list

        Returns a list of strings containing all currently selected items in the knob.
        """
        ...

    def setSelectedItems(self,) -> None:
        """
        self.setSelectedItems() -> None

        Takes a list of strings of items contained in the knob and sets them as selected.
        """
        ...

    def getHighlightedItem(self,) -> str:
        """
        self.getHighlightedItem() -> string

        Returns a string containing the item which is currently highlighted.
        """
        ...
