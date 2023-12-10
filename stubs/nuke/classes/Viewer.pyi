from typing import *
from numbers import Number

import nuke

from . import *

class Viewer(Node):
    """

    """
    def __repr__(self, ) -> None:
        """
        Return repr(self).
        """
        ...

    def __str__(self, ) -> None:
        """
        Return str(self).
        """
        ...

    def __len__(self, ) -> None:
        """
        Return len(self).
        """
        ...

    def __getitem__(self, key, ) -> None:
        """
        Return self[key].
        """
        ...

    def roi(self,) -> dict:
        """
        self.roi() -> dict
        Region of interest set in the viewer in pixel space coordinates.
        Returns None if the Viewer has no window yet.
        @return: Dict with keys x, y, r and t or None.
        """
        ...

    def roiEnabled(self,) -> Union[bool, None]:
        """
        self.roiEnabled() -> bool
        Whether the viewing of just a region of interest is enabled.
        Returns None if the Viewer has no window yet.
        @return: Boolean or None.
        """
        ...

    def setRoi(self, box:dict) -> None:
        """
        self.setRoi(box) -> None.
        Set the region of interest in pixel space.
        @param box: A dictionary with the x, y, r and t keys.@return: None.
        """
        ...

    def playbackRange(self,) -> Number:
        """
        self.playbackRange() -> FrameRange.
        Return the frame range that's currently set to be played back in the viewer.@return: FrameRange.
        """
        ...

    def visibleRange(self,) -> Number:
        """
        self.visibleRange() -> FrameRange.
        Return the frame range that is currently visible in the viewer.@return: FrameRange.
        """
        ...

    def frameCached(self,f) -> bool:
        """
        frameCached(f) -> Bool

        Determine whether frame /f/ is known to be in the memory cache.
        """
        ...

    def sendMouseEvent(self,) -> bool:
        """
        sendMouseEvent() -> Bool

        Temporary:
        Post a mouse event to the viewer window.
        """
        ...

    def recordMouse(self,) -> bool:
        """
        recordMouse() -> Bool

        Start viewer window mouse recording.@return: Recording started?
        """
        ...

    def recordMouseStop(self,) -> None:
        """
        recordMouseStop()

        Stop viewer window mouse recording.
        """
        ...

    def replayMouseSync(self, xmlRecordingFilename) -> bool:
        """
        replayMouseSync(xmlRecordingFilename) -> Bool

        Start direct (synchronous) playback of a viewer window mouse recording.@param: Name of recording xml file to play@return: Replay succeeded?
        """
        ...

    def replayMouseAsync(self, xmlRecordingFilename) -> bool:
        """
        replayMouseAsync(xmlRecordingFilename) -> Bool

        Start timer based (asynchronous) playback of a viewer window mouse recording.@param: Name of recording xml file to play@return: Replay started?
        """
        ...

    def isPlayingOrRecording(self,) -> bool:
        """
        isPlayingOrRecording() -> Bool

        @return: Is a recording being made or played?
        """
        ...

    def toggleMouseTrails(self,) -> bool:
        """
        toggleMouseTrails() -> Bool

        Toggle mouse trails in the viewer window on/off.@return: Trails now showing?
        """
        ...

    def toggleWaitOnEvents(self,) -> bool:
        """
        toggleWaitOnEvents() -> Bool

        Toggle whether asynchronous playback waits on each event.
        Otherwise events will be handled by the next nuke update.@return: Now waiting?
        """
        ...

    def capture(self,file) -> None:
        """
        capture(file) -> None

        Capture the viewer image to a file.  Only jpg files are supported at present.  The image is captured immediately even if the viewer is mid-render.To capture a fully rendered image at a frame or frame range use nuke.render passing in the viewer node you want to capture.When using nuke.render the filename is specified by the 'file' knob on the viewer node.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
