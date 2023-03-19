import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class ForwardRef(_Final):
    """
    Internal wrapper to hold a forward reference.
    """
    __slots__ = ('__forward_arg__', '__forward_code__', '__forward_evaluated__', '__forward_value__',
                 '__forward_is_argument__', '__forward_is_class__', '__forward_module__')

    def __init__(self, arg, is_argument=True, module=None, *, is_class=False):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def _evaluate(self, globalns, localns, recursive_guard):
        """

        """
        return None

    def __eq__(self, other):
        """
        Return self==value.
        """
        return None

    def __hash__(self):
        """
        Return hash(self).
        """
        return None

    def __repr__(self):
        """
        Return repr(self).
        """
        return None

    __forward_arg__: Any = None
    __forward_code__: Any = None
    __forward_evaluated__: Any = None
    __forward_is_argument__: Any = None
    __forward_is_class__: Any = None
    __forward_module__: Any = None
    __forward_value__: Any = None
