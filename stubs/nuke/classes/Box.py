"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class Box(object):
    """
    A 2-dimensional rectangle. Described by left, right, top and bottom coords (width and height are calculated as necessary).
    """

    def __new__(cls, *args, **kwargs) -> Box:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __hash__(self) -> int:
        """
        Return hash(self).
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def x(self,) -> int:
        """
        self.x() -> int

        The left edge of the box.
        """
        ...

    def setX(self, n: int) -> None:
        """
        self.setX(n) -> None

        Set the left edge. The parameter n is an integer.
        """
        ...

    def y(self,) -> int:
        """
        self.y() -> int

        Return the bottom edge.
        """
        ...

    def setY(self, n: int) -> None:
        """
        self.setY(n) -> None

        Set the bottom edge. The parameter n is an integer.
        """
        ...

    def r(self,) -> int:
        """
        self.r() -> int

        Return the right edge of the box.
        """
        ...

    def setR(self, n: int) -> None:
        """
        self.setR(n) -> None

        Set the right edge. The parameter n is an integer.
        """
        ...

    def t(self,) -> int:
        """
        self.t() -> int

        Return top edge.
        """
        ...

    def setT(self, n: int) -> None:
        """
        self.setT(n) -> None

        Set top edge.
        """
        ...

    def w(self,) -> int:
        """
        self.w() -> int

        Return width.
        """
        ...

    def setW(self, n: int) -> None:
        """
        self.setW(n) -> None

        Set width by moving right edge.
        """
        ...

    def h(self,) -> int:
        """
        self.h() -> int

        Return height.
        """
        ...

    def setH(self, n: int) -> None:
        """
        self.setH(n) -> None

        Set height by moving top edge.
        """
        ...

    def centerX(self,) -> float:
        """
        self.centerX() -> float

        Return center in X.
        """
        ...

    def centerY(self,) -> float:
        """
        self.centerY() -> float

        Return height in Y.
        """
        ...

    def set(self, x: int, y: int, r: int, t: int) -> None:
        """
        self.set(x, y, r, t) -> None

        Set all values at once.
        """
        ...

    def isConstant(self,) -> bool:
        """
        self.isConstant() -> True if box is 1x1 in both directions, False otherwise.
        """
        ...

    def clear(self,) -> None:
        """
        self.clear() -> None.

        Set to is_constant().
        """
        ...

    def move(self, dx: int, dy: int) -> None:
        """
        self.move(dx, dy) -> None.

        Move all the sides and thus the entire box by the given deltas.
        """
        ...

    def pad(self, dx: int, dy: int, dr: int, dt: int) -> None:
        """
        self.pad(dx, dy, dr, dt) -> None.

        Move all the sides and thus the entire box by the given deltas.
        """
        ...

    def clampX(self, x: int) -> int:
        """
        self.clampX(x) -> int.

        Return x restricted to pointing at a pixel in the box.
        """
        ...

    def clampY(self, y: int) -> int:
        """
        self.clampY(y) -> int.

        Return y restricted to pointing at a pixel in the box.
        """
        ...

    def merge(self, x: int, y: int, r: int, t: int) -> None:
        """
        self.merge(x, y, r, t) -> None.

        Merge with the given edges.
        """
        ...

    def intersect(self, x: int, y: int, r: int, t: int) -> None:
        """
        self.intersect(x, y, r, t) -> None.

        Intersect with the given edges.
        """
        ...
