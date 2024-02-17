"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class FreeType_Knob(Knob):
    """
    A knob which holds a font family and style name.
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def getValue(self,) -> str:
        """
        self.getValue() -> [String, String]

        Returns the font family/style on this knob.

        :return: [String, String].
        """
        ...

    def setValue(self, family: str, style: str) -> None:
        """
        self.setValue(family,style) -> None.

        Change font family/style with a new one.

        :param family: String of the font family name.
        :param style: String of the font style name.
        :param filename: Font filename.
        :param index: Face index.
        :raises: It raises an exception if the font is not available.
        :return: None.
        """
        ...
