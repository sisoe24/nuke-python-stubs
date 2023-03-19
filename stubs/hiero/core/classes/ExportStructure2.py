import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class ExportStructure2(IExportStructure):
    """
    ExportStructure2 is the implementation of the datastructure used to represent
    the export tree, each node within the tree is represented by an ExportStructureElement.
    Although this matches how the export presets are viewed in the UI, when it comes
    running an export, or persisting the structure, it is flattened into a list
    of paths and task presets.
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def rootElement(self):
        """
        Return the root element in this hierarchy.
        The root element is not included in the path generation
        """
        return None

    def findElementsByPath(self, path):
        """
        Find the elements matching path. Returns a list.
        """
        return None

    def exportRootPath(self):
        """
        Returns the exportRootPath, the root of the export into which the export structure is built
        """
        return None

    def setExportRootPath(self, rootPath):
        """
        Set the exportRootPath, the root of the export into which the export structure is built
        """
        return None

    def _fromXml(self, element):
        """

        """
        return None

    def _toXml(self, parent):
        """

        """
        return None

    def restore(self, sequence):
        """
        Restore the hierarchy from a list of (path, preset) tuples
        """
        return None

    def _traverse(self, element):
        """
        Helper for flatten. Recursively traverse the structure, building a list
        of (path, preset) tuples for each element with no children.
        """
        return None

    def flatten(self):
        """
        Return the hierarchy as a list of (path, preset) tuples
        """
        return None

    def __repr__(self):
        """
        Return repr(self).
        """
        return None
