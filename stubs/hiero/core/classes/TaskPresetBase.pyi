import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *

class TaskPresetBase(ITaskPreset):
    """
    TaskPreset is the base class from which all Task Presets must derrive
    The purpose of a Task Preset is to store and data which must be serialized to file
    and shared between the Task and TaskUI user interface component
    """
    def __init__(self, parentType, presetName:str) -> None:
        """
        Initialise Exporter Preset Base Class

        @param parentType: Task type to which this preset object corresponds
        @param presetName: Name of preset
        """
        ...

    def initialiseCallbacks(self, exportStructure) -> None:
        """
        When parent ExportStructure is opened in the ui, initialise is called
        for each preset. Register any callbacks here.
        """
        ...

    def __eq__(self, other) -> None:
        """
        Implement equal operator. This will compare the TaskPreset name
        and it's properties. This method will ignore difference between
        lists an tuples, since the same TaskPreset can be copied and
        the only change existing is a list instead of a tuple.
        """
        ...

    def __ne__(self, other) -> None:
        """
        Implements not equal operator using self.__eq__
        """
        ...

    def __repr__(self) -> None:
        """
        Return repr(self).
        """
        ...

    def __exportTemplate__eq__(self, selfExportTemplate, otherExportTemplate) -> None:
        """
        __eq__ method for the export template property. The export template is
        a list (or tuple) of pairs with format [ path , export template ], and
        these pairs can be a list or a tuple as well. This method compares two
        exportTemplates ignoring the difference between list and tuples, so
        (path1,export1) , (path2,export2)) == [[path1,export1] , [path2,export2]]
        And the order of the pairs is ignored as well. A unique key is defined to
        order the list with the 'path', 'export template type' and 'file type'. So
        ((path1,export1),(path2,export2)) == ((path2,export2),(path1,export1))
        """
        ...

    def name(self) -> None:
        """
        Return Preset Name
        """
        ...

    def setName(self, name) -> None:
        """
        Set Preset Name
        """
        ...

    def summary(self) -> None:
        """
        Called by Hiero to get a summary of the preset settings as a string.
        """
        ...

    def properties(self) -> dict:
        """
        properties()
        Return the dictionary which is used to persist data within this preset.

        @return: dict
        """
        ...

    def nonPersistentProperties(self) -> dict:
        """
        nonPersistentProperties()
        Return the dictionary which contains properties not persisted within the preset.
        Properties which are only relevant during a single session.

        @return: dict
        """
        ...

    def ident(self) -> None:
        """
        ident(self)
        Returns a string used for identifying the type of task
        """
        ...

    def parentType(self) -> str:
        """
        parentType(self)
        Returns a the parent Task type for this TaskPreset.

        @return: TaskPreet class type
        """
        ...

    def addDefaultResolveEntries(self, resolver:ResolveTable) -> None:
        """
        addDefaultResolveEntries(self, resolver)
        Create resolve entries for default resolve tokens shared by all task types.

        @param resolver: ResolveTable object
        """
        ...

    def addCustomResolveEntries(self, resolver:ResolveTable) -> None:
        """
        addCustomResolveEntries(self, resolver)
        Impliment this function on custom export tasks to add resolve entries specific to that class.

        @param resolver: ResolveTable object
        """
        ...

    def addUserResolveEntries(self, resolver:ResolveTable) -> None:
        """
        addUserResolveEntries(self, resolver)
        Override this function to add user specific resolve tokens.
        When adding task specific tokens in derrived classes use TaskBase.addCustomResolveEntries().
        This is reserved for users to extend the available tokens.

        @param resolver: ResolveTable object
        """
        ...

    def createResolver(self) -> None:
        """
        createResolver(self)
        Instantiate ResolveTable, add default and custom resolve entries
        return ResolveTable object
        """
        ...

    def getResolveEntryCount(self) -> None:
        """
        getResolveEntryCount(self) (DEPRICATED)
        Return the number of resolve entries in the resolve table
        """
        ...

    def resolveEntryCount(self) -> None:
        """
        resolveEntryCount(self)
        Return the number of resolve entries in the resolve table
        """
        ...

    def resolveEntryName(self, index) -> None:
        """
        resolveEntryName(self, index)
        return ResolveEntry name/token by index
        """
        ...

    def resolveEntryDescription(self, index) -> None:
        """
        resolveEntryDescription(self, index)
        return ResolveEntry description by index
        """
        ...

    def setSavePath(self, path) -> None:
        """
        setSavePath(self, path)
        Set the save path of the preset in order to ensure it is saved to the path it was loaded from
        """
        ...

    def savePath(self) -> None:
        """
        savePath(self)
        Return the path from which this preset was loaded. Will return None if this preset was not loaded from file
        """
        ...

    def setProject(self, project) -> None:
        """
        Set the Project() object which this preset is associated
        """
        ...

    def project(self) -> None:
        """
        Return the Project with which this preset is associated. If this is a local preset returns None
        """
        ...

    def setReadOnly(self, readOnly) -> None:
        """
        Set Read Only flag on preset, not enforced internally
        """
        ...

    def readOnly(self) -> None:
        """
        Return the read only flag for this preset
        """
        ...

    def markedForDeletion(self) -> None:
        """
        Return True if this preset is marked for deletion. Delete will be performed at save
        """
        ...

    def setMarkedForDeletion(self, markedForDeletion=True) -> None:
        """
        Set this preset as marked for deletion. Delete will be performed at save
        """
        ...

    def skipOffline(self) -> bool:
        """
        skipOffline()
        Returns True if flag has been set to skip any offline TrackItems

        @return: bool
        """
        ...

    def setSkipOffline(self, skip) -> None:
        """
        skipOffline(bool)
        Set flag to skip offline TrackItems during export.

        @param bool:
        """
        ...

    def setCompsToRender(self, comps) -> None:
        """
        Set the list of comps to render.
        """
        ...

    def setCompsToSkip(self, comps) -> None:
        """
        Set the list of comps to skip.
        """
        ...

    def isDeprecated(self) -> None:
        """
        Determines whether the preset is deprecated. Any configuration that is deprecated
        should be tested here.
        """
        ...

    __hash__: Any = None
