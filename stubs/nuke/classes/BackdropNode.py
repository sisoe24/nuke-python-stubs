"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class BackdropNode(Node):
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

    def selectNodes(self, selectNodes: bool) -> None:
        """
        self.selectNodes(selectNodes) -> None
        Select or deselect all nodes in backdrop node
        Example:
        backdrop = nuke.toNode("BackdropNode1")
        backdrop.selectNodes(True)

        @return: None.
        """
        ...

    def getNodes(self) -> list[nuke.Node]:
        """
        self.getNodes() -> a list of nodes contained inside the backdrop
        Get the nodes contained inside a backdrop node
        Example:
        backdrop = nuke.toNode("BackdropNode1")
        nodesInBackdrop = backdrop.getNodes()

        @return: a list of nodes contained inside the backdrop.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
