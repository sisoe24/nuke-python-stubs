from typing import *
from numbers import Number

import nuke

from . import *

class IArray_Knob(Array_Knob):
    """
    IArray_Knob
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

    def __new__(self,*args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def dimensions(self,*args, **kwargs) -> None:
        """
        Return number of dimensions.
        """
        ...

    def width(self,*args, **kwargs) -> None:
        """
        Return width of the array.
        """
        ...

    def height(self,*args, **kwargs) -> None:
        """
        Return height of the array.
        """
        ...

    def value(self,*args, **kwargs) -> None:
        """
        Return value of the array at position (x, y).
        """
        ...
