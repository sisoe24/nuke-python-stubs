# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import hiero.core.FnExporterBase as _hiero_core_FnExporterBase
from hiero.core import util as util
from hiero.core.FnExporterBase import TaskPresetBase as TaskPresetBase
from hiero.core.FnFloatRange import IntRange as IntRange

class ProcessorBase:
    """ProcessorBase is the base class from which all Processors should derive.
    The Processor object is responible for taking the object selection and spawning
    Tasks with the appropriate parameters.
    """
    def __init__(self, preset: Any, submission: Any, synchronous: bool = ...) -> None: ...
    def errors(self) -> str | None:
        """Get an error string from the processor.  Iterates over child tasks and
        adds their error messages to the string.  Returns None if there were no errors. 
        """
    def processTaskPreQueue(self) -> None:
        """processTaskPreQueue() Walk Tasks in submission and mark any duplicates.
        
        """
    def skipOffline(self) -> Any: ...
    def startProcessing(self, exportItems: Any, preview: bool = ...) -> Any:
        """Generate export tasks and add them to the export queue. If preview is
        True, the tasks are created and returned, but not scheduled for execution.
        """
    def validItem(self, supportedTypes: Any, item: Any) -> bool:
        """Get if the task is able to run on the item it was initialised with."""

class ProcessorPreset(_hiero_core_FnExporterBase.TaskPresetBase):
    """ProcessorPreset is the base class from which all Processor Presets must derrive
    The purpose of a Processor Preset is to store and data which must be serialized to file
    and shared between the Processor and ProcessorUI user interface component
    """
    def __eq__(self, other: Any) -> bool:
        """Override to compare projects.  The TaskRegistry relies on presets which are otherwise identical but with different projects not comparing equal. """
    def __init__(self, parentType: Any, presetName: Any) -> None:
        """Initialise Exporter Preset Base Class

        @param parentType: Processor type to which this preset object corresponds
        @param presetName: Name of preset
        """
