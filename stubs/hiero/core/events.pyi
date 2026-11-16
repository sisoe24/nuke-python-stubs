# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any

class Callback:
    def __init__(self, method: Any, connection: Any = ..., *args: Any, **kwargs: Any) -> None: ...
    def call(self, event: Any) -> None: ...

class Connection:
    """Execute callback always, no matter how the event is triggered. """
    kAny: int
    kDirect: int
    kQueued: int

class Event:
    def __init__(self, type: Any = ..., subtype: Any = ..., **kwargs: Any) -> None: ...
    def __str__(self) -> str: ...
    def accept(self) -> None: ...
    def ignore(self) -> None: ...
    def isAccepted(self) -> bool: ...
    def setAccepted(self, accepted: Any) -> None: ...

class EventType:
    kAfterNewProjectCreated: str
    kAfterProjectClose: str
    kAfterProjectGUIDChange: str
    kAfterProjectLoad: str
    kAfterProjectSave: str
    kAfterUserProjectLoad: str
    kAnnotationChanged: str
    kAny: str
    kAutoSaveTriggered: str
    kBeforeNewProjectCreated: str
    kBeforeProjectClose: str
    kBeforeProjectGUIDChange: str
    kBeforeProjectLoad: str
    kBeforeProjectSave: str
    kBin: str
    kBinItemAdded: str
    kBinItemMoved: str
    kBinItemRemoved: str
    kBinItemRenamed: str
    kClipAdded: str
    kClipKnobChanged: str
    kContextChanged: str
    kCurrentViewerChanged: str
    kDoubleClick: str
    kDrop: str
    kEffectItemKnobChanged: str
    kExportDialog: str
    kInOutLockEnabledChanged: str
    kInOutPointsChanged: str
    kPaste: str
    kPlayback: str
    kPlaybackClipChanged: str
    kPlaybackStarted: str
    kPlaybackStopped: str
    kPlayheadAtEnd: str
    kPlayheadAtStart: str
    kSelectionChanged: str
    kSequenceEdited: str
    kSequenceFormatChanged: str
    kShowContextMenu: str
    kShutdown: str
    kShutdownFinal: str
    kSpreadsheet: str
    kStartup: str
    kTimeline: str
    kTrackEnabledChanged: str
    kVersionChanged: str
    kVersionLinkedChanged: str
    kViewer: str

def registerEventType(name: Any) -> None:
    """Register a new event type. The type should be a string (suitable as an attribute name) describing the event, e.g. 'kStartup'."""

def registerInterest(type: Any, callback: Any, connection: Any = ..., *args: Any, **kwargs: Any) -> None:
    """Register interest in an event type. The callback will be called whenever an event of the given type is dispatched."""

def sendEvent(type: Any, subtype: Any, **kwargs: Any) -> None:
    """Send an event immediately. The caller will block until the event has been handled.
    This only calls listeners registered with connection = kDirect or connection = kAny.
    """

def unregisterEventType(name: Any) -> None:
    """Unregister an event type."""

def unregisterInterest(type: Any, callback: Any) -> None:
    """Unregister interest in an event type. The callback will no longer be called whenever an event of the given type is dispatched."""
