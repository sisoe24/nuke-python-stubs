from typing import *
from numbers import Number

import nuke

from . import *


class Gizmo(Group):
    """

    """

    def __repr__(self, ) -> None:
        """
        Return repr(self).
        """
        ...

    def __str__(self, ) -> None:
        """
        Return str(self).
        """
        ...

    def __len__(self, ) -> None:
        """
        Return len(self).
        """
        ...

    def __getitem__(self, key, ) -> None:
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
