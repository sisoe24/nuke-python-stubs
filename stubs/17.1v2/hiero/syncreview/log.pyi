# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any

LOG_DEBUG_ENABLED: bool

def closeLogger() -> None:
    """Close the logger instance """

def initLogger(name: Any) -> None:
    """Create the logger instance with the given name """

def logDebug(message: Any) -> None:
    """Debug log message. These aren't printed unless LOG_DEBUG_ENABLED is set """

def logException(msg: Any = ...) -> None:
    """Log the current exception details """

def logMessage(message: Any) -> None:
    """Write a message to the current log file """
