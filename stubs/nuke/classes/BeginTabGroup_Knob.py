from typing import *
from numbers import Number

import nuke

from . import *


class BeginTabGroup_Knob(Knob):
    """
    Begin a group of tabs. Subsequent knobs will all be part of the same tab group, until a matching EndTabGroup knob is found.
    """

    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
