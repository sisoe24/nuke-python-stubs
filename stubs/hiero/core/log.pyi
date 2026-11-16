# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any

kDebug: int
kError: int
kInfo: int

def debug(message: Any, *args: Any) -> None:
    """Log message at kDebug level. If the message is a string containing formatting placeholders, args will  be merged into it using the string formatting operator. 
    Otherwise the arguments will be concatenated into a string with spaces separating them.
    """

def error(message: Any, *args: Any) -> None:
    """Log message at kError level. If the message is a string containing formatting placeholders, args will  be merged into it using the string formatting operator. 
    Otherwise the arguments will be concatenated into a string with spaces separating them. 
    """

def exception(message: Any, *args: Any) -> None:
    """The same as error(), but also prints a stack trace.  Only call from an exception handler. """

def getFileLogger(name: Any) -> Any:
    """Get a logger which writes to a file in the user's NUKE_TEMP_DIR """

def info(message: Any, *args: Any) -> None:
    """Log message at kInfo level. If the message is a string containing formatting placeholders, args will  be merged into it using the string formatting operator. 
    Otherwise the arguments will be concatenated into a string with spaces separating them. 
    """

def logLevel() -> int:
    """Get the current log output level.  Possible values are: kDebug, kInfo, kError """

def setLogLevel(level: Any) -> None:
    """Set the logging output level.  Possible values are: kDebug, kInfo, kError """
