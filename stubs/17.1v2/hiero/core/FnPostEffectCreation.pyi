# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
from hiero.core.FnEffectHelpers import effectInputSourceCoods as effectInputSourceCoods

AfterEffectCreatedOperations: dict
OverrideEffectKnobDefaults: dict

def afterEffectCreated(effectItem: Any) -> None:
    """Perform timeline specific operation for the given soft effect
    that has just been created.
    @param effectItem: the effect that has just been created
    """

def overrideKnobDefaults(effectItem: Any) -> None:
    """Override timeline specific knob defaults for the given soft effect
    @param effectItem: the effect who's knob will be overriden
    """
