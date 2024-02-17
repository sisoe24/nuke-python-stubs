"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class Keyer_Knob(Array_Knob):
    """
    Keyer_Knob
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

    def names(self, n: int) -> str:
        """
        self.names(n) -> string

        @param n: The index of the name to return.
        @return: The name at position n.
        """
        ...

    def value(self, outputCtx: OutputContext, n: int) -> float:
        """
        self.value(outputCtx, n) -> float

        Get the value of argument n.
        @param outputCtx: The OutputContext to evaluate the argument in.
        @param n: The index of the argument to get the value of.
        @return: The value of argument n.
        """
        ...

    def lowSoft(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def lowTol(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def highTol(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def highSoft(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...
