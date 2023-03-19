import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class IExportStructure(Object):
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

    def childElement(self, path: str) -> core.IExportStructureElement:
        """

        """
        return core.IExportStructureElement()

    def exportRootPath(self) -> str:
        """

        """
        return str()

    def rootElement(self) -> core.IExportStructureElement:
        """

        """
        return core.IExportStructureElement()

    def setExportRootPath(self, path: str) -> None:
        """

        """
        return None

    def __copy__(self,) -> None:
        """

        """
        return None
