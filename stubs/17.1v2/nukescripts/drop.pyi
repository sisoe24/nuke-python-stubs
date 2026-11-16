# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any

def addDropDataCallback(callback: Any) -> None:
    """Add a function to the list of callbacks. This function will called whenever data is dropped onto the DAG. Override it to perform other actions.
    If you handle the drop, return True, otherwise return None.
    """

def dropData(mimeType: Any, text: Any) -> bool | None:
    """Handle data drops by invoking the list of callback functions until one has
    handled the event
    """
