# Type stubs for nuke 15.2v9. Generated; do not edit.

"""APIs for Nuke's localization functionality.

Use help('_localization') to get detailed help on the classes exposed here.

This module provides the public interface to the localization module and will
remain stable. It uses an underlying native module called _localization to
provide this interface. While there is nothing stopping you from using the
_localization module directly, it may change in a future release and break 
backwards compatibility.
"""

from typing import Any

class FileEvent:
    """Events received in file callbacks"""
    CACHE_FULL: int
    DISK_FULL: int
    LOCALIZED: int
    OUT_OF_DATE: int
    REMOVED: int

class ReadStatus:
    """Localization status recieved by Read callbacks"""
    LOCALIZATION_DISABLED: int
    LOCALIZED: int
    LOCALIZING: int
    NOT_LOCALIZED: int
    OUT_OF_DATE: int
    PARTIALLY_LOCALIZED: int

def addFileCallback(callback: Any) -> Any:
    """addFileCallback( callback ) -> Adds a callback for file localization events.

    :param callback: is a python callable object with arguments for path and event. See nuke.localization.FileEvent for possible file events.

    Usage Example:

    .. code-block::
       :caption: Usage Example
           def myCallback( path, event ):
               if event == nuke.localization.FileEvent.LOCALIZED:
                   print("file : " + path +  " is localized")
               if event == nuke.localization.FileEvent.OUT_OF_DATE:
                   print("file : " + path + " is out of date")

           nuke.localization.addFileCallback( myCallback )
           # Do some localization and process callbacks, when finished call:
           nuke.localization.removeFileCallback( myCallback )
    """

def addReadCallback(callback: Any) -> None:
    """addReadCallback( callback ) -> None

    Adds a callback for read localization events.

    :param callback: is a python callable object with arguments for Read and status.
    .. seealso:: nuke.localization.ReadStatus

    Usage Example:

    .. code-block:: python
        :linenos:

        def myCallback( read, event ):
            if event == nuke.localization.ReadStatus.LOCALIZED:
                print(\\read : \\ + read.name() + \\ localized\\)
            elif event == nuke.localization.ReadStatus.OUT_OF_DATE:
                print(\\file : \\ + read.name() + \\ is out of date\\)

        nuke.localization.addReadCallback( myCallback )\\n
        # do some localization and process callbacks, when finished call:
        nuke.localization.removeReadCallback( myCallback )
    """

def checkForUpdates() -> None:
    """checkForUpdates() -> None

    Trigger a manual file check, which checks and updates the states of localised files.
    """

def clearUnusedFiles(pathPrefix: str = ..., olderThan: Any = ...) -> None:
    """clearUnusedFiles(pathPrefix = "", olderThan = None) -> None

    Clears unused files in the localization folder.

    :param pathPrefix: Only clear files within this path.
    :param olderThan: Only clear files older than this date. Must be a DateTime.
    :return: None
    """

def findNodes() -> None:
    """findNodes() -> None

    Returns the list of read nodes that read from the argument paths.

    :param: List of strings containing paths of localized files.
    :return: List of read nodes that read from the @param paths.
    """

def forceUpdateAll() -> None:
    """forceUpdateAll() -> None

    Update all localized files currently in use in Nuke.

    :return: None
    """

def forceUpdateOnDemand() -> None:
    """forceUpdateAll() -> None

    Update all on-demand localized files

    :return: None
    """

def forceUpdateSelectedNodes() -> None:
    """forceUpdateSelectedNodes() -> None

    Update all localized files used by nodes that are currently selected.

    :return: None\\n
    """

def isLocalizationPaused() -> bool:
    """isLocalizationPaused() -> Check if localization is paused.

    :return: whether localization was paused
    """

def localizationProgress() -> float:
    """localizationProgress() -> None

    gets the percentage of localization completed.
    """

def localizedPaths() -> None:
    """localizedPaths() -> None

    gets paths of files which are currently localized.

    :return: List of strings containing file paths of localized paths
    """

def mode() -> str:
    """mode() -> None gets the current localization system mode.

    :return string 'on', 'off' or 'manual'
    """

def pauseLocalization() -> None:
    """pauseLocalization() -> None

    Pause the localization background thread if it was running.

    :return: None
    """

def removeFileCallback(callback: Any) -> None:
    """removeFileCallback( callback ) -> None

    Removes a callback for file localization events.

    :param callback: is a python callable object with arguments path and eventID. see addFileCallback for usage example.\\n
    """

def removeReadCallback(callback: Any) -> None:
    """removeReadCallback( callback ) -> None

    Removes a callback for read localization events

    :param callback: is a python callable object with arguments path and eventID.

    .. seealso:: addReadCallback for usage example.
    """

def resumeLocalization() -> None:
    """resumeLocalization() -> None

    Resume the localization background thread if it was paused

    :return: None
    """

def setMode(mode: Any) -> None:
    """setMode( mode ) -> None

    sets the localization system mode.

    :param mode str of value: 'on', 'off' or 'manual'
    :return None
    """
