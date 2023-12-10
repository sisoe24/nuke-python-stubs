from typing import *
from numbers import Number

import nuke

from . import *

class ViewerProcess(object):
    """
    ViewerProcess
    """
    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def register(self, name:str, call:Callable, args, kwargs=None) -> None:
        """
        nuke.ViewerProcess.register(name, call, args, kwargs) -> None.

        Register a ViewerProcess. This is a class method.

        :param name: Menu name.
        :param call: Python callable. Must return a Node.
        :param args: Arguments to call.
        :param kwargs: Optional named arguments.
        :return: None.
        """
        ...

    def unregister(self, name:str) -> None:
        """
        nuke.ViewerProcess.unregister(name) -> None.

        Unregister a ViewerProcess. This is a class method.

        :param name: Menu name.
        :return: None.
        """
        ...

    def node(self, name:Optional[str] = None, viewer:Optional[str] = None) -> Node:
        """
        nuke.ViewerProcess.node(name, viewer) -> Node.

        Returns a ViewerProcess node. Default is to return the current selected one. This is a class method.

        :param name: Optional ViewerProcess name.
        :param viewer: Optional viewer name.
        :return: Node.
        """
        ...

    def registeredNames(self,) -> list:
        """
        nuke.ViewerProcess.registeredNames() -> List.

        Returns a list containing the names of all currently regisered ViewerProcesses.

        :return: List.
        """
        ...

    def storeSelectionBeforeReload(self,) -> None:
        """
        nuke.ViewerProcess.storeSelectionBeforeReload() -> None.

        When the user reloads an OCIO or Nuke config the viewer process selection is stored in the the viewer process object
        Following the reload you can call nuke.ViewerProcess.restoreSelectionAfterReload() which will then restore the selection instead of the default.

        :return: None.
        """
        ...

    def restoreSelectionAfterReload(self,) -> None:
        """
        nuke.ViewerProcess.restoreSelectionAfterReload() -> None.

        Restores the viewer process selection after an OCIO or Nuke Config has been reloaded
        this is normally called after nuke.ViewerProcess.storeSelectionBeforeReload()

        :return: None.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
