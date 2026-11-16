# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.ui.FnExporterBaseUI as _hiero_ui_FnExporterBaseUI
from hiero.exporters import FnAudioConstants as FnAudioConstants
from hiero.exporters import FnAudioExportTask as FnAudioExportTask
from hiero.exporters import FnAudioHelper as FnAudioHelper
from hiero.ui.FnTaskUIFormLayout import TaskUIFormLayout as TaskUIFormLayout
from hiero.ui.FnUIProperty import UIPropertyFactory as UIPropertyFactory
import hiero as hiero

class AudioExportUI(_hiero_ui_FnExporterBaseUI.TaskUIBase):
    staticMetaObject: Any
    def __init__(self, preset: Any) -> None:
        """Initialize"""
    def codecChanged(self) -> None: ...
    def populateUI(self, widget: Any, exportTemplate: Any) -> None: ...
