# Type stubs for nuke 17.1v2. Generated; do not edit.

"""Code for writing hiero objects to Nuke scripts. This is an attempt to
replace the code in FnNukeHelpers.py, done in parallel so we can change things
on a case-by-case basis and avoid breaking everything. Hopefully the old code
can be removed before too long..
"""

from typing import Any
import hiero.core.nuke.Node as _hiero_core_nuke_Node
import hiero.core.nuke.Script as _hiero_core_nuke_Script
from hiero.core import FnNukeHelpers as FnNukeHelpers
from hiero.core import Transition as Transition
from hiero.core import nuke as nuke
from hiero.core.FnEffectHelpers import FormatChange as FormatChange
from hiero.core.FnEffectHelpers import transformNodeToFormatChange as transformNodeToFormatChange
from hiero.core.FnNukeHelpers import createAndAddNodesToGroupNode as createAndAddNodesToGroupNode
from hiero.core.FnNukeHelpers import generateUniqueSetNodeId as generateUniqueSetNodeId
from hiero.core.nuke.Node import ReformatNode as ReformatNode
import hiero as hiero

gJumpCount: int

class EffectsTrackJump:
    """Object which stores the jumpname for an effects track"""
    def __init__(self, track: Any) -> None: ...
    def getJumpName(self) -> str: ...
    def setJumpName(self, name: Any) -> None: ...

class ReadNodeInstanceInfo:
    """Simple class to hold the 3 parameters that will allow us to instance ReadNodes."""
    def __init__(self, startAt: Any, totalInstances: Any, instancesUsed: Any, readNodeID: Any) -> None: ...

class ReadNodeUsageCollator:
    """Class used to keep track of all instances of Read Nodes throughout
    a project. This enables us to replace multiple instances of the same Read
    Node with PostageStamps.
    """
    def __init__(self) -> None: ...
    def collateReadNodes(self, tracks: Any, params: Any, offset: Any, view: Any = ...) -> None: ...
    def getReadNodes(self) -> dict[Any, Any]: ...

class ScriptWriteParameters:
    """Class for specifying parameters when writing to Nuke scripts. """
    def __init__(self, includeEffects: bool = ..., retimeMethod: Any = ..., reformatMethod: Any = ..., additionalNodesCallback: Any = ..., views: Any = ...) -> None:
        """@param includeEffects: whether effects should be written to the script
        @param retimeMethod: method for retimes, if None retimes will not be included
        in the script
        @additionalNodesCallback: callback function for injecting additional nodes
        into the script, should return a list of the nodes
        """
    def doAdditionalNodesCallback(self, *args: Any) -> list[Any]:
        """If a callback for additional nodes has been set, call it, otherwise
        returns an empty list.
        """
    def includeEffects(self) -> bool:
        """Get whether effects should be included in the script. """
    def includeRetimes(self) -> bool:
        """Get whether retimes should be included in the script. """
    def retimeMethod(self) -> None:
        """Get the method used for retiming in the created OFlow node. """
    def views(self) -> list[Any]: ...

class SequenceScriptWriter:
    """Class for writing Sequences to a Nuke script. """
    def __init__(self, sequence: Any, params: Any) -> None: ...
    def needJoinViews(self) -> bool:
        """Test if the views need to be written separately and connected to a JoinViews
        node. This is the case if any of the tracks are set to output to a single view 
        """
    def writeToScript(self, script: Any, offset: Any = ..., skipOffline: bool = ..., mediaToSkip: Any = ..., disconnected: bool = ..., masterTracks: Any = ..., projectSettings: Any = ...) -> None: ...
    def writeTracks(self, connectedTracks: Any, disconnectedTracks: Any, script: Any, offset: Any, skipOffline: Any, mediaToSkip: Any, projectSettings: Any = ...) -> Any:
        """Write a set of tracks, some of which may not be connected to any output.
        If there are multiple connected these are connected to a Merge node.
        Returns a jump name for the final output node.
        """
    def writeTracksWithJoinViews(self, script: Any, offset: Any, skipOffline: Any, mediaToSkip: Any, disconnected: Any, masterTracks: Any) -> None:
        """Write the tracks for each view separately and then add a JoinViews node """

class TrackItemScriptWriter:
    """Class for writing TrackItems to a Nuke script. There are two somewhat different
    cases for this:

    1) Writing as part of a sequence, using the TrackItem's timeline in/out etc, with
    an optional offset from those times.
    This will extend the range to cover dissolves.
    It will also include any retimes applied to the TrackItem.

    2) Writing as a single shot. In this case a firstFrame value is usually given.
    This will be the first frame of the script being written and is inclusive of any
    handles, which will come from any dissolves, and also from custom handles
    specified by the user.
    Retimes may or may not be included in the export, which affects all the range
    calculations.
    """
    def __init__(self, trackItem: Any, params: Any, firstFrame: Any = ..., startHandle: Any = ..., endHandle: Any = ..., offset: Any = ...) -> None:
        """@param firstFrame: optional frame for the Read node to start at, including
                           handles if there are any
        @param startHandle: the number of frames of handles to include at the start
        @param endHandle: the number of frames of handles to include at the end
        @param offset: global frame offset applied across whole script, note this
                       is mutually exclusive with firstFrame
        """
    def addChannelNodeToScript(self, script: Any, added_nodes: Any) -> None:
        """We need an AddChannels node to add full alpha to the track.
        We want this put into a custom channel, so that it doesn't affect
        other parts of the comp - The Merge node will just be told to use
        this channel for its A alpha.
        First we need to create the layer which will contain the custom channel
        """
    def findLinkedEffects(self) -> list[Any]:
        """Find effects linked to the track item being written. """
    def getClipColorTransform(self, projectSettings: Any, clip: Any) -> str | None: ...
    def getColorspaceFromProperty(self, lutValue: Any) -> Any:
        """Get just the colorspace name (in parentheses if the LUT value is a role)."""
    def getReadNodeInfo(self) -> Any:
        """Helper function to get usage information about Read Nodes for this track item"""
    def makeOutputReformatNode(self) -> _hiero_core_nuke_Node.ReformatNode | None:
        """If outputting to a different format from the clip (e.g. to the sequence
        format), create a ReformatNode to do this. If no output format is set, or
        it's the same as that of the clip, returns None.
        """
    def outputFormat(self) -> Any:
        """Get the output format for the track item. """
    def writeEffects(self, script: Any, effectOffset: Any, additionalEffects: Any, transformToClipFormat: Any, pendingNodesScript: Any) -> list[Any]:
        """Write the track item's linked effects plus any additional sequence-level
        ones.
        """
    def writeFadeInAndOutTransitions(self, script: Any, added_nodes: Any) -> None: ...
    def writeReformatAndEffects(self, script: Any, additionalEffects: Any, pendingNodesScript: Any) -> list[Any]:
        """Write the nodes for reformat and effects, if needed. When outputting to
        sequence format, the reformat goes first. In other cases, the effects are
        modified to fit the input clip's format, and the reformat node is added after.
        """
    def writeToScript(self, script: _hiero_core_nuke_Script.ScriptWriter = ..., nodeLabel: Any = ..., additionalEffects: Any = ..., addChannelNode: bool = ..., readNodes: Any = ..., addTimeClip: bool = ..., projectSettings: Any = ..., pendingNodesScript: Any = ..., addTransitions: bool = ...) -> Any:
        """Writes the TrackItem to a script. Returns the added nodes.
        @param script: the script writer to add nodes to
        @param nodeLabel: label for the Read node
        @param additionalEffects: unlinked effects on the sequence which should be
                                  included
        @param addChannelNode: add an AddChannels Node to the TrackItem, which will
                               inject a full alpha channel to Node tree
        @param pendingNodesScript Certain nodes must not be added to the script immediately. They are stored here.
        @param addTransitions add fade-in/out transitions to the script.
        """

class VideoTrackScriptWriter:
    """Class for writing VideoTracks to a Nuke script. """
    def __init__(self, track: Any, params: Any) -> None: ...
    def allTrackItemsDisabled(self) -> bool: ...
    def getJumpName(self) -> str: ...
    def getMaskJumpName(self) -> str: ...
    def setJumpName(self, name: Any) -> None: ...
    def writeToScript(self, script: _hiero_core_nuke_Script.ScriptWriter = ..., offset: Any = ..., skipOffline: bool = ..., mediaToSkip: Any = ..., disconnected: bool = ..., needToAddChannelNode: bool = ..., readNodes: Any = ..., projectSettings: Any = ...) -> list[Any]: ...

def addSetAndPushNode(script: Any, added_nodes_list: Any) -> None: ...

def makeJumpNameForTrack(track: Any) -> str:
    """Makes a jump name for the track. This is the name which shall be used to identify the
    'set' and the 'push' nodes which corrispond to each track. This name consists of the Track
    Name (with any non-alphanumeric characters replaced by _) and also a global counter which
    is to make sure we don't get duplicate names.
    """

def removeBottomEmptyTracks(tracks: Any) -> list[Any]:
    """Remove tracks that do not contain any track items and are below the
    first track that does contain track items.

    Assumes tracks are ordered bottom -> top
    """
