# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any

def autoBackdrop() -> Any:
    """Automatically puts a backdrop behind the selected nodes.

    The backdrop will be just big enough to fit all the select nodes in, with room
    at the top for some text in a large font.
    """

def nodeIsInside(node: Any, backdropNode: Any) -> Any:
    """Returns true if node geometry is inside backdropNode otherwise returns false"""
