# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import hiero.ui.FnExporterBaseUI as _hiero_ui_FnExporterBaseUI
from hiero.exporters.FnNukeAnnotationsExporter import NukeAnnotationsExporter as NukeAnnotationsExporter
from hiero.exporters.FnNukeAnnotationsExporter import NukeAnnotationsPreset as NukeAnnotationsPreset
from hiero.ui.FnTaskUIFormLayout import TaskUIFormLayout as TaskUIFormLayout
from hiero.ui.FnUIProperty import UIPropertyFactory as UIPropertyFactory
import hiero as hiero

class NukeAnnotationsExporterUI(_hiero_ui_FnExporterBaseUI.RenderTaskUIBase):
    """UI for NukeAnnotationsExporter.  This is largely the same as the NukeShotExporterUI, with some options hidden. """
    kFileTypeLabel: str
    kFileTypeTooltip: str
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, preset: Any) -> None: ...
    def populateUI(self, widget: Any, exportTemplate: Any) -> None: ...
