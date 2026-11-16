# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.syncreview.synctool as _hiero_syncreview_synctool
from hiero.syncreview import messages as messages
from hiero.syncreview.synctool import SyncTool as SyncTool
import hiero as hiero

class SyncClientCursor(_hiero_syncreview_synctool.SyncTool):
    """Logic for syncing the cursor position within a session. """
    staticMetaObject: Any
    def __init__(self, messageDispatcher: Any, clientDataProvider: Any) -> None: ...
    def shutdown(self) -> None: ...
