# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any

class DisclosureButton:
    """Button used for showing/hiding widgets in a layout.  This is a Python reimplementation of the class of the same name in the Core/UI library."""
    staticMetaObject: Any
    def __init__(self, contentsVisible: bool = ..., parent: Any = ...) -> None:
        """Initialise the button with the given parent and contents visible flag. """
    def addWidget(self, widget: Any) -> None:
        """Add a new widget to the set of those controlled by this
        disclosure button (the widget is not a layout and so the
        new widget should be added to the hierarchy of displayed widgets
        in some other way).  If this checkbox is ticked and it's marked
        "contents visible" than the widget will be shown, otherwise
        it will be hidden. 
        """
    def paintEvent(self, event: Any) -> None:
        """Paint the widget. """
    def removeWidget(self, widget: Any) -> None:
        """Remove a widget from the button's control. """
    def setVisible(self, newVisible: Any) -> None:
        """Set the visibility of the widget.  Will also change the visibility of any controlled widgets. """
    def showOrHideWidgets(self) -> None:
        """Update the visibility of controlled widgets. """
    def widgetsVisible(self) -> Any:
        """Get if controlled widgets should be visible. """
