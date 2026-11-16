# Type stubs for nuke 17.1v2. Generated; do not edit.

"""A collection of tools and functions to help manage LUTs and color configuration"""

from typing import Any
from nuke import getOcioColorSpaces as getOcioColorSpaces
from nuke import usingOcio as usingOcio
from nuke_internal import callbacks as callbacks

defaultLUTMappers: dict

class ColorspaceLookupError(Exception):
    """an excpetion that should be thrown when looking up the colorspace """

def addDefaultColorspaceMapper(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Add a function to modify default colorspaces before Nuke passes them to
    Readers or Writers.

    Functions should have the same positional argument as in the definition of
    defaultLUTMapper()

    All added functions are called in backwards order.
    """

def defaultColorspaceMapper(colorspace: Any, dataTypeHint: Any) -> str:
    """Called by libnuke.
    Calls into Node-level callbacks first, then global callbacks

    Arguments:
        colorspace   - the name string of the initial colorspace
        dataTypeHint - sometimes Readers/Writer request the default for a
                       particular data-type, i.e. int8, in16, float, etc.
    Return:
        The return should be the transformed/modified colorspace name.
        None is the same as returning the string unchanged.
    """

def getColorspaceList(colorspaceKnob: Any) -> list[Any]:
    """Get a list of all colorspaces listed in an enumeration knob.
    This will strip family names if the knob has the STRIP_CASCADE_PREFIX flag set.
    """

def removeDefaultColorspaceMapper(call: Any, args: Any = ..., kwargs: Any = ..., nodeClass: str = ...) -> None:
    """Remove a previously-added callback with the same arguments."""
