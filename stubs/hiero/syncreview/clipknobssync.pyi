# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.syncreview.synctool as _hiero_syncreview_synctool
from hiero.core import Clip as Clip
from hiero.core import events as events
from hiero.core.find_items import findItemByGuid as findItemByGuid
from hiero.syncreview import messages as messages
from hiero.syncreview.log import logMessage as logMessage
from hiero.syncreview.synctool import SyncTool as SyncTool
from hiero.syncreview.synctool import localCallback as localCallback
from hiero.syncreview.synctool import remoteCallback as remoteCallback

class SyncClipKnobsTool(_hiero_syncreview_synctool.SyncTool):
    """Tool for syncing the knob values of clips"""
    staticMetaObject: Any
    def __init__(self, messageDispatcher: Any) -> None: ...
    def onLocalClipKnobChanged(self, *args: Any, **kwargs: Any) -> Any: ...
    def onRemoteClipKnobChanged(self, *args: Any, **kwargs: Any) -> Any: ...
