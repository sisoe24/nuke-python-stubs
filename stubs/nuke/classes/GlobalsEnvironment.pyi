from typing import *
from numbers import Number

import nuke

from . import *

class GlobalsEnvironment(object):
    """
    Dictionary-style object holding global Nuke state.
    Example:
    nuke.env['threads'] = 4
    """
    def __repr__(self, ) -> None:
        """
        Return repr(self).
        """
        ...

    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def __len__(self, ) -> None:
        """
        Return len(self).
        """
        ...

    def __getitem__(self, key, ) -> None:
        """
        Return self[key].
        """
        ...

    def __setitem__(self, key, value, ) -> None:
        """
        Set self[key] to value.
        """
        ...

    def __delitem__(self, key, ) -> None:
        """
        Delete self[key].
        """
        ...

    def __new__(self,*args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __contains__(self,*args, **kwargs) -> None:
        """

        """
        ...

    def keys(self,*args, **kwargs) -> None:
        """

        """
        ...

    def has_key(self,*args, **kwargs) -> None:
        """

        """
        ...

    def values(self,*args, **kwargs) -> None:
        """

        """
        ...

    def get(self,*args, **kwargs) -> None:
        """

        """
        ...

    def items(self,*args, **kwargs) -> None:
        """

        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
