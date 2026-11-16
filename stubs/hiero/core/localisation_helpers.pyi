# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.core as _hiero_core
from hiero.core import Clip as Clip
import hiero as hiero

def setLocalisationForAllVersionsInProject(proj: _hiero_core.Project, policy: Any) -> None:
    """Sets localisation policy for all Versions of All Clips in a project

    @param proj: hiero.core.Project
    @param: policy - the localisation policy from hiero.core.Clip. Options: kOnLocalize, kAutoLocalize, kOnDemandLocalize, kOffLocalize
    """

def setLocalisationPolicyOnBin(bin: Any, policy: Any, recursive: bool = ..., forceUpdate: bool = ...) -> None:
    """Sets localisation policy for all Clips found in a Bin and recursively found in all Sub-Bins

    @param: clipList - a list of hiero.core.Clip objects
    @param: policy - the localisation policy from hiero.core.Clip. Options: kOnLocalize, kAutoLocalize, kOnDemandLocalize, kOffLocalize
    @param: recursive (optional, default = True) - localises all Clips found recursively in a Bin Structure
    @param: forceUpdate - if set to True the clip files will be forced to update in case the localization mode is set to 'Manual'
    """

def setLocalisationPolicyOnClip(clip: Any, policy: Any, forceUpdate: Any) -> None:
    """Set the localisation policy on a clip, optionally forcing it to update the localised
    files.

    @param: clip - a hiero.core.Clip object
    @param: policy - the localisation policy from hiero.core.Clip. Options: kOnLocalize, kAutoLocalize, kOnDemandLocalize, kOffLocalize
    @param: forceUpdate - if set to True the clip files will be forced to update in case the localization mode is set to 'Manual'
    """

def setLocalisationPolicyOnSequence(sequence: Any, policy: Any, forceUpdate: bool = ...) -> None:
    """Sets localisation policy for all Clips used by TrackItems in a Sequence with a given policy.

    @param: sequence - a hiero.core.Sequence object
    @param: policy - the localisation policy from hiero.core.Clip. Options: kOnLocalize, kAutoLocalize, kOnDemandLocalize, kOffLocalize
    @param: forceUpdate - if set to True the clip files will be forced to update in case the localization mode is set to 'Manual'
    """

def setLocalisationPolicyOnTrack(track: Any, policy: Any, forceUpdate: bool = ...) -> None:
    """Sets localisation policy for all Clips used by TrackItems in a Track with a given policy.

    @param: track - a hiero.core.Track object
    @param: policy - the localisation policy from hiero.core.Clip. Options: kOnLocalize, kAutoLocalize, kOnDemandLocalize, kOffLocalize
    @param: forceUpdate - if set to True the clip files will be forced to update in case the localization mode is set to 'Manual'
    """

def setLocalisationPolicyOnTrackItem(trackItem: Any, policy: Any, forceUpdate: bool = ...) -> None:
    """Sets localisation policy for the source Clip of a TrackItem

    @param: track - a  hiero.core.TrackItem object
    @param: policy - the localisation policy from hiero.core.Clip. Options: kOnLocalize, kAutoLocalize, kOnDemandLocalize, kOffLocalize
    @param: forceUpdate - if set to True the clip files will be forced to update in case the localization mode is set to 'Manual'
    """
