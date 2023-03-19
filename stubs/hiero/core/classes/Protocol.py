import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class Protocol(Generic):
    """
    Base class for protocol classes.

    Protocol classes are defined as::

        class Proto(Protocol):
            def meth(self) -> int:
                ...

    Such classes are primarily used with static type checkers that recognize
    structural subtyping (static duck-typing), for example::

        class C:
            def meth(self) -> int:
                return 0

        def func(x: Proto) -> int:
            return x.meth()

        func(C())  # Passes static type check

    See PEP 544 for details. Protocol classes decorated with
    @typing.runtime_checkable act as simple-minded runtime protocols that check
    only the presence of given attributes, ignoring their type signatures.
    Protocol classes can be generic, they are defined as::

        class GenProto(Protocol[T]):
            def meth(self) -> T:
                ...
    """
    __slots__ = ()
    _is_protocol = True
    _is_runtime_protocol = False

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

    __parameters__ = ()
    __abstractmethods__ = frozenset()
    _abc_impl: Any = None

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None
