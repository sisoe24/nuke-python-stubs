import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class EffectTrackItem(SubTrackItem):
    """
    Class representing an effect on a sequence.  EffectTrackItem is derived from SubTrackItem and thus EffectTrackItem objects can be placed and trimmed on VideoTrack subtracks.
    The effect's node can be accessed with effect.node(), which can then be manipulated through the nuke Node API.To create effects, it is recommended you use the hiero.core.VideoTrack.createEffect() method.

    Usage:
    EffectTrackItem(effectType)
    EffectTrackItem(effectType, timelineIn, timelineOut)
    """

    def __setattr__(self, name, value, ) -> None:
        """
        Implement setattr(self, name, value).
        """
        ...

    def __delattr__(self, name, ) -> None:
        """
        Implement delattr(self, name).
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

    def clone(self) -> object:
        """
        self.clone() -> returns a deep copy of this object but, unlike copy(), this clones the underlying Nuke node so that the knobs are shared.
        """
        ...

    def copy(self) -> object:
        """
        self.copy() -> returns a deep copy of this object.
        """
        ...

    def declone(self) -> None:
        """
        self.declone() -> Declones the effect item. Has no effect if the item is not a clone.
        """
        ...

    def isValid(self) -> bool:
        """
        self.isValid() -> Returns true if the effect item is in a valid state and position and false otherwise.
        """
        ...

    def node(self) -> object:
        """
        self.node() -> Node

        Get the node used to apply the effect.

        @return: The effect node.
        """
        ...

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...

    def _EffectTrackItem_addToNukeScript(self, script, offset=0, inputs=1, startHandle=0, endHandle=0, addLifetime=True) -> None:
        """

        """
        ...

    def _EffectTrackItem_isRetimeEffect(self) -> None:
        """
        Check if an EffectTrackItem applies a retime.  Currently this only applies to TimeWarp effects.
        """
        ...

    def __EffectTrackItem_name(self) -> str:
        """
        self.name() -> Get the name of the effect's node.

        @return: string
        """
        ...

    def __EffectTrackItem_setName(self, name) -> None:
        """
        self.setName() -> Set the name of the effect's node.
        """
        ...
