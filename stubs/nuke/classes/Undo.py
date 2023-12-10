from typing import *
from numbers import Number

import nuke

from . import *


class Undo(object):
    """
    Undo
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def begin(self, *args, **kwargs) -> None:
        """
        Begin a new user-visible group of undo actions.
        """
        ...

    def name(self, *args, **kwargs) -> None:
        """
        Name current undo set.
        """
        ...

    def end(self, *args, **kwargs) -> None:
        """
        Complete current undo set and add it to the undo list.
        """
        ...

    def new(self, *args, **kwargs) -> None:
        """
        Same as end();begin().
        """
        ...

    def cancel(self, *args, **kwargs) -> None:
        """
        Undoes any actions recorded in the current set and throws it away.
        """
        ...

    def undoSize(self, *args, **kwargs) -> None:
        """
        Number of undo's that can be done.
        """
        ...

    def redoSize(self, *args, **kwargs) -> None:
        """
        Number of redo's that can be done.
        """
        ...

    def undoTruncate(self, *args, **kwargs) -> None:
        """
        Destroy any undo's greater or equal to n.
        """
        ...

    def redoTruncate(self, *args, **kwargs) -> None:
        """
        Destroy any redo's greater or equal to n.
        """
        ...

    def undoDescribe(self, *args, **kwargs) -> None:
        """
        Return short description of undo n.
        """
        ...

    def redoDescribe(self, *args, **kwargs) -> None:
        """
        Return short description of redo n.
        """
        ...

    def undoDescribeFully(self, *args, **kwargs) -> None:
        """
        Return long description of undo n.
        """
        ...

    def redoDescribeFully(self, *args, **kwargs) -> None:
        """
        Return long description of redo n.
        """
        ...

    def undo(self, *args, **kwargs) -> None:
        """
        Undoes 0'th undo.
        """
        ...

    def redo(self, *args, **kwargs) -> None:
        """
        Redoes 0'th redo.
        """
        ...

    def disable(self, *args, **kwargs) -> None:
        """
        Prevent recording undos until matching enable()
        """
        ...

    def enable(self, *args, **kwargs) -> None:
        """
        Undoes the previous disable()
        """
        ...

    def disabled(self, *args, **kwargs) -> None:
        """
        True if disable() has been called
        """
        ...

    def __enter__(self, *args, **kwargs) -> None:
        """

        """
        ...

    def __exit__(self, *args, **kwargs) -> None:
        """

        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
