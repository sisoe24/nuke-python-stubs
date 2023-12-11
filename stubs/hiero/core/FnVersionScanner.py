import re
import glob
import os.path

import hiero.core
from hiero.core import Clip, Version, MediaSource, log
from PySide2.QtCore import QDir
from hiero.core.util import findViewInPath


class VersionScanner():
    """ VersionScanner is a helper class that, given a Version, will scan for additional Versions and provides methods for working with Versions.

    Version scanning can detect a verion index using either the directory, or the full file path. See setVersionScanningIndexDetectionMethod()
    for more details.

    See versioning_example.py in the examples for a demonstration of how you might use the VersionScanner.
    """

    # WARNING: Modifying these regexes for "equivalent" ones might break code that depends on the grouping
    #          (parentheses) in them for obtaining bits of data. Be extra-careful if you do so.
    # NOTE: kRawSequenceRegex checks for preceding chars to distinguish from versions. This means it includes
    #       exactly 2 chars in front of the actual frame number, that need to be trimmed to retrieve it.
    _kVersionRegex = '([/._]v)(\\d+)'  # e.g.: "_v1", ".v024", "/v13"
    _kPaddedSequenceRegex = '%((\\d)*)(d)'  # e.g.: "%01d", "%d"
    # e.g.: "0001.dpx", "1.exr" - not preceded by "_v", ".v", "/v", or a digit
    _kRawSequenceRegex = '(.[^v0-9]|[^/._]v)(\\d+)(\\.[^\\.]+)$'

    # See the class description for more infomation on version index detection methods
    kDetectVersionDirectoryOnly = 0
    kDetectVersionFullPath = 1

    # Default scanning method
    DefaultVersionScanningIndexDetectionMethod = kDetectVersionFullPath

    def __init__(self):
        self._versionScanningIndexDetectionMethod = VersionScanner.DefaultVersionScanningIndexDetectionMethod

        # Optimisation: Cached regex matches (used by getMatches in checkNewVersion)
        self._regexMatches = None
        # Optimisation: Set of strings containing "file heads" for visited clips (used by isVisitedClip in checkNewVersion)
        self._visitedClips = set()

        # Path remaps that were applied to the clips being scanned. This will contain
        # tuples of (remapped path, original path)
        self._pathRemaps = set()

    def setVersionScanningIndexDetectionMethod(self, detectionMethod):
        """ Set the method for detecting additional versions of Clips or TrackItems.

        It can be set to either VersionScanner.kDetectVersionDirectoryOnly or VersionScanner.kDetectVersionFullPath, and
        defaults to kDetectVersionFullPath.

        Given an example path, '/dir_v1/file_v2.dpx', we can see how each method works:

        VersionScanner.kDetectVersionDirectoryOnly will get the version index from the directory, so the version would be v1.

        VersionScanner.kDetectVersionFullPath will get the version index from the full path, so v2. Note: we always find the
        version index looking from the right.

        @param detectionMethod: The detection method.

        @return: Nothing.
        """
        assert (detectionMethod == VersionScanner.kDetectVersionDirectoryOnly or detectionMethod ==
                VersionScanner.kDetectVersionFullPath)
        self._versionScanningIndexDetectionMethod = detectionMethod

    def getVersionScanningIndexDetectionMethod(self):
        """ Get the method for detecting additional versions of Clips or TrackItems.

        @return: The current method for detecting the version.
        """
        return self._versionScanningIndexDetectionMethod

    def doScan(self, version):
        """ Given a Version, scan for additional versions.

        @param version: An existing version.

        @return: A list of any versions found.
        """
        foundVersionFiles = self.findVersionFiles(version)

        binitem = version.parent()

        # Add versions to binitem, respecting the sorting
        newVersions = self.insertVersions(binitem, foundVersionFiles)
        VersionScanner.VersionScanLogger().info(
            'ScanForVersions - Versions found for %s: %s', version, newVersions)

        return newVersions

    def findVersionFiles(self, version):
        """ Find additional versions of an existing version

        @param version: An existing version.

        @return: A list of files that are different Versions of the given Version
        """
        binitem = version.parent()

        origfilename = self.getFilename(version)
        self._origextension = os.path.splitext(origfilename)[1]

        foundVersions = self.findNewVersions(version)

        VersionScanner.VersionScanLogger().info(
            'files found for {} (before sorting/filtering):\n{}'.format(version, '\n'.join(foundVersions)))

        # Filter versions according to filterVersion
        foundVersions = [v for v in foundVersions if self.filterVersion(binitem, v)]
        # Sort versions according to sortVersions (uses versionLessThan)
        foundVersions = self.sortVersions(foundVersions)

        VersionScanner.VersionScanLogger().info(
            'files found for {} (after sorting/filtering):\n{}'.format(version, '\n'.join(foundVersions)))

        return foundVersions

    def findNewVersions(self, version):
        """ Scan for files matching an existing Version.

        @param version: An existing Version.

        @return: A list of files corresponding to different Versions of the given Version
        """
        return self.findNewVersionsInPath(self.getFilename(version))

    def findNewVersionsInPath(self, filename):
        """ Scan for files matching an existing path.
        Note: This will include the files used by already added versions.

        @param filename: An existing Version's filename.

        @return: A list of matched files.
        """
        files = set()

        globex = self.getGlobExpression(filename)

        # If the path contains multi-view placeholders, first replace these with
        # wildcards in the glob expression so new versions with any views are found.
        isMultiViewPath = '%v' in filename or '%V' in filename
        if isMultiViewPath:
            globex = globex.replace('%v', '?').replace('%V', '*')

        foundFiles = [foundFile for foundFile in glob.iglob(globex)]
        foundFiles.sort()

        VersionScanner.VersionScanLogger().info('initial file={} glob={} found {} files'
                                                .format(filename, globex, len(foundFiles)))

        # If the original path was multi-view, ensure any matched versions also are
        # and contain the configured view names. In this case convert the matched
        # files back to %v form.
        if isMultiViewPath:
            project = version.parent().project()
            views = project.views()
            foundMultiViewFiles = []
            for foundFile in foundFiles:
                result = findViewInPath(foundFile, views)
                if result and result[1] not in foundMultiViewFiles:
                    foundMultiViewFiles.append(result[1])
            foundFiles = foundMultiViewFiles

        for foundFile in foundFiles:
            foundFile = re.sub('\\\\', '/', foundFile)
            if self.checkNewVersion(filename, foundFile):
                VersionScanner.VersionScanLogger().info('Found new version for file {}'.format(foundFile))
                files.add(foundFile)

        # Clear cache (it is only valid per Version object and needs clearing)
        self._regexMatches = None
        self._visitedClips.clear()

        return files

    def getFilename(self, version):
        """ Get the file name of a given Version

        @param version: A Version.

        @return: The name of the Version's file.
        """
        assert isinstance(version, Version)
        clip = version.item()
        readNode = clip.readNode()

        def cleanPath(path):
            return path.replace('\\', '/')

        # Normalize the original path and the remapped one to avoid issues with
        # backslashes etc. Note: using QDir.cleanPath() to do this because it
        # converts \ to / which is what is wanted here.
        filename = cleanPath(readNode['file'].getValue())

        # Filter through path remapping. If it was remapped, we want to look for files
        # in the remapped location but set the path on the new clips without the remapping,
        # so find the remapped part and store so the remapping be reversed when creating
        # the new clips
        remappedFilename = cleanPath(hiero.core.remapPath(filename))
        if filename != remappedFilename:
            for i in range(-1, 1-len(filename), -1):
                if filename[i] != remappedFilename[i]:
                    self._pathRemaps.add((remappedFilename[0:i+1], filename[0:i+1]))
                    break
        return remappedFilename

    def getActiveIndexFromPath(self, filepath):
        """ Get the active version from a file path. This will be affected by the index detection method. See
        setVersionScanningIndexDetectionMethod() for more details.

        @param filepath: The path of a file.

        @return: The index of a Version, given it's filepath.
        """
        (dirpath, filename) = os.path.split(filepath)

        if (self._versionScanningIndexDetectionMethod is VersionScanner.kDetectVersionDirectoryOnly):
            searchpath = dirpath
        elif (self._versionScanningIndexDetectionMethod is VersionScanner.kDetectVersionFullPath):
            searchpath = filepath

        # Replace version indices
        matches = [match for match in re.finditer(
            VersionScanner._kVersionRegex, searchpath, re.IGNORECASE)]
        if len(matches) > 0:
            # Obtain version index from the last version string, ignore the others
            match = matches[-1]
            versionIndex = int(match.group(2))
        return versionIndex

    def getGlobExpression(self, filename):
        """ Find substrings representing sequence padding (_kPaddedSequenceRegex) and version (_kVersionRegex) and replace them with
        suitable token strings in 'glob' format. For example:

        "/files/clip_v13.%03d.dpx" -> "/files/clip_v***.*"

        "/files/clip_v1.%01d.dpx" -> "/files/clip_v***.*"

        "/files/v3/clip_v1.%01d.dpx" -> "/files/v3/clip_v***.*

        @param filename: The name of the file.

        @return: The given filename reformatted to the 'glob' format.
        """
        # Replace version indices
        matches = [match for match in re.finditer(
            VersionScanner._kVersionRegex, filename, re.IGNORECASE)]
        if len(matches) > 0:

            # Obtain version index from the last version string, ignore the others
            match = matches[-1]

            # Get the version index from the file path
            versionIndex = self.getActiveIndexFromPath(filename)

            # Iterate through matches, if the version string equals versionIndex ("active one"), substitute
            # NB: Reverse iteration guarantees safety of modifying filename by splitting at given positions (match.start() / end())
            for match in reversed(matches):
                prefix = match.group(1)
                index = match.group(2)

                # #mat: This is where we're filtering ONLY on our active version index
                if int(index) == versionIndex:
                    filename = filename[:match.start()] + prefix + \
                        '*' + filename[match.end():]

        # Replace sequence padding.
        matches = [match for match in re.finditer(
            VersionScanner._kPaddedSequenceRegex, filename, re.IGNORECASE)]
        if len(matches) > 0:
            # Iterate through matches, if the version string equals versionIndex ("active one"), substitute
            # NB: Reverse iteration guarantees safety of modifying filename by splitting at given positions (match.start() / end())
            for match in matches:
                # -1 is to remove possibly leading '.' or similar before sequence padding
                pre = filename[:match.start() - 1]
                post = filename[match.end():]
                filename = pre + '*' + post

        # Replace extension
        # NB: This also allows for sequence padding to appear before the extension, in case the original filename did not have a frame number
        filename = os.path.splitext(filename)[0] + '*.*'

        return filename

    def checkNewVersion(self, originalFile, newFile):
        """ Check that newFile correctly matches a version of originalFile, where newFile is a real filename and originalFile includes
        sequence padding tokens (e.g. "%03d").

        @param originalFile: The original file.
        @param newFile: The new file.

        @return: True if the newFiles matches the version of originalFile, False otherwise.
        """
        if self.isVisitedClip(newFile):
            return False

        # ignore backup, tmp and autosave files
        if newFile.endswith('~') or newFile.endswith('.tmp') or newFile.endswith('.autosave'):
            return False

        # Fetch regex matches from cache or compute if needed
        originalVersionMatches = self.getMatches(originalFile)

        # Retrieve original originalVersionString bit for originalFile and check it matches in newFile
        if len(originalVersionMatches) > 0:
            originalVersionString = originalVersionMatches[-1].group(2)
            if not originalVersionString.isdigit():
                VersionScanner.VersionScanLogger().debug(
                    'checkNewVersion: originalVersionString is not digit %s', originalFile)
                return False
            originalVersionIndex = int(originalVersionString)

            # Retrieve version bit for this file
            newVersionMatches = [match for match in re.finditer(
                VersionScanner._kVersionRegex, newFile, re.IGNORECASE)]

            # If several matches, just look at the last one. Also check that we are looking at the right one
            # (same number of matches for original and new versions)
            if len(newVersionMatches) != len(originalVersionMatches):
                VersionScanner.VersionScanLogger().debug(
                    'checkNewVersion: number of originalVersionString strings differ for original and new files %s, %s', originalFile, newFile)
                return False

            # Obtain new version index
            newVersionString = newVersionMatches[-1].group(2)
            if not newVersionString.isdigit():
                VersionScanner.VersionScanLogger().debug(
                    'checkNewVersion: new version is not digit %s', originalFile)
                return False
            newVersionIndex = int(newVersionString)

            # Iterate through matches in the new file, comparing them to the matches in the old one
            for i in range(len(originalVersionMatches)):
                originalVersionIter = originalVersionMatches[i].group(2)
                newVersionIter = newVersionMatches[i].group(2)
                if not (originalVersionIter.isdigit() and newVersionIter.isdigit()):
                    VersionScanner.VersionScanLogger().debug(
                        'checkNewVersion: version is not digit %s, %s', originalFile, newFile)
                    return False
                originalVersionIndexIter = int(originalVersionIter)
                newVersionIndexIter = int(newVersionIter)

                # If this match contains the "active version" for the original file, we need to perform further tests,
                # but otherwise, the string should be the same since the globex replacement did not change it
                if originalVersionIndexIter == originalVersionIndex:
                    if newVersionIndexIter != newVersionIndex:
                        VersionScanner.VersionScanLogger().debug(
                            'checkNewVersion: found version string not updated to new version number %s, %s', originalFile, newFile)
                        return False

            self.markVisitedClip(newFile)
            return True

        VersionScanner.VersionScanLogger().debug(
            'checkNewVersion: No version found for original file %s, %s', originalFile, newFile)
        return False

    def getMatches(self, originalFile):
        """ Convenience function. When we get the glob results, we use regex to compare the original filename with the found files.
        Using _regexMatches, we ensure this regex matches are computed only once for each original filename.

        @param originalFile: The original file.

        @return: The regex matches.
        """
        if self._regexMatches == None:
            # Retrieve original version bit for originalFile and check it matches in newFile
            versionMatches = [match for match in re.finditer(
                VersionScanner._kVersionRegex, originalFile, re.IGNORECASE)]
            self._regexMatches = versionMatches
            return versionMatches

        return self._regexMatches

    def isVisitedClip(self, filename):
        """ Convenience function for determining whether a given file is part of an already visited sequence.

        @param filename: The name of the file.

        @return: True if the file has already been visited, False otherwise.
        """
        filehead = self.getFileHead(filename)

#    VersionScanLogger().debug("isVisitedClip: %s is %d for %s", filename, (filehead in self._visitedClips), self._visitedClips)

        return filehead in self._visitedClips

    def markVisitedClip(self, filename):
        """ Convenience function that will add a file's path to a list of files already visited.

        @param filename: The name of the file.

        @return: Nothing.
        """
        filehead = self.getFileHead(filename)
        self._visitedClips.add(filehead)

    def getFileHead(self, filename):
        """ Extracts "filehead" from "filename", removing sequence numbers.

        @param filename: The name of the file.

        @return: The filehead of the given file.
        """
        newSeqMatches = [match for match in re.finditer(
            VersionScanner._kRawSequenceRegex, filename, re.IGNORECASE)]
        if len(newSeqMatches) > 0:
            # To avoid matching version numbers as sequence numbers, we include in the regex the two leading chars
            # before the sequence number to make sure they are not the prefix "_v". We need to trim this two chars
            # before performing substitution:
            sequence = newSeqMatches[-1].group(0)[2:]
            index = newSeqMatches[-1].start()

            # Let's try putting the extension on to prevent it filtering out .jpg files when we're doing a version scan on .dpx for example
            fileExtension = os.path.splitext(filename)[1]

            return filename[:index] + filename[index:].replace(sequence, '') + fileExtension
        else:
            return filename

    def filterVersion(self, binitem, newVersionFile):
        """ Determine whether the file newVersionFile should be included as a new Version of binitem

        @param binitem: The BinItem.
        @param newVersionFile: The new Version file.

        @return: True if it should be included as a new Version, false otherwise.
        """
        extension = os.path.splitext(newVersionFile)[1]

        movieformats = set(['.mov', '.mp4', '.m4a', '.m4p',
                           '.m4b', '.m4r', '.m4v', '.r3d'])

        ismovieformat = extension.lower() in movieformats
        isorigmovieformat = self._origextension.lower() in movieformats

        # Don't mix movie extensions with sequence extensions as it can much up the frame ranges
        if ismovieformat != isorigmovieformat:
            return False

        index = 0
        while index < binitem.numVersions():
            version = list(binitem.items())[index]
            source = version.item().mediaSource()
            if (source is not None and source.fileinfos() is not None):
                versionFile = source.fileinfos()[0].filename()
                if (versionFile == newVersionFile):
                    return False
            index += 1

        return True

    def sortVersions(self, versionFiles):
        """ Basic bubble sort for versions (we do not expect large numbers of versions).

        @param versionFiles: a list of the Version files to be sorted

        @return: A list containing all the files in versionFiles, sorted according to versionLessThan().
        """
        versions = list(versionFiles)
        stop = False
        while not stop:
            stop = True
            for i in range(len(versions)-1):
                version1 = versions[i]
                version2 = versions[i+1]
                if self.versionLessThan(version2, version1):
                    versions[i] = version2
                    versions[i+1] = version1
                    stop = False
        return versions

    def versionLessThan(self, filename1, filename2):
        """  Compare method for sorting. Compares version filenames according to:
        1st) Version index
        2nd) File extension
        3rd) Full file name.

        @param filename1: The name of the first file
        @param filename2: The name of the second file

        @return: True if filename1 is less that filename2, False if filename2 is less.
        """
        # Retrieve version bit for these files
        newVersionMatches1 = [match for match in re.finditer(
            VersionScanner._kVersionRegex, filename1, re.IGNORECASE)]
        newVersionMatches2 = [match for match in re.finditer(
            VersionScanner._kVersionRegex, filename2, re.IGNORECASE)]

        if len(newVersionMatches1) > 0 and len(newVersionMatches2) > 0:
            # Obtain version indices
            versionString1 = newVersionMatches1[-1].group(2)
            if versionString1.isdigit():
                versionIndex1 = int(versionString1)
            else:
                VersionScanner.VersionScanLogger().debug(
                    'versionLessThan: version is not digit %s', filename1)
                versionIndex1 = -1

            versionString2 = newVersionMatches2[-1].group(2)
            if versionString2.isdigit():
                versionIndex2 = int(versionString2)
            else:
                VersionScanner.VersionScanLogger().debug(
                    'versionLessThan: version is not digit %s', filename2)
                versionIndex2 = -1

            if versionIndex1 != versionIndex2:
                return versionIndex1 < versionIndex2
        else:
            VersionScanner.VersionScanLogger().debug(
                'versionLessThan: could not find version indices in versions %s, %s', filename1, filename2)

        ext1 = os.path.splitext(filename1)[1]
        ext2 = os.path.splitext(filename2)[1]

        if ext1 != ext2:
            return ext1 < ext2

        return filename1 < filename2

    def determineVersionIndex(self, binitem, newFilename):
        """ Get the index at which to insert new version files into a BinItem.

        @param binitem: The BinItem the Version will be inserted into.
        @param newFilename: The name of the Version file being inserted.

        @return: The index at which newFileNames's associated Version should be inserted into the binitem.
        """
        destinationIndex = 0
        while destinationIndex < binitem.numVersions():
            version = list(binitem.items())[destinationIndex]
            if version and version.item() is not None and version.item().mediaSource() is not None:
                if self.versionLessThan(newFilename, version.item().mediaSource().firstpath()):
                    VersionScanner.VersionScanLogger().info('{} was less than version {} {}'.format(
                        newFilename, version, version.item().mediaSource().firstpath()))
                    break
            else:
                VersionScanner.VersionScanLogger().debug(
                    'Problem found with version at position {} of object {}'.format(destinationIndex, binitem))
            destinationIndex += 1
        return destinationIndex

    def insertVersions(self, binitem, versionFiles):
        """ Create Versions for a list of files and insert them into a BinItem.

        @param binitem: The BinItem the Versions will be inserted into.
        @param versionFiles: The list of Version files.

        @return: A list of the created Versions.
        """
        newVersions = []
        for newFilename in versionFiles:
            newVersion = self.createAndInsertClipVersion(binitem, newFilename)
            if newVersion:
                newVersions.append(newVersion)
        return newVersions

    def createAndInsertClipVersion(self, binitem, newFilename):
        """ Create a new Version of a clip for a path and insert it.

        @param binitem: The BinItem for which a new Version will be created.
        @param newFilename: The name of the new Version.

        @return: The created Version, or None if it fails.
        """
        # Reverse any path remapping that was applied to the original clip
        for remappedPath, origPath in self._pathRemaps:
            if newFilename.startswith(remappedPath):
                newFilename = origPath + newFilename[len(remappedPath):]
                break

        destinationIndex = self.determineVersionIndex(binitem, newFilename)
        try:
            newVersion = binitem.createClipVersion(destinationIndex, newFilename)
            VersionScanner.VersionScanLogger().info(
                'creating new version index={} file={}'.format(destinationIndex, newFilename))
            return newVersion
        except RuntimeError as e:
            VersionScanner.VersionScanLogger().error(
                "failed to create version index={} file={} '{}'".format(destinationIndex, newFilename, e))
            return None

    def getVersionIndicesForPath(self, path):
        """ Scan the given path and return a list of all the version indices which exist there.

        @param: The file path to be scanned.

        @return: A sorted list of all the version indicies found in the given path.
        """
        versionFiles = self.findNewVersionsInPath(path)
        versionIndices = sorted([self.getActiveIndexFromPath(path)
                                for path in versionFiles])
        return versionIndices

    def getNewVersionIndexForPath(self, path):
        """ Find the existing versions for the given path, and return a new version index which doesn't
        already exist.

        @param path: The file path of the existing verions.

        @return: An index equal to the current highest Version index incremented by one.
        """
        versionIndices = self.getVersionIndicesForPath(path)
        if versionIndices:
            return versionIndices[-1] + 1
        else:  # If there are no versioned files, raise an exception
            raise RuntimeError('No versioned files found')

    @staticmethod
    def VersionScanLogger():
        """ Returns a logger for logging messages relevant to the VersionScanner

        @return: The VersionScanner logger
        """
        return log.getFileLogger('versionscanner')
