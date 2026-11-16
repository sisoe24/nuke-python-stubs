# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.syncreview.synctool as _hiero_syncreview_synctool
from hiero.syncreview import messages as messages
from hiero.syncreview.messagedispatcher import MessageDispatcher as MessageDispatcher
from hiero.syncreview.synctool import SyncTool as SyncTool

class ClientDataProvider(_hiero_syncreview_synctool.SyncTool):
    """Class that holds connected client data. The key of this dictionary is the unique ID of the client. The value is a
    tuple holding the client name and a tuple of the RGB color associated to it.
    """
    clientDataChanged: Any
    clientDataCleared: Any
    staticMetaObject: Any
    def __init__(self, messageDispatcher: Any) -> None: ...
    def shutdown(self) -> None: ...

class ClientSyncGuest(ClientDataProvider):
    """Makes available the connected client data received from the server's ClientSyncHost tool. """
    staticMetaObject: Any
    def __init__(self, messageDispatcher: Any) -> None: ...

class ClientSyncHost(ClientDataProvider):
    """Listens for connections from other clients, updates the connected client data and sends it to guests. """
    staticMetaObject: Any
    def __init__(self, messageDispatcher: Any) -> None: ...
    def addGuest(self, clientId: Any, clientData: Any) -> None:
        """Adds a new guest to the client data without sending notifications to clients. """
