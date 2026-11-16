# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import PySide6.QtWidgets as _PySide6_QtWidgets
import hiero.ui.FnDisclosureButton as _hiero_ui_FnDisclosureButton
from hiero.ui.FnDisclosureButton import DisclosureButton as DisclosureButton
from hiero.ui.FnTaskUIFormLayout import TaskUIFormLayout as TaskUIFormLayout
from hiero.ui.FnUIProperty import CascadingEnumerationProperty as CascadingEnumerationProperty
from hiero.ui.FnUIProperty import UIPropertyFactory as UIPropertyFactory

class NodePropertyWidget(_PySide6_QtWidgets.QWidget):
    """This class generates a widget based on the passed in node. The created
    widget contains widgets for all the knobs that are present in the
    propertyDictionaries passed into the constructor. The widgets are created by
    calling makeWidget() on the respective knobs. This class will also update the
    values of the knob in the node when setting a value on a property widget. The
    layout of the property widgets will attempt to mimic the layout of the knobs
    on the node. Any non-default knob values will get written into the passed in
    preset dictionary.
    Note: the node must not be deleted until after the NodePropertyWidget
    has been deleted.
    """
    CASCADING_KNOB_TYPE: int
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, node: Any, propertyDictionaries: Any, presetDictionary: Any) -> None: ...
    def addWidgetsToNewRow(self, layout: Any, labels: Any, widgets: Any) -> None:
        """Adds widgets to the layout as a new row, adding them as
        multi widget rows as necessary, otherwise adding as a normal row
        if a single widget is provided (this is due to layout.setWidgetVisible
        behaving differently for multi widget rows which we don't want for
        a single widget row).
        """
    def createDisclosureWidget(self, tabKnob: Any) -> tuple[_hiero_ui_FnDisclosureButton.DisclosureButton, Any]:
        """Creates a DisclosureButton and an associated widget that's visibility
        is toggled by the DisclosureButton. The widget itself has a TaskUIFormLayout
        set on it. Returns the created widget.
        """
    def createKnobWidget(self, knob: Any) -> Any: ...
    def initializeUI(self, propertyDictionaries: Any) -> None:
        """Iterates through the propertyDictionaries and creates UIProperties
        for each key in the dictionaries, where each key should be the name of a
        desired knob on the Write node. The UIProperties will store their values
        in the _presetDictionary, using the knob name as the key. If the
        _presetDictionary already has a value for the knob name, it will also
        initialise the UIProperty with that value.
        """
    def knobChanged(self) -> None: ...
    def knobOnNewLine(self, knob: Any) -> Any:
        """Determines if a knob starts on a new row or is placed next
        to the previous knob.
        """
    def removeCallbacks(self) -> None: ...
    def updatePresetValue(self, knob: Any) -> None:
        """Sets the knob value in the preset dictionary if the knob is visible. If
        the knob isn't visible then the value is cleared as we don't want to store
        values of hidden knobs in the preset dictionary. This is so that we don't
        set the values on these hidden knobs on the node since setting the value
        of hidden knobs can have unintended consequences.
        """
    def updateProperties(self) -> None:
        """Iterates through the property widgets and updates their state
        to reflect the current value and visibility of their associated knobs.
        """
