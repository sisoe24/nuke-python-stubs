# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from typing_extensions import Self

class FnPySingleton:
    def __new__(type, *args: Any, **kwargs: Any) -> Self: ...

def loadModuleFromPath(name: Any, path: Any) -> Any:
    """Load a Python file and return the module object """

def script_directory() -> str: ...
