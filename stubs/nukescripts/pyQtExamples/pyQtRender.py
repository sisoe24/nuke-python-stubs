# Copyright (c) 2009 The Foundry Visionmongers Ltd.  All Rights Reserved.
# This example should be used if PySide2 was not built with the Nuke's own binaries
# otherwise please use pyQtRender2.py

import sys
import os.path

import nuke
import nukescripts
from nukescripts import utils, pyQtAppUtils


def initPyQtRenderDialog(pyQtApp, appArgv=['pyQtRenderDialog']):
    try:
        from PySide import QtCore, QtUiTools, QtWidgets
    except:
        from PySide2 import QtCore, QtUiTools, QtWidgets

    class pyRenderDialog(object):
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
                utils.executeInMainThread(i['Render'].execute)

    app = pyQtApp.getApplication(appArgv)
    dialog = pyQtRenderDialog()
    app.exec_()


def startQtRenderDialog():
    pyQtApp = pyQtAppUtils.pyQtAppHelper(start=True)
    pyQtApp.run(initPyQtRenderDialog, (pyQtApp,))
    return pyQtApp
