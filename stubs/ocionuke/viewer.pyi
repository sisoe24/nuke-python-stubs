# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from ocionuke import config as config

def get_active_views(ocioConfig: Any) -> list[Any]:
    """Return a list of all active views across all displays, ordered by user-defined precedence.
    If the active views are not explicitly set through the config or the environment,
    return all available views.
    """

def get_display_active_views(ocioConfig: Any, display: Any) -> list[Any]:
    """Return a list of active views of one display, ordered by user-defined precedence."""

def get_displays_and_active_views(ocioConfig: Any) -> list[tuple[Any, list[Any]]]:
    """Return a list of (active display, list of views)-tuples, ordered by user-defined precedence."""

def make_ocio_display(display_: Any, view_: Any, **kwargs: Any) -> Any:
    """If we try to create an OCIODisplay trying to pass the display and view
    through Python it will fail for the case of switching to a different display.
    This is because Python will try to set the knob values,
    which in case of the view depend on the display, and since the OCIODisplay is
    default-constructed it always starts out with only the default display's views.
    The requested knob value is not found and an error is thrown.

    This implements a workaround where we create the node initially with default settings,
    then change the display and view knobs afterwards, adding a new view name if needed.
    The OCIODisplay will detect the added view name and adjust itself accordingly.
    """

def register_viewers(ocioConfigPath: Any, also_remove: str = ..., isReload: bool = ...) -> None:
    """Registers the a viewer process for each display device/view, and
    sets the default viewer process.

    ``also_remove`` can be set to either:

    - "default" to remove the default sRGB/rec709 viewer processes
    - "all" to remove all processes
    - "none" to leave existing viewer processes untouched
    """

def restoreSelectionAfterReload() -> Any: ...

def storeSelectionBeforeReload() -> None: ...
