from typing import *
from numbers import Number

import nuke

from . import *


class Script_Knob(String_Knob):
    """
    A button which executes a TCL script.
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

    def command(self,) -> str:
        """
        self.command() -> str

        Get the current command.
        @return: The current command as a string, or None if there is no current command.
        """
        ...

    def value(self,) -> str:
        """
        self.value() -> str

        Get the current command.
        @return: The current command as a string, or None if there is no current command.
        """
        ...

    def setCommand(self, cmd: str) -> None:
        """
        self.setCommand(cmd) -> None
        Set the new command for this knob.
        @param cmd: String containing a TCL command.
        @return: None.
        """
        ...

    def setValue(self, cmd: str) -> None:
        """
        self.setValue(cmd) -> None
        Set the new command for this knob.
        @param cmd: String containing a TCL command.
        @return: None.
        """
        ...

    def execute(self,) -> None:
        """
        self.execute() -> None
        Execute the command.
        @return: None.
        """
        ...
