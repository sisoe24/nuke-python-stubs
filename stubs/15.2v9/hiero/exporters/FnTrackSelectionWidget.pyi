# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero as hiero

class TrackSelectionWidget:
    """Widget for selecting tracks for export.  Note that the way this is configured on the preset
    is slightly odd.  The excluded tracks are stored in the session by name, but for determining
    which tracks are actually excluded we use their guids.  This allows for the same selection to
    be used for different sequences, but means things can get a bit confused if there are multiple
    tracks with the same name. 
    """
    staticMetaObject: Any
    def __init__(self, sequences: Any, hiddenTrackNames: Any, excludedTrackNames: Any, excludedTrackIDs: Any, allowAll: bool = ..., parent: Any = ...) -> None: ...
    def findTrackByGuid(self, guid: Any) -> None:
        """Find a track in the list with the given GUID. """
    def getIconForTrack(self, track: Any) -> None:
        """Get the icon to use for a track. """
    def offlineTrackItems(self, track: Any) -> list[Any]:
        """Get a list offline track items for a track. """
    def onItemChanged(self, item: Any) -> None:
        """Handle the user checking/unchecking an item in the list. """

class _TrackViewKeyPressRedirect:
    """Event filter to catch Space being pressed on the tracks list view. """
    staticMetaObject: Any
    def __init__(self, parent: Any = ...) -> None: ...
    def eventFilter(self, obj: Any, event: Any) -> Any: ...
