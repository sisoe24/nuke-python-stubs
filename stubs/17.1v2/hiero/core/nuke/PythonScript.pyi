# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import hiero.core.nuke.Script as _hiero_core_nuke_Script
from hiero.core import util as util
from hiero.core.nuke.Script import NodeLayoutContext as NodeLayoutContext
from hiero.core.nuke.Script import ScriptWriter as ScriptWriter
from hiero.core.nuke.Script import executeNukeScript as executeNukeScript
from hiero.core.nuke.Script import getBundledNukePath as getBundledNukePath
from hiero.core.nuke.Script import getBundledPythonPath as getBundledPythonPath
from hiero.core.nuke.Script import getInteractiveNukeExecutablePath as getInteractiveNukeExecutablePath
from hiero.core.nuke.Script import getRenderOnlyNukeExecutablePath as getRenderOnlyNukeExecutablePath
from hiero.core.nuke.Script import hieroNukePath as hieroNukePath
from hiero.core.nuke.Script import launchNuke as launchNuke
from hiero.core.nuke.Script import nukeThreadsMemoryPreferences as nukeThreadsMemoryPreferences
from hiero.core.nuke.Script import openNukeProcess as openNukeProcess
from hiero.core.nuke.Script import useBundledNuke as useBundledNuke
from hiero.core.nuke.Script import useNukeXForInteractive as useNukeXForInteractive
from hiero.core.util import asUnicode as asUnicode
import hiero as hiero

FAST_TRANSCODES: int
RESPONSIVE_UI: int
USER_CONFIGURATION: int

class PythonScriptWriter(_hiero_core_nuke_Script.ScriptWriter):
    def __init__(self, autoConnectNodes: bool = ..., autoPosition: bool = ...) -> None: ...
    def __repr__(self) -> str: ...
    def beginSerializeNode(self, nodeType: Any) -> None: ...
    def endSerializeNode(self) -> None: ...
    def serializeKnob(self, knobType: Any, knobValue: Any) -> None: ...
    def serializeUserKnob(self, type: Any, knobName: Any, text: Any, tooltip: Any, value: Any) -> Any: ...
