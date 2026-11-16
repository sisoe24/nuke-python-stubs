# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
from typing import Sequence
from typing_extensions import Self
import PySide6.QtCore as _PySide6_QtCore
import PySide6.QtGui as _PySide6_QtGui
import PySide6.QtWidgets as _PySide6_QtWidgets
import enum as _enum
import hiero.core as _hiero_core
import hiero.ui.FnExportUIRegistry as _hiero_ui_FnExportUIRegistry
import hiero.ui.FnStatusBar as _hiero_ui_FnStatusBar
import nuke as _nuke
from . import BuildExternalMediaTrack as BuildExternalMediaTrack
from . import CopyCuts as CopyCuts
from . import FnCodecUIController as FnCodecUIController
from . import FnDirectExportContentUI as FnDirectExportContentUI
from . import FnDisclosureButton as FnDisclosureButton
from . import FnElidedLabel as FnElidedLabel
from . import FnExportUIRegistry as FnExportUIRegistry
from . import FnExporterBaseUI as FnExporterBaseUI
from . import FnNodePropertyWidget as FnNodePropertyWidget
from . import FnPathQueryDialog as FnPathQueryDialog
from . import FnPosterFrameUI as FnPosterFrameUI
from . import FnProcessorUI as FnProcessorUI
from . import FnReExportAction as FnReExportAction
from . import FnStatusBar as FnStatusBar
from . import FnTagFilterWidget as FnTagFilterWidget
from . import FnTaskUIFormLayout as FnTaskUIFormLayout
from . import FnUIProperty as FnUIProperty
from . import FnVersionWidget as FnVersionWidget
from . import FnViewerMethods as FnViewerMethods
from . import LocalisationMenu as LocalisationMenu
from . import RenameTimelineShots as RenameTimelineShots
from . import ScanForVersions as ScanForVersions
from . import SendToNuke as SendToNuke
from . import TagsMenu as TagsMenu
from . import nuke_bridge as nuke_bridge
from hiero.FnRedirect import TimelineEditorCreationFlag as TimelineEditorCreationFlag
from hiero.FnRedirect import activeSequence as activeSequence
from hiero.FnRedirect import activeView as activeView
from hiero.FnRedirect import currentWorkspace as currentWorkspace
from hiero.FnRedirect import findRegisteredAction as findRegisteredAction
from hiero.FnRedirect import findRegisteredActions as findRegisteredActions
from hiero.FnRedirect import getProjectBinView as getProjectBinView
from hiero.FnRedirect import getTagsBinView as getTagsBinView
from hiero.FnRedirect import getTimelineEditor as getTimelineEditor
from hiero.FnRedirect import mainWindow as mainWindow
from hiero.FnRedirect import menuBar as menuBar
from hiero.FnRedirect import registerAction as registerAction
from hiero.FnRedirect import registeredActions as registeredActions
from hiero.FnRedirect import resetCurrentWorkspace as resetCurrentWorkspace
from hiero.FnRedirect import saveWorkspace as saveWorkspace
from hiero.FnRedirect import setWorkspace as setWorkspace
from hiero.exporters.FnNukeAnnotationsExporter import renderSequenceToImage as renderSequenceToImage
from hiero.ui.FnExportUIRegistry import TaskUIRegistry as TaskUIRegistry
from hiero.ui.FnExporterBaseUI import InvalidOutputResolutionMessage as InvalidOutputResolutionMessage
from hiero.ui.FnExporterBaseUI import RenderTaskUIBase as RenderTaskUIBase
from hiero.ui.FnExporterBaseUI import TaskUIBase as TaskUIBase
from hiero.ui.FnProcessorUI import ProcessorUIBase as ProcessorUIBase
from hiero.ui.FnVersionWidget import VersionWidget as VersionWidget
import hiero as hiero

kContextComp: int
kContextNone: int
kContextProperty: str
kContextStudio: int
kContextTimeline: int
mainStatusBar: _hiero_ui_FnStatusBar.MainStatusBar
taskUIRegistry: _hiero_ui_FnExportUIRegistry.TaskUIRegistry

class BinView:
    """Object representing the Bin View. Passed as the sender object to the event handler callbacks registered for hiero.core.events.EventType.kShowContextMenu type events. Can also be retrieved using hiero.ui.currentContextMenuView when active during the context menu events."""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getSelection(self, *args: Any, **kwargs: Any) -> Any:
        """Deprecated; please use the selection method instead.

        @return: tuple of hiero.core.BinItem objects
        """
    def selection(self) -> Any:
        """self.selection() -> returns a tuple with the currently selected items.

        @return: tuple of hiero.core.BinItem objects
        """
    def window(self) -> Any:
        """self.window() -> Return the bin view window"""

class ColorButton(_PySide6_QtWidgets.QPushButton):
    colorChanged: _PySide6_QtCore.Signal
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def canBeInvalid(self, *args: Any, **kwargs: Any) -> Any: ...
    def color(self, *args: Any, **kwargs: Any) -> Any: ...
    def dragEnterEvent(self, *args: Any, **kwargs: Any) -> Any: ...
    def dropEvent(self, *args: Any, **kwargs: Any) -> Any: ...
    def mouseMoveEvent(self, *args: Any, **kwargs: Any) -> Any: ...
    def mousePressEvent(self, *args: Any, **kwargs: Any) -> Any: ...
    def paintEvent(self, *args: Any, **kwargs: Any) -> Any: ...
    def setCanBeInvalid(self, *args: Any, **kwargs: Any) -> Any: ...
    def setColor(self, *args: Any, **kwargs: Any) -> Any: ...
    def setValidColor(self, *args: Any, **kwargs: Any) -> Any: ...
    def sizeHint(self, *args: Any, **kwargs: Any) -> Any: ...
    def validColor(self, *args: Any, **kwargs: Any) -> Any: ...

class ColorPickerDialog(_PySide6_QtWidgets.QDialog):
    accepted: _PySide6_QtCore.Signal
    finished: _PySide6_QtCore.Signal
    rejected: _PySide6_QtCore.Signal
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def currentColor(self, *args: Any, **kwargs: Any) -> Any: ...
    def setCurrentColor(self, *args: Any, **kwargs: Any) -> Any: ...

class ContactSheetItem:
    """Object representing an item in the ContactSheetModel"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def item(self) -> Any:
        """self.item() -> returns the item shown in the contact sheet, which may be a TrackItem or a VideoTrack.

        @return: the associated item
        """

class ContactSheetMode(_enum.IntEnum):
    FromPython: ContactSheetMode
    FromSequenceSelection: ContactSheetMode
    FromSequenceTagsFilter: ContactSheetMode
    FromTracks: ContactSheetMode
    NotSet: ContactSheetMode
    def __new__(cls, value: Any) -> Self: ...

class ContactSheetModel(_PySide6_QtCore.QObject):
    """Class representing the contents of a ContactSheetView"""
    destroyed: _PySide6_QtCore.Signal
    objectNameChanged: _PySide6_QtCore.Signal
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addTrackItems(self) -> Any:
        """self.addTrackItems() -> adds track items to the Contact Sheet

        Items must belong to the same sequence, which must be the Contact Sheet’s active sequence.

        @param trackItems: list of track items to add
        """
    def clearSources(self) -> Any:
        """self.clearSources() -> clears the selection sources for the clips in the Contact Sheet"""
    def items(self) -> Any:
        """self.items() -> get the list of items in the model

        @return: list of ContactSheetItem instances
        """
    def mode(self) -> ContactSheetMode:
        """self.mode() -> get the current mode for the model

        @return: ContactSheetMode
        """
    def setMode(self, mode: Any) -> Any:
        """self.setMode(mode) -> set the mode for the model

        @param mode: the ContactSheetMode to set
        """
    def setSequence(self) -> Any:
        """self.setSequence() -> sets the active sequence on the model

        The active sequence is the sequence that provides the items shown in the Contact Sheet

        @param sequence: the sequence to set as active
        """
    def setSoftEffectMode(self, mode: Any) -> Any:
        """self.setSoftEffectMode(mode) -> set the soft effect mode for the contact sheet

        Available modes:

        - Disabled: soft effect tracks are not included in the contact sheet item render

        - EffectOnlyTracksEnabled: soft effect tracks above selected track items are included in the contact sheet item render

        @param mode: the ContactSheetSoftEffectMode to set
        """
    def setTagsFilters(self) -> Any:
        """self.setTagsFilters() -> set the tags to filter on in FromSequenceTagsFilter mode

        Filters track items in the Contact Sheet based on their tags:

        - A track item is excluded if it has any tag from excludeTags

        - A track item is included only if it has all the tags in includeTags

        - If includeTags is empty, all track items that do not have an excluded tag are included

        @param includeTags: list of tags to include in the filter

        @param excludeTags: optional list of tags to exclude in the filter
        """
    def setTrackItems(self) -> Any:
        """self.setTrackItems() -> clears the Contact Sheet and adds the given track items

        Items must belong to the same sequence, which must be the Contact Sheet’s active sequence.

        @param trackItems: list of track items to add
        """
    def softEffectMode(self) -> ContactSheetSoftEffectMode:
        """self.softEffectMode() -> get the soft effect mode currently selected for the contact sheet

        @return: ContactSheetSoftEffectMode
        """

class ContactSheetSoftEffectMode(_enum.IntEnum):
    Disabled: ContactSheetSoftEffectMode
    EffectOnlyTracksEnabled: ContactSheetSoftEffectMode
    def __new__(cls, value: Any) -> Self: ...

class Viewer(_PySide6_QtCore.QObject):
    """Object for manipulating viewers in Hiero. Get the currently active viewer by calling hiero.ui.currentViewer()."""
    class CompareMode(_enum.IntEnum):
        eCompareDifference: Viewer.CompareMode
        eCompareInvertAndAdd: Viewer.CompareMode
        eCompareMinus: Viewer.CompareMode
        eCompareNoBlend: Viewer.CompareMode
        eCompareOnionSkin: Viewer.CompareMode
        eCompareOver: Viewer.CompareMode
        eCompareUnder: Viewer.CompareMode
        def __new__(cls, value: Any) -> Self: ...
    class LayoutMode(_enum.IntEnum):
        eLayoutFree: Viewer.LayoutMode
        eLayoutGrid: Viewer.LayoutMode
        eLayoutHorizontal: Viewer.LayoutMode
        eLayoutStack: Viewer.LayoutMode
        eLayoutVertical: Viewer.LayoutMode
        eLayoutWipe: Viewer.LayoutMode
        def __new__(cls, value: Any) -> Self: ...
    class PlaybackMode(_enum.IntEnum):
        ePlaybackBounce: Viewer.PlaybackMode
        ePlaybackContinue: Viewer.PlaybackMode
        ePlaybackRepeat: Viewer.PlaybackMode
        ePlaybackStop: Viewer.PlaybackMode
        def __new__(cls, value: Any) -> Self: ...
    class ZoomMode(_enum.IntEnum):
        eZoomFill: Viewer.ZoomMode
        eZoomFit: Viewer.ZoomMode
        eZoomFitHeight: Viewer.ZoomMode
        eZoomFitWidth: Viewer.ZoomMode
        eZoomFixed: Viewer.ZoomMode
        def __new__(cls, value: Any) -> Self: ...
    channelsChanged: _PySide6_QtCore.Signal
    compareModeChanged: _PySide6_QtCore.Signal
    currentLayerChanged: _PySide6_QtCore.Signal
    frameDisplayed: _PySide6_QtCore.Signal
    gainChanged: _PySide6_QtCore.Signal
    gammaChanged: _PySide6_QtCore.Signal
    guideOverlayChanged: _PySide6_QtCore.Signal
    layoutModeChanged: _PySide6_QtCore.Signal
    maskOverlayChanged: _PySide6_QtCore.Signal
    maskOverlayStyleChanged: _PySide6_QtCore.Signal
    playbackModeChanged: _PySide6_QtCore.Signal
    playbackSpeedChanged: _PySide6_QtCore.Signal
    playheadStateChanged: _PySide6_QtCore.Signal
    saturationChanged: _PySide6_QtCore.Signal
    sequenceChanged: _PySide6_QtCore.Signal
    shuttleTargetFPSChanged: _PySide6_QtCore.Signal
    staticMetaObject: _PySide6_QtCore.QMetaObject
    targetFrameRateChanged: _PySide6_QtCore.Signal
    timeChanged: _PySide6_QtCore.Signal
    timeDisplayFormatChanged: _PySide6_QtCore.Signal
    trackSelectionChanged: _PySide6_QtCore.Signal
    transformChanged: _PySide6_QtCore.Signal
    def ROITool(self) -> ViewerTool:
        """self.ROITool() -> return the ROI tool for this viewer"""
    def annotationTool(self) -> ViewerTool:
        """self.annotationTool() -> return the annotation tool for this viewer."""
    def availableGuideOverlayNames(self) -> list[str]:
        """self.availableGuideOverlayNames() -> returns the names of all the guide overlays available in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: The names of all the guide overlays available in the viewer
        """
    def cachedFrames(self) -> set:
        """self.cachedFrames() -> get the frames which are currently cached in the viewer.

        @return: set containing the indices of the cached frames
        """
    def centerImage(self) -> Any:
        """self.centerImage() -> centers the viewer, resetting the pan values."""
    def channels(self) -> Player.Channels:
        """self.channels() -> returns the current channels in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer clip player's current channels
        """
    def compareMode(self) -> Viewer.CompareMode:
        """self.compareMode() -> returns the compare mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer.CompareMode object
        """
    def currentLayerName(self) -> str:
        """self.currentLayerName() -> returns the name of the current channels layer the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer clip player's channels layer name
        """
    def cursorTool(self) -> ViewerCursorTool: ...
    def displayDropFrames(self) -> bool:
        """self.displayDropFrames() -> True if the drop frames are beingdisplayed on the time format (when timecode is displayed)

        @return: True if the display frames are being displayed
        """
    def displayTimecode(self) -> bool:
        """self.displayTimecode() -> True if the timecode is being displayed on the time format

        @return: True if the timecode is being displayed
        """
    def enterFullScreen(self) -> Any:
        """self.enterFullScreen() -> puts the viewer into full screen mode. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread."""
    def exitFullScreen(self) -> Any:
        """self.exitFullScreen() -> takes the viewer out of full screen mode. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread."""
    def flushCache(self) -> Any:
        """self.flushCache() -> flush the cache on the viewer and pause caching."""
    def frameIncrement(self) -> int:
        """self.frameIncrement() -> returns the frame increment for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: the number of frames to skip or nudge
        """
    def gain(self) -> float:
        """self.gain() -> returns the gain value for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer clip player's gain value
        """
    def gamma(self) -> float:
        """self.gamma() -> returns the gamma value for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer clip player's gamma value
        """
    def getAchievedFPS(self) -> float:
        """self.getAchievedFPS() -> returns the average fps achieved by the viewer.

        @return: floating point frames per second average
        """
    def goToInTime(self) -> Any:
        """Move playhead to In point"""
    def goToNextEdit(self) -> Any:
        """self.goToNextEdit() -> Move playhead to next edit. Can only be called from the user interface thread."""
    def goToNextTag(self) -> Any:
        """self.goToNextTag() -> Move playhead to next tag. Can only be called from the user interface thread."""
    def goToOutTime(self) -> Any:
        """Move playhead to Out point"""
    def goToPrevEdit(self) -> Any:
        """self.goToPrevEdit() -> Move playhead to previous edit. Can only be called from the user interface thread."""
    def goToPrevTag(self) -> Any:
        """self.goToPrevTag() -> Move playhead to previous tag. Can only be called from the user interface thread."""
    def goToTag(self, tag: Any) -> Any:
        """Move playhead to Tag.
        If Tag (Tag Object or Tag name) does not exists on the Viewer's Sequence/Clip
        a KeyError is raised.

        @param tag: a Tag object or the name of the desired tag.
        """
    def goToTrackItemEnd(self, trackItem: Any) -> Any:
        """Move playhead to end of the trackItem.

        @param trackItem: sequence's track item.
        """
    def goToTrackItemMiddle(self, trackItem: Any) -> Any:
        """Move playhead to middle of the trackItem.

        @param trackItem: sequence's track item.
        """
    def goToTrackItemStart(self, trackItem: Any) -> Any:
        """Move playhead to start of the trackItem.

        @param trackItem: sequence's track item.
        """
    def image(self) -> _PySide6_QtGui.QImage:
        """self.image() -> returns the contents of the viewer as an image, including all overlays. Can only be called from the user interface thread.

        @return: a PySide6.QtGui.QImage object
        """
    def isCachingPaused(self) -> bool:
        """self.isCachingPaused() -> get whether caching is paused.

        @return: bool
        """
    def layoutMode(self) -> Viewer.LayoutMode:
        """self.layoutMode() -> returns the layout mode the viewer is currently in.

        @return: a Viewer.LayoutMode object
        """
    def maskOverlayName(self) -> str:
        """self.maskOverlayName() -> returns the name of the current mask overlay in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: The name of the mask overlay currently active in the viewer
        """
    def maskOverlayStyle(self) -> Player.MaskOverlayStyle:
        """self.maskOverlayStyle() -> returns the current mask overlay style set in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: The current mask overlay style active in the viewer
        """
    def overlaysShown(self) -> bool:
        """self.overlaysShown() -> get whether overlays are shown in the viewer.

        @return: bool
        """
    def pan(self, dx: Any, dy: Any) -> Any:
        """self.pan(dx, dy) -> pans the Viewer by (dx, dy).

        @param dx: float value to pan in x by
        @param dy: float value to pan in y by
        """
    def pauseCaching(self) -> Any:
        """self.pauseCaching() -> pause caching on the viewer."""
    def play(self) -> Any:
        """self.play() -> starts playback in the viewer in the forward direction. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread."""
    def playBackwards(self) -> Any:
        """self.playBackwards() -> starts playback in the viewer in the backwards direction. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread."""
    def playForwards(self) -> Any:
        """self.playForwards() -> starts playback in the viewer in the forward direction. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread."""
    def playbackMode(self) -> Viewer.PlaybackMode:
        """self.playbackMode() -> returns the compare mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer.PlaybackMode object
        """
    def playbackSpeed(self) -> int:
        """self.playbackSpeed() -> Get the current playback speed, which will be 0 if playback is not currently in progress."""
    def player(self, index: Any = ...) -> Player:
        """self.player(index) -> returns the player object attached to this viewer, based on the input index.

        @param index: integer index of the player to retrieve
        @return: hiero.ui.Player object
        """
    def resumeCaching(self) -> Any:
        """self.resumeCaching() -> resume caching on the viewer."""
    def saturation(self) -> float:
        """self.saturation() -> returns the saturation value for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer clip player's saturation value
        """
    def selectedGuideOverlayNames(self) -> list:
        """self.selectedGuideOverlayNames() -> returns the names of the current guide overlays in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: The names of all the guide overlays currently active in the viewer
        """
    def setChannels(self, channels: Any) -> Any:
        """self.setChannels(channels) -> Sets the channels in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param channels: the channels to be set in the viewer
        """
    def setCompareMode(self, mode: Any) -> Any:
        """self.setCompareMode(mode) -> changes the compare mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param compareMode: a Viewer.CompareMode value
        """
    def setDisplayTimecode(self, displayTimecode: Any) -> None:
        """self.setDisplayTimecode(displayTimecode) -> Sets the viewer to display Timecode if 'displayTimecode' is True, or Timeline Frame otherwise

        @return: None
        """
    def setExpanded(self, arg1: Any, /) -> Any:
        """self.setExpandState() -> set the expanded state of the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param expanded: Expand viewer
        """
    def setFrameIncrement(self, frames: Any) -> Any:
        """self.setFrameIncrement(frames) -> changes the frame increment for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param frames: the number of frames to skip or nudge
        """
    def setGain(self, gain: Any) -> Any:
        """self.setGain(gain) -> changes the gain for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param gain: a gain value to be set in the viewer
        """
    def setGamma(self, gamma: Any) -> Any:
        """self.setGamma(gamma) -> changes the gamma for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param gamma: a gamma value to be set in the viewer
        """
    def setGuideOverlayFromRemote(self) -> Any:
        """self.setGuideOverlayFromRemote() -> Sets the guide overlays in the viewer from a remote source. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param overlayNames: the names of the overlays to be set
        @param remoteOverlaysAvailable: the names of the overlays that are available to the remote client
        """
    def setLayer(self, layerName: Any) -> Any:
        """self.setLayer(layerName) -> Sets the channels layer in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param layerName: the name of the channels layer to be set in the viewer
        """
    def setLayoutMode(self, mode: Any) -> Any:
        """self.setLayoutMode(mode) -> changes the layout mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param layoutMode: a Viewer.LayoutMode value indicating what layout to set the viewer to
        """
    def setMaskOverlayFromRemote(self) -> Any:
        """self.setMaskOverlayFromRemote() -> Sets the guide overlays in the viewer from a remote source. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param remoteOverlayName: the name of the overlay to be set
        """
    def setMaskOverlayStyle(self) -> Any:
        """self.setMaskOverlayStyle() -> Sets the channels in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param pyStyle: the mask style to be set in the viewer
        """
    def setOverlaysShown(self, show: bool) -> Any:
        """self.setOverlaysShown(show) -> set whether overlays are shown in the viewer.

        @param show: bool
        """
    def setPlaybackMode(self, arg1: Any, /) -> Any:
        """self.setCompareMode(mode) -> changes the playback mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param mode: a Viewer.PlaybackMode value
        """
    def setPlaybackSpeed(self, speed: Any) -> Any:
        """self.setPlaybackSpeed(speed) -> Set the current playback speed. Setting to 0 will stop, -1 play in reverse, etc."""
    def setPlayer(self, index: Any) -> Any:
        """self.setPlayer(index) -> sets the active player if index is a valid player index.

        @param index: integer index of the player to set as the active player
        """
    def setSaturation(self, saturation: Any) -> Any:
        """self.setSaturation(saturation) -> changes the saturation for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param saturation: a saturation value to be set in the viewer
        """
    def setSequence(self) -> Any:
        """self.setSequence() -> set the sequence for this viewer

        @param sequence: the sequence to set on this viewer
        @param indexOfPlayer: index to specify which of the players the sequence should be set on
        """
    def setTime(self, time: Any) -> Any:
        """self.setTime(time) -> seeks the play head of the viewer to the time parameter. Works the same as scrubbing the timeline in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param time: frame to set the play head to
        """
    def setTimeDisplayFormat(self) -> Any:
        """self.setTimeDisplayFormat() -> Change the current time display format of the viewer

        @param displayTimecode: Display timecode
        @param displayDropFrames: Display drop frames
        """
    def setTracksMask(self) -> Any:
        """self.setTracksMask() -> modify the status of the tracks of one of the buffers. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param indexOfPlayer: integer index of the player
        @param tracksMask: TracksMask instance
        """
    def setView(self, name: str, viewIndex: Any = ...) -> Any:
        """setView(name, viewIndex) -> If name matches an existing view then the Viewers's active view for viewIndex is set to the view given by name.
        @param name: string
        @param viewIndex: optional; integer (for example in stereo a viewIndex of 0 corresponds to the primary view and 1 to the secondary view)
        """
    def setZoomMode(self, mode: Any) -> Any:
        """self.setZoomMode(mode) -> Change the current zoom mode. Use zoomAbsolute or zoomRelative for Fixed instead of this method.

        @param mode: ZoomMode
        """
    def stop(self) -> Any:
        """self.stop() -> stops playback in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread."""
    def syncShuttleTargetFPS(self) -> Any:
        """self.syncShuttleTargetFPS() -> Syncs the current target frame rate of the shuttle target frame rate

        @param fps: Target frame rate for the shuttle tool
        """
    def syncTargetFrameRate(self) -> Any:
        """self.syncTargetFrameRate() -> Syncs the target frame rate of the viewer when it is modifiedby other client during a sync review

        @param numerator: Numerator of the target frame rate
        @param denominator: Denominator of the target frame rate
        """
    def time(self) -> int:
        """self.time() -> returns the current frame of the viewer."""
    def toggleFullScreen(self) -> Any:
        """self.toggleFullScreen() -> toggles full screen mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread."""
    def toggleFullScreen1_1(self) -> Any:
        """self.toggleFullScreen1_1() -> toggles 1:1 full screen mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread."""
    def tracksMask(self) -> Any:
        """self.tracksMask() -> returns status of the tracks of one of the buffers. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param indexOfPlayer: integer index of the player
        @return: TracksMask instance
        """
    def translation(self) -> _PySide6_QtCore.QPointF:
        """self.translation() -> current translation.

        @return: QPointF
        """
    def view(self, viewIndex: Any = ...) -> str:
        """view(viewIndex) -> Returns the name of the active view for viewIndex.
        @param viewIndex: optional; integer (for example in stereo a viewIndex of 0 corresponds to the primary view and 1 to the secondary view)
        """
    def window(self) -> _PySide6_QtWidgets.QWidget:
        """self.window() -> Return the viewer window"""
    def wipeTool(self) -> ViewerTool:
        """self.wipeTool() -> return the wipe tool for this viewer"""
    def zoom(self) -> float:
        """self.zoom() -> current zoom.

        @return: float
        """
    def zoomAbsolute(self, centerX: Any, centerY: Any, zoom: Any) -> Any:
        """self.zoomAbsolute(centerX, centerY, zoom) -> sets the zoom to a specific center and zoom level, ignoring previous zoom state.

        @param centerX: new relative center of the zoom
        @param centerY: new relative center of the zoom
        @param zoom: float value scale by
        """
    def zoomCenter(self) -> _PySide6_QtCore.QPointF:
        """self.zoomCenter() -> current zoomCenter.

        @return: QPointF
        """
    def zoomMode(self) -> Viewer.ZoomMode:
        """self.zoomMode() -> current zoom mode.

        @return: ZoomMode
        """
    def zoomRelative(self, centerX: Any, centerY: Any, zoomFactor: Any) -> Any:
        """self.zoomRelative(centerX, centerY, zoomFactor) -> scales the images relatively and repositions the image.

        @param centerX: new x center of the images, in image pixels
        @param centerY: new y center of the images, in image pixels
        @param zoom: float value scale by
        """
    def zoomToActualSize(self) -> Any:
        """self.zoomToActualSize() -> scales and centers the images to the full size of the images."""
    def zoomToFill(self) -> Any:
        """self.zoomToFill() -> scales the images so that it fills the viewer window."""
    def zoomToFit(self) -> Any:
        """self.zoomToFit() -> scales the images so that it fits in the viewer window, maintaining the pixel aspect ratio."""
    def zoomToFitHeight(self) -> Any:
        """self.zoomToFitHeight() -> scales the images so that the height of the images fits in the viewer window, maintaining the pixel aspect ratio."""
    def zoomToFitWidth(self) -> Any:
        """self.zoomToFitWidth() -> scales the images so that the width of the image fits in the viewer window, maintaining the pixel aspect ratio."""
    def zoomToHalfSize(self) -> Any:
        """self.zoomToActualSize() -> scales and centers the images to half the size of the images."""
    def __new__(cls, *args: Any, **kwargs: Any) -> Viewer: ...

class ContactSheetViewer(Viewer):
    """Class representing the ContactSheetViewer"""
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def getModel(self) -> ContactSheetModel:
        """self.getModel() -> returns the ContactSheetModel for the viewer

        @return: ContactSheetModel
        """
    def getResolution(self) -> Any:
        """self.getResolution() -> returns the size of the Contact Sheet viewer

        @return: QSize
        """
    def hudExpression(self, corner: Any) -> str:
        """self.hudExpression(corner) -> returns the expression currently configured for the given HUD corner.

        Returns the built-in default expression for corners that have not been explicitly overridden (e.g. 'hiero/clip2' for TopLeft, 'hiero/shot' for BottomLeft).
        Returns 'none' if the corner has been explicitly set blank.

        @param corner: a hiero.ui.HUDCorner value
        @return: str
        """
    def hudFontScale(self) -> float:
        """self.hudFontScale() -> return the current HUD text font scale factor.

        @return: float
        """
    def hudTextColor(self) -> _PySide6_QtGui.QColor:
        """self.hudTextColor() -> return the current HUD text color.

        @return: PySide6.QtGui.QColor
        """
    def isHUDEnabled(self) -> bool:
        """self.isHUDEnabled() -> return whether the HUD overlay is currently enabled.

        @return: bool
        """
    def maximumColumnCount(self) -> int:
        """self.maximumColumnCount() -> returns the maximum column count of the Contact Sheet viewer

        @return: int
        """
    def maximumRowCount(self) -> int:
        """self.maximumRowCount() -> returns the maximum row count of the Contact Sheet viewer

        @return: int
        """
    def page(self) -> int:
        """self.page() -> returns the current page

        @return: int
        """
    def pageCount(self) -> int:
        """self.pageCount() -> returns the total number of pages

        The number is dynamically determined by the max rows, max columns, and the number of items in the Contact Sheet.

        @return: int
        """
    def setHUDEnabled(self, enabled: bool) -> Any:
        """self.setHUDEnabled(enabled) -> enable or disable the HUD overlay on the Contact Sheet.

        The HUD is disabled by default. It must be enabled before any per-corner metadata text will be painted over the contact sheet cells.

        @param enabled: bool
        """
    def setHUDExpression(self, corner: Any, metadataKey: Any) -> Any:
        """self.setHUDExpression(corner, metadataKey) -> sets the expression to evaluate at the specified HUD corner.

        Pass 'none' or an empty string to force the corner blank.

        @param corner: a hiero.ui.HUDCorner value (TopLeft, TopRight, BottomLeft, BottomRight)
        @param expression: expression text e.g. '[metadata input/filename]'
        """
    def setHudFontScale(self, scale: float) -> Any:
        """self.setHudFontScale(scale) -> set the HUD text font scale factor.

        A value of 1.0 is 100% (the default). Values above 1.0 enlarge the text;
        values below shrink it.

        @param scale: float
        """
    def setHudTextColor(self, color: Any) -> Any:
        """self.setHudTextColor(color) -> set the HUD text color.

        The default color is (200, 200, 200).

        @param color: QColor
        """
    def setMaximumColumnCount(self, maximumColumnCount: Any) -> Any:
        """self.setMaximumColumnCount(maximumColumnCount) -> sets the maximum column count of the Contact Sheet viewer

        The maximum column count is the number of column that can be shown on one page of the Contact Sheet.

        If there are more items than can fit in the maximumRowCount × maximumColumnCount grid,new pages will be created to display the extra items.

        @param maximumColumnCount: the maximum number of columns
        """
    def setMaximumRowCount(self, maximumRowCount: Any) -> Any:
        """self.setMaximumRowCount(maximumRowCount) -> sets the maximum row count of the Contact Sheet viewer

        The maximum row count is the number of rows that can be shown on one page of the Contact Sheet.

        If there are more items than can fit in the maximumRowCount × maximumColumnCount grid,new pages will be created to display the extra items.

        @param maximumRowCount: the maximum number of rows
        """
    def setPage(self, page: Any) -> Any:
        """self.setPage(page) -> sets the current page

        It is set to the first page if the page number is less than 0 and the last page if it is greater than the page count.

        @param page: the page number
        """
    def setResolution(self, resolution: Any) -> Any:
        """self.setResolution(resolution) -> sets the size of the Contact Sheet viewer

        @param resolution: a QSize object representing the resolution
        """
    def toggleStackView(self) -> Any:
        """self.toggleStackView() -> toggle stack view mode

        Swaps the current grid state between the normal grid and a stack view grid.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> ContactSheetViewer: ...

class ExportStructureViewer(_PySide6_QtWidgets.QWidget):
    class EditMode(_enum.IntEnum):
        Full: ExportStructureViewer.EditMode
        Limited: ExportStructureViewer.EditMode
        ReadOnly: ExportStructureViewer.EditMode
        def __new__(cls, value: Any) -> Self: ...
    kAddFileToolTip: str
    kAddFolderToolTip: str
    kRemoveToolTip: str
    kStructureContentToolTip: str
    kStructurePathToolTip: str
    selectionChanged: _PySide6_QtCore.Signal
    staticMetaObject: _PySide6_QtCore.QMetaObject
    structureModified: _PySide6_QtCore.Signal
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addFile(self, *args: Any, **kwargs: Any) -> Any: ...
    def addFolder(self, *args: Any, **kwargs: Any) -> Any: ...
    def allowNodeDelete(self, *args: Any, **kwargs: Any) -> Any: ...
    def clearResolveEntries(self, *args: Any, **kwargs: Any) -> Any: ...
    def copy(self, *args: Any, **kwargs: Any) -> Any: ...
    def cut(self, *args: Any, **kwargs: Any) -> Any: ...
    def exportRootChanged(self, *args: Any, **kwargs: Any) -> Any: ...
    def filenameField(self, *args: Any, **kwargs: Any) -> Any: ...
    def getWidget(self, *args: Any, **kwargs: Any) -> Any: ...
    def handleSelectionChanged(self, *args: Any, **kwargs: Any) -> Any: ...
    def initUI(self, *args: Any, **kwargs: Any) -> Any: ...
    def itemTypes(self, *args: Any, **kwargs: Any) -> Any: ...
    def keyPressEvent(self, *args: Any, **kwargs: Any) -> Any: ...
    def paste(self, *args: Any, **kwargs: Any) -> Any: ...
    def refresh(self, *args: Any, **kwargs: Any) -> Any: ...
    def refreshContentField(self, *args: Any, **kwargs: Any) -> Any: ...
    def removeNode(self, *args: Any, **kwargs: Any) -> Any: ...
    def selectFileIfOnlyOne(self, *args: Any, **kwargs: Any) -> Any: ...
    def selectFirstFile(self, *args: Any, **kwargs: Any) -> Any: ...
    def selection(self, *args: Any, **kwargs: Any) -> Any: ...
    def selectionAnchor(self, *args: Any, **kwargs: Any) -> Any: ...
    def selectionRect(self, *args: Any, **kwargs: Any) -> Any: ...
    def setAllowNodeDelete(self, *args: Any, **kwargs: Any) -> Any: ...
    def setExportStructure(self, *args: Any, **kwargs: Any) -> Any: ...
    def setItemTypes(self, *args: Any, **kwargs: Any) -> Any: ...
    def setProject(self, *args: Any, **kwargs: Any) -> Any: ...
    def setResolveEntry(self, *args: Any, **kwargs: Any) -> Any: ...

class FilePathWidget(_PySide6_QtWidgets.QWidget):
    filePathChanged: _PySide6_QtCore.Signal
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def filePath(self, *args: Any, **kwargs: Any) -> Any: ...
    def setFilePath(self, *args: Any, **kwargs: Any) -> Any: ...

class FormatChooser(_PySide6_QtWidgets.QComboBox):
    formatChanged: _PySide6_QtCore.Signal
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def currentFormat(self, *args: Any, **kwargs: Any) -> Any: ...
    def setCurrentFormat(self, *args: Any, **kwargs: Any) -> Any: ...
    def setProject(self, *args: Any, **kwargs: Any) -> Any: ...

class HUDCorner(_enum.IntEnum):
    BottomLeft: HUDCorner
    BottomRight: HUDCorner
    TopLeft: HUDCorner
    TopRight: HUDCorner
    def __new__(cls, value: Any) -> Self: ...

class IDirectExportUI:
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getValues(self, *args: Any, **kwargs: Any) -> Any: ...
    def populateUI(self, *args: Any, **kwargs: Any) -> Any: ...
    def startExport(self, *args: Any, **kwargs: Any) -> Any: ...
    def validate(self, *args: Any, **kwargs: Any) -> Any: ...

class IDirectExportUIFactoryWrapper:
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def createUI(self, *args: Any, **kwargs: Any) -> Any: ...
    def getKey(self, *args: Any, **kwargs: Any) -> Any: ...
    def registerme(self, *args: Any, **kwargs: Any) -> Any: ...

class IExporterUIRegistry:
    """IExporterUIRegistry provides a simple interface for our C++ Application to access the Python instance of TaskUIRegistry.

    This class should not be used directly; use hiero.ui.TaskUIRegistry instead.
    """
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def aquireProcessorUI(self) -> Any:
        """self.aquireProcessorUI() -> Called from Hiero Application to aquire a reference to an instance of the ProcessorUI object related to the specified hiero.core.TaskPreset.

        @param preset: hiero.core.ITaskPreset
        """
    def getProcessorUI(self, *args: Any, **kwargs: Any) -> Any: ...
    def getProcessorUIForPreset(self, *args: Any, **kwargs: Any) -> Any: ...
    def getTaskUI(self, *args: Any, **kwargs: Any) -> Any: ...
    def getTaskUIForPreset(self, *args: Any, **kwargs: Any) -> Any: ...
    def numProcessorUIs(self, *args: Any, **kwargs: Any) -> Any: ...
    def numTaskUIs(self, *args: Any, **kwargs: Any) -> Any: ...
    def registerme(self) -> Any:
        """self.registerme() -> Called from python implimentation of TaskUIRegistry to register instance as the Application TaskUI Registry."""
    def releaseProcessorUI(self) -> Any:
        """self.releaseProcessorUI() -> Called from Hiero Application to release the reference to a IProcessorUI object previously aquired using IExporterUIRegistry.aquireProcessorUI.

        @param processorUI: hiero.ui.IProcessorUI
        """

class IProcessorUI:
    """IProcessorUI provides a simple interface for our C++ Application to access Python instances of ProcessorUIBase.

    This class should not be used directly; use hiero.ui.ProcessorUIBase instead.
    """
    class EditMode(_enum.IntEnum):
        Full: IProcessorUI.EditMode
        Limited: IProcessorUI.EditMode
        ReadOnly: IProcessorUI.EditMode
        def __new__(cls, value: Any) -> Self: ...
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def displayName(self) -> str:
        """self.displayName() -> called by Hiero to get the Display name of a task for displaying in UI.

        @return: string
        """
    def populateUI(self) -> Any:
        """self.populateUI() -> called by Hiero to allow the IProcessorUI to populate a QWidget with the ui widgets neccessary to reflect the current preset.
        The EditMode is used to instruct the UI generation code to build in ReadOnly mode

        @param processorUIWidget: PySide6.QtGui.QWidget
        @param taskUIWidget: PySide6.QtGui.QWidget
        @param items: [hiero.core.ItemWrapper]
        @param editMode: hiero.core.IProcessorUI.EditMode
        """
    def preset(self) -> _hiero_core.ITaskPreset:
        """self.preset() -> called by Hiero to get the TaskPreset which this TaskUI is currently reflecting.

        @return: hiero.core.ITaskPreset
        """
    def refreshContent(self, *args: Any, **kwargs: Any) -> Any: ...
    def savePreset(self, *args: Any, **kwargs: Any) -> Any: ...
    def setPreset(self) -> Any:
        """self.setPreset() -> called by Hiero to set the TaskPreset which this TaskUI will reflect.

        @param preset: hiero.core.ITaskPreset
        """
    def toolTip(self) -> str:
        """self.toolTip() -> called by Hiero to get the desciption of a task for displaying in UI as a tooltip.

        @return: string
        """
    def validate(self) -> bool:
        """self.validate() -> called by Hiero to get .

        @param: [hiero.core.ItemWrapper]
        @return: bool
        """
    def validateSelection(self, *args: Any, **kwargs: Any) -> Any: ...

class ITaskUI:
    """ITaskUI provides a simple interface for our C++ Application to access Python instances of TaskUIBase.

    This class should not be used directly; use hiero.ui.TaskUIBase instead.
    """
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def displayName(self) -> str:
        """self.displayName() -> called by Hiero to get the Display name of a task for displaying in UI.

        @return: string
        """
    def ident(self) -> str:
        """self.ident() -> called by Hiero to get a unique identifier linking this TaskUI with a Task and TaskPreset.

        @return: string
        """
    def populateUI(self) -> Any:
        """self.populateUI() -> called by Hiero to allow the TaskUI to populate a QWidget with the ui widgets neccessary to reflect the current preset.

        @param widget: PySide6.QtGui.QWidget
        @param exportTemplate: hiero.core.IExportStructure
        """
    def preset(self) -> _hiero_core.ITaskPreset:
        """self.preset() -> called by Hiero to get the TaskPreset which this TaskUI is currently reflecting.

        @return: hiero.core.ITaskPreset
        """
    def setPreset(self) -> Any:
        """self.setPreset() -> called by Hiero to set the TaskPreset which this TaskUI will reflect.

        @param preset: hiero.core.ITaskPreset
        """

class MediaFlagsChooser(_PySide6_QtWidgets.QWidget):
    flagsChanged: _PySide6_QtCore.Signal
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class Player:
    """Object representing a video player in Hiero. Players are used by Viewer objects, and can be retrieved using the player() method of Viewer objects."""
    class Channels(_enum.IntEnum):
        eChannelA: Player.Channels
        eChannelB: Player.Channels
        eChannelG: Player.Channels
        eChannelLuma: Player.Channels
        eChannelR: Player.Channels
        eChannelRGB: Player.Channels
        def __new__(cls, value: Any) -> Self: ...
    class MaskOverlayStyle(_enum.IntEnum):
        eMaskOverlayFull: Player.MaskOverlayStyle
        eMaskOverlayHalf: Player.MaskOverlayStyle
        eMaskOverlayLines: Player.MaskOverlayStyle
        eMaskOverlayNone: Player.MaskOverlayStyle
        def __new__(cls, value: Any) -> Self: ...
    class ProxyResolution(_enum.IntEnum):
        eProxy16: Player.ProxyResolution
        eProxy2: Player.ProxyResolution
        eProxy32: Player.ProxyResolution
        eProxy4: Player.ProxyResolution
        eProxy8: Player.ProxyResolution
        eProxyAuto: Player.ProxyResolution
        eProxyFull: Player.ProxyResolution
        def __new__(cls, value: Any) -> Self: ...
    class WarningOverlay(_enum.IntEnum):
        eWarningExposure: Player.WarningOverlay
        eWarningNTSC: Player.WarningOverlay
        eWarningNone: Player.WarningOverlay
        eWarningPAL: Player.WarningOverlay
        def __new__(cls, value: Any) -> Self: ...
    def LUT(self) -> str:
        """self.LUT() -> returns the name of the LUT currently in use by the player.

        @return: string
        """
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def alphaIsTransparent(self) -> bool:
        """self.alphaIsTransparent() -> returns whether the player treats the alpha channel as premultiplied transparency (True) or not (False).

        @return: True or False
        """
    def channels(self) -> Player.Channels:
        """self.channels() -> returns channel(s) that the player is currently displaying.

        @return: hiero.ui.Player.Channels object
        """
    def displayGain(self) -> float:
        """self.displayGain() -> returns the current gain of the player. Defaults to 1.0

        @return: float
        """
    def displayGamma(self) -> float:
        """self.displayGamma() -> returns the current gamma of the player. Since the viewer displays pixels in linear space, this value defaults to 1.0.

        @return: float
        """
    def displaySaturation(self) -> float:
        """self.displaySaturation() -> returns the current saturation of the player. Can only be called from the user interface thread. Defaults to 1.0

        @return: float
        """
    def getCurrentErrorMessage(self) -> str:
        """self.getCurrentErrorMessage() -> Get any error that might be set on this Player

        @return: string
        """
    def guideOverlay(self) -> Any:
        """self.guideOverlay() -> returns the guide overlays displayed in the player.

        @return: sequence of foundry.ui.Drawing
        """
    def ignorePixelAspectRatio(self) -> bool:
        """self.ignorePixelAspectRatio() -> returns whether the player ignores the pixel aspect ratio or not.

        @return: True or False
        """
    def maskOverlay(self) -> Any:
        """self.maskOverlay() -> returns the drawing used as the mask overlay in the player.

        @return: foundry.ui.Drawing
        """
    def maskOverlayStyle(self) -> Player.MaskOverlayStyle:
        """self.maskOverlayStyle() -> returns the current drawing style of the mask overlay used by the player.

        @return: hiero.ui.Player.MaskOverlayStyle
        """
    def proxyResolution(self) -> Player.ProxyResolution:
        """self.proxyResolution() -> get the current proxy resolution setting for the player

        @return: Player.ProxyResolution
        """
    def rect(self) -> Any:
        """self.rect() -> player rectangular area in GL coordinates.

        @return: rectangle
        """
    def sequence(self) -> Any:
        """self.sequence() -> returns the object currently being played.

        @return: hiero.core.Clip object or hiero.core.Sequence object, depending on what is currently playing
        """
    def setAlphaIsTransparent(self, alphaIsTransparent: Any) -> Any:
        """self.setAlphaIsTransparent( alphaIsTransparent ) -> sets whether the player treats the alpha channel as premultiplied transparency.

        @param alphaIsTransparent: True to have the player treat alpha as premultiplied transparency, False otherwise
        """
    def setChannels(self, channels: Player.Channels) -> Any:
        """self.setChannels(channels) -> sets the channels to display in the player. It's currently either one of the channels or red, green and blue.

        @param channels: hiero.ui.Player.Channels object
        """
    def setDisplayGain(self, gain: float) -> Any:
        """self.setDisplayGain(gain) -> sets the gain of the player.

        @param gain: float
        """
    def setDisplayGamma(self, gamma: float) -> Any:
        """self.setDisplayGamma(gamma) -> sets the gamma of the player.

        @param gamma: float
        """
    def setDisplaySaturation(self, saturation: float) -> Any:
        """self.setDisplaySaturation(saturation) -> sets the saturation of the player. Can only be called from the user interface thread. 

        @param saturation: float
        """
    def setGuideOverlay(self, guideOverlays: Any) -> Any:
        """self.setGuideOverlay(guideOverlays) -> sets the guide overlays to display in the player.

        @param guideOverlays: sequence of foundry.ui.Drawing
        """
    def setIgnorePixelAspectRatio(self, ignorePixelAspectRatio: Any) -> Any:
        """self.setIgnorePixelAspectRatio(ignorePixelAspectRatio) -> tells the player whether or not to display in anamorphic mode.

        @param ignorePixelAspectRatio: True to have the player ignore the pixel aspect ratio, False otherwise
        """
    def setLUT(self, lut: Any) -> Any:
        """self.setLUT(lut) -> sets the LUT to use in the player. If the lut doesn't exist, will raise an exception.

        @param lut: string name of the lut to use
        """
    def setMaskOverlay(self, aspect: Any) -> Any:
        """self.setMaskOverlay(aspect) -> sets the drawing to use for the mask overlay.

        @param aspect: foundry.ui.Drawing
        """
    def setMaskOverlayStyle(self, style: Player) -> Any:
        """self.setMaskOverlayStyle(style) -> sets the drawing style of the mask overlay.

        @param style: hiero.ui.Player.MaskOverlayStyle style
        """
    def setProxyResolution(self, resolution: Player.ProxyResolution) -> Any:
        """self.setProxyResolution(resolution) -> set the player proxy resolution.

        @param resolution: Player.ProxyResolution
        """
    def setSequence(self, clip: Any) -> Any:
        """self.setSequence(clip) -> deprecated; use Viewer.setSequence instead"""
    def setWarningOverlay(self, warningOverlay: Any) -> Any:
        """self.setWarningOverlay(warningOverlay) -> sets the warning overlay.

        @param warningOverlay: One of the following enums: eWarningNone, eWarningExposure, eWarningPAL or eWarningNTSC
        """
    def time(self) -> Any:
        """self.time() -> gets the time of the playhead.

        @return: frame number
        """
    def translation(self) -> float:
        """self.translation() -> translation applied to the footage in the player.

        @return: float
        """
    def warningOverlay(self) -> Any:
        """self.warningOverlay() -> returns player's warningOverlay.

        @return: One of the following enums: eWarningNone, eWarningExposure, eWarningPAL or eWarningNTSC
        """
    def zoom(self, *args: Any, **kwargs: Any) -> float:
        """self.zoomMode() -> current zoom

        @return: float
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> Player: ...

class Render:
    class ImageRenderFlag(_enum.IntFlag):
        eIncludeAnnotations: Render.ImageRenderFlag
        eNone: Render.ImageRenderFlag
        def __and__(self, other: Any) -> Any: ...
        def __invert__(self) -> Any: ...
        def __new__(cls, value: Any) -> Self: ...
        def __or__(self, other: Any) -> Any: ...
        def __rand__(self, other: Any) -> Any: ...
        def __ror__(self, other: Any) -> Any: ...
        def __rxor__(self, other: Any) -> Any: ...
        def __xor__(self, other: Any) -> Any: ...
    @staticmethod
    def sequenceToImage(sequence: Any, frame: Any, renderFlags: Any, colorspace: Any = ..., ocioDisplay: Any = ..., ocioView: Any = ...) -> Any:
        """hiero.ui.Render.sequenceToImage(sequence, frame, renderFlags, colorspace=None, ocioDisplay=None, ocioView=None) -> Render the given frame for a sequence to a QImage.

        A color transform for the render may be specified either with the colorspace parameter, or with the ocioDisplay and ocioView
        parameters which will apply a display transform. If none of these are specified, the setting for thumbnails in the project
        will be used.

        @param sequence: hiero.core.SequenceBase object to render
        @param frame: the frame to render at
        @param renderFlags, optional: ImageRenderFlags with options for behaviour
        @param colorspace, optional: colorspace to apply to the render
        @param ocioDisplay, optional: display device. If used, ocioView must also be given
        @param ocioView, optional: view transform to apply to the render. If used, ocioDisplay must also be given

        @return: QImage with QImage.Format_RGBA32
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> Render: ...

class SpreadsheetView:
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def beginSelectionUpdate(self) -> Any:
        """self.beginSelectionUpdate() -> Call beginSelectionUpdate before, and endSelectionUpdate after, making multiple setSelection."""
    def endSelectionUpdate(self) -> Any:
        """self.endSelectionUpdate() -> Call beginSelectionUpdate before, and endSelectionUpdate after, making multiple setSelection."""
    def selectAll(self) -> Any:
        """self.selectAll( )

        Select All TrackItems within current sequence.
        """
    def selectNone(self) -> Any:
        """self.selectNone( )

        Unselect all TrackItems.
        """
    def selection(self, *args: Any, **kwargs: Any) -> Any: ...
    def sequence(self, *args: Any, **kwargs: Any) -> Any: ...
    def setSelection(self, *args: Any, **kwargs: Any) -> Any:
        """self.setSelection( hiero.core.TrackItem )
        self.setSelection( [hiero.core.TrackItem] )
        Will throw exception if selection is not subset of current sequence.

        @param selection: track item(s) to be selected.
        """
    def window(self) -> Any:
        """self.window() -> Return the spreadsheet view window"""

class TimelineEditor:
    """Object representing the Timeline Editor."""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def beginSelectionUpdate(self) -> Any:
        """self.beginSelectionUpdate() -> Call beginSelectionUpdate before, and endSelectionUpdate after, making multiple setSelection."""
    def endSelectionUpdate(self) -> Any:
        """self.endSelectionUpdate() -> Call beginSelectionUpdate before, and endSelectionUpdate after, making multiple setSelection."""
    def getSelection(self, *args: Any, **kwargs: Any) -> Any:
        """Deprecated; please use the selection method instead.

        @return: tuple of TrackItem and Transition objects
        """
    def hasAutoSelection(self) -> bool:
        """self.hasAutoSelection() -> bool

        Returns True if the items returned by selection() were automatically selected 
        rather than explicitly selected by the user. This will only return True when 
        there is no user selection and auto-selection is enabled.

        @return: True if selection contains auto-selected items, False otherwise
        """
    def selectAll(self) -> Any:
        """self.selectAll( )

        Select All TrackItems within current sequence.
        """
    def selectNone(self) -> Any:
        """self.selectNone( )

        Unselect all TrackItems and Tracks.
        """
    def selection(self) -> Any:
        """self.selection() -> returns a tuple with the currently selected items.

        @return: tuple of TrackItem and Transition objects
        Use self.hasAutoSelection() to determine if the selection is an auto-selection.
        """
    def sequence(self) -> Sequence:
        """self.sequence() -> returns the Sequence currently being edited in the timeline editor.

        @return: Sequence object
        """
    def setSelection(self, *args: Any, **kwargs: Any) -> Any:
        """self.setSelection( hiero.core.TrackItem )
        self.setSelection( [hiero.core.TrackItem] )
        Will throw exception if selection is not subset of current sequence.

        @param selection: track item(s) to be selected.
        """
    def setTrackSelection(self, *args: Any, **kwargs: Any) -> Any:
        """self.setTrackSelection( hiero.core.TrackBase )
        self.setTrackSelection( [hiero.core.TrackBase] )
        Will throw exception if selection is not subset of current sequence.

        @param selection: Tracks to be selected.
        """
    def window(self) -> Any:
        """self.window()

        Return the TimelineEditor widget.
        Note: This includes the sequence and track item properties panels, tool selectors,
        multiple playhead and contact sheet controls, etc, not just the video and audio tracks.
        """

class TracksMask:
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def setTracks(self, *args: Any, **kwargs: Any) -> Any: ...
    def setVisibleByDefault(self, *args: Any, **kwargs: Any) -> Any: ...
    def tracks(self, *args: Any, **kwargs: Any) -> Any: ...
    def visibleByDefault(self, *args: Any, **kwargs: Any) -> Any: ...

class ViewerTool(_PySide6_QtCore.QObject):
    """Python interface for the viewer tools"""
    activeChanged: _PySide6_QtCore.Signal
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def isActive(self) -> Any:
        """self.isActive() -> get the tool's active state"""
    def setActive(self, active: Any) -> Any:
        """self.setActive(active) -> set the tool's active state"""
    def __new__(cls, *args: Any, **kwargs: Any) -> ViewerTool: ...

class ViewerAnnotationTool(ViewerTool):
    """Python interface for the viewer annotation tool"""
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def addAnimatedStrokeToOverlay(self, stroke: Any) -> Any:
        """self.addAnimatedStrokeToOverlay(stroke) -> add an animated stroke to the overlay scene"""
    def overlayScenePaintObjects(self) -> Any:
        """self.overlayScenePaintObjects() -> get all animated strokes from the overlay scene"""
    def removeAnimatedStrokeFromOverlay(self, stroke: Any) -> Any:
        """self.removeAnimatedStrokeFromOverlay(stroke) -> remove an animated stroke from the overlay scene"""
    def __new__(cls, *args: Any, **kwargs: Any) -> ViewerAnnotationTool: ...

class ViewerCursor:
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    color: Any
    label: Any
    pos: Any

class ViewerCursorTool(_PySide6_QtCore.QObject):
    cursorLeave: _PySide6_QtCore.Signal
    cursorPositionChanged: _PySide6_QtCore.Signal
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def setCursors(self, *args: Any, **kwargs: Any) -> Any: ...
    def __new__(cls, *args: Any, **kwargs: Any) -> ViewerCursorTool: ...

class ViewerROITool(ViewerTool):
    activeChanged: _PySide6_QtCore.Signal
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def ROI(self, *args: Any, **kwargs: Any) -> Any: ...
    def setROI(self, *args: Any, **kwargs: Any) -> Any: ...
    def __new__(cls, *args: Any, **kwargs: Any) -> ViewerROITool: ...

class ViewerWipeTool(ViewerTool):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    wipeToolStateChanged: _PySide6_QtCore.Signal
    def setWipeToolState(self, *args: Any, **kwargs: Any) -> Any: ...
    def wipeToolState(self, *args: Any, **kwargs: Any) -> Any: ...
    def __new__(cls, *args: Any, **kwargs: Any) -> ViewerWipeTool: ...

class WindowManager:
    """Global object to handle window management in Hiero. Use hiero.ui.windowManager() to get the single instance of this object to use."""
    class WindowMenuSection(_enum.IntEnum):
        kApplicationSection: WindowManager.WindowMenuSection
        kDocumentSection: WindowManager.WindowMenuSection
        kNumGroups: WindowManager.WindowMenuSection
        kQAToolsSection: WindowManager.WindowMenuSection
        def __new__(cls, value: Any) -> Self: ...
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def addWindow(self, window: Any, section: Any, shortcut: Any) -> Any:
        """self.addWindow(window, section, shortcut) -> adds a window to the window manager and insert a menu item for it into the Window menu. This will also make the window dockable with Hiero's other windows.

        @param window: QWidget object for the window
        @param section: section (either an int, or a WindowManager.WindowMenuSection) to insert the menu item into
        @param shortcut: shortcut to apply to the menu item. See the documentation on QKeySequence for more info
        """
    def popupWindow(self, window: Any) -> Any:
        """self.popupWindow(window) -> Opens the window in a floating dock panel.

        @param window: QWidget object for the window
        """
    def showWindow(self, window: Any) -> Any:
        """self.showWindow(window) -> Opens the window in its layout position or if as a floating dock panel

        @param window: QWidget object for the window
        """
    def windows(self) -> list:
        """self.windows() -> Returns a list with the available widgets in WindowManager

        @return: list of the available widgets in WindowManager
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> WindowManager: ...

class WipeToolState:
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    gauge: Any
    rotation: Any
    translateX: Any
    translateY: Any

def PaintBlendModeName(arg1: Any, /) -> Any: ...

def addMenuAction(path: Any, action: Any, before: Any = ...) -> bool:
    """Add a QAction to the main menubar. The 'path' parameter specifies the menu to which to add the action as a '/'-separated string.
    The path may contain either internal action names or display names. e.g. 'View/Transform', or (better) 'foundry.menu.view/foundry.view.transform'."
    The optional 'before' parameter specifies the name of an item the action should be inserted before. If this is not specified, the action is appended to the menu.
    """

def browseForApplication(message: Any, initialPath: Any, parentWidget: Any) -> str:
    """hiero.ui.browseForApplication (message, initialPath, parentWidget) -> brings up the file browser to allow the user to select an application. Allows the user to select an executable file on Windows and Linux, and to select an application bundle (\\*.app) directory on OSX.

    @param message: prompt to display to the user in the file browser
    @param initialPath: initial path to set the file browser to. Can be a zero length string
    @param parentWidget: QWidget to set as the parent of the file browser. Can be None.
    @return: string
    """

def createMenuAction(name: Any, method: Any, icon: Any = ..., path: Any = ...) -> Any:
    """Creates a menu action (QAction) for use in context menus or Main menubar.
    The 'name' parameter specifies the title of the action.

    @param: name - the title of the menu action
    @param: method - the Python method which this action triggers
    @param: icon (optional) - provides an icon for the action. This can be an absolute path ('/var/tmp/myIcon.png'), or relative path ('icons:myIcon.png')
    @param: path (optional) - the path to the menu action. The action objects name will be set to this value
    """

def currentContextMenuView() -> Viewer:
    """hiero.ui.currentContextMenuView() -> returns the current view for the context menu. Only valid during a kShowContextMenu event callback.

    @return: hiero.ui.Viewer, hiero.ui.TimelineEditor, hiero.ui.BinView, depending on which window had the context menu created for it
    """

def currentViewer() -> Viewer:
    """hiero.ui.currentViewer() -> returns the current viewer window.

    @return: hiero.ui.Viewer
    """

def findMenuAction(name: Any) -> None:
    """Find a QAction in the main menubar. The 'name' parameter specifies the name of the action.
    The name may be either an internal action name or a display name. e.g. 'Cut', or (better) 'foundry.application.cut'.\"
    """

def flushAllViewersCache() -> Any:
    """self.flushAllViewersCache() -> flush the cache of all viewers and pause caching"""

def getFlipbook() -> Viewer: ...

def getProjectRootInteractive(project: Any) -> None:
    """Try to get a valid root path from the project.  If the existing exportRootDirectory()
    is not set or doesn't exist, the user will be prompted to select one.  If no path
    is selected, returns None. 
    """

def insertMenuAction(action: Any, menu: Any, before: Any = ..., after: Any = ...) -> None:
    """Insert a QAction into the given QMenu. If strings 'before' or 'after' are specified, the action is inserted before or after the action with that name.
    If no such action is found or 'before/after' are not given, the action is appended to the menu.
    """

def isInAnyProject(arg1: Any, /) -> Any: ...

def isInAnyTimeline(arg1: Any, /) -> Any: ...

def monitorOutNode() -> _nuke.Node: ...

def openFileBrowser(caption: str = ..., mode: Any = ..., pattern: str = ..., initialPath: str = ..., forSave: bool = ..., canChooseMultiple: bool = ..., sequencesEnabled: bool = ..., mayNotExist: bool = ..., showAllFileTypes: bool = ..., confirmOverwrite: bool = ..., requiredExtension: str = ...) -> Any:
    """openFileBrowser(caption="", mode=1, pattern="", initialPath="", forSave=False, canChooseMultiple=False, sequencesEnabled=False, mayNotExist=False, showAllFileTypes=False, confirmOverwrite=True, requiredExtension="") -> string list.

    Displays a modal foundry file browser dialog.

    @param caption: Optional. Message to display in the dialog.
    @param mode: Optional. Selection mode (1=Files Only, 2=Directories Only, 3=Files and Directories)
    @param pattern: Optional. File filter pattern.
    @param initialPath: Optional. The selected path on dialog creation.
    @param forSave: Optional. Configure dialog for saving a file.
    @param multipleSelection: Optional. Allow selection of multiple files.
    @param sequencesEnabled: Optional. Configure file browser for showing sequences.
    @param mayNotExist: Optional. Allow return of paths that don't exist e.g. for saving.
    @param showAllFileTypes: Optional. Show all files regardless of the filter.
    @param confirmOverwrite: Optional. If file exists will ask user to confirm overwrite. If canceled the file will not be in the returned list of paths.
    @param requiredExtension: Optional. Enforce a certain file extension.
    @return: The selected files as a list of strings
    """

def openInContactSheet(*args: Any, **kwargs: Any) -> ContactSheetViewer:
    """hiero.ui.openInContactSheet( hiero.core.Sequence ) -> Open a Sequence in a ContactSheetViewer.
    @return: hiero.ui.ContactSheetViewer object
    """

def openInNewViewer(*args: Any, **kwargs: Any) -> Viewer:
    """hiero.ui.openInNewViewer( hiero.core.BinItem ) -> Opens a BinItem's activeItem (Clip/Sequence) in a new Viewer.
    hiero.ui.openInNewViewer( hiero.core.Sequence ) -> Opens a Sequence in a new Viewer.
    hiero.ui.openInNewViewer( hiero.core.Clip ) -> Opens a Clip in a new Viewer.
    @return: hiero.ui.Viewer object
    """

def openInOSShell(*args: Any, **kwargs: Any) -> Any: ...

def openInSpreadsheet(*args: Any, **kwargs: Any) -> SpreadsheetView:
    """hiero.ui.openInSpreadsheet( hiero.core.Sequence ) -> Opens a Sequence in a Spreadsheet.
    @return: hiero.ui.SpreadsheetView object
    """

def openInTimeline(*args: Any, **kwargs: Any) -> TimelineEditor:
    """hiero.ui.openInTimeline( hiero.core.BinItem ) -> Opens a BinItem's activeItem (Clip/Sequence) in a Timeline View.
    hiero.ui.openInTimeline( hiero.core.Sequence ) -> Opens a Sequence in a Timeline View.
    hiero.ui.openInTimeline( hiero.core.Clip ) -> Opens a Clip in a Timeline View.
    @return: hiero.ui.TimelineEditor object
    hiero.ui.openInTimeline( [hiero.core.BinItem] ) -> Opens a list of BinItems' activeItems (Clips/Sequences) in a Timeline View.
    @return: tuple of hiero.ui.TimelineEditor objects
    """

def openInViewer(*args: Any, **kwargs: Any) -> Viewer:
    """hiero.ui.openInViewer( hiero.core.BinItem ) -> Opens a BinItem's activeItem (Clip/Sequence) in the Viewer.
    hiero.ui.openInViewer( hiero.core.Sequence ) -> Opens a Sequence in the Viewer.
    hiero.ui.openInViewer( hiero.core.Clip ) -> Opens a Clip in the Viewer.
    @return: hiero.ui.Viewer object
    """

def registerBinViewCustomMimeDataType(customMimeType: Any) -> Any:
    """hiero.ui.registerBinViewCustomMimeDataType(customMimeType) -> registers a custom mime type so that Hiero passes on drag and drop events through the event system. For an example of how to use this method, see the bin_drop.py example."""

def registerPanel(id: Any, command: Any) -> None: ...

def restorePanel(id: Any) -> None: ...

def sendToViewerA(*args: Any, **kwargs: Any) -> Any:
    """hiero.ui.sendToViewerA( hiero.core.BinItem ) -> Sends a BinItem's activeItem (Clip/Sequence) to the Viewer A.
    hiero.ui.sendToViewerA( hiero.core.Sequence ) -> Sends a Sequence to the Viewer A.
    hiero.ui.sendToViewerA( hiero.core.Clip ) -> Sends a Clip to the Viewer A.
    """

def sendToViewerB(*args: Any, **kwargs: Any) -> Any:
    """hiero.ui.sendToViewerB( hiero.core.BinItem ) -> Sends a BinItem's activeItem (Clip/Sequence) to the Viewer B.
    hiero.ui.sendToViewerB( hiero.core.Sequence ) -> Sends a Sequence to the Viewer B.
    hiero.ui.sendToViewerB( hiero.core.Clip ) -> Sends a Clip to the Viewer B.
    """

def trackNameValidator() -> Any: ...

def unregisterBinViewCustomMimeDataType(customMimeType: Any) -> Any:
    """hiero.ui.unregisterBinViewCustomMimeDataType(customMimeType) -> unregisters a custom mime type that was previously registered using hiero.ui.registerBinViewCustomMimeDataType()."""

def unregisterPanel(id: Any, command: Any) -> None: ...

def updateViewer(arg1: Any, arg2: Any, /) -> Any: ...

def windowManager() -> WindowManager:
    """hiero.ui.windowManager() -> returns the single WindowManager object.

    @return: hiero.ui.WindowManager
    """

ImageRenderFlag = Render.ImageRenderFlag
ImageRenderFlags = Render.ImageRenderFlag
