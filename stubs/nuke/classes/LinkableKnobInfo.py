"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class LinkableKnobInfo(object):
    """
    A linkable knob description. Holds a reference to a knob that may be linked to, as well as an indication whether this knob should be used as part of an absolute or relative expression and whether it is enabled.
    """

    def __getattribute__(self, name, ) -> None:
        """
        Return getattr(self, name).
        """
        ...

    def __setattr__(self, name, value, ) -> None:
        """
        Implement setattr(self, name, value).
        """
        ...

    def __delattr__(self, name, ) -> None:
        """
        Implement delattr(self, name).
        """
        ...

    def knob(self,) -> Knob:
        """
        self.knob() -> Knob
        Returns the knob that may be linked to.
        """
        ...

    def absolute(self,) -> bool:
        """
        self.absolute() -> Boolean
        Returns whether the values of this knob should be treated as absolute or relative. This may be useful for positions.
        """
        ...

    def enabled(self,) -> bool:
        """
        self.enabled() -> Boolean
        Returns whether the knob is currently enabled or not.
        """
        ...

    def displayName(self,) -> str:
        """
        self.displayName() -> String
        Returns the custom display name that will appear in Link-to menus.
        """
        ...

    def indices(self,) -> List:
        """
        self.indices() -> List
        Returns a list of the knob channels that should be used with this linkable knob.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
