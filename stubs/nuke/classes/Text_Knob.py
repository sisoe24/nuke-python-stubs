from typing import *
from numbers import Number

import nuke

from . import *


class Text_Knob(Knob):
    """
    A knob which holds a string value.
    """

    def __hash__(self, ):
        """
        Return hash(self).
        """
        return None

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def value(self, *args, **kwargs):
        """
        Return value at the current frame for channel 'c'.
        """
        return None

    def setValue(self, val, chan):
        """
        self.setValue(val, chan) -> bool

        Sets the value 'val' at channel 'chan'.
        @return: True if successful, False if not.
        """
        return bool()