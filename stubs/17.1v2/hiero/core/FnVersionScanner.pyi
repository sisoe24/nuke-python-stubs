# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
from hiero.core import Clip as Clip
from hiero.core import MediaSource as MediaSource
from hiero.core import Version as Version
from hiero.core import log as log
from hiero.core.util.pathviews import findViewInPath as findViewInPath
import hiero as hiero

class VersionScanner:
    """VersionScanner is a helper class that, given a Version, will scan for additional Versions and provides methods for working with Versions.

    Version scanning can detect a verion index using either the directory, or the full file path. See setVersionScanningIndexDetectionMethod()
    for more details.

    See versioning_example.py in the examples for a demonstration of how you might use the VersionScanner.
    """
    DefaultVersionScanningIndexDetectionMethod: int
    kDetectVersionDirectoryOnly: int
    kDetectVersionFullPath: int
    @staticmethod
    def VersionScanLogger() -> Any:
        """Returns a logger for logging messages relevant to the VersionScanner

        @return: The VersionScanner logger
        """
    def __init__(self) -> None: ...
    def checkNewVersion(self, originalFile: Any, newFile: Any) -> bool:
        """Check that newFile correctly matches a version of originalFile, where newFile is a real filename and originalFile includes
        sequence padding tokens (e.g. "%03d").

        @param originalFile: The original file.
        @param newFile: The new file.

        @return: True if the newFiles matches the version of originalFile, False otherwise.
        """
    def createAndInsertClipVersion(self, binitem: Any, newFilename: Any) -> None:
        """Create a new Version of a clip for a path and insert it.

        @param binitem: The BinItem for which a new Version will be created.
        @param newFilename: The name of the new Version.

        @return: The created Version, or None if it fails.
        """
    def determineVersionIndex(self, binitem: Any, newFilename: Any) -> int:
        """Get the index at which to insert new version files into a BinItem.

        @param binitem: The BinItem the Version will be inserted into.
        @param newFilename: The name of the Version file being inserted.

        @return: The index at which newFileNames's associated Version should be inserted into the binitem.
        """
    def doScan(self, version: Any) -> list[Any]:
        """Given a Version, scan for additional versions.

        @param version: An existing version.

        @return: A list of any versions found.
        """
    def filterVersion(self, binitem: Any, newVersionFile: Any) -> bool:
        """Determine whether the file newVersionFile should be included as a new Version of binitem

        @param binitem: The BinItem.
        @param newVersionFile: The new Version file.

        @return: True if it should be included as a new Version, false otherwise.
        """
    def findNewVersions(self, version: Any) -> set[Any]:
        """Scan for files matching an existing Version.

        @param version: An existing Version.

        @return: A list of files corresponding to different Versions of the given Version
        """
    def findNewVersionsInPath(self, filename: Any, views: Any = ...) -> set[Any]:
        """Scan for files matching an existing path.
        Note: This will include the files used by already added versions.

        @param filename: An existing Version's filename.

        @return: A list of matched files.
        """
    def findVersionFiles(self, version: Any) -> list[Any]:
        """Find additional versions of an existing version

        @param version: An existing version.

        @return: A list of files that are different Versions of the given Version
        """
    def getActiveIndexFromPath(self, filepath: Any) -> int:
        """Get the active version from a file path. This will be affected by the index detection method. See
        setVersionScanningIndexDetectionMethod() for more details.

        @param filepath: The path of a file.

        @return: The index of a Version, given it's filepath.
        """
    def getFileHead(self, filename: Any) -> Any:
        """Extracts "filehead" from "filename", removing sequence numbers.

        @param filename: The name of the file.

        @return: The filehead of the given file.
        """
    def getFilename(self, version: Any) -> Any:
        """Get the file name of a given Version

        @param version: A Version.

        @return: The name of the Version's file.
        """
    def getGlobExpression(self, filename: Any) -> Any:
        """Find substrings representing sequence padding (_kPaddedSequenceRegex) and version (_kVersionRegex) and replace them with
        suitable token strings in 'glob' format. For example:

        "/files/clip_v13.%03d.dpx" -> "/files/clip_v***.*"

        "/files/clip_v1.%01d.dpx" -> "/files/clip_v***.*"

        "/files/v3/clip_v1.%01d.dpx" -> "/files/v3/clip_v***.*

        @param filename: The name of the file.

        @return: The given filename reformatted to the 'glob' format.
        """
    def getMatches(self, originalFile: Any) -> list[Any]:
        """Convenience function. When we get the glob results, we use regex to compare the original filename with the found files.
        Using _regexMatches, we ensure this regex matches are computed only once for each original filename.

        @param originalFile: The original file.

        @return: The regex matches.
        """
    def getNewVersionIndexForPath(self, path: Any) -> int:
        """Find the existing versions for the given path, and return a new version index which doesn't
        already exist.

        @param path: The file path of the existing verions.

        @return: An index equal to the current highest Version index incremented by one.
        """
    def getVersionIndicesForPath(self, path: Any) -> list[int]:
        """Scan the given path and return a list of all the version indices which exist there.

        @param: The file path to be scanned.

        @return: A sorted list of all the version indicies found in the given path.
        """
    def getVersionScanningIndexDetectionMethod(self) -> int:
        """Get the method for detecting additional versions of Clips or TrackItems.

        @return: The current method for detecting the version.
        """
    def insertVersions(self, binitem: Any, versionFiles: Any) -> list[Any]:
        """Create Versions for a list of files and insert them into a BinItem.

        @param binitem: The BinItem the Versions will be inserted into.
        @param versionFiles: The list of Version files.

        @return: A list of the created Versions.
        """
    def isVisitedClip(self, filename: Any) -> bool:
        """Convenience function for determining whether a given file is part of an already visited sequence.

        @param filename: The name of the file.

        @return: True if the file has already been visited, False otherwise.
        """
    def markVisitedClip(self, filename: Any) -> None:
        """Convenience function that will add a file's path to a list of files already visited.

        @param filename: The name of the file.

        @return: Nothing.
        """
    def setVersionScanningIndexDetectionMethod(self, detectionMethod: Any) -> None:
        """Set the method for detecting additional versions of Clips or TrackItems.

        It can be set to either VersionScanner.kDetectVersionDirectoryOnly or VersionScanner.kDetectVersionFullPath, and
        defaults to kDetectVersionFullPath.

        Given an example path, '/dir_v1/file_v2.dpx', we can see how each method works:

        VersionScanner.kDetectVersionDirectoryOnly will get the version index from the directory, so the version would be v1.

        VersionScanner.kDetectVersionFullPath will get the version index from the full path, so v2. Note: we always find the
        version index looking from the right.

        @param detectionMethod: The detection method.

        @return: Nothing.
        """
    def sortVersions(self, versionFiles: Any) -> list[Any]:
        """Basic bubble sort for versions (we do not expect large numbers of versions).

        @param versionFiles: a list of the Version files to be sorted

        @return: A list containing all the files in versionFiles, sorted according to versionLessThan().
        """
    def versionLessThan(self, filename1: Any, filename2: Any) -> bool:
        """Compare method for sorting. Compares version filenames according to:
        1st) Version index
        2nd) File extension
        3rd) Full file name.

        @param filename1: The name of the first file
        @param filename2: The name of the second file

        @return: True if filename1 is less that filename2, False if filename2 is less.
        """
