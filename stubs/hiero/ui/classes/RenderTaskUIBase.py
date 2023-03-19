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

    def __init__(self, taskType, preset, displayName):
        """
        A task base that includes functionality for displaying output selection UI.
        """
        return None

    def codecTypeComboBoxChanged(self, value):
        """

        """
        return None

    def updateChannelsForFileType(self, fileType):
        """

        """
        return None

    def propertyChanged(self):
        """

        """
        return None

    def reformatChanged(self):
        """
        Callback when the Reformat combo box selection has changed. Enable/disable
        the reformat property widgets as appropriate.
        """
        return None

    def formatChanged(self):
        """

        """
        return None

    def setFormat(self, format):
        """

        """
        return None

    def deleteFirstChildFromWidget(self, widget):
        """
        Get the first child added to the widget's layout, and delete it, if it exists.
        """
        return None

    def updateCodecPropertiesWidget(self, file_type):
        """
        Update the codec properties widget. If applicable, also updates the encoder properties (for movs).
        """
        return None

    def _buildCodecWidget(self, file_type):
        """
        Create the codec properties widget.
        """
        return None

    def createCodecPropertyWidgets(self, file_type, propertyDictionaries):
        """
        Create widgets for the given property dictionaries, and add them to the given layout.
        """
        return None

    def _getLutOptions(self):
        """
        Return the LUT options to use.
        """
        return None

    def buildCodecUI(self, layout, itemTaskType):
        """
        Populate layout with widgets reflected from the RenderPresetBase class
        """
        return None

    def createChannelsWidget(self, layout):
        """

        """
        return None

    def createColourSpaceWidget(self, layout):
        """

        """
        return None

    def createViewsWidget(self, layout):
        """

        """
        return None

    def createFileTypeWidget(self, layout):
        """

        """
        return None

    def createCodecOptionsPlaceholder(self, layout):
        """

        """
        return None

    def createReformatWidgets(self, layout, itemTaskType):
        """

        """
        return None

    staticMetaObject: Any = None
