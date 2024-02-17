"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class CancelledError(Exception):
    """
    Common base class for all non-exit exceptions.
    """
    @property
    def __weakref__(self) -> typing.Any:
        """
        list of weak references to the object (if defined)
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
