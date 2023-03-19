import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class TaskUIBase(ITaskUI):
    """
    TaskUIBase is the base class from hich all TaskUI components should derrive
    """
    propertiesChanged = Signal()

    def __init__(self, taskType, preset, displayName):
        """
        Initialise Exporter Preset Base Class
        """
        return None

    def setPreset(self, preset):
        """
        Assign Preset to ExporterUI
        """
        return None

    def setTags(self, tags):
        """
        setTags passes the subset of tags associated with the selection for export
        """
        return None

    def preset(self):
        """
        Return Preset currently assigned to ExporterUI
        """
        return None

    def populateUI(self, widget, exportTemplate):
        """
        populateUI() Export dialog to allow the TaskUI to populate a QWidget with the ui widgets neccessary to reflect the current preset.
        """
        return None

    def setTaskItemType(self, type):
        """

        """
        return None

    def taskItemType(self):
        """

        """
        return None

    def displayName(self):
        """
        Exporter name to be displayed in the UI
        """
        return None

    def ident(self):
        """
        self.ident() -> called by Hiero to get a unique identifier linking this TaskUI with a Task and TaskPreset.

        @return: string
        """
        return str()

    def parentType(self):
        """

        """
        return None

    def setProject(self, project):
        """
        Set the project being used for the current export.
        """
        return None

    def initializeAndPopulateUI(self, widget, exportTemplate):
        """

        """
        return None

    def initializeUI(self, widget):
        """

        """
        return None

    staticMetaObject: Any = None
