# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from typing import final
import hiero.syncreview.synctool as _hiero_syncreview_synctool
from hiero.syncreview import config as config
from hiero.syncreview import messages as messages
from hiero.syncreview.log import logMessage as logMessage
from hiero.syncreview.synctool import SyncTool as SyncTool
import hiero as hiero

class HostProjectSyncTool(_hiero_syncreview_synctool.SyncTool):
    """Class for managing project syncing logic which is specific to the host.
    This includes:
      - Sending synced projects to clients when they first connect
      - Listening for opening and closing of projects and pushing those changes
        to other participants
    """
    staticMetaObject: Any
    def __init__(self, messageDispatcher: Any, pushTool: Any) -> None: ...

@final
class ProgressTask:
    """ProgressTask"""
    kDelayedPopup: int
    kDisable: int
    kKeepWhenFinished: int
    kModal: int
    kShowTimeToGo: int
    kUserCanCancel: int
    kUserCanPause: int
    def isCancelled(self) -> bool:
        """self.isCancelled() -> True if the user has requested the task to be cancelled."""
    def setMessage(self, s: Any) -> None:
        """self.setMessage(s) -> None.

        set the message for the progress task
        """
    def setProgress(self, i: Any) -> None:
        """self.setProgress(i) -> None.

        i is an integer representing the current progress
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> ProgressTask: ...

class ProjectPushTool(_hiero_syncreview_synctool.SyncTool):
    """Sync tool used for pushing projects to other clients and loading projects pushed from elsewhere. Provides
    functions for getting the current project, loading projects, and pushing projects to other clients.
    """
    STATE_IDLE: int
    STATE_LOADING_PROJECTS: int
    STATE_PUSHING_PROJECTS: int
    staticMetaObject: Any
    def __init__(self, messageDispatcher: Any, viewerSyncTool: Any, clientData: Any) -> None: ...
    def addProjects(self, projects: Any, pushNow: bool = ...) -> None:
        """Add projects for syncing. This should only be called on the host, clients
        get the project pushed to them.
        The optional pushNow arg can be set to True to have the new project pushed
        to connected clients.
        """
    def projects(self) -> list[Any]:
        """Get a list of synced projects """
    def pushAllProjects(self, receiver: Any) -> None:
        """Push all synced projects to the specified recipients """
    def removeProject(self, project: Any) -> None:
        """Remove a project from the sync session (this happens when the host closes it or
        uses save as). This sends messages to have it closed on connected clients.
        """
    def state(self) -> int:
        """Get the current state of the tool """

class ProjectSyncData:
    """Data container for a synced project """
    def __init__(self, project: Any) -> None: ...

class ProjectSyncProgressTool(_hiero_syncreview_synctool.SyncTool):
    """Manages the project sync progress of all other clients, and shows a progress task when appropriate.  """
    staticMetaObject: Any
    def __init__(self, messageDispatcher: Any) -> None: ...

def syncReviewTempDir(name: str = ...) -> str:
    """Get the directory for temp files related to the sync functionality, with an
    option sub-directory name, creating if necessary.
    """
