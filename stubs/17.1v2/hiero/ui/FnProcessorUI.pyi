# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
from typing import Generator
import hiero.ui as _hiero_ui
import hiero.ui.FnElidedLabel as _hiero_ui_FnElidedLabel
from hiero.core import FnExporterBase as FnExporterBase
from hiero.core.FnCompSourceInfo import CompSourceInfo as CompSourceInfo
from hiero.core.util import filesystem as filesystem
from hiero.ui import IProcessorUI as IProcessorUI
from hiero.ui.FnElidedLabel import ElidedLabel as ElidedLabel
import hiero as hiero

class ProcessorUIBase(_hiero_ui.IProcessorUI):
    """ProcessorUIBase is the base class from which all Processor UI components must derive.  Defines the UI structure followed
    by the specialised processor UIs. 
    """
    def __init__(self, preset: Any, itemTypes: Any) -> None: ...
    def checkOfflineMedia(self, exportItems: Any) -> bool: ...
    def checkUnrenderedComps(self, exportItems: Any) -> bool:
        """Check for unrendered comps selected for export and ask the user what to do. """
    def createPathPreviewWidget(self) -> _hiero_ui_FnElidedLabel.ElidedLabel:
        """Create a widget for showing a preview of the expanded export path. """
    def createProcessorSettingsWidget(self, exportItems: Any) -> Any:
        """Create the UI for processor-specific settings.  To be reimplemented by subclasses. """
    def createVersionWidget(self) -> Any:
        """Create a widget for selecting the version number for export. """
    def findCompItems(self, items: Any) -> Generator[Any, Any, None]:
        """Search for comp clips and track items in a list of ItemWrappers. """
    def findOfflineMedia(self, exportItems: Any) -> tuple[list[Any], list[Any]]: ...
    def findTagsForItems(self, exportItems: Any) -> list[Any]:
        """Find tags for the export items. """
    def getTaskItemType(self) -> Any: ...
    def isTranscodeExport(self) -> bool:
        """Check if there are transcode tasks in this export. """
    def offlineMediaPrompt(self, messageText: Any, messageDetails: Any, hasOnline: Any) -> bool: ...
    def onExportStructureModified(self) -> None:
        """Callback when the export structure is modified by the user. """
    def onExportStructureSelectionChanged(self) -> None:
        """Callback when the selection in the export structure viewer changes. """
    def onExportStructureViewerDestroyed(self) -> None:
        """Callback when the export structure viewer is destroyed.  Qt will delete it while we still
        have a reference, so reset to None when the destroyed() signal is emitted. 
        """
    def onVersionIndexChanged(self, value: Any) -> None:
        """Callback when the version index changes. """
    def onVersionPaddingChanged(self, padding: Any) -> None:
        """Callback when the version padding changes. """
    def populateUI(self, processorUIWidget: Any, taskUIWidget: Any, exportItems: Any) -> None:
        """Build the processor UI and add it to widget. """
    def preset(self) -> None:
        """Get the export preset. """
    def processorSettingsLabel(self) -> Any:
        """Get the label which is put on the tab for processor-specific settings.  To be reimplemented by subclasses. """
    def projectFromSelection(self, items: Any) -> None: ...
    def refreshContent(self) -> None:
        """Refresh the content area of this ProcessorUI """
    def savePreset(self) -> None:
        """Save the export template to the preset. """
    def setPreset(self, preset: Any) -> None:
        """Set the export preset. """
    def setTaskContent(self, preset: Any) -> None:
        """Get the UI for a task preset and add it in the 'Content' tab. """
    def skipOffline(self) -> Any: ...
    def toTrackItems(self, items: Any) -> Generator[Any, Any, None]: ...
    def updatePathPreview(self) -> None:
        """Update the path preview widget for the currently selected item in the
        tree view.
        """
    def validate(self, exportItems: Any) -> bool:
        """Validate settings in UI. Return False for failure in order to abort export."""

def isCompItemMissingRenders(compItem: Any) -> bool:
    """Check if renders for a comp item are missing or out of date. Returns
    (missing, out of date) 
    """
