# Type stubs for nuke 17.1v2. Generated; do not edit.

"""This module contains classes for performing a capture of the viewer."""

from typing import Any

class CaptureViewer:
    """This class provides a way of capturing the contents of the viewer to disk.
    
    """
    def __call__(self) -> None:
        """Start the capture.
        
        """
    def __init__(self, flipbook: Any, frameRange: Any, viewer: Any, selectedViews: Any, defaultWritePath: Any, customWritePath: Any, doFlipbook: Any, doCleanup: Any) -> None: ...
