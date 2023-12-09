import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class TaskBase(ITask):
    """
    TaskBase is the base class from which all Tasks must derrive.
    """

    def __init__(self, initDictionary: dict) -> None:
        """
        __init__(self, initDictionary)
        Initialise TaskBase Class

        @param initDictionary: a TaskData dictionary which seeds the task with all initialization data
        """
        ...

    def timeStampString(self, localtime) -> None:
        """
        timeStampString(localtime)
        Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string formated YEAR/MONTH/DAY TIME.
        """
        ...

    def setError(self, desc) -> None:
        """
        setError(self, desc) Call to set the state of this task to error, with a description of the error.
        If the task is synchronous, raise exception
        """
        ...

    def validate(self) -> None:
        """
        Check that the task is in a state that allows it to be executed. Should
        raise an exception if there is an error. The default implementation checks if
        the task can be used with a multi-view project.
        """
        ...

    def updateItem(self, originalItem, localtime) -> None:
        """
        updateItem - This is called by the processor prior to taskStart, crucially on the main thread.

        This gives the task an opportunity to modify the original item on the main thread, rather than the clone.
        """
        ...

    def timeStamp(self) -> None:
        """
        timeStamp(self)
        Returns the datetime object from time of task creation
        """
        ...

    def fileName(self) -> None:
        """
        filename(self)
        Returns the source items filename if applicable
        """
        ...

    def fileext(self) -> None:
        """
        fileext(self)
        Returns the source items file extention if applicable
        """
        ...

    def filebase(self) -> None:
        """
        filebase(self)
        Returns the source items file path less extension if applicable
        """
        ...

    def filehead(self) -> None:
        """
        filehead(self)
        Returns the source filename excluding image sequence frame padding and extension, if applicable
        """
        ...

    def filepath(self) -> None:
        """
        filepath(self)
        Returns the source file path, if applicable
        """
        ...

    def filepadding(self) -> None:
        """
        filepadding(self)
        Returns the padding used in source file if an image sequence, empty string otherwise
        """
        ...

    def shotName(self) -> None:
        """
        shotName(self)
        Returns the Tasks track item name
        """
        ...

    def clipName(self) -> None:
        """
        clipName(self)
        Returns the name of the clip in the bin
        """
        ...

    def trackName(self) -> None:
        """
        trackName(self)
        Returns the name of the parent track
        """
        ...

    def versionString(self) -> None:
        """
        versionString(self)
        Returns the version string used to resolve the {version} token
        """
        ...

    def sequenceName(self) -> None:
        """
        sequenceName(self)
        Returns the name of the sequence or parent sequence (if exporting a track item)
        """
        ...

    def shotNameIndex(self) -> None:
        """
        shotNameIndex(self)
        Returns the index string for the shot, if there are multiple shots with the same name on the sequence.
        """
        ...

    def name(self) -> None:
        """

        """
        ...

    def projectName(self) -> None:
        """
        projectName(self)
        Returns the name of the project, used for resolving the {project} token)
        """
        ...

    def projectRoot(self) -> None:
        """
        projectRoot(self)
        Returns the project root export path, used for resolving the {projectroot} token
        """
        ...

    def editId(self) -> None:
        """
        editId(self)
        Returns a str containing the id of this edit.  See hiero.core.TrackItem.eventNumber().
        """
        ...

    def _editIdPadding(self) -> None:
        """
        Get the padding for editId strings, based on the total number of track items in the sequence
        """
        ...

    def edlEditId(self) -> None:
        """
        edlEditId(self)
        Returns the id taken from the EDL used to create this edit, if there was one.
        """
        ...

    def ident(self) -> None:
        """
        ident(self)
        Returns a string used for identifying the type of export task
        """
        ...

    def addToQueue(self) -> None:
        """
        addToQueue(self)
        Called by the processor in order to add the Task to the ExportQueue
        If derrived classes impliment this function, this base function must be called.

        Populates name, description and destination fields in the export queue
        """
        ...

    def printState(self) -> None:
        """
        Print summary of the task parameters
        """
        ...

    def resolvePath(self, path) -> None:
        """
        Replace any recognized tokens in path with their current value.
        """
        ...

    def resolvedExportPath(self) -> None:
        """
        resolvedExportPath()
        returns the output path with and tokens resolved
        """
        ...

    def _outputHandles(self, ignoreRetimes) -> None:
        """
        Internal _outputHandles() method.  Should be reimplemented by sub-classes
        rather than outputHandles().
        """
        ...

    def outputHandles(self, ignoreRetimes=False) -> tuple:
        """
        outputHandles( ignoreRetimes = False )
        Return a tuple of the in/out handles generated by this task.
        Handles may be cropped such as to prevent negative frame indexes.
        Note that both handles are positive, i.e. if 12 frames of handles are specified, this will return (12, 12)
        Sub-classes should reimplement _outputHandles() rather than this method.

        @return: (in_handle, out_handle) tuple
        """
        ...

    def availableOutputHandles(self) -> None:
        """
        Get the available output handles, based on self._cutHandles.
        If outputting to sequence time, the start handle is clamped to prevent going into negative frames.
        """
        ...

    def inputRange(self, ignoreHandles=False, ignoreRetimes=False, clampToSource=True) -> None:
        """
        inputRange()
        Returns the input frame range (as a tuple) for this task if applicable

        @param: ignoreHandles - If True calculate Input Range excluding export handles
        @param: ignoreRetimes - If True calculate Input Range without taking retimes into account
        @param: clampToSource - If True the input range will be clamped to the available media range
        """
        ...

    def outputSequenceTime(self) -> None:
        """
        Test if the output frame range should be in sequence time rather than source. This
        only applies when a TrackItem is being exported.

        NOTE: This option has been disabled for the time being.  The code is left in place in case we want to re-enable it,
        but it is not available to users.
        """
        ...

    def outputRange(self, ignoreHandles=False, ignoreRetimes=False, clampToSource=True) -> None:
        """
        outputRange()
        Returns the output file range (as tuple) for this task, if applicable.
        This default implementation works if the task was initialised with a Clip or TrackItem
        """
        ...

    def preSequence(self) -> None:
        """
        preSequence()
        This function serves as hook for custom scripts to add functionality before a task starts exporting anything with the sequence
        """
        ...

    def postSequence(self) -> None:
        """
        preSequence()
        This function serves as hook for custom scripts to add functionality on completion of exporting the contents of the sequence
        """
        ...

    def startTask(self) -> None:
        """
        startTask()
        Called when task reaches head of the export queue and begins execution
        """
        ...

    def views(self) -> None:
        """
        Get the view names used by the task. Tasks which support exporting from
        multi-view projects should reimplement this to return a non-empty list.
        """
        ...

    def _makePath(self) -> None:
        """
        _makePath()
        Resolve export path and make directories as neccessary.
        """
        ...

    def taskStep(self) -> None:
        """
        taskStep()
        Called every frame until task completes.
        Return True value to indicate task requires more steps.
        Return False value to indicate synchronous processing of the task is complete.
        The task may continue to run in the background.
        """
        ...

    def progress(self) -> None:
        """
        progress()
        Returns a float value 0..1 to indicate progress of task.
        The task is considered complete once the progress is reported as 1.
        """
        ...

    def finishTask(self) -> None:
        """
        finishTask()
        Called once Task has signaled completion.  Sub-classes should call this base implementation.
        """
        ...

    def _sequenceHasAudio(self, sequence) -> None:
        """

        """
        ...

    def hasValidItem(self) -> None:
        """
        Get if the task is able to run on the item it was initialised with.
        """
        ...

    def supportedType(self, item) -> None:
        """
        Interface for defining what type of items a Task Supports.
        Return True to indicate item is of supported type
        """
        ...

    def isExportingItem(self, item) -> None:
        """
        Check if this task is already including an item in its export.
        Used for preventing duplicates when collating shots into a single script.
        """
        ...

    def deleteTemporaryFile(self, filePath) -> None:
        """
        Delete a file which is an artifact of the export, but should be removed after it's finished.
        Returns whether the file was successfully deleted.
        """
        ...
