# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from hiero.core import ApplicationSettings as ApplicationSettings
from hiero.syncreview import config as config
from hiero.syncreview.connectionmanager import ConnectionManager as ConnectionManager
from hiero.syncreview.connectionstate import ConnectionState as ConnectionState
import hiero as hiero

class ConnectDialog:
    """Dialog for connecting as a client, allowing the user to specify the hostname
    and port to connect on
    """
    CANCELLED_CONNECTION_LABEL: str
    DEFAULT_ERROR_MESSAGE: str
    ERROR_LABEL: str
    READY_TO_CONNECT_LABEL: str
    staticMetaObject: Any
    def __init__(self, connectionManager: Any, parent: Any = ...) -> None: ...
    def cancel(self) -> None:
        """Close the dialog and cancel any in-progress connections """
    def connect(self) -> None:
        """Try to connect with the current settings """
    def getClientData(self) -> tuple[Any, tuple[Any, Any, Any]]:
        """Get the current client data info from the dialog """
    def getHostAndPort(self) -> tuple[Any, Any]:
        """Get the hostname and port to connect to """
    def onConnectDetailsChanged(self) -> None:
        """Called whenever the hostname or port is edited. If a connection attempt was
        already in progress, it will be cancelled.
        """
    def onConnectError(self, error: Any, errorText: Any) -> None:
        """Connection error handling """
    def onConnectionStateChanged(self, state: Any) -> None:
        """Connection state change handling """
    def setStatusConnecting(self) -> None:
        """Show the connecting spinner """
    def setStatusText(self, text: Any) -> None:
        """Set the status label text """
    def updateConnectButtonEnabled(self) -> None:
        """Set if the connect button is enabled state based on the connection state
        and the settings. At the moment it just checks if the hostname field has anything
        in it. We could maybe make this check the host is valid before the user tries to
        connect
        """

class _PasteFilter:
    staticMetaObject: Any
    def __init__(self, callback: Any, parent: Any = ...) -> None: ...
    def eventFilter(self, _: Any, event: Any) -> bool: ...

class _PasteLineEdit:
    staticMetaObject: Any
    def __init__(self, callback: Any, parent: Any = ...) -> None: ...
    def contextMenuEvent(self, event: Any) -> None: ...
    def createPasteContextMenu(self) -> Any: ...

class _PasteSpinBox:
    staticMetaObject: Any
    def __init__(self, callback: Any, parent: Any = ...) -> None: ...
    def contextMenuEvent(self, event: Any) -> None: ...
