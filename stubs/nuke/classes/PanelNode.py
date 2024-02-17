"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class PanelNode(object):
    """
    PanelNode
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

    def __str__(self, ) -> None:
        """
        Return str(self).
        """
        ...

    def addKnob(self, k: Knob) -> None:
        """
        self.addKnob(k) -> None.
        Add knob k to this node or panel.
        @param k: Knob.
        @return: None.
        """
        ...

    def removeKnob(self, k: Knob) -> None:
        """
        self.removeKnob(k) -> None.
        Remove knob k from this node or panel. Throws a ValueError exception if k is not found on the node.
        @param k: Knob.
        @return: None.
        """
        ...

    def readKnobs(self, s: str) -> None:
        """
        self.readKnobs(s) -> None.
        Read the knobs from a string (TCL syntax).
        @param s: A string.
        @return: None.
        """
        ...

    def writeKnobs(self, i) -> str:
        """
        self.writeKnobs(i) -> String in .nk form.
        Return a tcl list. If TO_SCRIPT | TO_VALUE is not on, this is a simple list
        of knob names. If it is on, it is an alternating list of knob names
        and the output of to_script().

        Flags can be any of these or'd together:
        - nuke.TO_SCRIPT produces to_script(0) values
        - nuke.TO_VALUE produces to_script(context) values
        - nuke.WRITE_NON_DEFAULT_ONLY skips knobs with not_default() false
        - nuke.WRITE_USER_KNOB_DEFS writes addUserKnob commands for user knobs
        - nuke.WRITE_ALL writes normally invisible knobs like name, xpos, ypos

        @param i: The set of flags or'd together. Default is TO_SCRIPT | TO_VALUE.
        @return: String in .nk form.
        """
        ...

    def knobs(self,) -> dict:
        """
        self.knobs() -> dict

        Get a dictionary of (name, knob) pairs for all knobs in this node.

        For example:

           >>> b = nuke.nodes.Blur()
           >>> b.knobs()

        @return: Dictionary of all knobs.

        Note that this doesn't follow the links for Link_Knobs
        """
        ...

    def createWidget(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Create the widget for the panel
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
