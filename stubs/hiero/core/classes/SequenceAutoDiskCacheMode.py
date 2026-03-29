"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import ui
import core
import nuke
import hiero
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class SequenceAutoDiskCacheMode(object):
    """

    """

    def __new__(cls, *args, **kwargs) -> SequenceAutoDiskCacheMode:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __repr__(self) -> str:
        """
        Return repr(self).
        """
        ...

    def __hash__(self) -> int:
        """
        Return hash(self).
        """
        ...

    def __str__(self) -> str:
        """
        Return str(self).
        """
        ...

    def __lt__(self, value) -> bool:
        """
        Return self<value.
        """
        ...

    def __le__(self, value) -> bool:
        """
        Return self<=value.
        """
        ...

    def __eq__(self, value) -> bool:
        """
        Return self==value.
        """
        ...

    def __ne__(self, value) -> bool:
        """
        Return self!=value.
        """
        ...

    def __gt__(self, value) -> bool:
        """
        Return self>value.
        """
        ...

    def __ge__(self, value) -> bool:
        """
        Return self>=value.
        """
        ...

    def __add__(self, value) -> SequenceAutoDiskCacheMode:
        """
        Return self+value.
        """
        ...

    def __radd__(self, value) -> SequenceAutoDiskCacheMode:
        """
        Return value+self.
        """
        ...

    def __sub__(self, value) -> SequenceAutoDiskCacheMode:
        """
        Return self-value.
        """
        ...

    def __rsub__(self, value) -> SequenceAutoDiskCacheMode:
        """
        Return value-self.
        """
        ...

    def __mul__(self, value) -> SequenceAutoDiskCacheMode:
        """
        Return self*value.
        """
        ...

    def __rmul__(self, value) -> SequenceAutoDiskCacheMode:
        """
        Return value*self.
        """
        ...

    def __pos__(self) -> SequenceAutoDiskCacheMode:
        """
        +self
        """
        ...

    def __bool__(self) -> bool:
        """
        True if self else False
        """
        ...

    def __and__(self, value) -> SequenceAutoDiskCacheMode:
        """
        Return self&value.
        """
        ...

    def __rand__(self, value) -> SequenceAutoDiskCacheMode:
        """
        Return value&self.
        """
        ...

    def __xor__(self, value) -> SequenceAutoDiskCacheMode:
        """
        Return self^value.
        """
        ...

    def __rxor__(self, value) -> SequenceAutoDiskCacheMode:
        """
        Return value^self.
        """
        ...

    def __or__(self, value) -> SequenceAutoDiskCacheMode:
        """
        Return self|value.
        """
        ...

    def __ror__(self, value) -> SequenceAutoDiskCacheMode:
        """
        Return value|self.
        """
        ...

    def __int__(self) -> int:
        """
        int(self)
        """
        ...

    def __index__(self) -> int:
        """
        Return self converted to an integer, if self is suitable for use as an index into a list.
        """
        ...

    def __reduce__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Helper for pickle.
        """
        ...

    @property
    def name(self) -> typing.Any:
        """

        """
        ...

    values = {'eUnknown': hiero.core.SequenceAutoDiskCacheMode.eUnknown, 'eManual': hiero.core.SequenceAutoDiskCacheMode.eManual,
              'eAuto': hiero.core.SequenceAutoDiskCacheMode.eAuto, 'eDefault': hiero.core.SequenceAutoDiskCacheMode.eDefault}
    eUnknown: Any = None
    eManual: Any = None
    eAuto: Any = None
    eDefault: Any = None

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
