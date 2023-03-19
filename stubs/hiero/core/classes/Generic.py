import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class Generic(object):
    """
    Abstract base class for generic types.

    A generic type is typically declared by inheriting from
    this class parameterized with one or more type variables.
    For example, a generic mapping type might be defined as::

      class Mapping(Generic[KT, VT]):
          def __getitem__(self, key: KT) -> VT:
              ...
          # Etc.

    This class can then be used as follows::

      def lookup_name(mapping: Mapping[KT, VT], key: KT, default: VT) -> VT:
          try:
              return mapping[key]
          except KeyError:
              return default
    """
    __slots__ = ()
    _is_protocol = False

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
