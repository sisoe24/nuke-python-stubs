# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import nukescripts.panels as _nukescripts_panels
from nukescripts.panels import PythonPanel as PythonPanel

class FrameRangePanel(_nukescripts_panels.PythonPanel):
    """class that creates a Python panel for editing frame ranges"""
    def __init__(self, initalStart: Any, initialEnd: Any) -> None:
        """Constructor that takes 2 arguments for the initial start and end frame numbers"""
    def showDialog(self) -> None:
        """show panel dialog, returns if accept was pressed"""
