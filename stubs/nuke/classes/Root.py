from typing import *
from numbers import Number

import nuke

from . import *


class Root(Group):
    """

    """

    def __repr__(self, ) -> None:
        """
        Return repr(self).
        """
        ...

    def __str__(self, ) -> None:
        """
        Return str(self).
        """
        ...

    def __len__(self, ) -> None:
        """
        Return len(self).
        """
        ...

    def __getitem__(self, key, ) -> None:
        """
        Return self[key].
        """
        ...

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def clones(self,) -> Number:
        """
        self.clones() -> Number of clones.
        @return: Number of clones.
        """
        ...

    def inputs(self,) -> int:
        """
        self.inputs() -> Gets the maximum number of connected inputs.
        @return: Number of the highest connected input + 1. If inputs 0, 1, and 3 are connected, this will return 4.
        """
        ...

    def input(self, i: Number) -> int:
        """
        self.input(i) -> The i'th input.
        @param i: Input number.
        @return: The i'th input.
        """
        ...

    def setInput(self, i: Number, node: Node) -> bool:
        """
        self.setInput(i, node) -> bool
        Connect input i to node if canSetInput() returns true.
        @param i: Input number.
        @param node: The node to connect to input i.
        @return: True if canSetInput() returns true, or if the input is already correct.
        """
        ...

    def optionalInput(self,) -> Number:
        """
        self.optionalInput() -> Number of first optional input.
        @return: Number of first optional input.
        """
        ...

    def minimumInputs(self,) -> Number:
        """
        self.minimumInputs() -> Minimum number of inputs this node can have.
        @return: Minimum number of inputs this node can have.
        """
        ...

    def maximumInputs(self,) -> Number:
        """
        self.maximumInputs() -> Maximum number of inputs this node can have.
        @return: Maximum number of inputs this node can have.
        """
        ...

    def maximumOutputs(self,) -> Number:
        """
        self.maximumOutputs() -> Maximum number of outputs this node can have.
        @return: Maximum number of outputs this node can have.
        """
        ...

    def connectInput(self, i: Number, node: Node) -> bool:
        """
        self.connectInput(i, node) -> bool
        Connect the output of 'node' to the i'th input or the next available unconnected input. The requested input is tried first, but if it is already set then subsequent inputs are tried until an unconnected one is found, as when you drop a connection arrow onto a node in the GUI.
        @param i: Input number to try first.
        @param node: The node to connect to input i.
        @return: True if a connection is made, False otherwise.
        """
        ...

    def canSetInput(self, i: Number, node: Node) -> bool:
        """
        self.canSetInput(i, node) -> bool
        Check whether the output of 'node' can be connected to input i.
        @param i: Input number.
        @param node: The node to be connected to input i.
        @return: True if node can be connected, False otherwise.
        """
        ...

    def modified(self,) -> bool:
        """
        self.modified() -> True if modified, False otherwise.
        Get or set the 'modified' flag in a script
        @return: True if modified, False otherwise.
        """
        ...

    def setModified(self, b: bool) -> None:
        """
        self.setModified(b) -> None.
        Set the 'modified' flag in a script.
        Setting the value will turn the indicator in the title bar on/off and will start or stop the autosave timeout.
        @param b: Boolean convertible object.
        @return: None.
        """
        ...

    def proxy(self,) -> bool:
        """
        self.proxy() -> True if proxy is set, False otherwise.
        @return: True if proxy is set, False otherwise.
        """
        ...

    def setProxy(self, b: bool) -> None:
        """
        self.setProxy(b) -> None.
        Set proxy.
        @param b: Boolean convertible object.
        @return: None.
        """
        ...

    def firstFrame(self,) -> int:
        """
        self.firstFrame() -> Integer.
        First frame.
        @return: Integer.
        """
        ...

    def lastFrame(self,) -> int:
        """
        self.lastFrame() -> Integer.
        Last frame.
        @return: Integer.
        """
        ...

    def fps(self,) -> int:
        """
        self.fps() -> integer
        Return the FPS rounded to an int. This is deprecated. Please use real_fps().
        """
        ...

    def realFps(self,) -> float:
        """
        self.realFps() -> float
        The global frames per second setting.
        """
        ...

    def mergeFrameRange(self, a: Number, b: Number) -> None:
        """
        self.mergeFrameRange(a, b) -> None.
        Merge frame range.
        @param a: Low-end of interval range.
        @param b: High-end of interval range.
        @return: None.
        """
        ...

    def addView(self, name: str, color: Optional[list] = None) -> None:
        """
        self.addView(name, color) -> None.
        Add view.
        @param name: String - name of view.
        @param color: Optional. String in the format #RGB, #RRGGBB, #RRRGGGBBB, #RRRRGGGGBBBB or a name from the list of colors defined in the list of SVG color keyword names.
        @return: None.
        """
        ...

    def deleteView(self, s: str) -> None:
        """
        self.deleteView(s) -> None.
        Delete view.
        @param s: Name of view.
        @return: None.
        """
        ...

    def setFrame(self, n: int) -> None:
        """
        self.setFrame(n) -> None.
        Set frame.
        @param n: Frame number.
        @return: None.
        """
        ...

    def setView(self, s: str) -> None:
        """
        self.setView(s) -> None.
        Set view.
        @param s: Name of view.
        @return: None.
        """
        ...

    def layers(self,) -> list:
        """
        nuke.Root.layers() -> Layer list.
        Class method.
        @return: Layer list.
        """
        ...

    def channels(self,) -> list:
        """
        nuke.Root.channels() -> Channel list.
        Class method.
        @return: Channel list.
        """
        ...

    def getOCIOColorspaceFromViewTransform(self, display: str, view: str) -> str:
        """
        nuke.root.getOCIOColorspaceFromViewTransform(display, view) -> Colorspace name
        Gets the name of the colorspace to which the specified display and view names are mapped
        for the root node's current OCIO config.
        @param display: Display name.
        @param view: View name.
        @return: The corresponding colorspace name.
        """
        ...

    def getOCIOColorspaceFamily(self, colorspace: str) -> str:
        """
        nuke.root.getOCIOColorspaceFamily(colorspace) -> Family of colorspace
        Gets the name of the family to which the specified colorspace belongs,
        for the root node's current OCIO config.
        @param colorspace: Colorspace name.
        @return: Family name, may be an empty string.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
