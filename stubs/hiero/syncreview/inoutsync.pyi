# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.syncreview.synctool as _hiero_syncreview_synctool
from hiero.core import Clip as Clip
from hiero.core import Sequence as Sequence
from hiero.core import events as events
from hiero.core.find_items import findItemByGuid as findItemByGuid
from hiero.syncreview import messages as messages
from hiero.syncreview.synctool import SyncTool as SyncTool
from hiero.syncreview.synctool import localCallback as localCallback
from hiero.syncreview.synctool import remoteCallback as remoteCallback

class SyncInOutTool(_hiero_syncreview_synctool.SyncTool):
    """Tool for syncing changes to the 'in' and 'out' points. """
    staticMetaObject: Any
    def __init__(self, messageDispatcher: Any) -> None: ...
