# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.syncreview.synctool as _hiero_syncreview_synctool
from hiero.core.util import asUnicode as asUnicode
from hiero.syncreview import messages as messages
from hiero.syncreview.log import logMessage as logMessage
from hiero.syncreview.synctool import SyncTool as SyncTool
from hiero.syncreview.synctool import localCallback as localCallback
from hiero.syncreview.synctool import remoteCallback as remoteCallback
from hiero.ui import Player as Player
from hiero.ui import TracksMask as TracksMask
from hiero.ui import Viewer as Viewer
import hiero as hiero

class SyncViewerSubTool(_hiero_syncreview_synctool.SyncTool):
    """Base class for sub-tools which implement different parts of the viewer sync
    logic. These are owned and managed by the SyncViewerTool class.
    """
    staticMetaObject: Any
    def __init__(self, syncViewerTool: Any) -> None: ...
    def pushState(self) -> Any:
        """Push the tool state to remotes """
    def viewer(self) -> Any:
        """Get the current viewer """
    def viewerChanged(self, viewer: Any, oldViewer: Any) -> Any:
        """Called when the current viewer changes """

class SyncViewerAnnotationTool(SyncViewerSubTool):
    """Tool for syncing the state of the annotations tool in the viewer. """
    staticMetaObject: Any
    def __init__(self, syncViewerTool: Any) -> None: ...
    def onRemoteAnnotationsToolChanged(self, *args: Any, **kwargs: Any) -> Any: ...
    def pushState(self, *args: Any, **kwargs: Any) -> Any: ...
    def viewerChanged(self, viewer: Any, oldViewer: Any) -> None: ...

class SyncViewerBufferTool(SyncViewerSubTool):
    """Tool for syncing the viewer's A/B buffer options. Sequences are handled by SyncViewerTool. """
    staticMetaObject: Any
    def __init__(self, syncViewerTool: Any) -> None: ...
    def pushState(self, *args: Any, **kwargs: Any) -> Any: ...
    def viewerChanged(self, viewer: Any, oldViewer: Any) -> None:
        """Called when the current viewer changes """

class SyncViewerChannelsTool(SyncViewerSubTool):
    """Tool for syncing the channel setting on the viewer """
    staticMetaObject: Any
    def __init__(self, syncViewerTool: Any) -> None: ...
    def pushState(self, *args: Any, **kwargs: Any) -> Any: ...
    def viewerChanged(self, viewer: Any, oldViewer: Any) -> None: ...

class SyncViewerCompareModeTool(SyncViewerSubTool):
    """Tool for syncing the compare mode of the A/B buffers in the viewer """
    staticMetaObject: Any
    def __init__(self, syncViewerTool: Any) -> None: ...
    def pushState(self, *args: Any, **kwargs: Any) -> Any: ...
    def viewerChanged(self, viewer: Any, oldViewer: Any) -> None: ...

class SyncViewerGainTool(SyncViewerSubTool):
    """Tool for syncing the gain in the viewer """
    staticMetaObject: Any
    def __init__(self, syncViewerTool: Any) -> None: ...
    def pushState(self, *args: Any, **kwargs: Any) -> Any: ...
    def viewerChanged(self, viewer: Any, oldViewer: Any) -> None: ...

class SyncViewerGammaTool(SyncViewerSubTool):
    """Tool for syncing the gamma in the viewer """
    staticMetaObject: Any
    def __init__(self, syncViewerTool: Any) -> None: ...
    def pushState(self, *args: Any, **kwargs: Any) -> Any: ...
    def viewerChanged(self, viewer: Any, oldViewer: Any) -> None: ...

class SyncViewerGuideOverlayTool(SyncViewerSubTool):
    """Logic for syncing the guide overlays within a session. """
    staticMetaObject: Any
    def __init__(self, syncViewerTool: Any) -> None: ...
    def pushState(self, *args: Any, **kwargs: Any) -> Any: ...
    def viewerChanged(self, viewer: Any, oldViewer: Any) -> None: ...

class SyncViewerInOutTool(SyncViewerSubTool):
    """Tool for syncing the 'in' and 'out' points of the viewer. """
    staticMetaObject: Any
    def __init__(self, syncViewerTool: Any) -> None: ...
    def pushState(self) -> None:
        """Push the 'in' and 'out' points of the current viewer. """

class SyncViewerLayerTool(SyncViewerSubTool):
    """Logic for syncing the channels layer state within a session. """
    staticMetaObject: Any
    def __init__(self, syncViewerTool: Any) -> None: ...
    def pushState(self, *args: Any, **kwargs: Any) -> Any: ...
    def viewerChanged(self, viewer: Any, oldViewer: Any) -> None: ...

class SyncViewerLayoutModeTool(SyncViewerSubTool):
    """Tool for syncing the layout mode of the A/B buffers in the viewer """
    staticMetaObject: Any
    def __init__(self, syncViewerTool: Any) -> None: ...
    def pushState(self, *args: Any, **kwargs: Any) -> Any: ...
    def viewerChanged(self, viewer: Any, oldViewer: Any) -> None: ...

class SyncViewerMaskOverlayStyleTool(SyncViewerSubTool):
    """Logic for syncing the mask overlay style within a session. """
    staticMetaObject: Any
    def __init__(self, syncViewerTool: Any) -> None: ...
    def pushState(self, *args: Any, **kwargs: Any) -> Any: ...
    def viewerChanged(self, viewer: Any, oldViewer: Any) -> None: ...

class SyncViewerMaskOverlayTool(SyncViewerSubTool):
    """Logic for syncing the mask overlay within a session. """
    staticMetaObject: Any
    def __init__(self, syncViewerTool: Any) -> None: ...
    def pushState(self, *args: Any, **kwargs: Any) -> Any: ...
    def viewerChanged(self, viewer: Any, oldViewer: Any) -> None: ...

class SyncViewerPlaybackModeTool(SyncViewerSubTool):
    """Tool for syncing the playback mode (bounce/repeat/etc) setting on the viewer """
    staticMetaObject: Any
    def __init__(self, syncViewerTool: Any) -> None: ...
    def pushState(self, *args: Any, **kwargs: Any) -> Any: ...
    def viewerChanged(self, viewer: Any, oldViewer: Any) -> None: ...

class SyncViewerSaturationTool(SyncViewerSubTool):
    """Tool for syncing the saturation in the viewer """
    staticMetaObject: Any
    def __init__(self, syncViewerTool: Any) -> None: ...
    def pushState(self, *args: Any, **kwargs: Any) -> Any: ...
    def viewerChanged(self, viewer: Any, oldViewer: Any) -> None: ...

class SyncViewerTimeDisplayFormatTool(SyncViewerSubTool):
    """Tool for syncing the time display format of the viewer. """
    staticMetaObject: Any
    def __init__(self, syncViewerTool: Any) -> None: ...
    def pushState(self) -> None:
        """Push the zoom state to remote clients. """
    def viewerChanged(self, viewer: Any, oldViewer: Any) -> None:
        """Called when the current viewer changes. """

class SyncViewerTool(_hiero_syncreview_synctool.SyncTool):
    """Logic for a syncing the view within a session.
  
    """
    SYNC_NONE: int
    SYNC_PLAYBACK: int
    SYNC_TIME: int
    staticMetaObject: Any
    def __init__(self, messageDispatcher: Any) -> None: ...
    def pushViewerState(self) -> None:
        """Send the current state of the viewer to other participants. This should
        sync the current sequences, time, etc
        """
    def sendMessage(self, msg: Any) -> None: ...
    def setProjectLoading(self, loading: Any) -> None:
        """Block viewer tool messages the while the project is being loaded to avoid extra callbacks.
        Stop the playback until the project has been loaded.
        """
    def shutdown(self) -> None: ...
    def stopPlayback(self) -> None:
        """Stop the playback on the viewer. This change is not pushed to other participants. """
    def updateCurrentSequences(self) -> bool:
        """Update the current sequence GUIDs cached in the tool.
    
        """

class SyncViewerWipeTool(SyncViewerSubTool):
    """Logic for syncing the wipe tools state within a session. """
    staticMetaObject: Any
    def __init__(self, syncViewerTool: Any) -> None: ...
    def pushState(self, *args: Any, **kwargs: Any) -> Any: ...
    def viewerChanged(self, viewer: Any, oldViewer: Any) -> None:
        """Called when the current viewer changes """

class SyncViewerZoomTool(SyncViewerSubTool):
    """Tool for syncing the zoom mode of the players of the viewer. """
    staticMetaObject: Any
    def __init__(self, syncViewerTool: Any) -> None: ...
    def pushState(self) -> None:
        """Push the zoom state to remote clients. """
    def viewerChanged(self, viewer: Any, oldViewer: Any) -> None:
        """Called when the current viewer changes. """
