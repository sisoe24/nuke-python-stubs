# Type stubs for nuke 15.2v9. Generated; do not edit.

"""Functions used by the UnrealReader node"""

from typing import Any
import nuke as nuke
import nukescripts as nukescripts

def cameraClass(node: Any) -> str:
    """Returns the correct camera class for the 3D system in use."""

def createCamera(unrealReaderNode: Any) -> None:
    """Create a camera node based on the values set in the given unreal reader node"""

def createReadNode(unrealReaderNode: Any) -> None:
    """Create a read node for the rendered output"""

def new3D(node: Any) -> bool:
    """Checks if the node is using the new 3D system."""
