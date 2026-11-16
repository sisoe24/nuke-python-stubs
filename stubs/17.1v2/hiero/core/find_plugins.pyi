# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
from hiero.core.log import exception as exception
from hiero.core.log import info as info
import hiero as hiero
import nuke_internal as nuke_internal

verbosePlugins: bool

def findExportPresets() -> None: ...

def findExporters() -> None: ...

def findPlugins() -> None: ...

def launchedInSafeMode() -> bool:
    """Returns whether Hiero was launched in Safe mode (--safe) on the command line"""

def listPlugins() -> None: ...

def loadPluginsFromFolder(path: Any) -> None: ...

def loadPluginsFromPluginPath(suffix: Any) -> None: ...
