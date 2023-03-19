import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class TextIO(IO):
    """
    Typed version of the return of open() in text mode.
    """
    __slots__ = ()
    buffer: Any = None
    encoding: Any = None
    errors: Any = None
    line_buffering: Any = None
    newlines: Any = None

    def __enter__(self) -> 'TextIO':
        """

        """
        return 'TextIO'()

    __orig_bases__ = (typing.IO[str],)
    __parameters__ = ()

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None
