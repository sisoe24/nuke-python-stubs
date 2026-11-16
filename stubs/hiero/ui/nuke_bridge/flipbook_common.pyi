# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any

kNukeFlipbookCapabilities: dict
kNukeViewerLUTFormat: str

def getColorspaceFromNode(node: Any) -> str:
    """If node is Read or Write it returns the colorspace known value,
    for the remaining nodes 'linear' will be returned
    """

def getIsUsingNukeColorspaces(rootNode: Any) -> bool:
    """Helper function that returns True if the the specified root node is using the original Nuke color management
    and False otherwise, i.e. when OCIO color management is being used.
    """

def getOCIOConfigPath() -> str:
    """Returns the OCIO config filepath used in the Nuke project.
    Returns an empty string if using Nuke Root LUTs
    """

def getRawViewerLUT() -> str:
    """Helper function to return a 'raw' viewer LUT string compatible with the
    current color management mode, and current OCIO config if OCIO color management
    is being used. In the case of OCIO, other than when using the nuke-default
    config, this does a case-insensitive search through the available combinations
    of displays and views, looking for the first view whose name is 'raw' (using a
    case insensitive check). 
    """

def mapViewerLUTString(lut: Any) -> str:
    """Map a viewer LUT string into the form expected by the flipbook viewer """
