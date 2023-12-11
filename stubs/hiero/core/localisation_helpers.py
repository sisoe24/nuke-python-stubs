# localisation_helpers - convenience methods for setting Localisation policy on items of a Project
# Copyright (c) 2012 The Foundry Visionmongers Ltd.  All Rights Reserved.

import hiero.core
from hiero.core import Clip

__all__ = ['setLocalisationPolicyOnClip',
           'setLocalisationPolicyOnTrack',
           'setLocalisationPolicyOnTrackItem',
           'setLocalisationPolicyOnSequence',
           'setLocalisationPolicyOnBin',
           'setLocalisationForAllVersionsInProject']


def setLocalisationPolicyOnClip(clip, policy, forceUpdate):
    """ Set the localisation policy on a clip, optionally forcing it to update the localised
    files.

    @param: clip - a hiero.core.Clip object
    @param: policy - the localisation policy from hiero.core.Clip. Options: kOnLocalize, kAutoLocalize, kOnDemandLocalize, kOffLocalize
    @param: forceUpdate - if set to True the clip files will be forced to update in case the localization mode is set to 'Manual'
    """
    clip.setLocalizationPolicy(policy)
    if forceUpdate:
        clip.readNode().forceUpdateLocalization()


def setLocalisationPolicyOnTrackItem(trackItem, policy, forceUpdate=False):
    """Sets localisation policy for the source Clip of a TrackItem

      @param: track - a  hiero.core.TrackItem object
      @param: policy - the localisation policy from hiero.core.Clip. Options: kOnLocalize, kAutoLocalize, kOnDemandLocalize, kOffLocalize
      @param: forceUpdate - if set to True the clip files will be forced to update in case the localization mode is set to 'Manual'
      """
    if not isinstance(trackItem, hiero.core.TrackItem):
        raise Exception('Firs argument must be a hiero.core.TrackItem')
    else:
        clip = trackItem.source()
        setLocalisationPolicyOnClip(clip, policy, forceUpdate)


def setLocalisationPolicyOnTrack(track, policy, forceUpdate=False):
    """Sets localisation policy for all Clips used by TrackItems in a Track with a given policy.

    @param: track - a hiero.core.Track object
    @param: policy - the localisation policy from hiero.core.Clip. Options: kOnLocalize, kAutoLocalize, kOnDemandLocalize, kOffLocalize
    @param: forceUpdate - if set to True the clip files will be forced to update in case the localization mode is set to 'Manual'
    """
    if not isinstance(track, (hiero.core.VideoTrack, hiero.core.AudioTrack)):
        raise Exception(
            'First argument must be a hiero.core.VideoTrack/hiero.core.AudioTrack')
    else:
        for ti in track:
            setLocalisationPolicyOnTrackItem(ti, policy, forceUpdate)


def setLocalisationPolicyOnSequence(sequence, policy, forceUpdate=False):
    """Sets localisation policy for all Clips used by TrackItems in a Sequence with a given policy.

    @param: sequence - a hiero.core.Sequence object
    @param: policy - the localisation policy from hiero.core.Clip. Options: kOnLocalize, kAutoLocalize, kOnDemandLocalize, kOffLocalize
    @param: forceUpdate - if set to True the clip files will be forced to update in case the localization mode is set to 'Manual'
    """

    if not isinstance(sequence, (hiero.core.Sequence)):
        raise Exception('First argument must be a hiero.core.Sequence')
    else:
        for track in list(sequence.items()):
            for ti in track:
                setLocalisationPolicyOnTrackItem(ti, policy, forceUpdate)


def setLocalisationPolicyOnBin(bin, policy, recursive=True, forceUpdate=False):
    """Sets localisation policy for all Clips found in a Bin and recursively found in all Sub-Bins

    @param: clipList - a list of hiero.core.Clip objects
    @param: policy - the localisation policy from hiero.core.Clip. Options: kOnLocalize, kAutoLocalize, kOnDemandLocalize, kOffLocalize
    @param: recursive (optional, default = True) - localises all Clips found recursively in a Bin Structure
    @param: forceUpdate - if set to True the clip files will be forced to update in case the localization mode is set to 'Manual'
    """

    clips = []

    if not isinstance(bin, (hiero.core.Bin)):
        raise Exception('First argument must be a hiero.core.Bin')
    else:
        if recursive:
            # Here we're going to walk the entire Bin view, for all Clips contained in this Bin
            clips += hiero.core.findItemsInBin(bin, filter=hiero.core.Clip)
        else:
            # Here we just get Clips at the 1st level of the Bin
            clips = bin.clips()

    for clip in clips:
        setLocalisationPolicyOnClip(clip, policy, forceUpdate)


def setLocalisationForAllVersionsInProject(proj, policy):
    """Sets localisation policy for all Versions of All Clips in a project

    @param proj: hiero.core.Project
    @param: policy - the localisation policy from hiero.core.Clip. Options: kOnLocalize, kAutoLocalize, kOnDemandLocalize, kOffLocalize
    """

    clips = hiero.core.findItemsInProject(proj, 'clips')

    for clip in clips:
        bi = clip.binItem()
        for version in list(bi.items()):
            bi.setActiveVersion(version)
            c = bi.activeItem()
            c.setLocalizationPolicy(policy)
