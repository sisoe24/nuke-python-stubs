# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
from nukescripts.run_framecycler import framecycler_this as framecycler_this

prev_inrange: str
prev_userrange: str

def flipbook(command: Any, node: Any, framesAndViews: Any = ...) -> Any:
    """Runs an arbitrary command on the images output by a node. This checks
    to see if the node is a Read or Write and calls the function directly
    otherwise it creates a temporary Write, executes it, and then calls
    the command on that temporary Write, then deletes it.

    By writing your own function you can use this to launch your own
    flipbook or video-output programs.

    Specify framesAndViews as a tuple if desired, like so: ("1,5", ["main"])
    This can be useful when running without a GUI.
    """
