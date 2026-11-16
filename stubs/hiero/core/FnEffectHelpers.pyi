# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from typing import Generator
from hiero.core import EffectTrackItem as EffectTrackItem
from hiero.core import ReformatState as ReformatState
from hiero.core import TrackItem as TrackItem
from hiero.core import formats as formats
from hiero.core.find_items import findItemsInAllProjects as findItemsInAllProjects
from nuke import Undo as Undo

EffectTransforms: dict

class EffectTransform:
    """Class for handling scale and translation of effect knob values. """
    def __init__(self, scaleX: float = ..., scaleY: float = ..., translateX: float = ..., translateY: float = ...) -> None: ...
    def __str__(self) -> str: ...
    def getScale(self) -> tuple[Any, Any]: ...
    def scaleX(self, value: Any) -> Any: ...
    def scaleY(self, value: Any) -> Any: ...
    def setScale(self, scaleX: Any, scaleY: Any) -> None: ...
    def setTranslate(self, translateX: Any, translateY: Any) -> None: ...
    def translateAndScaleX(self, value: Any) -> Any: ...
    def translateAndScaleY(self, value: Any) -> Any: ...

class FormatChange:
    """Helper class for calculating the changes between two formats. """
    def __init__(self, newFormat: Any, oldFormat: Any, clipFormat: Any = ..., reformatState: Any = ...) -> None: ...
    def calculateCenterOffset(self, transform: Any) -> None:
        """Add translation required to center the image for the scale in the
        given transform.
        """
    def calculateScale(self, resizeType: Any) -> tuple[Any, Any]:
        """Calculate the scaling from the old format to the new format for the given
        resize type.
        """
    def getTransformForFormat(self) -> EffectTransform:
        """Get the transform to shift to the new format, taking into account the
        clip reformat state.
        """
    def getTransformForFormatNoReformatState(self) -> EffectTransform:
        """Calculate the transform for a format change. This just scales by the ratio
        of the width/height of the old to new format. 
        """
    def getTransformForReformatState(self) -> EffectTransform:
        """Calculate the transform for a format change, taking into account the
        reformat settings on a track item.
        """
    def getTransformOffsetUnscaledClip(self) -> EffectTransform:
        """If clips are not scaled to sequence format, when the format changes
        transforms should just be offset to compensate for the centering of the clip
        in the new format.
        """
    def hasUnscaledClip(self) -> dict[str, Any] | None: ...
    def heightRatio(self) -> float: ...
    def isClipReformatCentered(self) -> None:
        """Check if the clip is centered in the sequence format. This is always
        true if set to 'disabled'.
        """
    def newHeight(self) -> float: ...
    def newWidth(self) -> float: ...
    def oldHeight(self) -> float: ...
    def oldWidth(self) -> float: ...
    def reformatStateResizeCenter(self) -> None: ...
    def reformatStateResizeType(self) -> None: ...
    def reformatStateType(self) -> None: ...
    def widthRatio(self) -> float: ...

def calculateReformat(inFormat: Any, outFormat: Any, resizeType: Any, center: Any, scale: Any) -> tuple[Any, Any, Any, Any]:
    """Converts from inFormat to outFormat using the specified resizeType and
    center to determine how the reformat should happen.  Returns a tuple
    (x, y, w, h) providing the format's coordinates within the new format space.
    The logic of this function comes from the Reformat node, but ommitting
    flip, flop and turn.
    """

def effectInputSourceCoods(effectItem: Any) -> tuple[int, int, Any, Any] | tuple[int, int, int, int]:
    """Find the track item linked to the given effectItem and return the coordinates of its 
    source clip  mapped to the sequence output format space. If there is no linked track item,
    the coordinates of the sequence format is returned.
    @param effectItem: a soft effect in a sequence
    """

def executeEffectNode(effectNode: Any, frames: Any) -> None:
    """Execute a node belonging to a soft effect in the timeline. This is similar
    to the nuke.execute() function.
    @param effectNode: the node to execute
    @param frames: a sequence of frame numbers to execute
    """

def findLinkedTrackItem(effectItem: Any) -> None:
    """Find the main video track item linked to an effect. """

def iterSequenceEffects(sequence: Any) -> Generator[Any, Any, None]:
    """Generator for iteration over the EffectTrackItems in a sequence. """

def reformatStateToDict(reformatState: Any) -> dict[str, Any]:
    """Helper to convert hiero.core.ReformatState to dict. """

def transformEffectToFormat(effectItem: Any, format: Any, oldFormat: Any, errorCallback: Any) -> None: ...

def transformNodeToFormatChange(node: Any, formatChange: Any, errorCallback: Any) -> None: ...

def transformSequenceEffectsToFormat(sequence: Any, format: Any, oldFormat: Any, errorCallback: Any) -> None: ...
