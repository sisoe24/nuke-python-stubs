"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import ui
import core
import hiero
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class AnnotationElement(Object):
    """
    Base class for types of elements that may be added to an Annotation.
    This class should not be used directly and AnnotationElement objects should not be created.
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

    def __bool__(self, ) -> None:
        """
        True if self else False
        """
        ...

    def color(self) -> object:
        """
        self.color() -> returns a tuple containing the color for this annotation element in the form (red, green, blue, alpha),
        with the components represented as floating point values in the range [0, 1].

        @return: tuple of (red, green, blue, alpha)
        """
        ...

    def isNull(self) -> bool:
        """

        """
        ...

    def setColor(self, red: float, green: float, blue: float, alpha: float) -> None:
        """
        self.setColor() -> None

        Sets the color and alpha of the element.
        Each component must be a floating point value in the range [0, 1].

        @param red: The new red component.
        @param green: The new green component.
        @param blue: The new blue component.
        @param alpha: The new alpha component.
        """
        ...

    def toString(self) -> str:
        """
        self.toString() -> string

        Returns a description of the object. Equivalent to str(object).

        @return: A string describing the object.
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...
