import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class ReformatState(Object):
    """
    Object representing a the reformatting settings for a track item.  This corresponds to the Nuke 'Reformat' node.
    """

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

    def boxForceShape(self) -> bool:
        """
        self.boxForceShape() -> returns the box 'force shape' flag.

        @return: bool
        """
        return bool()

    def boxPAR(self) -> float:
        """
        self.boxPAR() -> returns the box pixel aspect ratio.

        @return: double
        """
        return float()

    def boxSize(self) -> PySide2.QtCore.QSize:
        """
        self.boxSize() -> returns the box size.

        @return: QSize
        """
        return Any

    def isNull(self) -> bool:
        """

        """
        return bool()

    def originalResizeFlip(self) -> bool:
        """
        self.originalResizeFlip() -> returns the original resize flip flag, which may be a deprecated value if it was loaded from an old project.

        @return: bool
        """
        return bool()

    def originalResizeFlop(self) -> bool:
        """
        self.originalResizeFlop() -> returns the original resize flop flag, which may be a deprecated value if it was loaded from an old project.

        @return: bool
        """
        return bool()

    def originalResizeTurn(self) -> bool:
        """
        self.originalResizeTurn() -> returns the original resize turn flag, which may be a deprecated value if it was loaded from an old project.

        @return: bool
        """
        return bool()

    def originalType(self) -> str:
        """
        self.originalType() -> returns the original reformat type of the state, which may be a deprecated value if it was loaded from an old project.

        @return: string
        """
        return str()

    def resizeCenter(self) -> bool:
        """
        self.resizeCenter() -> returns the resize center flag.

        @return: bool
        """
        return bool()

    def resizeFlip(self) -> bool:
        """
        self.resizeFlip() -> returns the resize flip flag. Note: the flip option has been removed, this method should not be called.

        @return: bool
        """
        return bool()

    def resizeFlop(self) -> bool:
        """
        self.resizeFlop() -> returns the resize flop flag. Note: the flop option has been removed, this method should not be called.

        @return: bool
        """
        return bool()

    def resizeTurn(self) -> bool:
        """
        self.resizeTurn() -> returns the resize turn flag. Note: the turn option has been removed, this method should not be called.

        @return: bool
        """
        return bool()

    def resizeType(self) -> str:
        """
        self.resizeType() -> returns the resize type.

        @return: string
        """
        return str()

    def scale(self) -> float:
        """
        self.scale() -> returns the scaling factor. Note: the scale option has been removed, this method should not be called.

        @return: double
        """
        return float()

    def setBoxForceShape(self, force: bool) -> None:
        """
        self.setBoxForceShape() -> sets the box 'force shape' flag if the reformat type is set to 'to box'.

        @param setBoxForceShape: bool
        """
        return None

    def setBoxPAR(self, PAR: float) -> None:
        """
        self.setBoxPAR() -> sets the box pixel aspect ratio if the reformat type is set to 'to box'.

        @param PAR: double
        """
        return None

    def setBoxSize(self, size: PySide2.QtCore.QSize) -> None:
        """
        self.setBoxSize() -> sets the box size if the reformat type is set to 'to box'.

        @param size: QSize
        """
        return None

    def setResizeCenter(self, center: bool) -> None:
        """
        self.setResizeCenter() -> sets the resize center flag on the track item.

        @param center: bool
        """
        return None

    def setResizeFlip(self, flip: bool) -> None:
        """
        self.setResizeFlip() -> the flip option has been removed, this method exists only for compatibility reasons
        """
        return None

    def setResizeFlop(self, flop: bool) -> None:
        """
        self.setResizeFlop() -> the flop option has been removed, this method exists only for compatibility reasons
        """
        return None

    def setResizeTurn(self, turn: bool) -> None:
        """
        self.setResizeTurn() -> the turn option has been removed, this method exists only for compatibility reasons
        """
        return None

    def setResizeType(self, newResizeType: str) -> None:
        """
        self.setResizeType() -> sets the resize type of the state.

        @param newResizeType: string
        """
        return None

    def setScale(self, value: float) -> None:
        """
        self.setScale() -> the scale option has been removed, this method exists only for compatibility reasons
        """
        return None

    def setType(self, newType: str) -> None:
        """
        self.setType() -> sets the reformat type of the state.

        @param newType: string
        """
        return None

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        return str()

    def type(self) -> str:
        """
        self.type() -> returns the reformat type of the state.

        @return: string
        """
        return str()

    def __copy__(self,) -> None:
        """

        """
        return None
