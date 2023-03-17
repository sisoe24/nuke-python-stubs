from typing import *
from numbers import Number

import nuke

from . import *


class Path_Knob(EvalString_Knob):
    """
    A string-valued knob for entering stage paths.
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

    def evaluate(self,):
        """
        self.evaluate() -> String.
        Evaluate the string, performing substitutions.
        @return: String.
        """
        return str()
