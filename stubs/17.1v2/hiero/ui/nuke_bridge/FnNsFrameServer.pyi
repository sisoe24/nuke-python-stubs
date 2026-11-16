# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import hiero.core as _hiero_core
from nuke_internal.executeInMain import executeInMainThread as executeInMainThread
import hiero as hiero

backgroundRenderObserver: _hiero_core.BackgroundRenderObserver
backgroundRenderer: Any
frameServer: Any
renderProgressObserver: _hiero_core.RenderProgressObserver

def addBackgroundRenderObserver(observer: Any) -> None: ...

def cancelFrames(scriptPath: Any, nodeName: str = ...) -> None:
    """Cancel background render of all the frames for the given script. """

def configureFrameServerFromCommandArgs() -> None:
    """Check for the --frameserverloglevel command line argument for setting the
    frame server log level.  Note that this can't be done on module import because
    hiero.core.rawArgs is not available until afterwards. 
    """

def isServerRunning(timeout: Any = ...) -> bool:
    """Test if the Nuke frame server is running.  This is done by sending a message to it
    and waiting for a response.  Returns false if no reply was received within timeout seconds.
    @param timeout: time in seconds to wait for a response.  Defaults to 1 
    """

def onError(message: Any) -> None:
    """A callback which gets called when the framserver encounters a non-fatal error."""

def onFatalError(exitcode: Any) -> None:
    """A callback which gets called when frameserver encounters a fatal error.
    It returns a known exit code which indicates the reason for the fatal failure.

    This will get called from some random thread, so take care calling UI.
    """

def postProcessScript(scriptPath: Any) -> None:
    """Send a command to post-process the Nuke script to the post processor."""

def promptFrameServerKill(port: Any) -> None: ...

def removeBackgroundRenderObserver(observer: Any) -> None: ...

def renderFrames(scriptPath: Any, frameRanges: Any, writeNode: Any, views: Any) -> None:
    """Queue background render of a range of frames for a script. """

def renderScript(scriptName: Any) -> None:
    """Queue background render of all the frames for a script. """

def setBackgroundRenderer(renderer: Any) -> None:
    """Set the background renderer instance to be used for rendering. """

def startServer() -> None:
    """Start the Nuke frame server. """

def stopServer(event: Any) -> None:
    """Handle shutdown event to stop the frame server. """

def workerCount() -> int: ...
