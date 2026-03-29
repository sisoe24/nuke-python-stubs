"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import ui
import core
import nuke
import hiero
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class TaskGroup(ITask):
    """
    TaskGroup is a Task which maintains a list of child Tasks.
    """

    def __init__(self) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def addChild(self, child: Task) -> None:
        """
        Add a child to the list.
        """
        ...

    def children(self) -> list[Task]:
        """
        Get the TaskGroup's children.
        """
        ...

    def getLeafTasks(self) -> list[Task]:
        """
        Get a list of all leaf tasks recursively, i.e. those with no child tasks.
        """
        ...

    def addToQueue(self) -> None:
        """
        self.addToQueue() -> adds this task into the task queue.
        """
        ...

    def progress(self) -> float:
        """
        Get the group progress.  Returns a value based on the progress of child tasks.
        """
        ...
