import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class IExporterRegistry(Object):
    """
    IExporterRegistry provides a simple interface for our C++ Application to access python instance of hiero.core.TaskRegistry.

    This class should not be used directly; use hiero.core.TaskRegistry instead.
    """

    def __setattr__(self, name, value, ):
        """
        Implement setattr(self, name, value).
        """
        return None

    def __delattr__(self, name, ):
        """
        Implement delattr(self, name).
        """
        return None

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def assignPresetToProject(self, preset: core.ITaskPreset, project: core.Project) -> None:
        """
        self.assignPresetToProject(hiero.core.TaskPreset, hiero.core.Project) -> Called by the C++ application to assign a TaskPreset to .
        a null hiero.core.Project will remove the project assignment and revernt the preset to local ownership.

        @param: hiero.core.TaskPreset
        @param: hiero.core.Project
        """
        return None

    def copyAndAddProcessorPreset(self, preset: core.ITaskPreset) -> core.ITaskPreset:
        """
        self.copyAndAddProcessorPreset() -> Called by the C++ application to duplicate a preset.

        @param: hiero.core.TaskPreset instance for duplication
        @return: new hiero.core.TaskPreset instance
        """
        return core.ITaskPreset()

    def copyAndAddProjectPreset(self, preset: core.ITaskPreset, project: core.Project) -> core.ITaskPreset:
        """
        copyAndAddProjectPreset() -> Called by the C++ application to duplicate a preset and assign it to a new project.

        @param: hiero.core.TaskPreset instance for duplication
        @param: hiero.core.Project to which cloned preset should be assigned
        @return: new hiero.core.TaskPreset instance
        """
        return core.ITaskPreset()

    def createAndAddProcessorPreset(self, preset: str, typetemplate: core.ITaskPreset) -> core.ITaskPreset:
        """
        self.createAndAddProcessorPreset(string, hiero.core.TaskPreset) -> Called by the C++ application to create a new preset, using typetemplate as a template.

        @param: string - Preset name
        @return: hiero.core.TaskPreset instance as type template
        """
        return core.ITaskPreset()

    def createAndExecuteProcessor(self, preset: core.ITaskPreset, items: typing.List*args, submissionName: str) -> None:
        """
        self.createAndExecuteProcessor(hiero.core.TaskPreset, [hiero.core.ItemWrapper], string) -> Called by the C++ application to instantiate the Processor associated with specified preset and execute on the selected items.

        @param: hiero.core.TaskPreset
        @param: list of items for export
        @param: name of submission object used for dispatching job to renderfarm
        """
        return None

    def discardPresetChanges(self, project: core.Project) -> None:
        """
        self.startPresetChanges(hiero.core.Project) -> Discard any changes to the presets since startPresetChanges() was called.

        @param: hiero.core.Project)
        """
        return None

    def loadPresets(self, path: str) -> bool:
        """
        self.loadPresets(string) -> Called by the C++ application to load presets from a specified path.

        @param: path as string
        """
        return bool()

    def localPresets(self) -> typing.List*args:
        """
        self.projectPresets() -> Returns a list of local presets assigned to the specified Project.

        @return: list of TaskPreset instances
        """
        return list()

    def localPresetsChanged(self) -> bool:
        """
        self.localPresetsChanged() -> Called by the C++ application to check whether local presets have changed since last save.

        @return: bool changed state
        """
        return bool()

    def nukeShotExportPresets(self, project: core.Project) -> typing.List*args:
        """
        self.nukeShotExportPresets(hiero.core.Project) -> Get a list of presets which are contain Nuke shot exports.

        @return: list of TaskPreset instances
        """
        return list()

    def presetFromXml(self, xml: str) -> core.ITaskPreset:
        """
        self.presetFromXml(string) -> Called by the C++ application to ask the TaskRegistry to deserialize a Task preset from xml.

        @param: string - Preset XML
        @return: hiero.core.TaskPreset instance
        """
        return core.ITaskPreset()

    def presetToPrettyXml(self, preset: core.ITaskPreset) -> str:
        """
        self.presetToPrettyXml(hiero.core.TaskPreset) -> Called by the C++ application to ask the TaskRegistry to serialize a Task preset to human friendly formatted xml.

        @param: hiero.core.TaskPreset instance
        @return: string - Preset XML
        """
        return str()

    def presetToXml(self, preset: core.ITaskPreset) -> str:
        """
        self.presetToXml(hiero.core.TaskPreset) -> Called by the C++ application to ask the TaskRegistry to serialize a Task preset to xml.

        @param: hiero.core.TaskPreset instance
        @return: string - Preset XML
        """
        return str()

    def presetsSubDirectory(self) -> str:
        """
        self.presetsSubDirectory() -> Get the sub-directory in the plugin paths to search for presets.
        """
        return str()

    def projectDuplicated(self, project: core.Project, newProject: core.Project) -> None:
        """
        projectDuplicated(hiero.core.Project, hiero.core.Project) -> Called by the C++ application to notify the TaskRegistry that a project has been duplicated and its associated Presets should be duplicated and assigned to the new project.

        @param: hiero.core.Project - original project
        @param: hiero.core.Project - new project
        """
        return None

    def projectExportHistoryXml(self, project: core.Project) -> typing.List*args:
        """
        self.projectExportHistoryXml(hiero.core.Project) -> Returns a list of XML fragments containing the project export history.

        @param hiero.core.Project: project
        @return: list of strings
        """
        return list()

    def projectPresets(self, project: core.Project) -> typing.List*args:
        """
        self.projectPresets(hiero.core.Project) -> Returns a list of project presets assigned to the specified Project.

        @param: hiero.core.Project
        @return: list of TaskPreset instances
        """
        return list()

    def projectPresetsChanged(self, project: core.Project) -> bool:
        """
        self.projectPresetsChanged(hiero.core.Project) -> Called by the C++ application to check whether project presets have changed since project last save.

        @param: hiero.core.Project
        """
        return bool()

    def projectUnloaded(self, project: core.Project) -> None:
        """
        self.projectUnloaded(hiero.core.Project) -> Called by the C++ application to notify the TaskRegistry that a project has been unloaded and its associated Presets should be released.

        @param: hiero.core.Project
        """
        return None

    def registerme(self) -> None:
        """
        self.registerme() -> Called from python implimentation of TaskRegistry to register instance as the Application Task Registry.
        """
        return None

    def removeProcessorPreset(self, preset: core.ITaskPreset) -> None:
        """
        self.removeProcessorPreset(hiero.core.TaskPreset) -> Called by the C++ application to remove a preset from the registry.

        @param: hiero.core.TaskPreset
        """
        return None

    def renameProcessorPreset(self, preset: core.ITaskPreset, newname: str) -> None:
        """
        self.renameProcessorPreset(hiero.core.TaskPreset, string) -> Called by the C++ application to rename a preset in the registry.

        @param: hiero.core.TaskPreset
        """
        return None

    def restoreProjectExportHistoryXml(self, project: core.Project, history: typing.List*args) -> None:
        """
        self.restoreProjectExportHistoryXml(hiero.core.Project, list) -> Restore the export history for a project.

        @param hiero.core.Project: project
        @param list: list of strings containing export history
        """
        return None

    def revertDefaultPresets(self) -> None:
        """
        self.revertDefaultPresets(string) -> Called by the C++ application reconstruct the default presets.

        @param: path as string
        """
        return None

    def savePresets(self, path: str) -> bool:
        """
        self.savePresets(string) -> Called by the C++ application to save presets to a specified path.

        @param: path as string
        """
        return bool()

    def startPresetChanges(self, project: core.Project) -> None:
        """
        self.startPresetChanges(hiero.core.Project) -> Called when the user might start editing the presets, so the changes can be reverted if necessary.

        @param: hiero.core.Project)
        """
        return None

    def submissionChanged(self, submissionName: str) -> None:
        """
        self.submissionChanged(string, hiero.core.Project) -> Called by the C++ application when the submission choice changes in the Export Dialog.

        @param: submission name as a string
        """
        return None

    def submissionNames(self) -> typing.List*args:
        """
        self.submissionNames() -> Called by the C++ application to get a list of the available Submission objects. Submission objects are used to manage render farm renders.

        @return: list of name strings
        """
        return list()

    def validateExport(self, preset: core.ITaskPreset, items: typing.List*args) -> str:
        """
        self.validateExport(hiero.core.TaskPreset, [hiero.core.ItemWrapper]) -> Called by the C++ application to determinate if preset and selected items have valid resolution according the application mode.
        A warning message will be shown in case of any invalid output resolution.

        @param: hiero.core.TaskPreset
        @param: list of items for export
        @return: An error string if disallowed, otherwise an empty string.
        """
        return str()

    def __copy__(self,) -> None:
        """

        """
        return None
