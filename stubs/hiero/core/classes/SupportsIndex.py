import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class SupportsIndex(Protocol):
    """
    An ABC with one abstract method __index__.
    """
    __slots__ = ()

    def __index__(self) -> int:
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

    __abstractmethods__ = frozenset({'__index__'})
    _abc_impl: Any = None
    _is_runtime_protocol = True
