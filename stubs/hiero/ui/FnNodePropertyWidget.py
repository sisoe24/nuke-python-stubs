# Copyright (c) 2020 The Foundry Visionmongers Ltd.  All Rights Reserved.

import nuke_internal as nuke
import PySide2.QtCore as QtCore
import PySide2.QtWidgets as QtWidgets
from hiero.ui.FnUIProperty import (UIPropertyFactory,
                                   CascadingEnumerationProperty)
from hiero.core.FnFloatRange import IntRange, FloatRange
from hiero.ui.FnTaskUIFormLayout import TaskUIFormLayout

from .FnDisclosureButton import DisclosureButton


class NodePropertyWidget(QtWidgets.QWidget):
    """ This class generates a widget based on the passed in node. The created
    widget contains widgets for all the knobs that are present in the
    propertyDictionaries passed into the constructor. The widgets are created by
    calling makeWidget() on the respective knobs. This class will also update the
    values of the knob in the node when setting a value on a property widget. The
    layout of the property widgets will attempt to mimic the layout of the knobs
    on the node. Any non-default knob values will get written into the passed in
    preset dictionary.
    Note: the node must not be deleted until after the NodePropertyWidget
    has been deleted."""

    # Knob flags that aren't exposed in the nuke Python API
    CASCADING_KNOB_TYPE = 68

    def __init__(self, node, propertyDictionaries, presetDictionary):
        QtWidgets.QWidget.__init__(self)
        self._node = node
        self._presetDictionary = presetDictionary
        self._knobs = []
        self._linkKnobMap = {}
        self._layout = TaskUIFormLayout()
        self.initializeUI(propertyDictionaries)
        self.setLayout(self._layout)
        self.updateProperties()
        nuke.addKnobChanged(self.knobChanged, nodeClass='Write', node=self._node)

    def removeCallbacks(self):
        nuke.removeKnobChanged(self.knobChanged, nodeClass='Write', node=self._node)

    def createKnobWidget(self, knob):
        widget = knob.makeWidget()
        knobName = knob.name()
        actualKnob = knob.getLinkedKnob() if isinstance(knob, nuke.Link_Knob) else knob
        if actualKnob.name() is not knobName:
            self._linkKnobMap[actualKnob.name()] = knobName
        self._knobs.append((knobName, widget))
        if (knobName in self._presetDictionary) and (self._presetDictionary[knobName] is not None):
            actualKnob.setValue(self._presetDictionary[knobName])
        else:
            self.updatePresetValue(knob)
        return widget

    def updatePresetValue(self, knob):
        """ Sets the knob value in the preset dictionary if the knob is visible. If
        the knob isn't visible then the value is cleared as we don't want to store
        values of hidden knobs in the preset dictionary. This is so that we don't
        set the values on these hidden knobs on the node since setting the value
        of hidden knobs can have unintended consequences."""
        knobName = self._linkKnobMap.get(knob.name(), knob.name())
        actualKnob = knob.getLinkedKnob() if isinstance(knob, nuke.Link_Knob) else knob
        notDefault = True
        # Some knobs don't have notDefault() implemented in which case we always
        # write the value into the dictionary
        try:
            notDefault = actualKnob.notDefault()
        except Exception:
            pass
        if knob.visible() and notDefault:
            isInt = knob.getFlag(nuke.STORE_INTEGER) and not isinstance(
                knob, nuke.Enumeration_Knob)
            self._presetDictionary[knobName] = int(
                actualKnob.value()) if isInt else actualKnob.toScript()
        else:
            # Remove key
            self._presetDictionary.pop(knobName, None)

    def knobChanged(self):
        if nuke.thisNode().name() == self._node.name():
            # Check if the knob is one of the knobs that this widget is displaying
            knobName = self._linkKnobMap.get(
                nuke.thisKnob().name(), nuke.thisKnob().name())
            if knobName in [knobWidgetPair[0] for knobWidgetPair in self._knobs]:
                self.updateProperties()
                self.updatePresetValue(nuke.thisKnob())

    def updateProperties(self):
        """ Iterates through the property widgets and updates their state
        to reflect the current value and visibility of their associated knobs."""
        for key, widget in self._knobs:
            knob = self._node.knobs()[key]

            actualKnob = knob.getLinkedKnob() if isinstance(knob, nuke.Link_Knob) else knob

            # update visibility and enabled state
            widget.parentWidget().layout().setWidgetVisible(widget, knob.visible())
            widget.setEnabled(knob.enabled())

    def createDisclosureWidget(self, tabKnob):
        """ Creates a DisclosureButton and an associated widget that's visibility
        is toggled by the DisclosureButton. The widget itself has a TaskUIFormLayout
        set on it. Returns the created widget."""
        disclosureWidget = QtWidgets.QWidget()
        disclosureWidget.setLayout(TaskUIFormLayout())
        disclosureButton = DisclosureButton(False)
        disclosureButton.setText(tabKnob.label())
        disclosureButton.addWidget(disclosureWidget)
        return disclosureButton, disclosureWidget

    def knobOnNewLine(self, knob):
        """ Determines if a knob starts on a new row or is placed next
        to the previous knob."""
        return knob.getFlag(nuke.STARTLINE)

    def addWidgetsToNewRow(self, layout, labels, widgets):
        """ Adds widgets to the layout as a new row, adding them as
        multi widget rows as necessary, otherwise adding as a normal row
        if a single widget is provided (this is due to layout.setWidgetVisible
        behaving differently for multi widget rows which we don't want for
        a single widget row)."""
        if widgets:
            layout.addMultiWidgetRow(labels, widgets)

            del labels[:]
            del widgets[:]

    def initializeUI(self, propertyDictionaries):
        """ Iterates through the propertyDictionaries and creates UIProperties
        for each key in the dictionaries, where each key should be the name of a
        desired knob on the Write node. The UIProperties will store their values
        in the _presetDictionary, using the knob name as the key. If the
        _presetDictionary already has a value for the knob name, it will also
        initialise the UIProperty with that value."""
        labels = []
        widgets = []
        knobNames = []
        disclosureWidget = None
        disclosureButton = None

        # Used to provide DisclosureButton functionality for closed Tab_Knob groups
        layoutStack = [self._layout]

        for properties in propertyDictionaries:
            knobNames.extend(properties.keys())

        # We use a range based for loop rather than a for-each loop
        # here as we want to iterate through the knobs in the order
        # they appear and calling knobs() on the node does not return
        # them in order.
        for knob in self._node.allKnobs():
            if isinstance(knob, nuke.Obsolete_Knob):
                continue

            knob.setFlag(nuke.KNOB_CHANGED_ALWAYS)
            knob.setFlag(nuke.KNOB_CHANGED_RIGHTCONTEXT)

            knobName = knob.name()

            if isinstance(knob, nuke.Tab_Knob):
                # Tab_Knob.value() effectively returns true if the tab is open. In the
                # node a collapsible/expandable tab knob will report as closed since
                # they are created using BeginClosedGroup. The group is ended by using
                # EndGroup which will insert a Tab_Knob that is open. The code will
                # create a DisclosureWidget when it first encounters a closed Tab_Knob
                # and will add all subsequent knobs to that DisclosureWidget until it
                # reaches an open Tab_Knob. This approach almost certainly doesn't capture
                # the nuances of the different Tab_Knob::Types but works for our current
                # limited use case.
                isOpen = knob.value()
                if isOpen and (len(layoutStack) > 1):
                    if layoutStack[-1].rowCount() or len(widgets):
                        self.addWidgetsToNewRow(layoutStack[-1], labels, widgets)
                        layoutStack.pop()
                        layoutStack[-1].addRow(disclosureButton)
                        layoutStack[-1].addRow(disclosureWidget)
                    else:  # Empty DisclosureWidget so don't add to layout
                        layoutStack.pop()
                    disclosureWidget = None
                    disclosureButton = None
                elif not isOpen:
                    self.addWidgetsToNewRow(layoutStack[-1], labels, widgets)
                    disclosureButton, disclosureWidget = self.createDisclosureWidget(knob)
                    layoutStack.append(disclosureWidget.layout())

            if self.knobOnNewLine(knob):
                self.addWidgetsToNewRow(layoutStack[-1], labels, widgets)

            if knobName in knobNames:
                knobNames.remove(knobName)
                widget = self.createKnobWidget(knob)
                label = knob.label()
                widgets.append(widget)
                labels.append(label)

        # Add any remaining widgets
        self.addWidgetsToNewRow(layoutStack[-1], labels, widgets)

        assert len(knobNames) == 0, ('If this is false then not all of the knob names could be matched to knobs'
                                     ' on the Write node, suggesting the propertyDictionaries should be updated.'
                                     ' Unmatched knobNames:\n' + ', '.join(str(name) for name in knobNames))
