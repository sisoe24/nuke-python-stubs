from typing import *
from numbers import Number

import nuke

from . import *


class ColorspaceLookupError(Exception):
    """
    an excpetion that should be thrown when looking up the colorspace
    """
    @property
    def __weakref__(self) -> Any:
        """
        list of weak references to the object (if defined)
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...