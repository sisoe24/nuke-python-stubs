# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import hiero.ui.FnExporterBaseUI as _hiero_ui_FnExporterBaseUI
from hiero.exporters.FnOTIOExportTask import OTIOExportPreset as OTIOExportPreset
from hiero.exporters.FnOTIOExportTask import OTIOExportTask as OTIOExportTask
from hiero.ui.FnTaskUIFormLayout import TaskUIFormLayout as TaskUIFormLayout
from hiero.ui.FnUIProperty import UIPropertyFactory as UIPropertyFactory
import hiero as hiero

class OTIOExportUI(_hiero_ui_FnExporterBaseUI.TaskUIBase):
    """UI for OTIO file export.
    Currently empty until we need to add some parameters to the export.
    """
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, preset: Any) -> None: ...
    def populateUI(self, widget: Any, exportTemplate: Any) -> None: ...
