# Type stubs for nuke 17.1v2. Generated; do not edit.

"""Functions used by the ApplyMaterial node"""

from typing import Any
import nukescripts.panels as _nukescripts_panels
from nukescripts.panels import PythonPanel as PythonPanel

class ObjectNameChooserDialog(_nukescripts_panels.PythonPanel):
    """A dialog box with a SceneView_Knob for choosing from a tree of names.

    The easiest way to use this is via the chooseObjectName function from this
    module, e.g.:

      chooseObjectName(["/root/foo", "/root/bar", "/root/bar/baz"])

    This will create and display the dialog as a modal popup and give you the
    selected name, or None if cancel was pressed.
    """
    def __init__(self, names: Any) -> None: ...
    def selectedName(self) -> Any:
        """Get the name selected in the SceneView_Knob."""

def chooseObjectName(amfNode: Any) -> None:
    """Given an ApplyMaterial node, show a modal ObjectNameChooserDialog
    for it then set the filter_name knob to whatever name was selected in the
    dialog.
    """
