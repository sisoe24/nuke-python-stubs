"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class PathExpression_Knob(Path_Knob):
    """
    Stores a Prim path expression.
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

    def match(self, pattern: str) -> list:
        """
        self.match(pattern: str) -> list

        Returns a list of paths (strings) that match the given stage using the pattern expression.
        """
        ...
