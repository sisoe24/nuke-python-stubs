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

    def __init__(self, initDictionary: dict):
        """
        __init__(self, initDictionary)
        Initialise TaskBase Class

        @param initDictionary: a TaskData dictionary which seeds the task with all initialization data
        """
        return None

    def timeStampString(self, localtime):
        """
        timeStampString(localtime)
        Convert a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string formated YEAR/MONTH/DAY TIME.
        """
        return None

    def setError(self, desc):
        """
        setError(self, desc) Call to set the state of this task to error, with a description of the error.
        If the task is synchronous, raise exception
        """
        return None

    def validate(self):
        """
        Check that the task is in a state that allows it to be executed. Should
        raise an exception if there is an error. The default implementation checks if
        the task can be used with a multi-view project.
        """
        return None

    def updateItem(self, originalItem, localtime):
        """
        updateItem - This is called by the processor prior to taskStart, crucially on the main thread.

        This gives the task an opportunity to modify the original item on the main thread, rather than the clone.
        """
        return None

    def timeStamp(self):
        """
        timeStamp(self)
        Returns the datetime object from time of task creation
        """
        return None

    def fileName(self):
        """
        filename(self)
        Returns the source items filename if applicable
        """
        return None

    def fileext(self):
        """
        fileext(self)
        Returns the source items file extention if applicable
        """
        return None

    def filebase(self):
        """
        filebase(self)
        Returns the source items file path less extension if applicable
        """
        return None

    def filehead(self):
        """
        filehead(self)
        Returns the source filename excluding image sequence frame padding and extension, if applicable
        """
        return None

    def filepath(self):
        """
        filepath(self)
        Returns the source file path, if applicable
        """
        return None

    def filepadding(self):
        """
        filepadding(self)
        Returns the padding used in source file if an image sequence, empty string otherwise
        """
        return None

    def shotName(self):
        """
        shotName(self)
        Returns the Tasks track item name
        """
        return None

    def clipName(self):
        """
        clipName(self)
        Returns the name of the clip in the bin
        """
        return None

    def trackName(self):
        """
        trackName(self)
        Returns the name of the parent track
        """
        return None

    def versionString(self):
        """
        versionString(self)
        Returns the version string used to resolve the {version} token
        """
        return None

    def sequenceName(self):
        """
        sequenceName(self)
        Returns the name of the sequence or parent sequence (if exporting a track item)
        """
        return None

    def shotNameIndex(self):
        """
        shotNameIndex(self)
        Returns the index string for the shot, if there are multiple shots with the same name on the sequence.
        """
        return None

    def name(self):
        """

        """
        return None

    def projectName(self):
        """
        projectName(self)
        Returns the name of the project, used for resolving the {project} token)
        """
        return None

    def projectRoot(self):
        """
        projectRoot(self)
        Returns the project root export path, used for resolving the {projectroot} token
        """
        return None

    def editId(self):
        """
        editId(self)
        Returns a str containing the id of this edit.  See hiero.core.TrackItem.eventNumber().
        """
        return None

    def _editIdPadding(self):
        """
        Get the padding for editId strings, based on the total number of track items in the sequence
        """
        return None

    def edlEditId(self):
        """
        edlEditId(self)
        Returns the id taken from the EDL used to create this edit, if there was one.
        """
        return None

    def ident(self):
        """
        ident(self)
        Returns a string used for identifying the type of export task
        """
        return None

    def addToQueue(self):
        """
        addToQueue(self)
        Called by the processor in order to add the Task to the ExportQueue
        If derrived classes impliment this function, this base function must be called.

        Populates name, description and destination fields in the export queue
        """
        return None

    def printState(self):
        """
        Print summary of the task parameters
        """
        return None

    def resolvePath(self, path):
        """
        Replace any recognized tokens in path with their current value.
        """
        return None

    def resolvedExportPath(self):
        """
        resolvedExportPath()
        returns the output path with and tokens resolved
        """
        return None

    def _outputHandles(self, ignoreRetimes):
        """
        Internal _outputHandles() method.  Should be reimplemented by sub-classes
        rather than outputHandles().
        """
        return None

    def outputHandles(self, ignoreRetimes=False):
        """
        outputHandles( ignoreRetimes = False )
        Return a tuple of the in/out handles generated by this task.
        Handles may be cropped such as to prevent negative frame indexes.
        Note that both handles are positive, i.e. if 12 frames of handles are specified, this will return (12, 12)
        Sub-classes should reimplement _outputHandles() rather than this method.

        @return: (in_handle, out_handle) tuple
        """
        return Iterable()

    def availableOutputHandles(self):
        """
        Get the available output handles, based on self._cutHandles.
        If outputting to sequence time, the start handle is clamped to prevent going into negative frames.
        """
        return None

    def inputRange(self, ignoreHandles=False, ignoreRetimes=False, clampToSource=True):
        """
        inputRange()
        Returns the input frame range (as a tuple) for this task if applicable

        @param: ignoreHandles - If True calculate Input Range excluding export handles
        @param: ignoreRetimes - If True calculate Input Range without taking retimes into account
        @param: clampToSource - If True the input range will be clamped to the available media range
        """
        return None

    def outputSequenceTime(self):
        """
        Test if the output frame range should be in sequence time rather than source. This
        only applies when a TrackItem is being exported.

        NOTE: This option has been disabled for the time being.  The code is left in place in case we want to re-enable it,
        but it is not available to users.
        """
        return None

    def outputRange(self, ignoreHandles=False, ignoreRetimes=False, clampToSource=True):
        """
        outputRange()
        Returns the output file range (as tuple) for this task, if applicable.
        This default implementation works if the task was initialised with a Clip or TrackItem
        """
        return None

    def preSequence(self):
        """
        preSequence()
        This function serves as hook for custom scripts to add functionality before a task starts exporting anything with the sequence
        """
        return None

    def postSequence(self):
        """
        preSequence()
        This function serves as hook for custom scripts to add functionality on completion of exporting the contents of the sequence
        """
        return None

    def startTask(self):
        """
        startTask()
        Called when task reaches head of the export queue and begins execution
        """
        return None

    def views(self):
        """
        Get the view names used by the task. Tasks which support exporting from
        multi-view projects should reimplement this to return a non-empty list.
        """
        return None

    def _makePath(self):
        """
        _makePath()
        Resolve export path and make directories as neccessary.
        """
        return None

    def taskStep(self):
        """
        taskStep()
        Called every frame until task completes.
        Return True value to indicate task requires more steps.
        Return False value to indicate synchronous processing of the task is complete.
        The task may continue to run in the background.
        """
        return None

    def progress(self):
        """
        progress()
        Returns a float value 0..1 to indicate progress of task.
        The task is considered complete once the progress is reported as 1.
        """
        return None

    def finishTask(self):
        """
        finishTask()
        Called once Task has signaled completion.  Sub-classes should call this base implementation.
        """
        return None

    def _sequenceHasAudio(self, sequence):
        """

        """
        return None

    def hasValidItem(self):
        """
        Get if the task is able to run on the item it was initialised with.
        """
        return None

    def supportedType(self, item):
        """
        Interface for defining what type of items a Task Supports.
        Return True to indicate item is of supported type
        """
        return None

    def isExportingItem(self, item):
        """
        Check if this task is already including an item in its export.
        Used for preventing duplicates when collating shots into a single script.
        """
        return None

    def deleteTemporaryFile(self, filePath):
        """
        Delete a file which is an artifact of the export, but should be removed after it's finished.
        Returns whether the file was successfully deleted.
        """
        return None
