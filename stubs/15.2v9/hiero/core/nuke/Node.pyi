# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero as hiero

class Node:
    """Base class for objects which represent elements in the written Nuke script.  Note that not all Node
    objects are actually nodes, some are just used to insert tcl commands into the script. 
    """
    USER_KNOB_TYPE_CHECKBOX: int
    USER_KNOB_TYPE_FILENAME: int
    USER_KNOB_TYPE_INPUTTEXT: int
    USER_KNOB_TYPE_TAB: int
    kNodeAlignX: int
    kNodeAlignY: int
    def __init__(self, nodeType: Any, inputNode0: Any = ..., inputNodes: Any = ..., **keywords: Any) -> None: ...
    def addCheckboxKnob(self, knobName: Any, text: Any = ..., tooltip: Any = ..., value: bool = ..., visible: bool = ...) -> None:
        """Add a checkbox knob. """
    def addEnabledRange(self, startRange: Any, endRange: Any, firstCompFrame: Any) -> None:
        """Add a Range of KeyFrames for which the Node is enabled. """
    def addFilenameKnob(self, knobName: Any, text: Any = ..., tooltip: Any = ..., value: Any = ..., visible: bool = ...) -> None:
        """Add a filename knob. """
    def addInputTextKnob(self, knobName: Any, text: Any = ..., tooltip: Any = ..., value: Any = ..., visible: bool = ...) -> None:
        """Add an input text knob. """
    def addRawKnob(self, text: Any) -> None:
        """Add raw knob text to the node.  This is written directly to the script with no formatting. """
    def addTabKnob(self, knobName: Any, text: Any = ..., tooltip: Any = ...) -> None:
        """Add a tab knob. """
    def formatString(self, width: Any, height: Any, pixelAspect: Any = ...) -> str:
        """Helper function for creating a format string. """
    def getAlignToNode(self) -> None:
        """Get the node to align this one to when the script is laid out. """
    def getAlignmentOffsetX(self) -> int:
        """Get the X alignment offset. """
    def getAlignmentOffsetY(self) -> int:
        """Get the Y alignment offset. """
    def getNodeAlignment(self) -> int:
        """Get the Alignment direction between this Node and its AlignTo Node. """
    def getNodeSize(self) -> tuple[int, int]:
        """Get the size of the node.  This is an estimate, since in Nuke the size can be affected by
        the font size (and possibly other factors), but it works in most cases for layout of scripts. 
        """
    def getPosition(self) -> tuple[Any, Any] | tuple[None, None]:
        """Try to get the position of the node if it's been set, otherwise returns None, None. """
    def getTopSpacing(self) -> int:
        """Get the spacing that will be added to the Node's top position. """
    def inputNodes(self) -> dict[Any, Any]: ...
    def isNode(self) -> bool:
        """Check if this is actually a node, as opposed to a tcl command.  This default implementation
        looks at the node type string, if it starts with an upper case character it's treated as a node. 
        """
    def knob(self, knobName: Any) -> Any:
        """Get a knob value.  An exception is raised if no knob of that name exists. """
    def knobs(self) -> dict[Any, Any]:
        """Get a dict with all the node's knobs. """
    def serialize(self, serializer: Any) -> None:
        """Serialize the node to the given serializer object. """
    def setAlignToNode(self, node: Any, alignment: Any = ...) -> None:
        """Set the node to align this one to when the script is laid out. """
    def setAlignmentOffset(self, alignmentOffsetX: Any, alignmentOffsetY: Any) -> None:
        """Set an offset to add space between this Node and its AlignTo Node. """
    def setInputNode(self, index: Any, node: Any) -> None: ...
    def setKnob(self, knobName: Any, knobValue: Any) -> None:
        """Set a knob value. """
    def setName(self, name: Any) -> None:
        """Set the node name. """
    def setPosition(self, xpos: Any, ypos: Any) -> None:
        """Set the xpos and ypos knobs for the node position. """
    def type(self) -> Any:
        """Get the node type. """

class AddChannelsNode(Node):
    def __init__(self) -> None: ...

class AddLayerCommand(Node):
    """This class doesn't represent a Nuke Node, instead it injects add_layer commands into
    the script. Since these have similar formatting to Nodes, this is enough to achieve this
    """
    def __init__(self) -> None: ...

class AddTimeCodeNode(Node):
    def __init__(self, timecodeStart: Any, fps: Any, dropFrames: Any, frame: Any = ..., metafps: bool = ..., inputs: Any = ..., inputNode: Any = ...) -> None:
        """timecodeStart should be a time (frame) value, fps should be a TimeBase object, and dropFrames should be true or false"""

class AppendClipNode(Node):
    def __init__(self, inputs: Any, inputNode: Any = ..., **kwargs: Any) -> None: ...

class BackdropNode(Node):
    """BackdropNode class. """
    def __init__(self, xpos: Any, ypos: Any, width: Any, height: Any) -> None:
        """Construct the backdrop with x, y, width, height. """
    def getNodeSize(self) -> tuple[Any, Any]:
        """Get the backdrop size. """
    def setColor(self, color: Any) -> None:
        """Set the backdrop color. """
    def setLabel(self, text: Any) -> None:
        """Set the node label.  Adds the center tag to it. """
    def setLabelFontSize(self, size: Any) -> None:
        """Set the font size of the label. """
    def setZOrder(self, zorder: Any) -> None:
        """Set the z ordering for the backdrop. """

class CompositeNode(Node):
    def __init__(self, nodeType: Any, inputNode0: Any = ..., inputNodes: Any = ..., **keywords: Any) -> None: ...
    def addNode(self, node: Any) -> None: ...
    def getNodes(self) -> list[Any]: ...
    def serialize(self, serializer: Any) -> None: ...

class ConstantNode(Node):
    """Constant node class. """
    def __init__(self, first: Any, last: Any, channels: str = ..., **knobs: Any) -> None:
        """Construct the node with first and last frames. """
    def getNodeSize(self) -> tuple[int, int]:
        """Get the size of the node.  This is an estimate, since in Nuke the size can be affected by
        the font size (and possibly other factors), but it works in most cases for layout of scripts. 
        """

class CopyNode(Node):
    def __init__(self, inputNodes: Any = ...) -> None: ...

class DefaultNodeKnobFormatter:
    def serialize(self, serializer: Any, nodeType: Any, knobValues: Any, userKnobs: Any, rawKnobs: Any) -> None: ...

class DissolveNode(Node):
    """Dissolve node. """
    def __init__(self) -> None: ...
    def getNodeSize(self) -> tuple[int, int]:
        """Get the size of the node.  This is an estimate, since in Nuke the size can be affected by
        the font size (and possibly other factors), but it works in most cases for layout of scripts. 
        """
    def setWhichKeys(self, *keys: Any) -> None:
        """Set the keys for the which knob as a set of tuples with (frame, value) """

class DotNode(Node):
    """Dot node class. """
    def __init__(self, **knobs: Any) -> None:
        """Construct the node. """
    def align(self, inputNode: Any, outputNode: Any) -> None:
        """align the Node vertically below its input and horizontally with its output. """
    def getNodeSize(self) -> tuple[int, int]:
        """Get the size of the node.  This is an estimate, since in Nuke the size can be affected by
        the font size (and possibly other factors), but it works in most cases for layout of scripts. 
        """

class FrameRangeNode(Node):
    """FrameRange node class. """
    def __init__(self, first_frame: Any, last_frame: Any) -> None:
        """Construct the node with first and last frame. """
    def getNodeSize(self) -> tuple[int, int]:
        """Get the size of the node.  This is an estimate, since in Nuke the size can be affected by
        the font size (and possibly other factors), but it works in most cases for layout of scripts. 
        """

class GroupNode(CompositeNode):
    def __init__(self, name: Any, **kwargs: Any) -> None: ...
    def serialize(self, serializer: Any) -> None: ...

class MergeNode(Node):
    def __init__(self, inputNodes: Any = ...) -> None: ...
    def getNodeSize(self) -> tuple[int, int]:
        """Get the size of the node.  This is an estimate, since in Nuke the size can be affected by
        the font size (and possibly other factors), but it works in most cases for layout of scripts. 
        """
    def layoutDotInputs(self) -> None: ...
    def setDotInputs(self, dotAInput: Any = ..., dotMaskInput: Any = ...) -> None: ...

class MetadataNode(Node):
    """Class which corresponds to the Nuke ModifyMetaData node. """
    kCharacterEscapeTable: tuple
    def __init__(self, metadatavalues: Any = ..., inputNode: Any = ..., inputs: Any = ...) -> None: ...
    def addMetadata(self, metadatavalues: Any) -> None:
        """Add keys/values to the metadata.  metadatavalues should either be a dict or a list of tuples with (key, value). """
    def addMetadataFromTag(self, tag: Any, prefix: Any) -> None:
        """Add metadata from a single tag. """
    def addMetadataFromTags(self, tags: Any, prefix: Any) -> None:
        """Add metadata from a list of tags. """
    def escape(self, value: Any) -> str:
        """Make sure metadata strings are properly escaped, following the kCharacterEscapeTable. """

class PostageStampNode(Node):
    def __init__(self) -> None: ...
    def getNodeSize(self) -> tuple[int, int]:
        """Get the size of the node.  This is an estimate, since in Nuke the size can be affected by
        the font size (and possibly other factors), but it works in most cases for layout of scripts. 
        """

class PrecompNode(Node):
    def __init__(self, filePath: Any, **knobs: Any) -> None: ...

class PushNode(Node):
    """Not really a node, this adds a push command to the script. """
    def __init__(self, var: Any) -> None: ...
    def isNode(self) -> bool: ...
    def serialize(self, serializer: Any) -> None: ...

class ReadNode(Node):
    def __init__(self, filePath: Any, width: Any = ..., height: Any = ..., pixelAspect: Any = ..., firstFrame: Any = ..., lastFrame: Any = ...) -> None: ...
    def getNodeSize(self) -> tuple[int, int]:
        """Get the size of the node.  This is an estimate, since in Nuke the size can be affected by
        the font size (and possibly other factors), but it works in most cases for layout of scripts. 
        """

class ReadNodeKnobFormatter:
    def serialize(self, serializer: Any, nodeType: Any, knobValues: Any, userKnobs: Any, rawKnobs: Any) -> None: ...

class ReformatNode(Node):
    kCompFormatAsPlate: str
    kCompReformatToFormat: str
    kCompReformatToSequence: str
    kCustomLabel: str
    kDisabled: str
    kResizeDistort: str
    kResizeFill: str
    kResizeFit: str
    kResizeHeight: str
    kResizeNone: str
    kResizeWidth: str
    kToBox: str
    kToFormat: str
    kToScale: str
    kToScaleLabel: str
    def __init__(self, resize: str = ..., center: bool = ..., flip: bool = ..., flop: bool = ..., turn: bool = ..., to_type: str = ..., format: Any = ..., scale: Any = ..., filter: Any = ..., box: Any = ..., pbb: bool = ..., black_outside: bool = ...) -> None:
        """Build a Nuke Reformat node.
        Set resize to one of kResizeNone, kResizeWidth, kResizeHeight, kResizeFit, kResizeFill, kResizeDistort.
        Set to_type to one of kCustom, kToScale, or kToBox.
        Supply the flag for center, defaults to True.
        Supply the flag for flip, defaults to False.
        Supply the flag for flop, defaults to False.
        Supply the flag for turn, defaults to False.
        Supply format in a tuple of (width, height, pixel aspect, name).
        Supply scale as a single floating point number.
        Supply box in a tuple of (width, height, pixel aspect).
        Note that this will always set "black outside".
        """

class RetimeNode(Node):
    def __init__(self, src_start: Any, src_end: Any, dst_start: Any, dst_end: Any, reverse: bool = ...) -> None:
        """Build a Nuke Retime node. Note that before/after are defaulted to "black" to
        mimic the way clips in Hiero are empty outside their defined range.
        """

class RootNode(Node):
    kTimelineWriteNodeKnobName: str
    def __init__(self, first_frame: Any, last_frame: Any, fps: Any = ..., showAnnotations: bool = ...) -> None: ...
    def addProjectSettings(self, projectSettings: Any) -> None:
        """Add knobs related to the color management options to the node. """
    def setViewsConfiguration(self, viewsColors: Any, heroView: Any = ..., showColors: Any = ...) -> None:
        """Set the view related knobs on the Root node """

class SetNode(Node):
    """Not really a node, this adds a set command to the script. """
    def __init__(self, var: Any, stack: Any) -> None: ...
    def isNode(self) -> bool: ...
    def serialize(self, serializer: Any) -> None: ...

class TimeClipNode(Node):
    """TimeClip node class. """
    def __init__(self, ifirst: Any, ilast: Any, origFirst: Any, origLast: Any, startTime: Any) -> None: ...
    def getNodeSize(self) -> tuple[int, int]:
        """Get the size of the node.  This is an estimate, since in Nuke the size can be affected by
        the font size (and possibly other factors), but it works in most cases for layout of scripts. 
        """

class TimeOffsetNode(Node):
    def __init__(self, offset: Any) -> None: ...

class UserDefinedNode(Node):
    """Node which can be used to insert node text into the script. """
    def __init__(self, data: Any) -> None: ...
    def getPosition(self) -> tuple[None, None] | tuple[Any, Any]:
        """Override.  The base class relies on the xpos and ypos knobs being inserted into the _knobValues dict.
        This class doesn't use that, so the position is stored separately.  Return it. 
        """
    def isNode(self) -> bool:
        """Assume that this actually is a node. """
    def serialize(self, serializer: Any) -> None: ...
    def setKnob(self, knobName: Any, knobValue: Any) -> None:
        """Set a knob value. """
    def setPosition(self, xpos: Any, ypos: Any) -> None:
        """Override.  This class does not use the Node knobs dictionary, since it just has raw tcl script
        which is inserted into the output.  This inserts xpos and ypos knob lines into the script. 
        """

class WriteNode(CompositeNode):
    def __init__(self, filePath: Any, inputNode: Any = ...) -> None: ...
    def getNodeSize(self) -> tuple[int, int]:
        """Get the size of the node.  This is an estimate, since in Nuke the size can be affected by
        the font size (and possibly other factors), but it works in most cases for layout of scripts. 
        """

class WriteNodeKnobFormatter:
    def serialize(self, serializer: Any, nodeType: Any, knobValues: Any, userKnobs: Any, rawKnobs: Any) -> None: ...

def RegisterCustomNukeKnobFormatter(nodeType: Any, nodeKnobFormatter: Any) -> None: ...

def appendMetadataNodesForPerFrameTagsToList(tags: Any, prefix: Any, addedNodes: Any, offset: Any = ..., inTime: Any = ..., outTime: Any = ...) -> None: ...

def fixPathForNuke(path: Any) -> Any:
    """Clean up a path to be used in a file knob. """

def tagAppliesToWhole(tag: Any) -> bool:
    """Return true if tag applies to whole sequence. """
