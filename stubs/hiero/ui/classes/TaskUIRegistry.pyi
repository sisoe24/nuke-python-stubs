import typing
from typing import *
from numbers import Number

import ui
import core
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

    def numTaskUIs(self) -> None:
        """
        Get the number of registered ITaskUI classes.
        """
        ...

    def numProcessorUIs(self) -> None:
        """
        Get the number of registered IProcessorUI classes.
        """
        ...

    def getTaskUI(self, index) -> None:
        """
        Return TaskUI registered at specified index
        """
        ...

    def getProcessorUI(self, index) -> None:
        """
        Return ProcessorUI registered at specified index
        """
        ...

    def processorUIByIndex(self, index) -> None:
        """
        Return ProcessorUI registered at specified index
        """
        ...

    def getTaskUIForPreset(self, preset) -> None:
        """
        Return TaskUI object associated with the preset type.  Note that this
        returns a stored instance of the preset, which is suitable for calling
        from C++ code.  For actually constructing UIs, getNewTaskUIForPreset()
        should be called to create a new object.
        """
        ...

    def getNewTaskUIForPreset(self, preset) -> None:
        """
        Get a new instance of the task UI class for the preset.
        """
        ...

    def getProcessorUIForPreset(self, preset) -> None:
        """
        Return ProcessorUI object associated with the preset type.  Note that
        this returns a stored instance of the preset.
        """
        ...
