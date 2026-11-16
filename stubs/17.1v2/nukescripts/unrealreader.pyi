# Type stubs for nuke 17.1v2. Generated; do not edit.

"""Functions used by the UnrealReader node"""

from typing import Any
import nuke as nuke

def cameraClass(node: Any) -> str:
    """Returns the correct camera class for the 3D system in use."""

def classic3D(node: Any) -> bool:
    """Checks if the node is using the classic 3D system."""

def createCamera(unrealReaderNode: Any) -> None:
    """Create a camera node based on the values set in the given unreal reader node"""

def createReadNode(unrealReaderNode: Any) -> None:
    """Create a read node for the rendered output"""
