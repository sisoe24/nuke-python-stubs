import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class ITask(object):
    """
    ITask provides a simple interface for our C++ Application to access Python instances of TaskBase.

    This class should not be used directly; use hiero.core.TaskBase instead.
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __setattr__(self, name, value, ) -> None:
        """
        Implement setattr(self, name, value).
        """
        ...

    def __delattr__(self, name, ) -> None:
        """
        Implement delattr(self, name).
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def addToQueue(self) -> None:
        """
        self.addToQueue() -> adds this task into the task queue.
        """
        ...

    def children(self) -> typing.List[core.ITask]:
        """
        self.children() -> get a list of child tasks.  Note that this list should not change after addToQueue() has been called.
        """
        ...

    def clearError(self) -> None:
        """
        self.clearError() -> clears the error or warning string for this task.
        """
        ...

    def destinationDescription(self) -> str:
        """
        self.destinationDescription() -> Get the destination description.
        """
        ...

    def error(self) -> str:
        """
        self.error() -> Get the error string if one has been set.
        """
        ...

    def finishTask(self) -> None:
        """
        self.finishTask() -> called by Hiero to tell the Task to that it's finished. Subclasses should finish processing in their override of this method (close files, clean up).
        """
        ...

    def forcedAbort(self) -> None:
        """
        self.forcedAbort() -> called by Hiero when the user presses the Abort button. Subclasses should do any clean up in their override of this method.
        """
        ...

    def formatDescription(self) -> str:
        """
        self.formatDescription() -> Get a description of the format that this task writes to.
        """
        ...

    def getExportDuration(self) -> float:
        """
        self.getExportDuration() -> Return the time this task took to export in milliseconds. Will return 0 until the task has finished exporting.
        """
        ...

    def ident(self) -> str:
        """
        self.ident() -> called by Hiero to get a unique identifier for this task.
        """
        ...

    def progress(self) -> float:
        """
        self.progress() -> called by Hiero to find out from the task what it's progress is, between 0.0 and 1.0.
        """
        ...

    def setDestinationDescription(self, desc: str) -> None:
        """
        self.setDestinationDescription(desc) ->

        @param desc: string
        """
        ...

    def setDuplicate(self) -> None:
        """
        self.setDuplicate() -> Sets the flag cancelling this task and marking as duplicate.
        """
        ...

    def setError(self, desc: str) -> None:
        """
        self.setError(desc) -> sets the error string displayed to the user in the task dialog. Error strings display in red.

        @param desc: the text to display
        """
        ...

    def setExportDuration(self, duration: float) -> None:
        """
        For internal use only. Do not use.
        """
        ...

    def setFormatDescription(self, desc: str) -> None:
        """
        self.setFormatDescription(desc) -> tells Hiero a description of the format that this task writes to.

        @param desc: description of the format that this task outputs
        """
        ...

    def setSynchronous(self) -> None:
        """
        self.setSynchronous() -> Flags this task as synchronous. When added to the queue, this task will be executed imediately on the current thread. The Flag must be set prior to adding to queue
        """
        ...

    def setTaskDescription(self, desc: str) -> None:
        """
        self.setTaskDescription(description) -> tells Hiero a descriptive string for the task that it can use to show the user through the user interface and/or store it for reference. Helpful when debugging.

        @param desc: description of the task
        """
        ...

    def setWarning(self, desc: str) -> None:
        """
        self.setWarning(desc) -> sets the warning string displayed to the user in the task dialog. Warning strings display in orange.

        @param desc: the text to display
        """
        ...

    def startTask(self) -> None:
        """
        self.startTask() -> called by Hiero to tell the Task to start. Subclasses should start processing in their override of this method.
        """
        ...

    def synchronous(self) -> bool:
        """
        self.synchronous() -> Returns the state of the Synchronous flag. If True, wheb added to the queue, this task will be executed imediately on the current thread.
        """
        ...

    def taskDescription(self) -> str:
        """
        self.taskDescription() -> Get a description of the task.
        """
        ...

    def taskStep(self) -> bool:
        """
        self.taskStep() -> called by Hiero repeatedly until the progress method returns 1.0 or greater. Step based processing should occur in this method by subclasses of Task.
        """
        ...
