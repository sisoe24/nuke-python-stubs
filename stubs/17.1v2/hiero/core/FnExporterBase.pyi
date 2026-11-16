# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import collections as _collections
import hiero.core as _hiero_core
import hiero.core.FnResolveTable as _hiero_core_FnResolveTable
from hiero.core import ApplicationSettings as ApplicationSettings
from hiero.core import AudioTrack as AudioTrack
from hiero.core import Clip as Clip
from hiero.core import ITask as ITask
from hiero.core import ITaskPreset as ITaskPreset
from hiero.core import ItemWrapper as ItemWrapper
from hiero.core import Keys as Keys
from hiero.core import MediaSource as MediaSource
from hiero.core import Sequence as Sequence
from hiero.core import TrackItem as TrackItem
from hiero.core import Transition as Transition
from hiero.core import VideoTrack as VideoTrack
from hiero.core import defaultFrameRates as defaultFrameRates
from hiero.core import isVideoFileExtension as isVideoFileExtension
from hiero.core import log as log
from hiero.core import remapPath as remapPath
from hiero.core import util as util
from hiero.core.FnCompSourceInfo import CompSourceInfo as CompSourceInfo
from hiero.core.FnFloatRange import CustomList as CustomList
from hiero.core.FnFloatRange import Default as Default
from hiero.core.FnFloatRange import FloatRange as FloatRange
from hiero.core.FnFloatRange import IntRange as IntRange
from hiero.core.FnFloatRange import QuicktimeCodec as QuicktimeCodec
from hiero.core.FnFloatRange import QuicktimeSettings as QuicktimeSettings
from hiero.core.FnResolveTable import ResolveTable as ResolveTable

class TaskBase(_hiero_core.ITask):
    """TaskBase is the base class from which all Tasks must derrive."""
    def __init__(self, initDictionary: Any) -> None:
        """__init__(self, initDictionary)
        Initialise TaskBase Class

        @param initDictionary: a TaskData dictionary which seeds the task with all initialization data
        """
    def addToQueue(self) -> None:
        """addToQueue(self)
        Called by the processor in order to add the Task to the ExportQueue
        If derrived classes impliment this function, this base function must be called.

        Populates name, description and destination fields in the export queue
        """
    def availableOutputHandles(self) -> tuple[Any, Any]:
        """Get the available output handles, based on self._cutHandles. """
    def clipName(self) -> Any:
        """clipName(self)
        Returns the name of the clip in the bin
        """
    def deleteTemporaryFile(self, filePath: Any) -> bool:
        """Delete a file which is an artifact of the export, but should be removed after it's finished.
        Returns whether the file was successfully deleted.
        """
    def editId(self) -> str:
        """editId(self)
        Returns a str containing the id of this edit.  See hiero.core.TrackItem.eventNumber(). 
        """
    def edlEditId(self) -> str:
        """edlEditId(self)
        Returns the id taken from the EDL used to create this edit, if there was one. 
        """
    def fileName(self) -> None:
        """filename(self)
        Returns the source items filename if applicable
        """
    def filebase(self) -> None:
        """filebase(self)
        Returns the source items file path less extension if applicable
        """
    def fileext(self) -> str:
        """fileext(self)
        Returns the source items file extention if applicable
        """
    def filehead(self) -> None:
        """filehead(self)
        Returns the source filename excluding image sequence frame padding and extension, if applicable
        """
    def filepadding(self) -> str:
        """filepadding(self)
        Returns the padding used in source file if an image sequence, empty string otherwise
        """
    def filepath(self) -> str:
        """filepath(self)
        Returns the source file path, if applicable
        """
    def finishTask(self) -> None:
        """finishTask()
        Called once Task has signaled completion.  Sub-classes should call this base implementation. 
        """
    def hasValidItem(self) -> bool:
        """Get if the task is able to run on the item it was initialised with."""
    def ident(self) -> Any:
        """ident(self)
        Returns a string used for identifying the type of export task
        """
    def inputRange(self, ignoreHandles: bool = ..., ignoreRetimes: bool = ..., clampToSource: bool = ...) -> tuple[Any, Any]:
        """inputRange()
        Returns the input frame range (as a tuple) for this task if applicable

        @param: ignoreHandles - If True calculate Input Range excluding export handles
        @param: ignoreRetimes - If True calculate Input Range without taking retimes into account
        @param: clampToSource - If True the input range will be clamped to the available media range
        """
    def isExportingItem(self, item: Any) -> bool:
        """Check if this task is already including an item in its export.
        Used for preventing duplicates when collating shots into a single script. 
        """
    def name(self) -> str: ...
    def outputHandles(self, ignoreRetimes: bool = ...) -> tuple[int, int]:
        """outputHandles( ignoreRetimes = False )
        Return a tuple of the in/out handles generated by this task.
        Handles may be cropped such as to prevent negative frame indexes.
        Note that both handles are positive, i.e. if 12 frames of handles are specified, this will return (12, 12)
        Sub-classes should reimplement _outputHandles() rather than this method.

        @return: (in_handle, out_handle) tuple
        """
    def outputRange(self, ignoreHandles: bool = ..., ignoreRetimes: bool = ..., clampToSource: bool = ...) -> tuple[Any, Any]:
        """outputRange()
        Returns the output file range (as tuple) for this task, if applicable.
        This default implementation works if the task was initialised with a Clip or TrackItem
        """
    def postSequence(self) -> Any:
        """preSequence()
        This function serves as hook for custom scripts to add functionality on completion of exporting the contents of the sequence
        """
    def preSequence(self) -> Any:
        """preSequence()
        This function serves as hook for custom scripts to add functionality before a task starts exporting anything with the sequence
        """
    def printState(self) -> None:
        """Print summary of the task parameters"""
    def progress(self) -> float:
        """progress()
        Returns a float value 0..1 to indicate progress of task.
        The task is considered complete once the progress is reported as 1.
        """
    def projectName(self) -> str:
        """projectName(self)
        Returns the name of the project, used for resolving the {project} token)
        """
    def projectRoot(self) -> str:
        """projectRoot(self)
        Returns the project root export path, used for resolving the {projectroot} token
        """
    def resolvePath(self, path: Any) -> str:
        """Replace any recognized tokens in path with their current value."""
    def resolvedExportPath(self) -> str:
        """resolvedExportPath()
        returns the output path with and tokens resolved
        """
    def sequenceName(self) -> str:
        """sequenceName(self)
        Returns the name of the sequence or parent sequence (if exporting a track item)
        """
    def setError(self, desc: Any) -> None:
        """setError(self, desc) Call to set the state of this task to error, with a description of the error.
        If the task is synchronous, raise exception
        """
    def shotName(self) -> Any:
        """shotName(self)
        Returns the Tasks track item name
        """
    def shotNameIndex(self) -> Any:
        """shotNameIndex(self)
        Returns the index string for the shot, if there are multiple shots with the same name on the sequence. 
        """
    def startTask(self) -> None:
        """startTask()
        Called when task reaches head of the export queue and begins execution
        """
    def supportedType(self, item: Any) -> bool:
        """Interface for defining what type of items a Task Supports.
        Return True to indicate item is of supported type
        """
    def taskStep(self) -> bool:
        """taskStep()
        Called every frame until task completes.
        Return True value to indicate task requires more steps.
        Return False value to indicate synchronous processing of the task is complete.
        The task may continue to run in the background.
        """
    def timeStamp(self) -> Any:
        """timeStamp(self)
        Returns the datetime object from time of task creation
        """
    def timeStampString(self, localtime: Any) -> str:
        """timeStampString(localtime)
        Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string formated YEAR/MONTH/DAY TIME.
        """
    def trackName(self) -> Any:
        """trackName(self)
        Returns the name of the parent track
        """
    def updateItem(self, originalItem: Any, localtime: Any) -> Any:
        """updateItem - This is called by the processor prior to taskStart, crucially on the main thread.

        This gives the task an opportunity to modify the original item on the main thread, rather than the clone.
        """
    def validate(self) -> None:
        """Check that the task is in a state that allows it to be executed. Should
        raise an exception if there is an error. The default implementation checks if
        the task can be used with a multi-view project.
        """
    def versionString(self) -> str:
        """versionString(self)
        Returns the version string used to resolve the {version} token
        """
    def views(self) -> list[Any]:
        """Get the view names used by the task. Tasks which support exporting from
        multi-view projects should reimplement this to return a non-empty list.
        """

class FolderTask(TaskBase):
    """Task which just creates an empty folder. """
    def __init__(self, initDict: Any) -> None: ...

class TaskPresetBase(_hiero_core.ITaskPreset):
    """TaskPreset is the base class from which all Task Presets must derrive
    The purpose of a Task Preset is to store and data which must be serialized to file
    and shared between the Task and TaskUI user interface component
    """
    def __eq__(self, other: Any) -> bool:
        """Implement equal operator. This will compare the TaskPreset name
        and it's properties. This method will ignore difference between
        lists an tuples, since the same TaskPreset can be copied and
        the only change existing is a list instead of a tuple.
        """
    def __exportTemplate__eq__(self, selfExportTemplate: Any, otherExportTemplate: Any) -> bool:
        """__eq__ method for the export template property. The export template is
        a list (or tuple) of pairs with format [ path , export template ], and
        these pairs can be a list or a tuple as well. This method compares two
        exportTemplates ignoring the difference between list and tuples, so
        (path1,export1) , (path2,export2)) == [[path1,export1] , [path2,export2]]
        And the order of the pairs is ignored as well. A unique key is defined to
        order the list with the 'path', 'export template type' and 'file type'. So
        ((path1,export1),(path2,export2)) == ((path2,export2),(path1,export1))
        """
    def __init__(self, parentType: Any, presetName: Any) -> None:
        """Initialise Exporter Preset Base Class

        @param parentType: Task type to which this preset object corresponds
        @param presetName: Name of preset
        """
    def __ne__(self, other: Any) -> bool:
        """Implements not equal operator using self.__eq__ """
    def __repr__(self) -> str: ...
    def addCustomResolveEntries(self, resolver: _hiero_core_FnResolveTable.ResolveTable) -> Any:
        """addCustomResolveEntries(self, resolver)
        Impliment this function on custom export tasks to add resolve entries specific to that class.

        @param resolver: ResolveTable object
        """
    def addDefaultResolveEntries(self, resolver: _hiero_core_FnResolveTable.ResolveTable) -> None:
        """addDefaultResolveEntries(self, resolver)
        Create resolve entries for default resolve tokens shared by all task types.

        @param resolver: ResolveTable object
        """
    def addUserResolveEntries(self, resolver: _hiero_core_FnResolveTable.ResolveTable) -> Any:
        """addUserResolveEntries(self, resolver)
        Override this function to add user specific resolve tokens.
        When adding task specific tokens in derrived classes use TaskBase.addCustomResolveEntries().
        This is reserved for users to extend the available tokens.

        @param resolver: ResolveTable object
        """
    def createResolver(self) -> _hiero_core_FnResolveTable.ResolveTable:
        """createResolver(self)
        Instantiate ResolveTable, add default and custom resolve entries
        return ResolveTable object
        """
    def exportsAllTracks(self) -> bool:
        """Check if this preset can export all tracks, including ones which are empty or not enabled. """
    def getResolveEntryCount(self) -> int:
        """getResolveEntryCount(self) (DEPRICATED)
        Return the number of resolve entries in the resolve table
        """
    def ident(self) -> str:
        """ident(self)
        Returns a string used for identifying the type of task
        """
    def initialiseCallbacks(self, exportStructure: Any) -> Any:
        """When parent ExportStructure is opened in the ui, initialise is called
        for each preset. Register any callbacks here.
        """
    def isDeprecated(self) -> bool:
        """Determines whether the preset is deprecated. Any configuration that is deprecated
        should be tested here.
        """
    def markedForDeletion(self) -> bool:
        """Return True if this preset is marked for deletion. Delete will be performed at save"""
    def name(self) -> Any:
        """Return Preset Name"""
    def nonPersistentProperties(self) -> dict:
        """nonPersistentProperties()
        Return the dictionary which contains properties not persisted within the preset.
        Properties which are only relevant during a single session.

        @return: dict
        """
    def parentType(self) -> Any:
        """parentType(self)
        Returns a the parent Task type for this TaskPreset.

        @return: TaskPreet class type
        """
    def project(self) -> None:
        """Return the Project with which this preset is associated. If this is a local preset returns None"""
    def properties(self) -> dict:
        """properties()
        Return the dictionary which is used to persist data within this preset.

        @return: dict
        """
    def readOnly(self) -> bool:
        """Return the read only flag for this preset"""
    def resolveEntryCount(self) -> int:
        """resolveEntryCount(self)
        Return the number of resolve entries in the resolve table
        """
    def resolveEntryDescription(self, index: Any) -> Any:
        """resolveEntryDescription(self, index)
        return ResolveEntry description by index
        """
    def resolveEntryName(self, index: Any) -> Any:
        """resolveEntryName(self, index)
        return ResolveEntry name/token by index
        """
    def savePath(self) -> str:
        """savePath(self)
        Return the path from which this preset was loaded. Will return None if this preset was not loaded from file
        """
    def setCompsToRender(self, comps: Any) -> None:
        """Set the list of comps to render. """
    def setCompsToSkip(self, comps: Any) -> None:
        """Set the list of comps to skip. """
    def setMarkedForDeletion(self, markedForDeletion: bool = ...) -> None:
        """Set this preset as marked for deletion. Delete will be performed at save"""
    def setName(self, name: Any) -> None:
        """Set Preset Name"""
    def setProject(self, project: Any) -> None:
        """Set the Project() object which this preset is associated"""
    def setReadOnly(self, readOnly: Any) -> None:
        """Set Read Only flag on preset, not enforced internally"""
    def setSavePath(self, path: Any) -> None:
        """setSavePath(self, path)
        Set the save path of the preset in order to ensure it is saved to the path it was loaded from
        """
    def setSkipOffline(self, skip: Any) -> None:
        """skipOffline(bool)
        Set flag to skip offline TrackItems during export.

        @param bool:
        """
    def skipOffline(self) -> bool:
        """skipOffline()
        Returns True if flag has been set to skip any offline TrackItems

        @return: bool
        """
    def summary(self) -> str:
        """Called by Hiero to get a summary of the preset settings as a string."""

class FolderTaskPreset(TaskPresetBase):
    """Preset which can be used for creating an empty folder. """
    def __init__(self, name: Any, properties: Any) -> None: ...

class RenderTaskPreset(TaskPresetBase):
    """RenderTaskPreset is a specialization of the TaskPreset which contains parameters
    associated with generating Nuke render output. 
    """
    @staticmethod
    def AllViews() -> list[str]:
        """Get the special cased value for all on the views knob """
    def __init__(self, taskType: Any, name: Any, properties: Any) -> None:
        """Initialise presets to default values"""
    def addCustomResolveEntries(self, resolver: _hiero_core_FnResolveTable.ResolveTable) -> None:
        """addCustomResolveEntries(self, resolver)
        RenderTaskPreset adds specialized tokens specific to this type of export, such as {ext} which returns the output format extension.

        @param resolver: ResolveTable object
        """
    def codecName(self) -> Any: ...
    def codecProperties(self) -> Any: ...
    def codecSettings(self) -> Any: ...
    def extension(self) -> Any: ...
    def summary(self) -> str: ...

class RenderTaskPresetBase(RenderTaskPreset):
    """RenderTaskPresetBase (Deprecated)
    - Use RenderTaskPreset
    """

class TaskCallbacks:
    """This class manages callback functions that can be called
    when a Task goes into a particular state.
    """
    onTaskFinish: str
    onTaskStart: str
    @classmethod
    def addCallback(cls, callbackType: Any, callbackFn: Any) -> None:
        """Add the given callback function and callbackType.
        The callback will be executed when TaskCallbacks.call
        is called with the same callbackType.
        """
    @classmethod
    def call(cls, callbackType: Any, task: Any) -> None:
        """Call all the callback functions for the given callbackType passing in
        task as the only argument.
        """

class TaskData(dict):
    """TaskData is used as a seed for creating classes, wrapping up all of
    the parameters and making it simpler to add new ones
    """
    kCutHandles: str
    kExportRoot: str
    kExportTemplate: str
    kItem: str
    kMediaToSkip: str
    kPreset: str
    kPresetId: str
    kProject: str
    kResolver: str
    kRetime: str
    kShotNameIndex: str
    kShotPath: str
    kSkipOffline: str
    kStartFrame: str
    kStartFrameSource: str
    kSubmission: str
    kVersion: str
    def __init__(self, preset: Any, item: Any, exportRoot: Any, shotPath: Any, version: Any, exportTemplate: Any, project: Any, cutHandles: Any = ..., resolver: Any = ..., retime: bool = ..., startFrame: Any = ..., startFrameSource: Any = ..., submission: Any = ..., skipOffline: bool = ..., presetId: Any = ..., shotNameIndex: str = ..., mediaToSkip: Any = ...) -> None: ...

class TaskGroup(_hiero_core.ITask):
    """TaskGroup is a Task which maintains a list of child Tasks. """
    def __init__(self) -> None: ...
    def addChild(self, child: Any) -> None:
        """Add a child to the list. """
    def addToQueue(self) -> None: ...
    def children(self) -> list[Any]:
        """Get the TaskGroup's children. """
    def getLeafTasks(self) -> list[Any]:
        """Get a list of all leaf tasks recursively, i.e. those with no child tasks. """
    def progress(self) -> float:
        """Get the group progress.  Returns a value based on the progress of child tasks. """

class TaskPreset(TaskPresetBase):
    """Deprecated - Use TaskPresetBase"""
    def __init__(self, parentType: Any, presetName: Any) -> None: ...

def GetFramerates() -> tuple[float, float, float, float, float, float, float, float, float, float, float, float, float]: ...

def classBasename(objecttype: Any) -> str: ...

def getMovProperties() -> _collections.OrderedDict[str, None]:
    """A hardcoded dictionary of all the knobs we are interested in displaying to the
    user for mov exports. This dictionary contains the union of knob names for all mov
    codecs. It is assumed that any knob not relevant to a particular codec will
    be hidden and no value should be set for it. When creating the write node for
    the export script any knob names with unset values will be ignored.
    NB the knob names are ordered to match the order within the mov64Writer so that
    they get written to script in the same order.
    """

def getMxfProperties() -> _collections.OrderedDict[str, None]:
    """Returns a dictionary of all the knob names for the knobs that should be
    displayed to the user in the export widget. All the values are set to None
    by default. NB the knob names are ordered to match the order within the mxfWriter
    node so that they get written to script in the same order.
    """

def mediaSourceExportFileHead(source: Any) -> Any:
    """Get the filename head from a media source, fixing for use as a keyword. """

def mediaSourceExportReadPath(source: Any, useFirstFrame: Any) -> Any:
    """Get the path to include in exports from a media source.  If the source is an nk script
    return the comp write path.  If useFirstFrame is True, for file sequences will return e.g.
    clip.0001.dpx rather than clip.%04d.dpx 
    """

def tagsFromSelection(selection: Any, includeChildren: bool = ..., includeParents: bool = ...) -> list[Any]:
    """Returns a list of tuples for tag/parent type pairs"""
