from typing import *
from numbers import Number

import nuke

from . import *


class Link_Knob(Knob):
    """
    Link_Knob
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

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def value(self,) -> str:
        """
        value() -> string

        Return value of knob.
        """
        ...

    def setValue(self,) -> None:
        """
        setValue() -> None

        Set value of knob.
        """
        ...

    def setLink(self, s) -> None:
        """
        setLink(s) -> None
        """
        ...

    def makeLink(self, s, t) -> None:
        """
        makeLink(s, t) -> None
        """
        ...

    def getLinkedKnob(self,) -> knob:
        """
        getLinkedKnob() -> knob
        """
        ...

    def getLink(self,) -> Any:
        """
        getLink() -> s
        """
        ...

    def applyOverride(self,) -> bool:
        """
        applyOverride() -> bool
        This function only affects link knobs that are placed on a LiveGroup node. It replaces the value of the linked knob in the live group with the value set in the LiveGroup node.
        """
        ...

    def revertOverride(self,) -> bool:
        """
        revertOverride() -> bool
        This function only affects link knobs that are placed on a LiveGroup node. When called the LinkKnob will revert to the linked knob value and will follow it after reloads.
        """
        ...
