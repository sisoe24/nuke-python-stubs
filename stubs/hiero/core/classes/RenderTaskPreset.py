import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class RenderTaskPreset(TaskPresetBase):
    """
    RenderTaskPreset is a specialization of the TaskPreset which contains parameters
    associated with generating Nuke render output.
    """

    def AllViews(self, *args, **kwargs) -> Any:
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, ...):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
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
