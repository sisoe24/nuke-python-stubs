# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.syncreview.synctool as _hiero_syncreview_synctool
from hiero.core import Annotation as Annotation
from hiero.core import Clip as Clip
from hiero.core import Sequence as Sequence
from hiero.core import events as events
from hiero.core.util import asBytes as asBytes
from hiero.core.util import asUnicode as asUnicode
from hiero.syncreview import messages as messages
from hiero.syncreview.log import logMessage as logMessage
from hiero.syncreview.synctool import SyncTool as SyncTool
import hiero as hiero

class SyncAnnotationsTool(_hiero_syncreview_synctool.SyncTool):
    """Tool for syncing annotations in the viewer. This receives callbacks from
    the annotations tool, and syncs them across the session
    """
    staticMetaObject: Any
    def __init__(self, messageDispatcher: Any) -> None: ...
    def onLocalAnnotationAdded(self, annotation: Any) -> None:
        """Local annotation added, send message to remotes to create it there """
    def onLocalAnnotationChange(self, event: Any) -> None:
        """Callback when a local annotation is added/removed/edited """
    def onLocalAnnotationChanged(self, annotation: Any) -> None:
        """Local annotation edited, send message to remotes to create it there """
    def onLocalAnnotationRemoved(self, annotation: Any) -> None:
        """Local annotation removed, send message to remotes to remove it there """
    def onRemoteAnnotationAdded(self, msg: Any) -> None:
        """Handle message to create an annotation """
    def onRemoteAnnotationChanged(self, msg: Any) -> None:
        """Handle message to change an annotation. Note that right now, the whole
        annotation is being rebuilt. This should be ok, there's not a huge amount
        of data being sent, but if necessary we could just send e.g. individual points
        being added to a stroke
        """
    def onRemoteAnnotationRemoved(self, msg: Any) -> None:
        """Handle message to remove an annotation """
