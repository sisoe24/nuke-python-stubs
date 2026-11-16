# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import hiero.core as _hiero_core
from hiero.core import FnFloatRange as FnFloatRange
from hiero.core import Format as Format
from hiero.core import IExporterRegistry as IExporterRegistry
from hiero.core import isIndie as isIndie
from hiero.core import isNC as isNC
from hiero.core import log as log
from hiero.core import project as project
from hiero.core import util as util
from hiero.core.FnExporterBase import FolderTask as FolderTask
from hiero.core.FnExporterBase import FolderTaskPreset as FolderTaskPreset
from hiero.core.FnExporterBase import TaskBase as TaskBase
from hiero.core.FnExporterBase import TaskPresetBase as TaskPresetBase
from hiero.core.FnExporterBase import classBasename as classBasename

taskRegistry: TaskRegistry

class ExportHistory:
    def __init__(self, presets: Any = ...) -> None: ...
    def addPreset(self, preset: Any) -> str: ...
    def findPreset(self, presetId: Any) -> None: ...
    def presets(self) -> Any: ...

class TaskRegistry(_hiero_core.IExporterRegistry):
    def __init__(self) -> None: ...
    def addDefaultPresets(self, overwrite: bool = ...) -> None: ...
    def addPresetToProjectExportHistory(self, project: Any, preset: Any) -> str:
        """Add a preset to the export history for a project. """
    def addProcessorPreset(self, name: Any, preset: Any) -> None:
        """Register Processor Preset Instance"""
    def addSubmission(self, name: Any, submissionClass: Any) -> None: ...
    def assignPresetToProject(self, preset: Any, project: Any) -> None:
        """Assign preset to project and ensure name is unique within project. Project may be None in which case preset will be assigned 'local'"""
    def copyAndAddProcessorPreset(self, preset: Any) -> None: ...
    def copyAndAddProjectPreset(self, preset: Any, project: Any) -> None:
        """Duplicate a preset and assign it to a project imediately to prevent name clashes"""
    def copyPreset(self, preset: Any) -> None:
        """Create a copy of a preset.  The copy is not added to the registry. """
    def createAndAddProcessorPreset(self, name: Any, typeTemplate: Any) -> Any: ...
    def createAndExecuteProcessor(self, preset: Any, items: Any, submissionName: Any = ..., synchronous: bool = ...) -> None:
        """Instantiate the Processor associated with preset and startProcessing items"""
    def createProcessor(self, preset: Any, submissionName: Any = ..., synchronous: bool = ...) -> Any:
        """Create the processor for an export and return it. This doesn't start
        the export.
        """
    def createTaskFromPreset(self, preset: Any, initDictionary: Any) -> None: ...
    def discardPresetChanges(self, project: Any) -> None: ...
    def findPresetInProjectExportHistory(self, project: Any, presetId: Any) -> None:
        """Attempt to find a preset in a project's export history. """
    def getPresetId(self, preset: Any) -> str:
        """Get the id (hash) of the given preset. """
    def getPresetType(self, ident: Any) -> None: ...
    def getProcessor(self, index: Any) -> Any: ...
    def getProcessorFromPreset(self, presetName: Any) -> Any: ...
    def getProcessorPreset(self, index: Any) -> Any: ...
    def isNukeShotExportPreset(self, preset: Any) -> bool:
        """Check if a preset is valid for Nuke shot export.  To be considered valid, the preset must contain
        a NukeShotExporter and a NukeRenderTask (write node). 
        """
    def isSingleSocketAllowed(self) -> bool:
        """Return whether or not single socket exports are allowed. """
    def loadPresets(self, path: Any) -> bool:
        """Load all xml presets within specified path and register"""
    def localPresets(self) -> list[Any]:
        """Returns a list of preset names NOT associated with the specified project"""
    def localPresetsChanged(self) -> bool:
        """Check if the local task presets have changed since startPresetChanges() was called. """
    def nukeShotExportPresets(self, project: Any) -> list[Any]:
        """Get a list of presets which can export shots as Nuke scripts.
        Includes local presets and those in the project. 
        """
    def numProcessorPresets(self) -> int:
        """Return the total number of Processor preset instances registered"""
    def numProcessors(self) -> int:
        """Return the number or processors in the Registry"""
    def numTasks(self) -> int:
        """Returns the number of Tasks Registered"""
    def presetFromXml(self, xml: Any, register: bool = ...) -> None:
        """Deserialize preset from xml string.
        Requires derived TaskPreset classes to be registered.
        """
    def presetToXml(self, preset: Any) -> str:
        """Serialise a TaskPreset to XML and return as string.
        Returns an empty string on failure.
        """
    def presetTypeFromIdent(self, ident: Any) -> None:
        """Resolve preset ident string to Preset class type"""
    def presetsSubDirectory(self) -> str: ...
    def processorByIndex(self, index: Any) -> Any:
        """Returns a processor by index"""
    def processorFromPreset(self, presetName: Any) -> Any:
        """Return type of task from preset name"""
    def processorName(self, index: Any) -> Any:
        """Returns a Processor name by index"""
    def processorPresetByIndex(self, index: Any) -> Any:
        """Return instance of TaskPreset Object"""
    def processorPresetByName(self, name: Any, project: Any = ...) -> None:
        """Returns the preset with specified name associated with project. If project is None preset will be searched for in local presets"""
    def processorPresetName(self, index: Any) -> Any:
        """Return the name of Processor preset by index"""
    def processorPresetNames(self) -> list[Any]:
        """Returns a tuple of Processor Preset names"""
    def projectDuplicated(self, project: Any, newProject: Any) -> None:
        """Called on project clone to duplicate the associated project presets"""
    def projectExportHistoryXml(self, project: Any) -> list[str] | list[Any]:
        """Get the project export history as a list of xml fragments. Use the xml to avoid problems with reference
        counting the preset objects when calling from C++. 
        """
    def projectPresets(self, project: Any) -> list[Any]:
        """Returns a list of preset names associated with the specified project"""
    def projectPresetsChanged(self, project: Any) -> bool:
        """Check if the task presets for the given project have changed since startPresetChanges(project) was called. """
    def projectUnloaded(self, project: Any) -> None:
        """Called on project unload to remove presets associated with project"""
    def registerPreset(self, parentType: Any, preset: Any) -> None:
        """Register a preset instance and association with parentType"""
    def registerProcessor(self, preset: Any, processor: Any) -> None:
        """Register the association between a Processor and ProcessorPreset"""
    def registerTask(self, preset: Any, task: Any) -> None:
        """Register the association between a Task and TaskPreset"""
    def removeProcessorPreset(self, preset: Any) -> None:
        """Remove Processor preset from registry"""
    def renameProcessorPreset(self, preset: Any, newName: Any) -> None:
        """Validate and update name of Processor Preset"""
    def restoreProjectExportHistoryXml(self, project: Any, presetsXml: Any) -> None:
        """Set the project export history as a list of xml fragments. Use the xml to avoid problems with reference
        counting the preset objects when calling from C++. 
        """
    def revertDefaultPresets(self) -> None: ...
    def savePresets(self, path: Any) -> bool:
        """Save all registered presets, as xml, to path specified. """
    def setDefaultPresets(self, defaultPresets: Any) -> None: ...
    def startPresetChanges(self, project: Any) -> None: ...
    def submissionByName(self, name: Any) -> None: ...
    def submissionChanged(self, submissionName: Any) -> None: ...
    def submissionNames(self) -> list[Any]: ...
    def taskName(self, index: Any) -> Any:
        """Returns a Task name by Index"""
    def validateExport(self, preset: Any, items: Any) -> str:
        """Implements IExporterRegistry.validateExport """
