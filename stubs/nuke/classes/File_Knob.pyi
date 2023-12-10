from typing import *
from numbers import Number

import nuke

from . import *

class File_Knob(EvalString_Knob):
    """
    A knob which holds a filename. When it appears in a Node panel it provides a text field to show the filename and a button which opens the file chooser dialog.
    """
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

    def __new__(self,*args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def getEvaluatedValue(self,) -> str:
        """
        self.getEvaluatedValue() -> String.
        Returns the string on this knob, will be normalized to technical notation if sequence (%4d).
        @return: String.
        """
        ...

    def getEvaluatedValue(self,) -> str:
        """
        self.getEvaluatedValue() -> String.
        Returns the string on this knob, will be normalized to technical notation if sequence (%4d).
        @return: String.
        """
        ...

    def getValue(self,oc) -> str:
        """
        self.getValue(oc) -> String.
        Returns the string on this knob, will be normalized to technical notation if sequence (%4d). Will also evaluate the string for any tcl expressions
        @parm oc: the output context to use, if None the knob uiContext will be used.
        @return: String.
        """
        ...

    def fromUserText(self, s:str) -> None:
        """
        self.fromUserText(s) -> None.
        Assign string to knob, parses frame range off the end and opens file to get set the format.
        @param s: String to assign.
        @return: None.
        """
        ...

    def fromScript(self, s:str) -> None:
        """
        self.fromScript(s) -> None.
        Assign string to knob.
        @param s: String to assign.
        @return: None.
        """
        ...

    def fromScript(self, s:str) -> None:
        """
        self.fromScript(s) -> None.
        Assign string to knob.
        @param s: String to assign.
        @return: None.
        """
        ...
