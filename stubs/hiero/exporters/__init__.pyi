# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.core.FnExportRegistry as _hiero_core_FnExportRegistry
import nuke as _nuke
from . import FnAdditionalNodesDialog as FnAdditionalNodesDialog
from . import FnAudioConstants as FnAudioConstants
from . import FnAudioExportTask as FnAudioExportTask
from . import FnAudioExportUI as FnAudioExportUI
from . import FnAudioHelper as FnAudioHelper
from . import FnBinProcessor as FnBinProcessor
from . import FnBinProcessorUI as FnBinProcessorUI
from . import FnCompRenderTask as FnCompRenderTask
from . import FnCopyExporter as FnCopyExporter
from . import FnCopyExporterUI as FnCopyExporterUI
from . import FnEDLExportTask as FnEDLExportTask
from . import FnEDLExportUI as FnEDLExportUI
from . import FnEffectHelpers as FnEffectHelpers
from . import FnExportKeywords as FnExportKeywords
from . import FnExportUtil as FnExportUtil
from . import FnExternalRender as FnExternalRender
from . import FnExternalRenderUI as FnExternalRenderUI
from . import FnFrameExporter as FnFrameExporter
from . import FnFrameServerRender as FnFrameServerRender
from . import FnLocalNukeRender as FnLocalNukeRender
from . import FnNukeAnnotationsExporter as FnNukeAnnotationsExporter
from . import FnNukeAnnotationsExporterUI as FnNukeAnnotationsExporterUI
from . import FnNukeExporterWidgets as FnNukeExporterWidgets
from . import FnNukeShotExporter as FnNukeShotExporter
from . import FnNukeShotExporterUI as FnNukeShotExporterUI
from . import FnOTIOExportTask as FnOTIOExportTask
from . import FnOTIOExportUI as FnOTIOExportUI
from . import FnReformatHelpers as FnReformatHelpers
from . import FnScriptLayout as FnScriptLayout
from . import FnShotExporter as FnShotExporter
from . import FnShotProcessor as FnShotProcessor
from . import FnShotProcessorUI as FnShotProcessorUI
from . import FnSubmission as FnSubmission
from . import FnSymLinkExporter as FnSymLinkExporter
from . import FnSymLinkExporterUI as FnSymLinkExporterUI
from . import FnTimelineProcessor as FnTimelineProcessor
from . import FnTimelineProcessorUI as FnTimelineProcessorUI
from . import FnTrackSelectionWidget as FnTrackSelectionWidget
from . import FnTranscodeExporter as FnTranscodeExporter
from . import FnTranscodeExporterUI as FnTranscodeExporterUI
from . import FnXMLExportTask as FnXMLExportTask
from . import FnXMLExportUI as FnXMLExportUI
from hiero.exporters.FnSubmission import Submission as Submission
import hiero as hiero

nukeEnv: _nuke.GlobalsEnvironment
registry: _hiero_core_FnExportRegistry.TaskRegistry

def AddDefaultPresets(overwrite: Any) -> None:
    """Configure the default export presets.  If overwrite is true, this will
    replace the existing presets. 
    """

def GetDefaultMovTranscodePresets() -> dict[Any, Any]:
    """Generate a dict of presets for the default mov transcode presets.
    These will be populated with all the default values for the encoder properties.
    """

def GetDefaultMxfPreset() -> dict[Any, Any]: ...

def MakeExportProcessorTemplate(processorPreset: Any, path: Any, transcodePreset: Any) -> tuple[Any, dict[str, tuple[tuple[Any, Any]]]]:
    """Make a template for a processor preset, path, and transcode preset. """

def MakeTranscodePreset(file_type: Any, properties: Any) -> Any:
    """Make a transcode preset for a given file type and
    codec properties dictionary.
    """
