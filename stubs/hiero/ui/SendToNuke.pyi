# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.core.nuke.Node as _hiero_core_nuke_Node
from hiero.core import TimeBase as TimeBase
from hiero.core import Timecode as Timecode
from hiero.core.FnNukeHelpers import isNonZeroStartFrameMovieFile as isNonZeroStartFrameMovieFile
from hiero.core.nuke import Script as Script
from hiero.core.nuke.Node import AddChannelsNode as AddChannelsNode
from hiero.core.nuke.Node import AddLayerCommand as AddLayerCommand
from hiero.core.nuke.Node import AddTimeCodeNode as AddTimeCodeNode
from hiero.core.nuke.Node import AppendClipNode as AppendClipNode
from hiero.core.nuke.Node import BackdropNode as BackdropNode
from hiero.core.nuke.Node import CompositeNode as CompositeNode
from hiero.core.nuke.Node import ConstantNode as ConstantNode
from hiero.core.nuke.Node import CopyNode as CopyNode
from hiero.core.nuke.Node import DefaultNodeKnobFormatter as DefaultNodeKnobFormatter
from hiero.core.nuke.Node import DissolveNode as DissolveNode
from hiero.core.nuke.Node import DotNode as DotNode
from hiero.core.nuke.Node import FrameRangeNode as FrameRangeNode
from hiero.core.nuke.Node import GroupNode as GroupNode
from hiero.core.nuke.Node import MergeNode as MergeNode
from hiero.core.nuke.Node import MetadataNode as MetadataNode
from hiero.core.nuke.Node import Node as Node
from hiero.core.nuke.Node import PostageStampNode as PostageStampNode
from hiero.core.nuke.Node import PrecompNode as PrecompNode
from hiero.core.nuke.Node import PushNode as PushNode
from hiero.core.nuke.Node import ReadNode as ReadNode
from hiero.core.nuke.Node import ReadNodeKnobFormatter as ReadNodeKnobFormatter
from hiero.core.nuke.Node import ReformatNode as ReformatNode
from hiero.core.nuke.Node import RegisterCustomNukeKnobFormatter as RegisterCustomNukeKnobFormatter
from hiero.core.nuke.Node import RetimeNode as RetimeNode
from hiero.core.nuke.Node import RootNode as RootNode
from hiero.core.nuke.Node import SetNode as SetNode
from hiero.core.nuke.Node import TimeClipNode as TimeClipNode
from hiero.core.nuke.Node import TimeOffsetNode as TimeOffsetNode
from hiero.core.nuke.Node import UserDefinedNode as UserDefinedNode
from hiero.core.nuke.Node import WriteNode as WriteNode
from hiero.core.nuke.Node import WriteNodeKnobFormatter as WriteNodeKnobFormatter
from hiero.core.nuke.Node import appendMetadataNodesForPerFrameTagsToList as appendMetadataNodesForPerFrameTagsToList
from hiero.core.nuke.Node import fixPathForNuke as fixPathForNuke
from hiero.core.nuke.Node import tagAppliesToWhole as tagAppliesToWhole
from hiero.core.nuke.PythonScript import PythonScriptWriter as PythonScriptWriter
from hiero.core.nuke.Script import ScriptWriter as ScriptWriter
import hiero as hiero

NUM_DECIMALS: int
add32Action: Convert32Action
remove32Action: Convert32Action
sendToNukeAction: SendToNukeAction

class SendToNukeAction:
    staticMetaObject: Any
    def __init__(self, menuText: Any, settingsPrefix: str = ...) -> None: ...
    def checkForSoftTrims(self, clips: Any) -> bool: ...
    def doit(self, force32Mode: bool = ...) -> Any: ...
    def eventHandler(self, event: Any) -> None: ...
    def findClips(self, container: Any, clips: Any, parents: Any) -> None: ...
    def getMediaRange(self, clips: Any, useSoftTrims: Any) -> tuple[Any, Any]: ...
    def selectedClips(self) -> tuple[list[Any], dict[Any, Any]]: ...

class Convert32Action(SendToNukeAction):
    staticMetaObject: Any
    def __init__(self, text: Any, settingsPrefix: Any, timebase: Any, timebaseNTSC: Any) -> None: ...
    def doit(self) -> None: ...
    def eventHandler(self, event: Any) -> None: ...

class SendToNukeDialog:
    kRetimeAdd32PulldownText: str
    kRetimeNoneText: str
    kRetimeRemove32PulldownText: str
    kRetimeSpeedText: str
    kRetimeTimebaseText: str
    staticMetaObject: Any
    def __init__(self, enableSoftTrims: Any, clipFps: Any, settingsPrefix: Any, force32Mode: bool = ..., parent: Any = ..., windowTitle: str = ...) -> None: ...
    def accept(self) -> None: ...
    def addReformatNode(self, rootNode: Any) -> None: ...
    def addRetimeNode(self) -> _hiero_core_nuke_Node.Node | None: ...
    def addWriteNode(self, outputPath: Any, inputNode: Any, framerate: Any, projectsettings: Any) -> _hiero_core_nuke_Node.WriteNode: ...
    def createTranscodeUI(self, presetProperties: Any) -> Any: ...
    def fileTypeChanged(self) -> None: ...
    def filenameChanged(self) -> None: ...
    def getFps(self) -> None: ...
    def ingest(self) -> Any: ...
    def outputPath(self) -> Any: ...
    def retimeChanged(self, index: Any) -> None: ...
    def retimeFrameRange(self, start: Any, end: Any) -> tuple[Any, Any, Any]: ...
    def saveSettings(self) -> None: ...
    def scriptPath(self) -> Any: ...
    def useSoftTrims(self) -> Any: ...
