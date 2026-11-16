# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import PySide6.QtWidgets as _PySide6_QtWidgets
from hiero.core import ApplicationSettings as ApplicationSettings
from hiero.syncreview import config as config
from hiero.syncreview.connectionstate import ConnectionState as ConnectionState
import hiero as hiero

class SessionSetupDialog(_PySide6_QtWidgets.QDialog):
    """Dialog for setting up a new sync review session
    
    """
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, connectionManager: Any, project: Any, parent: Any = ...) -> None: ...
    def getClientData(self) -> tuple[str, tuple[Any, Any, Any]]:
        """Get the clients data from the dialog """
    def getPort(self) -> int:
        """Get the port number from the dialog """
    def startSession(self) -> None:
        """Start the server session using the current dialog info"""
