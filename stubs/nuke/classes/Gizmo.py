"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class Gizmo(Group):
    """

    """

    def __repr__(self) -> str:
        """
        Return repr(self).
        """
        ...

    def __str__(self) -> str:
        """
        Return str(self).
        """
        ...

    def __len__(self) -> int:
        """
        Return len(self).
        """
        ...

    def __getitem__(self, key: Any) -> Any:
        """
        Return self[key].
        """
        ...

    def command(self,) -> str:
        """
        self.command() -> String.
        Gizmo command.
        @return: String.
        """
        ...

    def filename(self,) -> str:
        """
        self.filename() -> String.
        Gizmo filename.
        @return: String.
        """
        ...

    def makeGroup(self,) -> Group:
        """
        self.makeGroup() -> Group
        Creates a Group node copy of the Gizmo node.
        @return: Group.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
