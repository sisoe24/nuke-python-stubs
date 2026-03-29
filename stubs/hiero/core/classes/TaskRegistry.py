"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import ui
import core
import nuke
import hiero
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class TaskRegistry(IExporterRegistry):
    """
    IExporterRegistry provides a simple interface for our C++ Application to access python instance of hiero.core.TaskRegistry.

    This class should not be used directly; use hiero.core.TaskRegistry instead.
    """

    def __init__(self) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def registerTask(self, preset: TaskPreset, task: Task) -> None:
        """
        Register the association between a Task and TaskPreset
        """
        ...

    def registerProcessor(self, preset: ProcessorPreset, processor: Processor) -> None:
        """
        Register the association between a Processor and ProcessorPreset
        """
        ...

    def registerPreset(self, parentType: type, preset: TaskPreset) -> None:
        """
        Register a preset instance and association with parentType
        """
        ...

    def projectUnloaded(self, project: Project) -> None:
        """
        Called on project unload to remove presets associated with project
        """
        ...

    def projectDuplicated(self, project: Project, newProject: Project) -> None:
        """
        Called on project clone to duplicate the associated project presets
        """
        ...

    def loadPresets(self, path: str) -> None:
        """
        Load all xml presets within specified path and register
        """
        ...

    def _loadPresets(self, path, list) -> None:
        """

        """
        ...

    def presetFromXml(self, xml: str, register: bool = True) -> TaskPreset:
        """
        Deserialize preset from xml string.
        Requires derived TaskPreset classes to be registered.
        """
        ...

    def _loadPresetElement(self, element) -> None:
        """

        """
        ...

    def savePresets(self, path: str) -> None:
        """
        Save all registered presets, as xml, to path specified.
        """
        ...

    def _savePresets(self, path, presetlist, dictionary) -> None:
        """

        """
        ...

    def presetToXml(self, preset: TaskPreset) -> str:
        """
        Serialise a TaskPreset to XML and return as string.
        Returns an empty string on failure.
        """
        ...

    def _presetToXml(self, preset: TaskPreset) -> object:
        """
        Serialize a preset to XML and return the root element. Throws on failure.
        """
        ...

    def _savePresetElement(self, key: str, value: object, parent: object) -> None:
        """
        Save a preset key/value as an XML element and append it to the parent.  Called recursively for containers.
        """
        ...

    def presetsSubDirectory(self) -> str:
        """
        self.presetsSubDirectory() -> Get the sub-directory in the plugin paths to search for presets.
        """
        ...

    def revertDefaultPresets(self, path: str) -> None:
        """
        self.revertDefaultPresets(string) -> Called by the C++ application reconstruct the default presets.

        @param: path as string
        """
        ...

    def setDefaultPresets(self, defaultPresets) -> None:
        """

        """
        ...

    def addDefaultPresets(self, overwrite=False) -> None:
        """

        """
        ...

    def startPresetChanges(self, project: Project) -> None:
        """
        self.startPresetChanges(hiero.core.Project) -> Called when the user might start editing the presets, so the changes can be reverted if necessary.

        @param: hiero.core.Project)
        """
        ...

    def discardPresetChanges(self, project: Project) -> None:
        """
        self.startPresetChanges(hiero.core.Project) -> Discard any changes to the presets since startPresetChanges() was called.

        @param: hiero.core.Project)
        """
        ...

    def createAndAddProcessorPreset(self, name: str, typeTemplate: TaskPreset) -> TaskPreset:
        """
        self.createAndAddProcessorPreset(string, hiero.core.TaskPreset) -> Called by the C++ application to create a new preset, using typetemplate as a template.

        @param: string - Preset name
        @return: hiero.core.TaskPreset instance as type template
        """
        ...

    def copyPreset(self, preset: TaskPreset) -> None:
        """
        Create a copy of a preset.  The copy is not added to the registry.
        """
        ...

    def copyAndAddProcessorPreset(self, preset: TaskPreset) -> TaskPreset:
        """
        self.copyAndAddProcessorPreset() -> Called by the C++ application to duplicate a preset.

        @param: hiero.core.TaskPreset instance for duplication
        @return: new hiero.core.TaskPreset instance
        """
        ...

    def copyAndAddProjectPreset(self, preset: TaskPreset, project: Project) -> None:
        """
        Duplicate a preset and assign it to a project imediately to prevent name clashes
        """
        ...

    def addProcessorPreset(self, name: str, preset: ProcessorPreset) -> None:
        """
        Register Processor Preset Instance
        """
        ...

    def removeProcessorPreset(self, preset: ProcessorPreset) -> None:
        """
        Remove Processor preset from registry
        """
        ...

    def renameProcessorPreset(self, preset: ProcessorPreset, newName: str) -> None:
        """
        Validate and update name of Processor Preset
        """
        ...

    def assignPresetToProject(self, preset: TaskPreset, project: Project | None) -> None:
        """
        Assign preset to project and ensure name is unique within project. Project may be None in which case preset will be assigned 'local'
        """
        ...

    def numProcessorPresets(self) -> int:
        """
        Return the total number of Processor preset instances registered
        """
        ...

    def processorPresetName(self, index: int) -> str:
        """
        Return the name of Processor preset by index
        """
        ...

    def numTasks(self) -> int:
        """
        Returns the number of Tasks Registered
        """
        ...

    def numProcessors(self) -> int:
        """
        Return the number or processors in the Registry
        """
        ...

    def taskName(self, index: int) -> str:
        """
        Returns a Task name by Index
        """
        ...

    def processorName(self, index: int) -> str:
        """
        Returns a Processor name by index
        """
        ...

    def processorPresetNames(self) -> tuple[str, ...]:
        """
        Returns a tuple of Processor Preset names
        """
        ...

    def processorPresetByName(self, name: str, project: Project | None = None) -> TaskPreset | None:
        """
        Returns the preset with specified name associated with project. If project is None preset will be searched for in local presets
        """
        ...

    def _getPresetsFromList(self, presetsList: list[TaskPreset], projectToFilter: Project | None) -> list[str]:
        """
        Returns a list of presets name associated with 'projectToFilter' from the specified 'presetsList'
        """
        ...

    def projectPresets(self, project: Project) -> list[str]:
        """
        Returns a list of preset names associated with the specified project
        """
        ...

    def localPresets(self) -> list[str]:
        """
        Returns a list of preset names NOT associated with the specified project
        """
        ...

    def projectExportHistoryXml(self, project: Project) -> list[str]:
        """
        Get the project export history as a list of xml fragments. Use the xml to avoid problems with reference
        counting the preset objects when calling from C++.
        """
        ...

    def restoreProjectExportHistoryXml(self, project: Project, presetsXml: list[str]) -> None:
        """
        Set the project export history as a list of xml fragments. Use the xml to avoid problems with reference
        counting the preset objects when calling from C++.
        """
        ...

    def addPresetToProjectExportHistory(self, project: Project, preset: TaskPreset) -> None:
        """
        Add a preset to the export history for a project.
        """
        ...

    def findPresetInProjectExportHistory(self, project: Project, presetId: int) -> TaskPreset | None:
        """
        Attempt to find a preset in a project's export history.
        """
        ...

    def _computePresetsHash(self, presets) -> None:
        """

        """
        ...

    def getPresetId(self, preset: TaskPreset) -> int:
        """
        Get the id (hash) of the given preset.
        """
        ...

    def localPresetsChanged(self) -> bool:
        """
        Check if the local task presets have changed since startPresetChanges() was called.
        """
        ...

    def projectPresetsChanged(self, project: Project) -> bool:
        """
        Check if the task presets for the given project have changed since startPresetChanges(project) was called.
        """
        ...

    def getProcessor(self, index) -> None:
        """

        """
        ...

    def processorByIndex(self, index: int) -> Processor:
        """
        Returns a processor by index
        """
        ...

    def getPresetType(self, ident) -> None:
        """

        """
        ...

    def presetTypeFromIdent(self, ident: str) -> type:
        """
        Resolve preset ident string to Preset class type
        """
        ...

    def createTaskFromPreset(self, preset, initDictionary) -> None:
        """

        """
        ...

    def getProcessorFromPreset(self, presetName) -> None:
        """

        """
        ...

    def processorFromPreset(self, presetName: str) -> Processor:
        """
        Return type of task from preset name
        """
        ...

    def _checkPresetToFormat(self, presetName: str, exportTemplate: object) -> None:
        """
        Checks if 'exportTemplate' defines a specific output format and if its
        valid by creating a hiero.core.Format.
        Raises a ValueError exception if a format is not valid.
        """
        ...

    def _getToScaleFromPreset(self, exportTemplate: object) -> list[str]:
        """
        Returns a list of scale options defined in 'exportTemplate'

        """
        ...

    def _checkToScaleForSequence(self, presetName: str, toScaleOptions: list[str], itemName: str, seqFormat: object) -> None:
        """
        Checks if the output format for a specific sequence/clip is valid when
        scalled with th 'scale' option defined in the exportTemplate preset.
        Raises a ValueError exception if a format is not valid.
        """
        ...

    def _checkOutputResolution(self, preset: TaskPreset, items: list[object]) -> None:
        """
        Checks if the output resolution defined in the preset or defined by the
        items to be exported are valid for PLE / Indie variants.
        Raises a ValueError exception if a format is not valid.
        """
        ...

    def validateExport(self, preset: TaskPreset, items: list[object]) -> None:
        """
        Implements IExporterRegistry.validateExport
        """
        ...

    def createProcessor(self, preset: 'TaskPreset', submissionName: str | None = None, synchronous: bool = False) -> 'Processor':
        """
        Create the processor for an export and return it. This doesn't start
        the export.
        """
        ...

    def createAndExecuteProcessor(self, preset: 'TaskPreset', items: list, submissionName: str | None = None, synchronous: bool = False) -> 'Processor':
        """
        Instantiate the Processor associated with preset and startProcessing items
        """
        ...

    def getProcessorPreset(self, index) -> None:
        """

        """
        ...

    def processorPresetByIndex(self, index: int) -> 'TaskPreset':
        """
        Return instance of TaskPreset Object
        """
        ...

    def submissionNames(self) -> list[str]:
        """
        self.submissionNames() -> Called by the C++ application to get a list of the available Submission objects. Submission objects are used to manage render farm renders.

        @return: list of name strings
        """
        ...

    def submissionByName(self, name) -> None:
        """

        """
        ...

    def addSubmission(self, name, submissionClass) -> None:
        """

        """
        ...

    def submissionChanged(self, submissionName: str) -> None:
        """
        self.submissionChanged(string, hiero.core.Project) -> Called by the C++ application when the submission choice changes in the Export Dialog.

        @param: submission name as a string
        """
        ...

    def isNukeShotExportPreset(self, preset: 'TaskPreset') -> bool:
        """
        Check if a preset is valid for Nuke shot export.  To be considered valid, the preset must contain
        a NukeShotExporter and a NukeRenderTask (write node).
        """
        ...

    def nukeShotExportPresets(self, project: 'Project') -> list['TaskPreset']:
        """
        Get a list of presets which can export shots as Nuke scripts.
        Includes local presets and those in the project.
        """
        ...

    def isSingleSocketAllowed(self) -> bool:
        """
        Return whether or not single socket exports are allowed.
        """
        ...
