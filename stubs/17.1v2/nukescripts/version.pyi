# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any

class Versions:
    @staticmethod
    def fileknob_from_class(className: Any) -> str | None: ...

def version_down(n: Any = ...) -> None:
    """All new version_down that uses the version_get/set functions.
    This script takes the render version up one in selected iread/writes.
    """

def version_get(string: Any, prefix: Any, suffix: Any = ...) -> tuple[Any, str]:
    """Extract version information from filenames used by DD (and Weta, apparently)
    These are _v# or /v# or .v# where v is a prefix string, in our case
    we use "v" for render version and "c" for camera track version.
    See the version.py and camera.py plugins for usage.
    """

def version_latest() -> None:
    """Like version_up, but only goes up to the highest numbered version
    that exists.

    Works on all selected Read nodes, or all Read nodes if nothing is
    selected.

    Does not modify Write nodes.
    """

def version_set(string: Any, prefix: Any, oldintval: Any, newintval: Any) -> str:
    """Changes version information from filenames used by DD (and Weta, apparently)
    These are _v# or /v# or .v# where v is a prefix string, in our case
    we use "v" for render version and "c" for camera track version.
    See the version.py and camera.py plugins for usage.
    """

def version_up(n: Any = ...) -> None:
    """All new version_up that uses the version_get/set functions.
    This script takes the render version up one in selected iread/writes.
    """
