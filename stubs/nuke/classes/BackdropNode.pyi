from typing import *
from numbers import Number

import nuke

from . import *

class BackdropNode(Node):
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

    def selectNodes(self,selectNodes) -> None:
        """
        self.selectNodes(selectNodes) -> None
        Select or deselect all nodes in backdrop node
        Example:
        backdrop = nuke.toNode("BackdropNode1")
        backdrop.selectNodes(True)

        @return: None.
        """
        ...

    def getNodes(self,) -> list:
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
