import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class AnnotationText(AnnotationElement):
    """
    A class, derived from AnnotationElement, storing a single item of text within an annotation.
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

    def box(self) -> object:
        """
        self.box -> Returns a tuple containing the position and size of the text box, as floating point values.

        The position is that of the box's lower left corner.

        @return: The text box position and size in the form (x, y, width, height)
        """
        ...

    def fontPath(self) -> str:
        """
        self.fontPath() -> string

        Returns the current font path for this annotation text object.

        @return: A string containing the current font path.
        """
        ...

    def fontSize(self) -> float:
        """

        """
        ...

    def horizontalJustification(self) -> core.AnnotationText.HorizontalJustification:
        """
        self.horizontalJustification

        Returns the horizontal justification of the text.

        @return: One of eHLeft, eHCenter, eHRight, eHJustify.
        """
        ...

    def isNull(self) -> bool:
        """

        """
        ...

    def rotation(self) -> float:
        """
        self.rotation -> float

        Returns the rotation angle of the text, as a floating point value in degrees.

        @return: The text's rotation angle.
        """
        ...

    def setBox(self, x: float, y: float, width: float, height: float) -> None:
        """
        self.setBox(x, y, width, height) -> None

        Sets the text box for this annotation text object.
        The text box determines the position and layout of the text (the layout also being affected
        by the alignment). The size of the text box does not affect the size of the glyphs that make up
        the text, that's determined by the font size - see setFontSize() and fontSize().

        @param x: The new x-component of the bottom left corner of the text box, before any rotation.
        @param y: The new y-component of the bottom left corner of the text box, before any rotation.
        @param width: The new width of the text box.
        @param height: The new height of the text box.
        """
        ...

    def setFontPath(self, fontPath: str) -> None:
        """
        self.setFontPath() -> None

        Sets the path to the file from which to load the font for use with this annotation text object.
        """
        ...

    def setFontSize(self, size: float) -> None:
        """

        """
        ...

    def setHorizontalJustification(self, justify: core.AnnotationText.HorizontalJustification) -> None:
        """
        self.setHorizontalJustification -> None

        Set the horizontal justification of the text.

        @param justify: One of eHLeft, eHCenter, eHRight, eHJustify.
        """
        ...

    def setRotation(self, rotation: float) -> None:
        """
        self.setRotation -> None

        Sets the rotation angle of the text, with a floating point value, replacing the previous angle.

        @param rotation: The new rotation angle, in degrees.
        """
        ...

    def setText(self, text: str) -> None:
        """
        self.setText() -> None

        Sets the text for this annotation text object.

        @param text: The new text string.
        """
        ...

    def setVerticalJustification(self, justify: core.AnnotationText.VerticalJustification) -> None:
        """
        self.setVerticalJustification -> None

        Set the vertical justificaiton of the text.

        @param justify: One of eVBaseline, eVTop, eVCenter, eVBottom.
        """
        ...

    def text(self) -> str:
        """
        self.text() -> string

        @return: A string containing the current text for this annotation text object.
        """
        ...

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        ...

    def verticalJustification(self) -> core.AnnotationText.VerticalJustification:
        """
        self.verticalJustification

        Returns the vertical justification of the text.

        @return: One of eVBaseline, eVTop, eVCenter, eVBottom.
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...

    HorizontalJustification: Any = None
    eHLeft: Any = None
    eHCenter: Any = None
    eHRight: Any = None
    eHJustify: Any = None
    VerticalJustification: Any = None
    eVBaseline: Any = None
    eVTop: Any = None
    eVCenter: Any = None
    eVBottom: Any = None
