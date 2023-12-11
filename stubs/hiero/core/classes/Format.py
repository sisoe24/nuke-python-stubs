import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class Format(Object):
    """
    Object containing width, height, pixel aspect, and name of a Clip/Sequence format.

    Initialisation:
    Format(width, height, pixel_aspect, name)

    Format(formatStr)

    @param: width - the format's width in pixels (integer)
    @param: height - the format's height in pixels (integer)
    @param: pixel_aspect - the format's pixel aspect ratio (float)
    @param: name - the display name of the format (string)

    @param: formatStr - the string representation of the format in the form returned by str(format)

    Examples: F = hiero.core.Format(2048, 400, 2.37, 'MyFormat'), F = hiero.core.Format('2048 400 0 0 2048 400 2.37 MyFormat')
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __repr__(self) -> object:
        """
        Return repr(self).
        """
        ...

    def __lt__(self, value, ) -> None:
        """
        Return self<value.
        """
        ...

    def __le__(self, value, ) -> None:
        """
        Return self<=value.
        """
        ...

    def __eq__(self, value, ) -> None:
        """
        Return self==value.
        """
        ...

    def __ne__(self, value, ) -> None:
        """
        Return self!=value.
        """
        ...

    def __gt__(self, value, ) -> None:
        """
        Return self>value.
        """
        ...

    def __ge__(self, value, ) -> None:
        """
        Return self>=value.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def aspect(self) -> float:
        """
        self.aspect() -> returns the aspect ratio of this format.

        @return: float
        """
        ...

    def cleanAperture(self) -> object:
        """
        self.cleanAperture() -> returns a 4 element tuple with the rectangle (x1, y1, x2, y2) of the clean aperture.

        @return: tuple
        """
        ...

    def height(self) -> int:
        """
        self.height() -> returns the height of this format.

        @return: int
        """
        ...

    def isValid(self) -> bool:
        """
        self.isValid() -> returns whether or not this format object has valid data.

        @return: True or False
        """
        ...

    def name(self) -> str:
        """
        self.name() -> returns the name of this format.

        @return: string
        """
        ...

    def pixelAspect(self) -> float:
        """
        self.pixelAspect() -> returns the pixel aspect ratio of this format.

        @return: float
        """
        ...

    def productionAperture(self) -> object:
        """
        self.productionAperture() -> returns a 4 element tuple with the rectangle (x1, y1, x2, y2) of the production aperture.

        @return: tuple
        """
        ...

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        ...

    def width(self) -> int:
        """
        self.width() -> returns the width of this format

        @return: int
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...

    __hash__: Any = None

    def _Format_addToNukeScript(self, script=None, resize='width', black_outside=True) -> None:
        """
        self.addToNukeScript(self, script, to_type) -> adds a Reformat node matching this Format to the specified script and returns the nuke node object.     @param script: Nuke script object to add nodes to, or None to just generate and return the node.   @param resize: Type of resize (use constants from nuke.ReformatNode, default is kResizeWidth).   @parm black_outside: Value for the black_outside knob.   @return: hiero.core.nuke.ReformatNode object

        """
        ...
