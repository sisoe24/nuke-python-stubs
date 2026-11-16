# Type stubs for nuke 17.1v2. Generated; do not edit.

"""Various utilities relating to the OCIOCDLTransform node"""

from typing import Any
import nukescripts as nukescripts

def SelectCCCIDPanel(*args: Any, **kwargs: Any) -> Any: ...

def export_as_cc(node: Any = ..., filename: Any = ...) -> None:
    """Export a OCIOCDLTransform node as a ColorCorrection XML file
    (.cc)

    If node is None, "nuke.thisNode()" will be used. If filename is
    not specified, the user will be prompted.
    """

def export_multiple_to_ccc(filename: Any = ...) -> None:
    """Exported all selected OCIOCDLTransform nodes to a
    ColorCorrectionCollection XML file (.ccc)
    """

def import_cc_from_xml(node: Any = ..., filename: Any = ...) -> None:
    """Import a ColorCorrection XML (.cc) into a OCIOCDLTransform node.

    If node is None, "nuke.thisNode()" will be used. If filename is
    not specified, the user will be prompted.
    """

def import_multiple_from_ccc(filename: Any = ...) -> None:
    """Import a ColorCorrectionCollection file (.ccc) into multiple
    OCIOCDLTransform nodes. Also creates a single node for a .cc file
    """

def select_cccid_for_filetransform(node: Any = ..., fileknob: str = ..., cccidknob: str = ...) -> None:
    """Select cccid button for the OCIOFileTransform node, also used
    in OCIOCDLTransform. Presents user with list of cccid's within the
    specified .ccc file, and sets the cccid knob to the selected ID.
    """
