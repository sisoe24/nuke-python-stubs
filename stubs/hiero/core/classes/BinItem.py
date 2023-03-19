import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class BinItem(Object):
    """
    Generic object wrapper with shared functionality for sequences and clips.
    """

    def __repr__(self) -> object:
        """
        Return repr(self).
        """
        return None

    def __hash__(self, ):
        """
        Return hash(self).
        """
        return None

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

    def __getitem__(self, key, ):
        """
        Return self[key].
        """
        return None

    def __len__(self, ):
        """
        Return len(self).
        """
        return None

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def activeItem(self) -> None:
        """
        self.activeItem() -> returns the item contained by this bin item.

        @return: hiero.core.Clip or hiero.core.Sequence object
        """
        return Iterable()

    def activeVersion(self) -> core.Version:
        """
        self.activeVersion() -> gets the currently active Version object of the bin item.

        @return: hiero.core.Version object
        """
        return Version()

    def addSnapshot(self, *args, **kwargs):
        """
        self.addSnapshot(comment) -> adds a new snapshot for the object, with a comment.
        self.addSnapshot(sequence, comment) -> adds a new snapshot for the object, using the sequence as the new snapshot, setting the comment.

        @param comment: a comment string to set on the snapshot
        @param sequence: a hiero.core.Sequence object to create the Snapshot from
        @return: hiero.core.Snapshot object
        """
        return Snapshot()

    def addVersion(self, version: core.Version, position: int = -1) -> core.Version:
        """
        self.addVersion(version) -> adds the version parameter to the bin item.

        @param version: hiero.core.Version object for the new version
        @param position: position at which the new Version must be inserted, if -1 then insert at end
        @return: hiero.core.Version object
        """
        return Version()

    def clone(self, *args, **kwargs):
        """
        self.clone() -> returns a deep copy of this object.

        @return: hiero.core.BinItem object

        WARNING - DEPRECATED ( clone ): This method is deprecated and will not be present in future versions of the Python API.
        This method has been replaced by copy().
        """
        return BinItem()

    def color(self) -> PySide2.QtGui.QColor:
        """
        self.color() -> Get the bin item display color, or an invalid QColor if not set.

        @return: PySide2.QtGui.QColor
        """
        return Any

    def copy(self) -> object:
        """
        self.copy() -> returns a deep copy of this object.

        @return: hiero.core.BinItem object
        """
        return BinItem()

    def createClipVersion(self, *args, **knobs):
        """
        self.createClipVersion(position, path, **knobs) -> Construct a clip from a path and optional knob values, and add it as a new version. Raises RuntimeError if creating the clip fails or the path already exists as a version.

        @param position: position at which the new Version must be inserted, if -1 then insert at end
        @param path: path to use, may contain expressions
        @param knobs: keyword args for specifying additional knobs to set
        @return: the created Version
        """
        return Version()

    def deserializeChildItem(self, data: str, index: int) -> None:
        """

        """
        return None

    def displayColor(self) -> PySide2.QtGui.QColor:
        """
        self.displayColor() -> Returns the item's color if one is set, otherwise returns the preference color associated with this item type.

        @return: PySide2.QtGui.QColor
        """
        return Any

    def guid(self) -> object:
        """

        """
        return None

    def hasVersion(self, *args, **kwargs):
        """
        self.hasVersion(index) -> checks if a given version exists and is valid.

        @param index: index of the version to check for
        @return: True or False
        """
        return Union[True, False]

    def isClipVersion(self, clip: core.Clip) -> bool:
        """
        self.isClipVersion(index) -> checks if a given clip belongs to this BinItem as a version.

        @param clip: Clip to look for
        @return: True or False
        """
        return Union[True, False]

    def isNull(self) -> bool:
        """
        self.isNull() -> returns True if the object contains a invalid hiero.core.Sequence or hiero.core.Clip object.

        @return: True or False
        """
        return Union[True, False]

    def items(self) -> object:
        """
        self.items() -> returns a tuple containing all of the different versions of this object.

        @return: tuple of hiero.core.Version objects
        """
        return tuple()

    def maxVersion(self) -> core.Version:
        """
        self.maxVersion() -> finds the maximum (last) version and sets it as the active version on this bin item and any linked TrackItems. Offline versions and hidden versions will be ignored during the search.

        @return: hiero.core.Version object
        """
        return Version()

    def minVersion(self) -> core.Version:
        """
        self.minVersion() -> finds the minimum (first) version and sets it as the active version on this bin item and any linked TrackItems. Offline versions and hidden versions will be ignored during the search.

        @return: hiero.core.Version object
        """
        return Version()

    def name(self) -> str:
        """
        self.name() -> returns the name of the item.

        @return: string
        """
        return str()

    def nextVersion(self) -> core.Version:
        """
        self.nextVersion() -> finds the next version and sets it as the active version on this bin item and any linked TrackItems. Offline versions and hidden versions will be ignored during the search.

        @return: hiero.core.Version object
        """
        return Version()

    def numSnapshots(self) -> int:
        """
        self.numSnapshots() -> returns the number of snapshots that this bin item has.

        @return: int
        """
        return int()

    def numVersions(self) -> int:
        """
        self.numVersions() -> returns the number of versions for this bin item.

        @return: int
        """
        return int()

    def parentBin(self) -> object:
        """
        self.parentBin() -> returns the bin object that contains this bin item.

        @return: hiero.core.Bin object
        """
        return Bin()

    def prevVersion(self) -> core.Version:
        """
        self.prevVersion() -> finds the previous version and sets it as the active version on this bin item and any linked TrackItems. Offline versions and hidden versions will be ignored during the search.

        @return: hiero.core.Version object
        """
        return Version()

    def project(self) -> object:
        """
        self.project() -> returns the Project object that this object is attached to, or None if the object is not attached to a project.

        @return: heiro.core.Project object
        """
        return Project()

    def removeVersion(self, version: core.Version) -> None:
        """
        self.removeVersion(version) -> remove a version from the BinItem. The version must not currently be in use in the project.

        @param version: hiero.core.Version object to be removed
        """
        return None

    def restoreToSnapshot(self, index: int) -> None:
        """
        self.restoreToSnapshot(index) -> adds a new snapshot for the object, with a comment.

        @param index: index of the Snapshot to restore from. Generates an exception if the index is out of range
        """
        return None

    def serialize(self) -> str:
        """

        """
        return str()

    def setActiveVersion(self, version: core.Version) -> core.Version:
        """
        self.setActiveVersion(version) -> sets the active version to the version parameter.
        @return: hiero.core.Version object
        """
        return Version()

    def setActiveVersionIndex(self, *args, **kwargs):
        """
        self.setActiveVersionIndex(version) -> sets the currently active version by index.

        @param index: index of the version to make active
        @return: hiero.core.Version object

        WARNING - DEPRECATED ( setActiveVersionIndex ): This method is deprecated and will not be present in future versions of the Python API.
        Version indices are no longer unique identifiers and should not be used as such. Please use BinItem.setActiveVersion() instead.
        """
        return Version()

    def setColor(self, arg__1: PySide2.QtGui.QColor) -> None:
        """
        self.setColor(color) -> Set the bin item display color.

        @param color: the color to set, as a PySide2.QtGui.QColor, a string (e.g. '#ff0000') or an integer containing the RGB components (e.g. 0x11aa33).
        """
        return None

    def setName(self, name: str) -> None:
        """
        self.setName(name) -> set the name of the item.
        """
        return None

    def snapshots(self) -> object:
        """
        self.snapshots() -> returns a tuple of all of the snapshots contained by this object.

        @return: tuple of hiero.core.Snapshot objects
        """
        return tuple()

    def syncName(self, name: str) -> None:
        """
        self.syncName(name) -> set the name of the item without sending additional notifications.
        """
        return None

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        return str()

    def version(self, *args, **kwargs):
        """
        self.version(index) -> gets a Version object for the version of the bin item specified by the index.

        @param index: index of the version to get
        @return: hiero.core.Version object
        """
        return Version()

    def versionDown(self, *args, **kwargs):
        """
        self.versionDown() -> decrements the current/active version and returns the newly active Version object of the bin item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionDown ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from BinItem. To find new versions, please use hiero.core.VersionScanner. To obtain the next version, please use BinItem.prevVersion().
        """
        return Version()

    def versionMaxAvailable(self, *args, **kwargs):
        """
        self.versionMaxAvailable() -> finds the highest version that is currently loaded and does not have missing or offline media and sets it as the active version on this bin item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionMaxAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from BinItem. This method has been replaced by BinItem.maxVersion().
        """
        return Version()

    def versionMinAvailable(self, *args, **kwargs):
        """
        self.versionMinAvailable() -> finds the lowest version that is currently loaded and does not have missing or offline media and sets it as the active version on this bin item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionMinAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from BinItem. This method has been replaced by BinItem.minVersion().
        """
        return Version()

    def versionNextAvailable(self, *args, **kwargs):
        """
        self.versionNextAvailable() -> finds the next (higher) version that is currently loaded and does not have missing or offline media and sets it as the active version on this bin item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionNextAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from BinItem. This method has been replaced by BinItem.nextVersion().
        """
        return Version()

    def versionPrevAvailable(self, *args, **kwargs):
        """
        self.versionPrevAvailable() -> finds the prev (lower) version that is currently loaded and does not have missing or offline media and sets it as the active version on this bin item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionPrevAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from BinItem. This method has been replaced by BinItem.prevVersion().
        """
        return Version()

    def versionUp(self, *args, **kwargs):
        """
        self.versionUp() -> increments the current/active version and returns the newly active Version object of the bin item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionUp ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from BinItem. To find new versions, please use hiero.core.VersionScanner. To obtain the next version, please use BinItem.nextVersion().
        """
        return Version()

    def __copy__(self,) -> None:
        """

        """
        return None
