# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any

class ElidedLabel:
    """Class for showing text which is elided if it exceeds the widget's width.
    Note that this can currently only handle showing a single line of text.
    """
    staticMetaObject: Any
    def __init__(self, parent: Any = ...) -> None: ...
    def elideMode(self) -> Any:
        """Get the elide mode. """
    def minimumSizeHint(self) -> Any: ...
    def paintEvent(self, event: Any) -> None: ...
    def setElideMode(self, mode: Any) -> None:
        """Set the elide mode. """
    def setText(self, text: Any) -> None:
        """Set the text to display. """
    def text(self) -> str:
        """Get the text being displayed. """
