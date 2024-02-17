"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import ui
import core
import hiero
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class ResolveTable(object):
    """
    Used to store name/value pairs that can be resolved in strings.
    Example: Assuming the resolve table has an item "{filename}" that resolves to example.mov,
    Then calling resolveTable.resolve(taskObject, "someprefix_{filename}") will return "someprefix_example.mov"
    To use, create an object, call addResolver on it with whatever key/value pairs you want, and then you can call resolve on the object to resolve a string.
    You can also merge two ResolveTable objects, replacing existing key's with those in the ResolveTable passed in.
    And you can use functions to do the resolve. These take one parameter, the task that the resolve is applying to.
    For an example of how to use this, see FnExporterBase.py.
    """
    StringItem: Any = None
    CallbackItem: Any = None

    def __init__(self) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def duplicate(self) -> None:
        """

        """
        ...

    def entries(self) -> None:
        """

        """
        ...

    def entryCount(self) -> None:
        """
        self.entryCount() -> returns the number of entries in this resolver.
        """
        ...

    def entryName(self, index) -> None:
        """
        self.entryCount(index) -> returns the name of the entry based on the index.
        """
        ...

    def entryDescription(self, index) -> None:
        """
        self.entryDescription(index) -> returns a description of the item, which can be used to populate a dialog to the user when they are picking keywords.
        """
        ...

    def addResolver(self, name, description, resolver) -> None:
        """

        """
        ...

    def merge(self, resolver) -> None:
        """

        """
        ...

    def pathSensitiveReplace(self, initialString, findValue, replaceValue, isPath) -> None:
        """

        """
        ...

    def resolve(self, task, value, isPath=False) -> None:
        """

        """
        ...

    def addEntriesToExportStructureViewer(self, viewer) -> None:
        """

        """
        ...

    @property
    def __dict__(self) -> typing.Any:
        """
        dictionary for instance variables (if defined)
        """
        ...

    @property
    def __weakref__(self) -> typing.Any:
        """
        list of weak references to the object (if defined)
        """
        ...
