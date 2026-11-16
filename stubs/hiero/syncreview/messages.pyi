# Type stubs for nuke 15.2v9. Generated; do not edit.

"""Code for creating and serializing messages.
Message classes should be created with the defineMessageType() function, e.g.
messages.defineMessageType('MyMessage', ('someData', int))
"""

from typing import Any
from typing import Callable
from typing_extensions import Self
from hiero.core.util import asBytes as asBytes
from hiero.core.util import asUnicode as asUnicode
from hiero.syncreview.log import logDebug as logDebug

Bool: tuple
Compressed: tuple
Json: tuple

class Message:
    """Class for messages used in the sync protocol. Concrete message types should
    be created with the defineMessageType() function.
    Each message has:
    - a sender, which should an id uniquely identifying the client machine
    - a target, which defaults to TARGET_BROADCAST indicating it should be routed to
      all clients, otherwise the server will try to send it to the specified client.
    - Optionally, a data payload
    """
    TARGET_BROADCAST: str
    def __init__(self, target: Any) -> None: ...
    def __str__(self) -> str: ...
    @classmethod
    def deserialize(cls, data: Any) -> Self:
        """Factory method for constructing messages from their serialized representation
    
        """
    def serialize(self) -> list[bytes]:
        """Get the serialized representation of a message. This is in the form:
        [classname, sender, target, data...].
        """

class AnnotationAdd(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class AnnotationChange(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class AnnotationRemove(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class BinItemAdded(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class BinItemMoved(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class BinItemRemoved(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class BinItemRenamed(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class ClipKnobChanged(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class Connect(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class ConnectResponse(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class Disconnect(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class Disconnected(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class EffectItemKnobChange(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class InOutChange(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class InOutLockEnabledChange(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class ItemStatusChange(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class Notification(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class NumberOfPeers(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class Ping(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class Pong(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class ProjectClose(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class ProjectLoadProgress(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class ProjectPush(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class ProjectPushBegin(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class ProjectPushEnd(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SequenceEdit(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncClientData(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncCursorLeave(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncCursorPosition(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerActivePlayhead(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerAnnotationsTool(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerBuffer(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerChannels(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerCompareMode(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerGain(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerGamma(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerGuideOverlay(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerLayerState(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerLayoutMode(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerMaskOverlay(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerMaskOverlayStyle(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerPlaybackMode(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerPlaybackSpeed(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerSaturation(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerSequence(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerShuttleTargetFPS(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerTargetFrameRate(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerTime(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerTimeDisplayFormat(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerWipeToolState(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class SyncViewerZoom(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class VersionChange(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

class VersionLinkedChange(Message):
    def __init__(self, target: str = ..., **fields: Any) -> None: ...

def RemoveDuplicateMessagesFilter(msgType: Any, matchAttributes: Any) -> Callable[..., list[Any]]:
    """Create filter where for messages which:
      a) have msgType and
      b) for the given list of attributes, match the values of a message sent later
    the earlier messages are discarded.
    """

def addMessageFilter(filter: Any) -> None:
    """Add a filter for incoming messages. This should be a callable which takes
    a list of messages and returns the filtered list.
    """

def applyMessageFilters(msgList: Any) -> Any:
    """Filter a set of incoming messages. This can be used to e.g. discard duplicate
    messages when only the most recent one is needed.
    Returns the filtered list.
    """

def defineMessageType(className: Any, *fieldDefs: Any) -> Any:
    """Define a new message class which will be added to the messages module.
    Fields can be defined with a name and specification of how they should be serialized.
    This can be just a type or conversion function, e.g. ('myField', int) where for
    serialization the data will just be converted to a string.
    Where control is needed over the serialization as well, you can specify a pair
    of functions, e.g. ('myField', (ValueToData, ValueFromData)). In this case they
    should return and accept a bytes object respectively
    """

def deserializeMessage(data: Any) -> Any:
    """Factory function for creating a message instance from its serialized
    representation.
    """
