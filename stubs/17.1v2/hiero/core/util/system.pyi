# Type stubs for nuke 17.1v2. Generated; do not edit.

"""Module for querying CPU related system information"""

from hiero.core import log as log

class SystemInfo:
    """Query CPU related information about this system."""
    def __init__(self) -> None: ...
    def coresPerSocket(self) -> float:
        """Return how many cores are available per CPU socket. This assumes that all CPUs on
        a multi CPU system have the same number of cores.
        """
    def singleSocketLaunchArguments(self) -> tuple[str, str, str] | tuple[str, str, str, str, str, str, str, str, str, str]:
        """Return the arguments requried to launch a process that is limited to
        a single CPU. These arguments should be prepended to the command that
        is to be run.
        """
    def socketCount(self) -> int:
        """Return how many CPU sockets are available."""
