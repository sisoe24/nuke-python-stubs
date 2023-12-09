from typing import *
from numbers import Number

import nuke

from . import *


class FnPySingleton(object):
    """

    """

    def __new__(self, *args, **kwargs) -> Any:
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, ...):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
        ...

    @property
    def __dict__(self) -> Any:
        """
        dictionary for instance variables (if defined)
        """
        ...

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
