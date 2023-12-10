from typing import *
from numbers import Number

import nuke

from . import *


class PythonCustomKnob(Script_Knob):
    """
    PythonCustomKnob
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

    def getObject(self, *args, **kwargs) -> None:
        """
        Returns the custom knob object as created in the by the 'command' argument to the PyCuston_Knob constructor.
        """
        ...
