# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import hiero.syncreview.synctool as _hiero_syncreview_synctool
from hiero.syncreview import messages as messages
from hiero.syncreview.messagedispatcher import MessageDispatcher as MessageDispatcher
from hiero.syncreview.synctool import SyncTool as SyncTool

class ClientDataProvider(_hiero_syncreview_synctool.SyncTool):
    """Class that holds connected client data. The key of this dictionary is the unique ID of the client. The value is a
    tuple holding the client name and a tuple of the RGB color associated to it.
    """
    clientDataChanged: _PySide6_QtCore.Signal
    clientDataCleared: _PySide6_QtCore.Signal
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, messageDispatcher: Any) -> None: ...
    def shutdown(self) -> None: ...

class ClientSyncGuest(ClientDataProvider):
    """Makes available the connected client data received from the server's ClientSyncHost tool. """
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, messageDispatcher: Any) -> None: ...

class ClientSyncHost(ClientDataProvider):
    """Listens for connections from other clients, updates the connected client data and sends it to guests. """
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, messageDispatcher: Any) -> None: ...
    def addGuest(self, clientId: Any, clientData: Any) -> None:
        """Adds a new guest to the client data without sending notifications to clients. """
