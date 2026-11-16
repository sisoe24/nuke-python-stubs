# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
from nukescripts import nodes as nodes

def autocrop(first: Any = ..., last: Any = ..., inc: Any = ..., layer: str = ...) -> None:
    """Run the CurveTool's AutoCrop function on each selected node over the
    specified frame range and channels. If the range values are None, the
    project first_frame and last_frame are used; if inc is None, 1 is used.
    After execution, the CurveTool AutoCrop results are copied into a Crop
    node attached to each selected node.
    """
