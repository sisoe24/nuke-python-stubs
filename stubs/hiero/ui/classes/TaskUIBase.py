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

    def __init__(self, taskType, preset, displayName) -> None:
        """
        Initialise Exporter Preset Base Class
        """
        ...

    def setPreset(self, preset) -> None:
        """
        Assign Preset to ExporterUI
        """
        ...

    def setTags(self, tags) -> None:
        """
        setTags passes the subset of tags associated with the selection for export
        """
        ...

    def preset(self) -> None:
        """
        Return Preset currently assigned to ExporterUI
        """
        ...

    def populateUI(self, widget, exportTemplate) -> None:
        """
        populateUI() Export dialog to allow the TaskUI to populate a QWidget with the ui widgets neccessary to reflect the current preset.
        """
        ...

    def setTaskItemType(self, type) -> None:
        """

        """
        ...

    def taskItemType(self) -> None:
        """

        """
        ...

    def displayName(self) -> None:
        """
        Exporter name to be displayed in the UI
        """
        ...

    def ident(self) -> str:
        """
        self.ident() -> called by Hiero to get a unique identifier linking this TaskUI with a Task and TaskPreset.

        @return: string
        """
        ...

    def parentType(self) -> None:
        """

        """
        ...

    def setProject(self, project) -> None:
        """
        Set the project being used for the current export.
        """
        ...

    def initializeAndPopulateUI(self, widget, exportTemplate) -> None:
        """

        """
        ...

    def initializeUI(self, widget) -> None:
        """

        """
        ...

    staticMetaObject: Any = None
