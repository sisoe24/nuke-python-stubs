# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore

class ConnectionState(_PySide6_QtCore.QObject):
    """Class representing the sync connection state. Defines the possible states
    and emits signals when it changes
    """
    CLIENT_CONNECTED: int
    CLIENT_CONNECTING: int
    DISCONNECTED: int
    ERROR_BIND_FAILURE: int
    ERROR_CONNECTION_LOST: int
    ERROR_CONNECT_INCOMPATIBLE_VERSION: int
    ERROR_CONNECT_INVALID_HOST: int
    ERROR_CONNECT_TIMEOUT: int
    ERROR_NONE: int
    ERROR_UNKNOWN: int
    SERVER_RUNNING: int
    changed: _PySide6_QtCore.Signal
    error: _PySide6_QtCore.Signal
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __eq__(self, state: Any) -> bool:
        """Convenience implementation for comparing the object to the state values """
    def __init__(self) -> None: ...
    def __ne__(self, state: Any) -> bool: ...
    def errorState(self) -> int: ...
    def errorText(self) -> str: ...
    def setError(self, error: Any, errorText: str = ...) -> None:
        """Set the error flag, and reset the main state to DISCONNECTED """
    def setState(self, state: Any) -> None:
        """Set the connection state. Clears any error that was set """
    def state(self) -> int: ...
