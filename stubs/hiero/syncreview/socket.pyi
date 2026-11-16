# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from hiero.core.util import asBytes as asBytes
from hiero.syncreview import config as config
from hiero.syncreview.eventloop import Timer as Timer
from hiero.syncreview.log import logDebug as logDebug

class Socket:
    """Class which wraps around a zmq socket and allows for integration into an asyncio event loop."""
    def __init__(self) -> None: ...
    def close(self) -> None:
        """Close the socket and reset its state """
    def setDataReceivedCallback(self, callback: Any) -> None: ...
    def socketId(self) -> str:
        """Get the zmq socket id. If the socket was not yet created returns an
        empty string
        """

class ClientSocket(Socket):
    """Socket which connects to a port and uses a DEALER socket for communications 
    with a server.
    """
    def __init__(self) -> None: ...
    def connectToHost(self, url: Any) -> None: ...
    def send(self, frames: Any) -> None: ...

class ServerSocket(Socket):
    """Socket which binds on a port and uses a ROUTER socket which can route messages 
    to multiple clients.
    """
    def __init__(self) -> None: ...
    def bind(self, url: Any) -> None:
        """Create the socket and bind on the specified url.
    
        """
    def send(self, receiver: Any, frames: Any) -> None:
        """Send message frames to a given receiver. """
