from typing import *
from numbers import Number

import nuke

from . import *

class LiveGroup(Precomp):
    """

    """
    def __repr__(self, ) -> None:
        """
        Return repr(self).
        """
        ...

    def __str__(self, ) -> None:
        """
        Return str(self).
        """
        ...

    def __len__(self, ) -> None:
        """
        Return len(self).
        """
        ...

    def __getitem__(self, key, ) -> None:
        """
        Return self[key].
        """
        ...

    def makeLocal(self,) -> None:
        """
        makeLocal() -> None
        Puts the LiveGroup into "local" state.
        WARNING: This function is deprecated. Use makeEditable() instead.
        """
        ...

    def isLocal(self,) -> bool:
        """
        isLocal() -> bool
        Checks if the LiveGroup is local.WARNING: This function is deprecated. Use published() instead.
        """
        ...

    def makeEditable(self,) -> None:
        """
        makeEditable() -> None
        Puts the LiveGroup into "editable" state.
        """
        ...

    def published(self,) -> bool:
        """
        published() -> bool
        Returns True if the LiveGroup is published.
        """
        ...

    def publishLiveGroup(self, file:Optional[str] = None) -> bool:
        """
        publishLiveGroup(file) -> bool

        Writes a LiveGroup to a file.

        :param file: (optional) The path to which we want to publish this LiveGroup. If None then write to the path currently defined by the file knob. If the file specified by this param already exists, Nuke will attempt to over write it without a warning. Otherwise a new file will be created.

        :return: bool. True if successful, else, False.
        """
        ...

    def applyOverride(self,) -> bool:
        """
        applyOverride() -> bool
        This function only affects link knobs that are placed on a LiveGroup type node. It replaces the value of the linked knob in the live group with the value set in the LiveGroup node.
        """
        ...

    def revertOverride(self,) -> bool:
        """
        revertOverride() -> bool
        This function only affects link knobs that are placed on a LiveGroup type node. When called the LinkKnob will revert to the linked knob value and will follow it after reloads.
        """
        ...

    def anyOverrides(self,) -> bool:
        """
        anyOverrides() -> bool
        If any of the exposed link knobs are overridden it returns with True.
        """
        ...

    def modified(self,) -> bool:
        """
        modified() -> bool
        Returns True if the anything within the livegroup has changed.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
