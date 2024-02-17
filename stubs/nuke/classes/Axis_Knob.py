"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class Axis_Knob(Knob):
    """
    A knob which descibes a 3D affine transformation, by combining rotations around each principal axis, scaling, translation, skew and a pivot point.
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

    def translate(self,) -> XYZ_Knob:
        """
        self.translate() -> XYZ_Knob

        Return translation knob.
        """
        ...

    def rotate(self,) -> XYZ_Knob:
        """
        self.rotate() -> XYZ_Knob

        Return rotation knob.
        """
        ...

    def scale(self,) -> Scale_Knob:
        """
        self.scale() -> Scale_Knob

        Return scale knob.
        """
        ...

    def uniformScale(self,) -> Double_Knob:
        """
        self.uniformScale() -> Double_Knob

        Return uniform scale knob.
        """
        ...

    def pivot(self,) -> XYZ_Knob:
        """
        self.pivot() -> XYZ_Knob

        Return pivot knob.
        """
        ...

    def skew(self,) -> XYZ_Knob:
        """
        self.skew() -> XYZ_Knob

        Return skew knob.
        """
        ...

    def value(self,) -> Any:
        """
        self.value() -> _nukemath.Matrix4
        Return the transform matrix formed by combining the input knob values for translate, rotate, scale, skew and pivot.
        """
        ...
