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

    def __init__(self, parentType: Any, presetName: str):
        """
        Initialise Exporter Preset Base Class

        @param parentType: Task type to which this preset object corresponds
        @param presetName: Name of preset
        """
        return None

    def initialiseCallbacks(self, exportStructure):
        """
        When parent ExportStructure is opened in the ui, initialise is called
        for each preset. Register any callbacks here.
        """
        return None

    def __eq__(self, other):
        """
        Implement equal operator. This will compare the TaskPreset name
        and it's properties. This method will ignore difference between
        lists an tuples, since the same TaskPreset can be copied and
        the only change existing is a list instead of a tuple.
        """
        return None

    def __ne__(self, other):
        """
        Implements not equal operator using self.__eq__
        """
        return None

    def __repr__(self):
        """
        Return repr(self).
        """
        return None

    def __exportTemplate__eq__(self, selfExportTemplate, otherExportTemplate):
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
        return None

    def name(self):
        """
        Return Preset Name
        """
        return None

    def setName(self, name):
        """
        Set Preset Name
        """
        return None

    def summary(self):
        """
        Called by Hiero to get a summary of the preset settings as a string.
        """
        return None

    def properties(self):
        """
        properties()
        Return the dictionary which is used to persist data within this preset.

        @return: dict
        """
        return dict()

    def nonPersistentProperties(self):
        """
        nonPersistentProperties()
        Return the dictionary which contains properties not persisted within the preset.
        Properties which are only relevant during a single session.

        @return: dict
        """
        return dict()

    def ident(self):
        """
        ident(self)
        Returns a string used for identifying the type of task
        """
        return None

    def parentType(self):
        """
        parentType(self)
        Returns a the parent Task type for this TaskPreset.

        @return: TaskPreet class type
        """
        return str()

    def addDefaultResolveEntries(self, resolver: ResolveTable):
        """
        addDefaultResolveEntries(self, resolver)
        Create resolve entries for default resolve tokens shared by all task types.

        @param resolver: ResolveTable object
        """
        return None

    def addCustomResolveEntries(self, resolver: ResolveTable):
        """
        addCustomResolveEntries(self, resolver)
        Impliment this function on custom export tasks to add resolve entries specific to that class.

        @param resolver: ResolveTable object
        """
        return None

    def addUserResolveEntries(self, resolver: ResolveTable):
        """
        addUserResolveEntries(self, resolver)
        Override this function to add user specific resolve tokens.
        When adding task specific tokens in derrived classes use TaskBase.addCustomResolveEntries().
        This is reserved for users to extend the available tokens.

        @param resolver: ResolveTable object
        """
        return None

    def createResolver(self):
        """
        createResolver(self)
        Instantiate ResolveTable, add default and custom resolve entries
        return ResolveTable object
        """
        return None

    def getResolveEntryCount(self):
        """
        getResolveEntryCount(self) (DEPRICATED)
        Return the number of resolve entries in the resolve table
        """
        return None

    def resolveEntryCount(self):
        """
        resolveEntryCount(self)
        Return the number of resolve entries in the resolve table
        """
        return None

    def resolveEntryName(self, index):
        """
        resolveEntryName(self, index)
        return ResolveEntry name/token by index
        """
        return None

    def resolveEntryDescription(self, index):
        """
        resolveEntryDescription(self, index)
        return ResolveEntry description by index
        """
        return None

    def setSavePath(self, path):
        """
        setSavePath(self, path)
        Set the save path of the preset in order to ensure it is saved to the path it was loaded from
        """
        return None

    def savePath(self):
        """
        savePath(self)
        Return the path from which this preset was loaded. Will return None if this preset was not loaded from file
        """
        return None

    def setProject(self, project):
        """
        Set the Project() object which this preset is associated
        """
        return None

    def project(self):
        """
        Return the Project with which this preset is associated. If this is a local preset returns None
        """
        return None

    def setReadOnly(self, readOnly):
        """
        Set Read Only flag on preset, not enforced internally
        """
        return None

    def readOnly(self):
        """
        Return the read only flag for this preset
        """
        return None

    def markedForDeletion(self):
        """
        Return True if this preset is marked for deletion. Delete will be performed at save
        """
        return None

    def setMarkedForDeletion(self, markedForDeletion=True):
        """
        Set this preset as marked for deletion. Delete will be performed at save
        """
        return None

    def skipOffline(self):
        """
        skipOffline()
        Returns True if flag has been set to skip any offline TrackItems

        @return: bool
        """
        return bool()

    def setSkipOffline(self, skip):
        """
        skipOffline(bool)
        Set flag to skip offline TrackItems during export.

        @param bool:
        """
        return None

    def setCompsToRender(self, comps):
        """
        Set the list of comps to render.
        """
        return None

    def setCompsToSkip(self, comps):
        """
        Set the list of comps to skip.
        """
        return None

    def isDeprecated(self):
        """
        Determines whether the preset is deprecated. Any configuration that is deprecated
        should be tested here.
        """
        return None

    __hash__: Any = None
