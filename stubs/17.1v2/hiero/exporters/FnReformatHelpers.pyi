# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import hiero.core.nuke.Node as _hiero_core_nuke_Node
from hiero.core.nuke.Node import ReformatNode as ReformatNode
import hiero as hiero

kReformatDefaults: dict

def reformatNodeFromPreset(preset: Any, sequenceFormat: Any, trackItem: Any = ...) -> _hiero_core_nuke_Node.ReformatNode | None:
    """If reformat options are configured in the preset, return a ReformatNode
    created from them. Otherwise returns None.
    @param sequenceFormat: Specifies the sequence format.  Used only when preset
    specifies reformatting to sequence format
    @param trackItem: item from which to take the reformat settings when
    to sequence format is specified.
    """

def reformatSettingsFromPreset(preset: Any) -> tuple[str, Any, float | None, Any, Any, str]:
    """Extract the reformat properties from a task preset.  If the reformat type is 'to format', the format returns the format,
    if it's 'scale' returns the scale value. 
    """
