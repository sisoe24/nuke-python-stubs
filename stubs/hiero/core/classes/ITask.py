import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class ITask(Object):
    """
    ITask provides a simple interface for our C++ Application to access Python instances of TaskBase.

    This class should not be used directly; use hiero.core.TaskBase instead.
    """

    def __setattr__(self, name, value, ):
        """
        Implement setattr(self, name, value).
        """
        return None

    def __delattr__(self, name, ):
        """
        Implement delattr(self, name).
        """
        return None

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def addToQueue(self) -> None:
        """
        self.addToQueue() -> adds this task into the task queue.
        """
        return None

    def children(self) -> typing.List[core.ITask]:
        """
        self.children() -> get a list of child tasks.  Note that this list should not change after addToQueue() has been called.
        """
        return list()

    def clearError(self) -> None:
        """
        self.clearError() -> clears the error or warning string for this task.
        """
        return None

    def destinationDescription(self) -> str:
        """
        self.destinationDescription() -> Get the destination description.
        """
        return str()

    def error(self) -> str:
        """
        self.error() -> Get the error string if one has been set.
        """
        return str()

    def finishTask(self) -> None:
        """
        self.finishTask() -> called by Hiero to tell the Task to that it's finished. Subclasses should finish processing in their override of this method (close files, clean up).
        """
        return None

    def forcedAbort(self) -> None:
        """
        self.forcedAbort() -> called by Hiero when the user presses the Abort button. Subclasses should do any clean up in their override of this method.
        """
        return None

    def formatDescription(self) -> str:
        """
        self.formatDescription() -> Get a description of the format that this task writes to.
        """
        return str()

    def getExportDuration(self) -> float:
        """
        self.getExportDuration() -> Return the time this task took to export in milliseconds. Will return 0 until the task has finished exporting.
        """
        return float()

    def ident(self) -> str:
        """
        self.ident() -> called by Hiero to get a unique identifier for this task.
        """
        return str()

    def progress(self) -> float:
        """
        self.progress() -> called by Hiero to find out from the task what it's progress is, between 0.0 and 1.0.
        """
        return float()

    def setDestinationDescription(self, desc: str) -> None:
        """
        self.setDestinationDescription(desc) ->

        @param desc: string
        """
        return None

    def setDuplicate(self) -> None:
        """
        self.setDuplicate() -> Sets the flag cancelling this task and marking as duplicate.
        """
        return None

    def setError(self, desc: str) -> None:
        """
        self.setError(desc) -> sets the error string displayed to the user in the task dialog. Error strings display in red.

        @param desc: the text to display
        """
        return None

    def setExportDuration(self, duration: float) -> None:
        """
        For internal use only. Do not use.
        """
        return None

    def setFormatDescription(self, desc: str) -> None:
        """
        self.setFormatDescription(desc) -> tells Hiero a description of the format that this task writes to.

        @param desc: description of the format that this task outputs
        """
        return None

    def setSynchronous(self) -> None:
        """
        self.setSynchronous() -> Flags this task as synchronous. When added to the queue, this task will be executed imediately on the current thread. The Flag must be set prior to adding to queue
        """
        return None

    def setTaskDescription(self, desc: str) -> None:
        """
        self.setTaskDescription(description) -> tells Hiero a descriptive string for the task that it can use to show the user through the user interface and/or store it for reference. Helpful when debugging.

        @param desc: description of the task
        """
        return None

    def setWarning(self, desc: str) -> None:
        """
        self.setWarning(desc) -> sets the warning string displayed to the user in the task dialog. Warning strings display in orange.

        @param desc: the text to display
        """
        return None

    def startTask(self) -> None:
        """
        self.startTask() -> called by Hiero to tell the Task to start. Subclasses should start processing in their override of this method.
        """
        return None

    def synchronous(self) -> bool:
        """
        self.synchronous() -> Returns the state of the Synchronous flag. If True, wheb added to the queue, this task will be executed imediately on the current thread.
        """
        return bool()

    def taskDescription(self) -> str:
        """
        self.taskDescription() -> Get a description of the task.
        """
        return str()

    def taskStep(self) -> bool:
        """
        self.taskStep() -> called by Hiero repeatedly until the progress method returns 1.0 or greater. Step based processing should occur in this method by subclasses of Task.
        """
        return bool()
