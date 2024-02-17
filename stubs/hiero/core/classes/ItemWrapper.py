"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import ui
import core
import hiero
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class ItemWrapper:
    """

    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def __bool__(self, ) -> None:
        """
        True if self else False
        """
        ...

    def bin(self) -> core.Bin:
        """
        self.bin() -> converts this ItemWrapper to a hiero.core.Bin object. If the item wrapper isn't wrapping a Bin object, it will return a non-functioning (isNull returns True) TrackItem object (meaning that it has all of the methods of a Bin object, but the methods don't do anything)

        @return: hiero.core.Bin object
        """
        ...

    def binItem(self) -> core.BinItem:
        """
        self.binItem() -> converts this ItemWrapper to a hiero.core.BinItem object. If the item wrapper isn't wrapping a BinItem object, it will return a non-functioning (isNull returns True) TrackItem object (meaning that it has all of the methods of a BinItem object, but the methods don't do anything)

        @return: hiero.core.BinItem object
        """
        ...

    def clip(self) -> core.Clip:
        """
        self.clip() -> converts this ItemWrapper to a hiero.core.Clip object. If the item wrapper isn't wrapping a Clip object, it will return a non-functioning (isNull returns True) Clip object (meaning that it has all of the methods of a Clip object, but the methods don't do anything)

        @return: hiero.core.Clip object
        """
        ...

    def ignore(self) -> bool:
        """

        """
        ...

    def isNull(self) -> bool:
        """
        self.isNull() -> returns True if this is a invalid or uninitialized item, or False otherwise

        @return: True or False
        """
        ...

    def item(self) -> object:
        """
        self.item() -> Return the item contained within this wrapper.

        @return: hiero.core.Sequence | hiero.core.Clip | hiero.core.TrackItemBase | hiero.core.BinItem
        """
        ...

    def name(self) -> str:
        """
        self.name() -> Returns item name.

        @return: string
        """
        ...

    def root(self) -> core.Bin:
        """
        self.root() -> the root is the highest level in the bin selected for export, Root may be null.

        @return: hiero.core.Bin object
        """
        ...

    def sequence(self) -> core.Sequence:
        """
        self.sequence() -> converts this ItemWrapper to a hiero.core.Sequence object. If the item wrapper isn't wrapping a Sequence object, it will return a non-functioning (isNull returns True) Sequence object (meaning that it has all of the methods of a Sequence object, but the methods don't do anything)

        @return: hiero.core.Sequence object
        """
        ...

    def setTrackItemsForViews(self, items: typing.List[core.TrackItemBase]) -> None:
        """

        """
        ...

    def trackItem(self) -> core.TrackItemBase:
        """
        self.trackItem() -> converts this ItemWrapper to a hiero.core.TrackItemBase object. If the item wrapper isn't wrapping a TrackItem object, it will return a non-functioning (isNull returns True) TrackItem object (meaning that it has all of the methods of a TrackItem object, but the methods don't do anything)

        @return: hiero.core.TrackItem object
        """
        ...

    def trackItemsForViews(self) -> typing.List[core.TrackItemBase]:
        """

        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...

    @property
    def _ignore(self) -> typing.Any:
        """

        """
        ...
