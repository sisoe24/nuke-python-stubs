# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
from hiero.ui.nuke_bridge import FnNsFrameServer as FnNsFrameServer
import hiero as hiero

exeDir: str
nukePath: str
pathRemaps: list
postProcessServer: Any
scriptPath: str

def postProcessScript(scriptPath: Any) -> str | None:
    """Send a command to post-process the Nuke script to the post processor. If
    an error occurs, returns a string containing an error message, otherwise
    returns None.
    """

def stopServer(event: Any) -> None: ...
