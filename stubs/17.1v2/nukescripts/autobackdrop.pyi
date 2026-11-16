# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any

def autoBackdrop() -> Any:
    """Automatically puts a backdrop behind the selected nodes.
    The backdrop will be just big enough to fit all the select nodes in, with room
    at the top for some text in a large font.
    """

def nodeIsInside(node: Any, backdropNode: Any) -> bool:
    """Checks whether the node geometry is inside backdropNode

    :return: `True` if it is, `False` otherwise
    :rtype: bool
    """
