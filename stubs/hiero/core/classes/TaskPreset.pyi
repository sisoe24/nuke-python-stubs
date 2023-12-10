import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *

class TaskPreset(TaskPresetBase):
    """
    Deprecated - Use TaskPresetBase
    """
    def __init__(self, parentType, presetName:str) -> None:
        """
        Initialise Exporter Preset Base Class

        @param parentType: Task type to which this preset object corresponds
        @param presetName: Name of preset
        """
        ...
