# Type stubs for fxhost 1.0v1. Generated; do not edit.

from typing import Any
from . import utils as utils
from fxhost.utils import frame_range as frame_range

ADD_VIEWS: int
EXE_PATH: str
VERSION: str

class Format:
    """Has C-level data descriptors."""
    height: Any
    width: Any

class GeoSelectionItem:
    def getWorldPoints(self, stage: Any, time: float = ...) -> Any:
        """getWorldPoints(self: _nuke.GeoSelectionItem, stage: usg::Stage, time: float = nan) -> usg::Array<fdk::Vec3<float> >
        
        """

class Knob: ...

class Node:
    def __getitem__(self, *args: Any, **kwargs: Any) -> Any:
        """Return self[key]."""
    def __len__(self, *args: Any, **kwargs: Any) -> int:
        """Return len(self)."""
    def knob(self, p: Any, follow_link: Any = ...) -> Any:
        """self.knob(p[, follow_link]) -> The knob named p or the pth knob.
        @param p: A string or an integer.
        @param follow_link: Should it follow links to Link_Knob until resolution. Default is True.
        @return: The knob named p or the pth knob.
        """
    def name(self) -> str:
        """self.name() -> str
        @return: Name of node.
        """

class Sequence:
    """Reports a module name that cannot be imported, as hiero classes do."""
    def videoTracks(self) -> Any:
        """self.videoTracks() -> returns a tuple of the video tracks in this sequence."""

class TimelineEditor:
    selectionChanged: Any
    def sequence(self) -> Any:
        """self.sequence() -> returns the sequence that this editor is displaying."""

class Track:
    def items(self) -> Any:
        """self.items() -> tuple of the items on this track."""

def allNodes(filter: Any = ..., group: Any = ...) -> Any:
    """allNodes(filter, group) -> List.

    List of all nodes in a group. If you need to get all the nodes in the script
    from a context which has no child nodes, for instance a control panel, use
    nuke.root().nodes().

    :param filter: Optional. Only return nodes of the specified class.
    :param group: Optional. If the group is omitted the current group (ie the group the user picked a menu item from the toolbar of) is used.
    :param recurseGroups: Optional. If True, will also return all child nodes within any group nodes. This is done recursively and defaults to False.
    :return: List
    """

def root() -> Any:
    """root() -> node

    Get the DAG's root node. Always succeeds.

    :return: The root node. This will never be None.
    """

def toNode(s: Any) -> Node:
    """toNode(s) -> Node

    Search for a node in the DAG by name and return it as a Python object.

    :param s: Node name.
    :return: Node or None if it does not exist.
    """

def withTextSignature(module: Any, name: Any, index: Any = ..., /) -> Any:
    """A C function that does declare a signature."""
