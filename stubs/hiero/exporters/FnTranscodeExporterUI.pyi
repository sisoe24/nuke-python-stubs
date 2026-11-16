# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.exporters.FnExternalRenderUI as _hiero_exporters_FnExternalRenderUI
from hiero.core.FnFloatRange import CustomList as CustomList
from hiero.core.FnFloatRange import Default as Default
from hiero.core.FnFloatRange import FloatRange as FloatRange
from hiero.core.FnFloatRange import IntRange as IntRange
from hiero.core.FnFloatRange import QuicktimeCodec as QuicktimeCodec
from hiero.core.FnFloatRange import QuicktimeSettings as QuicktimeSettings
from hiero.exporters import FnAdditionalNodesDialog as FnAdditionalNodesDialog
from hiero.exporters import FnAudioConstants as FnAudioConstants
from hiero.exporters import FnAudioHelper as FnAudioHelper
from hiero.exporters import FnExternalRenderUI as FnExternalRenderUI
from hiero.exporters import FnTranscodeExporter as FnTranscodeExporter
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

class TranscodeExporterUI(_hiero_exporters_FnExternalRenderUI.NukeRenderTaskUI):
    staticMetaObject: Any
    def __init__(self, preset: Any) -> None:
        """Initialize"""
    def codecTypeComboBoxChanged(self, value: Any) -> None: ...
    def movCodecComboBoxChanged(self) -> None: ...
    def onIncludeAudioChanged(self) -> None: ...
    def populateUI(self, widget: Any, exportTemplate: Any) -> None: ...
    def setTags(self, tags: Any) -> None:
        """setTags passes the subset of tags associated with the selection for export"""
    def updateAudioSettings(self) -> None: ...
