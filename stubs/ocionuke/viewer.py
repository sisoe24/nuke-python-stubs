# SPDX-License-Identifier: BSD-3-Clause
# Copyright Contributors to the OpenColorIO Project.

import os
from functools import partial

import nuke_internal as nuke

from . import config


def get_active_views(ocioConfig):
    """
    Return a list of all active views across all displays, ordered by user-defined precedence.
    If the active views are not explicitly set through the config or the environment,
    return all available views.
    """
    active_views = os.environ['OCIO_ACTIVE_VIEWS'].split(
        ':') if 'OCIO_ACTIVE_VIEWS' in os.environ else ocioConfig.getActiveViews().split(', ')
    active_views = [_f for _f in active_views if _f]
    if not active_views:
        active_views = [view for display in ocioConfig.getDisplays()
                        for view in ocioConfig.getViews(display)]
    return active_views


def get_display_active_views(ocioConfig, display):
    """
    Return a list of active views of one display, ordered by user-defined precedence.
    """
    active_views = get_active_views(ocioConfig)
    display_views_set = set(ocioConfig.getViews(display))
    return [active_view for active_view in active_views if active_view in display_views_set]


def get_displays_and_active_views(ocioConfig):
    """
    Return a list of (active display, list of views)-tuples, ordered by user-defined precedence.
    """
    return [(display, get_display_active_views(ocioConfig, display), ) for display in ocioConfig.getDisplays()]


def make_ocio_display(display_, view_, **kwargs):
    """
    If we try to create an OCIODisplay trying to pass the display and view
    through Python it will fail for the case of switching to a different display.
    This is because Python will try to set the knob values,
    which in case of the view depend on the display, and since the OCIODisplay is
    default-constructed it always starts out with only the default display's views.
    The requested knob value is not found and an error is thrown.

    This implements a workaround where we create the node initially with default settings,
    then change the display and view knobs afterwards, adding a new view name if needed.
    The OCIODisplay will detect the added view name and adjust itself accordingly.
    """
    node = nuke.nodes.OCIODisplay()

    current_views = list(node.knob('view').values())
    if not view_ in current_views:
        node.knob('view').setValues(current_views + [view_])

    node.knob('display').setValue(display_)
    node.knob('view').setValue(view_)

    return node


def storeSelectionBeforeReload():
    nuke.ViewerProcess.storeSelectionBeforeReload()


def restoreSelectionAfterReload():
    return nuke.ViewerProcess.restoreSelectionAfterReload()


def register_viewers(ocioConfigPath, also_remove='default', isReload=False):
    """Registers the a viewer process for each display device/view, and
    sets the default viewer process.

    ``also_remove`` can be set to either:

    - "default" to remove the default sRGB/rec709 viewer processes
    - "all" to remove all processes
    - "none" to leave existing viewer processes untouched
    """

    if also_remove not in ('default', 'none', 'all'):
        raise ValueError("also_remove should be set to 'default', 'none' or 'all'")

    if also_remove == 'default':
        nuke.ViewerProcess.unregister('rec1886')
        nuke.ViewerProcess.unregister('rec709')
        nuke.ViewerProcess.unregister('sRGB')
        nuke.ViewerProcess.unregister('None')
    elif also_remove == 'all':
        # Unregister all processes, including None, which should be defined in config.ocio
        for curname in nuke.ViewerProcess.registeredNames():
            nuke.ViewerProcess.unregister(curname)

    # Formats the display and transform, e.g "Film1D (sRGB)"
    DISPLAY_UI_FORMAT = '%(view)s (%(display)s)'

    ocioConfig = config.loadConfig(ocioConfigPath)

    # Get the default display and view
    defaultDisplay = ocioConfig.getDefaultDisplay()
    defaultView = ocioConfig.getDefaultView(defaultDisplay)

    displays_and_views = get_displays_and_active_views(ocioConfig)
    for display, view_list in displays_and_views:
        # Register the node
        for view in view_list:
            nuke.ViewerProcess.register(
                name=DISPLAY_UI_FORMAT % {'view': view, 'display': display},
                call=partial(make_ocio_display, display, view),
                args=(),
                kwargs={'display': defaultDisplay, 'view': defaultView, 'layer': 'all'})

    if isReload:
        restoreSelectionAfterReload()
    else:
        # Set default display and view as the default used on Nuke startup
        nuke.knobDefault(
            'Viewer.viewerProcess',
            DISPLAY_UI_FORMAT % {'view': defaultView, 'display': defaultDisplay})
