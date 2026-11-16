# Type stubs for nuke 15.2v9. Generated; do not edit.

"""A file for helper functions related to exporting which may be shared between
tasks.
"""

from typing import Any
from hiero.core import FnNukeHelpers as FnNukeHelpers
from hiero.core import FnNukeHelpersV2 as FnNukeHelpersV2
from hiero.core import nuke as nuke
import hiero as hiero

class TrackItemExportScriptWriter:
    """Helper class for writing TrackItems to a Nuke script. This provides a
    higher-level wrapper around the code in FnNukeHelpers/FnNukeHelpersV2.
    TODO Could probably be got rid of with some refactoring.
    """
    def __init__(self, trackItem: Any) -> None: ...
    def setAdditionalNodesCallback(self, callback: Any) -> None: ...
    def setAnnotations(self, shouldWrite: Any, sequenceAnnotations: Any = ...) -> None:
        """Set whether annotations should be written and add any Sequence-level
        effects that should be included.
        """
    def setEffects(self, shouldWrite: Any, sequenceEffects: Any = ...) -> None:
        """Set whether effects should be written and add any Sequence-level
        effects that should be included.
        """
    def setFirstFrame(self, firstFrame: Any) -> None:
        """Set the first frame of the script.  This is used to apply appropriate
        offsets to the written nodes.
        """
    def setIncludeRetimes(self, includeRetimes: Any, retimeMethod: Any) -> None:
        """Set whether retime nodes should be written and the retime method knob
        value.
        """
    def setOutputClipLength(self) -> None:
        """Set to output the full clip length.  Calculates the handle values
        accordingly.
        """
    def setOutputHandles(self, startHandle: Any, endHandle: Any) -> None:
        """Set the handles to be included around the TrackItem cut times in
        the exported script.
        """
    def setReformat(self, reformatProperties: Any) -> None:
        """Sets information for reformatting in the Nuke script"""
    def writeToScript(self, script: Any, pendingNodesScript: Any = ...) -> None: ...
    def writeToScript_old(self, script: Any) -> None:
        """Add the nodes for the TrackItem to a script writer.
    
        """

def createViewerNode(projectSettings: Any) -> Any:
    """Create a Viewer node, with the viewerProcess configured based on the
    projectSettings.
    """

def trackItemTimeCodeNodeStartFrame(scriptStartFrame: Any, trackItem: Any, startHandle: Any, endHandle: Any) -> Any:
    """Calculate the frame for an AddTimeCode node when exporting a single track item to a Nuke script, adjusting
    for the trim and handles.

    If playback speed is positive, this should be offset by the track item's source in and the start handle.
    Otherwise the offset should use the source out and end handle.
    """

def writeSequenceAudioWithHandles(filePath: Any, sequence: Any, inTime: Any, outTime: Any, inHandle: Any, outHandle: Any, numChannels: Any, sampleRate: Any, bitDepth: Any, bitRate: Any) -> None:
    """Helper function for writing audio on a sequence with handles. This will:
    - find audio items which intersect the original time range
    - if they intersect the start or end times, extend those items by the in/out
      handles specified
    - write out the audio file with the given time range, plus handles
    """
