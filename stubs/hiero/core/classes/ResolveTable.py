import typing
from typing import *
from numbers import Number

import core
import PySide2

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

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def duplicate(self):
        """

        """
        return None

    def entries(self):
        """

        """
        return None

    def entryCount(self):
        """
        self.entryCount() -> returns the number of entries in this resolver.
        """
        return None

    def entryName(self, index):
        """
        self.entryCount(index) -> returns the name of the entry based on the index.
        """
        return None

    def entryDescription(self, index):
        """
        self.entryDescription(index) -> returns a description of the item, which can be used to populate a dialog to the user when they are picking keywords.
        """
        return None

    def addResolver(self, name, description, resolver):
        """

        """
        return None

    def merge(self, resolver):
        """

        """
        return None

    def pathSensitiveReplace(self, initialString, findValue, replaceValue, isPath):
        """

        """
        return None

    def resolve(self, task, value, isPath=False):
        """

        """
        return None

    def addEntriesToExportStructureViewer(self, viewer):
        """

        """
        return None

    @property
    def __dict__(self) -> Any:
        """
        dictionary for instance variables (if defined)
        """
        return None

    @property
    def __weakref__(self) -> Any:
        """
        list of weak references to the object (if defined)
        """
        return None
