from typing import *
from numbers import Number

import nuke

from . import *

class EvalString_Knob(String_Knob):
    """
    A string-valued knob which evaluates its value as a TCL expression.
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

    def evaluate(self,) -> str:
        """
        self.evaluate() -> String.
        Evaluate the string, performing substitutions.
        @return: String.
        """
        ...
