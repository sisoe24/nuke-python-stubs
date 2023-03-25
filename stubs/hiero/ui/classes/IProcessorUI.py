import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class IProcessorUI(Object):
    """
    IProcessorUI provides a simple interface for our C++ Application to access Python instances of ProcessorUIBase.

    This class should not be used directly; use hiero.ui.ProcessorUIBase instead.
    """

    def __setattr__(self, name, value, ):
        """
        Implement setattr(self, name, value).
        """
        return None

    def __delattr__(self, name, ):
        """
        Implement delattr(self, name).
        """
        return None

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def displayName(self) -> str:
        """
        self.displayName() -> called by Hiero to get the Display name of a task for displaying in UI.

        @return: string
        """
        return str()

    def populateUI(self, processorUIWidget: PySide2.QtWidgets.QWidget, taskUIWidget: PySide2.QtWidgets.QWidget, items: typing.List[core.ItemWrapper]) -> None:
        """
        self.populateUI() -> called by Hiero to allow the IProcessorUI to populate a QWidget with the ui widgets neccessary to reflect the current preset.
        The EditMode is used to instruct the UI generation code to build in ReadOnly mode

        @param processorUIWidget: PySide2.QtGui.QWidget
        @param taskUIWidget: PySide2.QtGui.QWidget
        @param items: [hiero.core.ItemWrapper]
        @param editMode: hiero.core.IProcessorUI.EditMode
        """
        return None

    def preset(self) -> core.ITaskPreset:
        """
        self.preset() -> called by Hiero to get the TaskPreset which this TaskUI is currently reflecting.

        @return: hiero.core.ITaskPreset
        """
        return ITaskPreset()

    def refreshContent(self) -> None:
        """

        """
        return None

    def savePreset(self) -> None:
        """

        """
        return None

    def setPreset(self, preset: core.ITaskPreset) -> None:
        """
        self.setPreset() -> called by Hiero to set the TaskPreset which this TaskUI will reflect.

        @param preset: hiero.core.ITaskPreset
        """
        return None

    def toolTip(self) -> str:
        """
        self.toolTip() -> called by Hiero to get the desciption of a task for displaying in UI as a tooltip.

        @return: string
        """
        return str()

    def validate(self, selection: typing.List[core.ItemWrapper]) -> bool:
        """
        self.validate() -> called by Hiero to get .

        @param: [hiero.core.ItemWrapper]
        @return: bool
        """
        return bool()

    def validateSelection(self, selection: typing.List[core.ItemWrapper]) -> bool:
        """

        """
        return bool()

    def __copy__(self,) -> None:
        """

        """
        return None

    EditMode: Any = None
    ReadOnly: Any = None
    Limited: Any = None
    Full: Any = None
