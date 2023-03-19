import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class SupportsInt(Protocol):
    """
    An ABC with one abstract method __int__.
    """
    __slots__ = ()

    def __int__(self) -> int:
        """

        """
        return int()

    __parameters__ = ()
    _is_protocol = True

    def _proto_hook(self, other):
        """

        """
        return None

    def _no_init_or_replace_init(self, *args, **kwargs):
        """

        """
        return None

    __abstractmethods__ = frozenset({'__int__'})
    _abc_impl: Any = None
    _is_runtime_protocol = True
