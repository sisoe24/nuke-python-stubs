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

    def addChild(self, child: core.IExportStructureElement) -> None:
        """

        """
        return None

    def child(self, index: int) -> core.IExportStructureElement:
        """

        """
        return core.IExportStructureElement()

    def childCount(self) -> int:
        """

        """
        return int()

    def childIndex(self, child: core.IExportStructureElement) -> int:
        """

        """
        return int()

    def clearChildren(self) -> None:
        """

        """
        return None

    def createChildFolder(self, name: str) -> core.IExportStructureElement:
        """

        """
        return core.IExportStructureElement()

    def createChildTask(self, name: str) -> core.IExportStructureElement:
        """

        """
        return core.IExportStructureElement()

    def fromXml(self, xml: str) -> None:
        """

        """
        return None

    def isLeaf(self) -> bool:
        """

        """
        return bool()

    def name(self) -> str:
        """

        """
        return str()

    def parent(self) -> core.IExportStructureElement:
        """

        """
        return core.IExportStructureElement()

    def path(self) -> str:
        """

        """
        return str()

    def preset(self) -> core.ITaskPreset:
        """

        """
        return core.ITaskPreset()

    def removeChild(self, child: core.IExportStructureElement) -> None:
        """

        """
        return None

    def setName(self, name: str) -> None:
        """

        """
        return None

    def setPreset(self, preset: core.ITaskPreset) -> None:
        """

        """
        return None

    def setPresetType(self, type: str) -> None:
        """

        """
        return None

    def toXml(self) -> str:
        """

        """
        return str()

    def __copy__(self,) -> None:
        """

        """
        return None
