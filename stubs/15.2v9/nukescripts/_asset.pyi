# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import nuke as nuke

Iterable: Any

class ResolveAccess:
    """Members:

    kRead

    kManagerDriven
    """
    kManagerDriven: ResolveAccess
    kRead: ResolveAccess
    def __eq__(self, other: object) -> bool:
        """__eq__(self: object, other: object) -> bool"""
    def __getstate__(self) -> int:
        """__getstate__(self: object) -> int"""
    def __hash__(self) -> int:
        """__hash__(self: object) -> int"""
    def __index__(self) -> int:
        """__index__(self: openassetio._openassetio.access.ResolveAccess) -> int"""
    def __init__(self, value: int) -> None:
        """__init__(self: openassetio._openassetio.access.ResolveAccess, value: int) -> None"""
    def __int__(self) -> int:
        """__int__(self: openassetio._openassetio.access.ResolveAccess) -> int"""
    @property
    def __members__(self) -> dict:
        """__members__(arg0: handle) -> dict"""
    def __ne__(self, other: object) -> bool:
        """__ne__(self: object, other: object) -> bool"""
    def __repr__(self) -> str:
        """__repr__(self: object) -> str"""
    def __setstate__(self, state: int) -> None:
        """__setstate__(self: openassetio._openassetio.access.ResolveAccess, state: int) -> None"""
    def __str__(self) -> str:
        """name(self: handle) -> str"""
    @property
    def name(self) -> str:
        """name(self: handle) -> str"""
    @property
    def value(self) -> int:
        """(arg0: openassetio._openassetio.access.ResolveAccess) -> int"""

def deassetize(nodes: Any) -> tuple:
    """Finds all assetized File_Knob's in nodes and replaces their entity reference
    by their respective resolved file path.

    :param nodes:      A list of nodes to be deassetized

    :return: A tuple. The first element is a boolean that is True if all assetized
             knobs were successfully deassetized and the second is a list of
             unresolved knobs that are assetized but failed to be resolved.

             If OpenAssetIO isn't correctly configured, (False, []) is returned.
    """
