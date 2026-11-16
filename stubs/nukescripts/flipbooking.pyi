# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any

gFlipbookFactory: FlipbookFactory
gFlipbookLUTPathRegistry: FlipbookLUTPathRegistry

class FlipbookApplication:
    """An interface, for so far as Python supports it. To add support for a
    flipbook this needs to be subclassed and the 3 methods implemented. The
    default  implementation just raises an exception so any sub implementer
    will soon find out whether his implementation works.
    """
    def __init__(self) -> None: ...
    def cacheDir(self) -> str:
        """Return the preferred directory for rendering.
        @return: String
        """
    def capabilities(self) -> Any:
        """Return the capabilities of the flipbook application in a dict. Currently used are:
        canPreLaunch: bool, whether the flipbook can display a frames that are still being rendered by Nuke.
        maximumViews: int, the number of views supported by this flipbook, should be 1 or higher.
        fileTypes: list, the extensions of the file types supported by this format. Must all be lowercase, e.g ["exr", "jpg", ...].
                   A wildcard ["*"] can also be used to indicate support for any file type Nuke supports
        "roi: bool, whether the flipbook supports region-of-interest
        @return: dict with the capabilities above.
        """
    def dialogKnobChanged(self, dialog: Any, knob: Any) -> None:
        """Called whenever this flipbook is selected and one of the knobs added in dialogKnobs was changed.
        @param dialog: The FlipbookDialog that contains the knob
        @param knob: The knob added in dialogKnobs that was modified.
        @return: None
        """
    def dialogKnobs(self, dialog: Any) -> None:
        """This is called when the user has selected this flipbook application, and will be interested in any knobs that you might have to show for custom settings.
        @param dialog: The FlipbookDialog that has requested the knobs to be added to it, e.g. dialog.addKnob(...)
        @return: None
        """
    def getExtraOptions(self, flipbookDialog: Any, nodeToFlipbook: Any) -> dict[Any, Any]:
        """Called whenever this flipbook is selected to retrieve extra options from the node selected to flipbook
        and the flipbook dialog.
        @param flipbookDialog: the flipbook dialog
        @param nodeToFlipbook: node selected to flipbook
        @return: a dictionary with the extra options 
        """
    def name(self) -> str:
        """Return the name of the flipbook.
        @return: String
        """
    def path(self) -> str:
        """Return the executable path required to run a flipbook.
        @return: String
        """
    def run(self, path: Any, frameRanges: Any, views: Any, options: Any) -> None:
        """Execute the flipbook on a path.
        @param path: The path to run the flipbook on. This will be similar to /path/to/foo%03d.exr
        @param frameRanges: A FrameRanges object representing the range that should be flipbooked. Note that in 6.2v1-2 this was a FrameRange object.
        @param views: A list of strings comprising of the views to flipbook. Willnot be more than the maximum supported by the flipbook.
        @param options: A dictionary of options to use. This may contain the keys pixelAspect, roi, dimensions, audio and lut. These contain a float, a dict with bounding box dimensions, a dict with width and height, a path to audio file and a string indicating the LUT conversion to apply.
        @return: None
        """
    def runFromNode(self, nodeToFlipbook: Any, frameRanges: Any, views: Any, options: Any) -> None:
        """Execute the flipbook on a node.
        This method will use the node's filename to call run()
        @param node: The node to run the flipbook
        @param frameRanges: A FrameRanges object representing the range that should be flipbooked. Note that in 6.2v1-2 this was a FrameRange object.
        @param views: A list of strings comprising of the views to flipbook. Willnot be more than the maximum supported by the flipbook.
        @param options: A dictionary of options to use. This may contain the keys pixelAspect, roi, dimensions, audio and lut. These contain a float, a dict with bounding box dimensions, a dict with width and height, a path to audio file and a string indicating the LUT conversion to apply.
        @return: None
        """

class FlipbookFactory:
    def __init__(self) -> None: ...
    def getApplication(self, name: Any) -> Any:
        """Returns the flipbook app implementation with the given name, raises an exception if none could be found.
        @param name: The name of a flipbook that was registered.
        @return: FlipBookApplication
        """
    def getNames(self) -> list:
        """Returns a list of the names of all available flipbook apps.
        @return: list
        """
    def isRegistered(self, flipbook: Any) -> bool:
        """Return whether a flipbook app with that name has already been registered.
        @param flipbook: FlipBookApplication object that's tested for.
        @return: bool
        """
    def register(self, flipbookApplication: Any) -> None:
        """Register a flipbook app. It will fail if the flipbook app name isn't unique.
        @param flipbook: FlipBookApplication object to register
        @return: None
        """

class FlipbookLUTPathRegistry:
    """A registery of all LUT files against LUTs for each specific flipbook."""
    def __init__(self) -> None: ...
    def getLUTPathForFlipbook(self, flipbook: Any, lut: Any) -> Any:
        """Return the path for the given flipbook and lut. May return an empty string if none registered.
        @param flipbook: The unique name of the flipbook
        @param lut: The unique name for the LUT, e.g. 'sRGB' and 'rec709'
        """
    def registerLUTPathForFlipbook(self, flipbook: Any, lut: Any, path: Any) -> None:
        """Register the given LUT file.
        @param flipbook: The unique name of the flipbook
        @param lut: The unique name for the LUT, e.g. 'sRGB' and 'rec709'
        @param path: Location of the flipbook specific file.
        """

def getLUTPath(flipbookAppliction: Any, lut: Any) -> Any:
    """Returns a path to a LUT file for the given flipbook. The contents of the file will be different for each flipbook application. Please see the relevant documentation for the specific flipbook applications.
    @param flipbook: The unique name of the flipbook
    @param lut: The unique name for the LUT, e.g. 'sRGB' and 'rec709'
    """

def register(flipbookApplication: Any) -> None:
    """Register a flipbook. Convenience function that simple calls register() on the FlipbookFactory."""

def registerLUTPath(flipbookApplication: Any, lut: Any, path: Any) -> None:
    """Register a LUT for a specific flipbook. The path should refer to a file that contains the LUT for the given flipbook identified by the name in flipbookApplication. It is up to the flipbook subimplementation to actually use this file and the format may vary.
    @param flipbook: The unique name of the flipbook
    @param lut: The unique name for the LUT, e.g. 'sRGB' and 'rec709'
    @param path: Location of the flipbook specific file.
    """
