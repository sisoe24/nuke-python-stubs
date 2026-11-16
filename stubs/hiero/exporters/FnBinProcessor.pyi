# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.core.FnProcessor as _hiero_core_FnProcessor
from hiero.exporters.FnEffectHelpers import ensureEffectsNodesCreated as ensureEffectsNodesCreated
import hiero as hiero

KeywordTooltips: dict
kFileBaseKeyword: str
kFileHeadKeyword: str
kFilePathKeyword: str

class BinProcessor(_hiero_core_FnProcessor.ProcessorBase):
    def __init__(self, preset: Any, submission: Any = ..., synchronous: bool = ...) -> None:
        """Initialize"""
    def preset(self) -> Any: ...
    def setPreset(self, preset: Any) -> None: ...
    def startProcessing(self, exportItems: Any, preview: bool = ...) -> list[Any]: ...

class BinProcessorPreset(_hiero_core_FnProcessor.ProcessorPreset):
    def __init__(self, name: Any, properties: Any) -> None: ...
    def addCustomResolveEntries(self, resolver: Any) -> None:
        """addDefaultResolveEntries(self, resolver)
        Create resolve entries for default resolve tokens shared by all task types.
        @param resolver : ResolveTable object
        """
