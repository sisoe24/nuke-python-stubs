# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtWidgets as _PySide6_QtWidgets
from hiero.ui.nuke_bridge.FnNsFrameServer import isServerRunning as isServerRunning
from hiero.ui.nuke_bridge.FnNsFrameServer import startServer as startServer
from hiero.ui.nuke_bridge.FnNsFrameServer import stopServer as stopServer
import hiero as hiero

FRAMESERVER_DISABLED_ENV: str
FRAMESERVER_DISABLED_ENV_DEFAULT: int
app: _PySide6_QtWidgets.QApplication
isPlayer: bool
runningInGui: bool

def isFrameServerEnabled() -> bool:
    """Check if running the frameserver on startup is enabled. """

def setup() -> Any: ...

def startServerIfEnabled() -> None:
    """Start the Nuke frame server unless it was disabled by the user """
