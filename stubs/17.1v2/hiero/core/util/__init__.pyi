# Type stubs for nuke 17.1v2. Generated; do not edit.

"""Utility functions for Hiero."""

from typing import Any
from . import filesystem as filesystem
from . import pathviews as pathviews
from . import system as system
from hiero.core.util.pathviews import findViewInPath as findViewInPath
from hiero.core.util.pathviews import formatMultiViewPath as formatMultiViewPath
from hiero.core.util.pathviews import isMultiViewPath as isMultiViewPath
import hiero as hiero

def GetClipFrameRange(clip: Any, trimmed: bool = ...) -> tuple[Any, Any]: ...

def HasFrameIdentifier(path: Any) -> list[Any]:
    """Returns true if the path contains either ### or %4d notation for the frame identifier"""

def HashesToPrintf(original: Any) -> str:
    """Convert hashes in the given string into printf style notation."""

def ResizePadding(path: Any, minimum: Any) -> str:
    """Return path with padding width increased to minimum size"""

def SequenceifyFilename(filename: Any, addPadding: Any) -> Any: ...

def asBytes(value: Any) -> bytes:
    """Get value as bytes, encoded as a UTF-8 string if the input was not bytes """

def asUnicode(value: Any) -> str:
    """Get value as a unicode string. If the input is bytes, decode it from UTF-8. """

def coresPerCPUSocket() -> float:
    """Return how many cores are availble on a single cpu socket. This assumes that all CPUs on
    a multi CPU system have the same number of cores.
    """

def flattenedPathRemappings() -> list[Any]:
    """Get a list of path remappings set in the preferences where each entry is a
    tuple of from/to paths appropriate for the current OS 
    """

def hasMultipleCPUSockets() -> bool:
    """Return whether this system has multiple CPU sockets."""

def remapPath(path: Any) -> Any:
    """Apply remapping preferences to a path and return the remapped path, or if
    no remaps were found, the original path.
    """

def singleCPUSocketLaunchArguments() -> tuple[str, str, str] | tuple[str, str, str, str, str, str, str, str, str, str]:
    """Return the arguments required to launch a process that is limited to
    a single CPU. These arguments should be prepended to the command that
    is to be run.
    """

def uniqueKey(key: Any, dictionary: Any) -> Any:
    """uniqueKey (key, dictionary)
    If key clashes in dictionary, add/identify trailing number and increment.
    return new key
    """

def uniquify(seq: Any) -> list[Any]:
    """uniquify(seq)
    Returns a unique, order-preserved list of items in a Python list or tuple.
    Compatible with hashable items such as dicts.
    @param seq: a Python list or sequence.
    @returns: list of unique items.

    Example:

    A = ['a', (0,1), [4,'2'], (0,1), 'b', {'foo':1}, 'b', 'a', [4,'2'], {'foo':1}]
    uniquify(A)
    Result: ['a', (0, 1), [4, '2'], 'b', {'foo': 1}]
    """

def version_get(string: Any, prefix: Any, suffix: Any = ...) -> tuple[Any, str]:
    """Extract version information from filenames
    These are _v# or /v# or .v# where v is a prefix string, in our case
    we use "v" for render version and "c" for camera track version.
    See the version.py and camera.py plugins for usage.
    """

def version_set(string: Any, prefix: Any, oldintval: Any, newintval: Any) -> str:
    """Changes version information from filenames
    These are _v# or /v# or .v# where v is a prefix string, in our case
    we use "v" for render version and "c" for camera track version.
    See the version.py and camera.py plugins for usage.
    """
