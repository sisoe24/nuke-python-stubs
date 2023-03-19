import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class BinaryIO(IO):
    """
    Typed version of the return of open() in binary mode.
    """
    __slots__ = ()

    def write(self, s: typing.Union*args) -> int:
        """

        """
        return int()

    def __enter__(self) -> 'BinaryIO':
        """

        """
        return 'BinaryIO'()

    __orig_bases__ = (typing.IO[bytes],)
    __parameters__ = ()

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None
