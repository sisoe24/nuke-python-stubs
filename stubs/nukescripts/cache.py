# Copyright (c) 2009 The Foundry Visionmongers Ltd.  All Rights Reserved.

import nuke_internal as nuke
from nuke import memory2 as memory
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QLabel, QDialog, QApplication


def clearAllCaches():
    """
    Clears all caches. The disk cache, viewer playback cache and memory buffers.
    """
    nuke.clearDiskCache()
    nuke.clearRAMCache()
    nuke.clearBlinkCache()
    memory.clearUsage()


def humanReadable(numBytes):
    """
    Returns a string containing the number of bytes and the ISO/IEC units used.
    """

    def formatBytes(numBytes, unit):
        return '{:.2f} {}B'.format(numBytes, unit)

    units = ('  ', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi', 'Yi')

    if numBytes < 0:
        return formatBytes(0, units[0])

    for unit in units[:-1]:
        if numBytes < 1024:
            return formatBytes(numBytes, unit)
        numBytes /= 1024

    return formatBytes(numBytes, units[-1])


class ValueLabel(QLabel):
    def __init__(self, text):
        QLabel.__init__(self, text)
        self.setAlignment(Qt.AlignRight | Qt.AlignVCenter)


class ReportTree(QDialog):
    def __init__(self):
        from PySide2.QtWidgets import QVBoxLayout

        QDialog.__init__(self, parent=QApplication.activeWindow(), f=Qt.Tool)

        self.setWindowTitle('Buffer Report')
        self.resize(800, 400)

        layout = QVBoxLayout()

        self.headerLayout = self.createHeaderLayout()
        self.updateUsageLabels()
        layout.addLayout(self.headerLayout)

        self.tree = self.createTree()
        self.updateTreeContents()
        layout.addWidget(self.tree)

        layout.addWidget(self.createButtonBox())

        self.setLayout(layout)

    def createHeaderLayout(self):
        from PySide2.QtWidgets import QGridLayout

        layout = QGridLayout()

        layout.addWidget(QLabel('Usage'), 0, 0)
        layout.addWidget(QLabel('Max Usage'), 1, 0)
        layout.addWidget(QLabel('Total Memory'), 2, 0)

        self.labels = []

        total = min(memory.totalRAM(), memory.totalVM())
        layout.addWidget(ValueLabel(humanReadable(total)), 2, 1)

        layout.setColumnStretch(3, 1)

        return layout

    def updateUsageLabels(self):
        if self.labels:
            for label in self.labels:
                self.headerLayout.removeWidget(label)
                label.hide()
                del label
            self.labels = []

        self.labels.append(ValueLabel(humanReadable(memory.usage())))
        self.headerLayout.addWidget(self.labels[0], 0, 1)

        percentage = (memory.usage() / memory.maxUsage()) * 100.0
        self.labels.append(ValueLabel('{:.2f} %'.format(percentage)))
        self.headerLayout.addWidget(self.labels[1], 0, 2)

        self.labels.append(ValueLabel(humanReadable(memory.maxUsage())))
        self.headerLayout.addWidget(self.labels[2], 1, 1)

        percentage = nuke.toNode('preferences')['CacheLimit'].value()
        self.labels.append(ValueLabel('{:.2f} %'.format(percentage)))
        self.headerLayout.addWidget(self.labels[3], 1, 2)

    def createTree(self):
        from PySide2.QtWidgets import (QHeaderView, QSizePolicy, QTreeWidget,
                                       QAbstractItemView)

        tree = QTreeWidget()

        headers = ['Name', 'Size', 'User', 'Data']
        tree.setColumnCount(len(headers))
        tree.setHeaderLabels(headers)
        tree.header().setSectionResizeMode(QHeaderView.Fixed)

        tree.setSelectionBehavior(QAbstractItemView.SelectRows)
        tree.setAlternatingRowColors(True)
        tree.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        return tree

    def updateTreeContents(self):
        from operator import itemgetter

        from PySide2.QtWidgets import QTreeWidgetItem

        def sumTotalBytes(items):
            return sum([item['bytes'] for item in items])

        self.info = memory.info()

        info = list(self.info.items())
        info.sort(key=lambda x: sumTotalBytes(x[1]), reverse=True)

        for name, items in info:
            branch = QTreeWidgetItem(self.tree)
            branch.setText(0, name)
            branch.setText(1, humanReadable(sumTotalBytes(items)))
            branch.setTextAlignment(1, Qt.AlignRight | Qt.AlignVCenter)

            items.sort(key=itemgetter('bytes'), reverse=True)

            for item in items:
                stem = QTreeWidgetItem(branch)
                stem.setText(0, item['name'])
                stem.setText(1, humanReadable(item['bytes']))
                stem.setTextAlignment(1, Qt.AlignRight | Qt.AlignVCenter)

                for user, data in item.items():
                    if user == 'name' or user == 'bytes':
                        continue

                    leaf = QTreeWidgetItem(stem)
                    leaf.setText(2, user)
                    leaf.setText(3, data)

        self.expandTree()
        for i in range(self.tree.columnCount()):
            self.tree.resizeColumnToContents(i)
        self.collapseTree()

    def createButtonBox(self):
        from PySide2.QtWidgets import QDialogButtonBox

        buttonBox = QDialogButtonBox()

        def addButton(name, function, tip=None):
            from PySide2.QtWidgets import QPushButton

            button = QPushButton(name)
            button.clicked.connect(function)
            if tip:
                button.setToolTip(tip)

            buttonBox.addButton(button, QDialogButtonBox.ActionRole)

        addButton('Expand All', self.expandTree)
        addButton('Collapse All', self.collapseTree)
        addButton('Update', self.updateContents)
        addButton('Save', self.save, 'Saves the memory info structure to a Json file.')

        return buttonBox

    def expandTree(self):
        self.expand(True)

    def collapseTree(self):
        self.expand(False)

    def __recursiveExpand(self, item, expand):
        for i in range(item.childCount()):
            child = item.child(i)
            self.__recursiveExpand(child, expand)
        item.setExpanded(expand)

    def expand(self, expand):
        for i in range(self.tree.topLevelItemCount()):
            item = self.tree.topLevelItem(i)
            self.__recursiveExpand(item, expand)

    def updateContents(self):
        self.updateUsageLabels()
        self.tree.clear()
        self.updateTreeContents()

    def save(self):
        from json import dump

        from PySide2.QtWidgets import QFileDialog

        path = QFileDialog.getSaveFileName(
            parent=self, caption='Save as', filter='Json (*.json)')

        if path is None:
            return

        dump(self.info, open(path[0], 'w'), indent=2)


def showReportDialog():
    """
    Creates a tree containing memory information from tracked allocations.
    """

    for widget in QApplication.topLevelWidgets():
        if isinstance(widget, ReportTree):
            widget.updateContents()
            widget.show()
            widget.windowHandle().requestActivate()
            return

    dialog = ReportTree()
    dialog.show()
