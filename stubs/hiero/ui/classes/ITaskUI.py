import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class ITaskUI(Object):
    """
    ITaskUI provides a simple interface for our C++ Application to access Python instances of TaskUIBase.

    This class should not be used directly; use hiero.ui.TaskUIBase instead.
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __setattr__(self, name, value, ) -> None:
        """
        Implement setattr(self, name, value).
        """
        ...

    def __delattr__(self, name, ) -> None:
        """
        Implement delattr(self, name).
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def displayName(self) -> str:
        """
        self.displayName() -> called by Hiero to get the Display name of a task for displaying in UI.

        @return: string
        """
        ...

    def ident(self) -> str:
        """
        self.ident() -> called by Hiero to get a unique identifier linking this TaskUI with a Task and TaskPreset.

        @return: string
        """
        ...

    def populateUI(self, widget: PySide2.QtWidgets.QWidget, exportTemplate: core.IExportStructure) -> None:
        """
        self.populateUI() -> called by Hiero to allow the TaskUI to populate a QWidget with the ui widgets neccessary to reflect the current preset.

        @param widget: PySide2.QtGui.QWidget
        @param exportTemplate: hiero.core.IExportStructure
        """
        ...

    def preset(self) -> core.ITaskPreset:
        """
        self.preset() -> called by Hiero to get the TaskPreset which this TaskUI is currently reflecting.

        @return: hiero.core.ITaskPreset
        """
        ...

    def setPreset(self, preset: core.ITaskPreset) -> None:
        """
        self.setPreset() -> called by Hiero to set the TaskPreset which this TaskUI will reflect.

        @param preset: hiero.core.ITaskPreset
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...
