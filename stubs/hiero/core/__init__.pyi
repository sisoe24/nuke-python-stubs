'''Stubs generated automatically from Nuke's internal interpreter.'''
from typing import *
from numbers import Number

import ui
import core

from . import nuke
from .classes import *

# Constants
GUI = True
env = {'VersionDate': '', 'VersionMajor': '', 'VersionMinor': '', 'VersionRelease': '', 'VersionString': '', 'VersionPhaseNumber': '', 'ProductName': '', 'ApplicationName': '', 'HomeDirectory': '', 'SystemMemory': '', 'Features': ''}
# Built-in methods
def LUTGroup(*args, **kwargs) -> None:
    """

    """
    ...

def LUTs(*args, **kwargs) -> tuple:
    """
    hiero.core.LUTs() -> returns a tuple with the names of all of the available luts.

    @return: tuple of strings
    """
    ...

def ViewerProcessNameFromDisplayTransformName(arg__1: str) -> object:
    """

    """
    ...

def addPathRemap(arg__1: str, arg__2: str, arg__3: str) -> None:
    """
    hiero.core.addPathRemap(windowsPathPrefix, osxPathPrefix, linuxPathPrefix) -> adds to the table of file path remapping prefixes that Hiero maintains. Pairs of path prefixes added to this table will be used to convert paths between Windows, OSX and Linux. When on Windows, Hiero will replace any Linux or OSX prefixes found with the corresponding Windows prefix. On OSX, Hiero will search for the Windows and Linux path prefixes and replace them with the corresponding OSX prefix. The same applies for OSX/Windows prefixes being replaced on Linux. These can also be configured through the user interface in the General tab of the Preferences dialog.

    @param windowsPathPrefix: string
    @param osxPathPrefix: string
    @param linuxPathPrefix: string

    @return: None
    """
    ...

def addPluginPath(*args, **kwargs) -> list:
    """
    hiero.core.addPluginPath(pluginPath) -> adds a new path to the list of plugin paths searched for Python plugins (in Python/Startup and Python/StartupUI folders). The user's .nuke folder will be the first in this list.
    hiero.core.addPluginPath(pluginPath, index) -> the same as above, except that the index specifies which item in the list of paths to place the new one before.

    @param pluginPath: the new path to add
    @param index: optional; if not specified or negative, the new path will be added to the end of the list
    """
    ...

def closeAllProjects(*args, **kwargs) -> Any:
    """
    hiero.core.closeProject() -> closes all of the existing projects without saving.
    hiero.core.closeProject(bool dontSave) -> same as above, but if the parameter is set to false, unsaved projects will cause Hiero to popup a dialog for each unsaved project, asking the user if they'd like to save.

    @param dontSave: True or False
    """
    ...

def conformer() -> Conformer:
    """
    hiero.core.conformer() -> returns an interface for setting the conforming options.

    @return: a hiero.core.Conformer object
    """
    ...

def formats() -> object:
    """
    hiero.core.formats() -> returns a tuple with all of the formats currently available.

    @return: tuple of hiero.core.Format objects
    """
    ...

def getFilenameList(arg__1: str, arg__2: bool, arg__3: bool, arg__4: bool, arg__5: bool) -> object:
    """
    Deprecated. Do not use. Use hiero.core.filenameList() instead
    """
    ...

def getLibraryDirectory(arg__1: str) -> object:
    """
    hiero.core.getLibraryDirectory(subdirectory) -> deprecated; use hiero.core.libraryDirectory() instead.
    """
    ...

def getPluginPath() -> Any:
    """
    hiero.core.getPluginPath() -> deprecated; please use hiero.core.pluginPath instead.
    """
    ...

def getRoleColorspace(*args, **kwargs) -> None:
    """

    """
    ...

def isHieroPlayer() -> object:
    """

    """
    ...

def isIndie() -> object:
    """

    """
    ...

def isNC() -> object:
    """

    """
    ...

def libraryDirectory(arg__1: str) -> object:
    """
    hiero.core.libraryDirectory(subdirectory) -> returns the input appended to the location of the user's .nuke directory.

    @param subdirectory: path to append to the .nuke directory
    @return: string
    """
    ...

def newProject(*args, **kwargs) -> Project:
    """
    hiero.core.newProject(name=None) -> creates and returns a new Project object. A name can optionally be given for the project.

    @return: hiero.core.Project object
    """
    ...

def openProject(path: str, flags: int = 'Hiero.Python.Project.kProjectOpenNoFlags') -> core.Project:
    """
    hiero.core.openProject(path)

    Opens the project found at the specified path. Must be called on the main thread. Throws an exception on failure.
    @param path: Path to the project file (\*.hrox).
    @return: Opened project.
    """
    ...

def pathRemappings() -> object:
    """
    hiero.core.pathRemappings() -> returns the path remappings specified in the application preferences, or added through addPathRemap().

    @return: a list of path remappings each containing the mapping for (windows, osx, linux)
    """
    ...

def pluginPath() -> tuple:
    """
    hiero.core.pluginPath() -> Returns a tuple of the search paths used by Hiero to load Python scripts.

    @return: tuple of strings
    """
    ...

def project(arg__1: str) -> Project:
    """
    hiero.core.project(name) -> returns the Project with the specified name, if it can be found, or None.

    @return: hiero.core.Project object
    """
    ...

def projects(*args, **kwargs) -> Tuple[Project, ...]:
    """
    hiero.core.projects() -> returns a tuple of currently loaded projects which are user projects (not startup). Same effect as calling the method below passing Project.kUserProjects.
    hiero.core.projects(projectTypes) -> returns a tuple of currently loaded projects, filtered according to projectTypes. Use hiero.core.projects()[-1] to get the last loaded project.
    @param projectTypes: optional; one of Project.kAllProjects, Project.kUserProjects, Project.kStartupProjects

    @return: tuple of hiero.core.Project objects
    """
    ...

def quit(*args, **kwargs) -> int:
    """
    hiero.core.quit() -> shuts down Hiero, without saving any existing projects. Safer than calling sys.exit(), which doesn't always clean up properly and can cause Hiero to crash. This version sets the exit code of the Hiero process to 0.

    Note that this must be the last line in a script.
    hiero.core.quit(exitCode) -> same as the first version of this method, except that this one sets the exit code of the process to the exitCode variable.

    @param exitCode: optional; integer value to set the process's exit code to
    """
    ...

def redo() -> object:
    """

    """
    ...

def redoSize() -> object:
    """

    """
    ...

def remapPath(arg__1: str) -> object:
    """
    hiero.core.remapPath(path) -> uses the platform specific path remapping rules from the user's preferences and applies them to the input path.

    @param path: string path to apply the path remapping rules to
    @return: string
    """
    ...

def stopScriptAndQuit(*args, **kwargs) -> None:
    """

    """
    ...

def undo() -> object:
    """

    """
    ...

def undoSize() -> object:
    """

    """
    ...
