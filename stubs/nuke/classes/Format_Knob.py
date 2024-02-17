"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class Format_Knob(Knob):
    """
    Format_Knob
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

    def name(self,) -> str:
        """
        name() -> string.

        Return name of knob.
        """
        ...

    def value(self,) -> Format:
        """
        value() -> Format.

        Return value of knob.
        """
        ...

    def actualValue(self,) -> Format:
        """
        actualValue() -> Format.

        Return value of knob.
        """
        ...

    def setValue(self, format) -> bool:
        """
        setValue(format) -> True if succeeded, False otherwise.

        Set value of knob to format (either a Format object or a name of a format, e.g. "NTSC").
        """
        ...

    def fromScript(self, s) -> bool:
        """
        fromScript(s) -> True if succeeded, False otherwise.

        Initialise from script s.
        """
        ...

    def toScript(self, quote, context=None) -> str:
        """
        toScript(quote, context=current) -> string.

        Return the value of the knob in script syntax.
        Pass True for quote to return results quoted in {}.
        Pass None for context to get results for all views and key times (as stored in a .nk file).
        """
        ...

    def notDefault(self,) -> bool:
        """
        notDefault() -> True if set to its default value, False otherwise.
        """
        ...
