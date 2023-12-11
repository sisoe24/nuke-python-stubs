from typing import *
from numbers import Number

import nuke

from . import *


class NodeConstructor(object):
    """
    NodeConstructor
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

    def __call__(self,  *args, **kwargs) -> None:
        """
        Call self as a function.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
