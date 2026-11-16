# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
from typing import final
import hiero.core as _hiero_core
import hiero.core.FnExporterBase as _hiero_core_FnExporterBase
import hiero.exporters.FnShotExporter as _hiero_exporters_FnShotExporter
import hiero.ui as _hiero_ui
from hiero.core import Annotation as Annotation
from hiero.core import FnNukeHelpers as FnNukeHelpers
from hiero.core import SequenceBase as SequenceBase
from hiero.core import nuke as nuke
from hiero.exporters import FnScriptLayout as FnScriptLayout
from hiero.exporters import FnShotExporter as FnShotExporter
from hiero.exporters.FnExportUtil import OutputTransformKnobs as OutputTransformKnobs
from hiero.exporters.FnExportUtil import TransformTypeValues as TransformTypeValues
from hiero.exporters.FnExportUtil import createViewerNode as createViewerNode
import hiero as hiero
import nuke_internal as nuke_internal

class AnnotationExportInfo:
    """AnnotationExportInfo(annotation: core.Annotation, startFrame: int, endFrame: int, parentSequence: core.SequenceBase)"""
    def __eq__(self, other: Any) -> bool: ...
    def __init__(self, annotation: _hiero_core.Annotation, startFrame: int, endFrame: int, parentSequence: _hiero_core.SequenceBase) -> None: ...
    def __repr__(self) -> str: ...

class NukeAnnotationsExporter(_hiero_exporters_FnShotExporter.ShotTask):
    """Exporter for rendering and exporting annotation frames as PNG images.

    Renders clip and sequence level annotations using renderSequenceToImage.
    A Read node is created to display the exported annotation images (black where
    no annotations exist), and a NoOp node stores annotation metadata
    (annotation_key / annotation_count) for navigation between annotations.
    """
    def __init__(self, initDict: Any) -> None: ...
    def createAnnotationsOp(self, script: Any) -> None:
        """Create a Nuke NoOp node to store annotation keyframes.
        Adds user knobs for navigating annotations and sets keyframe data with frame offsets.
        """
    def createOCIODisplayNode(self, script: Any) -> None:
        """Create an OCIODisplay node from the values in self._outputTransformParams and adds it to script. """
    def createReadNode(self, script: Any) -> None:
        """Create a Nuke Read node for all exported images, keyed by frame."""
    def exportImages(self) -> bool:
        """Render and export annotation keyframe images using renderSequenceToImage."""
    def getAnnotationsExportInfo(self) -> list[Any]:
        """Get all annotation time ranges from sequence and clip annotations within the clip's source range."""
    def getClipAnnotationsOffset(self) -> int:
        """Calculate the frame offset needed to align annotation times with the clip's
        exported frame range, taking into account custom start frames and cut handles.
        """
    def getParentSequence(self) -> None:
        """Get the original parent sequence"""
    def getResolvedExportPath(self) -> str:
        """Return the resolved export path with a frame sequence pattern."""
    def getSourceInOut(self) -> tuple[Any, Any]:
        """Return the in and out frame range for the clip.
        Adjusts for full-clip exports if cut handles are not set.
        """
    def runOnMainThread(self) -> bool: ...
    def setupOutputTransformParams(self) -> None:
        """Set up the parameters for the output transform to be applied when rendering. Creates a Write node to get
        the correct defaults from the project's OCIO config.
        """
    def taskStep(self) -> bool: ...
    def updateItem(self, originalItem: Any, localtime: Any) -> None: ...

class NukeAnnotationsPreset(_hiero_core_FnExporterBase.TaskPresetBase):
    kFileTypeDefault: str
    kFileTypeExtensions: dict
    kFileTypeOptions: tuple
    kFileTypeProperty: str
    def __init__(self, name: Any, properties: Any) -> None: ...
    def addCustomResolveEntries(self, resolver: Any) -> None: ...
    def supportedItems(self) -> Any: ...

@final
class ProgressTask:
    """ProgressTask"""
    kDelayedPopup: int
    kDisable: int
    kKeepWhenFinished: int
    kModal: int
    kShowTimeToGo: int
    kUserCanCancel: int
    kUserCanPause: int
    def isCancelled(self) -> bool:
        """self.isCancelled() -> True if the user has requested the task to be cancelled."""
    def setMessage(self, s: Any) -> None:
        """self.setMessage(s) -> None.

        set the message for the progress task
        """
    def setProgress(self, i: Any) -> None:
        """self.setProgress(i) -> None.

        i is an integer representing the current progress
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> ProgressTask: ...

def annotationCommentToJsonHelper(comment: Any) -> dict[str, Any]: ...

def annotationToJsonHelper(annotationInfo: Any, offset: Any) -> dict[Any, Any]: ...

def annotationsToJson(annotationTimeRanges: Any, offset: Any) -> str: ...

def escapeString(string: Any) -> Any: ...

def renderSequenceToImage(sequence: Any, frame: Any, renderFlags: Any, colorspace: Any = ..., ocioDisplay: Any = ..., ocioView: Any = ...) -> Any:
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

ImageRenderFlag = _hiero_ui.Render.ImageRenderFlag
