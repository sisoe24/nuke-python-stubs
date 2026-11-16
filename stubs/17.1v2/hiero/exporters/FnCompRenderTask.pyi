# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import hiero.core.FnExporterBase as _hiero_core_FnExporterBase
from hiero.core.FnCompSourceInfo import CompSourceInfo as CompSourceInfo
from hiero.core.FnExporterBase import TaskBase as TaskBase
from hiero.core.FnExporterBase import TaskData as TaskData
from hiero.core.FnExporterBase import TaskGroup as TaskGroup
from hiero.core.FnExporterBase import TaskPresetBase as TaskPresetBase
from hiero.exporters.FnSubmission import Submission as Submission

class CompRenderTask(_hiero_core_FnExporterBase.TaskBase):
    """Task for rendering a comp.  This is just a wrapper which creates the actual render task
    through the submission. 
    """
    def __init__(self, initDict: Any, compToRender: Any) -> None: ...
    def checkError(self) -> None: ...
    def finishTask(self) -> None: ...
    def forcedAbort(self) -> None: ...
    def progress(self) -> Any: ...
    def startTask(self) -> None: ...
    def taskStep(self) -> Any: ...

class CompRenderTaskPreset(_hiero_core_FnExporterBase.TaskPresetBase):
    """Preset for CompRenderTask.  This is only needed
    so the keepNukeScript parameter gets passed through to the
    render tasks generated from the submission. 
    """
    def __init__(self) -> None: ...

def createCompRenderTasks(processor: Any, project: Any) -> None:
    """Generate Comp render tasks for the given processor. """
