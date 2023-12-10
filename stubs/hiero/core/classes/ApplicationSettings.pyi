import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *

class ApplicationSettings(Object):
    """
    Helper object to set and get application settings.
    """
    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def __new__(self,*args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def boolValue(self, *args, **kwargs) -> str:
        """
        self.boolValue(key, defaultValue) -> returns the previously stored value as True or False, named by the key parameter, or the defaultValue parameter
        self.boolValue(key) ->  returns the previously stored value as True or False, named by the key parameter, or the default value as configured (if configured) by the Hiero code. Use this method if you're looking up a value used by Hiero internally.
        Note: use self.value(key, defaultValue) if you just want to retrieve a string setting

        @param key: string name of the value to retrieve
        @param defaultValue: the value to return if this setting hasn't been saved before. Does not save the value to the default.
        @return: string
        """
        ...

    def setBoolValue(self, key: str, value: bool) -> None:
        """
        self.setBoolValue(key, value) -> saves the value as True or False with the application's settings using the key

        @param key: string name of the value to retrieve
        @param value: the bool (True or False) value to save.
        """
        ...

    def setValueOverride(self, name, value) -> None:
        """
        self.setValue(key, value) -> saves the value with the application's settings using the key

        @param key: string name of the value to save

        @param value: the value to store
        """
        ...

    def getValueOverride(self, name, defaultValue=None) -> int:
        """
        self.value(key, defaultValue=None) -> returns the previously stored string value named by the key parameter, or the defaultValue parameter

        @param key: string name of the value to retrieve
        @param defaultValue: the value to return if this setting hasn't been saved before. Does not save the value to the default
        @return: string, unless the defaultValue is set, in which case, the return value will be the same type as the defaultValue (string, int or bool)
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...
