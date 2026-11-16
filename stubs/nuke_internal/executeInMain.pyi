# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any

def executeInMainThread(call: Any, args: Any = ..., kwargs: Any = ...) -> None:
    """Execute the callable 'call' with optional arguments 'args' and named
    arguments 'kwargs' i n Nuke's main thread and return immediately. 
    """

def executeInMainThreadWithResult(call: Any, args: Any = ..., kwargs: Any = ...) -> None:
    """Execute the callable 'call' with optional arguments 'args' and named arguments 'kwargs' in
    Nuke's main thread and wait for the result to become available. 
    """
