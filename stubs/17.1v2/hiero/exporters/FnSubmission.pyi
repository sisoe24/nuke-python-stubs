# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import hiero.core.FnExporterBase as _hiero_core_FnExporterBase
from hiero.core.FnExporterBase import TaskGroup as TaskGroup

class Submission(_hiero_core_FnExporterBase.TaskGroup):
    """The Submission class is used for sending jobs such as renders to
    external processes.

    Tasks which need to start a job call addJob(), and the Submission may
    optionally return a Task to report on the job's progress.
    """
    kCommandLine: str
    kNukeRender: str
    def __init__(self) -> None: ...
    def addJob(self, jobType: Any, initDict: Any, filePath: Any) -> Any:
        """Add a job to the submission.  May return a Task object which should be processed
        by the caller.
        """
    def finishTask(self) -> Any:
        """This will be called after jobs have been added."""
    def initialise(self) -> Any:
        """Called before any jobs are added, can be used to e.g. show a dialog
        to configure the Submission.
        """
    def startTask(self) -> Any:
        """This will be called when the export queue starts processing this submission,
        before any jobs are added.
        """
    def taskStep(self) -> bool: ...
