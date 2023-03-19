import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class TaskPreset(TaskPresetBase):
    """
    Deprecated - Use TaskPresetBase
    """

    def __init__(self, parentType: Any, presetName: str):
        """
        Initialise Exporter Preset Base Class

        @param parentType: Task type to which this preset object corresponds
        @param presetName: Name of preset
        """
        return None
