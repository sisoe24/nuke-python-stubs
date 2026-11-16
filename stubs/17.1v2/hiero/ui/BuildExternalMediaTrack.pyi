# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import PySide6.QtGui as _PySide6_QtGui
import PySide6.QtWidgets as _PySide6_QtWidgets
from hiero.core.FnVersionScanner import VersionScanner as VersionScanner
import hiero as hiero

app: _PySide6_QtWidgets.QApplication
buildExternalMediaTrackAction: BuildTrack

class BuildTrackActionBase(_PySide6_QtGui.QAction):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, name: Any) -> None: ...
    def buildShotFromFiles(self, files: Any, name: Any, sequence: Any, track: Any, bin: Any, originalTrackItem: Any, expectedStartTime: Any, expectedDuration: Any, expectedStartHandle: Any, expectedEndHandle: Any, expectedOffset: Any) -> Any: ...
    def buildingFromExternalRender(self) -> bool:
        """Check if the the track is being built from external render tasks.  The behaviour needs to be different in this case because
        the frame range of those renders may not be what is expected. 
        """
    def configure(self, project: Any, selection: Any) -> bool: ...
    def doit(self) -> None: ...
    @staticmethod
    def findFiles(paths: Any) -> list[Any]: ...
    def getExpectedFormat(self, trackItem: Any) -> Any:
        """Get the expected format from the original track item.  The default implementation
        returns the parent sequence format. 
        """
    def getExpectedRange(self, trackItem: Any) -> tuple[int, int, None, None, int]:
        """Get range information.  Returns a tuple containing the values: (start, duration, starthandle, endhandle, offset) """
    def getExternalFilePaths(self, trackItem: Any) -> str: ...
    def getTimelineRange(self, trackItem: Any) -> tuple[Any, Any]:
        """Get the (timelineIn, timelineOut) for items being built from trackItem.  The default behaviour
        is to return trackItem's timeline range. 
        """
    def getTrackItems(self) -> list[Any] | None: ...
    def trackItemAdded(self, newTrackItem: Any, track: Any, originalTrackItem: Any) -> Any:
        """Method called when a new TrackItem is called while building a track.  The default implementation
        does nothing but can be implemented by sub-classes which need to customize the behavior. 
        """
    def trackName(self) -> str: ...
    @staticmethod
    def updateVersions(trackItem: Any) -> None:
        """Scan for versions on a track item and change to the highest available """

class BuildExternalMediaTrackAction(BuildTrackActionBase):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self) -> None: ...
    def buildingFromExternalRender(self) -> bool:
        """Override.  Check if the selected task preset is an External Render. """
    def configure(self, project: Any, selection: Any) -> bool: ...
    def getExpectedRange(self, trackItem: Any) -> tuple[Any, Any, None, None, int]:
        """Override. Get expected range based on the original track item.
        Returns None for handles so that they are calculated based on the duration
        of the new media. 
        """
    def getExternalFilePaths(self, trackItem: Any) -> list[Any]: ...
    def trackName(self) -> str: ...

class BuildExternalMediaTrackDialog(_PySide6_QtWidgets.QDialog):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, selection: Any, parent: Any = ...) -> None: ...
    def acceptTest(self) -> None: ...
    def itemProject(self, item: Any) -> None: ...
    def presetChanged(self, index: Any) -> None: ...
    def trackName(self) -> str: ...
    def useLatestVersion(self) -> bool:
        """Returns the state of the 'Use Latest Version' checkbox."""

class BuildTrack(_PySide6_QtWidgets.QMenu):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    @staticmethod
    def CalcTransitionExtraLengths(trackItem: Any) -> tuple[Any, Any]: ...
    @staticmethod
    def CheckForTrackItemCollisions(timelineIn: Any, timelineOut: Any, track: Any, isNewTrack: Any, collidedItems: Any, collidedTransitions: Any) -> None: ...
    @staticmethod
    def CheckForTransitionCollisions(originalTrackItem: Any, track: Any, collidedTransitions: Any) -> None: ...
    @staticmethod
    def CopyTimingFrom(toTrackItem: Any, fromTrackItem: Any, expectedHandles: Any = ...) -> None:
        """Copy timing information between track items.  If expectedHandles are given, tries to use them to
        set the source in/out of the track item, otherwise calculates handles based on the frame range of
        toTrackItem's media source.

        Note that this function does not deal well with cases where the expected handles are incorrect, or there are retimes involved.
        BuildTrackFromExportTagAction no longer uses it.
        """
    @staticmethod
    def FindOrCreateBin(project: Any, binName: Any) -> Any: ...
    @staticmethod
    def FindOrCreateClip(mediaSource: Any, destBin: Any, project: Any) -> Any:
        """Try to find an existing Clip which uses mediaSource.  If not found, creates a new clip and adds it to destBin.
        Returns the found or created clip. 
        """
    @staticmethod
    def GetTagIdentifier(tag: Any) -> Any:
        """Get an identifier for the tag.  Just tag.name() is not reliable, since
        tasks which are part of the same export can have the same name.  Combine it
        with the output path, if that is present in the tag metadata. 
        """
    @staticmethod
    def ProjectTrackNameDefault(selection: Any) -> None: ...
    @staticmethod
    def SetTrackItemReformatState(originalTrackItem: Any, trackItem: Any) -> None:
        """Set the reformat state of the created track item based on that of the
        original so they look the same on the timeline.
        """
    def __init__(self) -> None: ...
    def eventHandler(self, event: Any) -> None: ...

class BuildTrackFromExportTagAction(BuildTrackActionBase):
    """Action for the Build Track/From Export Tag functionality. """
    kCreateCompClipsPreferenceKey: str
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self) -> None: ...
    def buildTrackFromParams(self, trackItems: Any, tag: Any, trackName: Any, createCompClips: Any) -> None:
        """Perform the action with the parameters configured programatically rather
        than through the UI. This is to facilitate auto-testing.

        @param trackItems: list of track items to build from
        @param tag: the export tag to build from
        @param trackName: name of the track to put built items on
        @param createCompClips: control whether the built items reference the comp
        or rendered files
        """
    def configure(self, project: Any, selection: Any) -> bool: ...
    def findShotExporterTag(self, trackItem: Any) -> None:
        """Try to find a tag added by the Nuke Shot Exporter by checking it has the expected metadata keys. """
    def findTag(self, trackItem: Any) -> None: ...
    def getExpectedFormat(self, trackItem: Any) -> Any:
        """Reimplemented.  Tries to get the expected format from the tag metadata.
        If not present, returns the parent sequence format. 
        """
    def getExpectedRange(self, trackItem: Any) -> tuple[int, int, int | None, int | None, int]: ...
    def getExternalFilePaths(self, trackItem: Any) -> None: ...
    def getTimelineRange(self, trackItem: Any) -> tuple[Any, Any]:
        """Override.  The created track item is not necessarily the same length as the source, if multiple clips have been exported
        together (particularly with Create Comp).  Use the duration of the new source, minus handles. 
        """
    def retimesAppliedInExport(self, item: Any) -> int | bool:
        """Look up whether retimes were applied in the export.  Item can either be a Tag or a TrackItem.  In the latter case,
        the tag is looked up using findTag() 
        """
    def trackItemAdded(self, newTrackItem: Any, track: Any, originalTrackItem: Any) -> None:
        """Reimplementation.  Adds a tag to the new track item, and copies any retime effects if necessary. """
    def trackName(self) -> str: ...

class BuildTrackFromExportTagDialog(_PySide6_QtWidgets.QDialog):
    """Dialog for configuring a Build Track/From Export Tag action. """
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, selection: Any, createCompClips: Any, parent: Any = ...) -> None: ...
    def acceptTest(self) -> None: ...
    def createCompClips(self) -> bool: ...
    def tagIdentifier(self) -> str: ...
    def tagSelectionChanged(self, selection: Any) -> None: ...
    def trackName(self) -> str: ...

class TrackFinderByNameWithDialog:
    """Find or create tracks to build on based on the track name.  Also checks for collisions and shows a dialog
    if there are any so the user can choose what to do. 
    """
    def __init__(self, trackBuilder: Any) -> None: ...
    def checkTrackItemCollisionsShowDialog(self, selection: Any, track: Any) -> tuple[None, str] | tuple[Any, Any] | tuple[list[Any], Any] | tuple[list[Any], None]:
        """Check for collisions with items on the destination track.  If there are any, shows a TrackItemCollisionDialog. """
    def findOrCreateTrackByName(self, sequence: Any, trackName: Any) -> tuple[Any, bool]:
        """Searches the sequence for a track with the given name.  If none are found,
        creates a new one. 
        """
    def findTrack(self, name: Any, selection: Any, sequence: Any) -> tuple[Any, Any] | bool:
        """Find or create a track to build on for the given selection, and with name. """

class TrackFinderByTag:
    """Find or create tracks to build based on a tag name.  Searches for tracks above the selected items
    which have the expected tag and have no colliding items, otherwise creates a new one. 
    """
    @staticmethod
    def FindOrCreateTrackFromIndex(startIndex: Any, sequence: Any, tagName: Any) -> tuple[Any, bool, Any]:
        """Finds the next track in sequence above startIndex which has the tag tagName.
        If no track exists, one will be created.
        Returns the track, whether the track is new and the index of te track. 
        """
    @staticmethod
    def GetTopmostSelectedItem(selection: Any) -> int:
        """find the index fo the topmost seleted track """
    @staticmethod
    def NumberTaggedTracks(sequence: Any, tagName: Any) -> int:
        """Find the nuber of Tracks with the tag tagName """
    def __init__(self, trackBuilder: Any) -> None: ...
    def checkTrackItemCollisions(self, selection: Any, track: Any) -> bool:
        """Check for selected track items which collide with those on the destination track.
        Returns true if there were collisions, else returns false. 
        """
    def findTrack(self, name: Any, selection: Any, sequence: Any) -> tuple[Any, Any]:
        """Find or create a track to build on for the given selection, and with tag matching name. """

class TrackItemCollisionDialog(_PySide6_QtWidgets.QDialog):
    kDeleteDestCollisions: int
    kMakeNewTrack: int
    kRefreshDestCollisions: int
    kSkipSrcCollisions: int
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, numCollisions: Any, track: Any, uniqueTrackName: Any, labelText: Any = ..., parent: Any = ..., enableDeleteButton: bool = ..., enableRefreshButton: bool = ...) -> None: ...
    def optionChanged(self) -> None: ...
    def selectedAction(self) -> int: ...
