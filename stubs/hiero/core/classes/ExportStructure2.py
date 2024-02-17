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


class ExportStructure2(IExportStructure):
    """
    ExportStructure2 is the implementation of the datastructure used to represent
    the export tree, each node within the tree is represented by an ExportStructureElement.
    Although this matches how the export presets are viewed in the UI, when it comes
    running an export, or persisting the structure, it is flattened into a list
    of paths and task presets.
    """

    def __init__(self) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def rootElement(self) -> None:
        """
        Return the root element in this hierarchy.
        The root element is not included in the path generation
        """
        ...

    def findElementsByPath(self, path) -> None:
        """
        Find the elements matching path. Returns a list.
        """
        ...

    def exportRootPath(self) -> None:
        """
        Returns the exportRootPath, the root of the export into which the export structure is built
        """
        ...

    def setExportRootPath(self, rootPath) -> None:
        """
        Set the exportRootPath, the root of the export into which the export structure is built
        """
        ...

    def _fromXml(self, element) -> None:
        """

        """
        ...

    def _toXml(self, parent) -> None:
        """

        """
        ...

    def restore(self, sequence) -> None:
        """
        Restore the hierarchy from a list of (path, preset) tuples
        """
        ...

    def _traverse(self, element) -> None:
        """
        Helper for flatten. Recursively traverse the structure, building a list
        of (path, preset) tuples for each element with no children.
        """
        ...

    def flatten(self) -> None:
        """
        Return the hierarchy as a list of (path, preset) tuples
        """
        ...

    def __repr__(self) -> None:
        """
        Return repr(self).
        """
        ...
