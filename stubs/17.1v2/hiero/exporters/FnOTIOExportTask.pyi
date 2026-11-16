# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import hiero.core.FnExporterBase as _hiero_core_FnExporterBase
from hiero.core.FnCompSourceInfo import CompSourceInfo as CompSourceInfo
from hiero.core.FnEffectHelpers import reformatStateToDict as reformatStateToDict
from hiero.exporters.FnExportUtil import OutputTransformKnobs as OutputTransformKnobs
import hiero as hiero

kOtioMarkerColorMappedToHieroTagIcons: dict

class OTIOExportPreset(_hiero_core_FnExporterBase.TaskPresetBase):
    """Export preset for OTIO file export """
    def __init__(self, name: Any, properties: Any) -> None: ...
    def addCustomResolveEntries(self, resolver: Any) -> None: ...
    def exportsAllTracks(self) -> bool: ...
    def supportedItems(self) -> Any: ...
    def supportsAudio(self) -> bool: ...

class OTIOExportTask(_hiero_core_FnExporterBase.TaskBase):
    """Export task for exporting a Sequence as an OTIO file """
    def __init__(self, initDict: Any) -> None: ...
    def finishTask(self) -> None: ...
    def startTask(self) -> Any: ...
    def taskStep(self) -> bool: ...

class OTIOTimelineBuilder:
    """Helper class for creating an otio.schema.Timeline from a hiero.core.Sequence
    object.
    """
    kHieroTagIconsMappedToOtioMarkerColor: dict
    kKnobsToExclude: list
    def __init__(self, hieroSequence: Any, writeCompRenderPaths: Any, includeEffects: Any) -> None: ...
    def buildTimeline(self) -> Any:
        """Create the timeline """
    def warnings(self) -> list[Any]:
        """Get the list of warnings from building the timeline """
