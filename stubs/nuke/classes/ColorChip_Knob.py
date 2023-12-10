from typing import *
from numbers import Number

import nuke

from . import *


class ColorChip_Knob(Unsigned_Knob):
    """
    A knob which holds a single unsigned int that describes a user interface colour. The color format is 0xRRGGBB00.
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
