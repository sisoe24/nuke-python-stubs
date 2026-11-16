# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import hiero.core.FnExportRegistry as _hiero_core_FnExportRegistry
import hiero.core.FnExporterBase as _hiero_core_FnExporterBase
from hiero.core import Clip as Clip
from hiero.core import Sequence as Sequence
from hiero.core import TrackItem as TrackItem
from hiero.core.FnExporterBase import TaskBase as TaskBase
from hiero.core.FnExporterBase import TaskPresetBase as TaskPresetBase
from hiero.exporters import FnAudioConstants as FnAudioConstants
from hiero.exporters import FnAudioHelper as FnAudioHelper
from hiero.exporters.FnExportUtil import writeSequenceAudioWithHandles as writeSequenceAudioWithHandles

taskRegistry: _hiero_core_FnExportRegistry.TaskRegistry

class AudioExportPreset(_hiero_core_FnExporterBase.TaskPresetBase):
    def __init__(self, name: Any, properties: Any) -> None: ...
    def supportedItems(self) -> Any: ...

class AudioExportTask(_hiero_core_FnExporterBase.TaskBase):
    def __init__(self, initDict: Any) -> None:
        """Initialize"""
    def sequenceInOutPoints(self, sequence: Any, indefault: Any, outdefault: Any) -> tuple[Any, Any]:
        """Return tuple (start, end) of in/out points. If either in/out is not set, return in/outdefault in its place."""
    def setExportSettings(self) -> None: ...
    def startTask(self) -> None: ...
    def taskStep(self) -> bool: ...
