import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class TaskGroup(ITask):
    """
    TaskGroup is a Task which maintains a list of child Tasks.
    """

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def addChild(self, child):
        """
        Add a child to the list.
        """
        return None

    def children(self):
        """
        Get the TaskGroup's children.
        """
        return None

    def getLeafTasks(self):
        """
        Get a list of all leaf tasks recursively, i.e. those with no child tasks.
        """
        return None

    def addToQueue(self):
        """
        self.addToQueue() -> adds this task into the task queue.
        """
        return None

    def progress(self):
        """
        Get the group progress.  Returns a value based on the progress of child tasks.
        """
        return None
