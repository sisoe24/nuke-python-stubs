import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class SupportsRound(Protocol):
    """
    An ABC with one abstract method __round__ that is covariant in its return type.
    """
    __slots__ = ()

    def __round__(self, ndigits: int = 0) -> +T_co:
        """

        """
        return Any

    __orig_bases__ = (typing.Protocol[+T_co],)
    __parameters__ = (+T_co,)
    _is_protocol = True

    def _proto_hook(self, other):
        """

        """
        return None

    def _no_init_or_replace_init(self, *args, **kwargs):
        """

        """
        return None

    __abstractmethods__ = frozenset({'__round__'})
    _abc_impl: Any = None
    _is_runtime_protocol = True
