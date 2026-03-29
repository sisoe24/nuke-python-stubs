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


class TaskUIRegistry(IExporterUIRegistry):
    """
    Registry/factory for ITaskUI and IProcessorUI objects.
    """

    def __init__(self) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def registerTaskUI(self, taskPreset, taskUI) -> None:
        """
        Register an ITaskUI class and associate with an ITaskPreset class
        """
        ...

    def registerProcessorUI(self, processorPreset, processorUI) -> None:
        """
        Register IProcessorUI class and associate with IProcessorPreset class
        """
        ...

    def numTaskUIs(self) -> int:
        """
        Get the number of registered ITaskUI classes.
        """
        ...

    def numProcessorUIs(self) -> int:
        """
        Get the number of registered IProcessorUI classes.
        """
        ...

    def getTaskUI(self, index: int) -> 'TaskUI':
        """
        Return TaskUI registered at specified index
        """
        ...

    def getProcessorUI(self, index: int) -> 'ProcessorUI':
        """
        Return ProcessorUI registered at specified index
        """
        ...

    def processorUIByIndex(self, index: int) -> 'ProcessorUI':
        """
        Return ProcessorUI registered at specified index
        """
        ...

    def getTaskUIForPreset(self, preset: 'ITaskPreset') -> 'TaskUI':
        """
        Return TaskUI object associated with the preset type.  Note that this
        returns a stored instance of the preset, which is suitable for calling
        from C++ code.  For actually constructing UIs, getNewTaskUIForPreset()
        should be called to create a new object.
        """
        ...

    def getNewTaskUIForPreset(self, preset: 'ITaskPreset') -> 'TaskUI':
        """
        Get a new instance of the task UI class for the preset.
        """
        ...

    def getProcessorUIForPreset(self, preset: 'IProcessorPreset') -> 'ProcessorUI':
        """
        Return ProcessorUI object associated with the preset type.  Note that
        this returns a stored instance of the preset.
        """
        ...
