"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class OutputContext(object):
    """
    Describes a context in which expressions can be evaluated.
    """

    def __new__(cls, *args, **kwargs) -> OutputContext:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __hash__(self) -> int:
        """
        Return hash(self).
        """
        ...

    def view(self,) -> int:
        """
        view() -> int

        Return view number.
        """
        ...

    def setView(self, n: int) -> bool:
        """
        setView(n) -> True

        Set view number. The n argument is an integer in the range of 0 to number of views.
        """
        ...

    def frame(self,) -> float:
        """
        frame() -> float

        Return frame value.
        """
        ...

    def setFrame(self, f: float) -> bool:
        """
        setFrame(f) -> True

        Set frame value. The f argument is a float.
        """
        ...

    def viewname(self, n: int) -> str:
        """
        viewname(n) -> string

        Return name of the view. The n argument is an integer in the range of 0 to number of views.
        """
        ...

    def viewshort(self, n: int) -> str:
        """
        viewshort(n) -> string

        Return short name of the view. The n argument is an integer in the range of 0 to number of views.
        """
        ...

    def viewcount(self,) -> int:
        """
        viewcount() -> int

        Return number of views.
        """
        ...

    def viewFromName(self, name: str) -> int:
        """
        viewFromName(name) -> int

        Returns the index of the view with name matching the argument name or -1 if there is no match.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
