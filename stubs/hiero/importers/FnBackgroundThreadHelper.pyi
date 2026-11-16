# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any

class BackgroundFuncCallRunnable:
    """Helper class for executing function in a thread belonging to a QThreadPool.
    Emits the _finished signal when the executions is completed. 
    """
    staticMetaObject: Any
    def __init__(self, func: Any, args: Any) -> None: ...
    def run(self) -> None: ...

def runFunctionInBackgroundThread(func: Any, *args: Any) -> None:
    """Execute the function with the given args in one of the threads owned by QThreadPool.globalInstance() but
    block until completed and return the result. The blocking is done in such a way that it 
    allows the Qt event loop to run i.e. ensuring that the UI is responsive if called from the main thread. 
    If an exception is thrown when running the function, it will be raised after the function is executed
    """
