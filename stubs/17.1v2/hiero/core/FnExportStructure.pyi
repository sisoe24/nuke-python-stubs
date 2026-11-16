# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
from typing_extensions import Self
import hiero.core as _hiero_core
import hiero.core.FnExportRegistry as _hiero_core_FnExportRegistry
import hiero.core.FnExporterBase as _hiero_core_FnExporterBase
from hiero.core import IExportStructure as IExportStructure
from hiero.core import IExportStructureElement as IExportStructureElement
from hiero.core import log as log
from hiero.core.FnExporterBase import FolderTaskPreset as FolderTaskPreset
from hiero.core.FnExporterBase import TaskBase as TaskBase
from hiero.core.FnExporterBase import TaskPresetBase as TaskPresetBase
from hiero.core.FnExporterBase import classBasename as classBasename

taskRegistry: _hiero_core_FnExportRegistry.TaskRegistry

class ExportStructure2(_hiero_core.IExportStructure):
    """ExportStructure2 is the implementation of the datastructure used to represent
    the export tree, each node within the tree is represented by an ExportStructureElement.
    Although this matches how the export presets are viewed in the UI, when it comes
    running an export, or persisting the structure, it is flattened into a list
    of paths and task presets.
    """
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def exportRootPath(self) -> str | dict[Any, Any] | list[Any] | tuple[Any, ...] | float | int | dict[bytes, bytes] | None:
        """Returns the exportRootPath, the root of the export into which the export structure is built"""
    def findElementsByPath(self, path: Any) -> list[Any]:
        """Find the elements matching path. Returns a list. """
    def flatten(self) -> list[Any]:
        """Return the hierarchy as a list of (path, preset) tuples"""
    def restore(self, sequence: Any) -> None:
        """Restore the hierarchy from a list of (path, preset) tuples"""
    def rootElement(self) -> ExportStructureElement:
        """Return the root element in this hierarchy.
        The root element is not included in the path generation
        """
    def setExportRootPath(self, rootPath: Any) -> None:
        """Set the exportRootPath, the root of the export into which the export structure is built"""

class ExportStructureElement(_hiero_core.IExportStructureElement):
    """ExportStructureElement represents a node within the export structure"""
    def __bool__(self) -> bool:
        """Implemented because otherwise the __len__ method is used for evaluation
        in boolean contexts. 'if element' should always succeed.
        """
    def __contains__(self, name: Any) -> bool: ...
    def __getitem__(self, index: Any) -> Any: ...
    def __init__(self, name: Any, isFolder: Any) -> None: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...
    def addChild(self, child: Any) -> None:
        """Add a child to this Element"""
    def addPathChangedCallback(self, callback: Any) -> None:
        """Add a callback to be notified when the path of this element has changed,
        callbacks should take the arguments (oldPath, newPath).
        """
    def child(self, index: Any) -> Any:
        """Return a child by index"""
    def childCount(self) -> int:
        """Return the number of children"""
    def childIndex(self, element: Any) -> int:
        """Given a child element, identify and return the index of the child within
        the children array. Returns -1 if child not found.
        """
    def children(self) -> list[Any]:
        """Return a list of children"""
    def clearChildren(self) -> None:
        """Clear all the children"""
    def createChildFolder(self, path: Any) -> Self | ExportStructureElement | None: ...
    def createChildFromPreset(self, path: Any, preset: Any) -> Self | ExportStructureElement | None:
        """Create a child element from a path and existing preset """
    def createChildTask(self, path: Any) -> Self | ExportStructureElement | None: ...
    def findElementsByPath(self, path: Any) -> list[Any]:
        """Search recursively through the element tree finding elements which
        match path. Returns a list.
        """
    def fromXml(self, xml: Any) -> None:
        """Build Child Elements from XML data"""
    def isLeaf(self) -> bool:
        """Returns True if node is flagged as leaf and may not accept children"""
    def name(self) -> Any:
        """Return the name of this Element"""
    def parent(self) -> None:
        """Return the parent element of this Element"""
    def path(self) -> str:
        """Return the path of this Element"""
    def pathChanged(self, oldPath: Any) -> None:
        """Notify children and any observers that the element's path has changed. """
    def preset(self) -> _hiero_core_FnExporterBase.TaskPresetBase | None:
        """Return the preset assigned to this Element. May be None"""
    def removeChild(self, child: Any) -> None:
        """Remove a child from this Element"""
    def setName(self, name: Any) -> None:
        """Set the name of this element. """
    def setPreset(self, preset: Any) -> None:
        """Set the preset assigned to this Element. May be None"""
    def setPresetType(self, identifier: Any) -> None:
        """setPresetType(self, identifier)

        @param identifier: Unique identifier from the Task which is used to associate the preset type
        """
    def toXml(self) -> str:
        """Serialize Element and children to XML"""
