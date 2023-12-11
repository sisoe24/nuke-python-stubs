import nuke_internal as nuke
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QSplitter, QVBoxLayout

from .blinkscripteditor import *


class ScriptEditor(QWidget):

    def __init__(self, knob, parent=None, language='blink'):
        super(ScriptEditor, self).__init__(parent)

        self.knob = knob

        # Set title
        self.setWindowTitle('BlinkScript Editor')

        # Make splitter
        splitter = QSplitter(Qt.Vertical)

        # Setup main layout
        self.myTextWindow = ScriptInputArea(None, self, self, language)
        if language == 'usd':
            self.myTextWindow.setLineWrapMode(self.myTextWindow.NoWrap)
        splitter.addWidget(self.myTextWindow)

        layout = QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(splitter)

        # Update the stored text on the knob when the user changes it
        self.myTextWindow.userChangedEvent.connect(self.storeTextOnKnob)

    def printText(self):
        data = self.myTextWindow.toPlainText()
        print(str(data))

    def getText(self):
        data = self.myTextWindow.toPlainText()
        return data

    def storeTextOnKnob(self):
        self.knob.setText(self.myTextWindow.toPlainText())

    def updateValue(self):
        # Update the UI text from the knob if contents differ
        # (avoids scroll position jumping on focus out after typing)
        knobText = self.knob.getText()
        if knobText != self.myTextWindow.toPlainText():
            self.myTextWindow.setPlainText(knobText)


class ScriptEditorWidgetKnob():
    def __init__(self, knob, language='blink'):
        self.knob = knob
        self.language = language

    def makeUI(self):
        return ScriptEditor(self.knob, None, self.language)


def makeScriptEditorKnob(language='blink'):
    return ScriptEditorWidgetKnob(nuke.thisKnob(), language)
