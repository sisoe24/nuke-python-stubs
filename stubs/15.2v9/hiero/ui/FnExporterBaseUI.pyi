# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.ui as _hiero_ui
import hiero.ui.FnCodecUIController as _hiero_ui_FnCodecUIController
import hiero.ui.FnNodePropertyWidget as _hiero_ui_FnNodePropertyWidget
from hiero.FnRedirect import TimelineEditorCreationFlag as TimelineEditorCreationFlag
from hiero.FnRedirect import activeSequence as activeSequence
from hiero.FnRedirect import activeView as activeView
from hiero.FnRedirect import currentWorkspace as currentWorkspace
from hiero.FnRedirect import findRegisteredAction as findRegisteredAction
from hiero.FnRedirect import findRegisteredActions as findRegisteredActions
from hiero.FnRedirect import getTimelineEditor as getTimelineEditor
from hiero.FnRedirect import mainWindow as mainWindow
from hiero.FnRedirect import menuBar as menuBar
from hiero.FnRedirect import registerAction as registerAction
from hiero.FnRedirect import registeredActions as registeredActions
from hiero.FnRedirect import resetCurrentWorkspace as resetCurrentWorkspace
from hiero.FnRedirect import saveWorkspace as saveWorkspace
from hiero.FnRedirect import setWorkspace as setWorkspace
from hiero.core import nuke as nuke
from hiero.core import util as util
from hiero.core.FnExporterBase import classBasename as classBasename
from hiero.core.FnFloatRange import CustomList as CustomList
from hiero.core.FnFloatRange import Default as Default
from hiero.core.FnFloatRange import FloatRange as FloatRange
from hiero.core.FnFloatRange import IntRange as IntRange
from hiero.core.FnFloatRange import QuicktimeCodec as QuicktimeCodec
from hiero.core.FnFloatRange import QuicktimeSettings as QuicktimeSettings
from hiero.ui import BinView as BinView
from hiero.ui import ColorButton as ColorButton
from hiero.ui import ColorPickerDialog as ColorPickerDialog
from hiero.ui import ExportStructureViewer as ExportStructureViewer
from hiero.ui import FilePathWidget as FilePathWidget
from hiero.ui import FormatChooser as FormatChooser
from hiero.ui import IDirectExportUI as IDirectExportUI
from hiero.ui import IDirectExportUIFactoryWrapper as IDirectExportUIFactoryWrapper
from hiero.ui import IExporterUIRegistry as IExporterUIRegistry
from hiero.ui import IProcessorUI as IProcessorUI
from hiero.ui import ITaskUI as ITaskUI
from hiero.ui import ImageRenderFlag as ImageRenderFlag
from hiero.ui import ImageRenderFlags as ImageRenderFlags
from hiero.ui import Initialise as Initialise
from hiero.ui import MediaFlagsChooser as MediaFlagsChooser
from hiero.ui import Player as Player
from hiero.ui import SpreadsheetView as SpreadsheetView
from hiero.ui import TimelineEditor as TimelineEditor
from hiero.ui import TracksMask as TracksMask
from hiero.ui import Viewer as Viewer
from hiero.ui import ViewerCursor as ViewerCursor
from hiero.ui import ViewerCursorTool as ViewerCursorTool
from hiero.ui import ViewerROITool as ViewerROITool
from hiero.ui import ViewerTool as ViewerTool
from hiero.ui import ViewerWipeTool as ViewerWipeTool
from hiero.ui import WindowManager as WindowManager
from hiero.ui import WipeToolState as WipeToolState
from hiero.ui import browseForApplication as browseForApplication
from hiero.ui import currentContextMenuView as currentContextMenuView
from hiero.ui import currentViewer as currentViewer
from hiero.ui import flushAllViewersCache as flushAllViewersCache
from hiero.ui import getFlipbook as getFlipbook
from hiero.ui import isInAnyProject as isInAnyProject
from hiero.ui import isInAnyTimeline as isInAnyTimeline
from hiero.ui import monitorOutNode as monitorOutNode
from hiero.ui import openInNewViewer as openInNewViewer
from hiero.ui import openInOSShell as openInOSShell
from hiero.ui import openInSpreadsheet as openInSpreadsheet
from hiero.ui import openInTimeline as openInTimeline
from hiero.ui import openInViewer as openInViewer
from hiero.ui import openProject as openProject
from hiero.ui import registerBinViewCustomMimeDataType as registerBinViewCustomMimeDataType
from hiero.ui import renderSequenceToImage as renderSequenceToImage
from hiero.ui import sendToViewerA as sendToViewerA
from hiero.ui import sendToViewerB as sendToViewerB
from hiero.ui import unregisterBinViewCustomMimeDataType as unregisterBinViewCustomMimeDataType
from hiero.ui import updateViewer as updateViewer
from hiero.ui import windowManager as windowManager
from hiero.ui.FnCodecUIController import CodecUIController as CodecUIController
from hiero.ui.FnCodecUIController import EXRCodecUIController as EXRCodecUIController
from hiero.ui.FnDisclosureButton import DisclosureButton as DisclosureButton
from hiero.ui.FnNodePropertyWidget import NodePropertyWidget as NodePropertyWidget
from hiero.ui.FnPathQueryDialog import PathQueryDialog as PathQueryDialog
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

eIncludeAnnotations: _hiero_ui.ImageRenderFlag
eNone: _hiero_ui.ImageRenderFlag

class ReformatToolTips:
    """Class for defining refomat related tooltip text"""
    center: str
    filter: str
    format: str
    resize: str
    scale: str
    totype: dict
    @staticmethod
    def createToTypeToolTip(values: Any) -> str:
        """Different reformat options are available depending on the exporter.
        Construct the tooltip based on the options being used.
        """

class TaskUIBase(_hiero_ui.ITaskUI):
    """TaskUIBase is the base class from hich all TaskUI components should derrive"""
    propertiesChanged: Any
    staticMetaObject: Any
    def __init__(self, taskType: Any, preset: Any, displayName: Any) -> None:
        """Initialise Exporter Preset Base Class"""
    def displayName(self) -> Any:
        """Exporter name to be displayed in the UI"""
    def ident(self) -> str: ...
    def initializeAndPopulateUI(self, widget: Any, exportTemplate: Any) -> None: ...
    def initializeUI(self, widget: Any) -> None: ...
    def parentType(self) -> Any: ...
    def populateUI(self, widget: Any, exportTemplate: Any) -> Any:
        """populateUI() Export dialog to allow the TaskUI to populate a QWidget with the ui widgets neccessary to reflect the current preset."""
    def preset(self) -> Any:
        """Return Preset currently assigned to ExporterUI"""
    def setPreset(self, preset: Any) -> None:
        """Assign Preset to ExporterUI"""
    def setProject(self, project: Any) -> None:
        """Set the project being used for the current export. """
    def setTags(self, tags: Any) -> Any:
        """setTags passes the subset of tags associated with the selection for export"""
    def setTaskItemType(self, type: Any) -> None: ...
    def taskItemType(self) -> Any: ...

class RenderTaskUIBase(TaskUIBase):
    """RenderTaskUIBase is a specialization of TaskUIBase which reflects the codec properties in RenderTaskPreset into UI"""
    staticMetaObject: Any
    def __del__(self) -> None: ...
    def __init__(self, taskType: Any, preset: Any, displayName: Any) -> None:
        """A task base that includes functionality for displaying output selection UI."""
    def buildCodecUI(self, layout: Any, itemTaskType: Any) -> None:
        """Populate layout with widgets reflected from the RenderPresetBase class"""
    def codecTypeComboBoxChanged(self, value: Any) -> None: ...
    def createChannelsWidget(self, layout: Any) -> None: ...
    def createCodecOptionsPlaceholder(self, layout: Any) -> None: ...
    def createCodecPropertyWidgets(self, file_type: Any, propertyDictionaries: Any) -> _hiero_ui_FnNodePropertyWidget.NodePropertyWidget | _hiero_ui_FnCodecUIController.EXRCodecUIController | _hiero_ui_FnCodecUIController.CodecUIController:
        """Create widgets for the given property dictionaries, and add them to the given layout. """
    def createFileTypeWidget(self, layout: Any) -> None: ...
    def createOutputTransformWidgets(self, layout: Any) -> None: ...
    def createReformatWidgets(self, layout: Any, itemTaskType: Any) -> None: ...
    def createViewsWidget(self, layout: Any) -> None: ...
    def deleteFirstChildFromWidget(self, widget: Any) -> None:
        """Get the first child added to the widget's layout, and delete it, if it exists. """
    def formatChanged(self) -> None: ...
    def getOutputTransformProperties(self) -> Any: ...
    def propertyChanged(self) -> None: ...
    def reformatChanged(self) -> None:
        """Callback when the Reformat combo box selection has changed. Enable/disable
        the reformat property widgets as appropriate.
        """
    def setFormat(self, format: Any) -> None: ...
    def setWriteNodeFileType(self, fileType: Any) -> None: ...
    def updateChannelsForFileType(self, fileType: Any) -> None: ...
    def updateCodecPropertiesWidget(self, file_type: Any) -> None:
        """Update the codec properties widget. If applicable, also updates the encoder properties (for movs). """
    def writeNode(self) -> Any: ...

def InvalidOutputResolutionMessage(message: Any) -> None: ...
