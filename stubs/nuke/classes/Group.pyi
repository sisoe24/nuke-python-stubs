from typing import *
from numbers import Number

import nuke

from . import *

class Group(Node):
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

    def nodes(self,) -> list:
        """
        self.nodes() -> List of nodes
        List of nodes in group.
        @return: List of nodes
        """
        ...

    def numNodes(self,) -> Number:
        """
        self.numNodes() -> Number of nodes
        Number of nodes in group.
        @return: Number of nodes
        """
        ...

    def node(self, s:str) -> str:
        """
        self.node(s) -> Node with name s or None.
        Locate a node by name.
        @param s: A string.
        @return: Node with name s or None.
        """
        ...

    def run(self, callable:Callable) -> Callable:
        """
        self.run(callable) -> Result of callable.
        Execute in the context of node. All names are evaluated relative to this object.
        @param callable: callable to execute.
        @return: Result of callable.
        """
        ...

    def begin(self,) -> Group:
        """
        self.begin() -> Group.
        All python code that follows will be executed in the context of node. All names are evaluated relative to this object. Must be paired with end.
        @return: Group.
        """
        ...

    def end(self,) -> None:
        """
        self.end() -> None.
        All python code that follows will no longer be executed in the context of node. Must be paired with begin.
        @return: None.
        """
        ...

    def output(self,) -> Union[Node, None]:
        """
        self.output() -> Node or None.
        Return output node of group.
        @return: Node or None.
        """
        ...

    def selectedNode(self,) -> Union[Node, None]:
        """
        self.selectedNode() -> Node or None.
        Returns the node the user is most likely thinking about. This is the last node the user clicked on, if it is selected.  Otherwise it is an 'output' (one with no selected outputs) of the set of selected nodes. If no nodes are selected then None is returned.
        @return: Node or None.
        """
        ...

    def selectedNodes(self,) -> Union[Node, None]:
        """
        self.selectedNodes() -> Node or None.
        Selected nodes.
        @return: Node or None.
        """
        ...

    def connectSelectedNodes(self,backward, inputA) -> None:
        """
        self.connectSelectedNodes(backward, inputA) -> None.
        Connect the selected nodes.
        @param backward.
        @param inputA.
        @return: None.
        """
        ...

    def splaySelectedNodes(self,backward, inputA) -> None:
        """
        self.splaySelectedNodes(backward, inputA) -> None.
        Splay the selected nodes.
        @param backward.
        @param inputA.
        @return: None.
        """
        ...

    def expand(self,) -> None:
        """
        self.expand() -> None.
        Moves all nodes from the group node into its parent group, maintaining node input
        and output connections, and deletes the group.
        Returns the nodes that were moved, which will also be selected.
        @return: None.
        """
        ...

    def __enter__(self,*args, **kwargs) -> None:
        """

        """
        ...

    def __exit__(self,*args, **kwargs) -> None:
        """

        """
        ...

    def __reduce_ex__(self,*args, **kwargs) -> None:
        """
        Helper for pickle.
        """
        ...

    def subgraphLocked(self,*args, **kwargs) -> None:
        """

        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
