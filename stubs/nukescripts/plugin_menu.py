# Copyright (c) 2009 The Foundry Visionmongers Ltd.  All Rights Reserved.

import os.path

import nuke_internal as nuke

# Warning this relies on nuke replacing matching menu entries so that
# we don't get duplicates:


def update_plugin_menu(menuname):
    pluginList = []
    if nuke.env['nc']:
        plugins = nuke.plugins(nuke.ALL | nuke.NODIR | nuke.REGISTERED | nuke.NOREADERWRITER,
                               '*.'+nuke.PLUGIN_EXT, '*.ofx.bundle', '*.gizmo', '*.gznc')
    else:
        plugins = nuke.plugins(nuke.ALL | nuke.NODIR | nuke.REGISTERED |
                               nuke.NOREADERWRITER, '*.'+nuke.PLUGIN_EXT, '*.ofx.bundle', '*.gizmo')
    for i in plugins:
        (root, ext) = os.path.splitext(i)
        (root, ext) = os.path.splitext(root)
        # Sometimes we get files like ._Glare.gizmo, etc due to Mac OS X
        # or editors and that returns an empty string for root.
        if root is None or len(root) == 0:
            continue
        if not root[0] == '@':
            pluginList.append(root)
    n = nuke.menu('Nodes').addMenu('Other/'+menuname)
    pluginList.sort()

    for plugin in pluginList:
        s = plugin.upper()
        p = n.addMenu(s[0])
        p.addCommand(plugin, "nuke.createNode('"+plugin+"')")
