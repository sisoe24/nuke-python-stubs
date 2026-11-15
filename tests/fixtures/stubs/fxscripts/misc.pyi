# Type stubs for fxhost 1.0v1. Generated; do not edit.

"""Pure-Python host scripts: real bodies, few annotations."""

from typing import Any
from typing_extensions import Self
import fxhost as fxhost

class Panel:
    """A panel with every member kind."""
    class Options:
        compact: bool
    closed: Any
    title: str
    width: int
    def __init__(self, name: Any, parent: Any = ...) -> None: ...
    @classmethod
    def create(cls, name: Any) -> Self: ...
    @staticmethod
    def default_size() -> tuple[int, int]: ...
    @property
    def name(self) -> str:
        """The panel name."""
    def on_close(self) -> Any:
        """Called when the panel closes. Subclasses return False to veto."""
    def show(self, modal: bool = ...) -> bool: ...
    @property
    def size(self) -> Any: ...
    @size.setter
    def size(self, value: Any) -> None: ...

def find_panel(name: Any) -> Panel | None: ...

def make_node() -> Any: ...

def node_names(nodes: Any = ..., upper: bool = ..., prefix: str = ...) -> list[Any]: ...

def script_directory(path: str | None = ...) -> str: ...

select = node_names
