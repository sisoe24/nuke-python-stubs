import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class IExportStructureElement(Object):
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

    def addChild(self, child: core.IExportStructureElement) -> None:
        """

        """
        ...

    def child(self, index: int) -> core.IExportStructureElement:
        """

        """
        ...

    def childCount(self) -> int:
        """

        """
        ...

    def childIndex(self, child: core.IExportStructureElement) -> int:
        """

        """
        ...

    def clearChildren(self) -> None:
        """

        """
        ...

    def createChildFolder(self, name: str) -> core.IExportStructureElement:
        """

        """
        ...

    def createChildTask(self, name: str) -> core.IExportStructureElement:
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

    def parent(self) -> core.IExportStructureElement:
        """

        """
        ...

    def path(self) -> str:
        """

        """
        ...

    def preset(self) -> core.ITaskPreset:
        """

        """
        ...

    def removeChild(self, child: core.IExportStructureElement) -> None:
        """

        """
        ...

    def setName(self, name: str) -> None:
        """

        """
        ...

    def setPreset(self, preset: core.ITaskPreset) -> None:
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
