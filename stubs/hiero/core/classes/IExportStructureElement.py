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


class IExportStructureElement:
    """

    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

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

    def addChild(self, child: hiero.core.IExportStructureElement) -> None:
        """

        """
        ...

    def child(self, index: int) -> hiero.core.IExportStructureElement:
        """

        """
        ...

    def childCount(self) -> int:
        """

        """
        ...

    def childIndex(self, child: hiero.core.IExportStructureElement) -> int:
        """

        """
        ...

    def clearChildren(self) -> None:
        """

        """
        ...

    def createChildFolder(self, name: str) -> hiero.core.IExportStructureElement:
        """

        """
        ...

    def createChildTask(self, name: str) -> hiero.core.IExportStructureElement:
        """

        """
        ...

    def fromXml(self, xml: str) -> None:
        """

        """
        ...

    def isLeaf(self) -> bool:
        """

        """
        ...

    def name(self) -> str:
        """

        """
        ...

    def parent(self) -> hiero.core.IExportStructureElement:
        """

        """
        ...

    def path(self) -> str:
        """

        """
        ...

    def preset(self) -> hiero.core.ITaskPreset:
        """

        """
        ...

    def removeChild(self, child: hiero.core.IExportStructureElement) -> None:
        """

        """
        ...

    def setName(self, name: str) -> None:
        """

        """
        ...

    def setPreset(self, preset: hiero.core.ITaskPreset) -> None:
        """

        """
        ...

    def setPresetType(self, type: str) -> None:
        """

        """
        ...

    def toXml(self) -> str:
        """

        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...
