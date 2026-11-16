# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from hiero.core.FnVersionScanner import VersionScanner as VersionScanner
import hiero as hiero

action: ScanForVersionsAction

class ScanForVersionsAction:
    staticMetaObject: Any
    def __init__(self) -> None: ...
    def alreadyHaveVersion(self, findversion: Any, versions: Any) -> bool: ...
    def doit(self) -> None: ...
    def eventHandler(self, event: Any) -> None: ...
    def findActiveVersions(self, container: Any, versions: Any) -> None: ...
    def selectedVersions(self) -> list[Any]: ...

class ScanForVersionsTask:
    def __init__(self) -> None: ...
    def displayResults(self, numNewVersions: Any) -> None:
        """Display results """
    def processEventsAndCheckCancelled(self) -> None:
        """Call QCoreApplication.processEvents() and check if the user has cancelled
        the progress task.  If cancelled, StopIteration will be raised.
        """
    def rescanClipRanges(self, activeVersion: Any) -> None:
        """From an active version, iterates through all the siblings inside the BinItem """
    def scanForVersions(self, versions: Any, postScanFunc: Any, shouldDisplayResults: Any) -> bool:
        """Scan a list of versions for new versions.  If postScanFunc is provided,
        this will be called after the scan.
        Returns True if scanning was completed, or False if the user cancelled or
        an error occurred.
        """
    def scanForVersionsInternal(self, versions: Any, postScanFunc: Any, shouldDisplayResults: Any) -> None: ...

def ScanAndMaxVersion(version: Any) -> None:
    """Scan then move to max version"""

def ScanAndMaxVersionTrackItems(trackItems: Any) -> bool:
    """Scan then move to next version on the track items"""

def ScanAndMinVersion(version: Any) -> None:
    """Scan then move to min version"""

def ScanAndMinVersionTrackItems(trackItems: Any) -> bool:
    """Scan then move to next version on the track items"""

def ScanAndNextVersion(version: Any) -> None:
    """Scan then move to next version"""

def ScanAndNextVersionTrackItems(trackItems: Any) -> bool:
    """Scan then move to next version on the track items"""

def ScanAndPrevVersion(version: Any) -> None:
    """Scan then move to prev version"""

def ScanAndPrevVersionTrackItems(trackItems: Any) -> bool:
    """Scan then move to next version on the track items"""

def ScanVersionsAndCallbackTrackItems(trackItems: Any, callback: Any) -> bool:
    """Helper function for track items version changes.  Does the scan and
    calls callback on each item.
    """
