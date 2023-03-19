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

    def box(self) -> object:
        """
        self.box -> Returns a tuple containing the position and size of the text box, as floating point values.

        The position is that of the box's lower left corner.

        @return: The text box position and size in the form (x, y, width, height)
        """
        return str()

    def fontPath(self) -> str:
        """
        self.fontPath() -> string

        Returns the current font path for this annotation text object.

        @return: A string containing the current font path.
        """
        return str()

    def fontSize(self) -> float:
        """

        """
        return float()

    def horizontalJustification(self) -> core.AnnotationText.HorizontalJustification:
        """
        self.horizontalJustification

        Returns the horizontal justification of the text.

        @return: One of eHLeft, eHCenter, eHRight, eHJustify.
        """
        return core.AnnotationText.HorizontalJustification()

    def isNull(self) -> bool:
        """

        """
        return bool()

    def rotation(self) -> float:
        """
        self.rotation -> float

        Returns the rotation angle of the text, as a floating point value in degrees.

        @return: The text's rotation angle.
        """
        return str()

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
        return None

    def setFontPath(self, fontPath: str) -> None:
        """
        self.setFontPath() -> None

        Sets the path to the file from which to load the font for use with this annotation text object.
        """
        return None

    def setFontSize(self, size: float) -> None:
        """

        """
        return None

    def setHorizontalJustification(self, justify: core.AnnotationText.HorizontalJustification) -> None:
        """
        self.setHorizontalJustification -> None

        Set the horizontal justification of the text.

        @param justify: One of eHLeft, eHCenter, eHRight, eHJustify.
        """
        return None

    def setRotation(self, rotation: float) -> None:
        """
        self.setRotation -> None

        Sets the rotation angle of the text, with a floating point value, replacing the previous angle.

        @param rotation: The new rotation angle, in degrees.
        """
        return None

    def setText(self, text: str) -> None:
        """
        self.setText() -> None

        Sets the text for this annotation text object.

        @param text: The new text string.
        """
        return None

    def setVerticalJustification(self, justify: core.AnnotationText.VerticalJustification) -> None:
        """
        self.setVerticalJustification -> None

        Set the vertical justificaiton of the text.

        @param justify: One of eVBaseline, eVTop, eVCenter, eVBottom.
        """
        return None

    def text(self) -> str:
        """
        self.text() -> string

        @return: A string containing the current text for this annotation text object.
        """
        return str()

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        return str()

    def verticalJustification(self) -> core.AnnotationText.VerticalJustification:
        """
        self.verticalJustification

        Returns the vertical justification of the text.

        @return: One of eVBaseline, eVTop, eVCenter, eVBottom.
        """
        return core.AnnotationText.VerticalJustification()

    def __copy__(self,) -> None:
        """

        """
        return None

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
