# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.ui.FnExporterBaseUI as _hiero_ui_FnExporterBaseUI
from hiero.exporters import FnEDLExportTask as FnEDLExportTask
from hiero.ui.FnTaskUIFormLayout import TaskUIFormLayout as TaskUIFormLayout
import hiero as hiero

class EDLExportUI(_hiero_ui_FnExporterBaseUI.TaskUIBase):
    staticMetaObject: Any
    def __init__(self, preset: Any) -> None:
        """Initialize"""
    def absPathCheckboxChanged(self, state: Any) -> None: ...
    def fromClipChanged(self) -> None: ...
    def populateUI(self, widget: Any, exportTemplate: Any) -> None: ...
    def reelNameChanged(self) -> None: ...
    def truncateCheckboxChanged(self, state: Any) -> None: ...
