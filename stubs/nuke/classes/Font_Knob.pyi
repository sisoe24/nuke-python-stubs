from typing import *
from numbers import Number

import nuke

from . import *

class Font_Knob(Knob):
    """
    A knob for choosing a font.
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

    def value(self,*args, **kwargs) -> None:
        """
        Return value at the current frame for channel 'c'.
        """
        ...

    def setValue(self,val, chan) -> bool:
        """
        self.setValue(val, chan) -> bool

        Sets the value 'val' at channel 'chan'.
        @return: True if successful, False if not.
        """
        ...
