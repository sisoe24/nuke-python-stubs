# Copyright (c) 2022 The Foundry Visionmongers Ltd. All Rights Reserved.

import hiero.ui

from .FnOTIOExportTask import OTIOExportTask, OTIOExportPreset


class OTIOExportUI(hiero.ui.TaskUIBase):
    """ UI for OTIO file export.
    Currently empty until we need to add some parameters to the export.
    """

    def __init__(self, preset):
        hiero.ui.TaskUIBase.__init__(self, OTIOExportTask, preset, 'OTIO Exporter (Beta)')


hiero.ui.taskUIRegistry.registerTaskUI(OTIOExportPreset, OTIOExportUI)
