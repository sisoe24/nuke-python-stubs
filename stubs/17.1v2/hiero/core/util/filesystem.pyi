# Type stubs for nuke 17.1v2. Generated; do not edit.

"""Helper functions for dealing with the filesystem which try to handle
unicode correctly.
"""

from typing import Any
from hiero.core.util import asUnicode as asUnicode

def access(path: Any, mode: Any) -> bool:
    """Wrapper around os.access() """

def exists(path: Any) -> bool:
    """Wrapper around os.path.exists() """

def lexists(path: Any) -> bool:
    """Wrapper around os.path.lexists() """

def makeDirs(dirPath: Any) -> None:
    """Make the directories for the given path if they don't already
    exist.
    """

def openFile(path: Any, *args: Any, encoding: Any = ...) -> Any:
    """Wrapper around open. """

def remove(path: Any) -> None:
    """Wrapper around os.remove. """

def stat(path: Any) -> Any:
    """Wrapper around os.stat() """
