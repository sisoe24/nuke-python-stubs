import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class Annotation(SubTrackItem):
    """
    Class for objects that can hold multiple stroke and/or text elements to provide annotation functionality.
    Annotation is derived from SubTrackItem and thus Annotation objects can be placed and trimmed on VideoTrack
    subtracks. Strokes and/or text can be added to an annotation by creating AnnotationStroke and/or AnnotationText
    objects and using addElement().
    """

    def __repr__(self) -> object:
        """
        Return repr(self).
        """
        return object()

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

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def addElement(self, element: core.AnnotationElement) -> core.AnnotationElement:
        """
        self.addElement() -> Adds the specified AnnotationElement, which should be an instance of an AnnotationElement sub-class, i.e. either
        an AnnotationStroke or an AnnotationText object.

        @return: If there was no error, returns the added element.
        """
        return core.AnnotationElement()

    def deserialize(self, data: str) -> None:
        """
        self.deserialize() -> restore the annotation from XML data
        """
        return None

    def elements(self) -> object:
        """
        self.elements() -> returns a tuple with all of the elements contained in this annotation.

        @return: tuple of hiero.core.Element sub-class objects
        """
        return object()

    def serialize(self) -> str:
        """
        self.serialize() -> serialize the annotation object to XML
        """
        return str()

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

    def _Annotation_addToNukeScript(self, script, offset=0, inputs=0, cliptype=None):
        """

        """
        return None
