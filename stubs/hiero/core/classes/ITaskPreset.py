import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class ITaskPreset(Object):
    """
    ITaskPreset provides a simple interface for our C++ Application to access Python instances of TaskPreset.

    This class should not be used directly; use hiero.core.TaskPresetBase instead.
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

    def getResolveEntryCount(self) -> int:
        """
        self.getResolveEntryCount() -> called by Hiero to get the number of resolve tokens available on this TaskPreset.
        """
        return int()

    def ident(self) -> str:
        """
        self.ident() -> called by Hiero to get a unique identifier for the Task related to this TaskPreset.
        """
        return str()

    def isDeprecated(self) -> bool:
        """
        self.isDeprecated() -> returns whether or not this task preset is using a deprecated configuration.

        @return: True or False
        """
        return Union[True, False]

    def markedForDeletion(self) -> bool:
        """
        self.markedForDeletion() -> called by Hiero to check if the preset is marked for deletion.
        """
        return bool()

    def name(self) -> str:
        """
        self.name() -> called by Hiero to get the preset name.
        """
        return str()

    def project(self) -> core.Project:
        """
        self.project() -> called by Hiero to discover which Project (if any), this preset is assigned to
        """
        return core.Project()

    def readOnly(self) -> bool:
        """
        self.readOnly() -> called by Hiero to discover if this preset is marked ReadOnly.
        """
        return bool()

    def resolveEntryDescription(self, index: int) -> str:
        """
        self.resolveEntryDescription() -> called by Hiero to get a resolve token description by index.
        """
        return str()

    def resolveEntryName(self, index: int) -> str:
        """
        self.resolveEntryName() -> called by Hiero to get a resolve token ({shot}) by index.
        """
        return str()

    def setMarkedForDeletion(self, markedForDeletion: bool = True) -> None:
        """
        self.setMarkedForDeletion() -> called by Hiero to mark this preset for deletion. The delete is not performed until presets are saved.
        """
        return None

    def setProject(self, project: core.Project) -> None:
        """
        self.setProject() -> called by Hiero to assign a preset to a Project.
        """
        return None

    def setReadOnly(self, readOnly: bool) -> None:
        """
        self.setReadOnly() -> called by Hiero to mark this preset as ReadOnly.
        """
        return None

    def summary(self) -> str:
        """
        self.summary() -> called by Hiero to get the preset description.
        """
        return str()

    def supportedItems(self) -> int:
        """
        self.supportedItems() -> called by Hiero to establish what types of object this export task operates on (Clips, Sequences, TrackItems).
        """
        return int()

    def supportsAudio(self) -> bool:
        """
        self.supportsAudio() -> returns whether or not this task preset supports audio.

        @return: True or False
        """
        return Union[True, False]

    ItemTypes: Any = None
    kSequence: Any = None
    kTrackItem: Any = None
    kAudioTrackItem: Any = None
    kClip: Any = None
    kAllItems: Any = None
