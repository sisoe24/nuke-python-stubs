# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.core.FnExporterBase as _hiero_core_FnExporterBase
import hiero.exporters.FnLocalNukeRender as _hiero_exporters_FnLocalNukeRender
import hiero.exporters.FnSubmission as _hiero_exporters_FnSubmission
from hiero.core.FnExporterBase import TaskBase as TaskBase
from hiero.exporters.FnLocalNukeRender import LocalNukeRenderTask as LocalNukeRenderTask
from hiero.exporters.FnSubmission import Submission as Submission
import hiero as hiero

class FrameServerRenderTask(_hiero_core_FnExporterBase.TaskBase):
    """Task for rendering Nuke scripts through the frame server. """
    def __init__(self, initDict: Any, scriptPath: Any) -> None: ...
    def cancelRenders(self) -> None:
        """Remove the script from the render queue. """
    def finishTask(self) -> None: ...
    def forcedAbort(self) -> None: ...
    def onFrameRenderError(self, path: Any, frame: Any, nodeName: Any, errorMsg: Any) -> None:
        """Callback when there is an error rendering a frame.  Set the error state
        and cancel. 
        """
    def onFrameRendered(self, path: Any, frame: Any, writeNode: Any) -> None:
        """Callback when a frame is rendered.  If it's for the script being
        rendered, increment the count. 
        """
    def progress(self) -> float: ...
    def startTask(self) -> None: ...
    def taskStep(self) -> bool: ...

class FrameServerSubmission(_hiero_exporters_FnSubmission.Submission):
    """Submission class for rendering an nk script through the frame server.  If
    that is not possible, will fall back to using the LocalNukeRenderTask. 
    """
    def __init__(self) -> None: ...
    def addJob(self, jobType: Any, initDict: Any, filePath: Any) -> FrameServerRenderTask | _hiero_exporters_FnLocalNukeRender.LocalNukeRenderTask: ...
    def canRenderOnFrameServer(self, initDict: Any) -> bool:
        """Check if this render can be done through the frame server.  Currently
        it can't be used to render video formats. 
        """
