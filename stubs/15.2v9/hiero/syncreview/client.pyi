# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from hiero.syncreview import config as config
from hiero.syncreview import messages as messages
from hiero.syncreview.connectionstate import ConnectionState as ConnectionState
from hiero.syncreview.eventloop import Timer as Timer
from hiero.syncreview.log import logDebug as logDebug
from hiero.syncreview.log import logException as logException
from hiero.syncreview.log import logMessage as logMessage
from hiero.syncreview.socket import ClientSocket as ClientSocket

class Client:
    """Class representing a client in the sync. Maintains a connection to the server
    and allows for sending and receiving messages.
    """
    def __init__(self, connectionState: Any, clientId: Any) -> None: ...
    def connectToHost(self, host: Any, port: Any, clientData: Any) -> None:
        """Try to connect on the given host and port. May raise an exception if the
        host isn't valid.
        """
    def connectionState(self) -> Any:
        """Get the client's connection state """
    def disconnectFromHost(self) -> None:
        """Close the connection. If a connection had been successfully established
        with the host, a disconnect message is sent, otherwise just close the socket
        etc
        """
    def sendMessage(self, msg: Any) -> None: ...
    def setMessageReceivedCallback(self, callback: Any) -> None: ...
    def setNumberOfClientsChangedCallback(self, callback: Any) -> None: ...
    def socketId(self) -> str:
        """Get the socket Id used by this client. """

def allowClientTimeout(clientId: Any) -> Any:
    """Check if the client should time out, this does not happen for the client
    object used by the host.
    """
