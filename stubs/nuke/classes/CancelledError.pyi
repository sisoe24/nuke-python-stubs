from typing import *
from numbers import Number

import nuke

from . import *

class CancelledError(Exception):
    """
    Common base class for all non-exit exceptions.
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
