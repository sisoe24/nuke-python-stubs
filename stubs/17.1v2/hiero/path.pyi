# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
from typing import Generator
import hiero as hiero

def abspath(path: Any) -> str:
    """Return an absolute path."""

def basename(p: Any) -> Any:
    """Returns the final component of a pathname"""

def cd(path: Any) -> None: ...

def dirname(p: Any) -> Any:
    """Returns the directory component of a pathname"""

def glob(path: Any) -> list[Any]:
    """Returns a list of all items matching the given path, where the path may contain * and ? wildcards.
    
    """

def iglob(path: Any, parent: Any = ...) -> Generator[Any, Any, None]:
    """Returns a iterator of all items matching the given path, where the path may contain * and ? wildcards.
    
    """

def isabs(s: Any) -> Any: ...

def itemForPath(path: Any) -> None:
    """Returns the item corresponding to the given path, or None if no item exists at the path.
    
    """

def join(a: Any, *p: Any) -> Any: ...

def ls(path: str = ...) -> None: ...

def normpath(path: Any) -> str: ...

def pathForItem(item: Any) -> str:
    """Returns the path corresponding to the given item.
    
    """

def pwd() -> None: ...

def split(p: Any) -> tuple[Any, Any]: ...
