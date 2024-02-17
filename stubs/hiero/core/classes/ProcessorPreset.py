"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import ui
import core
import hiero
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class ProcessorPreset(TaskPresetBase):
    """
    ProcessorPreset is the base class from which all Processor Presets must derrive
    The purpose of a Processor Preset is to store and data which must be serialized to file
    and shared between the Processor and ProcessorUI user interface component
    """

    def __init__(self, parentType, presetName) -> None:
        """
        Initialise Exporter Preset Base Class

        @param parentType: Processor type to which this preset object corresponds
        @param presetName: Name of preset
        """
        ...

    def __eq__(self, other) -> None:
        """
        Override to compare projects.  The TaskRegistry relies on presets which are otherwise identical but with different projects not comparing equal.
        """
        ...

    __hash__: Any = None
