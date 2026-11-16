# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from hiero.FnRedirect import findRegisteredAction as findRegisteredAction
from hiero.core import util as util
from hiero.core.FnCompSourceInfo import isNukeScript as isNukeScript
from hiero.exporters import FnFrameServerRender as FnFrameServerRender
from hiero.ui import findMenuAction as findMenuAction
from hiero.ui.nuke_bridge import add_effect as add_effect
from hiero.ui.nuke_bridge import hiero_state as hiero_state
from hiero.ui.nuke_bridge import initFrameServer as initFrameServer
import hiero as hiero
import nukescripts as nukescripts

addEffectHandler: Any
eventHandler: Any
hieroState: Any
isPlayer: bool
localisation: Any
timelineAction: Any

class HieroEventHandler:
    def __init__(self) -> None: ...
    def getNukeScriptPathFromItem(self, item: Any) -> Any:
        """Extract the path from the given item, and check if it points to a Nuke script.
        Returns None if no path was found or if it wasn't a Nuke script. 
        """
    def onDoubleClick(self, event: Any) -> None: ...
    def openNuke(self, filePath: Any) -> None:
        """Open a script in new Nuke process
        The caller should make sure the filePath is actually a valid Nuke script. 
        """

class OpenInNukeAction:
    staticMetaObject: Any
    def __init__(self, hieroEventHandler: Any) -> None: ...
    def doOpen(self) -> None: ...
    def eventHandler(self, event: Any) -> None: ...

def setup() -> None: ...
