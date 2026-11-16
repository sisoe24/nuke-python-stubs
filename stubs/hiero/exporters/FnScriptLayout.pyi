# Type stubs for nuke 15.2v9. Generated; do not edit.

"""Code for layout of exported Nuke scripts."""

from typing import Any
import hiero as hiero

class LayoutBase:
    """Base class for layouts.  Each layout context should have an associated layout class with
    appropriate behaviour.  This base class contains helper functions and a default layout
    implementation, with some customisation through members set on the object. 
    """
    kAlignCenter: int
    kAlignLeft: int
    def __init__(self, script: Any, layoutContext: Any) -> None:
        """Initialise with a script writer and layout context.  Iterates over child contexts
        and creates sub-layouts. 
        """
    def alignmentForNodesLayout(self, left: Any) -> tuple[Any, int]:
        """Get the position and alignment flag for the horizontal positioning of
        nodes. By default aligns to the left border argument. 
        """
    def createBackdrop(self, color: Any, rect: Any, label: Any, zorder: Any) -> None:
        """Create a backdrop node, and add it to the script. """
    def doLayout(self, xpos: Any, ypos: Any, zorder: Any) -> Any:
        """Perform layout, and return the bounding rect.  This default implementation lays out child layouts horizontally,
        and then arranges nodes below them vertically. 
        """
    def getAlignHint(self) -> tuple[Any, Any] | tuple[int, int]:
        """Get x and y positions to align to.  If the layout has nodes, it will return the
        center of the last node, otherwise it will return the align hint of the last child layout. 
        """
    def getBackdropLabelHeight(self, label: Any, width: Any) -> Any:
        """Get the height of the backdrop label for the given width. """
    def getLayoutWidth(self) -> int:
        """Determine the width of the layout.  This can be done without actually determining the position
        of anything, and is required for determining the height of backdrop labels. 
        """
    def layoutChildContexts(self, layouts: Any, xpos: Any, ypos: Any, zorder: Any) -> Any:
        """Layout child contexts with the given orientation, starting from (xpos, ypos).  Returns the bounding rect. """
    def layoutNode(self, node: Any, xpos: Any, ypos: Any, alignment: Any, rect: Any) -> tuple[Any, Any]:
        """Layout nodes vertically, with the given alignment to the xpos.  Returns the bounding rect.  If the
        node has been set to align to another node, will attempt to align them horizontally. 
        """
    def layoutNodes(self, nodes: Any, xpos: Any, ypos: Any, alignment: Any) -> Any:
        """Layout child nodes with the given alignment to the xpos.  Returns the bounding rect."""

class ClipLayout(LayoutBase):
    """Clip layout. """
    def __init__(self, script: Any, layoutContext: Any) -> None: ...
    def doLayout(self, xpos: Any, ypos: Any, zorder: Any) -> Any:
        """Perform layout, and return the bounding rect.  Lays out nodes in two columns, with constant nodes
        (for gaps in the timeline) on the left. 
        """
    def getLayoutWidth(self) -> int: ...

class TrackLayout(LayoutBase):
    """Track level layout. """
    def __init__(self, script: Any, layoutContext: Any) -> None: ...
    def doLayout(self, xpos: Any, ypos: Any, zorder: Any) -> Any:
        """Do the track layout.  Reimplemented as the node layout is a bit different to the default. """
    def getTrackName(self) -> Any: ...
    def getVerticalLayoutAlignHint(self) -> tuple[Any, Any] | tuple[int, int]: ...
    def layoutHorizontal(self, xpos: Any, ypos: Any, zorder: Any) -> Any: ...
    def layoutVertical(self, xpos: Any, ypos: Any, zorder: Any) -> Any: ...
    def setMerge(self, merge: Any) -> None: ...
    def subTrackItemsOnly(self) -> bool:
        """Get if the track being laid out only has sub-track items (i.e. effects and annotations) on it. """

class EffectsTrackLayout(TrackLayout):
    """Layout for the effects track and associated nodes. """
    def __init__(self, script: Any, layoutContext: Any) -> None: ...
    def getVerticallayoutAlignHint(self) -> tuple[Any, Any] | tuple[int, int]: ...
    def layoutHorizontal(self, xpos: Any, ypos: Any, zorder: Any) -> Any: ...
    def layoutNodes(self, nodes: Any, xpos: Any, ypos: Any, alignment: Any) -> Any: ...
    def layoutVertical(self, xpos: Any, ypos: Any, zorder: Any) -> Any: ...
    def subTrackItemsOnly(self) -> bool:
        """Merge layouts should act like layouts that only contain sub-track items, with layout vertically
        below the output track. 
        """

class MainLayout(LayoutBase):
    """Main layout, which arranges the clip/sequence and the write nodes with a gap in between. """
    kWriteLayoutSpacing: int
    def __init__(self, script: Any, layoutContext: Any) -> None: ...
    def doLayout(self, xpos: Any, ypos: Any, zorder: Any) -> Any: ...

class MergeLayout(LayoutBase):
    """Layout for the merge and associated nodes. """
    def __init__(self, script: Any, layoutContext: Any) -> None: ...
    def getAlignHint(self) -> tuple[Any, Any] | tuple[int, int]:
        """Get x and y positions to align to.  Aligns to the actual merge node and not any dot nodes which
        happen to be in the layout.
        """
    def getInputA(self) -> Any: ...
    def getMainInputTrack(self) -> Any: ...
    def layoutNodes(self, nodes: Any, xpos: Any, ypos: Any, alignment: Any) -> Any: ...
    def subTrackItemsOnly(self) -> bool:
        """Merge layouts should act like layouts that only contain sub-track items, with layout vertically
        below the output track. 
        """

class SequenceLayout(LayoutBase):
    def __init__(self, script: Any, layoutContext: Any) -> None: ...
    def alignmentForNodesLayout(self, left: Any) -> tuple[Any, int]:
        """Override. Align to the last child layout. """

class TracksLayout(LayoutBase):
    """Class for laying out a list of tracks. This is currently just used for the ViewLayout """
    def __init__(self, script: Any, layoutContext: Any) -> None: ...
    def doLayout(self, xpos: Any, ypos: Any, zorder: Any) -> Any:
        """Layout the sequence.  Lays out tracks horizontally, except tracks that only have soft effects or annotations, which
        are laid out vertically underneath. 
        """
    def getAlignHint(self) -> tuple[Any, Any] | tuple[int, int]: ...
    def getLayoutWidth(self) -> int:
        """Determine the width of the layout.  This can be done without actually determining the position
        of anything, and is required for determining the height of backdrop labels. 
        """

class ViewLayout(TracksLayout):
    """Used for laying out the views for a sequence separately. """
    def __init__(self, script: Any, layoutContext: Any) -> None: ...

class WriteLayout(TrackLayout):
    """Layout for the write and associated nodes. """
    def __init__(self, script: Any, layoutContext: Any) -> None: ...
    def layoutNodes(self, nodes: Any, xpos: Any, ypos: Any, alignment: Any) -> Any: ...
    def layoutWriteNodes(self, writeNode: Any, xpos: Any, ypos: Any, alignment: Any, rect: Any) -> tuple[Any, Any]: ...

def scriptLayout(script: Any) -> None:
    """Layout a script. """
