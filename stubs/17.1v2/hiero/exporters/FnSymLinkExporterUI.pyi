# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import hiero.ui.FnExporterBaseUI as _hiero_ui_FnExporterBaseUI
from hiero.exporters import FnSymLinkExporter as FnSymLinkExporter
import hiero as hiero

class SymLinkExporterUI(_hiero_ui_FnExporterBaseUI.TaskUIBase):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, preset: Any) -> None:
        """Initialize"""
    def populateUI(self, widget: Any, exportTemplate: Any) -> None: ...
