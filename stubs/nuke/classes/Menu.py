from typing import *
from numbers import Number

import nuke

from . import *


class Menu(MenuItem):
    """
    Menu
    """

    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def addCommand(self, name: str, command: Optional[str] = None, shortcut: Optional[str] = None, icon: Optional[str] = None, tooltip: Optional[str] = None, index: Optional[Number] = None, readonly: Optional[bool] = None, shortcutContext: Optional[int] = None, tag: Optional[int] = None, tagTarget: Optional[int] = None, node) -> Any:
        """
        self.addCommand(name, command, shortcut, icon, tooltip, index, readonly, shortcutContext, tag, tagTarget, node) -> The menu/toolbar item that was added to hold the command.
        Add a new command to this menu/toolbar. Note that when invoked, the command is automatically enclosed in an undo group, so that undo/redo functionality works. Optional arguments can be specified by name.
        Note that if the command argument is not specified, then the command will be auto-created as a "nuke.createNode()" using the name argument as the node to create.

        Example:
        menubar = nuke.menu('Nuke')
        fileMenu = menubar.findItem('File')
        fileMenu.addCommand('NewCommand', 'print 10', shortcut='t')

        @param name: The name for the menu/toolbar item. The name may contain submenu names delimited by '/' or '', and submenus are created as needed.
        @param command: Optional. The command to add to the menu/toolbar. This can be a string to evaluate or a Python Callable (function, method, etc) to run.
        @param shortcut: Optional. The keyboard shortcut for the command, such as 'R', 'F5' or 'Ctrl-H'. Note that this overrides pre-existing other uses for the shortcut.
        @param icon: Optional. An icon for the command. This should be a path to an icon in the nuke.pluginPath() directory. If the icon is not specified, Nuke will automatically try to find an icon with the name argument and .png appended to it.
        @param tooltip: Optional. The tooltip text, displayed on mouseover for toolbar buttons.
        @param index: Optional. The position to insert the new item in, in the menu/toolbar. This defaults to last in the menu/toolbar.
        @param readonly: Optional. True/False for whether the item should be available when the menu is invoked in a read-only context.
        @param shortcutContext: Optional. Sets the shortcut context (0==Window, 1=Application, 2=DAG).
        @param tag: Optional. Sets the tag icon that is displayed on the menu/toolbar item (0==None, 1=Beta, 2=Classic).
        @param tagTarget: Optional. Determines which type of the menu/toolbar should display the specified tag (0==Unknown, 1=Beta, 2=TabMenu, 3=ContextMenu, 7=All).
        @param nodeClass: The NodeClass the tag should apply to.@return: The menu/toolbar item that was added to hold the command.
        """
        ...

    def addMenu(self, **kwargs) -> Any:
        """
        self.addMenu(**kwargs) -> The submenu that was added.
        Add a new submenu.
        @param **kwargs The following keyword arguments are accepted:
                        name      The name for the menu/toolbar item
                        icon      An icon for the menu. Loaded from the nuke search path.
                        tooltip   The tooltip text.
                        index     The position to insert the menu in. Use -1 to add to the end of the menu.
                        tag       Optional. Sets the tag icon that is displayed on the menu/toolbar item (0==None, 1=Beta, 2=Classic).
        @return: The submenu that was added.
        """
        ...

    def clearMenu(self,) -> bool:
        """
        self.clearMenu()
        Clears a menu.
        @param **kwargs The following keyword arguments are accepted:
                        name      The name for the menu/toolbar item
        @return: true if cleared, false if menu not found
        """
        ...

    def addSeparator(self, **kwargs) -> Any:
        """
        self.addSeparator(**kwargs) -> The separator that was created.
        Add a separator to this menu/toolbar.
        @param **kwargs The following keyword arguments are accepted:
        index     The position to insert the new separator in, in the menu/toolbar.
        @return: The separator that was created.
        """
        ...

    def findItem(self, name: str) -> None:
        """
        self.findItem(name) -> Menu or None
        Finds a submenu or command with a particular name.
        @param name: The name to search for.
        @return: The submenu or command we found, or None if we could not find anything.
        """
        ...

    def menu(self, name: str) -> None:
        """
        self.menu(name) -> Menu or None
        Finds a submenu or command with a particular name.
        @param name: The name to search for.
        @return: The submenu or command we found, or None if we could not find anything.
        """
        ...

    def removeItem(self, name: str) -> bool:
        """
        self.removeItem(name) -> None
        Removes a submenu or command with a particular name. If the containing menu becomes empty, it will be removed too.
        @param name: The name to remove for.
        @return: true if removed, false if menu not found
        """
        ...

    def items(self,) -> None:
        """
        self.items() -> None
        Returns a list of sub menu items.
        """
        ...

    def name(self,) -> str:
        """
        self.name() -> String
        Returns the name of the menu item.
        """
        ...

    def addAction(self, action) -> bool:
        """
        self.addAction(action) -> bool
        Adds the QAction to the menu.
        """
        ...

    def updateMenuItems(self,) -> None:
        """
        updateMenuItems() -> None
        Updates menu items' states. Call on about to show menu.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
