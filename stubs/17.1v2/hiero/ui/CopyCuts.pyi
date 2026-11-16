# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
from typing_extensions import Self
import PySide6.QtCore as _PySide6_QtCore
import PySide6.QtGui as _PySide6_QtGui
import PySide6.QtWidgets as _PySide6_QtWidgets
import enum as _enum
from hiero.core import EffectTrackItem as EffectTrackItem
from hiero.core import VideoTrack as VideoTrack
import hiero as hiero

Sequence: Any
copyCutsFromTrackAction: CopyCutsFromTrackAction

class CopyCutsFromTrack(_PySide6_QtWidgets.QDialog):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, sequence: Any, parent: Any = ...) -> None: ...
    def buildTracksList(self, sequence: Any) -> None: ...
    def cutSelectionBehavior(self) -> Any: ...
    def effectBehavior(self) -> Any: ...
    def fromTrackSelectionChanged(self, item: Any) -> None: ...
    def getCurrentFromTrack(self) -> Any:
        """Get the selected source track """
    def getDestinationTracks(self) -> list[Any]:
        """Get the selected destination tracks """
    def getIconForTrack(self, track: Any) -> Any: ...
    def nameBehavior(self) -> NameBehavior: ...
    def populateTrackListModel(self) -> None:
        """Build the model for the target track selection. Empty or locked tracks
        are disabled, all other video tracks are enabled by default.
        """
    def tagBehavior(self) -> Any: ...
    def toggleAllTracks(self) -> None: ...

class CopyCutsFromTrackAction(_PySide6_QtGui.QAction):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self) -> None: ...
    def doCuts(self) -> None: ...
    def eventHandler(self, event: Any) -> None: ...
    def toggleTrackLock(self, tracklist: Any, lockstate: bool = ...) -> None: ...

class CutDataCopier:
    """Class for performing the copying of cuts and related behaviors """
    def execute(self, nameBehavior: NameBehavior, effectBehavior: EffectAndTagBehavior, tagBehavior: EffectAndTagBehavior, srcItems: Any, dstTracks: Any) -> None:
        """Main method for performing the cut copying. Will also copy names and
        effects depending on the specified parameters.
        """

class CutSelectionBehavior(_enum.Enum):
    eCopyAllFromTrack: CutSelectionBehavior
    eCopySelected: CutSelectionBehavior
    def __new__(cls, value: Any) -> Self: ...

class DestinationTracksFilterModel(_PySide6_QtCore.QSortFilterProxyModel):
    """Model for filtering out the currently selected source track from the list
    of possible destination tracks.
    """
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, dialog: Any) -> None: ...
    def filterAcceptsRow(self, sourceRow: Any, sourceParent: Any) -> Any: ...

class EffectAndTagBehavior(_enum.Enum):
    eAdd: EffectAndTagBehavior
    eDontCopy: EffectAndTagBehavior
    eReplace: EffectAndTagBehavior
    def __new__(cls, value: Any) -> Self: ...

class EffectAndTagCopyWidget(_PySide6_QtWidgets.QWidget):
    """Widget for choosing how effects and tags should be copied """
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, forTags: Any) -> None: ...
    def copyBehavior(self) -> Any: ...

class NameBehavior(_enum.Enum):
    eCopy: NameBehavior
    eDontCopy: NameBehavior
    def __new__(cls, value: Any) -> Self: ...
