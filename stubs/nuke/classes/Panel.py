from typing import *
from numbers import Number

import nuke

from . import *


class Panel(object):
    """
    Panel
    """

    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def width(self,) -> int:
        """
        self.width() -> The width as an int.
        Get the width of the panel.
        @return: The width as an int.
        """
        ...

    def setWidth(self, val: int) -> bool:
        """
        self.setWidth(val) -> True if successful.
        Set the width of the panel.
        @param val: The width as an int.
        @return: True if successful.
        """
        ...

    def title(self,) -> str:
        """
        self.title() -> The title as a string.
        Get the current title for the panel.
        @return: The title as a string.
        """
        ...

    def setTitle(self, val: str) -> bool:
        """
        self.setTitle(val) -> True if successful.
        Set the current title for the panel.
        @param val: The title as a string.
        @return: True if successful.
        """
        ...

    def addSingleLineInput(self, name: str, value) -> bool:
        """
        self.addSingleLineInput(name, value) -> True if successful.
        Add a single-line input knob to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
        ...

    def addPasswordInput(self, name: str, value) -> bool:
        """
        self.addPasswordInput(name, value) -> True if successful.
        Add a password input knob to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
        ...

    def addFilenameSearch(self, name: str, value) -> bool:
        """
        self.addFilenameSearch(name, value) -> True if successful.
        Add a filename search knob to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
        ...

    def addClipnameSearch(self, name: str, value) -> bool:
        """
        self.addClipnameSearch(name, value) -> True if successful.
        Add a clipname search knob to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
        ...

    def addMultilineTextInput(self, name: str, value) -> bool:
        """
        self.addMultilineTextInput(name, value) -> True if successful.
        Add a multi-line text knob to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
        ...

    def addNotepad(self, name: str, value) -> bool:
        """
        self.addNotepad(name, value) -> True if successful.
        Add a text edit widget to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
        ...

    def addBooleanCheckBox(self, name: str, value) -> bool:
        """
        self.addBooleanCheckBox(name, value) -> True if successful.
        Add a boolean check box knob to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
        ...

    def addRGBColorChip(self, name: str, value) -> bool:
        """
        self.addRGBColorChip(name, value) -> True if successful.
        Add a color chooser to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
        ...

    def addEnumerationPulldown(self, name: str, value) -> bool:
        """
        self.addEnumerationPulldown(name, value) -> True if successful.
        Add a pulldown menu to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
        ...

    def addTextFontPulldown(self, name: str, value) -> bool:
        """
        self.addTextFontPulldown(name, value) -> True if successful.
        Add a font chooser to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
        ...

    def addExpressionInput(self, name: str, value) -> bool:
        """
        self.addExpressionInput(name, value) -> True if successful.
        Add an expression evaluator to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
        ...

    def addScriptCommand(self, name: str, value) -> bool:
        """
        self.addScriptCommand(name, value) -> True if successful.
        Add a script command evaluator to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
        ...

    def addButton(self, name: str, value) -> bool:
        """
        self.addButton(name, value) -> True if successful.
        Add a button to the panel.
        @param name: The name for the new knob.
        @param value: The initial value for the new knob.
        @return: True if successful.
        """
        ...

    def value(self, name: str) -> None:
        """
        self.value(name) -> The value for the field if any, otherwise None.
        Get the value of a particular control in the panel.
        @param name: The name of the knob to get a value from.
        @return: The value for the field if any, otherwise None.
        """
        ...

    def execute(self, name: str) -> str:
        """
        self.execute(name) -> The result of the script as a string, or None if it fails.
        Execute the script command associated with a particular label and return the result as a string.
        @param name: The name of the script field to execute.
        @return: The result of the script as a string, or None if it fails.
        """
        ...

    def clear(self,) -> None:
        """
        self.clear() -> None
        Clear all panel attributes.
        """
        ...

    def show(self,) -> int:
        """
        self.show() -> An int value indicating how the dialog was closed (normally, or cancelled).
        Display the panel.
        @return: An int value indicating how the dialog was closed (normally, or cancelled).
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
