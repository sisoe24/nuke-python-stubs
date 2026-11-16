# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from nukescripts.blinkscripteditor import InputHighlighter as InputHighlighter
from nukescripts.blinkscripteditor import LineNumberArea as LineNumberArea
from nukescripts.blinkscripteditor import ScriptInputArea as ScriptInputArea
from nukescripts.pythonhighlighter import PythonHighlighter as PythonHighlighter
from nukescripts.usdhighlighter import UsdHighlighter as UsdHighlighter

blinkFuncsColour: Any
blinkTypesColour: Any
commentsFgColour: Any
kwdsFgColour: Any
stringLiteralsFgColourDQ: Any
stringLiteralsFgColourSQ: Any

class ScriptEditor:
    staticMetaObject: Any
    def __init__(self, knob: Any, parent: Any = ..., language: str = ...) -> None: ...
    def getText(self) -> Any: ...
    def printText(self) -> None: ...
    def storeTextOnKnob(self) -> None: ...
    def updateValue(self) -> None: ...

class ScriptEditorWidgetKnob:
    def __init__(self, knob: Any, language: str = ...) -> None: ...
    def makeUI(self) -> ScriptEditor: ...

def makeScriptEditorKnob(language: str = ...) -> ScriptEditorWidgetKnob: ...
