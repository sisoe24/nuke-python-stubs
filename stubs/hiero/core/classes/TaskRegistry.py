import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class TaskRegistry(IExporterRegistry):
    """
    IExporterRegistry provides a simple interface for our C++ Application to access python instance of hiero.core.TaskRegistry.

    This class should not be used directly; use hiero.core.TaskRegistry instead.
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def registerTask(self, preset, task):
        """
        Register the association between a Task and TaskPreset
        """
        return None

    def registerProcessor(self, preset, processor):
        """
        Register the association between a Processor and ProcessorPreset
        """
        return None

    def registerPreset(self, parentType, preset):
        """
        Register a preset instance and association with parentType
        """
        return None

    def projectUnloaded(self, project):
        """
        Called on project unload to remove presets associated with project
        """
        return None

    def projectDuplicated(self, project, newProject):
        """
        Called on project clone to duplicate the associated project presets
        """
        return None

    def loadPresets(self, path):
        """
        Load all xml presets within specified path and register
        """
        return None

    def _loadPresets(self, path, list):
        """

        """
        return None

    def presetFromXml(self, xml, register=True):
        """
        Deserialize preset from xml string.
        Requires derived TaskPreset classes to be registered.
        """
        return None

    def _loadPresetElement(self, element):
        """

        """
        return None

    def savePresets(self, path):
        """
        Save all registered presets, as xml, to path specified.
        """
        return None

    def _savePresets(self, path, presetlist, dictionary):
        """

        """
        return None

    def presetToXml(self, preset):
        """
        Serialise a TaskPreset to XML and return as string.
        Returns an empty string on failure.
        """
        return None

    def _presetToXml(self, preset):
        """
        Serialize a preset to XML and return the root element. Throws on failure.
        """
        return None

    def _savePresetElement(self, key, value, parent):
        """
        Save a preset key/value as an XML element and append it to the parent.  Called recursively for containers.
        """
        return None

    def presetsSubDirectory(self):
        """
        self.presetsSubDirectory() -> Get the sub-directory in the plugin paths to search for presets.
        """
        return None

    def revertDefaultPresets(self):
        """
        self.revertDefaultPresets(string) -> Called by the C++ application reconstruct the default presets.

        @param: path as string
        """
        return None

    def setDefaultPresets(self, defaultPresets):
        """

        """
        return None

    def addDefaultPresets(self, overwrite=False):
        """

        """
        return None

    def startPresetChanges(self, project):
        """
        self.startPresetChanges(hiero.core.Project) -> Called when the user might start editing the presets, so the changes can be reverted if necessary.

        @param: hiero.core.Project)
        """
        return None

    def discardPresetChanges(self, project):
        """
        self.startPresetChanges(hiero.core.Project) -> Discard any changes to the presets since startPresetChanges() was called.

        @param: hiero.core.Project)
        """
        return None

    def createAndAddProcessorPreset(self, name, typeTemplate):
        """
        self.createAndAddProcessorPreset(string, hiero.core.TaskPreset) -> Called by the C++ application to create a new preset, using typetemplate as a template.

        @param: string - Preset name
        @return: hiero.core.TaskPreset instance as type template
        """
        return Any

    def copyPreset(self, preset):
        """
        Create a copy of a preset.  The copy is not added to the registry.
        """
        return None

    def copyAndAddProcessorPreset(self, preset):
        """
        self.copyAndAddProcessorPreset() -> Called by the C++ application to duplicate a preset.

        @param: hiero.core.TaskPreset instance for duplication
        @return: new hiero.core.TaskPreset instance
        """
        return Any

    def copyAndAddProjectPreset(self, preset, project):
        """
        Duplicate a preset and assign it to a project imediately to prevent name clashes
        """
        return None

    def addProcessorPreset(self, name, preset):
        """
        Register Processor Preset Instance
        """
        return None

    def removeProcessorPreset(self, preset):
        """
        Remove Processor preset from registry
        """
        return None

    def renameProcessorPreset(self, preset, newName):
        """
        Validate and update name of Processor Preset
        """
        return None

    def assignPresetToProject(self, preset, project):
        """
        Assign preset to project and ensure name is unique within project. Project may be None in which case preset will be assigned 'local'
        """
        return None

    def numProcessorPresets(self):
        """
        Return the total number of Processor preset instances registered
        """
        return None

    def processorPresetName(self, index):
        """
        Return the name of Processor preset by index
        """
        return None

    def numTasks(self):
        """
        Returns the number of Tasks Registered
        """
        return None

    def numProcessors(self):
        """
        Return the number or processors in the Registry
        """
        return None

    def taskName(self, index):
        """
        Returns a Task name by Index
        """
        return None

    def processorName(self, index):
        """
        Returns a Processor name by index
        """
        return None

    def processorPresetNames(self):
        """
        Returns a tuple of Processor Preset names
        """
        return None

    def processorPresetByName(self, name, project=None):
        """
        Returns the preset with specified name associated with project. If project is None preset will be searched for in local presets
        """
        return None

    def _getPresetsFromList(self, presetsList, projectToFilter):
        """
        Returns a list of presets name associated with 'projectToFilter' from the specified 'presetsList'
        """
        return None

    def projectPresets(self, project):
        """
        Returns a list of preset names associated with the specified project
        """
        return None

    def localPresets(self):
        """
        Returns a list of preset names NOT associated with the specified project
        """
        return None

    def projectExportHistoryXml(self, project):
        """
        Get the project export history as a list of xml fragments. Use the xml to avoid problems with reference
        counting the preset objects when calling from C++.
        """
        return None

    def restoreProjectExportHistoryXml(self, project, presetsXml):
        """
        Set the project export history as a list of xml fragments. Use the xml to avoid problems with reference
        counting the preset objects when calling from C++.
        """
        return None

    def addPresetToProjectExportHistory(self, project, preset):
        """
        Add a preset to the export history for a project.
        """
        return None

    def findPresetInProjectExportHistory(self, project, presetId):
        """
        Attempt to find a preset in a project's export history.
        """
        return None

    def _computePresetsHash(self, presets):
        """

        """
        return None

    def getPresetId(self, preset):
        """
        Get the id (hash) of the given preset.
        """
        return None

    def localPresetsChanged(self):
        """
        Check if the local task presets have changed since startPresetChanges() was called.
        """
        return None

    def projectPresetsChanged(self, project):
        """
        Check if the task presets for the given project have changed since startPresetChanges(project) was called.
        """
        return None

    def getProcessor(self, index):
        """

        """
        return None

    def processorByIndex(self, index):
        """
        Returns a processor by index
        """
        return None

    def getPresetType(self, ident):
        """

        """
        return None

    def presetTypeFromIdent(self, ident):
        """
        Resolve preset ident string to Preset class type
        """
        return None

    def createTaskFromPreset(self, preset, initDictionary):
        """

        """
        return None

    def getProcessorFromPreset(self, presetName):
        """

        """
        return None

    def processorFromPreset(self, presetName):
        """
        Return type of task from preset name
        """
        return None

    def _checkPresetToFormat(self, presetName, exportTemplate):
        """
        Checks if 'exportTemplate' defines a specific output format and if its
        valid by creating a hiero.core.Format.
        Raises a ValueError exception if a format is not valid.
        """
        return None

    def _getToScaleFromPreset(self, exportTemplate):
        """
        Returns a list of scale options defined in 'exportTemplate'

        """
        return None

    def _checkToScaleForSequence(self, presetName, toScaleOptions, itemName, seqFormat):
        """
        Checks if the output format for a specific sequence/clip is valid when
        scalled with th 'scale' option defined in the exportTemplate preset.
        Raises a ValueError exception if a format is not valid.
        """
        return None

    def _checkOutputResolution(self, preset, items):
        """
        Checks if the output resolution defined in the preset or defined by the
        items to be exported are valid for PLE / Indie variants.
        Raises a ValueError exception if a format is not valid.
        """
        return None

    def validateExport(self, preset, items):
        """
        Implements IExporterRegistry.validateExport
        """
        return None

    def createProcessor(self, preset, submissionName=None, synchronous=False):
        """
        Create the processor for an export and return it. This doesn't start
        the export.
        """
        return None

    def createAndExecuteProcessor(self, preset, items, submissionName=None, synchronous=False):
        """
        Instantiate the Processor associated with preset and startProcessing items
        """
        return None

    def getProcessorPreset(self, index):
        """

        """
        return None

    def processorPresetByIndex(self, index):
        """
        Return instance of TaskPreset Object
        """
        return None

    def submissionNames(self):
        """
        self.submissionNames() -> Called by the C++ application to get a list of the available Submission objects. Submission objects are used to manage render farm renders.

        @return: list of name strings
        """
        return list()

    def submissionByName(self, name):
        """

        """
        return None

    def addSubmission(self, name, submissionClass):
        """

        """
        return None

    def submissionChanged(self, submissionName):
        """
        self.submissionChanged(string, hiero.core.Project) -> Called by the C++ application when the submission choice changes in the Export Dialog.

        @param: submission name as a string
        """
        return None

    def isNukeShotExportPreset(self, preset):
        """
        Check if a preset is valid for Nuke shot export.  To be considered valid, the preset must contain
        a NukeShotExporter and a NukeRenderTask (write node).
        """
        return None

    def nukeShotExportPresets(self, project):
        """
        Get a list of presets which can export shots as Nuke scripts.
        Includes local presets and those in the project.
        """
        return None

    def isSingleSocketAllowed(self):
        """
        Return whether or not single socket exports are allowed.
        """
        return None
