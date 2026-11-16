# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from hiero.core.log import info as info

CRLF: str

class EditDecision:
    """Represents an entry in an Edit Decision list.
    Additional parameters are catalogued as key value pairs.
    """
    def __init__(self, editId: Any, name: Any, mode: Any, effect: Any, srcEntry: Any, srcExit: Any, syncEntry: Any, syncExit: Any) -> None: ...
    def __repr__(self) -> str:
        """Return a string representing the Edit Decision"""
    def addElement(self, element: Any) -> None:
        """Add NamedElement object to list of key value pairs
        Values are stored in a list if duplicates are added 
        """
    def conflicts(self, other: Any) -> bool: ...
    def editId(self) -> Any:
        """Return Edit index"""
    def effectfield(self) -> Any:
        """Return effect field object"""
    def getElement(self, key: Any) -> Any:
        """Return list of values with matching key"""
    def getSource(self) -> str: ...
    def hasElement(self, key: Any) -> bool:
        """Returns true if list of KVPs contains matching key"""
    def isBlank(self) -> Any:
        """Return true if tape name is BL or BLANK"""
    def mode(self) -> Any:
        """Return mode field object"""
    def name(self) -> Any:
        """Return tape name"""
    def removeElement(self, key: Any) -> None:
        """Remove all elements with matching key in list of KVPs"""
    def retime(self) -> RetimeElement | None: ...
    def setEditId(self, editId: Any) -> None:
        """Set Edit index"""
    def setRetime(self, fps: Any, srcEntry: Any = ...) -> None: ...
    def setSource(self, edlSource: Any) -> None: ...
    def srcEntry(self) -> Any:
        """Return source in timecode obj"""
    def srcExit(self) -> Any:
        """Return source out timecode obj"""
    def syncEntry(self) -> Any:
        """Return timeline in timecode obj"""
    def syncExit(self) -> Any:
        """Return timeline out timecode obj"""

class EffectField:
    """Represents the Effect Field of and EDL entry.
    The Effect Field describes the transition into the EDL entry.
    """
    CUT: str
    DISSOLVE: str
    KEY: str
    KEY_BACKGROUND: str
    WIPE: str
    def __init__(self, effect: Any, effectParameter: Any) -> None: ...
    def __repr__(self) -> str:
        """Returns a string representation of the EffectField."""
    def effect(self) -> Any: ...
    def effectparameter(self) -> Any: ...
    def isKeyBackground(self) -> Any: ...
    def isKeyIn(self) -> Any: ...
    def isWipe(self) -> Any: ...

class ModeField:
    """Represents the Mode field of an EDL entry.
    Audio, Video or Both. 
    """
    def __init__(self, audio: Any, video: Any, channels: Any) -> None: ...
    def __repr__(self) -> str:
        """Return string representation of Mode Field"""
    def hasAudio(self) -> Any: ...
    def hasVideo(self) -> Any: ...
    def numAudioChannels(self) -> int:
        """Returns True if has one or more audio track"""

class NamedElement:
    """Simple object containing key value pair
    This shouldnt be neccessary.
    """
    def __init__(self, field: Any, value: Any) -> None: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def key(self) -> Any: ...
    def val(self) -> Any: ...

class RetimeElement:
    """A class representing a retime directive  """
    def __init__(self, name: Any, framerate: Any, srcEntry: Any = ...) -> None: ...
    def __repr__(self) -> str: ...
    def framerate(self) -> Any:
        """Return resulting framerate"""
    def getSource(self) -> str: ...
    def matches(self, rhs: Any) -> bool:
        """Return True if rhs object has same name and timecode"""
    def name(self) -> Any:
        """Return reel name for retime"""
    def setSource(self, edlSource: Any) -> None: ...
    def setSrcEntry(self, srcEntry: Any) -> None:
        """Set the src entry timecode value for this retime."""
    def srcEntry(self) -> None:
        """Return src entry timecode for retime. This can be None if a parsed EDL did not contain it."""

class TimeCode:
    """Represesents a TimeCode"""
    def __ge__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __init__(self, h: Any, m: Any, s: Any, f: Any, sf: Any, dropFrame: Any) -> None: ...
    def __le__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __repr__(self) -> str:
        """return string representation of timecode"""
    def addFrames(self, time: Any, fps: Any) -> TimeCode:
        """Return a new TimeCode offset by a given number of frames."""
    @staticmethod
    def createFromFrames(time: Any, fps: Any, dropFrame: Any) -> TimeCode: ...
    def frames(self) -> Any:
        """Return Frames component of timecode"""
    def fromFrames(self, time: Any, fps: Any, dropFrame: Any) -> None: ...
    def hrs(self) -> Any:
        """Return Hours component of timecode"""
    def isDropFrame(self) -> Any:
        """Return True if timecode is dropframe
        http://documentation.apple.com/en/finalcutpro/usermanual/index.html#chapter=D%26section=6%26tasks=true
        """
    def isEqual(self, rhs: Any) -> Any:
        """Compare two time code objects"""
    def mins(self) -> Any:
        """Return Minutes component of timecode"""
    def secs(self) -> Any:
        """Return Seconds component of timecode"""
    def toFrames(self, fps: Any) -> Any:
        """Return timecode as frame index given framerate"""
