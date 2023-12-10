from typing import *
from numbers import Number

import nuke

from . import *

class Boolean_Knob(Array_Knob):
    """
    A knob which holds a boolean value. This appears in a Node panel as a check box.
    """
    def __hash__(self, ) -> None:
        """
        Return hash(self).
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

    def value(self,) -> Union[True, False]:
        """
        self.value() -> bool
        Get the boolean value for this knob.
        @return: True or False.
        """
        ...

    def setValue(self, b:bool) -> bool:
        """
        self.setValue(b) -> bool
        Set the boolean value of this knob.
        @param b: Boolean convertible object.
        @return: True if modified, False otherwise.
        """
        ...
