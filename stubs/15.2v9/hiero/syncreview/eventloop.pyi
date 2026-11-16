# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from hiero.syncreview import log as log

class EventLoop:
    """Wrapper around ayncio IOLoop, with some helpers for integrating it into the application. """
    def __init__(self) -> None: ...
    def callInThread(self, callback: Any, *args: Any) -> None:
        """Add a callback in the thread the event loop is running in.
        Can only be called once the event loop is running.
        """
    def exit(self) -> None:
        """Exit the event loop. """
    def start(self) -> None:
        """Start the event loop. Should be run in a thread. """
    def waitForStart(self) -> None:
        """Wait for the loop to start in another thread. """

class Timer:
    """Timer class for use with EventLoop. Somewhat mimics the QTimer interface. """
    def __init__(self) -> None: ...
    def setCallback(self, callback: Any) -> None:
        """Set the callback when the timer fires. """
    def setInterval(self, interval: Any) -> None:
        """Set the timer interval, as a datetime.timedelta """
    def setSingleShot(self, singleShot: Any) -> None:
        """Set whether the timer should only fire once. """
    def start(self) -> None:
        """Start or restart the timer. """
    def stop(self) -> None:
        """Stop the timer if it was running. """
