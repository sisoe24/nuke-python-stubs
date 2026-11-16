# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import hiero.ui.FnExporterBaseUI as _hiero_ui_FnExporterBaseUI
from hiero.exporters import FnAudioConstants as FnAudioConstants
from hiero.exporters import FnAudioExportTask as FnAudioExportTask
from hiero.exporters import FnAudioHelper as FnAudioHelper
from hiero.ui.FnTaskUIFormLayout import TaskUIFormLayout as TaskUIFormLayout
from hiero.ui.FnUIProperty import UIPropertyFactory as UIPropertyFactory
import hiero as hiero

class AudioExportUI(_hiero_ui_FnExporterBaseUI.TaskUIBase):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, preset: Any) -> None:
        """Initialize"""
    def codecChanged(self) -> None: ...
    def populateUI(self, widget: Any, exportTemplate: Any) -> None: ...
