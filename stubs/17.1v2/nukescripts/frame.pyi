# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any

def goto_frame() -> None: ...

def replaceHashes(filename: Any) -> str:
    """replaceHashes(filename) -> string
    Replace any sequences of 1 or more hash marks (#) with a printf-style %0nd specifier.
    """
