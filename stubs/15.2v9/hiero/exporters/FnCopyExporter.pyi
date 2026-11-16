# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.core.FnExporterBase as _hiero_core_FnExporterBase
import hiero.exporters.FnFrameExporter as _hiero_exporters_FnFrameExporter
from hiero.core import util as util
from hiero.exporters import FnFrameExporter as FnFrameExporter
import hiero as hiero

class CopyExporter(_hiero_exporters_FnFrameExporter.FrameExporter):
    def __init__(self, initDict: Any) -> None:
        """Initialize"""
    def doFrame(self, src: Any, dst: Any) -> None: ...

class CopyPreset(_hiero_core_FnExporterBase.TaskPresetBase):
    def __init__(self, name: Any, properties: Any) -> None: ...
    def supportedItems(self) -> Any: ...
