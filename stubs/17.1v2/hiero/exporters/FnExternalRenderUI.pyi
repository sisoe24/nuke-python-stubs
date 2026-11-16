# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import PySide6.QtGui as _PySide6_QtGui
import PySide6.QtWidgets as _PySide6_QtWidgets
import hiero.ui.FnExporterBaseUI as _hiero_ui_FnExporterBaseUI
from hiero.exporters import FnExternalRender as FnExternalRender
from hiero.ui.FnTaskUIFormLayout import TaskUIFormLayout as TaskUIFormLayout
from hiero.ui.FnUIProperty import UIPropertyFactory as UIPropertyFactory
import hiero as hiero

class BracketValidator(_PySide6_QtGui.QValidator):
    BRACKETS: tuple
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self) -> None: ...
    def validate(self, input: Any, pos: Any) -> Any: ...

class ExternalRenderTaskUI(_hiero_ui_FnExporterBaseUI.TaskUIBase):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, preset: Any) -> None:
        """Initialize"""
    def populateUI(self, widget: Any, exportTemplate: Any) -> Any: ...

class KnobEditDialog(_PySide6_QtWidgets.QDialog):
    """A Dialog to reflect a dictionary for the purpose of selecting knob values"""
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, data: Any, properties: Any, parent: Any = ...) -> None: ...
    def accept(self) -> None: ...
    def data(self) -> dict[Any, Any]: ...
    def initUI(self) -> None: ...
    def reset(self) -> None: ...

class NukeRenderTaskUI(_hiero_ui_FnExporterBaseUI.RenderTaskUIBase):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, preset: Any, parenttask: Any = ..., displayName: str = ...) -> None:
        """Initialize"""
    def createBurnInWidgets(self, formLayout: Any) -> None: ...
    def createCreateDirsWidget(self, formLayout: Any) -> None:
        """Create the widget for the create_dirs knob. """
    def keepNukeScriptCheckboxChanged(self, state: Any) -> None: ...
    def populateUI(self, widget: Any, exportTemplate: Any) -> None: ...
    def readAllLinesCheckboxChanged(self, state: Any) -> None: ...
