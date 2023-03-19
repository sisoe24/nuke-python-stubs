import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class SupportsFloat(Protocol):
    """
    An ABC with one abstract method __float__.
    """
    __slots__ = ()

    def __float__(self) -> float:
        """

        """
        return float()

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

    __abstractmethods__ = frozenset({'__float__'})
    _abc_impl: Any = None
    _is_runtime_protocol = True
