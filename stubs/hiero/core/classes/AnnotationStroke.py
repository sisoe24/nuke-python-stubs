import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class AnnotationStroke(AnnotationElement):
    """
    A class, derived from AnnotationElement, storing a set of 2d points to represent a single stroke
    within an annotation.
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

    def __bool__(self, ):
        """
        self != 0
        """
        return None

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def isNull(self) -> bool:
        """

        """
        return bool()

    def lineWidth(self) -> float:
        """

        """
        return float()

    def points(self) -> object:
        """
        self.points -> Returns a variable tuple containing the 2d points forming the stroke. Each point is
        represented as a 2 component tuple, with the x and y components of the point as floating point values.

        @return: tuple of 2 component tuples, each of the form (x, y)
        """
        return object()

    def setLineWidth(self, lineWidth: float) -> None:
        """

        """
        return None

    def setPoints(self, arg__1: object) -> None:
        """
        self.setPoints -> Sets the points that make up this stroke, replacing any points the stroke already had.
        The points must be specified as a list (not tuple) of 2d points, each point being a 2 component tuple of
        floats or integers, e.g. [(100, 200), (123.456, 300)].
        """
        return None

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        return str()

    def __copy__(self,) -> None:
        """

        """
        return None
