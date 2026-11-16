# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
from hiero.syncreview import config as config
from hiero.syncreview import syncreviewstatuspanel as syncreviewstatuspanel
from hiero.syncreview.connectdialog import ConnectDialog as ConnectDialog
from hiero.syncreview.connectionmanager import ConnectionManager as ConnectionManager
from hiero.syncreview.connectionstate import ConnectionState as ConnectionState
from hiero.syncreview.messages import Notification as Notification
from hiero.syncreview.sessionsetupdialog import SessionSetupDialog as SessionSetupDialog
import hiero as hiero
import nuke as nuke

class ClientConnectUI(_PySide6_QtCore.QObject):
    """Class for handling showing dialogs and error messages when connecting as a
    client to a sync session.
    """
    DISCONNECTED_MSGBOX_TEXT: str
    DISCONNECTED_MSGBOX_TITLE: str
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, connectionManager: Any) -> None: ...
    def connectClient(self, autoConnect: bool = ...) -> None:
        """Connect as a client to a running server, showing UI to get the host and port
        to connect on. If autoConnect is True, will show the dialog and try to connect
        automatically with the previous settings
        """
    def disconnectClient(self) -> None:
        """Disconnect the client """
    def onConnectStateChanged(self, newState: Any, oldState: Any) -> None: ...
    def onConnectionError(self, error: Any, errorText: Any) -> None:
        """Handle connection errors. If a connection is lost, gives the user the option
        to reconnect.
        """

class HostUI(_PySide6_QtCore.QObject):
    """Class for handling showing dialogs and error messages when acting as host
    in a sync session.
    """
    SAVE_PROJECT_MSGBOX_TEXT: str
    SAVE_PROJECT_MSGBOX_TITLE: str
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, connectionManager: Any) -> None: ...
    def startServer(self) -> None:
        """Start the server, getting the port from the user """
    def stopServer(self) -> None:
        """Stop the server if it was running """

class MenuBuilder(_PySide6_QtCore.QObject):
    """Class which handles the menu logic for the sync functionality """
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, connectionManager: Any) -> None: ...
    def createMenus(self) -> None:
        """Add entries to the file menu for managing the connection """
    def updateMenuEnabledStates(self) -> None:
        """Set the enabled states of sync menu actions """
