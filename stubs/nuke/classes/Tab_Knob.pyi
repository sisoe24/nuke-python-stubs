from typing import *
from numbers import Number

import nuke

from . import *

class Tab_Knob(Knob):
    """
    Groups subsequent knobs onto a tab.
    """
    def __hash__(self, ) -> None:
        """
        Return hash(self).
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

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
