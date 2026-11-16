# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import PySide6.QtGui as _PySide6_QtGui

class UsdHighlighter(_PySide6_QtGui.QSyntaxHighlighter):
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, doc: Any, parent: Any = ...) -> None: ...
    def highlightBlock(self, text: Any) -> None: ...
