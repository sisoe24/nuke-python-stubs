import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class SupportsComplex(Protocol):
    """
    An ABC with one abstract method __complex__.
    """
    __slots__ = ()

    def __complex__(self) -> complex:
        """

        """
        return complex()

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

    __abstractmethods__ = frozenset({'__complex__'})
    _abc_impl: Any = None
    _is_runtime_protocol = True
