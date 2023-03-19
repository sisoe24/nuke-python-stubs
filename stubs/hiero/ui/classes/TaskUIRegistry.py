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

    def __init__(self):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def registerTaskUI(self, taskPreset, taskUI):
        """
        Register an ITaskUI class and associate with an ITaskPreset class
        """
        return None

    def registerProcessorUI(self, processorPreset, processorUI):
        """
        Register IProcessorUI class and associate with IProcessorPreset class
        """
        return None

    def numTaskUIs(self):
        """
        Get the number of registered ITaskUI classes.
        """
        return None

    def numProcessorUIs(self):
        """
        Get the number of registered IProcessorUI classes.
        """
        return None

    def getTaskUI(self, index):
        """
        Return TaskUI registered at specified index
        """
        return None

    def getProcessorUI(self, index):
        """
        Return ProcessorUI registered at specified index
        """
        return None

    def processorUIByIndex(self, index):
        """
        Return ProcessorUI registered at specified index
        """
        return None

    def getTaskUIForPreset(self, preset):
        """
        Return TaskUI object associated with the preset type.  Note that this
        returns a stored instance of the preset, which is suitable for calling
        from C++ code.  For actually constructing UIs, getNewTaskUIForPreset()
        should be called to create a new object.
        """
        return None

    def getNewTaskUIForPreset(self, preset):
        """
        Get a new instance of the task UI class for the preset.
        """
        return None

    def getProcessorUIForPreset(self, preset):
        """
        Return ProcessorUI object associated with the preset type.  Note that
        this returns a stored instance of the preset.
        """
        return None
