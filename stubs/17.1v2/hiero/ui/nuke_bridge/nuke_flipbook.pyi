# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import nukescripts.flipbooking as _nukescripts_flipbooking
import nukescripts.renderdialog as _nukescripts_renderdialog
from hiero.FnRedirect import menuBar as menuBar
from hiero.core import log as log
from hiero.core import util as util
from hiero.ui import findMenuAction as findMenuAction
from hiero.ui.nuke_bridge.flipbook_common import getColorspaceFromNode as getColorspaceFromNode
from hiero.ui.nuke_bridge.flipbook_common import getIsUsingNukeColorspaces as getIsUsingNukeColorspaces
from hiero.ui.nuke_bridge.flipbook_common import getOCIOConfigPath as getOCIOConfigPath
from hiero.ui.nuke_bridge.flipbook_common import getRawViewerLUT as getRawViewerLUT
from hiero.ui.nuke_bridge.flipbook_common import mapViewerLUTString as mapViewerLUTString
from nuke_internal.executeInMain import executeInMainThreadWithResult as executeInMainThreadWithResult
from nukescripts import captureViewer as captureViewer
from nukescripts import flipbooking as flipbooking
from nukescripts.fnFlipbookRenderer import getFlipbookRenderer as getFlipbookRenderer
from nukescripts.panels import PythonPanel as PythonPanel
from nukescripts.renderdialog import DialogState as DialogState
from nukescripts.renderdialog import ExecuteDialog as ExecuteDialog
from nukescripts.renderdialog import FlipbookDialog as FlipbookDialog
from nukescripts.renderdialog import RenderDialog as RenderDialog
from nukescripts.renderdialog import ViewerCaptureDialog as ViewerCaptureDialog
from nukescripts.renderdialog import ViewerCaptureDialogThread as ViewerCaptureDialogThread
from nukescripts.renderdialog import bboxToTopLeft as bboxToTopLeft
from nukescripts.renderdialog import setFlipbookDefaultOption as setFlipbookDefaultOption
from nukescripts.renderdialog import setRenderDialogDefaultOption as setRenderDialogDefaultOption
from nukescripts.renderdialog import showExecuteDialog as showExecuteDialog
from nukescripts.renderdialog import showFlipbookDialog as showFlipbookDialog
from nukescripts.renderdialog import showFlipbookDialogForSelected as showFlipbookDialogForSelected
from nukescripts.renderdialog import showRenderDialog as showRenderDialog
from nukescripts.renderdialog import showViewerCaptureDialog as showViewerCaptureDialog
import hiero as hiero
import nukescripts as nukescripts
import ocionuke as ocionuke

gFlipbookViewer: Any
kNukeFlipbookCapabilities: dict

class LUTCorrection:
    """Base class for objects which correct the LUT of a flipbook render."""
    def __init__(self, manager: Any) -> None: ...

class CustomLUTCorrection(LUTCorrection):
    """LUT correction for when when using a custom OCIO config is being used."""
    def applyLUT(self, videoTrack: Any, first: Any, last: Any, inColorspace: Any) -> None: ...
    def isLUTAvailableForNode(self, node: Any) -> bool: ...

class FlipbookEventHandler:
    def __init__(self) -> None: ...
    def onContextChanged(self, event: Any) -> None:
        """Notification that keyboard focus has changed. """

class FlipbookNuke(_nukescripts_flipbooking.FlipbookApplication):
    """The Nuke built in flipbook"""
    LUT_OUT_DELIM: str
    def __init__(self) -> None: ...
    def cacheDir(self) -> Any: ...
    def capabilities(self) -> dict[str, Any]: ...
    def dialogKnobs(self, parent: Any) -> None: ...
    def flipbook(self, videoClips: Any, audioClip: Any, first: Any, last: Any, views: Any, options: Any) -> Any:
        """Flipbook a set of video clips.
        This method creates a sequence with all the video clips and the audio clip and plays it
        from first to last.
        @param videoClips: a list of tuples with ( clip, inputColorspace). The input colorspace
        for each clip is used to add a softeffect to correct the clip colorspace to linear to be
        @param audioClip: a audio clip to be added to the sequence
        @param first: defines the In position
        @param last: defines the Out position
        @param options: A dictionary of options to use.
        """
    def getExtraOptions(self, flipbookDialog: Any, nodeToFlipbook: Any) -> dict[Any, Any]:
        """Implements FlipbookApplication.getExtraOptions"""
    def isLUTAvailableForNode(self, node: Any) -> bool: ...
    def name(self) -> str: ...
    def path(self) -> Any: ...
    def run(self, filename: Any, frameRanges: Any, views: Any, options: Any) -> None: ...
    def runFromNode(self, nodeToFlipbook: Any, frameRanges: Any, views: Any, options: Any) -> None:
        """Execute the fipbook on a node.
        If the node is a AppendClip and all the inputs are Read nodes, the flipbook
        will be executed directly with the inputs filenames  instead of rendering
        everything.
        """

class NukeDefaultLUTCorrection(LUTCorrection):
    """LUT correction for when the default Nuke OCIO config is used."""
    def applyLUT(self, videoTrack: Any, first: Any, last: Any, inColorspace: Any) -> None: ...
    def isLUTAvailableForNode(self, node: Any) -> bool: ...

def fixedAudioFlipbookDialogPostKnobs(self: Any) -> None: ...

def recursiveSetActionVisibility(action: Any, visible: Any) -> None: ...

flipbookDialogRequiredIntermediateNode = _nukescripts_renderdialog.FlipbookDialog._requireIntermediateNode
oldPostKnobs = _nukescripts_renderdialog.FlipbookDialog._addPostKnobs
