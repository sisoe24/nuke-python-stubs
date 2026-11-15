"""Stand-in for a host C extension.

Docstrings are copied from Nuke 15.0v1. Bodies are irrelevant: `_builtin`
removes the signature, as a C function without `__text_signature__` has none.
"""
from __future__ import annotations

from PySide2.QtCore import Signal


def _builtin(func):
    # inspect.signature raises TypeError on a non-Signature __signature__.
    func.__signature__ = False
    return func


VERSION = '1.0v1'
ADD_VIEWS = 1
EXE_PATH = '/Applications/Host/host'


@_builtin
def allNodes(*args, **kwargs):
    """allNodes(filter, group) -> List.

    List of all nodes in a group. If you need to get all the nodes in the script
    from a context which has no child nodes, for instance a control panel, use
    nuke.root().nodes().

    :param filter: Optional. Only return nodes of the specified class.
    :param group: Optional. If the group is omitted the current group (ie the group the user picked a menu item from the toolbar of) is used.
    :param recurseGroups: Optional. If True, will also return all child nodes within any group nodes. This is done recursively and defaults to False.
    :return: List
    """


@_builtin
def root(*args, **kwargs):
    """root() -> node

    Get the DAG's root node. Always succeeds.

    :return: The root node. This will never be None.
    """


@_builtin
def toNode(*args, **kwargs):
    """toNode(s) -> Node

    Search for a node in the DAG by name and return it as a Python object.

    :param s: Node name.
    :return: Node or None if it does not exist.
    """


def withTextSignature(name, index=0):
    """A C function that does declare a signature."""


withTextSignature.__text_signature__ = '($module, name, index=0, /)'


class Knob:
    pass


class Node:
    @_builtin
    def knob(self, *args, **kwargs):
        """self.knob(p[, follow_link]) -> The knob named p or the pth knob.
        @param p: A string or an integer.
        @param follow_link: Should it follow links to Link_Knob until resolution. Default is True.
        @return: The knob named p or the pth knob.
        """

    @_builtin
    def name(self, *args, **kwargs):
        """self.name() -> str
        @return: Name of node.
        """

    @_builtin
    def __getitem__(self, *args, **kwargs):
        """Return self[key]."""

    @_builtin
    def __len__(self, *args, **kwargs):
        """Return len(self)."""


class GeoSelectionItem:
    @_builtin
    def getWorldPoints(self, *args, **kwargs):
        """getWorldPoints(self: _nuke.GeoSelectionItem, stage: usg::Stage, time: float = nan) -> usg::Array<fdk::Vec3<float> >
        """


class Format:
    """Has C-level data descriptors."""
    __slots__ = ('width', 'height')


class Sequence:
    """Reports a module name that cannot be imported, as hiero classes do."""

    @_builtin
    def videoTracks(self, *args, **kwargs):
        """self.videoTracks() -> returns a tuple of the video tracks in this sequence."""


Sequence.__module__ = 'core'


class TimelineEditor:
    selectionChanged = Signal()

    @_builtin
    def sequence(self, *args, **kwargs):
        """self.sequence() -> returns the sequence that this editor is displaying."""
