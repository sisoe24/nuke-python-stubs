from typing import *
from numbers import Number

import nuke

from . import *


class View(object):
    """
    A named view.
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

    def __str__(self, ) -> None:
        """
        Return str(self).
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def string(self,) -> str:
        """
        self.string() -> Name of view.
        @return: Name of view.
        """
        ...

    def value(self,) -> Any:
        """
        self.value() -> Value of view.
        @return: Value of view.
        """
        ...
