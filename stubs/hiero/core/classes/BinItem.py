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


class BinItem(Object):
    """
    Generic object wrapper with shared functionality for sequences and clips.
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

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
        True if self else False
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

    def activeItem(self) -> None:
        """
        self.activeItem() -> returns the item contained by this bin item.

        @return: hiero.core.Clip or hiero.core.Sequence object
        """
        ...

    def activeVersion(self) -> core.Version:
        """
        self.activeVersion() -> gets the currently active Version object of the bin item.

        @return: hiero.core.Version object
        """
        ...

    def addSnapshot(self, *args: typing.Any, **kwargs: typing.Any) -> Snapshot:
        """
        self.addSnapshot(comment) -> adds a new snapshot for the object, with a comment.
        self.addSnapshot(sequence, comment) -> adds a new snapshot for the object, using the sequence as the new snapshot, setting the comment.

        @param comment: a comment string to set on the snapshot
        @param sequence: a hiero.core.Sequence object to create the Snapshot from
        @return: hiero.core.Snapshot object
        """
        ...

    def addVersion(self, version: core.Version, position: int = -1) -> core.Version:
        """
        self.addVersion(version) -> adds the version parameter to the bin item.

        @param version: hiero.core.Version object for the new version
        @param position: position at which the new Version must be inserted, if -1 then insert at end
        @return: hiero.core.Version object
        """
        ...

    def clone(self, *args, **kwargs) -> BinItem:
        """
        self.clone() -> returns a deep copy of this object.

        @return: hiero.core.BinItem object

        WARNING - DEPRECATED ( clone ): This method is deprecated and will not be present in future versions of the Python API.
        This method has been replaced by copy().
        """
        ...

    def color(self) -> PySide2.QtGui.QColor:
        """
        self.color() -> Get the bin item display color, or an invalid QColor if not set.

        @return: PySide2.QtGui.QColor
        """
        ...

    def copy(self) -> object:
        """
        self.copy() -> returns a deep copy of this object.

        @return: hiero.core.BinItem object
        """
        ...

    def createClipVersion(self, *args, **knobs) -> Version:
        """
        self.createClipVersion(position, path, **knobs) -> Construct a clip from a path and optional knob values, and add it as a new version. Raises RuntimeError if creating the clip fails or the path already exists as a version.

        @param position: position at which the new Version must be inserted, if -1 then insert at end
        @param path: path to use, may contain expressions
        @param knobs: keyword args for specifying additional knobs to set
        @return: the created Version
        """
        ...

    def deserializeChildItem(self, data: str, index: int) -> None:
        """

        """
        ...

    def displayColor(self) -> PySide2.QtGui.QColor:
        """
        self.displayColor() -> Returns the item's color if one is set, otherwise returns the preference color associated with this item type.

        @return: PySide2.QtGui.QColor
        """
        ...

    def guid(self) -> object:
        """

        """
        ...

    def hasVersion(self, *args: typing.Any, **kwargs: typing.Any) -> Union[True, False]:
        """
        self.hasVersion(index) -> checks if a given version exists and is valid.

        @param index: index of the version to check for
        @return: True or False
        """
        ...

    def isClipVersion(self, clip: core.Clip) -> bool:
        """
        self.isClipVersion(index) -> checks if a given clip belongs to this BinItem as a version.

        @param clip: Clip to look for
        @return: True or False
        """
        ...

    def isNull(self) -> bool:
        """
        self.isNull() -> returns True if the object contains a invalid hiero.core.Sequence or hiero.core.Clip object.

        @return: True or False
        """
        ...

    def items(self) -> object:
        """
        self.items() -> returns a tuple containing all of the different versions of this object.

        @return: tuple of hiero.core.Version objects
        """
        ...

    def maxVersion(self) -> core.Version:
        """
        self.maxVersion() -> finds the maximum (last) version and sets it as the active version on this bin item and any linked TrackItems. Offline versions and hidden versions will be ignored during the search.

        @return: hiero.core.Version object
        """
        ...

    def minVersion(self) -> core.Version:
        """
        self.minVersion() -> finds the minimum (first) version and sets it as the active version on this bin item and any linked TrackItems. Offline versions and hidden versions will be ignored during the search.

        @return: hiero.core.Version object
        """
        ...

    def name(self) -> str:
        """
        self.name() -> returns the name of the item.

        @return: string
        """
        ...

    def nextVersion(self) -> core.Version:
        """
        self.nextVersion() -> finds the next version and sets it as the active version on this bin item and any linked TrackItems. Offline versions and hidden versions will be ignored during the search.

        @return: hiero.core.Version object
        """
        ...

    def numSnapshots(self) -> int:
        """
        self.numSnapshots() -> returns the number of snapshots that this bin item has.

        @return: int
        """
        ...

    def numVersions(self) -> int:
        """
        self.numVersions() -> returns the number of versions for this bin item.

        @return: int
        """
        ...

    def parentBin(self) -> object:
        """
        self.parentBin() -> returns the bin object that contains this bin item.

        @return: hiero.core.Bin object
        """
        ...

    def prevVersion(self) -> core.Version:
        """
        self.prevVersion() -> finds the previous version and sets it as the active version on this bin item and any linked TrackItems. Offline versions and hidden versions will be ignored during the search.

        @return: hiero.core.Version object
        """
        ...

    def project(self) -> object:
        """
        self.project() -> returns the Project object that this object is attached to, or None if the object is not attached to a project.

        @return: heiro.core.Project object
        """
        ...

    def removeVersion(self, version: core.Version) -> None:
        """
        self.removeVersion(version) -> remove a version from the BinItem. The version must not currently be in use in the project.

        @param version: hiero.core.Version object to be removed
        """
        ...

    def restoreToSnapshot(self, index: int) -> None:
        """
        self.restoreToSnapshot(index) -> adds a new snapshot for the object, with a comment.

        @param index: index of the Snapshot to restore from. Generates an exception if the index is out of range
        """
        ...

    def serialize(self) -> str:
        """

        """
        ...

    def setActiveVersion(self, version: core.Version) -> core.Version:
        """
        self.setActiveVersion(version) -> sets the active version to the version parameter.
        @return: hiero.core.Version object
        """
        ...

    def setActiveVersionIndex(self, *args, **kwargs) -> Version:
        """
        self.setActiveVersionIndex(version) -> sets the currently active version by index.

        @param index: index of the version to make active
        @return: hiero.core.Version object

        WARNING - DEPRECATED ( setActiveVersionIndex ): This method is deprecated and will not be present in future versions of the Python API.
        Version indices are no longer unique identifiers and should not be used as such. Please use BinItem.setActiveVersion() instead.
        """
        ...

    def setColor(self, arg__1: PySide2.QtGui.QColor) -> None:
        """
        self.setColor(color) -> Set the bin item display color.

        @param color: the color to set, as a PySide2.QtGui.QColor, a string (e.g. '#ff0000') or an integer containing the RGB components (e.g. 0x11aa33).
        """
        ...

    def setName(self, name: str) -> None:
        """
        self.setName(name) -> set the name of the item.
        """
        ...

    def snapshots(self) -> object:
        """
        self.snapshots() -> returns a tuple of all of the snapshots contained by this object.

        @return: tuple of hiero.core.Snapshot objects
        """
        ...

    def syncName(self, name: str) -> None:
        """
        self.syncName(name) -> set the name of the item without sending additional notifications.
        """
        ...

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        ...

    def version(self, *args: typing.Any, **kwargs: typing.Any) -> Version:
        """
        self.version(index) -> gets a Version object for the version of the bin item specified by the index.

        @param index: index of the version to get
        @return: hiero.core.Version object
        """
        ...

    def versionDown(self, *args, **kwargs) -> Version:
        """
        self.versionDown() -> decrements the current/active version and returns the newly active Version object of the bin item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionDown ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from BinItem. To find new versions, please use hiero.core.VersionScanner. To obtain the next version, please use BinItem.prevVersion().
        """
        ...

    def versionMaxAvailable(self, *args, **kwargs) -> Version:
        """
        self.versionMaxAvailable() -> finds the highest version that is currently loaded and does not have missing or offline media and sets it as the active version on this bin item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionMaxAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from BinItem. This method has been replaced by BinItem.maxVersion().
        """
        ...

    def versionMinAvailable(self, *args, **kwargs) -> Version:
        """
        self.versionMinAvailable() -> finds the lowest version that is currently loaded and does not have missing or offline media and sets it as the active version on this bin item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionMinAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from BinItem. This method has been replaced by BinItem.minVersion().
        """
        ...

    def versionNextAvailable(self, *args, **kwargs) -> Version:
        """
        self.versionNextAvailable() -> finds the next (higher) version that is currently loaded and does not have missing or offline media and sets it as the active version on this bin item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionNextAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from BinItem. This method has been replaced by BinItem.nextVersion().
        """
        ...

    def versionPrevAvailable(self, *args, **kwargs) -> Version:
        """
        self.versionPrevAvailable() -> finds the prev (lower) version that is currently loaded and does not have missing or offline media and sets it as the active version on this bin item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionPrevAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from BinItem. This method has been replaced by BinItem.prevVersion().
        """
        ...

    def versionUp(self, *args, **kwargs) -> Version:
        """
        self.versionUp() -> increments the current/active version and returns the newly active Version object of the bin item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionUp ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from BinItem. To find new versions, please use hiero.core.VersionScanner. To obtain the next version, please use BinItem.nextVersion().
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...
