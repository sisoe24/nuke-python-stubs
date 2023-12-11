from typing import *
from numbers import Number

import nuke

from . import *


class Multiline_Eval_String_Knob(EvalString_Knob):
    """
    A knob which evaluates it's string value as a TCL expression. It provides a multiline text area when it appears in a Node panel.
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
