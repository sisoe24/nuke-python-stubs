# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.syncreview.synctool as _hiero_syncreview_synctool
from hiero.core import BinItem as BinItem
from hiero.core import TrackItem as TrackItem
from hiero.core import events as events
from hiero.core.find_items import findItemByGuid as findItemByGuid
from hiero.syncreview import messages as messages
from hiero.syncreview.log import logMessage as logMessage
from hiero.syncreview.synctool import SyncTool as SyncTool
from hiero.syncreview.synctool import localCallback as localCallback
from hiero.syncreview.synctool import remoteCallback as remoteCallback

class SyncVersionsTool(_hiero_syncreview_synctool.SyncTool):
    """Tool for syncing version changes on bin and track items. """
    staticMetaObject: Any
    def __init__(self, messageDispatcher: Any) -> None: ...
