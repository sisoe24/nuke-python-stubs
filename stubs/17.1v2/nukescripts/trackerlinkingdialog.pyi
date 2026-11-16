# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import nukescripts.panels as _nukescripts_panels
from nukescripts.panels import PythonPanel as PythonPanel

class LinkToTrackPanel(_nukescripts_panels.PythonPanel):
    """This panel offers the user a selection of Tracker nodes in the project and
    returns an expression referencing either the Tracker's 'translate' knob or
    computing the average value of the selected track points on the node.
    """
    def __init__(self, groupContext: Any) -> None: ...
    def addToPane(self) -> None: ...
    def knobChanged(self, knob: Any) -> None: ...

def trackerlinkingdialog(groupContext: Any) -> list[Any] | None: ...

def trackerlinkingdialogexpressionx() -> str: ...

def trackerlinkingdialogexpressiony() -> str: ...
