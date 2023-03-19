import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class TypeVar(_Final):
    """
    Type variable.

    Usage::

      T = TypeVar('T')  # Can be anything
      A = TypeVar('A', str, bytes)  # Must be str or bytes

    Type variables exist primarily for the benefit of static type
    checkers.  They serve as the parameters for generic types as well
    as for generic function definitions.  See class Generic for more
    information on generic types.  Generic functions work as follows:

      def repeat(x: T, n: int) -> List[T]:
          '''Return a list containing n references to x.'''
          return [x]*n

      def longest(x: A, y: A) -> A:
          '''Return the longest of two strings.'''
          return x if len(x) >= len(y) else y

    The latter example's signature is essentially the overloading
    of (str, str) -> str and (bytes, bytes) -> bytes.  Also note
    that if the arguments are instances of some subclass of str,
    the return type is still plain str.

    At runtime, isinstance(x, T) and issubclass(C, T) will raise TypeError.

    Type variables defined with covariant=True or contravariant=True
    can be used to declare covariant or contravariant generic types.
    See PEP 484 for more details. By default generic types are invariant
    in all type variables.

    Type variables can be introspected. e.g.:

      T.__name__ == 'T'
      T.__constraints__ == ()
      T.__covariant__ == False
      T.__contravariant__ = False
      A.__constraints__ == (str, bytes)

    Note that only type variables defined in global scope can be pickled.
    """
    __slots__ = ('__name__', '__bound__', '__constraints__',
                 '__covariant__', '__contravariant__', '__dict__')

    def __init__(self, name, *constraints, bound=None, covariant=False, contravariant=False):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def __repr__(self):
        """
        Return repr(self).
        """
        return None

    def __reduce__(self):
        """
        Helper for pickle.
        """
        return None

    __bound__: Any = None
    __constraints__: Any = None
    __contravariant__: Any = None
    __covariant__: Any = None
    __name__: Any = None

    @property
    def __dict__(self) -> Any:
        """
        dictionary for instance variables (if defined)
        """
        return None
