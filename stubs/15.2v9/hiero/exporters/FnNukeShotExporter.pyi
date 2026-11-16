# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.core.FnExporterBase as _hiero_core_FnExporterBase
import hiero.exporters.FnShotExporter as _hiero_exporters_FnShotExporter
from hiero.core import EffectTrackItem as EffectTrackItem
from hiero.core import FnNukeHelpersV2 as FnNukeHelpersV2
from hiero.core import Transition as Transition
from hiero.core import nuke as nuke
from hiero.core.FnEffectHelpers import FormatChange as FormatChange
from hiero.core.FnEffectHelpers import transformNodeToFormatChange as transformNodeToFormatChange
from hiero.core.FnNukeHelpers import offsetNodeAnimationFrames as offsetNodeAnimationFrames
from hiero.exporters import FnEffectHelpers as FnEffectHelpers
from hiero.exporters import FnExternalRender as FnExternalRender
from hiero.exporters import FnScriptLayout as FnScriptLayout
from hiero.exporters import FnShotExporter as FnShotExporter
from hiero.exporters.FnExportUtil import TrackItemExportScriptWriter as TrackItemExportScriptWriter
from hiero.exporters.FnExportUtil import createViewerNode as createViewerNode
from hiero.exporters.FnExportUtil import trackItemTimeCodeNodeStartFrame as trackItemTimeCodeNodeStartFrame
from hiero.exporters.FnReformatHelpers import reformatNodeFromPreset as reformatNodeFromPreset
from hiero.exporters.FnReformatHelpers import reformatSettingsFromPreset as reformatSettingsFromPreset
import hiero as hiero

class NukeShotExporter(_hiero_exporters_FnShotExporter.ShotTask):
    kCollatedSequenceFrameOffset: int
    def __init__(self, initDict: Any) -> None:
        """Initialize"""
    def finishTask(self) -> None: ...
    def includeAnnotations(self) -> Any:
        """Check if annotations are included. """
    def includeEffects(self) -> Any:
        """Check if soft effects should be included in the export. """
    def isExportingItem(self, item: Any) -> bool:
        """Check if this task is already including an item in its export.
        Used for preventing duplicates when collating shots into a single script. 
        """
    def outputRange(self, ignoreHandles: bool = ..., ignoreRetimes: bool = ..., clampToSource: bool = ...) -> tuple[Any, Any]:
        """outputRange(self)
        Returns the output file range (as tuple) for this task, if applicable
        """
    def outputRangeForCollatedSequence(self, ignoreHandles: Any) -> tuple[Any, Any]:
        """Get the output range for the collated sequence, with or without handles. """
    def outputRangeForTrackItem(self, ignoreHandles: bool = ..., ignoreRetimes: bool = ..., clampToSource: bool = ...) -> tuple[Any, Any]:
        """Get the output range for the single track item case. """
    def rootFormat(self) -> str:
        """Get the string representation of the format that should be set on the
        Root node.
        """
    def taskStep(self) -> bool: ...
    def updateItem(self, originalItem: Any, localtime: Any) -> None:
        """updateItem - This is called by the processor prior to taskStart, crucially on the main thread.

        This gives the task an opportunity to modify the original item on the main thread, rather than the copy.
        """
    def validate(self) -> None: ...
    def views(self) -> Any: ...
    def writeSequence(self, script: Any) -> None:
        """Write the collated sequence to the script. """
    def writeTrackItem(self, script: Any, firstFrame: Any) -> None:
        """Write the track item to the script. """
    def writeTrackItemCustomReadPaths(self, script: Any, firstFrame: Any) -> bool:
        """If other export items are selected as Read nodes, add those to the
        script.  This allows for e.g. using the output of the copy exporter as
        the path for the read node.

        Returns True if any read paths were set.
        """
    def writeTrackItemOriginalReadPath(self, script: Any, firstFrame: Any) -> None:
        """Write the source track item to the script. """
    def writingSequence(self) -> bool:
        """Check if we're writing a single clip or a sequence.  This is the case if the object was initialised with a sequence, or if the collate option is set. """
    def writingSequenceDisconnected(self) -> bool:
        """Check if a sequence being written should be 'disconnected', with only the master track connected to the Write node. """

class NukeSequenceExporter(NukeShotExporter):
    """Exporter for 'Process as Sequence' script export. This only exists because
    we need a distinct type to be used for this. It doesn't yet do anything.
    """
    def __init__(self, initDict: Any) -> None: ...

class NukeShotPresetBase(_hiero_core_FnExporterBase.TaskPresetBase):
    """Base class for Nuke Project File exports. This only exists because we need
    slightly different behaviour when exporting as shots or sequences, and the way
    exporters are registered requires different types to make that work.
    """
    def __init__(self, name: Any, properties: Any, task: Any) -> None:
        """Initialise presets to default values"""
    def addCustomResolveEntries(self, resolver: Any) -> None: ...
    def initDefaultProperties(self) -> None: ...
    def initialiseCallbacks(self, exportStructure: Any) -> None:
        """Reimplemented.  This preset contains paths which reference other
        elements in the export structure.  Registers callbacks which update
        those paths when they change in the UI.
        """
    def onElementPathChanged(self, oldPath: Any, newPath: Any) -> None:
        """Callback when the path for an element changes.  This updates the paths
        referencing other tasks for read/write/annotations.
        """
    def propertiesForPathCallbacks(self) -> tuple[Any, Any, Any]:
        """Get a list of properties used for path callbacks """

class NukeSequencePreset(NukeShotPresetBase):
    """Preset for 'Process as Sequence' script export. """
    def __init__(self, name: Any, properties: Any, task: Any = ...) -> None: ...
    def initDefaultProperties(self) -> None: ...
    def supportedItems(self) -> Any: ...

class NukeShotPreset(NukeShotPresetBase):
    """Preset for 'Process as Shots' script export. """
    def __init__(self, name: Any, properties: Any, task: Any = ...) -> None: ...
    def initDefaultProperties(self) -> None: ...
    def supportedItems(self) -> Any: ...
