# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from hiero.syncreview import config as config
from hiero.syncreview import messages as messages
from hiero.syncreview.client import allowClientTimeout as allowClientTimeout
from hiero.syncreview.connectionstate import ConnectionState as ConnectionState
from hiero.syncreview.eventloop import Timer as Timer
from hiero.syncreview.log import logDebug as logDebug
from hiero.syncreview.log import logMessage as logMessage
from hiero.syncreview.socket import ServerSocket as ServerSocket

class ClientConnection:
    """Per-client state for the server """
    def __init__(self, socketId: Any, allowTimeout: Any) -> None: ...
    def disconnected(self) -> None: ...
    def resetHeartbeatTimer(self) -> None: ...

class Server:
    """A server listening on connections from clients and routing messages."""
    def __init__(self) -> None: ...
    def bind(self, port: Any) -> None: ...
    def sendMessageToAllClients(self, msg: Any, exclude: Any = ...) -> None:
        """Send a message to connected clients, optionally excluding one
    
        """
    def shutdown(self) -> None: ...
