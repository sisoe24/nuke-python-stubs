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


class ITaskPreset(Object):
    """
    ITaskPreset provides a simple interface for our C++ Application to access Python instances of TaskPreset.

    This class should not be used directly; use hiero.core.TaskPresetBase instead.
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
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

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def getResolveEntryCount(self) -> int:
        """
        self.getResolveEntryCount() -> called by Hiero to get the number of resolve tokens available on this TaskPreset.
        """
        ...

    def ident(self) -> str:
        """
        self.ident() -> called by Hiero to get a unique identifier for the Task related to this TaskPreset.
        """
        ...

    def isDeprecated(self) -> bool:
        """
        self.isDeprecated() -> returns whether or not this task preset is using a deprecated configuration.

        @return: True or False
        """
        ...

    def markedForDeletion(self) -> bool:
        """
        self.markedForDeletion() -> called by Hiero to check if the preset is marked for deletion.
        """
        ...

    def name(self) -> str:
        """
        self.name() -> called by Hiero to get the preset name.
        """
        ...

    def project(self) -> core.Project:
        """
        self.project() -> called by Hiero to discover which Project (if any), this preset is assigned to
        """
        ...

    def readOnly(self) -> bool:
        """
        self.readOnly() -> called by Hiero to discover if this preset is marked ReadOnly.
        """
        ...

    def resolveEntryDescription(self, index: int) -> str:
        """
        self.resolveEntryDescription() -> called by Hiero to get a resolve token description by index.
        """
        ...

    def resolveEntryName(self, index: int) -> str:
        """
        self.resolveEntryName() -> called by Hiero to get a resolve token ({shot}) by index.
        """
        ...

    def setMarkedForDeletion(self, markedForDeletion: bool = True) -> None:
        """
        self.setMarkedForDeletion() -> called by Hiero to mark this preset for deletion. The delete is not performed until presets are saved.
        """
        ...

    def setProject(self, project: core.Project) -> None:
        """
        self.setProject() -> called by Hiero to assign a preset to a Project.
        """
        ...

    def setReadOnly(self, readOnly: bool) -> None:
        """
        self.setReadOnly() -> called by Hiero to mark this preset as ReadOnly.
        """
        ...

    def summary(self) -> str:
        """
        self.summary() -> called by Hiero to get the preset description.
        """
        ...

    def supportedItems(self) -> int:
        """
        self.supportedItems() -> called by Hiero to establish what types of object this export task operates on (Clips, Sequences, TrackItems).
        """
        ...

    def supportsAudio(self) -> bool:
        """
        self.supportsAudio() -> returns whether or not this task preset supports audio.

        @return: True or False
        """
        ...

    ItemTypes: Any = None
    kSequence: Any = None
    kTrackItem: Any = None
    kAudioTrackItem: Any = None
    kClip: Any = None
    kAllItems: Any = None
