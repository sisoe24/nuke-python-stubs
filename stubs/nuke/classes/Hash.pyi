from typing import *
from numbers import Number

import nuke

from . import *

class Hash(object):
    """
    A hash value for any number of objects.

    The append() method is used to add objects to the hash; the value will be recomputed efficiently as each new object is added.
    """
    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def __getattribute__(self, name, ) -> None:
        """
        Return getattr(self, name).
        """
        ...

    def __setattr__(self, name, value, ) -> None:
        """
        Implement setattr(self, name, value).
        """
        ...

    def __delattr__(self, name, ) -> None:
        """
        Implement delattr(self, name).
        """
        ...

    def __lt__(self, value, ) -> None:
        """
        Return self<value.
        """
        ...

    def __le__(self, value, ) -> None:
        """
        Return self<=value.
        """
        ...

    def __eq__(self, value, ) -> None:
        """
        Return self==value.
        """
        ...

    def __ne__(self, value, ) -> None:
        """
        Return self!=value.
        """
        ...

    def __gt__(self, value, ) -> None:
        """
        Return self>value.
        """
        ...

    def __ge__(self, value, ) -> None:
        """
        Return self>=value.
        """
        ...

    def __new__(self,*args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def getHash(self,*args, **kwargs) -> None:
        """
        Get the current value of the hash.
        """
        ...

    def setHash(self,*args, **kwargs) -> None:
        """
        Set the current value of the hash.
        """
        ...

    def reset(self,*args, **kwargs) -> None:
        """
        Reset the hash.
        """
        ...

    def append(self,*args, **kwargs) -> None:
        """
        Add another value to the hash.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
