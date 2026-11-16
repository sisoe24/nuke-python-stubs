# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.syncreview.client as _hiero_syncreview_client
from hiero.core import executeInMainThread as executeInMainThread
from hiero.syncreview import config as config
from hiero.syncreview import log as log
from hiero.syncreview import messages as messages
from hiero.syncreview.annotationsync import SyncAnnotationsTool as SyncAnnotationsTool
from hiero.syncreview.binitemsync import SyncBinItemTool as SyncBinItemTool
from hiero.syncreview.client import Client as Client
from hiero.syncreview.clientsync import ClientSyncGuest as ClientSyncGuest
from hiero.syncreview.clientsync import ClientSyncHost as ClientSyncHost
from hiero.syncreview.clipknobssync import SyncClipKnobsTool as SyncClipKnobsTool
from hiero.syncreview.connectionstate import ConnectionState as ConnectionState
from hiero.syncreview.cursorsync import SyncClientCursor as SyncClientCursor
from hiero.syncreview.editorialsync import SyncSequenceEditsTool as SyncSequenceEditsTool
from hiero.syncreview.effectitemsync import SyncEffectItemKnobsTool as SyncEffectItemKnobsTool
from hiero.syncreview.eventloop import EventLoop as EventLoop
from hiero.syncreview.inoutsync import SyncInOutTool as SyncInOutTool
from hiero.syncreview.itemstatussync import SyncItemStatusTool as SyncItemStatusTool
from hiero.syncreview.messagedispatcher import MessageDispatcher as MessageDispatcher
from hiero.syncreview.projectsync import HostProjectSyncTool as HostProjectSyncTool
from hiero.syncreview.projectsync import ProjectPushTool as ProjectPushTool
from hiero.syncreview.projectsync import ProjectSyncProgressTool as ProjectSyncProgressTool
from hiero.syncreview.server import Server as Server
from hiero.syncreview.versionsync import SyncVersionsTool as SyncVersionsTool
from hiero.syncreview.viewsync import SyncViewerTool as SyncViewerTool

class Session:
    staticMetaObject: Any
    def __init__(self) -> None: ...
    def clientDataProvider(self) -> None:
        """Holds data about the current participants of a sync review session. """

class ClientSession(Session):
    """Class representing a session running with a client connected to an external
    server.
    """
    staticMetaObject: Any
    def __init__(self, hostname: Any, port: Any, connectionState: Any, clientData: Any) -> None: ...
    def stop(self) -> None: ...

class ConnectionManager:
    """Class for managing the connection state of the sync review functionality.
    This can be used to either start a listening server, or to connect a client to
    a running server.

    When running a session object will be created which sets up all the logic for
    the sync functionality and message dispatch.

    Note that in either case, a Client object is created. When running in server
    mode, this will connect locally and be used for the sending and receiving of
    messages.
    """
    numberOfClientsChanged: Any
    staticMetaObject: Any
    def __init__(self) -> None: ...
    def connectClient(self, hostname: Any, port: Any, clientData: Any) -> None:
        """Connect as a client to the given hostname and port """
    def disconnectClient(self) -> None:
        """Disconnect the client """
    def getConnectionInfo(self) -> None:
        """Get the current connection info """
    def getProjects(self) -> list[Any]:
        """Get the project used for the sync session """
    def onConnectionStateChanged(self, state: Any) -> None:
        """Callback when the connection state changes. Resets the session when
        disconnected for any reason
        """
    def pushSession(self) -> None:
        """Pushes the project to all other clients. """
    def sessionMessageHandler(self) -> _hiero_syncreview_client.Client:
        """Get the object used for sending and receiving messages in the current session. """
    def setConnectionInfo(self, connectionInfo: Any) -> None:
        """Set the current connection info """
    def shutdown(self) -> None:
        """Shut down the connection if there was one """
    def startServer(self, port: Any, clientData: Any, project: Any) -> None:
        """Start the server and listen on the given port """
    def stopServer(self) -> None:
        """Stop the server """

class ServerSession(Session):
    """Class representing a session running with a server. This creates a Server
    and a Client object which connects to the server and is used for sending and
    receiving messages.
    """
    staticMetaObject: Any
    def __init__(self, port: Any, clientData: Any, project: Any) -> None: ...
    def stop(self) -> None: ...
