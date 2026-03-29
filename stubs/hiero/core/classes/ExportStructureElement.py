"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import ui
import core
import nuke
import hiero
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class ExportStructureElement(IExportStructureElement):
    """
    ExportStructureElement represents a node within the export structure
    """

    def __init__(self, name: str, isFolder: bool) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def preset(self) -> Optional[Any]:
        """
        Return the preset assigned to this Element. May be None
        """
        ...

    def setPreset(self, preset: Optional[Any]) -> None:
        """
        Set the preset assigned to this Element. May be None
        """
        ...

    def setPresetType(self, identifier: str) -> None:
        """
        setPresetType(self, identifier)

        @param identifier: Unique identifier from the Task which is used to associate the preset type
        """
        ...

    def path(self) -> str:
        """
        Return the path of this Element
        """
        ...

    def name(self) -> str:
        """
        Return the name of this Element
        """
        ...

    def setName(self, name: str) -> None:
        """
        Set the name of this element.
        """
        ...

    def pathChanged(self, oldPath: str) -> None:
        """
        Notify children and any observers that the element's path has changed.
        """
        ...

    def addPathChangedCallback(self, callback: Callable[[str, str], None]) -> None:
        """
        Add a callback to be notified when the path of this element has changed,
        callbacks should take the arguments (oldPath, newPath).
        """
        ...

    def isLeaf(self) -> bool:
        """
        Returns True if node is flagged as leaf and may not accept children
        """
        ...

    def parent(self) -> Optional[ExportStructureElement]:
        """
        Return the parent element of this Element
        """
        ...

    def _setParent(self, parent: Optional[ExportStructureElement]) -> None:
        """
        Set the parent element of this Element. Note: this is an internal method
        and should not be called directly. Elements should be added to a parent by
        calling parent.addChild()
        """
        ...

    def childIndex(self, element: ExportStructureElement) -> int:
        """
        Given a child element, identify and return the index of the child within
        the children array. Returns -1 if child not found.
        """
        ...

    def child(self, index: int) -> Optional[ExportStructureElement]:
        """
        Return a child by index
        """
        ...

    def children(self) -> List[ExportStructureElement]:
        """
        Return a list of children
        """
        ...

    def childCount(self) -> int:
        """
        Return the number of children
        """
        ...

    def __bool__(self) -> bool:
        """
        Implemented because otherwise the __len__ method is used for evaluation
        in boolean contexts. 'if element' should always succeed.
        """
        ...

    def __len__(self) -> None:
        """

        """
        ...

    def __contains__(self, name) -> None:
        """

        """
        ...

    def __getitem__(self, index) -> None:
        """

        """
        ...

    def __repr__(self) -> str:
        """
        Return repr(self).
        """
        ...

    def findElementsByPath(self, path: str) -> List[ExportStructureElement]:
        """
        Search recursively through the element tree finding elements which
        match path. Returns a list.
        """
        ...

    def addChild(self, child: ExportStructureElement) -> None:
        """
        Add a child to this Element
        """
        ...

    def _createChildren(self, path: str, isFolder: bool, preset: Optional[Any] = None) -> ExportStructureElement:
        """
        Create and add a child element. If path has / separators, recursively
        adds children. Returns the final created element.
        """
        ...

    def createChildFolder(self, path) -> None:
        """

        """
        ...

    def createChildTask(self, path) -> None:
        """

        """
        ...

    def createChildFromPreset(self, path: str, preset: Optional[Any]) -> None:
        """
        Create a child element from a path and existing preset
        """
        ...

    def removeChild(self, child: ExportStructureElement) -> None:
        """
        Remove a child from this Element
        """
        ...

    def clearChildren(self) -> None:
        """
        Clear all the children
        """
        ...

    def toXml(self) -> str:
        """
        Serialize Element and children to XML
        """
        ...

    def _toXml(self, parent) -> None:
        """

        """
        ...

    def fromXml(self, xml: str) -> None:
        """
        Build Child Elements from XML data
        """
        ...

    def _fromXml(self, element) -> None:
        """

        """
        ...
