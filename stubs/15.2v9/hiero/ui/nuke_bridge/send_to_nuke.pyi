# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.ui.BuildExternalMediaTrack as _hiero_ui_BuildExternalMediaTrack
from hiero.core.FnVersionScanner import VersionScanner as VersionScanner
from hiero.ui import SendToNuke as SendToNuke
from hiero.ui.BuildExternalMediaTrack import BuildExternalMediaTrackAction as BuildExternalMediaTrackAction
from hiero.ui.BuildExternalMediaTrack import BuildExternalMediaTrackDialog as BuildExternalMediaTrackDialog
from hiero.ui.BuildExternalMediaTrack import BuildTrack as BuildTrack
from hiero.ui.BuildExternalMediaTrack import BuildTrackActionBase as BuildTrackActionBase
from hiero.ui.BuildExternalMediaTrack import BuildTrackFromExportTagAction as BuildTrackFromExportTagAction
from hiero.ui.BuildExternalMediaTrack import BuildTrackFromExportTagDialog as BuildTrackFromExportTagDialog
from hiero.ui.BuildExternalMediaTrack import TrackFinderByNameWithDialog as TrackFinderByNameWithDialog
from hiero.ui.BuildExternalMediaTrack import TrackFinderByTag as TrackFinderByTag
from hiero.ui.BuildExternalMediaTrack import TrackItemCollisionDialog as TrackItemCollisionDialog
from hiero.ui.nuke_bridge.hiero_state import HieroMediaDescriptor as HieroMediaDescriptor
import hiero as hiero

buildExternalMediaTrackAction: _hiero_ui_BuildExternalMediaTrack.BuildTrack

class ProjectShotPresetDialog:
    """Dialog for selecting a project shot preset. """
    staticMetaObject: Any
    def __init__(self, project: Any, text: Any) -> None: ...
    @staticmethod
    def getPresetFromDialog(project: Any, text: Any) -> None:
        """Show a ProjectShotPresetDialog and return the selected preset, or None if the user cancelled. """
    def selectedPreset(self) -> Any: ...

class SendToNukeHandler:
    def __init__(self, hieroState: Any) -> None: ...
    def binContextMenuEventHandler(self, event: Any) -> Any: ...
    def timelineContextMenuEventHandler(self, event: Any) -> Any: ...

def getProjectShotPreset(project: Any) -> None:
    """Get the project shot preset, prompting the user if the currently selected preset
    does not exist or is invalid. 
    """
