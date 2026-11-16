# Type stubs for nuke 17.1v2. Generated; do not edit.

"""Python code to be executed after a Studio project is loaded. Currently this
is just used to fix up deprecated reformatting options for track items on a
sequence.
"""

from typing import Any
from hiero.core.FnEffectHelpers import calculateReformat as calculateReformat
from hiero.core.events import EventType as EventType
from hiero.core.events import registerInterest as registerInterest
import hiero as hiero

def fixDeprecatedReformatStateProperties(project: Any) -> None:
    """Find track items in the project which are set to reformat in a way which
    is now invalid. Creates soft effect items which are equivalent to the old
    behavior.
    """

def onProjectLoaded(event: Any) -> None:
    """Callback after a project is loaded. """

def shiftLinkedSubTrackItems(trackItem: Any) -> None:
    """Move a track item's linked sub-track items up to the next sub-track so new
    effects can be inserted at the bottom.
    """
