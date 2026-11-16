# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any

class CameraFilmBackPresets:
    """A simple container object for holding the label and film back data of a camera."""
    def __init__(self) -> None:
        """Initialise by adding all of our presets."""
    def addPreset(self, label: Any, filmBackDict: Any) -> None:
        """Parse a dict for the camera aperture size and add to the list."""

def addPreset(label: Any, haperture: Any, vaperture: Any) -> None:
    """Adds a preset to the global list of presets."""

def getFilmBackSize(index: Any) -> list[Any]:
    """Returns the film back size for the given index."""

def getLabels() -> list[Any]:
    """Returns the list of preset labels for display in the knob."""
