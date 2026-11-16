# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.ui as _hiero_ui
import hiero as hiero

taskUIRegistry: TaskUIRegistry

class TaskUIRegistry(_hiero_ui.IExporterUIRegistry):
    """Registry/factory for ITaskUI and IProcessorUI objects. """
    def __init__(self) -> None: ...
    def getNewTaskUIForPreset(self, preset: Any) -> Any:
        """Get a new instance of the task UI class for the preset. """
    def getProcessorUI(self, index: Any) -> Any:
        """Return ProcessorUI registered at specified index """
    def getProcessorUIForPreset(self, preset: Any) -> None:
        """Return ProcessorUI object associated with the preset type.  Note that
        this returns a stored instance of the preset. 
        """
    def getTaskUI(self, index: Any) -> Any:
        """Return TaskUI registered at specified index """
    def getTaskUIForPreset(self, preset: Any) -> None:
        """Return TaskUI object associated with the preset type.  Note that this
        returns a stored instance of the preset, which is suitable for calling
        from C++ code.  For actually constructing UIs, getNewTaskUIForPreset()
        should be called to create a new object.
        """
    def numProcessorUIs(self) -> int:
        """Get the number of registered IProcessorUI classes. """
    def numTaskUIs(self) -> int:
        """Get the number of registered ITaskUI classes. """
    def processorUIByIndex(self, index: Any) -> Any:
        """Return ProcessorUI registered at specified index"""
    def registerProcessorUI(self, processorPreset: Any, processorUI: Any) -> None:
        """Register IProcessorUI class and associate with IProcessorPreset class """
    def registerTaskUI(self, taskPreset: Any, taskUI: Any) -> None:
        """Register an ITaskUI class and associate with an ITaskPreset class """
