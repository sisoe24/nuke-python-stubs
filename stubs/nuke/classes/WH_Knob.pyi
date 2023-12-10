from typing import *
from numbers import Number

import nuke

from . import *

class WH_Knob(Array_Knob):
    """
    A knob which holds width and height values.
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

    def names(self,*args, **kwargs) -> None:
        """
        Return name for dimension 'i'.
        """
        ...

    def x(self,*args, **kwargs) -> None:
        """
        Return value for X position.
        """
        ...

    def y(self,*args, **kwargs) -> None:
        """
        Return value for Y position.
        """
        ...

    def x_at(self,*args, **kwargs) -> None:
        """
        Return value for X position at time 't'.
        """
        ...

    def y_at(self,*args, **kwargs) -> None:
        """
        Return value for Y position at time 't'.
        """
        ...
