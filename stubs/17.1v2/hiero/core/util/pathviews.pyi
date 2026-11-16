# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any

def findViewInPath(path: Any, views: Any) -> Any:
    """Try to find a view name in a path from the list of views. If successful,
    returns a list of the matched view name and the path with %v/%V substituted.
    Otherwise returns None.
    """

def formatMultiViewPath(path: Any, view: Any) -> Any:
    """Format a path string with %v/V placeholders with a view name """

def isMultiViewPath(path: Any) -> bool:
    """Test if a path contains %v placeholders for multiple views """
