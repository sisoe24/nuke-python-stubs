import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class ProcessorUIBase(IProcessorUI):
    """
    ProcessorUIBase is the base class from which all Processor UI components must derive.  Defines the UI structure followed
    by the specialised processor UIs.
    """

    def getTaskItemType(self):
        """

        """
        return None

    def __init__(self, preset, itemTypes):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def validate(self, exportItems):
        """
        Validate settings in UI. Return False for failure in order to abort export.
        """
        return None

    def isTranscodeExport(self):
        """
        Check if there are transcode tasks in this export.
        """
        return None

    def findCompItems(self, items):
        """
        Search for comp clips and track items in a list of ItemWrappers.
        """
        return None

    def checkUnrenderedComps(self, exportItems):
        """
        Check for unrendered comps selected for export and ask the user what to do.
        """
        return None

    def projectFromSelection(self, items):
        """

        """
        return None

    def toTrackItems(self, items):
        """

        """
        return None

    def findOfflineMedia(self, exportItems):
        """

        """
        return None

    def offlineMediaPrompt(self, messageText, messageDetails, hasOnline):
        """

        """
        return None

    def checkOfflineMedia(self, exportItems):
        """

        """
        return None

    def findTagsForItems(self, exportItems):
        """
        Find tags for the export items.
        """
        return None

    def populateUI(self, processorUIWidget, taskUIWidget, exportItems):
        """
        Build the processor UI and add it to widget.
        """
        return None

    def setPreset(self, preset):
        """
        Set the export preset.
        """
        return None

    def preset(self):
        """
        Get the export preset.
        """
        return None

    def setTaskContent(self, preset):
        """
        Get the UI for a task preset and add it in the 'Content' tab.
        """
        return None

    def onExportStructureModified(self):
        """
        Callback when the export structure is modified by the user.
        """
        return None

    def onExportStructureSelectionChanged(self):
        """
        Callback when the selection in the export structure viewer changes.
        """
        return None

    def onExportStructureViewerDestroyed(self):
        """
        Callback when the export structure viewer is destroyed.  Qt will delete it while we still
        have a reference, so reset to None when the destroyed() signal is emitted.
        """
        return None

    def createProcessorSettingsWidget(self, exportItems):
        """
        Create the UI for processor-specific settings.  To be reimplemented by subclasses.
        """
        return None

    def processorSettingsLabel(self):
        """
        Get the label which is put on the tab for processor-specific settings.  To be reimplemented by subclasses.
        """
        return None

    def savePreset(self):
        """
        Save the export template to the preset.
        """
        return None

    def createVersionWidget(self):
        """
        Create a widget for selecting the version number for export.
        """
        return None

    def onVersionIndexChanged(self, value):
        """
        Callback when the version index changes.
        """
        return None

    def onVersionPaddingChanged(self, padding):
        """
        Callback when the version padding changes.
        """
        return None

    def createPathPreviewWidget(self):
        """
        Create a widget for showing a preview of the expanded export path.
        """
        return None

    def updatePathPreview(self):
        """
        Update the path preview widget for the currently selected item in the
        tree view.
        """
        return None

    def skipOffline(self):
        """

        """
        return None

    def refreshContent(self):
        """
        Refresh the content area of this ProcessorUI
        """
        return None
