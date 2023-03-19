import typing
from typing import *
from numbers import Number

import core
import PySide2

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
        return object()

    def __lt__(self, value, ):
        """
        Return self<value.
        """
        return None

    def __le__(self, value, ):
        """
        Return self<=value.
        """
        return None

    def __eq__(self, value, ):
        """
        Return self==value.
        """
        return None

    def __ne__(self, value, ):
        """
        Return self!=value.
        """
        return None

    def __gt__(self, value, ):
        """
        Return self>value.
        """
        return None

    def __ge__(self, value, ):
        """
        Return self>=value.
        """
        return None

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def __bool__(self, ):
        """
        self != 0
        """
        return None

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def copy(self) -> core.Tag:
        """

        """
        return core.Tag()

    def guid(self) -> str:
        """
        self.guid() -> Return the Tag guid.

        @return: object guid as string
        """
        return str()

    def icon(self) -> str:
        """
        self.icon() -> returns the tags icon path.
        If the file doesn't exist, it will search for it in the plugin paths and the project folder and return the located file.

        @return: string
        """
        return str()

    def inTime(self) -> int:
        """
        self.inTime() -> returns the in time of the tag.

        @return: frame
        """
        return int()

    def isNull(self) -> bool:
        """
        self.isNull() -> returns True if the tag is invalid, False otherwise.

        @return: True or False
        """
        return bool()

    def metadata(self) -> core.DataCollection:
        """
        self.metadata() -> returns the clip's metadata.

        @return: hiero.core.DataCollection object
        """
        return core.DataCollection()

    def name(self) -> str:
        """
        self.name() -> returns the label of the tag.

        @return: string
        """
        return str()

    def note(self) -> str:
        """
        self.note() -> returns the note on the tag.

        @return: string
        """
        return str()

    def outTime(self) -> int:
        """
        self.outTime() -> returns the out time of the tag.

        @return: frame
        """
        return int()

    def parentBin(self) -> object:
        """

        """
        return object()

    def project(self) -> object:
        """
        self.project() -> returns the Project object that this is attached to, or None if the object is not attached to a project.

        @return: hiero.core.Project object
        """
        return object()

    def serialize(self) -> str:
        """

        """
        return str()

    def setIcon(self, iconPath: str) -> None:
        """
        self.setIcon() -> sets the icon on the tag.

        @param note: path to icon file
        """
        return None

    def setInTime(self, time: int) -> None:
        """
        self.setInTime(time) -> set the in time of the tag.

        @param time: the in time
        """
        return None

    def setName(self, name: str) -> None:
        """
        self.setName() -> sets the name label of the tag.

        @param name: name to assign to tag
        """
        return None

    def setNote(self, note: str) -> None:
        """
        self.setNote() -> sets the note on the tag.

        @param note: string note to assign to tag
        """
        return None

    def setOutTime(self, time: int) -> None:
        """
        self.setOutTime(time) -> set the out time of the tag.

        @param time: the out time
        """
        return None

    def setVisible(self, visible: bool) -> None:
        """
        self.setVisible() -> sets the visiblity of the tag.

        @param visible: visibility state
        """
        return None

    def syncName(self, name: str) -> None:
        """
        self.syncName(name) -> set the name of the tag without sending additional notifications.
        """
        return None

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        return str()

    def visible(self) -> bool:
        """
        self.visible() -> gets the visiblity state of the tag.

        @return: bool
        """
        return bool()

    def __copy__(self,) -> None:
        """

        """
        return None

    __hash__: Any = None
