# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import hiero.core.FnProcessor as _hiero_core_FnProcessor
from hiero.exporters.FnCompRenderTask import createCompRenderTasks as createCompRenderTasks
from hiero.exporters.FnEffectHelpers import ensureEffectsNodesCreated as ensureEffectsNodesCreated
import hiero as hiero

class TimelineProcessor(_hiero_core_FnProcessor.ProcessorBase):
    def __init__(self, preset: Any, submission: Any = ..., synchronous: bool = ...) -> None:
        """Initialize"""
    def createSequenceCopy(self, sequence: Any, excludedTracks: Any, preview: Any, itemFilter: Any = ...) -> Any:
        """Create a copy of a sequence, not including any tracks which are in the
        excluded list, and filtering track items with the itemFilter function if
        given.
        """
    def exportSequenceForSequence(self, sequence: Any, excludedTracks: Any, preview: Any) -> tuple[Any, Any, Any]:
        """Create a copy of the sequence and remove any excluded tracks from it
        Return a tuple of the sequence, the copy, and the project name
        """
    def exportSequenceForTrackItem(self, trackItem: Any, exportItems: Any, excludedTracks: Any, preview: Any) -> tuple[Any, Any, Any]:
        """Create a copy of the track item's sequence, removing any excluded
        tracks or unselected items from it.
        Return a tuple of the sequence, the copy, and the project
        """
    def preset(self) -> Any: ...
    def sequenceRange(self, sequence: Any) -> tuple[Any, Any]: ...
    def setPreset(self, preset: Any) -> None: ...
    def startFrameOffset(self) -> int:
        """If the export start frame is set to 'Custom', return the custom value.
        Otherwise returns 0.
        """
    def startProcessing(self, exportItems: Any, preview: bool = ...) -> list[Any]: ...

class TimelineProcessorPreset(_hiero_core_FnProcessor.ProcessorPreset):
    def __init__(self, name: Any, properties: Any) -> None: ...
    def addCustomResolveEntries(self, resolver: Any) -> None:
        """addDefaultResolveEntries(self, resolver)
        Create resolve entries for default resolve tokens shared by all task types.
        @param resolver : ResolveTable object
        """
