# Copyright (c) 2009 The Foundry Visionmongers Ltd.  All Rights Reserved.

import nuke_internal as nuke

isHiero = nuke.env['hiero']
if isHiero:
    # Callbacks for localisation preferences
    from . import localisationprefs
    from .panels import *
    from .nodepresets import *
else:

    from .crop import *
    from .drop import *
    from .edit import *
    from .flip import *
    from .info import *
    from .misc import *
    from .udim import *
    from .cache import *
    from .flags import *
    from .frame import *
    from .group import *
    from .nodes import *
    from .reads import *
    from .utils import *
    from .camera import *
    from .create import *
    from .script import *
    from .select import *
    from .snap3d import *
    from .execute import *
    from .openurl import *
    from .precomp import *
    from .version import *
    from .animation import *
    from .all_plugins import *
    from .flipbooking import *
    # from .panel_test import *
    from .plugin_menu import *
    from .renderpanel import *
    from .autobackdrop import *
    from .importexport import *
    from .nukeprofiler import *
    from .unrealreader import *
    from .searchreplace import *
    from .scripteditorknob import *
    if nuke.GUI:
        # Callbacks for localisation preferences
        # Callback for viewsettings preferences
        from . import readviewscheck, localisationprefs, viewsettingsprefs
        from .panels import *
        from .cattery import *
        from .toolbars import *
        from .toolsets import *
        from .nodepresets import *
        from .renderdialog import *
        from .framerangepanel import *
        from .trackerlinkingdialog import *

    # Leave these in their module namespace rather than pulling into
    # top level of nukescripts.
    from . import psd, stereo, bookmarks
