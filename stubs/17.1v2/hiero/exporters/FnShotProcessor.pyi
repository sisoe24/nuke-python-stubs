# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import hiero.core.FnProcessor as _hiero_core_FnProcessor
from hiero.core import FnExporterBase as FnExporterBase
from hiero.core.FnVersionScanner import VersionScanner as VersionScanner
from hiero.exporters.FnEffectHelpers import ensureEffectsNodesCreated as ensureEffectsNodesCreated
import hiero as hiero

KeywordTooltips: dict
kFileBaseKeyword: str
kFileHeadKeyword: str
kFilePathKeyword: str

class ShotProcessor(_hiero_core_FnProcessor.ProcessorBase):
    kStartFrameCustom: str
    kStartFrameSource: str
    def __init__(self, preset: Any, submission: Any = ..., synchronous: bool = ...) -> None:
        """Initialize"""
    def offlineTrackItems(self, track: Any) -> list[Any]: ...
    def preset(self) -> Any: ...
    def setPreset(self, preset: Any) -> None: ...
    def startProcessing(self, exportItems: Any, preview: bool = ...) -> Any: ...

class ShotProcessorPreset(_hiero_core_FnProcessor.ProcessorPreset):
    def __init__(self, name: Any, properties: Any) -> None: ...
    def addCustomResolveEntries(self, resolver: Any) -> None:
        """addDefaultResolveEntries(self, resolver)
        Create resolve entries for default resolve tokens shared by all task types.
        @param resolver : ResolveTable object
        """
    def isValid(self) -> tuple[bool, str]: ...

def buildTagsData(exportItems: Any) -> list[tuple[Any, Any]]: ...

def findTrackItemExportTag(preset: Any, item: Any) -> None:
    """Find a tag from a previous export. """

def getShotNameIndex(trackItem: Any) -> str:
    """Get the name index string for a track item.  This counts other items on the sequence
    with the same name and returns a string in the form '_{index}'.
    If this is the first item, or there are no others with the same name, returns an empty string. 
    """
