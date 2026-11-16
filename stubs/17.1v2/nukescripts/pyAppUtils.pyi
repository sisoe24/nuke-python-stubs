# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any

class pyAppHelper:
    """Helper class to run python commands in a separate thread. """
    def __init__(self, start: Any = ...) -> None:
        """constructor """
    def initiate(self) -> None:
        """Start the thread associated with this object """
    def run(self, call: Any, args: Any = ..., kwargs: Any = ...) -> None:
        """Runs the specified call in a separate thread. """
    def terminate(self) -> None:
        """Terminated the thread associated with this object """
