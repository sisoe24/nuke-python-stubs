# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import hiero.core.FnExporterBase as _hiero_core_FnExporterBase
import hiero.exporters.FnExternalRender as _hiero_exporters_FnExternalRender
from hiero.core import FnNukeHelpersV2 as FnNukeHelpersV2
from hiero.core import log as log
from hiero.core import nuke as nuke
from hiero.exporters import FnAudioConstants as FnAudioConstants
from hiero.exporters import FnAudioHelper as FnAudioHelper
from hiero.exporters import FnEffectHelpers as FnEffectHelpers
from hiero.exporters import FnExternalRender as FnExternalRender
from hiero.exporters import FnScriptLayout as FnScriptLayout
from hiero.exporters import FnShotExporter as FnShotExporter
from hiero.exporters.FnExportUtil import TrackItemExportScriptWriter as TrackItemExportScriptWriter
from hiero.exporters.FnExportUtil import createViewerNode as createViewerNode
from hiero.exporters.FnExportUtil import trackItemTimeCodeNodeStartFrame as trackItemTimeCodeNodeStartFrame
from hiero.exporters.FnExportUtil import writeSequenceAudioWithHandles as writeSequenceAudioWithHandles
from hiero.exporters.FnReformatHelpers import reformatNodeFromPreset as reformatNodeFromPreset
from hiero.exporters.FnSubmission import Submission as Submission
import hiero as hiero

class TranscodeExporter(_hiero_exporters_FnExternalRender.NukeRenderTask):
    def __init__(self, initDict: Any) -> None:
        """Initialize"""
    def addWriteNodeToScript(self, script: Any, rootNode: Any, framerate: Any) -> None:
        """Build Write node from transcode settings and add it to the script. """
    def buildScript(self) -> None: ...
    def cleanupAudio(self) -> None: ...
    def createPresetReformatNode(self) -> Any:
        """If reformat options are selected on the preset, create a ReformatNode.  Otherwise returns None. """
    def finishTask(self) -> None: ...
    def forcedAbort(self) -> None: ...
    def includeEffects(self) -> Any:
        """Check if soft effects should be included in the export. """
    def isExportingItem(self, item: Any) -> bool:
        """Prevent duplicates when multiple multi-view track items have been included in a render """
    def makeRootNode(self, start: Any, end: Any, fps: Any) -> Any: ...
    def outputHandles(self, ignoreRetimes: bool = ...) -> tuple[int, int]:
        """Override which does nothing except changing the default value of
        ignoreRetimes from False to True.  This is not good, but the code calling
        this method is currently depending on it.
        """
    def outputRange(self, ignoreHandles: bool = ..., ignoreRetimes: bool = ..., clampToSource: bool = ...) -> tuple[Any, Any]:
        """outputRange(self)
        Returns the output file range (as tuple) for this task, if applicable
        """
    def progress(self) -> float: ...
    def setAudioExportSettings(self) -> None: ...
    def startTask(self) -> None: ...
    def taskStep(self) -> bool: ...
    def updateItem(self, originalItem: Any, localtime: Any) -> None:
        """updateItem - This is called by the processor prior to taskStart, crucially on the main thread.

        This gives the task an opportunity to modify the original item on the main thread, rather than the clone.
        """
    def validate(self) -> None: ...
    def viewsFromSource(self) -> list[str]: ...
    def writeAudio(self) -> None: ...
    def writeClipOrTrackItemToScript(self, script: Any) -> None:
        """When exporting a Clip or TrackItem, write it to a script.
        
        """
    def writeScript(self) -> None: ...
    def writeSequenceToScript(self, script: Any) -> None:
        """When exporting a Sequence, write it to a script.
        
        """

class TranscodePreset(_hiero_core_FnExporterBase.RenderTaskPreset):
    def __init__(self, name: Any, properties: Any) -> None: ...
    def deleteAudioOnFinished(self) -> bool:
        """Check whether audio should be deleted when finished. """
    def deleteAudioValid(self) -> bool:
        """Check if the delete audio option is valid for the current configuration. """
    def fileTypeSupportsAudio(self) -> bool:
        """Check if the selected file type supports audio tracks. This currently
        only works for files being written with the the mov writer.
        """
    def includeAudio(self) -> Any:
        """Check whether an audio file should be generated for the export. """
    def supportedItems(self) -> Any: ...
