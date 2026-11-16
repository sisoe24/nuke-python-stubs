# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.syncreview.synctool as _hiero_syncreview_synctool
from hiero.core import Bin as Bin
from hiero.core import BinItem as BinItem
from hiero.core import Version as Version
from hiero.core import events as events
from hiero.core.find_items import findItemByGuid as findItemByGuid
from hiero.core.find_items import findProjectTags as findProjectTags
from hiero.syncreview import messages as messages
from hiero.syncreview.log import logMessage as logMessage
from hiero.syncreview.synctool import SyncTool as SyncTool
from hiero.syncreview.synctool import localCallback as localCallback
from hiero.syncreview.synctool import remoteCallback as remoteCallback

class SyncBinItemTool(_hiero_syncreview_synctool.SyncTool):
    """Tool for syncing generic bin item operations such as adding empty items.
    Type-specific operations should be handled by other tools.
    """
    staticMetaObject: Any
    def __init__(self, messageDispatcher: Any) -> None: ...
    def onLocalBinItemAdded(self, *args: Any, **kwargs: Any) -> Any: ...
    def onLocalBinItemMoved(self, *args: Any, **kwargs: Any) -> Any: ...
    def onLocalBinItemRemoved(self, *args: Any, **kwargs: Any) -> Any: ...
    def onLocalBinItemRenamed(self, *args: Any, **kwargs: Any) -> Any: ...
    def onRemoteBinItemAdded(self, *args: Any, **kwargs: Any) -> Any: ...
    def onRemoteBinItemMoved(self, *args: Any, **kwargs: Any) -> Any: ...
    def onRemoteBinItemRemoved(self, *args: Any, **kwargs: Any) -> Any: ...
    def onRemoteBinItemRenamed(self, *args: Any, **kwargs: Any) -> Any: ...
