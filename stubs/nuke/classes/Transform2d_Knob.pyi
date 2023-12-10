from typing import *
from numbers import Number

import nuke

from . import *

class Transform2d_Knob(Knob):
    """
    Transform2d_Knob
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

    def value(self,oc) -> Any:
        """
        value(oc) -> matrix

        Return transformation matrix. The argument oc is an OutputContext. Both arguments are optional.
        """
        ...
