"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import ui
import core
import nuke
import hiero
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class Clip(SequenceBase):
    """
    Object representing a clip.

    Initialisation:
      * Clip(mediaSource)
      * Clip(mediaSource, first, last)

    mediaSource may be a MediaSource object or a string containing the media path.  If first and last are given, the Clip only plays frames within this range.
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __repr__(self) -> object:
        """
        Return repr(self).
        """
        ...

    def __setattr__(self, name, value, ) -> None:
        """
        Implement setattr(self, name, value).
        """
        ...

    def __delattr__(self, name, ) -> None:
        """
        Implement delattr(self, name).
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def __bool__(self, ) -> None:
        """
        True if self else False
        """
        ...

    def addTag(self, tag: hiero.core.Tag) -> hiero.core.Tag:
        """
        self.addTag() -> adds the tag to the set of tags attached to the Clip.

        @param tag: the tag object to add
        @return: hiero.core.Tag object
        """
        ...

    def addTagToRange(self, tag: hiero.core.Tag, inTime: int, outTime: int) -> hiero.core.Tag:
        """
        self.addTagToRange(tag, inTime, outTime) -> adds the tag to the specified range of the Clip.

        @param tag: the tag object to add
        @param inTime: from - time to add tag
        @param outTime: to - time to add tag
        @return: hiero.core.Tag object
        """
        ...

    def clone(self, *args, **kwargs) -> Clip:
        """
        self.clone() -> returns a deep copy of this object.

        @return: hiero.core.Clip object

        WARNING - DEPRECATED ( clone ): This method is deprecated and will not be present in future versions of the Python API.
        This method has been replaced by copy().
        """
        ...

    def copy(self) -> object:
        """
        self.copy() -> returns a deep copy of this object.

        @return: hiero.core.Clip object
        """
        ...

    def entityReference(self) -> str:
        """
        self.entityReference() -> returns this clip's asset management system entity reference.

        @return: string
        """
        ...

    def getAvailableOcioColourTransforms(self) -> typing.List[str]:
        """
        self.getAvailableOcioColourTransforms() -> returns colour transform for the source media.

        @return: string
        """
        ...

    def guid(self) -> object:
        """

        """
        ...

    def hasError(self) -> bool:
        """
        self.hasError() -> check if the clip is in error state
        """
        ...

    def hasMultipleViews(self) -> bool:
        """
        self.hasMultipleViews() -> returns true if the Clip has multiple views available for display given the current settings of the project it belongs to.

        @return: bool
        """
        ...

    def isLocalizationOutdated(self) -> bool:
        """
        self.isLocalizationOutdated() -> Returns whether the source media has changed.

        @return: bool
        """
        ...

    def isLocalized(self) -> bool:
        """
        self.isLocalized() -> returns whether the clip is completely localized.

        @return: bool
        """
        ...

    def isNull(self) -> bool:
        """
        self.isNull() -> returns False if this is a valid Clip object, True otherwise.

        @return: True or False
        """
        ...

    def localizationPolicy(self) -> hiero.core.Clip.LocalizationPolicy:
        """
        self.localizationPolicy() -> returns the localization policy of the clip.

        @return: LocalizationPolicy
        """
        ...

    def localizationPriority(self) -> int:
        """
        self.localizationPriority() -> returns localization priority value which determines the order in which files are localized

        @return: int
        """
        ...

    def localizationProgress(self) -> float:
        """
        self.localizationProgress() -> returns the localization progress of the clip, where 0 is totally non-localized and 1 is completely localized.

        @return: double
        """
        ...

    def mediaSource(self) -> hiero.core.MediaSource:
        """
        self.mediaSource() -> returns the clip's media source.

        @return: hiero.core.MediaSource object
        """
        ...

    def metadata(self) -> hiero.core.DataCollection:
        """
        self.isNull() -> returns a *copy* of the clip's metadata.

        @return: hiero.core.Metadata object
        """
        ...

    def numAudioTracks(self) -> int:
        """
        self.numAudioTracks() -> returns number of audio tracks contained by this clip.

        @return: int
        """
        ...

    def numVideoTracks(self) -> int:
        """
        self.numVideoTracks() -> returns number of video tracks contained by this clip.

        @return: int
        """
        ...

    def readNode(self) -> nuke.Node:
        """
        self.readNode() -> returns the Read node representing the Clip's media

        @return: nuke.Node
        """
        ...

    def reconnectMedia(self, path: str) -> None:
        """
        self.reconnectMedia(path) -> Reconnect the Clip with media found in the specified path.

        @param path: path containing media to reconnect to
        """
        ...

    def refresh(self) -> None:
        """
        self.refresh() -> updates the clip if the source media has changed.
        """
        ...

    def removeTag(self, tag: hiero.core.Tag) -> None:
        """
        self.removeTag(tag) -> removes the tag from the clip.

        @param tag: hiero.core.Tag object
        """
        ...

    def rescan(self) -> None:
        """
        self.rescan() -> updates the clip and rescan the frame range if the source media has changed.
        """
        ...

    def setCameraColourTransform(self, arg__1: str) -> None:
        """
        self.setCameraColourTransform(colourTransform) -> sets the camera colour transform for the source media.

        @param colourTransform: Colour transform name
        """
        ...

    def setEntityReference(self, location: str) -> None:
        """
        self.setEntityReference(location) -> set this clip's (asset management system) entity reference.

        @param location: Asset management system's string identifier for the entity.
        """
        ...

    def setFrameRange(self, startFrame: int, endFrame: int) -> None:
        """
        self.setFrameRange() -> Sets the clip frame range to the specified values.
        """
        ...

    def setLocalizationPolicy(self, policy: hiero.core.Clip.LocalizationPolicy) -> None:
        """
        self.setLocalizationPolicy( policy ) -> sets the localization policy to the clip.

        @param policy: localization policy to apply to the clip
        """
        ...

    def setLocalizationPriority(self, priority: int) -> None:
        """
        self.setLocalizationPriority( priority ) -> sets localization priority value which determines the order in which files are localized

        @param: priority int
        """
        ...

    def setSourceMediaColourTransform(self, arg__1: str) -> None:
        """
        self.setSourceMediaColourTransform(colourTransform) -> sets the input colour transform for the source media.

        @param colourTransform: Colour transform name
        """
        ...

    def sourceIn(self) -> int:
        """
        self.sourceIn() -> returns the source in value for the clip.

        @return: frame
        """
        ...

    def sourceMediaColourTransform(self) -> str:
        """
        self.sourceMediaColourTransform() -> returns colour transform for the source media.

        @return: string
        """
        ...

    def sourceOut(self) -> int:
        """
        self.sourceOut() -> returns the source out value for the clip.

        @return: frame
        """
        ...

    def subTrackItems(self) -> object:
        """

        """
        ...

    def views(self) -> typing.List[str]:
        """
        self.views() -> get the list of views available for the clip. If it uses a path with %v/%V, this will return all the views for which media exists. If the source media contains multiple named views, it will return those (note this does not work for mov files). Otherwise returns an empty list.

        return: list(str)
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...

    LocalizationPolicy: Any = None
    kOffLocalize: Any = None
    kOnLocalize: Any = None
    kAutoLocalize: Any = None
    kOnDemandLocalize: Any = None
    kNeverLocalize: Any = None
    kAlwaysLocalize: Any = None

    def addAnnotationsToNukeScript(self, script, firstFrame, trimmed, trimStart=None, trimEnd=None):
        """
        Add the annotations inside a clip to a Nuke script.  This is separated from Clip.addToNukeScript()
        so it's easier to control where in the script the annotations are placed.  The parameters are used to determine
        the frame range for the annotations.
        """
        ...

    def getReadInfo(self, firstFrame=None):
        """
        Get information (filename and start at value) for any Read Node in this clip.

        @param firstFrame: Custom offset to move start frame of clip
        """
        ...

    def addToNukeScript(self, script: hiero.core.nuke.ScriptWriter, additionalNodes=list, additionalNodesCallback=None, firstFrame=None, trimmed=True, trimStart=None, trimEnd=None, colourTransform=None, metadataNode=None, includeMetadataNode=True, nodeLabel=None, enabled=True, includeEffects=True, beforeBehaviour=None, afterBehaviour=None, project=None, readNodes={}, addEffectsLifetime=True):
        """
        addToNukeScript(self, script, trimmed=True, trimStart=None, trimEnd=None)

        Add a Read node to the Nuke script for each media sequence/file used in this clip. If there is no media, nothing is added.

        @param script: Nuke script object to add nodes
        @param additionalNodes: List of nodes to be added post read
        @param additionalNodesCallback: callback to allow custom additional node per item function([Clip|TrackItem|Track|Sequence])
        @param firstFrame: Custom offset to move start frame of clip
        @param trimmed: If True, a TimeClip node will be added to trim the range output by the Read node. The range defaults to the clip's soft trim range. If soft trims are not enabled on the clip, the range defaults to the clip range. The range can be overridden by passing trimStart and/or trimEnd values.
        @param trimStart: Override the trim range start with this value.
        @param trimEnd: Override the trim range end with this value.
        @param colourTransform: if specified, is set as the color transform for the clip
        @param metadataNode: node containing metadata to be inserted into the script
        @param includeMetadataNode: specifies whether a metadata node should be added to the script
        @param nodeLabel: optional label for the Read node
        @param enabled: enabled status of the read node. True by default
        @param includeEffects: if True, soft effects in the clip are included
        @param beforeBehaviour: What to do for frames before the first ([hold|loop|bounce|black])
        @param afterBehaviour: What to do for frames after the last ([hold|loop|bounce|black])
        """
        ...
