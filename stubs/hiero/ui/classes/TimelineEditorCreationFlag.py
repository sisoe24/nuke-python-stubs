import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class TimelineEditorCreationFlag(IntEnum):
    """
    An enumeration.
    """

    def _generate_next_value_(self, name, start, count, last_values) -> None:
        """
        Generate the next value when not given.

        name: the name of the member
        start: the initial start value or None
        count: the number of existing members
        last_value: the last value assigned or None
        """
        ...

    _member_names_ = ['kDontCreate', 'kRecycleOrCreate', 'kForceCreation']
    _member_map_ = {'kDontCreate': < TimelineEditorCreationFlag.kDontCreate: 0 > , 'kRecycleOrCreate': < TimelineEditorCreationFlag.kRecycleOrCreate: 1 > , 'kForceCreation': < TimelineEditorCreationFlag.kForceCreation: 2 > }
    _member_type_: Any = None
    _value2member_map_ = {0: < TimelineEditorCreationFlag.kDontCreate: 0 > , 1: < TimelineEditorCreationFlag.kRecycleOrCreate: 1 > , 2: < TimelineEditorCreationFlag.kForceCreation: 2 > }
    kDontCreate: Any = None
    kRecycleOrCreate: Any = None
    kForceCreation: Any = None

    def __new__(self, cls, value) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
