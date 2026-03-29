"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class Transform2d_Knob(Knob):
    """
    Transform2d_Knob
    """

    def __new__(cls, *args, **kwargs) -> 'Transform2d_Knob':
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

    def value(self, oc: 'OutputContext' | None = None) -> 'matrix':
        """
        value(oc) -> matrix

        Return transformation matrix. The argument oc is an OutputContext. Both arguments are optional.
        """
        ...
