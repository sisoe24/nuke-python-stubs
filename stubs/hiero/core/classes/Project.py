import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class Project(Object):
    """
    Object for manipulating projects. Can be created using hiero.core.newProject() or by the following code:
    hiero.core.openProject(projectPath)
    project = hiero.core.projects()[-1]
    """

    def __repr__(self) -> object:
        """
        Return repr(self).
        """
        return object()

    def __hash__(self, ):
        """
        Return hash(self).
        """
        return None

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

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def addView(self, name: str, color: str = Default(self, Hiero.Python.String)) -> bool:
        """
        addView(name, color) -> Appends a view to this project's list of views. Returns False if name is empty or a view already exists with the same name.

        @param name: string
        @param color: optional; string in the format #RGB, #RRGGBB, #RRRGGGBBB, #RRRRGGGGBBBB or a name from the list of colors defined in the list of SVG color keyword names
        @return: True or False
        """
        return bool()

    def autosave(self) -> None:
        """
        self.autosave() -> if the project has been modified create an autosave file
        """
        return None

    def beginUndo(self, arg__1: str) -> core.UndoGroup:
        """
        self.beginUndo(name) -> starts a new undo action, which will group all other undo actions until self.endUndo() is called. Be aware that this method only works on the main thread, and will throw an exception otherwise.
        Note that for operations inside the undo to work Project.endUndo() must be called.  It is recommended that you use this in a with block to ensure that this happens.  For example:
          with project.beginUndo('My Undo'):
            // Undoable edits

        @return: UndoGroup object
        """
        return core.UndoGroup()

    def buildTrackName(self) -> str:
        """
        buildTrackName() -> get default track name used when building vfx trackthis can be configured in the project settings dialog
        """
        return str()

    def cancelUndo(self) -> None:
        """
        self.cancelUndo() -> cancels an undo action started previously by a call to self.beginUndo().
        """
        return None

    def clearUnusedLocalFiles(self) -> None:
        """
        clearUnusedLocalFiles() -> clear all localised files that are not in any currently open project. This requires localisation to be enabled
        """
        return None

    def clipsBin(self) -> core.Bin:
        """
        self.clipsBin() -> returns the bin object containing the top level clips, sequences and bins for this project.

        @return: hiero.core.Bin object
        """
        return core.Bin()

    def close(self) -> None:
        """
        self.close() -> closes the project. Be aware that this method will not save the project, even if changes have been made since the last save of the project.
        """
        return None

    def customExportDirectory(self) -> str:
        """
        self.customExportDirectory() -> Get the custom directory used for exports if useCustomExportDirectory() is set to True.

        @return: string
        """
        return str()

    def deletable(self) -> bool:
        """
        self.deletable() -> returns True if the project can be deleted.

        @return: True or False
        """
        return bool()

    def deleteView(self, name: str) -> bool:
        """
        deleteView(name) -> Removes the view with the matching name from this project's list of views. Returns False if no matching view is found or if the view to be deleted is the only view in the project.
        @param name: string
        @return: True or False
        """
        return bool()

    def editable(self) -> bool:
        """
        self.editable() -> returns True if the project can be edited.

        @return: True or False
        """
        return bool()

    def endUndo(self) -> None:
        """
        self.endUndo() -> ends an undo action started previously by a call to self.beginUndo(). This will put a new item into the Edit > Undo/Redo menu items.
        """
        return None

    def exportRootDirectory(self) -> str:
        """
        self.exportRootDirectory() -> The root directory to use for exports. This will return either self.projectDirectory(True) or self.customExportDirectory() depending on the self.useCustomExportDirectory() setting.

        @return: string
        """
        return str()

    def framerate(self) -> core.TimeBase:
        """
        framerate() -> project's default framerate for new sequences

        @return: TimeBase
        """
        return core.TimeBase()

    def guid(self) -> object:
        """

        """
        return object()

    def heroView(self) -> str:
        """
        heroView() -> Get the name of the hero view set on the project
        @return: str
        """
        return str()

    def isLocalisationEnabled(self) -> bool:
        """
        isLocalisationEnabled() -> return whether localisation is enabled

        @return: whether localisation is enabled
        """
        return bool()

    def isNull(self) -> bool:
        """
        self.isNull() -> returns False if this is a valid Project object, True otherwise.

        @return: True or False
        """
        return bool()

    def isRestricted(self) -> bool:
        """
        self.isRestricted() -> returns whether or not access to the project is restricted.

        @return: True or False
        """
        return bool()

    def lutSetting16Bit(self) -> str:
        """
        self.lutSetting16Bit() -> returns the project's 16 bit lut setting name.

        @return: string
        """
        return str()

    def lutSetting8Bit(self) -> str:
        """
        self.lutSetting8Bit() -> returns the project's 8 bit lut setting name.

        @return: string
        """
        return str()

    def lutSettingFloat(self) -> str:
        """
        self.lutSettingFloat() -> returns the project's float lut setting name.

        @return: string
        """
        return str()

    def lutSettingLog(self) -> str:
        """
        self.lutSettingLog() -> returns the project's log lut setting name.

        @return: string
        """
        return str()

    def lutSettingMonitorOut(self) -> str:
        """
        self.lutSettingMonitorOut() -> returns the project's Monitor Out lut setting name.

        @return: string
        """
        return str()

    def lutSettingThumbnail(self) -> str:
        """
        self.lutSettingThumbnail() -> returns the project's Thumbnail lut setting name.

        @return: string
        """
        return str()

    def lutSettingViewer(self) -> str:
        """
        self.lutSettingsViewer() -> returns the project's viewer lut setting name.

        @return: string
        """
        return str()

    def lutSettingWorkingSpace(self) -> str:
        """
        self.lutSettingWorkingSpace() -> returns the project's Working Space lut setting name.

        @return: string
        """
        return str()

    def lutUseOCIOForExport(self) -> bool:
        """
        self.lutUseOCIOForExport() -> returns the project setting for using OCIO in nuke script export.

        @return: bool
        """
        return bool()

    def modifiedSinceLastSave(self) -> bool:
        """
        self.modifiedSinceLastSave() -> Check if the project has been modified since it was last saved
        """
        return bool()

    def name(self) -> str:
        """
        self.name() -> returns the name of the project.

        @return: string
        """
        return str()

    def ocioConfigName(self) -> str:
        """
        self.ocioConfigName() -> returns the ocio config name loaded by NukeStudio. When using a custom ocio config an empty string is returned.

        @return: string
        """
        return str()

    def ocioConfigPath(self) -> str:
        """
        self.ocioConfigPath() -> returns the project settings for the ocio config path.

        @return: string
        """
        return str()

    def outputFormat(self) -> core.Format:
        """
        outputFormat() -> gets project's default outputFormat for new sequences.

        @return: Format
        """
        return core.Format()

    def path(self) -> str:
        """
        self.path() -> returns the path to the project.

        @return: string
        """
        return str()

    def posterFrameSettings(self) -> typing.Tuple*args:
        """
        posterFrameSettings() -> Get the poster frame settings used for clips added to the project.
        @return: tuple of poster frame setting and custom frame number
        """
        return int()

    def projectDirectory(self, expanded: bool) -> str:
        """
        self.projectDirectory() -> Get the project directory used for resolving relative paths and the exportRootDirectory() (if useCustomExportDirectory() is False).

        @param expanded: whether expressions in the path are expanded
        @return: string
        """
        return str()

    def redo(self) -> None:
        """
        self.redo() -> triggers a redo of the next item in the redo stack. Only works on the main thread. If called from any other thread, throws an exception.
        """
        return None

    def redoItemText(self) -> str:
        """
        self.redoItemText() -> returns the text of the next item on the redo stack. Only works on the main thread. Can be useful for testing that undo/redo works.

        @return: string
        """
        return str()

    def save(self) -> None:
        """
        self.save() -> saves a previously saved project to disk.
        """
        return None

    def saveAs(self, filename: str, saveFlags: int = 'kProjectSaveNoFlags') -> None:
        """
        self.saveAs(filename) -> saves the project to the path specified by the filename parameter. Throws an exception if the project couldn't be saved for any reason.

        @param filename: path to save the project to
        """
        return None

    def setCustomExportDirectory(self, path: str) -> None:
        """
        self.setCustomExportDirectory() -> Set the custom directory used for exports if useCustomExportDirectory() is set to True.

        @param path: path
        """
        return None

    def setDeletable(self, deletable: bool) -> None:
        """
        self.setDeletable(deletable) -> sets whether or not a project can be deleted.

        @param deletable: True or False
        """
        return None

    def setEditable(self, editable: bool) -> None:
        """
        self.setEditable(editable) -> sets whether or not a project can be edited.

        @param editable: True or False
        """
        return None

    def setFramerate(self, framerate: core.TimeBase) -> None:
        """
        setFramerate(TimeBase) -> sets project's default framerate for new sequences.This will persist when the application is restarted

        @param: TimeBase
        """
        return None

    def setHasMigratedSequenceProperties(self) -> None:
        """
        setHasMigratedSequenceProperties() -> Mark the project as having had deprecated sequence properties converted into soft effects.
        """
        return None

    def setLocalisationEnabled(self, isEnabled: bool) -> None:
        """
        setLocalisationEnabled() -> set whether localisation is enabled. This will persist when the application is restarted.

        @param isEnabled: whether localisation should be enabled
        """
        return None

    def setModified(self) -> None:
        """
        self.setModified() -> Set the project as modified even if just saved or loaded
        """
        return None

    def setOcioConfigPath(self, path: str) -> None:
        """
        self.setOcioConfigPath(path) -> set the ocio config for the project
        """
        return None

    def setOutputFormat(self, *args, **kwargs):
        """
        setOutputFormat(Format) -> sets project's default output format for new sequences.
        setOutputFormat(width, height, pixelAspect, name) -> sets project's default output format for new sequences. This will persist when the application is restarted

        @param width: width for the output format
        @param height: height for the output format
        @param pixelAspect: float for pixel aspect ratio
        @param name: string for the format name
        """
        return Iterable()

    def setPath(self, path: str) -> None:
        """
        self.setPath(path) -> set the path a project saves to without saving it
        """
        return None

    def setPosterFrameSettings(self, mode: core.Project.PosterFrameSetting, customFrame: int = 0) -> None:
        """
        setPosterFrameSettings() -> Set the poster frame settings used for clips added to the project.
        @param setting: the mode for setting poster frames
        @param customFrame: the frame number if mode is set to ePosterFrameCustom
        """
        return None

    def setProjectDirectory(self, path: str) -> None:
        """
        self.setProjectDirectory(string) -> Set the project directory used for resolving relative paths and the exportRootDirectory() (if useCustomExportDirectory() is False).

        @param path: the path or expression to set
        """
        return None

    def setShotPresetName(self, path: str) -> None:
        """
        self.setShotPresetName() -> set the name of Shot Preset which is usedwhen sending to nuke or creating a comp.

        @param name:
        """
        return None

    def setShowViewColors(self, show: bool) -> None:
        """
        setShowViewColors() -> Set if colors set for views are shown in the UI.
        """
        return None

    def setStartTimecode(self, timecode: int) -> None:
        """
        setStartTimecode(Time) -> sets project's default start timecode for new sequences. This will persist when the application is restarted

        @param startTime: TimeBase start timecode for sequence
        """
        return None

    def setTimeDisplayFormat(self, displayType: core.Timecode.DisplayType) -> None:
        """
        setTimeDisplayFormat() -> sets project's default displayType for new sequences.  This will persist when the application is restarted

        @param displayType: DisplayType to use
        """
        return None

    def setTrackItemVersionsLinkedToBin(self, linked: bool) -> None:
        """
        setTrackItemVersionsLinkedToBin(linked) -> Set whether track item versions are linked by default
        """
        return None

    def setUseCustomExportDirectory(self, arg__1: bool) -> None:
        """
        self.setUseCustomExportDirectory() -> Set if the export root directory should be a custom directory, or use the project directory.

        @param custom:
        """
        return None

    def setViews(self, *args, **kwargs):
        """
        setViews(views) -> Set the project's views.
        @param views: this can be either a list of view names, or a list of tuples with (name, color)
        """
        return Any

    def setViewsForStereo(self) -> None:
        """
        setViewsForStereo() -> Replaces the project's views with two views named "left" and "right".
        """
        return None

    def shotPresetName(self) -> str:
        """
        self.shotPresetName() -> get the name of Shot Preset which is usedwhen sending to nuke or creating a comp.

        @return: string
        """
        return str()

    def showViewColors(self) -> bool:
        """
        showViewColors() -> Get if colors set for views are shown in the UI.
        """
        return bool()

    def startTimecode(self) -> int:
        """
        startTimecode() -> gets project's default start frame for new sequences.

        @return: Time
        """
        return int()

    def tagsBin(self) -> core.Bin:
        """
        self.tagsBin() -> returns the bin object containing the top level tags for this project.

        @return: hiero.core.Bin object
        """
        return core.Bin()

    def timeDisplayFormat(self) -> core.Timecode.DisplayType:
        """
        timeDisplayFormat() -> gets project's default displayType for new sequences. @return: DisplayType
        """
        return core.Timecode.DisplayType()

    def toString(self) -> str:
        """
        self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
        return str()

    def trackItemVersionsLinkedToBin(self) -> bool:
        """
        trackItemVersionsLinkedToBin() -> Get whether track item versions are linked by default
        """
        return bool()

    def undo(self) -> None:
        """
        self.undo() -> triggers an undo on the last item previously added to the undo stack. Only works on the main thread. If called from any other thread, throws an exception.
        """
        return None

    def undoItemText(self) -> str:
        """
        self.undoItemText() -> returns the text of the last item on the undo stack. Only works on the main thread. Can be useful for testing that undo/redo works.

        @return: string
        """
        return str()

    def useCustomExportDirectory(self) -> bool:
        """
        self.useCustomExportDirectory() -> Get if the export root directory should be a custom directory, or use the project directory.

        @return: bool
        """
        return bool()

    def useOCIOEnvironmentOverride(self, *args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, ...):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
        return Any

    def views(self) -> typing.List*args:
        """
        views() -> Returns a list of this project's views.
        @return: list of strings
        """
        return list()

    def viewsAndColors(self) -> typing.List*args:
        """
        viewsAndColors() -> Returns a list of this project's views and corresponding colors.
        @return: list of (str, PySide2.QtGui.QColor) tuples
        """
        return list()

    def __copy__(self,) -> None:
        """

        """
        return None

    OpenFlags: Any = None
    kProjectOpenNoFlags: Any = None
    kProjectOpenStartup: Any = None
    kProjectOpenDontAddToRecent: Any = None
    SaveFlags: Any = None
    kProjectSaveNoFlags: Any = None
    kProjectSaveKeepName: Any = None
    kProjectSaveDontAddToRecent: Any = None
    kProjectSaveAsShowFileDialog: Any = None
    kProjectSaveDontChangeProjectPath: Any = None
    PosterFrameSetting: Any = None
    eFirst: Any = None
    eMiddle: Any = None
    eLast: Any = None
    eCustom: Any = None
    kAllProjects = 0
    kUserProjects = 1
    kStartupProjects = 2

    def _Project_extractSettings(self):
        """
        self.extractSettings() -> returns a dict of the project's settings.     @return: dict

        """
        return dict()

    def sequences(self, partialName=None):
        """
        self.sequences(partialName) -> returns all sequences in a project. User can filter by by partial name.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.
        @return: an array of hiero.core.Sequence objects.

        Example: finds all sequences in a project with 30Sec in the name:

        sequences = myProject.sequences('30Sec')
        """
        return list()

    def bins(self, partialName=None):
        """
        self.bins(partialName) -> returns all bins in a project. Searches recursively, so will return bins within other bins in the list.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.Bin objects.

        Example: finds all bins in a project with MyBin in the name:

        bins = myProject.bins('MyBin')
        """
        return list()

    def clips(self, partialName=None):
        """
        self.clips(partialName) -> returns all clips in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.Clip objects.

        Example: finds all clips in a project with 30Sec in the name:

        clips = myProject.clips('30Sec')
        """
        return list()

    def tracks(self, partialName=None):
        """
        self.tracks(partialName) -> returns all tracks in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.VideoTrack and hiero.core.AudioTrack objects.

        Example: finds all tracks in a project with 30Sec in the name:

        tracks = myProject.tracks('30Sec')
        """
        return list()

    def videoTracks(self, partialName=None):
        """
        self.videoTracks(partialName) -> returns all video tracks in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.VideoTrack objects.

        Example: finds all video tracks in a project with 30Sec in the name:

        tracks = myProject.videoTracks('30Sec')
        """
        return list()

    def audioTracks(self, partialName=None):
        """
        self.audioTracks(partialName) -> returns all audio tracks in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.AudioTrack objects.

        Example: finds all audio tracks in a project with 30Sec in the name:

        tracks = myProject.audioTracks('30Sec')
        """
        return list()

    def trackItems(self, partialName=None):
        """
        self.trackItems(partialName) -> returns all track items in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.TrackItem objects.

        Example: finds all track items in a project with 30Sec in the name:

        trackItems = myProject.trackItems('30Sec')
        """
        return list()

    def videoTrackItems(self, partialName=None):
        """
        self.videoTrackItems(partialName) -> returns all video track items in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.TrackItem objects.

        Example: finds all video track items in a project with 30Sec in the name:

        trackItems = myProject.videoTrackItems('30Sec')
        """
        return list()

    def audioTrackItems(self, partialName=None):
        """
        self.audioTrackItems(partialName) -> returns all audio track items in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.TrackItem objects.

        Example: finds all audio track items in a project with 30Sec in the name:

        trackItems = myProject.audioTrackItems('30Sec')
        """
        return list()
