# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import nukescripts.flipbooking as _nukescripts_flipbooking
from hiero.ui.nuke_bridge.flipbook_common import getColorspaceFromNode as getColorspaceFromNode
from hiero.ui.nuke_bridge.flipbook_common import getIsUsingNukeColorspaces as getIsUsingNukeColorspaces
from hiero.ui.nuke_bridge.flipbook_common import getOCIOConfigPath as getOCIOConfigPath
from hiero.ui.nuke_bridge.flipbook_common import getRawViewerLUT as getRawViewerLUT
from hiero.ui.nuke_bridge.flipbook_common import mapViewerLUTString as mapViewerLUTString
from nukescripts import flipbooking as flipbooking
import hiero as hiero

flipbookManager: PlayerFlipbookManager
kAudioNameKey: str
kAudioPathKey: str
kColorspaceKey: str
kCompNameKey: str
kFilepathKey: str
kFrameRangeKey: str
kNodeNameKey: str
kNukeFlipbookCapabilities: dict
kOcioConfigKey: str
kStartAtKey: str
kViewerLutKey: str
kViewsKey: str

class FlipbookNamer:
    """Helper class to generate names for flipbook objects in the bin. If naming
    information wasn't provided the methods will return None 
    """
    def __init__(self, compName: Any, nodeName: Any, audioName: Any) -> None: ...
    def audioName(self) -> str | None: ...
    def binName(self) -> str: ...
    def sequenceName(self) -> str | None: ...
    def videoName(self) -> str | None: ...

class PlayerFlipbookApplication(_nukescripts_flipbooking.FlipbookApplication):
    """Class which handles launching the flipbook in Hiero Player from Nuke """
    def __init__(self) -> None: ...
    def cacheDir(self) -> Any: ...
    def capabilities(self) -> dict[str, Any]: ...
    def getExtraOptions(self, flipbookDialog: Any, nodeToFlipbook: Any) -> dict[Any, Any]: ...
    def name(self) -> str: ...
    def path(self) -> Any: ...
    def run(self, path: Any, frameRanges: Any, views: Any, options: Any) -> None: ...

class PlayerFlipbookManager:
    """Manage flipbooking on the Hiero Player side. Receives flipbook commands
    from Nuke through the command line and creates projects/clips etc.
    """
    def __init__(self) -> None: ...
    def openFlipbook(self, filepath: Any, frameRange: Any, startAt: Any, ocioConfig: Any, viewerLUT: Any, namer: Any, views: Any, colorspace: Any, audioPath: Any) -> None:
        """Open a flipbook, creating clips, projects etc as needed """

def openFlipbook(data: Any) -> None:
    """Open a flipbook from json data. This can either be raw json, or a path to
    a file containing it
    """
