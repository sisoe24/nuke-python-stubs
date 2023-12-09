import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class FolderTask(TaskBase):
    """
    Task which just creates an empty folder.
    """

    def __init__(self, initDict) -> None:
        """
        __init__(self, initDictionary)
        Initialise TaskBase Class

        @param initDictionary: a TaskData dictionary which seeds the task with all initialization data
        """
        ...
