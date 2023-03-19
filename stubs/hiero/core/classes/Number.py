import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class Number(object):
    """
    All numbers inherit from this class.

    If you just want to check if an argument x is a number, without
    caring what kind, use isinstance(x, Number).
    """
    __slots__ = ()
    __hash__: Any = None
    __abstractmethods__ = frozenset()
    _abc_impl: Any = None

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None
