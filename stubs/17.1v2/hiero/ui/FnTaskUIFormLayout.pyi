# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import PySide6.QtWidgets as _PySide6_QtWidgets

class TaskUIFormLayout(_PySide6_QtWidgets.QFormLayout):
    """Specialised form layout for constructing task UIs. This includes helpers
    for adding dividers, multiple widgets on a row, and enabling/disabling widgets.
    """
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, parent: Any = ...) -> None: ...
    def addDivider(self, text: Any) -> TaskUILayoutDivider:
        """Add a divider showing the given text, and return it. """
    def addMultiWidgetRow(self, labels: Any, widgets: Any) -> None:
        """Add multiple widgets, each with a label, to a single row. """
    def setWidgetEnabled(self, widget: Any, enabled: Any) -> None:
        """Set the enabled state of a widget in the layout. This will also set the
        state of its label.
        """
    def setWidgetVisible(self, widget: Any, visible: Any) -> None:
        """Set the visible state of a widget in the layout. This will also set the
        state of its label.
        """

class TaskUILayoutDivider(_PySide6_QtWidgets.QWidget):
    """Widget for showing a divider in TaskUIFormLayout. """
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, text: Any) -> None: ...
    def setText(self, text: Any) -> None:
        """Set the text shown in the divider. """
