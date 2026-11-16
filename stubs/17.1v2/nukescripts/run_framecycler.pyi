# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any

fc_path: str
fc_suffix: str

def framecycler_linux_version() -> str: ...

def framecycler_sequence(frange: Any, filename: Any, cmd_args_size: Any) -> list[Any]: ...

def framecycler_stereo_available() -> bool:
    """This function used to detect if we were running on Mac OS Tiger; we no longer support Tiger, so this function always returns true now."""

def framecycler_this(node: Any, start: Any, end: Any, incr: Any, view: Any) -> None:
    """Run framecycler on a Read or Write node. See the flipbook command
    for how we run framecycler on *any* node.
    """

def run_app(app: Any, in_args: Any) -> bytes | str: ...
