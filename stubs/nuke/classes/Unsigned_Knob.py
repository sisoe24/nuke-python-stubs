from typing import *
from numbers import Number

import nuke

from . import *


class Unsigned_Knob(Array_Knob):
    """
    A knob which holds one or more unsigned integer values.
    """

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

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def value(self,) -> int:
        """
        self.value() -> int
        Get the value of this knob as an integer.
        @return: int
        """
        ...

    def setValue(self, val: int) -> bool:
        """
        self.setValue(val) -> bool
        Set the unsigned integer value of this knob.
        @param val: The new value for the knob. Must be an integer >= 0.
        @return: True if succeeded, False otherwise.
        """
        ...
