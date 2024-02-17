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


class RenderTaskPreset(TaskPresetBase):
    """
    RenderTaskPreset is a specialization of the TaskPreset which contains parameters
    associated with generating Nuke render output.
    """

    def AllViews(self,) -> None:
        """
        Get the special cased value for all on the views knob
        """
        ...

    def __init__(self, taskType, name, properties) -> None:
        """
        Initialise presets to default values
        """
        ...

    def _setCodecSettings(self, codecType, extension, fullname, isVideo, properties) -> None:
        """
        Build dictionary of format settings.
        """
        ...

    def _getCodecSettingsDefault(self, codecType, codecKey) -> None:
        """
        Search codec settings for a matching codecKey and return a default value.

        @param codecType - format identifier (mov, dpx, jpeg etc..)

        @param codecKey - codec settings key
        """
        ...

    def addCustomResolveEntries(self, resolver: ResolveTable) -> None:
        """
        addCustomResolveEntries(self, resolver)
        RenderTaskPreset adds specialized tokens specific to this type of export, such as {ext} which returns the output format extension.

        @param resolver: ResolveTable object
        """
        ...

    def summary(self) -> None:
        """
        Called by Hiero to get a summary of the preset settings as a string.
        """
        ...

    def extension(self) -> None:
        """

        """
        ...

    def codecName(self) -> None:
        """

        """
        ...

    def codecProperties(self) -> None:
        """

        """
        ...

    def codecSettings(self) -> None:
        """

        """
        ...
