# Type stubs for nuke 15.2v9. Generated; do not edit.

"""********************************************************************************
IMPORTANT: Most of the code in this file is now deprecated, with the replacement
functionality in FnNukeHelpersV2. Some of the functions are still in use (e.g.
for writing Clips, EffectTrackItems, Annotations).

If you make any further improvements to the code in this file, please move it
to FnNukeHelpersV2, clean it up, apply the changes there, and modify any usages
of it to the new version.
********************************************************************************

Punch addToNukeScript() functions into core classes to add equivalent Nuke nodes to a given script.
"""

from typing import Any
from hiero.core import Annotation as Annotation
from hiero.core import AnnotationStroke as AnnotationStroke
from hiero.core import AnnotationText as AnnotationText
from hiero.core import Clip as Clip
from hiero.core import EffectTrackItem as EffectTrackItem
from hiero.core import Format as Format
from hiero.core import Keys as Keys
from hiero.core import Sequence as Sequence
from hiero.core import TrackItem as TrackItem
from hiero.core import Transition as Transition
from hiero.core import VideoTrack as VideoTrack
from hiero.core import nuke as nuke
from hiero.core.FnCompSourceInfo import CompSourceInfo as CompSourceInfo
from hiero.core.FnCompSourceInfo import isNukeScript as isNukeScript
import hiero as hiero

localisationMap: dict

class NodeAnimationOffsetter:
    """Context manager for temporarily offsetting the animation on a node in a with block. """
    def __enter__(self) -> Any: ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...
    def __init__(self, node: Any, offset: Any) -> None: ...

def createAndAddNodesToGroupNode(name: Any, nodesToGroup: Any, addedNodesList: Any) -> Any: ...

def createAnnotationsGroup(script: Any, annotations: Any, offset: Any, inputs: Any, cliptype: Any = ...) -> list[Any]:
    """Add a list of annotations to a script and place them inside a group. """

def getConnectedDisconnectedTracks(sequence: Any, masterTracks: Any, disconnected: Any, includeEffects: Any, includeAnnotations: Any, view: Any = ...) -> tuple[list[Any], list[Any]]:
    """Helper function to determine the connected and disconnected tracks for the
    given sequence, master tracks (possibly one per view) and disconnected setting.
    This can also filter the tracks for a particular view 
    """

def getRetimeSourceOut(trackItem: Any) -> Any:
    """Determine the track item source out frame for writing to the OFlow node.
    This is now floored so the final frame matches what you get in the viewer, rather than possibly blending between two frames if the sourceOut() value didn't return an integer.
    The previous version of this is left commented out, this was added for Bug 45704, but caused incorrect behaviour in other cases. 
    """

def isNonZeroStartFrameMovieFile(filename: Any) -> bool:
    """Returns True if the filename is a from a movie file which Nuke must read from frame 1 or later (e.g. QuickTime/FFmpeg/MXF), False otherwise"""

def nukeColourTransformNameFromHiero(colourTransformName: Any, projectsettings: Any) -> str:
    """Hiero and Nuke can have different names for equivalent colour transforms.
    This function converts from a hiero colour transform to a nuke one.

    TODO Don't think this function is necessary any more, but it's still in use,
    so leaving it alone for now
    """

def offsetNodeAnimationFrames(node: Any, offset: Any) -> None:
    """Iterate over all the knobs in a Nuke node, offsetting the key frame numbers. """
