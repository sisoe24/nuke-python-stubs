"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class CascadingEnumeration_Knob(Enumeration_Knob):
    """
    Stores a single value between 0 and some maximum, and manages a
    set of keywords visible to the user. The words themselves are
    displayed on a pulldown list in the user interface, and are written
    to the saved scripts (so that the numerical values can change). To
    create cascading submenus simply use the forward slash ( '/' )
    e.g. menu/item1self.__init__(name, label, items) -> None
    @param name: Name.
    @param label: Label.
    @param items: List of strings.
    Example:
    k = nuke.Enumeration_Knob('MyEnumKnobName', 'MyEnumKnobLabel', ['menu1/label1', 'label2'])
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
