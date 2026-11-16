# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import PySide6.QtWidgets as _PySide6_QtWidgets
from hiero.core.FnFloatRange import CustomList as CustomList
from hiero.core.FnFloatRange import Default as Default
from hiero.core.FnFloatRange import FloatRange as FloatRange
from hiero.core.FnFloatRange import IntRange as IntRange
from hiero.core.FnFloatRange import QuicktimeCodec as QuicktimeCodec
from hiero.core.FnFloatRange import QuicktimeSettings as QuicktimeSettings
import hiero as hiero

class CascadingEnumerationComboBox(_PySide6_QtWidgets.QComboBox):
    """Combo box specialisation for supporting the cascading enumeration
    property.
    """
    kSeparator: str
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, values: Any) -> None: ...
    def onActionTriggered(self, action: Any) -> None:
        """Callback from a menu action being triggered, set the index. """
    def setCurrentIndex(self, index: Any) -> None:
        """Set the current index and set the checked state of the menu entries. """
    def showPopup(self) -> None:
        """Override default showPopup() and show our menu instead """

class UIPropertyBase(_PySide6_QtWidgets.QWidget):
    """UIProperty is a utility class which reflects data into a suitable Widget"""
    propertyChanged: _PySide6_QtCore.Signal
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, key: Any = ..., value: Any = ..., dictionary: Any = ..., label: Any = ..., tooltip: Any = ...) -> None:
        """@param key - Key against which to store value
        @param value - Value, type of which will determine UI widget
        @param dictionary - dictionary in which value will be saved (against key)
        @param label - Text Label to identify property. (optional, will default to key)
        @param tooltip - Tooltip describing property
        """
    @staticmethod
    def register(valuetypes: Any, objecttype: Any) -> None: ...
    def setAvailableValues(self, value: Any) -> Any:
        """Update the available values. This is relevant for properties where the value passed in on
        creation is used to create the available options, e.g. a ComboBox, rather than simply
        being used to determine the type of property to create. This is useful when the available
        options can change e.g. ComboBox options that change depending on another property.
        The values provided are assumed to be the same type as those used to create the property. 
        """
    def update(self, commit: bool = ...) -> Any:
        """Update the property.  If commit is True, the current UI value is written back to the
        properties dict.  This seems to be mostly useful when the value may not yet exist in
        the dict and should be set to a default. 
        """
    def updateToolTip(self, widget: Any) -> None: ...

class CascadingEnumerationProperty(UIPropertyBase):
    """Property widget which cascades items into sub-menus when the text has /
    separators, in a similar way to the Nuke cascading enumeration knob.
    """
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, stretch: float = ..., **kargs: Any) -> None: ...
    def onComboChanged(self, index: Any) -> None:
        """Slot callback when the combo box current item changes. """
    def update(self, commit: bool = ...) -> None: ...

class CheckboxProperty(UIPropertyBase):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, **kargs: Any) -> None: ...
    def checkboxChanged(self, state: Any) -> None: ...
    def update(self, commit: bool = ...) -> None: ...

class ComboProperty(UIPropertyBase):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, stretch: float = ..., **kargs: Any) -> None: ...
    def comboChanged(self, index: Any) -> None: ...
    def populateComboBox(self) -> None: ...
    def setAvailableValues(self, value: Any) -> None: ...
    def setFloatValue(self, newValue: Any, floatTolerance: float = ...) -> None:
        """sets the combobox value to the newValue, assuming it can find a string item in the list that is within floatTolerance of the newValue"""
    def update(self, commit: bool = ...) -> None: ...

class CustomComboProperty(ComboProperty):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, **kargs: Any) -> None: ...
    def checkValidation(self) -> bool: ...
    def customTextChanged(self) -> None: ...
    def update(self, commit: bool = ...) -> None: ...

class SliderProperty(UIPropertyBase):
    """Class which shows a UI for numeric ranges. """
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, **kargs: Any) -> None: ...
    def isIntRange(self) -> bool:
        """Check if the slider is representing an int range. """
    def onLineEditTextEdited(self, text: Any) -> None:
        """Callback when line edit text is edited. """
    def onSliderReleased(self) -> None:
        """Callback when slider is released, send property changed notifications. """
    def onSliderValueChanged(self, value: Any) -> None:
        """Callback when slider value changes. """
    def setSliderValue(self, value: Any) -> None:
        """Set the slider value. """
    def update(self, commit: bool = ...) -> None: ...
    def valueFromLineEdit(self) -> int | float:
        """Get the value from the line edit widget, as either an int or float depending on
        the range type. 
        """
    def valueFromSlider(self) -> int:
        """Get the value from the line edit widget, as either an int or float depending on the range type. """

class TextProperty(UIPropertyBase):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, **kargs: Any) -> None: ...
    def lineditChanged(self, value: Any) -> None: ...
    def update(self, commit: bool = ...) -> None: ...

class UIPropertyFactory:
    """Factory for registering and creating UIProperties"""
    PropertyDictionary: dict
    @staticmethod
    def create(type: Any, **kargs: Any) -> None: ...
    @staticmethod
    def register(valuetypes: Any, objecttype: Any) -> None: ...
    @staticmethod
    def unregister(valuetype: Any, objecttype: Any) -> None: ...

class ViewsPropertyWidget(UIPropertyBase):
    """Widget for selecting views. The UI follows the Write node 'views' knob """
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, **kwargs: Any) -> None: ...
    def onViewToggled(self, checked: Any) -> None: ...
    def update(self, commit: bool = ...) -> None: ...
    def views(self) -> None:
        """List of available views """

def getLabelData(item: Any) -> tuple[Any, Any]: ...
