# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any

class R3DLggParamConverter:
    """Functor for converting the R3D lift-gamma-gain parameters from the way
    they're stored in old hrox files to the values needed for the knobs.
    The maths here is taken directly from the C++ code which has to do this
    conversion for passing to the R3D SDK.
    """
    def __call__(self, value: Any) -> str: ...
    def __init__(self, isLift: Any) -> None: ...

def convertLegacyHroxFile(srcPath: Any, dstPath: Any) -> None:
    """Convert an hrox file to the format used by Nuke 11.1 (and later). Throws
    if there are any errors.
    """

def convertLegacyHroxString(srcStr: Any, dstPath: Any) -> Any:
    """Convert hrox XML data stored in a string, and return the result as a string.
    dstPath is the path the file will be written to, which is used for putting the
    project's name into the XML
    """
