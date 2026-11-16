# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import hiero.syncreview.synctool as _hiero_syncreview_synctool
from hiero.core import AnimatedAnnotationStroke as AnimatedAnnotationStroke
from hiero.core import Clip as Clip
from hiero.core import Sequence as Sequence
from hiero.core import events as events
from hiero.core.util import asBytes as asBytes
from hiero.core.util import asUnicode as asUnicode
from hiero.syncreview import messages as messages
from hiero.syncreview.synctool import SyncTool as SyncTool
from hiero.syncreview.synctool import localCallback as localCallback
from hiero.syncreview.synctool import remoteCallback as remoteCallback
import hiero as hiero

class SyncAnnotationsTool(_hiero_syncreview_synctool.SyncTool):
    """Tool for syncing annotations in the viewer. This receives callbacks from
    the annotations tool, and syncs them across the session
    """
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, messageDispatcher: Any) -> None: ...
    def onLocalAnnotationAdded(self, annotation: Any) -> None:
        """Local annotation added, send message to remotes to create it there """
    def onLocalAnnotationChange(self, *args: Any, **kwargs: Any) -> Any: ...
    def onLocalAnnotationChanged(self, annotation: Any) -> None:
        """Local annotation edited, send message to remotes to update it there """
    def onLocalAnnotationPaintObjectChange(self, *args: Any, **kwargs: Any) -> Any: ...
    def onLocalAnnotationRemoved(self, annotation: Any, sequence: Any) -> None:
        """Local annotation removed, send message to remotes to remove it there """
    def onRemoteAnimatedStrokeAdded(self, *args: Any, **kwargs: Any) -> Any: ...
    def onRemoteAnnotationAdded(self, *args: Any, **kwargs: Any) -> Any: ...
    def onRemoteAnnotationChanged(self, *args: Any, **kwargs: Any) -> Any: ...
    def onRemoteAnnotationPaintObjectAdded(self, *args: Any, **kwargs: Any) -> Any: ...
    def onRemoteAnnotationPaintObjectChanged(self, *args: Any, **kwargs: Any) -> Any: ...
    def onRemoteAnnotationPaintObjectRemoved(self, *args: Any, **kwargs: Any) -> Any: ...
    def onRemoteAnnotationRemoved(self, *args: Any, **kwargs: Any) -> Any: ...
    def syncVanishingBrushStrokes(self) -> None:
        """Sync animated strokes from the overlay scene (vanishing brush) """
