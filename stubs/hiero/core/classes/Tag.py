import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class Tag(Object):
    """
    Object representing a tag in Hiero.
    Can be created with a string name, an optional path to an icon and an optional editable (in gui) boolean parameter
    """

    def __repr__(self) -> object:
        """
        Return repr(self).
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

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def copy(self) -> core.Tag:
        """

        """
        ...

    def guid(self) -> str:
        """
        self.guid() -> Return the Tag guid.

        @return: object guid as string
        """
        ...

    def icon(self) -> str:
        """
        self.icon() -> returns the tags icon path.
        If the file doesn't exist, it will search for it in the plugin paths and the project folder and return the located file.

        @return: string
        """
        ...

    def inTime(self) -> int:
        """
        self.inTime() -> returns the in time of the tag.

        @return: frame
        """
        ...

    def isNull(self) -> bool:
        """
        self.isNull() -> returns True if the tag is invalid, False otherwise.

        @return: True or False
        """
        ...

    def metadata(self) -> core.DataCollection:
        """
        self.metadata() -> returns the clip's metadata.

        @return: hiero.core.DataCollection object
        """
        ...

    def name(self) -> str:
        """
        self.name() -> returns the label of the tag.

        @return: string
        """
        ...

    def note(self) -> str:
        """
        self.note() -> returns the note on the tag.

        @return: string
        """
        ...

    def outTime(self) -> int:
        """
        self.outTime() -> returns the out time of the tag.

        @return: frame
        """
        ...

    def parentBin(self) -> object:
        """

        """
        ...

    def project(self) -> object:
        """
        self.project() -> returns the Project object that this is attached to, or None if the object is not attached to a project.

        @return: hiero.core.Project object
        """
        ...

    def serialize(self) -> str:
        """

        """
        ...

    def setIcon(self, iconPath: str) -> None:
        """
        self.setIcon() -> sets the icon on the tag.

        @param note: path to icon file
        """
        ...

    def setInTime(self, time: int) -> None:
        """
        self.setInTime(time) -> set the in time of the tag.

        @param time: the in time
        """
        ...

    def setName(self, name: str) -> None:
        """
        self.setName() -> sets the name label of the tag.

        @param name: name to assign to tag
        """
        ...

    def setNote(self, note: str) -> None:
        """
        self.setNote() -> sets the note on the tag.

        @param note: string note to assign to tag
        """
        ...

    def setOutTime(self, time: int) -> None:
        """
        self.setOutTime(time) -> set the out time of the tag.

        @param time: the out time
        """
        ...

    def setVisible(self, visible: bool) -> None:
        """
        self.setVisible() -> sets the visiblity of the tag.

        @param visible: visibility state
        """
        ...

    def syncName(self, name: str) -> None:
        """
        self.syncName(name) -> set the name of the tag without sending additional notifications.
        """
        ...

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        ...

    def visible(self) -> bool:
        """
        self.visible() -> gets the visiblity state of the tag.

        @return: bool
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...

    __hash__: Any = None
