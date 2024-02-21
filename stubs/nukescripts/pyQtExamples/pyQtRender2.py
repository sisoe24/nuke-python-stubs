# Copyright (c) 2009 The Foundry Visionmongers Ltd.  All Rights Reserved.
# This example assumes that PySide was built and setup with Nuke's Qt Version
# !! It will only work in this situation !!
# otherwise use the other example PyQtRender.py
import sys
import os.path

import nuke
import nukescripts

try:
    from PySide import QtCore, QtUiTools, QtWidgets
except:
    from PySide2 import QtCore, QtUiTools, QtWidgets


class pyQtRenderDialog(object):
    def __init__(self):
        # Set up the user interface from Designer.
        filepath = os.path.join(os.path.dirname(nukescripts.__file__),
                                'pyQtExamples', 'pyQtRender.ui')
        file = QtCore.QFile(filepath)
        file.open(QtCore.QIODevice.ReadOnly)

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(file)
        self.ui.connect(self.ui.renderButton, QtCore.SIGNAL('clicked()'), self.render)
        nuke.addOnCreate(self.onCreateCallback)

    def showUI(self):
        self.ui.show()

    def onCreateCallback(self):
        n = nuke.thisNode()
        if n.Class() == 'Write':
            n.setName(n.name())
            self.addItem(n)

    def addItem(self, n):
        item = QtWidgets.QTreeWidgetItem()
        item.setText(0, n['name'].value())
        self.ui.treeWidget.addTopLevelItem(item)

    def render(self):
        selectedItems = self.ui.treeWidget.selectedItems()
        writeNodes = [j for i in selectedItems for j in nuke.allNodes(
        ) if j.Class() == 'Write' and j['name'].value() == i.text(0)]
        for i in writeNodes:
            i['Render'].execute()


def initRenderDialog():
    dialog = pyQtRenderDialog()
    dialog.showUI()
