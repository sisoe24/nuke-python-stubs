"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class Channel_Knob(Knob):
    """
    A knob which lets you select a layer and enable or disable individual channels.
    self.__init__(s, label, depth) -> None
    Constructor.
    @param s: name.
    @param label: Optional name to appear in GUI. Defaults to the knob's name.
    @param depth: Optional number of channels with zero being the Nuke default number of channels. Defaults to 0.
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

    def layerSelector(self,) -> bool:
        """
        self.layerSelector() -> bool
        """
        ...

    def channelSelector(self,) -> bool:
        """
        self.channelSelector() -> bool
        """
        ...

    def checkMarks(self,) -> bool:
        """
        self.checkMarks() -> bool
        """
        ...

    def isChannelEnabled(self, name: str) -> bool:
        """
        self.isChannelEnabled(name) -> bool

        Test if a channel is enabled.
        @param name: The name of the channel.@return: True if the channel is enabled, False otherwise.
        """
        ...

    def enableChannel(self, name: str, b: bool) -> None:
        """
        self.enableChannel(name, b) -> None

        Enable or disable a channel.
        @param name: The name of the channel.
        @param b: True to enable the channel, False to disable it.
        @return: None
        """
        ...

    def setEnable(self, name: str) -> None:
        """
        self.setEnable(name) -> None

        Enable a channel.
        @param name: The name of the channel to enable.
        @return: None
        """
        ...

    def depth(self,) -> int:
        """
        self.depth() -> int

        Get the channel depth.
        @return: The depth of the channel as an int.
        """
        ...

    def inputKnob(self,) -> bool:
        """
        self.inputKnob() -> bool
        """
        ...

    def inputNumber(self,) -> int:
        """
        self.inputNumber() -> int
        """
        ...

    def setInput(self, num: int | float) -> None:
        """
        self.setInput(num) -> None
        Set the input number for this knob.@param num: The number of the new input.
        @return: None
        """
        ...

    def value(self,) -> str:
        """
        self.value() -> str
        Get the name of the selected channel.
        @return: The name of the channel as a string.
        """
        ...

    def setValue(self, name: str) -> None:
        """
        self.setValue(name) -> None
        Set the selected channel using the channel name.
        @param name: The name of the new channel as a string.
        @return: None
        @raise ValueError exception if the channel doesn't exist.
        """
        ...
