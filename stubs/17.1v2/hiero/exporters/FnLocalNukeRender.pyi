# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import hiero.core.FnExporterBase as _hiero_core_FnExporterBase
import hiero.exporters.FnSubmission as _hiero_exporters_FnSubmission
from hiero.core import nuke as nuke
from hiero.core import util as util
from hiero.exporters.FnSubmission import Submission as Submission
import hiero as hiero

class LocalNukeRenderTask(_hiero_core_FnExporterBase.TaskBase):
    """Task for rendering Nuke scripts locally.

    This is for rendering synchronously, that is taskStep()
    returns True until the render has finished.
    """
    kNukeLicenseErrorReturnCode: int
    def __init__(self, initDict: Any, scriptPath: Any) -> None: ...
    def checkNukeProcessError(self) -> None:
        """Determine if there was a render error, and if so set an appropriate error message
        on the task.
        """
    def finishTask(self) -> None:
        """Clean up after render."""
    def forcedAbort(self) -> None:
        """Abort the Nuke process."""
    def parseErrorFromLog(self) -> str:
        """Parse any errors in the log file and return the result.  If no errors were
        found, will return an empty string.
        """
    def parseProgressOutput(self) -> None:
        """Parse progress from the log file."""
    def progress(self) -> float:
        """Get the render progress."""
    def startTask(self) -> None:
        """Start the Nuke process."""
    def taskStep(self) -> bool:
        """Check the state of the Nuke process.  Returns True while it is running."""

class LocalNukeSubmission(_hiero_exporters_FnSubmission.Submission):
    """Submission for rendering Nuke scripts locally.
    This is the default.
    """
    def __init__(self) -> None: ...
    def addJob(self, jobType: Any, initDict: Any, filePath: Any) -> LocalNukeRenderTask: ...
