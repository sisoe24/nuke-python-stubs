"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import ui
import core
import nuke
import hiero
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class IProcessorUI:
    """
    IProcessorUI provides a simple interface for our C++ Application to access Python instances of ProcessorUIBase.

    This class should not be used directly; use hiero.ui.ProcessorUIBase instead.
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

    def populateUI(self, processorUIWidget: PySide2.QtWidgets.QWidget, taskUIWidget: PySide2.QtWidgets.QWidget, items: typing.List[core.ItemWrapper]) -> None:
        """
        self.populateUI() -> called by Hiero to allow the IProcessorUI to populate a QWidget with the ui widgets neccessary to reflect the current preset.
        The EditMode is used to instruct the UI generation code to build in ReadOnly mode

        @param processorUIWidget: PySide2.QtGui.QWidget
        @param taskUIWidget: PySide2.QtGui.QWidget
        @param items: [hiero.core.ItemWrapper]
        @param editMode: hiero.core.IProcessorUI.EditMode
        """
        ...

    def preset(self) -> hiero.core.ITaskPreset:
        """
        self.preset() -> called by Hiero to get the TaskPreset which this TaskUI is currently reflecting.

        @return: hiero.core.ITaskPreset
        """
        ...

    def refreshContent(self) -> None:
        """

        """
        ...

    def savePreset(self) -> None:
        """

        """
        ...

    def setPreset(self, preset: hiero.core.ITaskPreset) -> None:
        """
        self.setPreset() -> called by Hiero to set the TaskPreset which this TaskUI will reflect.

        @param preset: hiero.core.ITaskPreset
        """
        ...

    def toolTip(self) -> str:
        """
        self.toolTip() -> called by Hiero to get the desciption of a task for displaying in UI as a tooltip.

        @return: string
        """
        ...

    def validate(self, selection: typing.List[core.ItemWrapper]) -> bool:
        """
        self.validate() -> called by Hiero to get .

        @param: [hiero.core.ItemWrapper]
        @return: bool
        """
        ...

    def validateSelection(self, selection: typing.List[core.ItemWrapper]) -> bool:
        """

        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...

    EditMode: Any = None
    ReadOnly: Any = None
    Limited: Any = None
    Full: Any = None
