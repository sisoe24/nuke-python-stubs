import os

import FnCyclone
import hiero.core.log
import opentimelineio as otio
from PySide2.QtCore import QUrl


class TransitionType:
    FADE_IN = 0
    FADE_OUT = 1
    DISSOLVE = 2


def _readOpenTimelineIOFile(filePath):
    timeline = None
    try:
        timeline = otio.adapters.read_from_file(filePath)
        # read_from_file returns an object that is not an otio.schema.Timeline instance in some cases, such as after reading
        # a valid JSON file that does not conform to the OpenTimelineIO file format specification documentation.
        if not isinstance(timeline, otio.schema.Timeline):
            hiero.core.log.error(
                'File {} does not contain an OpenTimelineIO timeline.'.format(filePath))
            timeline = None
    except ValueError:
        # read_from_file raises a ValueError exception when filePath is not a valid JSON file.
        hiero.core.log.error('File {} is not a JSON file'.format(filePath))
    except KeyError as e:
        # OpenTimelineIO raises KeyError exceptions when an object being read is missing an attribute of its schema.
        # From this point onwards it can be assumed that all OTIO objects have all expected attributes.
        hiero.core.log.error('{} import error {}'.format(filePath, e))
    except:
        # Unknown exception type.
        hiero.core.log.exception(
            'Unknown exception raised while importing {}.'.format(filePath))

    return timeline


def _getFrameRateFromClips(timeline):
    # This function assumes that the OpenTimelineIO TimeRange rate values of all clips are the same.
    # Returns the first valid frame rate found in the timeline.
    for track in timeline.tracks:
        for clip in track.each_clip():
            try:
                # trimmed_range may raise exceptions for clips that lack both a source_range and an available_range().
                if clip.trimmed_range() is not None:
                    return hiero.core.TimeBase(clip.trimmed_range().duration.rate)
            except otio.exceptions.CannotComputeAvailableRangeError:
                pass

    return hiero.core.TimeBase(24)


def _getSequenceProperties(timeline):
    """
    Obtain the Hiero sequence's starting timecode and frame rate from the OpenTimelineIO data.
    :param timeline: OpenTimelineIO sequence
    :return: Tuple containing the starting timecode and frame rate.
    """
    globalStartTime = timeline.global_start_time
    if globalStartTime is None:
        # If the global_start_time is missing, assume that the starting timecode is 00:00:00.
        sequenceTimecode = 0
        # Estimate the frame rate from the clips present in the timeline.
        frameRate = _getFrameRateFromClips(timeline)
    else:
        sequenceTimecode = globalStartTime.value
        frameRate = hiero.core.TimeBase(globalStartTime.rate)

    return sequenceTimecode, frameRate


def _clipRetime(clip):
    retime = 1.0
    for effect in clip.effects:
        if isinstance(effect, otio.schema.LinearTimeWarp):
            # Also handles otio.schema.FreezeFrame, derived from LinearTimeWarp. time_scalar should be 0.0 in that case.
            retime *= effect.time_scalar
    return retime


def _getClipTimeData(clip):
    try:
        availableRange = clip.available_range()
        mediaStartTime = availableRange.start_time.value
        mediaFrameRate = availableRange.duration.rate
        mediaDuration = availableRange.duration.value
    except otio.exceptions.CannotComputeAvailableRangeError:
        # The clip lacks an available_range entry in the OpenTimelineIO file.
        mediaStartTime = 0.0
        # At this point clip.trimmed_range() has already been checked before, and it is known it will return a valid value.
        mediaFrameRate = clip.trimmed_range().duration.rate
        mediaDuration = clip.trimmed_range().duration.value

    return mediaStartTime, hiero.core.TimeBase(mediaFrameRate), mediaDuration


def _getPathFromURL(urlString):
    url = QUrl(urlString)

    # The importer only needs to consider URLs with the 'file:' scheme or with no scheme at all. URLs without a scheme
    # are absolute or relative file system paths.
    # QUrl.toLocalFile() only returns valid paths when the scheme is set to file. Other cases are handled later.
    if url.isLocalFile():
        localFile = url.toLocalFile()
        # Remove leading '/' for local file path that begins with windows drive letter
        # Qt automatically does this on windows, so this is only required on linux and mac
        if len(localFile) > 2 and localFile[0] == '/' and localFile[2] == ':':
            return localFile[1:]
        return localFile
    elif url.scheme() == '':
        # Since the URL scheme is empty, the url string must be an absolute or relative file system path.
        return urlString
    else:
        # Prevent unsupported schemes from being considered as file system paths.
        raise ValueError(
            'OTIOImporter found a target_url with unsupported scheme: {}'.format(url.scheme()))


def _getMediaPath(media):
    if media is None or isinstance(media, otio.schema.MissingReference) or isinstance(media, otio.schema.GeneratorReference):
        return ''

    isImageSequence = hasattr(media, 'target_url_base')

    if isImageSequence:
        urlString = os.path.join(media.target_url_base, media.name_prefix)
    else:
        urlString = media.target_url

    path = _getPathFromURL(urlString)

    if isImageSequence:
        padding = media.frame_zero_padding

        # Even with zero padding, frame numbers will need to use at least one digit.
        padding = max(1, padding)

        # Huge (and likely incorrect) padding values prevent the "Parsing sequence file" task from ever finishing.
        if padding > 20:
            hiero.core.log.error(
                'OTIOImporter parsed a frame_zero_padding value of {}, which is too large. 0 will be used instead.'.format(
                    padding))
            padding = 0

        path += ('#' * padding) + media.name_suffix

    return path


def _getTransitionType(trackItems, index):
    if index == 0 or isinstance(trackItems[index-1], otio.schema.Gap) or trackItems[index].in_offset.value == 0:
        transitionType = TransitionType.FADE_IN
    elif index >= (len(trackItems)-1) or isinstance(trackItems[index+1], otio.schema.Gap) or trackItems[index].in_offset.value == 0:
        transitionType = TransitionType.FADE_OUT
    else:
        transitionType = TransitionType.DISSOLVE
    return transitionType


class OTIOImporterImpl:
    """ Imports an OpenTimelineIO timeline into Nuke. """

    def __init__(self):
        self._registeredMedia = dict()
        """ Maps a tuple of media properties to a registered media id. """

    def importTimeline(self, timeline):
        # Generate a Hiero sequence from the OTIO timeline.
        sequenceTimecode, frameRate = _getSequenceProperties(timeline)
        timelineProperties = {FnCyclone.kTimelineName: timeline.name,
                              FnCyclone.kTimelineFramerate: frameRate.toInt(),
                              FnCyclone.kTimelineFramerateIsNtsc: frameRate.isNTSC(),
                              FnCyclone.kTimelineSequenceTimecode: sequenceTimecode}
        timelineId = FnCyclone.addSequence(data=timelineProperties)

        # Import all tracks of the sequence.
        for track in timeline.video_tracks():
            self._importTrack(track, FnCyclone.kVideo, timelineId)

        for track in timeline.audio_tracks():
            self._importTrack(track, FnCyclone.kAudio, timelineId)

    def _importTrack(self, track, trackType, timelineId):
        trackProperties = {FnCyclone.kTrackName: track.name,
                           FnCyclone.kTrackType: trackType}
        trackId = FnCyclone.addTrack(parentTimeline=timelineId, data=trackProperties)

        trackItems = list(track)
        prevItemId = FnCyclone.kClipInvalid
        itemIndex = 0
        while itemIndex < len(trackItems):
            if isinstance(trackItems[itemIndex], otio.schema.Transition):
                # Importing a transition may require importing the next item in the list, so _importTransition will return the
                # correct index.
                itemIndex, prevItemId = self._importTransition(
                    trackItems, itemIndex, prevItemId, trackId, trackType)

            elif isinstance(trackItems[itemIndex], otio.schema.Clip):
                prevItemId = self._importClip(trackItems[itemIndex], trackId, trackType)
            itemIndex = itemIndex + 1

    def _importTransition(self, trackItems, index, prevItemId, trackId, trackType):
        transitionType = _getTransitionType(trackItems, index)

        nextItemId = FnCyclone.kClipInvalid
        if transitionType is not TransitionType.FADE_OUT:
            nextItemId = self._importClip(trackItems[index+1], trackId, trackType)

        if transitionType == TransitionType.FADE_IN:
            prevItemId = FnCyclone.kClipInvalid

        data = {FnCyclone.kTransitionInDuration: trackItems[index].in_offset.value,
                FnCyclone.kTransitionOutDuration: trackItems[index].out_offset.value,
                FnCyclone.kTransitionExclusive: 0}

        FnCyclone.addTransition(inClip=prevItemId, outClip=nextItemId, data=data)

        if transitionType is not TransitionType.FADE_OUT:
            index = index + 1
            prevItemId = nextItemId
        return index, prevItemId

    def _importClip(self, clip, trackId, trackType):
        try:
            trimmed_range = clip.trimmed_range()
        except otio.exceptions.CannotComputeAvailableRangeError:
            hiero.core.log.error(
                'Found opentimelineio.schema.Clip instance without a valid TimeRange.')
            return

        clipProperties = {FnCyclone.kClipName: clip.name,
                          FnCyclone.kClipSourceIn: trimmed_range.start_time.value,
                          FnCyclone.kClipTimelineIn: clip.range_in_parent().start_time.value,
                          FnCyclone.kClipDuration: trimmed_range.duration.value,
                          FnCyclone.kClipRetime: _clipRetime(clip),
                          FnCyclone.kMediaType: trackType}

        clipId = FnCyclone.addClip(parentTrack=trackId, data=clipProperties)

        # Try importing the media reference of this clip, and set the clip media if this operation succeeds.
        mediaId = self._importMedia(clip)
        if mediaId is not None:
            FnCyclone.setClipMediaByTimecode(clip=clipId, media=mediaId)

        return clipId

    def _importMedia(self, clip):
        mediaReference = clip.media_reference

        try:
            path = _getMediaPath(mediaReference)
        except ValueError as v:
            hiero.core.log.error(v)
            return None

        mediaName = mediaReference.name if mediaReference is not None else ''

        mediaStartTime, mediaFrameRate, mediaDuration = _getClipTimeData(clip)

        if hasattr(mediaReference, 'frame_step') and mediaReference.frame_step != 1:
            hiero.core.log.error('Unsupported media reference frame_step={} value found. 1 will be used instead.'.format(
                mediaReference.frame_step))
        elif isinstance(mediaReference, otio.schema.GeneratorReference):
            hiero.core.log.error(
                'otio.schema.GeneratorReference are currently treated as missing media.')

        mediaProperties = {FnCyclone.kMediaUrl: path,
                           FnCyclone.kMediaName: mediaName,
                           FnCyclone.kMediaTapeName: mediaName,
                           FnCyclone.kMediaAudioChannels: '0',
                           FnCyclone.kMediaStartTime: mediaStartTime,
                           FnCyclone.kMediaTimecode: mediaStartTime,
                           FnCyclone.kMediaForceTimecode: False,
                           FnCyclone.kMediaDuration: mediaDuration,
                           FnCyclone.kMediaFramerate: mediaFrameRate.toInt(),
                           FnCyclone.kMediaFramerateIsNtsc: mediaFrameRate.isNTSC(),
                           FnCyclone.kMediaSamplerate: mediaFrameRate.toInt()}

        # Properties used for checking if two media references should be imported as the same clip.
        mediaKey = path, mediaStartTime, mediaDuration, mediaFrameRate.toInt()

        mediaId = self._registeredMedia.get(mediaKey)
        # If the media key is not present in the dictionary, register the media and add it to the dictionary.
        if mediaId is None:
            mediaId = FnCyclone.addMedia(data=mediaProperties)
            self._registeredMedia[mediaKey] = mediaId

        return mediaId


class OtioImporter:
    """
    Implements the member functions required for an importer.
    """

    def __init__(self):
        pass

    def displayName(self):
        return 'Foundry OpenTimelineIO Importer'

    def isOptionRequired(self, _):
        return False

    def isValidFile(self, filePath):
        if not os.path.isfile(filePath):
            return False
        _, extension = os.path.splitext(filePath)
        return extension.lower() == '.otio'

    def importFile(self, filePath):
        timeline = _readOpenTimelineIOFile(filePath)
        if timeline is None:
            # Errors have already been handled and logged. See _readOpenTimelineIOFile for details.
            return False

        OTIOImporterImpl().importTimeline(timeline)

        return True
