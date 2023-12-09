import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class Bin(Object):
    """
    Container object for hiero.core.BinItem objects (wrapping hiero.core.Clip and hiero.core.Sequence objects) and other hiero.core.Bin objects.
    """

    def __repr__(self) -> object:
        """
        Return repr(self).
        """
        ...

    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

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

    def __lt__(self, value, ) -> None:
        """
        Return self<value.
        """
        ...

    def __le__(self, value, ) -> None:
        """
        Return self<=value.
        """
        ...

    def __eq__(self, value, ) -> None:
        """
        Return self==value.
        """
        ...

    def __ne__(self, value, ) -> None:
        """
        Return self!=value.
        """
        ...

    def __gt__(self, value, ) -> None:
        """
        Return self>value.
        """
        ...

    def __ge__(self, value, ) -> None:
        """
        Return self>=value.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def __bool__(self, ) -> None:
        """
        self != 0
        """
        ...

    def __getitem__(self, key, ) -> None:
        """
        Return self[key].
        """
        ...

    def __len__(self, ) -> None:
        """
        Return len(self).
        """
        ...

    def __contains__(self, key, ) -> None:
        """
        Return key in self.
        """
        ...

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def addItem(self, *args, **kwargs) -> Any:
        """
        self.addItem(object) -> adds the item to the bin object.

        @param object: hiero.core.Bin, hiero.core.BinItem, or hiero.core.Tag object, to be added as a sub item of the bin object
        @return: Added object
        """
        ...

    def bins(self) -> object:
        """
        self.bins() -> returns a tuple with all of the sub bins contained by this object.

        @return: tuple of hiero.core.Bin objects
        """
        ...

    def clips(self) -> object:
        """
        self.clips() -> returns a tuple with all of the BinItem's containing clips contained by this bin.

        @return: tuple of hiero.core.BinItem objects
        """
        ...

    def color(self) -> PySide2.QtGui.QColor:
        """
        self.color() -> Get the bin display color, or an invalid QColor if not set.

        @return: PySide2.QtGui.QColor
        """
        ...

    def createClip(self, *args, **knobs) -> Clip:
        """
        self.createClip(path, **knobs) -> Construct a clip from a path and optional knob values, and add it to the bin.

        @param path: path to use, may contain expressions
        @param knobs: keyword args for specifying additional knobs to set
        @return: the created Clip
        """
        ...

    def deserializeChildItem(self, data: str, index: int) -> None:
        """

        """
        ...

    def displayColor(self) -> PySide2.QtGui.QColor:
        """
        self.displayColor() -> Returns the bin's color if one is set, otherwise returns the preference color associated with this bin.

        @return: PySide2.QtGui.QColor
        """
        ...

    def guid(self) -> object:
        """

        """
        ...

    def importFolder(self, arg__1: str) -> core.Bin:
        """
        self.importFolder(path) -> imports the media in the path into this bin (needs a project).

        @param path: path to the media to import
        @return Bin: returns the bin created for imported media
        """
        ...

    def importSequence(self, filename: str, timeBase: core.TimeBase = Default(self, Hiero.Python.TimeBase), frameRate: float = 0.0, dropFrame: bool = False) -> core.Sequence:
        """
        self.importSequence(filename, timeBase=None, frameRate=None, dropFrame=False) -> imports the sequence stored in filename into this bin (needs a project).  If the timebase/frame rate for the sequence isnot specified, the project defaults will be used.

        @param filename: path to the file to import the sequence from
        @param timeBase: optional argument of type hiero.core.TimeBase specifying the timebase for the created sequence
        @param frameRate: optional float argument specifying the frame rate for the created sequence
        @return: hiero.core.Sequence the created sequence
        """
        ...

    def isNull(self) -> bool:
        """
        self.isNull() -> returns True if the object is invalid.

        @return: True or False
        """
        ...

    def items(self, *args, **kwargs) -> tuple:
        """
        self.items(typeFilter) -> returns a tuple with all of the objects contained by this bin, filtered by the typeFilter argument, if supplied.

        @param typeFilter: combination of hiero.core.Bin.ItemType flags
        @return: tuple of hiero.core.BinItem objects
        """
        ...

    def moveItem(self, *args, **kwargs) -> None:
        """

        """
        ...

    def name(self) -> str:
        """
        self.name() -> returns the name of the bin.

        @return: True or False
        """
        ...

    def numChildren(self) -> int:
        """
        self.numChildren() -> returns the number of child objects contained by this bin.

        @return: int
        """
        ...

    def parentBin(self) -> object:
        """
        self.parentBin() -> returns the bin that contains this object.

        @return: hiero.core.Bin object
        """
        ...

    def project(self) -> object:
        """
        self.project() -> returns the Project object that this is attached to, or None if the object is not attached to a project.

        @return: hiero.core.Project object
        """
        ...

    def reconnectMedia(self, path: str) -> None:
        """
        self.reconnectMedia(path) -> For any Clips or Sequences in the bin, reconnects media found in the specified path.

        @param path: path containing media to reconnect to
        """
        ...

    def removeItem(self, *args, **kwargs) -> Any:
        """
        self.removeItem(object) -> removes the item from the bin object. If the object is not a child item of the bin object, throws an exception.

        @param object: hiero.core.Bin, hiero.core.BinItem, or hiero.core.Tag object to be removed as a sub item of the bin object
        """
        ...

    def sequences(self) -> object:
        """
        self.sequences() -> returns a tuple with all of the BinItem's containing sequences contained by this bin.

        @return: tuple of hiero.core.BinItem objects
        """
        ...

    def serialize(self) -> str:
        """

        """
        ...

    def setColor(self, arg__1: PySide2.QtGui.QColor) -> None:
        """
        self.setColor(color) -> Set the bin display color.

        @param color: the color to set, as a PySide2.QtGui.QColor, a string (e.g. '#ff0000') or an integer containing the RGB components (e.g. 0x11aa33).
        """
        ...

    def setName(self, name: str) -> None:
        """
        self.setName(name) -> set the name of the bin.
        """
        ...

    def syncName(self, name: str) -> None:
        """
        self.syncName(name) -> set the name of the bin without sending additional notifications.
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

    ItemType: Any = None
    kNone: Any = None
    kClip: Any = None
    kSequence: Any = None
    kBin: Any = None
    kTag: Any = None
