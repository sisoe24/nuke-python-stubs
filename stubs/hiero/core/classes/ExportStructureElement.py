import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class ExportStructureElement(IExportStructureElement):
    """
    ExportStructureElement represents a node within the export structure
    """

    def __init__(self, name, isFolder):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def preset(self):
        """
        Return the preset assigned to this Element. May be None
        """
        return None

    def setPreset(self, preset):
        """
        Set the preset assigned to this Element. May be None
        """
        return None

    def setPresetType(self, identifier: Any):
        """
        setPresetType(self, identifier)

        @param identifier: Unique identifier from the Task which is used to associate the preset type
        """
        return None

    def path(self):
        """
        Return the path of this Element
        """
        return None

    def name(self):
        """
        Return the name of this Element
        """
        return None

    def setName(self, name):
        """
        Set the name of this element.
        """
        return None

    def pathChanged(self, oldPath):
        """
        Notify children and any observers that the element's path has changed.
        """
        return None

    def addPathChangedCallback(self, callback):
        """
        Add a callback to be notified when the path of this element has changed,
        callbacks should take the arguments (oldPath, newPath).
        """
        return None

    def isLeaf(self):
        """
        Returns True if node is flagged as leaf and may not accept children
        """
        return None

    def parent(self):
        """
        Return the parent element of this Element
        """
        return None

    def _setParent(self, parent):
        """
        Set the parent element of this Element. Note: this is an internal method
        and should not be called directly. Elements should be added to a parent by
        calling parent.addChild()
        """
        return None

    def childIndex(self, element):
        """
        Given a child element, identify and return the index of the child within
        the children array. Returns -1 if child not found.
        """
        return None

    def child(self, index):
        """
        Return a child by index
        """
        return None

    def children(self):
        """
        Return a list of children
        """
        return None

    def childCount(self):
        """
        Return the number of children
        """
        return None

    def __bool__(self):
        """
        Implemented because otherwise the __len__ method is used for evaluation
        in boolean contexts. 'if element' should always succeed.
        """
        return None

    def __len__(self):
        """

        """
        return None

    def __contains__(self, name):
        """

        """
        return None

    def __getitem__(self, index):
        """

        """
        return None

    def __repr__(self):
        """
        Return repr(self).
        """
        return None

    def findElementsByPath(self, path):
        """
        Search recursively through the element tree finding elements which
        match path. Returns a list.
        """
        return None

    def addChild(self, child):
        """
        Add a child to this Element
        """
        return None

    def _createChildren(self, path, isFolder, preset=None):
        """
        Create and add a child element. If path has / separators, recursively
        adds children. Returns the final created element.
        """
        return None

    def createChildFolder(self, path):
        """

        """
        return None

    def createChildTask(self, path):
        """

        """
        return None

    def createChildFromPreset(self, path, preset):
        """
        Create a child element from a path and existing preset
        """
        return None

    def removeChild(self, child):
        """
        Remove a child from this Element
        """
        return None

    def clearChildren(self):
        """
        Clear all the children
        """
        return None

    def toXml(self):
        """
        Serialize Element and children to XML
        """
        return None

    def _toXml(self, parent):
        """

        """
        return None

    def fromXml(self, xml):
        """
        Build Child Elements from XML data
        """
        return None

    def _fromXml(self, element):
        """

        """
        return None
