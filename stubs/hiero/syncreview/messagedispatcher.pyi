# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from hiero.core import executeInMainThread as executeInMainThread
from hiero.syncreview import messages as messages
from hiero.syncreview.log import logException as logException
from hiero.syncreview.log import logMessage as logMessage

class MessageDispatcher:
    """Receives messages from a connected session and forwards them to registered
    callbacks. Also allows for sending messages back.
    """
    staticMetaObject: Any
    def __init__(self, eventLoop: Any, messageClient: Any) -> None: ...
    def sendMessage(self, msg: Any) -> None:
        """Send a message back to the connected session """
    def shutdown(self) -> None: ...
