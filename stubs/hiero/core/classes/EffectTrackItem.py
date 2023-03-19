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

    def __setattr__(self, name, value, ):
        """
        Implement setattr(self, name, value).
        """
        return None

    def __delattr__(self, name, ):
        """
        Implement delattr(self, name).
        """
        return None

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def clone(self) -> object:
        """
        self.clone() -> returns a deep copy of this object but, unlike copy(), this clones the underlying Nuke node so that the knobs are shared.
        """
        return object()

    def copy(self) -> object:
        """
        self.copy() -> returns a deep copy of this object.
        """
        return object()

    def declone(self) -> None:
        """
        self.declone() -> Declones the effect item. Has no effect if the item is not a clone.
        """
        return None

    def isValid(self) -> bool:
        """
        self.isValid() -> Returns true if the effect item is in a valid state and position and false otherwise.
        """
        return bool()

    def node(self) -> object:
        """
        self.node() -> Node

        Get the node used to apply the effect.

        @return: The effect node.
        """
        return object()

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        return str()

    def __copy__(self,) -> None:
        """

        """
        return None

    def _EffectTrackItem_addToNukeScript(self, script, offset=0, inputs=1, startHandle=0, endHandle=0, addLifetime=True):
        """

        """
        return None

    def _EffectTrackItem_isRetimeEffect(self):
        """
        Check if an EffectTrackItem applies a retime.  Currently this only applies to TimeWarp effects.
        """
        return None

    def __EffectTrackItem_name(self):
        """
        self.name() -> Get the name of the effect's node.

        @return: string
        """
        return str()

    def __EffectTrackItem_setName(self, name):
        """
        self.setName() -> Set the name of the effect's node.
        """
        return None
