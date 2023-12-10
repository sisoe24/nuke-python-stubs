from typing import *
from numbers import Number

import nuke

from . import *

class MenuItem(object):
    """
    MenuItem
    """
    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def setEnabled(self, enabled:bool, recursive:bool) -> None:
        """
        self.setEnabled(enabled, recursive) -> None
        Enable or disable the item.
        @param enabled: True to enable the object; False to disable it.
        @param recursive: True to also setEnabled on submenu actions.
        """
        ...

    def setVisible(self, visible:bool) -> None:
        """
        self.setVisible(visible) -> None
        Show or hide the item.
        @param visible: True to show the object; False to hide it.
        """
        ...

    def invoke(self,) -> None:
        """
        self.invoke() -> None
        Perform the action associated with this menu item.
        """
        ...

    def action(self,) -> None:
        """
        self.action() -> None
        Get the action associated with this menu item.
        """
        ...

    def name(self,) -> str:
        """
        self.name() -> String
        Returns the name of the menu item.
        """
        ...

    def icon(self,) -> str:
        """
        self.icon() -> String
        Returns the name of the icon on this menu item as path of the icon.
        """
        ...

    def setIcon(self, icon:str) -> None:
        """
        self.setIcon(icon) -> None
        Set the icon on this menu item.
        @param icon: the new icon as a path
        """
        ...

    def script(self,) -> str:
        """
        self.script() -> String
        Returns the script that gets executed for this menu item.
        """
        ...

    def setScript(self,script) -> None:
        """
        self.setScript(script) -> None
        Set the script to be executed for this menu item.
        Note: To call a python script file, you can use the execfile() function. i.e:
        menu.setScript("execfile('script.py')")
        """
        ...

    def shortcut(self,) -> str:
        """
        self.shortcut() -> String
        Returns the keyboard shortcut on this menu item. The format of this is the PortableText format. It will return a string such as "Ctrl+Shift+P". Note that on Mac OS X the Command key is equivalent to Ctrl.
        """
        ...

    def setShortcut(self, keySequence:str) -> None:
        """
        self.setShortcut(keySequence) -> None
        Set the keyboard shortcut on this menu item.
        @param keySequence: the new shortcut in PortableText format, e.g. "Ctrl+Shift+P"
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
