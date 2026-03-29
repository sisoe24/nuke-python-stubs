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


class ProcessorUIBase(IProcessorUI):
    """
    ProcessorUIBase is the base class from which all Processor UI components must derive.  Defines the UI structure followed
    by the specialised processor UIs.
    """

    def getTaskItemType(self) -> None:
        """

        """
        ...

    def __init__(self, preset, itemTypes) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def validate(self, exportItems: object) -> bool:
        """
        Validate settings in UI. Return False for failure in order to abort export.
        """
        ...

    def isTranscodeExport(self) -> bool:
        """
        Check if there are transcode tasks in this export.
        """
        ...

    def findCompItems(self, items: object) -> list:
        """
        Search for comp clips and track items in a list of ItemWrappers.
        """
        ...

    def checkUnrenderedComps(self, exportItems: object) -> None:
        """
        Check for unrendered comps selected for export and ask the user what to do.
        """
        ...

    def projectFromSelection(self, items) -> None:
        """

        """
        ...

    def toTrackItems(self, items) -> None:
        """

        """
        ...

    def findOfflineMedia(self, exportItems) -> None:
        """

        """
        ...

    def offlineMediaPrompt(self, messageText, messageDetails, hasOnline) -> None:
        """

        """
        ...

    def checkOfflineMedia(self, exportItems) -> None:
        """

        """
        ...

    def findTagsForItems(self, exportItems: object) -> None:
        """
        Find tags for the export items.
        """
        ...

    def populateUI(self, processorUIWidget: object, taskUIWidget: object, exportItems: object) -> None:
        """
        Build the processor UI and add it to widget.
        """
        ...

    def setPreset(self, preset: object) -> None:
        """
        Set the export preset.
        """
        ...

    def preset(self) -> object:
        """
        Get the export preset.
        """
        ...

    def setTaskContent(self, preset: object) -> None:
        """
        Get the UI for a task preset and add it in the 'Content' tab.
        """
        ...

    def onExportStructureModified(self) -> None:
        """
        Callback when the export structure is modified by the user.
        """
        ...

    def onExportStructureSelectionChanged(self) -> None:
        """
        Callback when the selection in the export structure viewer changes.
        """
        ...

    def onExportStructureViewerDestroyed(self) -> None:
        """
        Callback when the export structure viewer is destroyed.  Qt will delete it while we still
        have a reference, so reset to None when the destroyed() signal is emitted.
        """
        ...

    def createProcessorSettingsWidget(self, exportItems) -> None:
        """
        Create the UI for processor-specific settings.  To be reimplemented by subclasses.
        """
        ...

    def processorSettingsLabel(self) -> str:
        """
        Get the label which is put on the tab for processor-specific settings.  To be reimplemented by subclasses.
        """
        ...

    def savePreset(self) -> None:
        """
        Save the export template to the preset.
        """
        ...

    def createVersionWidget(self) -> object:
        """
        Create a widget for selecting the version number for export.
        """
        ...

    def onVersionIndexChanged(self, value: int) -> None:
        """
        Callback when the version index changes.
        """
        ...

    def onVersionPaddingChanged(self, padding: int) -> None:
        """
        Callback when the version padding changes.
        """
        ...

    def createPathPreviewWidget(self) -> object:
        """
        Create a widget for showing a preview of the expanded export path.
        """
        ...

    def updatePathPreview(self) -> None:
        """
        Update the path preview widget for the currently selected item in the
        tree view.
        """
        ...

    def skipOffline(self) -> None:
        """

        """
        ...

    def refreshContent(self) -> None:
        """
        Refresh the content area of this ProcessorUI
        """
        ...
