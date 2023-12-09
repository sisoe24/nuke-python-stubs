from typing import *
from numbers import Number

import nuke

from . import *


class OutputContext(object):
    """
    Describes a context in which expressions can be evaluated.
    """

    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def view(self,) -> int:
        """
        view() -> int

        Return view number.
        """
        ...

    def setView(self, n) -> True:
        """
        setView(n) -> True

        Set view number. The n argument is an integer in the range of 0 to number of views.
        """
        ...

    def frame(self,) -> float:
        """
        frame() -> float

        Return frame value.
        """
        ...

    def setFrame(self, f) -> True:
        """
        setFrame(f) -> True

        Set frame value. The f argument is a float.
        """
        ...

    def viewname(self, n) -> str:
        """
        viewname(n) -> string

        Return name of the view. The n argument is an integer in the range of 0 to number of views.
        """
        ...

    def viewshort(self, n) -> str:
        """
        viewshort(n) -> string

        Return short name of the view. The n argument is an integer in the range of 0 to number of views.
        """
        ...

    def viewcount(self,) -> int:
        """
        viewcount() -> int

        Return number of views.
        """
        ...

    def viewFromName(self, name) -> int:
        """
        viewFromName(name) -> int

        Returns the index of the view with name matching the argument name or -1 if there is no match.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
