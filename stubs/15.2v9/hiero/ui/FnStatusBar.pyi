# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from hiero.core import log as log
from hiero.ui.nuke_bridge import FnNsFrameServer as FnNsFrameServer
from nuke_internal import localization as localization
import hiero as hiero

gEnableResourceMonitoring: bool

class MainStatusBar:
    """Adds a status bar to the bottom of the main window"""
    def __init__(self) -> None: ...
    def hide(self) -> None:
        """Hide the status bar"""
    def rendersExistInQueue(self) -> bool:
        """Return whether renders exist in the Frame server queue"""
    def restartServer(self) -> None:
        """Called to restart the Nuke Frame Server, done asynchronously"""
    def restartServerAsync(self) -> None: ...
    def setSyncReviewStatusWidget(self, syncReviewStatusWidget: Any) -> None: ...
    def setupUI(self) -> None:
        """Initialise the UI"""
    def show(self) -> None:
        """Show the status bar"""
    def startMonitoring(self) -> None:
        """This timer fires every X milliseconds to update the status."""
    def stopMonitoring(self) -> None:
        """Stops the monitoring process"""
    def updateChannelCountLabel(self) -> None:
        """Update the channel count label on based on preferences and channelCount"""
    def updateResourcesStatusLabel(self) -> None:
        """Updates the Memory Label String"""
    def updateStatusBar(self) -> None:
        """Updates the Status bar widgets depending on whether the frameServer is reachable"""

class PSUtilProcessWrapper:
    """This is a wrapper around a psutil.Process object, for the Nuke process"""
    def __init__(self) -> None: ...
    def nukeCPUUsageAsPercentage(self) -> float:
        """Returns Nuke's current CPU usage as percentage"""
    def nukeMemoryUsageAsPercentage(self) -> float:
        """Returns Nuke's current memory usage as percentage of Total memory"""
    def nukeMemoryUsageInGB(self) -> float:
        """Returns Nuke's current memory usage in GB"""
    def numOpenFiles(self) -> int:
        """Returns the number of open files. Unused at present."""
    def totalSystemMemory(self) -> float:
        """Returns the total System memory in GigaBytes"""
