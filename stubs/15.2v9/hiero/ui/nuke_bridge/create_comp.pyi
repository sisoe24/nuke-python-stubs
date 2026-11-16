# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.ui.BuildExternalMediaTrack as _hiero_ui_BuildExternalMediaTrack
from hiero.FnRedirect import showCreateCompSpecialDialog as showCreateCompSpecialDialog
from hiero.FnRedirect import viewIconForTrack as viewIconForTrack
from hiero.core import log as log
from hiero.core import nuke as nuke
from hiero.core import util as util
from hiero.core.FnVersionScanner import VersionScanner as VersionScanner
from hiero.ui.BuildExternalMediaTrack import BuildTrack as BuildTrack
from hiero.ui.BuildExternalMediaTrack import BuildTrackFromExportTagAction as BuildTrackFromExportTagAction
from hiero.ui.BuildExternalMediaTrack import TrackFinderByTag as TrackFinderByTag
from hiero.ui.BuildExternalMediaTrack import TrackItemCollisionDialog as TrackItemCollisionDialog
from hiero.ui.FnExporterBaseUI import InvalidOutputResolutionMessage as InvalidOutputResolutionMessage
from hiero.ui.FnPathQueryDialog import PathQueryDialog as PathQueryDialog
from hiero.ui.nuke_bridge.send_to_nuke import getProjectShotPreset as getProjectShotPreset
from nuke_internal.executeInMain import executeInMainThread as executeInMainThread
import hiero as hiero

kModelShotNameColumn: int
kModelTimesColumn: int
kModelTrackIndexRole: int
kModelTrackNameColumn: int

class CreateCompActionBase(_hiero_ui_BuildExternalMediaTrack.BuildTrackFromExportTagAction):
    staticMetaObject: Any
    def __init__(self, trackItems: Any, effectItems: Any, annotations: Any, title: Any) -> None: ...
    def createTrackItemCollisionDialog(self, srcCollisions: Any, track: Any, uniqueTrackName: Any) -> _hiero_ui_BuildExternalMediaTrack.TrackItemCollisionDialog: ...
    def doit(self) -> None: ...
    def execute(self, singleNukeScript: Any = ..., singleNukeScriptMasterTrackItem: Any = ...) -> None:
        """This function was created to set the master trackItem in popup dialog
        created in gui when creating comp out of multiple track items
        """
    def findExistingCreateCompTag(self, trackItem: Any) -> None:
        """Try to find a tag from a previous 'Create Comp' by checking that it has the expected metadata keys.
        Crucially, it should have the 'tag.trackItem' key indicating the tag had a comp track item created from it. 
        """
    def findTag(self, trackItem: Any) -> None:
        """Override from base class.  Find the Nuke Shot Exporter tag. """
    def findTransitionsToCopy(self, trackItems: Any) -> list[Any]:
        """Find transitions which should be copied to the VFX track. """
    def getExportPreset(self, project: Any) -> Any:
        """Get the export preset to be used as the basis for creating the comp.  To be implemented by sub-classes. """
    def getExternalFilePaths(self, trackItem: Any) -> None: ...
    def trackItemAdded(self, newTrackItem: Any, track: Any, originalTrackItem: Any) -> None: ...

class CreateCompAction(CreateCompActionBase):
    """Action for Create Comp.  Uses the project shot preset for export. """
    staticMetaObject: Any
    def __init__(self, trackItems: Any, effectItems: Any, annotations: Any, title: str = ...) -> None: ...
    def getExportPreset(self, project: Any) -> None: ...

class CreateCompForTrackItemsDialog:
    kCompTypeLabel: str
    kMasterShotTooltip: str
    kMasterTableLabel: str
    kMultiNukeText: str
    kSelectPresetButtonTooltip: str
    kSingleNukeText: str
    kWindowTitle: str
    staticMetaObject: Any
    def __init__(self, trackItems: Any, preset: Any, parent: Any = ...) -> None: ...
    def createCompTypeButtons(self) -> tuple[Any, Any]:
        """Create radio buttons for selecting between single/multi comp """
    def createLabel(self, text: Any) -> Any:
        """Create a label with the font set to bold """
    def createSelectPresetButton(self) -> Any:
        """Create the button for showing the Create Comp Special dialog """
    def createShotsTableWidget(self) -> Any:
        """Create the table for selecting the master track item """
    def masterTrackItem(self) -> Any:
        """For a single comp, get the selected master track item """
    def multipleComps(self) -> bool:
        """Get if creating a comp for each track item was selected """
    def preset(self) -> Any:
        """Get the export preset to use for the comp """
    def sizeHint(self) -> Any: ...

class CreateCompMessageBoxErrorHandler:
    """Class which handles error messages in Create Comp by showing a message box. """
    kDefaultBriefMessage: str
    def error(self, message: Any) -> None:
        """Handle an error message.  Currently shows a message box with the error text. """
    def getBriefTextFromMessage(self, message: Any) -> None:
        """Extract the error message from the text.  Due to the way the export system handles errors, the
        message that Create Comp gets is usually in the form of a full stack trace from the original exception.
        Try to find the exception message in that. 
        """
    def showErrorDialog(self, brief: Any, detail: Any) -> None:
        """Show an error message box with the brief and detailed text. """

class CreateCompShotTableDelegate:
    """Delegate for the table view in the create comp dialog. Allows for customising
    the icon size, and adding a left margin.
    """
    staticMetaObject: Any
    def __init__(self, iconSize: Any, leftMargin: Any, parent: Any = ...) -> None: ...
    def paint(self, painter: Any, option: Any, index: Any) -> None: ...
    def sizeHint(self, option: Any, index: Any) -> Any: ...

class CreateCompShotTableSortModel:
    """Proxy model for sorting shots. Overrides the defaults so
    a) times are sorted numerically
    b) for items which compare equal, breaks the tie by comparing track indexes
    """
    staticMetaObject: Any
    def __init__(self) -> None: ...
    def lessThan(self, source_left: Any, source_right: Any) -> bool: ...

class CreateCompSpecialAction(CreateCompActionBase):
    """Action for Create Comp Special.  Shows the export dialog for the user to choose and configure their preset. """
    staticMetaObject: Any
    def __init__(self, trackItems: Any, effectItems: Any, annotations: Any, title: str = ...) -> None: ...
    def getExportPreset(self, project: Any) -> Any: ...

def checkPresetRenderOutput(preset: Any) -> bool:
    """Check if the render output of the export preset is supported by create comp.  Only rendering to image sequences is allowed at the moment. """

def getRenderOutputType(preset: Any) -> Any:
    """Get the file type from the preset's Write node. """
