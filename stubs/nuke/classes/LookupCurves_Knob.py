"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class LookupCurves_Knob(Knob):
    """
    Provide a set of user-editable lookup curves.
    """

    def __new__(cls, *args, **kwargs) -> LookupCurves_Knob:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __hash__(self) -> int:
        """
        Return hash(self).
        """
        ...

    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def addCurve(self, curve: str | AnimationCurve, expr: str | None = None) -> None:
        """
        self.addCurve(curve, expr=None) -> None
        Adds a curve.
        @param curve: The name of an animation curve, or an AnimationCurve instance.
        @param expr: Optional parameter giving an expression for the curve.
        @return: None
        """
        ...

    def editCurve(self, curve: str | AnimationCurve, expr: str | None = None) -> None:
        """
        self.editCurve(curve, expr=None) -> None
        Edits an existing curve.
        @param curve: The name of an animation curve.
        @param expr: The new expression for the curve.
        @return: None
        """
        ...

    def delCurve(self, curve: str | AnimationCurve) -> None:
        """
        self.delCurve(curve) -> None
        Deletes a curve.
        @param curve: The name of the animation curve.
        @return: None
        """
        ...
