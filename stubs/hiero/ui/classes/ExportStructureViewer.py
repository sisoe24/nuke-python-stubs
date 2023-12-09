import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class ExportStructureViewer(QWidget):
    """
    QWidget(self, parent: typing.Optional[PySide2.QtWidgets.QWidget] = None, f: PySide2.QtCore.Qt.WindowFlags = Default(Qt.WindowFlags)) -> None
    """

    def __setattr__(self, name, value, ) -> None:
        """
        Implement setattr(self, name, value).
        """
        ...

    def __delattr__(self, name, ) -> None:
        """
        Implement delattr(self, name).
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def addFile(self) -> None:
        """

        """
        ...

    def addFolder(self) -> None:
        """

        """
        ...

    def allowNodeDelete(self) -> bool:
        """

        """
        ...

    def clearResolveEntries(self) -> None:
        """

        """
        ...

    def copy(self) -> None:
        """

        """
        ...

    def cut(self) -> None:
        """

        """
        ...

    def exportRootChanged(self) -> None:
        """

        """
        ...

    def filenameField(self) -> PySide2.QtWidgets.QWidget:
        """

        """
        ...

    def getWidget(self) -> PySide2.QtWidgets.QWidget:
        """

        """
        ...

    def handleSelectionChanged(self, selection: PySide2.QtCore.QItemSelection) -> None:
        """

        """
        ...

    def initUI(self) -> None:
        """

        """
        ...

    def itemTypes(self) -> core.ITaskPreset.ItemTypes:
        """

        """
        ...

    def keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None:
        """
        keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None
        """
        ...

    def paste(self) -> None:
        """

        """
        ...

    def refresh(self) -> None:
        """

        """
        ...

    def refreshContentField(self, element: core.IExportStructureElement) -> None:
        """

        """
        ...

    def removeNode(self) -> None:
        """

        """
        ...

    def selectFileIfOnlyOne(self) -> None:
        """

        """
        ...

    def selectFirstFile(self) -> None:
        """

        """
        ...

    def selection(self) -> core.IExportStructureElement:
        """

        """
        ...

    def selectionAnchor(self) -> PySide2.QtCore.QPoint:
        """

        """
        ...

    def selectionRect(self) -> PySide2.QtCore.QRect:
        """

        """
        ...

    def setAllowNodeDelete(self, allow: bool) -> None:
        """

        """
        ...

    def setExportStructure(self, exportStructure: core.IExportStructure) -> None:
        """

        """
        ...

    def setItemTypes(self, types: core.ITaskPreset.ItemTypes) -> None:
        """

        """
        ...

    def setProject(self, project: core.Project) -> None:
        """

        """
        ...

    def setResolveEntry(self, name: str, value: str, description: str) -> None:
        """

        """
        ...

    EditMode: Any = None
    Full: Any = None
    Limited: Any = None
    ReadOnly: Any = None
    selectionChanged = Signal()
    structureModified = Signal()
    kAddFolderToolTip = 'Adds a new directory to your export structure'
    kAddFileToolTip = 'Adds new file entry to the export structure'
    kRemoveToolTip = 'Deletes the selected file entry from the export structure'
    kStructurePathToolTip = 'This structure defines the path into which the exported content will be written. See the tokens listed within the tooltip to build unique paths for each item exported.'
    kStructureContentToolTip = 'The content written into the structure is defined by the export task selected here.'
    staticMetaObject: Any = None
