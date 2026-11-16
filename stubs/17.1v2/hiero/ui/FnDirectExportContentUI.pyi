# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import hiero.ui as _hiero_ui
from hiero.core import nuke as nuke
from hiero.core.FnFloatRange import CustomList as CustomList
from hiero.core.FnFloatRange import Default as Default
from hiero.core.FnFloatRange import FloatRange as FloatRange
from hiero.core.FnFloatRange import IntRange as IntRange
from hiero.core.FnFloatRange import QuicktimeCodec as QuicktimeCodec
from hiero.core.FnFloatRange import QuicktimeSettings as QuicktimeSettings
from hiero.ui import IDirectExportUI as IDirectExportUI
from hiero.ui import IDirectExportUIFactoryWrapper as IDirectExportUIFactoryWrapper
from hiero.ui.FnNodePropertyWidget import NodePropertyWidget as NodePropertyWidget
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
import nuke_internal as nuke_internal

Dict: Any
tdeUIFactory: PythonDirectExportUIFactory

class DirectExportToolTip:
    """This class stores tooltips for the Direct Export UI and provides access methods."""
    kColorPrimariesTooltip: str
    kCustomColorPrimariesTooltip: str
    kCustomTransferFunctionTooltip: str
    kDataRangeTooltip: str
    kFastStartTooltip: str
    kTransferFunctionTooltip: str
    kWriteTimecodeTooltip: str
    def __init__(self) -> None:
        """Initialize the tooltip dictionary."""
    def getAnnotationsTooltip(self) -> str:
        """Returns the tooltip for the Annotations setting."""
    def getAudioTooltip(self, propertyName: Any) -> str:
        """Returns the tooltip for an Audio property."""
    def getCodecAdvanceProperties(self, codecName: Any, propertyName: Any) -> str:
        """Returns the tooltip for a specific advanced codec property."""
    def getCodecPropertiesToolTip(self, codecName: Any, propertyName: Any) -> str:
        """Returns the tooltip for a specific codec property."""
    def getCodecTooltip(self) -> str:
        """Returns the tooltip for the Codec selection."""
    def getNCLCMetadataTooltip(self, propertyName: Any) -> str:
        """Returns the tooltip for an NCLC Metadata property."""
    def getReformatTooltip(self, propertyName: Any) -> str:
        """Returns the tooltip for reformat settings."""

class DirectExportUIController(_PySide6_QtCore.QObject, _hiero_ui.IDirectExportUI):
    """Class is used to create the Direct export UI properties
    and allows the user to select the properties for direct mov export
    """
    kBitRate: str
    kQuality: str
    kQuantizerMax: str
    kQuantizerMin: str
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __del__(self) -> None: ...
    def __init__(self, parent: Any = ...) -> None: ...
    def createAnnotationsWidget(self, layout: Any) -> None: ...
    def createAudioSettingsUISection(self, layout: Any) -> None: ...
    def createNCLCMetadataSettingsUISection(self, layout: Any) -> None:
        """Creates the UI section for Color Management options"""
    def createOutputTransformWidgets(self, layout: Any) -> None: ...
    def createProcessorUIContentWidget(self) -> Any: ...
    def createReformatWidgets(self, layout: Any) -> None: ...
    def createViewsWidget(self, layout: Any) -> None: ...
    def formatChanged(self) -> None: ...
    def getBitrateDefaultValueForH264(self, quality: Any) -> int | None: ...
    def getIndexForDefaultAudioItems(self, item: Any) -> int: ...
    def getIndexForDefaultCodecProfile(self, codec: Any) -> int: ...
    def getOutputTransformProperties(self) -> Any: ...
    def getQuantizerMaxDefaultValueForH264(self, quality: Any) -> int | None: ...
    def getQuantizerMinDefaultValueForH264(self, quality: Any) -> int | None: ...
    def getValues(self) -> dict[Any, Any]: ...
    def populateUI(self, processorUIWidget: Any, taskUIWidget: Any, exportItems: Any) -> None: ...
    def rePopulateUI(self) -> None: ...
    def reformatChanged(self) -> None:
        """Callback when the Reformat combo box selection has changed.  Enable/disable the reformat property widgets
        as appropriate.
        """
    def setFormat(self, format: Any) -> None: ...
    def startExport(self) -> None: ...
    def updateColorPrimariesDependencies(self) -> None:
        """Enable/disable the Custom Color Primaries Value based on selection"""
    def updateDefaultValuesForH264(self) -> None: ...
    def updateFilePath(self, newPath: Any) -> None:
        """Updates the internal file path when the signal is emitted. """
    def updateTransferFunctionDependencies(self) -> None:
        """Enable/disable the Custom Transfer Function Value based on selection"""
    def validate(self) -> bool: ...
    def writeNode(self) -> Any: ...

class PythonDirectExportUIFactory(_hiero_ui.IDirectExportUIFactoryWrapper):
    def createUI(self) -> DirectExportUIController: ...
    def getKey(self) -> str: ...
    def registerme(self) -> None: ...
