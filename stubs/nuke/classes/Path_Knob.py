from typing import *
from numbers import Number

import nuke

from . import *


class Path_Knob(EvalString_Knob):
    """
    Stores a Prim path.
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

    def stagePaths(self,) -> list:
        """
        self.stagePaths() -> list

        Returns a list of paths (strings) in the stage.
        """
        ...
