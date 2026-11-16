# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import hiero.ui.FnExporterBaseUI as _hiero_ui_FnExporterBaseUI
from hiero.core import nuke as nuke
from hiero.core.FnFloatRange import CustomList as CustomList
from hiero.core.FnFloatRange import Default as Default
from hiero.core.FnFloatRange import FloatRange as FloatRange
from hiero.core.FnFloatRange import IntRange as IntRange
from hiero.core.FnFloatRange import QuicktimeCodec as QuicktimeCodec
from hiero.core.FnFloatRange import QuicktimeSettings as QuicktimeSettings
from hiero.exporters import FnAdditionalNodesDialog as FnAdditionalNodesDialog
from hiero.exporters import FnNukeShotExporter as FnNukeShotExporter
from hiero.exporters.FnNukeExporterWidgets import NukeProjectNodeSelectionWidget as NukeProjectNodeSelectionWidget
from hiero.exporters.FnNukeExporterWidgets import TimelineWriteNodeWidget as TimelineWriteNodeWidget
from hiero.ui.FnExporterBaseUI import ReformatToolTips as ReformatToolTips
from hiero.ui.FnTaskUIFormLayout import TaskUIFormLayout as TaskUIFormLayout
from hiero.ui.FnUIProperty import CascadingEnumerationComboBox as CascadingEnumerationComboBox
from hiero.ui.FnUIProperty import CascadingEnumerationProperty as CascadingEnumerationProperty
from hiero.ui.FnUIProperty import CheckboxProperty as CheckboxProperty
from hiero.ui.FnUIProperty import ComboProperty as ComboProperty
from hiero.ui.FnUIProperty import CustomComboProperty as CustomComboProperty
from hiero.ui.FnUIProperty import SliderProperty as SliderProperty
from hiero.ui.FnUIProperty import TextProperty as TextProperty
from hiero.ui.FnUIProperty import UIPropertyBase as UIPropertyBase
from hiero.ui.FnUIProperty import UIPropertyFactory as UIPropertyFactory
from hiero.ui.FnUIProperty import ViewsPropertyWidget as ViewsPropertyWidget
from hiero.ui.FnUIProperty import getLabelData as getLabelData
import hiero as hiero

class NukeShotExporterUI(_hiero_ui_FnExporterBaseUI.TaskUIBase):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, preset: Any) -> None:
        """UI for NukeShotExporter task."""
    def annotationsPreCompPresetChanged(self, topLeft: Any, bottomRight: Any) -> None: ...
    def createNodeSelectionWidget(self, layout: Any, exportTemplate: Any) -> None: ...
    def formatChanged(self) -> None: ...
    def populateUI(self, widget: Any, exportTemplate: Any) -> None: ...
    def propertyChanged(self) -> None: ...
    def readPresetChanged(self, topLeft: Any, bottomRight: Any) -> None: ...
    def reformatChanged(self) -> None:
        """Callback when the Reformat combo box selection has changed.  Enable/disable the reformat property widgets
        as appropriate. 
        """
    def setFormat(self, format: Any) -> None: ...
    def setTags(self, tags: Any) -> None:
        """setTags passes the subset of tags associated with the selection for export"""
    def timelineWriteNodeChanged(self, text: Any) -> None: ...
    def writePresetChanged(self, topLeft: Any, bottomRight: Any) -> None: ...
