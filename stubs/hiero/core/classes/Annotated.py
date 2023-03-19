import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class Annotated(object):
    """
    Add context specific metadata to a type.

    Example: Annotated[int, runtime_check.Unsigned] indicates to the
    hypothetical runtime_check module that this type is an unsigned int.
    Every other consumer of this type can ignore this metadata and treat
    this type as int.

    The first argument to Annotated must be a valid type.

    Details:

    - It's an error to call `Annotated` with less than two arguments.
    - Nested Annotated are flattened::

        Annotated[Annotated[T, Ann1, Ann2], Ann3] == Annotated[T, Ann1, Ann2, Ann3]

    - Instantiating an annotated type is equivalent to instantiating the
    underlying type::

        Annotated[C, Ann1](5) == C(5)

    - Annotated can be used as a generic type alias::

        Optimized = Annotated[T, runtime.Optimize()]
        Optimized[int] == Annotated[int, runtime.Optimize()]

        OptimizedList = Annotated[List[T], runtime.Optimize()]
        OptimizedList[int] == Annotated[List[int], runtime.Optimize()]
    """
    __slots__ = ()

    def __new__(self, *args, **kwargs):
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
        return Any

    def __class_getitem__(self, *args, **kwargs):
        """
        classmethod(function) -> method

        Convert a function to be a class method.

        A class method receives the class as implicit first argument,
        just like an instance method receives the instance.
        To declare a class method, use this idiom:

          class C:
              @classmethod
              def f(cls, arg1, arg2, ...):
                  ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()).  The instance is ignored except for its class.
        If a class method is called for a derived class, the derived class
        object is passed as the implied first argument.

        Class methods are different than C++ or Java static methods.
        If you want those, see the staticmethod builtin.
        """
        return Any

    def __init_subclass__(self, *args, **kwargs):
        """
        classmethod(function) -> method

        Convert a function to be a class method.

        A class method receives the class as implicit first argument,
        just like an instance method receives the instance.
        To declare a class method, use this idiom:

          class C:
              @classmethod
              def f(cls, arg1, arg2, ...):
                  ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()).  The instance is ignored except for its class.
        If a class method is called for a derived class, the derived class
        object is passed as the implied first argument.

        Class methods are different than C++ or Java static methods.
        If you want those, see the staticmethod builtin.
        """
        return Any

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None
