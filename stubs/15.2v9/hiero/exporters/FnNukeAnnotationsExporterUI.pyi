# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.ui.FnExporterBaseUI as _hiero_ui_FnExporterBaseUI
from hiero.exporters import FnAdditionalNodesDialog as FnAdditionalNodesDialog
from hiero.exporters import FnNukeAnnotationsExporter as FnNukeAnnotationsExporter
from hiero.exporters.FnNukeExporterWidgets import NukeProjectNodeSelectionWidget as NukeProjectNodeSelectionWidget
from hiero.exporters.FnNukeExporterWidgets import TimelineWriteNodeWidget as TimelineWriteNodeWidget
from hiero.ui.FnTaskUIFormLayout import TaskUIFormLayout as TaskUIFormLayout
from hiero.ui.FnUIProperty import UIPropertyFactory as UIPropertyFactory
import hiero as hiero

class NukeAnnotationsExporterUI(_hiero_ui_FnExporterBaseUI.TaskUIBase):
    """UI for NukeAnnotationsExporter.  This is largely the same as the NukeShotExporterUI, with some options hidden. """
    staticMetaObject: Any
    def __init__(self, preset: Any) -> None: ...
    def populateUI(self, widget: Any, exportTemplate: Any) -> None: ...
    def readPresetChanged(self, topLeft: Any, bottomRight: Any) -> None: ...
    def setTags(self, tags: Any) -> None:
        """setTags passes the subset of tags associated with the selection for export"""
    def timelineWriteNodeChanged(self, text: Any) -> None: ...
    def updatePreset(self, presetValue: Any, model: Any, topLeft: Any, bottomRight: Any) -> None: ...
    def writePresetChanged(self, topLeft: Any, bottomRight: Any) -> None: ...
