from typing import *
from numbers import Number

import nuke

from . import *


class String_Knob(Knob):
    """
    A knob which holds a string value. Appears as a text entry field in a Node panel.
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def getText(self, oc=None) -> str:
        """
        self.getText(oc) -> string

        Get the non-evaluated value of this knob - also see `value()`
        @param oc: Optional parameter specifying the output context.
        Return text associated with knob.
        """
        ...

    def setValue(self, val, view='default') -> None:
        """
        self.setValue(val, view='default') -> None

        Set value of knob.
        @param val: The new value.
        @param view: Optional parameter specifying which view to set the value for. If omitted, the value will be set for the default view.
        @return: None
        """
        ...

    def value(self, oc=None) -> str:
        """
        self.value(oc) -> str

        Get the evaluated value of this knob as a string - also see `getText()`.
        @param oc: Optional parameter specifying the output context.
        @return: String value.
        """
        ...

    def value(self, oc=None) -> str:
        """
        self.value(oc) -> str

        Get the evaluated value of this knob as a string - also see `getText()`.
        @param oc: Optional parameter specifying the output context.
        @return: String value.
        """
        ...

    def setValue(self, val, view='default') -> None:
        """
        self.setValue(val, view='default') -> None

        Set value of knob.
        @param val: The new value.
        @param view: Optional parameter specifying which view to set the value for. If omitted, the value will be set for the default view.
        @return: None
        """
        ...

    def splitView(self, view=None) -> None:
        """
        self.splitView(view) -> None.
        Split the view away from the current knob value.
        @param view: Optional view. Default is current view.
        @return: None.
        """
        ...

    def unsplitView(self, view=None) -> None:
        """
        self.unsplitView(view) -> None.
        Unsplit the view so that it shares a value with other views.
        @param view: Optional view. Default is current view.
        @return: None.
        """
        ...
