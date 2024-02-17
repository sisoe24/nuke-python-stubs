"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

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

    def begin(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Begin a new user-visible group of undo actions.
        """
        ...

    def name(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Name current undo set.
        """
        ...

    def end(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Complete current undo set and add it to the undo list.
        """
        ...

    def new(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Same as end();begin().
        """
        ...

    def cancel(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Undoes any actions recorded in the current set and throws it away.
        """
        ...

    def undoSize(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Number of undo's that can be done.
        """
        ...

    def redoSize(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Number of redo's that can be done.
        """
        ...

    def undoTruncate(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Destroy any undo's greater or equal to n.
        """
        ...

    def redoTruncate(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Destroy any redo's greater or equal to n.
        """
        ...

    def undoDescribe(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return short description of undo n.
        """
        ...

    def redoDescribe(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return short description of redo n.
        """
        ...

    def undoDescribeFully(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return long description of undo n.
        """
        ...

    def redoDescribeFully(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Return long description of redo n.
        """
        ...

    def undo(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Undoes 0'th undo.
        """
        ...

    def redo(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Redoes 0'th redo.
        """
        ...

    def disable(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Prevent recording undos until matching enable()
        """
        ...

    def enable(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        Undoes the previous disable()
        """
        ...

    def disabled(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """
        True if disable() has been called
        """
        ...

    def __enter__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def __exit__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        """

        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
