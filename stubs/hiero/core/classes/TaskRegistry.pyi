import typing
from typing import *
from numbers import Number

import ui
import core
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

    def registerTask(self, preset, task) -> None:
        """
        Register the association between a Task and TaskPreset
        """
        ...

    def registerProcessor(self, preset, processor) -> None:
        """
        Register the association between a Processor and ProcessorPreset
        """
        ...

    def registerPreset(self, parentType, preset) -> None:
        """
        Register a preset instance and association with parentType
        """
        ...

    def projectUnloaded(self, project) -> None:
        """
        Called on project unload to remove presets associated with project
        """
        ...

    def projectDuplicated(self, project, newProject) -> None:
        """
        Called on project clone to duplicate the associated project presets
        """
        ...

    def loadPresets(self, path) -> None:
        """
        Load all xml presets within specified path and register
        """
        ...

    def _loadPresets(self, path, list) -> None:
        """

        """
        ...

    def presetFromXml(self, xml, register=True) -> None:
        """
        Deserialize preset from xml string.
        Requires derived TaskPreset classes to be registered.
        """
        ...

    def _loadPresetElement(self, element) -> None:
        """

        """
        ...

    def savePresets(self, path) -> None:
        """
        Save all registered presets, as xml, to path specified.
        """
        ...

    def _savePresets(self, path, presetlist, dictionary) -> None:
        """

        """
        ...

    def presetToXml(self, preset) -> None:
        """
        Serialise a TaskPreset to XML and return as string.
        Returns an empty string on failure.
        """
        ...

    def _presetToXml(self, preset) -> None:
        """
        Serialize a preset to XML and return the root element. Throws on failure.
        """
        ...

    def _savePresetElement(self, key, value, parent) -> None:
        """
        Save a preset key/value as an XML element and append it to the parent.  Called recursively for containers.
        """
        ...

    def presetsSubDirectory(self) -> None:
        """
        self.presetsSubDirectory() -> Get the sub-directory in the plugin paths to search for presets.
        """
        ...

    def revertDefaultPresets(self) -> None:
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

    def startPresetChanges(self, project) -> None:
        """
        self.startPresetChanges(hiero.core.Project) -> Called when the user might start editing the presets, so the changes can be reverted if necessary.

        @param: hiero.core.Project)
        """
        ...

    def discardPresetChanges(self, project) -> None:
        """
        self.startPresetChanges(hiero.core.Project) -> Discard any changes to the presets since startPresetChanges() was called.

        @param: hiero.core.Project)
        """
        ...

    def createAndAddProcessorPreset(self, name, typeTemplate) -> TaskPreset:
        """
        self.createAndAddProcessorPreset(string, hiero.core.TaskPreset) -> Called by the C++ application to create a new preset, using typetemplate as a template.

        @param: string - Preset name
        @return: hiero.core.TaskPreset instance as type template
        """
        ...

    def copyPreset(self, preset) -> None:
        """
        Create a copy of a preset.  The copy is not added to the registry.
        """
        ...

    def copyAndAddProcessorPreset(self, preset) -> TaskPreset:
        """
        self.copyAndAddProcessorPreset() -> Called by the C++ application to duplicate a preset.

        @param: hiero.core.TaskPreset instance for duplication
        @return: new hiero.core.TaskPreset instance
        """
        ...

    def copyAndAddProjectPreset(self, preset, project) -> None:
        """
        Duplicate a preset and assign it to a project imediately to prevent name clashes
        """
        ...

    def addProcessorPreset(self, name, preset) -> None:
        """
        Register Processor Preset Instance
        """
        ...

    def removeProcessorPreset(self, preset) -> None:
        """
        Remove Processor preset from registry
        """
        ...

    def renameProcessorPreset(self, preset, newName) -> None:
        """
        Validate and update name of Processor Preset
        """
        ...

    def assignPresetToProject(self, preset, project) -> None:
        """
        Assign preset to project and ensure name is unique within project. Project may be None in which case preset will be assigned 'local'
        """
        ...

    def numProcessorPresets(self) -> None:
        """
        Return the total number of Processor preset instances registered
        """
        ...

    def processorPresetName(self, index) -> None:
        """
        Return the name of Processor preset by index
        """
        ...

    def numTasks(self) -> None:
        """
        Returns the number of Tasks Registered
        """
        ...

    def numProcessors(self) -> None:
        """
        Return the number or processors in the Registry
        """
        ...

    def taskName(self, index) -> None:
        """
        Returns a Task name by Index
        """
        ...

    def processorName(self, index) -> None:
        """
        Returns a Processor name by index
        """
        ...

    def processorPresetNames(self) -> None:
        """
        Returns a tuple of Processor Preset names
        """
        ...

    def processorPresetByName(self, name, project=None) -> None:
        """
        Returns the preset with specified name associated with project. If project is None preset will be searched for in local presets
        """
        ...

    def _getPresetsFromList(self, presetsList, projectToFilter) -> None:
        """
        Returns a list of presets name associated with 'projectToFilter' from the specified 'presetsList'
        """
        ...

    def projectPresets(self, project) -> None:
        """
        Returns a list of preset names associated with the specified project
        """
        ...

    def localPresets(self) -> None:
        """
        Returns a list of preset names NOT associated with the specified project
        """
        ...

    def projectExportHistoryXml(self, project) -> None:
        """
        Get the project export history as a list of xml fragments. Use the xml to avoid problems with reference
        counting the preset objects when calling from C++.
        """
        ...

    def restoreProjectExportHistoryXml(self, project, presetsXml) -> None:
        """
        Set the project export history as a list of xml fragments. Use the xml to avoid problems with reference
        counting the preset objects when calling from C++.
        """
        ...

    def addPresetToProjectExportHistory(self, project, preset) -> None:
        """
        Add a preset to the export history for a project.
        """
        ...

    def findPresetInProjectExportHistory(self, project, presetId) -> None:
        """
        Attempt to find a preset in a project's export history.
        """
        ...

    def _computePresetsHash(self, presets) -> None:
        """

        """
        ...

    def getPresetId(self, preset) -> None:
        """
        Get the id (hash) of the given preset.
        """
        ...

    def localPresetsChanged(self) -> None:
        """
        Check if the local task presets have changed since startPresetChanges() was called.
        """
        ...

    def projectPresetsChanged(self, project) -> None:
        """
        Check if the task presets for the given project have changed since startPresetChanges(project) was called.
        """
        ...

    def getProcessor(self, index) -> None:
        """

        """
        ...

    def processorByIndex(self, index) -> None:
        """
        Returns a processor by index
        """
        ...

    def getPresetType(self, ident) -> None:
        """

        """
        ...

    def presetTypeFromIdent(self, ident) -> None:
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

    def processorFromPreset(self, presetName) -> None:
        """
        Return type of task from preset name
        """
        ...

    def _checkPresetToFormat(self, presetName, exportTemplate) -> None:
        """
        Checks if 'exportTemplate' defines a specific output format and if its
        valid by creating a hiero.core.Format.
        Raises a ValueError exception if a format is not valid.
        """
        ...

    def _getToScaleFromPreset(self, exportTemplate) -> None:
        """
        Returns a list of scale options defined in 'exportTemplate'

        """
        ...

    def _checkToScaleForSequence(self, presetName, toScaleOptions, itemName, seqFormat) -> None:
        """
        Checks if the output format for a specific sequence/clip is valid when
        scalled with th 'scale' option defined in the exportTemplate preset.
        Raises a ValueError exception if a format is not valid.
        """
        ...

    def _checkOutputResolution(self, preset, items) -> None:
        """
        Checks if the output resolution defined in the preset or defined by the
        items to be exported are valid for PLE / Indie variants.
        Raises a ValueError exception if a format is not valid.
        """
        ...

    def validateExport(self, preset, items) -> None:
        """
        Implements IExporterRegistry.validateExport
        """
        ...

    def createProcessor(self, preset, submissionName=None, synchronous=False) -> None:
        """
        Create the processor for an export and return it. This doesn't start
        the export.
        """
        ...

    def createAndExecuteProcessor(self, preset, items, submissionName=None, synchronous=False) -> None:
        """
        Instantiate the Processor associated with preset and startProcessing items
        """
        ...

    def getProcessorPreset(self, index) -> None:
        """

        """
        ...

    def processorPresetByIndex(self, index) -> None:
        """
        Return instance of TaskPreset Object
        """
        ...

    def submissionNames(self) -> list:
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

    def submissionChanged(self, submissionName) -> None:
        """
        self.submissionChanged(string, hiero.core.Project) -> Called by the C++ application when the submission choice changes in the Export Dialog.

        @param: submission name as a string
        """
        ...

    def isNukeShotExportPreset(self, preset) -> None:
        """
        Check if a preset is valid for Nuke shot export.  To be considered valid, the preset must contain
        a NukeShotExporter and a NukeRenderTask (write node).
        """
        ...

    def nukeShotExportPresets(self, project) -> None:
        """
        Get a list of presets which can export shots as Nuke scripts.
        Includes local presets and those in the project.
        """
        ...

    def isSingleSocketAllowed(self) -> None:
        """
        Return whether or not single socket exports are allowed.
        """
        ...
