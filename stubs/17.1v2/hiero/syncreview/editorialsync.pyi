# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import hiero.syncreview.synctool as _hiero_syncreview_synctool
from hiero.core import Sequence as Sequence
from hiero.core import events as events
from hiero.core.find_items import findItemByGuid as findItemByGuid
from hiero.syncreview import messages as messages
from hiero.syncreview.log import logMessage as logMessage
from hiero.syncreview.synctool import SyncTool as SyncTool
from hiero.syncreview.synctool import localCallback as localCallback
from hiero.syncreview.synctool import remoteCallback as remoteCallback

class SyncSequenceEditsTool(_hiero_syncreview_synctool.SyncTool):
    """Tool for syncing sequence edits. """
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, messageDispatcher: Any, viewerSyncTool: Any) -> None: ...
    def onLocalSequenceEdited(self, *args: Any, **kwargs: Any) -> Any: ...
    def onRemoteSequenceEdited(self, *args: Any, **kwargs: Any) -> Any: ...
