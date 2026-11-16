# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from typing import Callable
from hiero.core import events as events

class SyncTool:
    """Base class for 'tools' which handle the syncing logic. """
    staticMetaObject: Any
    def __init__(self, messageDispatcher: Any) -> None: ...
    def registerEventCallback(self, eventType: Any, callback: Any) -> None:
        """Register a callback with hiero.core.events. Will be cleaned up in shutdown() """
    def shutdown(self) -> None:
        """Clean up the tool, the default implementation unregisters any event callbacks """

def localCallback(func: Any) -> Callable[..., Any]:
    """Decorator for a local callback function (handling events/signals from local
    changes). Stops the function from being called if a remote message was being handled
    """

def remoteCallback(func: Any) -> Callable[..., Any]:
    """Decorator for a callback for handling remote messages. Sets the
    _handlingRemoteChange flag
    """
