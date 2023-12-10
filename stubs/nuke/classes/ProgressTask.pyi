from typing import *
from numbers import Number

import nuke

from . import *

class ProgressTask(object):
    """
    ProgressTask
    """
    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def __new__(self,*args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def setProgress(self,i) -> None:
        """
        self.setProgress(i) -> None.

        i is an integer representing the current progress
        """
        ...

    def setMessage(self,s) -> None:
        """
        self.setMessage(s) -> None.

        set the message for the progress task
        """
        ...

    def isCancelled(self,) -> bool:
        """
        self.isCancelled() -> True if the user has requested the task to be cancelled.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
