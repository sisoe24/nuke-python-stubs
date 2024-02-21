# Copyright (c) 2022 The Foundry Visionmongers Ltd. All Rights Reserved.

import os
import traceback

import hiero.core
import nuke_internal as nuke
import opentimelineio as otio
from PySide2.QtCore import QUrl


class OTIOTimelineBuilder:
    """ Helper class for creating an otio.schema.Timeline from a hiero.core.Sequence
    object.
    """

    def __init__(self, sequence):
        self._sequence = sequence
        self._warnings = []

    def buildTimeline(self):
        """ Create the timeline """
        otioTimeline = otio.schema.Timeline(name=self._sequence.name())
        otioTimeline.global_start_time = self._makeTime(self._sequence.timecodeStart())

        # Add some metadata about the Nuke version
        otioTimeline.metadata['nuke'] = {'version': nuke.env['NukeVersionString']}

        for track in self._sequence.videoTracks():
            otioTimeline.tracks.append(self._buildTrack(track))
        for track in self._sequence.audioTracks():
            otioTimeline.tracks.append(self._buildTrack(track))
        return otioTimeline

    def warnings(self):
        """ Get the list of warnings from building the timeline """
        return self._warnings

    def _addWarning(self, msg):
        """ Add a warning """
        self._warnings.append(msg)

    def _makeTime(self, frame, framerate=None):
        # Create a RationalTime object, if framerate not given uses the sequence rate
        framerate = framerate or self._sequence.framerate().toFloat()
        return otio.opentime.RationalTime(frame, framerate)

    def _makeRange(self, start, duration, framerate=None):
        # Create a TimeRange object from values or RationalTime objects.
        # If framerate not given uses the sequence rate
        if not isinstance(start, otio.opentime.RationalTime):
            start = self._makeTime(start, framerate)
        if not isinstance(duration, otio.opentime.RationalTime):
            duration = self._makeTime(duration, framerate)
        return otio.opentime.TimeRange(start_time=start, duration=duration)

    def _buildTrack(self, track):
        # Create an OTIO Track from a Hiero one
        otioTrack = otio.schema.Track(name=track.name())
        otioTrack.kind = 'Video' if isinstance(track, hiero.core.VideoTrack) else 'Audio'
        prevTrackItem = None
        for trackItem in track:
            # Add gaps if needed
            gap = trackItem.timelineIn() if not prevTrackItem else trackItem.timelineIn() - \
                (prevTrackItem.timelineOut()+1)
            if gap:
                otioTrack.append(otio.schema.Gap(source_range=self._makeRange(0, gap)))

            inTransition = trackItem.inTransition()
            if inTransition:
                self._appendTransition(otioTrack, inTransition, prevTrackItem)

            otioTrack.append(self._buildClip(trackItem))

            # Because a dissolve will be the inTransition of the next trackItem, ignore the current track item's
            # outTransition if it is a dissolve.
            outTransition = trackItem.outTransition()
            if outTransition and outTransition.alignment() != hiero.core.Transition.Alignments.kDissolve:
                self._appendTransition(otioTrack, outTransition, prevTrackItem)

            prevTrackItem = trackItem
        return otioTrack

    def _buildClip(self, trackItem):
        # Create an OTIO Clip from a Hiero TrackItem
        clip = trackItem.source()
        # If the frame rates do not match, store the start in the source rate and the
        # duration at the sequence rate. Unsure if this is correct, but it seems the
        # only way for this to work
        if clip.framerate() != self._sequence.framerate():
            self._addWarning("Clip '{}' frame rate {} does not match sequence".format(
                clip.name(), clip.framerate()))
        srcStartTime = self._makeTime(clip.timecodeStart(
        ) + trackItem.sourceIn(), framerate=clip.framerate().toFloat())
        srcRange = self._makeRange(srcStartTime, trackItem.duration())
        otioMediaRef = self._buildMediaReference(clip)
        otioClip = otio.schema.Clip(name=trackItem.name(),
                                    media_reference=otioMediaRef,
                                    source_range=srcRange)
        # Handle retimes
        speed = trackItem.playbackSpeed()
        if speed == 0.0:
            otioClip.effects.append(otio.schema.FreezeFrame())
        elif speed != 1.0:
            otioClip.effects.append(otio.schema.LinearTimeWarp(time_scalar=speed))
        hasTimeWarp = next((item for item in trackItem.linkedItems() if isinstance(
            item, hiero.core.EffectTrackItem) and item.isRetimeEffect()), None)
        if hasTimeWarp:
            self._addWarning(
                "Track item '{}' has TimeWarp effect which is not supported by OTIO export".format(trackItem.name()))
        return otioClip

    def _appendTransition(self, otioTrack, transition, prevTrackItem):
        duration = transition.timelineOut() - transition.timelineIn()
        if transition.alignment() == hiero.core.Transition.Alignments.kDissolve:
            inOffset = prevTrackItem.timelineOut() - transition.timelineIn() + 1
            outOffset = duration - inOffset + 1
        elif transition.alignment() == hiero.core.Transition.Alignments.kFadeIn:
            inOffset = 0
            outOffset = duration + 1
            otioTrack.append(otio.schema.Gap(source_range=self._makeRange(0, 0)))
        elif transition.alignment() == hiero.core.Transition.Alignments.kFadeOut:
            inOffset = duration + 1
            outOffset = 0

        otioTrack.append(otio.schema.Transition(name='Transition',
                                                transition_type='SMPTE_Dissolve',
                                                in_offset=self._makeTime(inOffset),
                                                out_offset=self._makeTime(outOffset)))

        if transition.alignment() == hiero.core.Transition.Alignments.kFadeOut:
            otioTrack.append(otio.schema.Gap(source_range=self._makeRange(0, 0)))

    def _buildMediaReference(self, clip):
        # Create an OTIO MediaReference from a Hiero Clip
        mediaSource = clip.mediaSource()
        sourceRange = self._makeRange(mediaSource.timecodeStart(
        ), mediaSource.duration(), framerate=clip.framerate().toFloat())
        if mediaSource.singleFile():
            # Single media file, create an ExternalReference
            path = mediaSource.firstpath()
            url = QUrl.fromLocalFile(path).toString(QUrl.FullyEncoded)
            return otio.schema.ExternalReference(target_url=url, available_range=sourceRange)
        else:
            # Image file sequence, create an ImageSequenceReference
            fileInfo = mediaSource.fileinfos()[0]
            namePrefix = mediaSource.filenameHead()
            dirPath, _ = os.path.split(fileInfo.filename())
            _, nameSuffix = os.path.splitext(fileInfo.filename())
            return otio.schema.ImageSequenceReference(
                available_range=sourceRange,
                start_frame=fileInfo.startFrame(),
                frame_step=1,
                rate=clip.framerate().toFloat(),
                target_url_base=QUrl.fromLocalFile(dirPath).toString(QUrl.FullyEncoded),
                name_prefix=namePrefix,
                name_suffix=nameSuffix,
                frame_zero_padding=mediaSource.filenamePadding())


class OTIOExportTask(hiero.core.TaskBase):
    """ Export task for exporting a Sequence as an OTIO file """

    def __init__(self, initDict):
        hiero.core.TaskBase.__init__(self, initDict)

    def startTask(self):
        pass

    def taskStep(self):
        return False

    def finishTask(self):
        try:
            # Create the OTIO Timeline structure and write to the target file
            builder = OTIOTimelineBuilder(self._sequence)
            otioTimeline = builder.buildTimeline()
            if builder.warnings():
                self.setWarning('\n'.join(builder.warnings()))
            exportPath = self.resolvedExportPath()
            # check export root exists
            dir = os.path.dirname(exportPath)
            hiero.core.util.filesystem.makeDirs(dir)
            otio.adapters.write_to_file(otioTimeline, exportPath)
        except Exception as e:
            self.setError(traceback.format_exc())
        hiero.core.TaskBase.finishTask(self)


class OTIOExportPreset(hiero.core.TaskPresetBase):
    """ Export preset for OTIO file export """

    def __init__(self, name, properties):
        hiero.core.TaskPresetBase.__init__(self, OTIOExportTask, name)

    def supportedItems(self):
        return hiero.core.TaskPresetBase.kSequence

    def addCustomResolveEntries(self, resolver):
        resolver.addResolver('{ext}', 'Extension of the file to be output',
                             lambda keyword, task: 'otio')

    def supportsAudio(self):
        return True


hiero.core.taskRegistry.registerTask(OTIOExportPreset, OTIOExportTask)
