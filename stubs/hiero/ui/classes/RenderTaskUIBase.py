import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class RenderTaskUIBase(TaskUIBase):
    """
    RenderTaskUIBase is a specialization of TaskUIBase which reflects the codec properties in RenderTaskPreset into UI
    """

    def __init__(self, taskType, preset, displayName) -> None:
        """
        A task base that includes functionality for displaying output selection UI.
        """
        ...

    def codecTypeComboBoxChanged(self, value) -> None:
        """

        """
        ...

    def updateChannelsForFileType(self, fileType) -> None:
        """

        """
        ...

    def propertyChanged(self) -> None:
        """

        """
        ...

    def reformatChanged(self) -> None:
        """
        Callback when the Reformat combo box selection has changed. Enable/disable
        the reformat property widgets as appropriate.
        """
        ...

    def formatChanged(self) -> None:
        """

        """
        ...

    def setFormat(self, format) -> None:
        """

        """
        ...

    def deleteFirstChildFromWidget(self, widget) -> None:
        """
        Get the first child added to the widget's layout, and delete it, if it exists.
        """
        ...

    def updateCodecPropertiesWidget(self, file_type) -> None:
        """
        Update the codec properties widget. If applicable, also updates the encoder properties (for movs).
        """
        ...

    def _buildCodecWidget(self, file_type) -> None:
        """
        Create the codec properties widget.
        """
        ...

    def createCodecPropertyWidgets(self, file_type, propertyDictionaries) -> None:
        """
        Create widgets for the given property dictionaries, and add them to the given layout.
        """
        ...

    def _getLutOptions(self) -> None:
        """
        Return the LUT options to use.
        """
        ...

    def buildCodecUI(self, layout, itemTaskType) -> None:
        """
        Populate layout with widgets reflected from the RenderPresetBase class
        """
        ...

    def createChannelsWidget(self, layout) -> None:
        """

        """
        ...

    def createColourSpaceWidget(self, layout) -> None:
        """

        """
        ...

    def createViewsWidget(self, layout) -> None:
        """

        """
        ...

    def createFileTypeWidget(self, layout) -> None:
        """

        """
        ...

    def createCodecOptionsPlaceholder(self, layout) -> None:
        """

        """
        ...

    def createReformatWidgets(self, layout, itemTaskType) -> None:
        """

        """
        ...

    staticMetaObject: Any = None
