from typing import *
from numbers import Number

import nuke

from . import *

class MultiView_Knob(Knob):
    """
    MultiView_Knob
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

    def fromScript(self,s) -> bool:
        """
        fromScript(s) -> True if succeeded, False otherwise.

        Initialise from script s.
        """
        ...

    def fromScript(self,s) -> bool:
        """
        fromScript(s) -> True if succeeded, False otherwise.

        Initialise from script s.
        """
        ...

    def toScriptPrefix(self,*args, **kwargs) -> None:
        """

        """
        ...

    def toScriptPrefixUserKnob(self,*args, **kwargs) -> None:
        """

        """
        ...

    def notDefault(self,) -> bool:
        """
        notDefault() -> True if set to its default value, False otherwise.
        """
        ...

    def toScript(self,quote, context=None) -> str:
        """
        toScript(quote, context=current) -> string.

        Return the value of the knob in script syntax.
        Pass True for quote to return results quoted in {}.
        Pass None for context to get results for all views and key times (as stored in a .nk file).
        """
        ...

    def toScript(self,quote, context=None) -> str:
        """
        toScript(quote, context=current) -> string.

        Return the value of the knob in script syntax.
        Pass True for quote to return results quoted in {}.
        Pass None for context to get results for all views and key times (as stored in a .nk file).
        """
        ...
