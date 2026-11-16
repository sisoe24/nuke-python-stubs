# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.ui.FnExporterBaseUI as _hiero_ui_FnExporterBaseUI
from hiero.exporters import FnXMLExportTask as FnXMLExportTask
from hiero.ui.FnTaskUIFormLayout import TaskUIFormLayout as TaskUIFormLayout
import hiero as hiero

class XMLExportUI(_hiero_ui_FnExporterBaseUI.TaskUIBase):
    staticMetaObject: Any
    def __init__(self, preset: Any) -> None:
        """Initialize"""
    def includeMarkersCheckboxChanged(self, state: Any) -> None: ...
    def populateUI(self, widget: Any, exportTemplate: Any) -> None: ...
