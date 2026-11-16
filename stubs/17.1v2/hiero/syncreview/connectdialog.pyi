# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import PySide6.QtWidgets as _PySide6_QtWidgets
from hiero.core import ApplicationSettings as ApplicationSettings
from hiero.syncreview import config as config
from hiero.syncreview.connectionmanager import ConnectionManager as ConnectionManager
from hiero.syncreview.connectionstate import ConnectionState as ConnectionState
import hiero as hiero

class ConnectDialog(_PySide6_QtWidgets.QDialog):
    """Dialog for connecting as a client, allowing the user to specify the hostname
    and port to connect on
    """
    CANCELLED_CONNECTION_LABEL: str
    DEFAULT_ERROR_MESSAGE: str
    ERROR_LABEL: str
    READY_TO_CONNECT_LABEL: str
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, connectionManager: Any, parent: Any = ...) -> None: ...
    def cancel(self) -> None:
        """Close the dialog and cancel any in-progress connections """
    def connect(self) -> None:
        """Try to connect with the current settings """
    def getClientData(self) -> tuple[str, tuple[Any, Any, Any]]:
        """Get the current client data info from the dialog """
    def getHostAndPort(self) -> tuple[str, int]:
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

class _PasteFilter(_PySide6_QtCore.QObject):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, callback: Any, parent: Any = ...) -> None: ...
    def eventFilter(self, _: Any, event: Any) -> bool: ...

class _PasteLineEdit(_PySide6_QtWidgets.QLineEdit):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, callback: Any, parent: Any = ...) -> None: ...
    def contextMenuEvent(self, event: Any) -> None: ...
    def createPasteContextMenu(self) -> Any: ...

class _PasteSpinBox(_PySide6_QtWidgets.QSpinBox):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, callback: Any, parent: Any = ...) -> None: ...
    def contextMenuEvent(self, event: Any) -> None: ...
