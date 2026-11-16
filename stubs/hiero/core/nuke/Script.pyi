# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from hiero.core import util as util
from hiero.core.util import asUnicode as asUnicode
import hiero as hiero

FAST_TRANSCODES: int
RESPONSIVE_UI: int
USER_CONFIGURATION: int

class NodeLayoutContext:
    """Class to assist with grouping nodes for layout purposes.
    May have nested child contexts and a list of nodes.
    Each context is initialised with a type, which can be used to decide the layout strategy,
    a name, which is used for to uniquely identify the context and for labelling purposes (unless a separate label is given,
    and arbitrary other data which can be used for determining the layout. 
    """
    def __init__(self, type: str = ..., name: str = ..., **data: Any) -> None: ...
    def addChild(self, child: Any) -> None:
        """Add a child context. """
    def addNode(self, node: Any) -> None:
        """Add a node or a sequence of nodes. """
    def getChildren(self) -> list[Any]:
        """Get the list of child contexts. """
    def getData(self, key: Any) -> None:
        """Try to retrieve extra data given to the context.  Returns the data, or None
        if it was not set. 
        """
    def getLabel(self) -> str:
        """Get the context label.  Returns the 'label' data if it was given, otherwise the name. """
    def getName(self) -> str:
        """Get the context name. """
    def getNodes(self) -> list[Any]:
        """Get the nodes added to this context. """
    def getType(self) -> str:
        """Get the context type. """

class ScriptWriter:
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def addNode(self, node: Any) -> None: ...
    def beginSerializeNode(self, nodeType: Any) -> None: ...
    def endSerializeNode(self) -> None: ...
    def getMainLayoutContext(self) -> Any:
        """Get the main layout context for the script. """
    def getNodes(self) -> list[Any]: ...
    def popLayoutContext(self) -> None:
        """Pop the current layout context from the stack. """
    def pushLayoutContext(self, type: Any, name: Any, **data: Any) -> None:
        """Push a layout context to the stack.  Any nodes added to the script will be included in the new
        layout context.  If the current context already has a child with the same type and name, that
        will be used instead of creating a new one. 
        """
    def serializeKnob(self, knobType: Any, knobValue: Any) -> None: ...
    def serializeKnobs(self, knobValues: Any) -> None: ...
    def serializeNode(self, nodeType: Any, knobValues: Any, userKnobs: Any, rawKnobs: Any) -> None: ...
    def serializeRawKnobs(self, rawKnobs: Any) -> None: ...
    def serializeUserKnob(self, type: Any, knobName: Any, text: Any, tooltip: Any, value: Any, visible: Any) -> None: ...
    def serializeUserKnobs(self, userKnobs: Any) -> None: ...
    def writeToDisk(self, scriptFilename: Any) -> None: ...

def executeNukeScript(path: Any, logfile: Any, executeOnSingleSocket: bool = ...) -> Any: ...

def getBundledNukePath() -> Any:
    """hiero.core.getBundledNukePath() -> return the bundled Nuke executable

    @return: A string containing the bundled Nuke executable path.
    """

def getBundledPythonPath() -> str:
    """hiero.core.getBundledPythonPath() -> return the bundled Python executable

    @return: A string containing the bundled Python executable path.
    """

def getInteractiveNukeExecutablePath() -> str: ...

def getRenderOnlyNukeExecutablePath() -> str: ...

def hieroNukePath() -> Any:
    """hiero.core.hieroNukePath() -> returns the HieroNuke executable path which ships with Hiero. DEPRECATED Use getBundledNukePath() instead.

    @return: A string containing the HieroNuke executable path.
    """

def launchNuke(path: Any = ..., *extraArgs: Any) -> Any:
    """Launches a Nuke edition subprocess of this executable, optionally with a Nuke Script specified by 'path'.

    Extra arguments may also be used by specifying a tuple/list of arguments in 'extraArgs'.

    launchNuke automatically checks your Preference for 'Open In > New Nuke Session launches Nuke X', and also adds a '-q' switch, to stop the Nuke splash screen from appearing.

    @param path - (optional) path to a Nuke Script (.nk) file to open.
    @param extraArgs - (optional) list/tuple of additional command line arguments.

    @return the subprocess.Popen object for the Nuke instance launched
    """

def nukeThreadsMemoryPreferences() -> tuple[int, int]:
    """Get the number of threads and memory in MB to be used for Nuke render processes from the application preferences. """

def openNukeProcess(*args: Any, **kwargs: Any) -> Any:
    """Helper function wrap around a Popen call to run Nuke.  On Macs, there
    seems to be a possibility of some output to stderr between the fork and
    exec calls, which results in an error in CoreFoundation because it's attempting
    to redirect the output to the script editor.  Temporarily reset stdout/err
    while calling Popen.
    """

def useBundledNuke() -> bool: ...

def useNukeXForInteractive() -> bool: ...
