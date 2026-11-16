# Type stubs for nuke 17.1v2. Generated; do not edit.

"""Code for handling changes in the localization default in the preferences
and applying that as knob defaults on Read nodes.
"""

from typing import Any

kLocalizationPolicyDefaultKnob: str

def initCallbacks() -> None:
    """Get the default localisation policy from the preferences node and set
    up the knob changed callback.
    """

def onPrefsKnobChanged() -> None:
    """Callback from the preferences node.  If the default localisation
    policy has changed, update it on the read nodes.
    """

def updateReadKnobLocalisationDefaults(value: Any) -> None:
    """Set the knob defaults for the nodes with the cacheLocal knob. """
