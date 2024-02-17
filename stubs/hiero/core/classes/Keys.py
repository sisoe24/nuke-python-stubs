"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import ui
import core
import hiero
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class Keys(Object):
    """

    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...

    kMediaUmid = 'umid'
    kMediaName = 'name'
    kMediaTapeName = 'tapeName'
    kMediaUrl = 'url'
    kMediaAudioChannels = 'audioChannels'
    kMediaDuration = 'duration'
    kMediaFramerate = 'framerate'
    kMediaFramerateIsNtsc = 'framerateIsNtsc'
    kMediaSamplerate = 'samplerate'
    kMediaMediaType = 'mediaType'
    kMediaMasterMediaType = 'masterMediaType'
    kMediaStartTime = 'startTime'
    kMediaTimecode = 'timecode'
    kMediaForceTimecode = 'forceTimecode'
    kMediaWidth = 'width'
    kMediaHeight = 'height'
    kMediaIsStillFrame = 'stillFrame'
    kSourceUmid = 'foundry.source.umid'
    kSourceFormat = 'foundry.source.format'
    kSourceNumSamples = 'foundry.source.numsamples'
    kSourceWidth = 'foundry.source.width'
    kSourceHeight = 'foundry.source.height'
    kSourcePixelAspectRatio = 'foundry.source.pixelAspect'
    kSourceDuration = 'foundry.source.duration'
    kSourceStartTime = 'foundry.source.starttime'
    kSourceFramerate = 'foundry.source.framerate'
    kSourceSamplerate = 'foundry.source.samplerate'
    kSourceOriginalSamplerate = 'foundry.source.originalsamplerate'
    kSourceNumAudioChannels = 'foundry.source.numaudiochannels'
    kSourceShootTime = 'foundry.source.shoottime'
    kSourceAudioBitDepth = 'foundry.source.audiobitdepth'
    kSourceSize = 'foundry.source.size'
    kSourceShortFileName = 'foundry.source.shortfilename'
    kSourceTimecode = 'foundry.source.timecode'
    kSourceTimecodeDropFrame = 'foundry.source.timecodedropframe'
    kSourceBitmapSize = 'foundry.source.bitmapsize'
    kSourceLayers = 'foundry.source.layers'
    kSourceViews = 'foundry.source.views'
    kSourceViewsDelimiter = ','
    kSourceViewUnspecifiedPrefix = '['
    kSourceViewUnspecifiedPostfix = ']'
    kSourceHasDefaultView = 'foundry.source.hasDefaultView'
    kSourceReelId = 'foundry.source.reelID'
    kSourceGamma = 'foundry.source.gamma'
    kTrackDuration = 'foundry.track.duration'
    kTrackLocked = 'foundry.track.locked'
    kTrackEnabled = 'foundry.track.enabled'
    kTrackBlendEnabled = 'foundry.track.blendEnabled'
    kTrackMaskBlendEnabled = 'foundry.track.maskBlendEnabled'
    kTrackBlendMode = 'foundry.track.blendMode'
    kTrackVolume = 'foundry.track.volume'
    kPlayerTrack = 'foundry.track.player'
    kTimelineName = 'foundry.timeline.name'
    kTimelineFramerate = 'foundry.timeline.framerate'
    kTimelineSamplerate = 'foundry.timeline.samplerate'
    kTimelineDuration = 'foundry.timeline.duration'
    kTimelineIn = 'foundry.timeline.in'
    kTimelineOut = 'foundry.timeline.out'
    kTimelinePoster = 'foundry.timeline.poster'
    kTimelinePosterLayer = 'foundry.timeline.posterLayer'
    kTimelineAudioSynced = 'foundry.timeline.audiosynced'
    kTimelineOverrideOutputFormat = 'foundry.timeline.overrideoutputformat'
    kTimelineOutputFormat = 'foundry.timeline.outputformat'
    kTimelineAutoDiskCacheMode = 'foundry.timeline.autodiskcachemode'
    kSourceInputColourTransform = 'foundry.source.colourtransform'
    kEdlName = 'foundry.edl.name'
    kEdlEditString = 'foundry.edl.editString'
    kEdlEditNumber = 'foundry.edl.editNumber'
    kEdlSourceReel = 'foundry.edl.sourceReel'
    kEdlSrcTimecode = 'foundry.edl.timecode'
    kEdlMode = 'foundry.edl.mode'
    kEdlEffect = 'foundry.edl.effect'
    kEdlTimelineIn = 'foundry.edl.dstIn'
    kEdlTimelineOut = 'foundry.edl.dstOut'
    kEdlSrcIn = 'foundry.edl.srcIn'
    kEdlSrcOut = 'foundry.edl.srcOut'
    kEdlRetime = 'foundry.edl.retime'
    kEdlComments = 'foundry.edl.comments'
    kClipComment = 'foundry.timeline.comment'
    kReadParams = 'foundry.timeline.readParams'
    kColorSpace = 'foundry.timeline.colorSpace'
    kAssetEntityReference = 'foundry.asset.entityReference'
    kQuickTimePreferredMatrix = 'com.apple.quicktime.preferred_matrix'
    kQuickTimePreferredTransfer = 'com.apple.quicktime.preferred_transfer'
    kQuickTimeGamma = 'com.apple.quicktime.gamma'
    kQuickTimePixelEncoding = 'com.apple.quicktime.codec_pixel_encoding'
    kQuickTimeColourspace = 'quicktime.thefoundry.Colorspace'
    kNukePixelEncodingMatrix = 'uk.co.thefoundry.YCbCrMatrix'
    kDDImageRootNodeName = 'media.'
    kMXFPreferredTransfer = 'mxf.thefoundry.PreferredTransfer'
