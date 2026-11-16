# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import PySide6.QtWidgets as _PySide6_QtWidgets
from nukescripts.reads import get_reads as get_reads
from nukescripts.version import version_get as version_get
from nukescripts.version import version_set as version_set

kCommandField: str
last_cmd: str

class VersionConflictDialog(_PySide6_QtWidgets.QDialog):
    """Dialog which gives the user options for resolving version conflicts"""
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, versionHelper: Any, parent: Any = ...) -> None: ...
    def getNewFilePath(self) -> None: ...
    def getNewVersionNumber(self) -> int | None: ...
    def showDialog(self) -> int | None: ...

class VersionHelper:
    """Helper class for storing the new version information"""
    def __init__(self, rootname: Any) -> None: ...
    def currentVersionString(self) -> Any: ...
    def hasVersion(self) -> bool: ...
    def maxVersion(self) -> int: ...
    def maxVersionString(self) -> Any: ...
    def nextVersion(self) -> int: ...
    def nextVersionString(self) -> Any: ...
    def versionString(self, version: Any) -> Any: ...

def findMaxVersionForFileName(filename: Any) -> int:
    """Helper function for finding the max version of a paticular
    script in it's current directory.
    Note that a file in the current directory will count towards the
    current version set if the string before the v number for that file
    is the same as the string before the v numebr of the current version.
    """

def get_script_data() -> Any: ...

def script_and_write_nodes_version_up() -> None: ...

def script_command(default_cmd: Any) -> None: ...

def script_data() -> None: ...

def script_directory() -> str: ...

def script_version_up() -> None:
    """Increments the versioning in the script name and the path of the timeline
    write nodes, then saves the new version. 
    """

def set_fileknob_version(knob: Any, version: Any) -> None:
    """Sets version of the filename knob to the passed in version.
    Throws with ValueError if fileKnob has no version.
    """

def timeline_write_version_set(version: Any) -> None:
    """Sets the version number in the file path of the 'timeline' write node"""
