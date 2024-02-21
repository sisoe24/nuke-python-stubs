# Copyright (c) 2011 The Foundry Visionmongers Ltd.  All Rights Reserved.

import os.path

import hiero.ui
from PySide2 import QtCore, QtWidgets
from hiero.ui.FnTaskUIFormLayout import TaskUIFormLayout

from . import FnXMLExportTask


class XMLExportUI(hiero.ui.TaskUIBase):
    def __init__(self, preset):
        """Initialize"""
        hiero.ui.TaskUIBase.__init__(self, FnXMLExportTask.XMLExportTask, preset, 'XML Exporter')

    def includeMarkersCheckboxChanged(self, state):
        # Slot to handle change of checkbox state
        self._preset.properties()['includeMarkers'] = state == QtCore.Qt.Checked

    def populateUI(self, widget, exportTemplate):
        layout = widget.layout()
        formLayout = TaskUIFormLayout()
        layout.addLayout(formLayout)

        # create checkboxes for whether the XML should contain timeline markers
        self.includeMarkersCheckbox = QtWidgets.QCheckBox()
        self.includeMarkersCheckbox.setToolTip(
            'Enable to include Tags as markers in the exported XML.')
        self.includeMarkersCheckbox.setCheckState(QtCore.Qt.Unchecked)
        if self._preset.properties()['includeMarkers']:
            self.includeMarkersCheckbox.setCheckState(QtCore.Qt.Checked)
        self.includeMarkersCheckbox.stateChanged.connect(self.includeMarkersCheckboxChanged)

        # Add Checkbox to layout
        formLayout.addRow('Include Markers:', self.includeMarkersCheckbox)


hiero.ui.taskUIRegistry.registerTaskUI(FnXMLExportTask.XMLExportPreset, XMLExportUI)
