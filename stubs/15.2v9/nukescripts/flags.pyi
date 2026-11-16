# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import nuke as _nuke
import nukescripts as _nukescripts
from nukescripts import TracebackType as TracebackType

class KnobFlagClearer:
    def __enter__(self) -> KnobFlagClearer: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: _nukescripts.TracebackType | None) -> bool | None: ...
    def __init__(self, knob: _nuke.Knob, flags: set[int]) -> None: ...

def get_fully_qualified_name(node: _nuke.Node) -> str:
    """Returns the full name of the node, including any parents, separated by periods.

    :param node: Node to retrieve name from.
    :type node: nuke.Node
    :return: Full name of the node, including any parents, separated by periods.
    :rtype: str
    """

def toggle(knob: Any) -> None:
    """"Inverts" some flags on the selected nodes.

    What this really does is set all of them to the same value, by finding the
    majority value and using the inverse of that.
    """
