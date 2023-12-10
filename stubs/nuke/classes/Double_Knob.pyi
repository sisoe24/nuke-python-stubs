from typing import *
from numbers import Number

import nuke

from . import *

class Double_Knob(Array_Knob):
    """
    A knob which holds one or more double-precision floating point values.
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
