# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from hiero.core import ApplicationSettings as ApplicationSettings
from hiero.syncreview import config as config
from hiero.syncreview.connectionstate import ConnectionState as ConnectionState
import hiero as hiero

class SessionSetupDialog:
    """Dialog for setting up a new sync review session
  
    """
    staticMetaObject: Any
    def __init__(self, connectionManager: Any, project: Any, parent: Any = ...) -> None: ...
    def getClientData(self) -> tuple[Any, tuple[Any, Any, Any]]:
        """Get the clients data from the dialog """
    def getPort(self) -> Any:
        """Get the port number from the dialog """
    def startSession(self) -> None:
        """Start the server session using the current dialog info"""
