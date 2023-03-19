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

    def __setattr__(self, name, value, ):
        """
        Implement setattr(self, name, value).
        """
        return None

    def __delattr__(self, name, ):
        """
        Implement delattr(self, name).
        """
        return None

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def addFile(self) -> None:
        """

        """
        return None

    def addFolder(self) -> None:
        """

        """
        return None

    def allowNodeDelete(self) -> bool:
        """

        """
        return bool()

    def clearResolveEntries(self) -> None:
        """

        """
        return None

    def copy(self) -> None:
        """

        """
        return None

    def cut(self) -> None:
        """

        """
        return None

    def exportRootChanged(self) -> None:
        """

        """
        return None

    def filenameField(self) -> PySide2.QtWidgets.QWidget:
        """

        """
        return Any

    def getWidget(self) -> PySide2.QtWidgets.QWidget:
        """

        """
        return Any

    def handleSelectionChanged(self, selection: PySide2.QtCore.QItemSelection) -> None:
        """

        """
        return None

    def initUI(self) -> None:
        """

        """
        return None

    def itemTypes(self) -> core.ITaskPreset.ItemTypes:
        """

        """
        return core.ITaskPreset.ItemTypes()

    def keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None:
        """
        keyPressEvent(self, event: PySide2.QtGui.QKeyEvent) -> None
        """
        return None

    def paste(self) -> None:
        """

        """
        return None

    def refresh(self) -> None:
        """

        """
        return None

    def refreshContentField(self, element: core.IExportStructureElement) -> None:
        """

        """
        return None

    def removeNode(self) -> None:
        """

        """
        return None

    def selectFileIfOnlyOne(self) -> None:
        """

        """
        return None

    def selectFirstFile(self) -> None:
        """

        """
        return None

    def selection(self) -> core.IExportStructureElement:
        """

        """
        return core.IExportStructureElement()

    def selectionAnchor(self) -> PySide2.QtCore.QPoint:
        """

        """
        return Any

    def selectionRect(self) -> PySide2.QtCore.QRect:
        """

        """
        return Any

    def setAllowNodeDelete(self, allow: bool) -> None:
        """

        """
        return None

    def setExportStructure(self, exportStructure: core.IExportStructure) -> None:
        """

        """
        return None

    def setItemTypes(self, types: core.ITaskPreset.ItemTypes) -> None:
        """

        """
        return None

    def setProject(self, project: core.Project) -> None:
        """

        """
        return None

    def setResolveEntry(self, name: str, value: str, description: str) -> None:
        """

        """
        return None

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
