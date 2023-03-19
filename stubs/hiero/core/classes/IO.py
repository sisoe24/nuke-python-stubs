import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class IO(Generic):
    """
    Generic base class for TextIO and BinaryIO.

    This is an abstract, generic version of the return of open().

    NOTE: This does not distinguish between the different possible
    classes (text vs. binary, read vs. write vs. read/write,
    append-only, unbuffered).  The TextIO and BinaryIO subclasses
    below capture the distinctions between text vs. binary, which is
    pervasive in the interface; however we currently do not offer a
    way to track the other distinctions in the type system.
    """
    __slots__ = ()
    mode: Any = None
    name: Any = None

    def close(self) -> None:
        """

        """
        return None

    closed: Any = None

    def fileno(self) -> int:
        """

        """
        return int()

    def flush(self) -> None:
        """

        """
        return None

    def isatty(self) -> bool:
        """

        """
        return bool()

    def read(self, n: int = -1) -> ~AnyStr:
        """

        """
        return Any

    def readable(self) -> bool:
        """

        """
        return bool()

    def readline(self, limit: int = -1) -> ~AnyStr:
        """

        """
        return Any

    def readlines(self, hint: int = -1) -> typing.List*args:
        """

        """
        return list()

    def seek(self, offset: int, whence: int = 0) -> int:
        """

        """
        return int()

    def seekable(self) -> bool:
        """

        """
        return bool()

    def tell(self) -> int:
        """

        """
        return int()

    def truncate(self, size: int = None) -> int:
        """

        """
        return int()

    def writable(self) -> bool:
        """

        """
        return bool()

    def write(self, s: ~AnyStr) -> int:
        """

        """
        return int()

    def writelines(self, lines: typing.List*args) -> None:
        """

        """
        return None

    def __enter__(self) -> 'IO*args':
        """

        """
        return 'IO[AnyStr]'

    def __exit__(self, type, value, traceback) -> None:
        """

        """
        return None

    __orig_bases__ = (typing.Generic[~AnyStr],)
    __parameters__ = (~AnyStr,)

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None
