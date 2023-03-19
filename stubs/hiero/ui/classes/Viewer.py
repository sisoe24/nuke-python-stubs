import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class Viewer(QObject):
    """
    Object for manipulating viewers in Hiero. Get the currently active viewer by calling hiero.ui.currentViewer().
    """

    def __setattr__(self, name, value, ):
        """
        Implement setattr(self, name, value).
        """
        return None

    def __delattr__(self, name, ):
        """
        Implement delattr(self, name).
        """
        return None

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def annotationTool(self) -> ui.ViewerTool:
        """
        self.annotationTool() -> return the annotation tool for this viewer.
        """
        return ui.ViewerTool()

    def availableGuideOverlayNames(self) -> typing.Set*args:
        """
        self.availableGuideOverlayNames() -> returns the names of all the guide overlays available in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: The names of all the guide overlays available in the viewer
        """
        return str()

    def cachedFrames(self) -> typing.Set*args:
        """
        self.cachedFrames() -> get the frames which are currently cached in the viewer.

        @return: set containing the indices of the cached frames
        """
        return int()

    def channels(self) -> ui.Player.Channels:
        """
        self.channels() -> returns the current channels in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer clip player's current channels
        """
        return Viewer()

    def compareMode(self) -> ui.Viewer.CompareMode:
        """
        self.compareMode() -> returns the compare mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer.CompareMode object
        """
        return Viewer()

    def currentLayerName(self) -> str:
        """
        self.currentLayerName() -> returns the name of the current channels layer the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer clip player's channels layer name
        """
        return str()

    def cursorTool(self) -> ui.ViewerCursorTool:
        """

        """
        return ui.ViewerCursorTool()

    def displayDropFrames(self) -> bool:
        """
        self.displayDropFrames() -> True if the drop frames are beingdisplayed on the time format (when timecode is displayed)

        @return: True if the display frames are being displayed
        """
        return bool()

    def displayTimecode(self) -> bool:
        """
        self.displayTimecode() -> True if the timecode is being displayed on the time format

        @return: True if the timecode is being displayed
        """
        return bool()

    def enterFullScreen(self) -> None:
        """
        self.enterFullScreen() -> puts the viewer into full screen mode. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.
        """
        return None

    def exitFullScreen(self) -> None:
        """
        self.exitFullScreen() -> takes the viewer out of full screen mode. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.
        """
        return None

    def flushCache(self) -> None:
        """
        self.flushCache() -> flush the cache on the viewer and pause caching.
        """
        return None

    def frameIncrement(self) -> int:
        """
        self.frameIncrement() -> returns the frame increment for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: the number of frames to skip or nudge
        """
        return Number()

    def gain(self) -> float:
        """
        self.gain() -> returns the gain value for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer clip player's gain value
        """
        return Viewer()

    def gamma(self) -> float:
        """
        self.gamma() -> returns the gamma value for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer clip player's gamma value
        """
        return Viewer()

    def getAchievedFPS(self) -> float:
        """
        self.getAchievedFPS() -> returns the average fps achieved by the viewer.

        @return: floating point frames per second average
        """
        return float()

    def goToNextEdit(self) -> None:
        """
        self.goToNextEdit() -> Move playhead to next edit. Can only be called from the user interface thread.
        """
        return None

    def goToNextTag(self) -> None:
        """
        self.goToNextTag() -> Move playhead to next tag. Can only be called from the user interface thread.
        """
        return None

    def goToPrevEdit(self) -> None:
        """
        self.goToPrevEdit() -> Move playhead to previous edit. Can only be called from the user interface thread.
        """
        return None

    def goToPrevTag(self) -> None:
        """
        self.goToPrevTag() -> Move playhead to previous tag. Can only be called from the user interface thread.
        """
        return None

    def image(self) -> PySide2.QtGui.QImage:
        """
        self.image() -> returns the contents of the viewer as an image, including all overlays. Can only be called from the user interface thread.

        @return: a PySide2.QtGui.QImage object
        """
        return Any

    def isCachingPaused(self) -> bool:
        """
        self.isCachingPaused() -> get whether caching is paused.

        @return: bool
        """
        return bool()

    def layoutMode(self) -> ui.Viewer.LayoutMode:
        """
        self.layoutMode() -> returns the layout mode the viewer is currently in.

        @return: a Viewer.LayoutMode object
        """
        return Viewer()

    def maskOverlayName(self) -> str:
        """
        self.maskOverlayName() -> returns the name of the current mask overlay in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: The name of the mask overlay currently active in the viewer
        """
        return str()

    def maskOverlayStyle(self) -> ui.Player.MaskOverlayStyle:
        """
        self.maskOverlayStyle() -> returns the current mask overlay style set in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: The current mask overlay style active in the viewer
        """
        return ui.Player.MaskOverlayStyle()

    def overlaysShown(self) -> bool:
        """
        self.overlaysShown() -> get whether overlays are shown in the viewer.

        @return: bool
        """
        return bool()

    def pauseCaching(self) -> None:
        """
        self.pauseCaching() -> pause caching on the viewer.
        """
        return None

    def play(self) -> None:
        """
        self.play() -> starts playback in the viewer in the forward direction. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.
        """
        return None

    def playBackwards(self) -> None:
        """
        self.playBackwards() -> starts playback in the viewer in the backwards direction. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.
        """
        return None

    def playForwards(self) -> None:
        """
        self.playForwards() -> starts playback in the viewer in the forward direction. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.
        """
        return None

    def playbackMode(self) -> ui.Viewer.PlaybackMode:
        """
        self.playbackMode() -> returns the compare mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: a Viewer.PlaybackMode object
        """
        return Viewer()

    def playbackSpeed(self) -> int:
        """
        self.playbackSpeed() -> Get the current playback speed, which will be 0 if playback is not currently in progress.
        """
        return int()

    def player(self, index: int = 0) -> ui.Player:
        """
        self.player(index) -> returns the player object attached to this viewer, based on the input index.

        @param index: integer index of the player to retrieve
        @return: hiero.ui.Player object
        """
        return Player()

    def resumeCaching(self) -> None:
        """
        self.resumeCaching() -> resume caching on the viewer.
        """
        return None

    def selectedGuideOverlayNames(self) -> typing.Set*args:
        """
        self.selectedGuideOverlayNames() -> returns the names of the current guide overlays in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @return: The names of all the guide overlays currently active in the viewer
        """
        return str()

    def setChannels(self, channels: ui.Player.Channels) -> None:
        """
        self.setChannels(channels) -> Sets the channels in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param channels: the channels to be set in the viewer
        """
        return None

    def setCompareMode(self, mode: ui.Viewer.CompareMode) -> None:
        """
        self.setCompareMode(mode) -> changes the compare mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param compareMode: a Viewer.CompareMode value
        """
        return None

    def setDisplayTimecode(self, displayTimecode: bool) -> None:
        """
        self.setDisplayTimecode(displayTimecode) -> Sets the viewer to display Timecode if 'displayTimecode' is True, or Timeline Frame otherwise

        @return: None
        """
        return None

    def setFrameIncrement(self, frameIncrement: int) -> None:
        """
        self.setFrameIncrement(frames) -> changes the frame increment for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param frames: the number of frames to skip or nudge
        """
        return None

    def setGain(self, gain: float) -> None:
        """
        self.setGain(gain) -> changes the gain for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param gain: a gain value to be set in the viewer
        """
        return None

    def setGamma(self, gamma: float) -> None:
        """
        self.setGamma(gamma) -> changes the gamma for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param gamma: a gamma value to be set in the viewer
        """
        return None

    def setGuideOverlayFromRemote(self, overlayNames: typing.Set*args) -> None:
        """
        self.setGuideOverlayFromRemote() -> Sets the guide overlays in the viewer from a remote source. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param overlayNames: the names of the overlays to be set
        @param remoteOverlaysAvailable: the names of the overlays that are available to the remote client
        """
        return None

    def setLayer(self, layerName: str) -> None:
        """
        self.setLayer(layerName) -> Sets the channels layer in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param layerName: the name of the channels layer to be set in the viewer
        """
        return None

    def setLayoutMode(self, layoutMode: ui.Viewer.LayoutMode) -> None:
        """
        self.setLayoutMode(mode) -> changes the layout mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param layoutMode: a Viewer.LayoutMode value indicating what layout to set the viewer to
        """
        return None

    def setMaskOverlayFromRemote(self, overlayName: str) -> None:
        """
        self.setMaskOverlayFromRemote() -> Sets the guide overlays in the viewer from a remote source. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param remoteOverlayName: the name of the overlay to be set
        """
        return None

    def setMaskOverlayStyle(self, pyStyle: ui.Player.MaskOverlayStyle) -> None:
        """
        self.setMaskOverlayStyle() -> Sets the channels in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param pyStyle: the mask style to be set in the viewer
        """
        return None

    def setOverlaysShown(self, show: bool) -> None:
        """
        self.setOverlaysShown(show) -> set whether overlays are shown in the viewer.

        @param show: bool
        """
        return None

    def setPlaybackMode(self, mode: ui.Viewer.PlaybackMode) -> None:
        """
        self.setCompareMode(mode) -> changes the playback mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param mode: a Viewer.PlaybackMode value
        """
        return None

    def setPlaybackSpeed(self, speed: int) -> None:
        """
        self.setPlaybackSpeed(speed) -> Set the current playback speed. Setting to 0 will stop, -1 play in reverse, etc.
        """
        return None

    def setPlayer(self, index: int) -> None:
        """
        self.setPlayer(index) -> sets the active player if index is a valid player index.

        @param index: integer index of the player to set as the active player
        """
        return None

    def setSequence(self, sequence: core.SequenceBase, indexOfPlayer: int) -> None:
        """
        self.setSequence() -> set the sequence for this viewer

        @param sequence: the sequence to set on this viewer
        @param indexOfPlayer: index to specify which of the players the sequence should be set on
        """
        return None

    def setTime(self, time: int) -> None:
        """
        self.setTime(time) -> seeks the play head of the viewer to the time parameter. Works the same as scrubbing the timeline in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param time: frame to set the play head to
        """
        return None

    def setTimeDisplayFormat(self, displayTimecode: bool, displayDropFrames: bool) -> None:
        """
        self.setTimeDisplayFormat() -> Change the current time display format of the viewer

        @param displayTimecode: Display timecode
        @param displayDropFrames: Display drop frames
        """
        return None

    def setTracksMask(self, indexOfPlayer: int, tracksMask: ui.TracksMask) -> None:
        """
        self.setTracksMask() -> modify the status of the tracks of one of the buffers. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param indexOfPlayer: integer index of the player
        @param tracksMask: TracksMask instance
        """
        return None

    def setView(self, name: str, viewIndex: int = 0) -> None:
        """
        setView(name, viewIndex) -> If name matches an existing view then the Viewers's active view for viewIndex is set to the view given by name.
        @param name: string
        @param viewIndex: optional; integer (for example in stereo a viewIndex of 0 corresponds to the primary view and 1 to the secondary view)
        """
        return None

    def stop(self) -> None:
        """
        self.stop() -> stops playback in the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.
        """
        return None

    def syncShuttleTargetFPS(self, fps: float) -> None:
        """
        self.syncShuttleTargetFPS() -> Syncs the current target frame rate of the shuttle target frame rate

        @param fps: Target frame rate for the shuttle tool
        """
        return None

    def syncTargetFrameRate(self, numerator: int, denominator: int) -> None:
        """
        self.syncTargetFrameRate() -> Syncs the target frame rate of the viewer when it is modifiedby other client during a sync review

        @param numerator: Numerator of the target frame rate
        @param denominator: Denominator of the target frame rate
        """
        return None

    def time(self) -> int:
        """
        self.time() -> returns the current frame of the viewer.
        """
        return int()

    def toggleFullScreen(self) -> None:
        """
        self.toggleFullScreen() -> toggles full screen mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.
        """
        return None

    def toggleFullScreen1_1(self) -> None:
        """
        self.toggleFullScreen1_1() -> toggles 1:1 full screen mode for the viewer. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.
        """
        return None

    def tracksMask(self, indexOfPlayer: int) -> ui.TracksMask:
        """
        self.tracksMask() -> returns status of the tracks of one of the buffers. Can only be called from the user interface thread. Use hiero.core.executeInMainThread if you need to call it from a non-ui thread.

        @param indexOfPlayer: integer index of the player
        @return: TracksMask instance
        """
        return TracksMask()

    def view(self, viewIndex: int = 0) -> str:
        """
        view(viewIndex) -> Returns the name of the active view for viewIndex.
        @param viewIndex: optional; integer (for example in stereo a viewIndex of 0 corresponds to the primary view and 1 to the secondary view)
        """
        return str()

    def window(self) -> PySide2.QtWidgets.QWidget:
        """
        self.window() -> Return the viewer window
        """
        return Any

    def wipeTool(self) -> ui.ViewerWipeTool:
        """
        self.wipeTool() -> return the wipe tool for this viewer
        """
        return ui.ViewerWipeTool()

    LayoutMode: Any = None
    eLayoutWipe: Any = None
    eLayoutStack: Any = None
    eLayoutHorizontal: Any = None
    eLayoutVertical: Any = None
    eLayoutGrid: Any = None
    eLayoutFree: Any = None
    CompareMode: Any = None
    eCompareNoBlend: Any = None
    eCompareOver: Any = None
    eCompareUnder: Any = None
    eCompareOnionSkin: Any = None
    eCompareDifference: Any = None
    eCompareInvertAndAdd: Any = None
    eCompareMinus: Any = None
    PlaybackMode: Any = None
    ePlaybackRepeat: Any = None
    ePlaybackBounce: Any = None
    ePlaybackStop: Any = None
    ePlaybackContinue: Any = None
    compareModeChanged = Signal()
    layoutModeChanged = Signal()
    transformChanged = Signal()
    maskOverlayChanged = Signal()
    gammaChanged = Signal()
    targetFrameRateChanged = Signal()
    gainChanged = Signal()
    sequenceChanged = Signal()
    maskOverlayStyleChanged = Signal()
    playbackSpeedChanged = Signal()
    currentLayerChanged = Signal()
    shuttleTargetFPSChanged = Signal()
    timeDisplayFormatChanged = Signal()
    trackSelectionChanged = Signal()
    timeChanged = Signal()
    channelsChanged = Signal()
    playbackModeChanged = Signal()
    frameDisplayed = Signal()
    guideOverlayChanged = Signal()
    staticMetaObject: Any = None

    def _goToTag(self, tag: str):
        """
        Move playhead to Tag.
        If Tag (Tag Object or Tag name) does not exists on the Viewer's Sequence/Clip
        a KeyError is raised.

        @param tag: a Tag object or the name of the desired tag.
        """
        return None

    def _goToInTime(self):
        """
        Move playhead to In point
        """
        return None

    def _goToOutTime(self):
        """
        Move playhead to Out point
        """
        return None

    def _goToTrackItemStart(self, trackItem: Iterable):
        """
        Move playhead to start of the trackItem.

        @param trackItem: sequence's track item.
        """
        return None

    def _goToTrackItemEnd(self, trackItem: Iterable):
        """
        Move playhead to end of the trackItem.

        @param trackItem: sequence's track item.
        """
        return None

    def _goToTrackItemMiddle(self, trackItem: Iterable):
        """
        Move playhead to middle of the trackItem.

        @param trackItem: sequence's track item.
        """
        return None

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None
