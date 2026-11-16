# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import nukescripts.pyAppUtils as _nukescripts_pyAppUtils
from nukescripts import pyAppUtils as pyAppUtils

class pyWxAppHelper(_nukescripts_pyAppUtils.pyAppHelper):
    """Helper class to initialise wxWidgets in a separate thread """
    def __init__(self, wxApp: Any, start: Any = ...) -> None: ...
    def getApplication(self) -> Any: ...
    def start(self) -> None: ...
