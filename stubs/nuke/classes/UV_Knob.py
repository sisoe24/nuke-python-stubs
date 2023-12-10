from typing import *
from numbers import Number

import nuke

from . import *


class UV_Knob(Array_Knob):
    """
    A knob which describes a texture coordinate.
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

    def names(self, n) -> str:
        """
        names(n) -> string

        Return name for dimension n. The argument n is an integer.
        """
        ...
