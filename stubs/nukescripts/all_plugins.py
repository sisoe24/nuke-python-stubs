# Copyright (c) 2009 The Foundry Visionmongers Ltd.  All Rights Reserved.

import nuke_internal as nuke

# List of libraries which may be in the plugins directory that are dependencies,
# not plugins themselves
PLUGINS_FILTER = [
    'Alembic_In',
    'BlackmagicRawAPI',
    'DNxHR',
    'DecoderCUDA',
    'DecoderOpenCL',
    'InstructionSetServicesAVX',
    'InstructionSetServicesAVX2',
    'FnNukeCodecs',
    'REDCuda-x64',
    'REDCuda-x86',
    'REDDecoder',
    'REDDecoder-x64',
    'REDDecoder-x86',
    'REDMetal',
    'REDOpenCL',
    'REDOpenCL-x64',
    'REDOpenCL-x86',
    'REDR3D',
    'REDR3D-x64',
    'REDR3D-x86',
    'SMDK-VC140-x64-4_21_0',
    'SonyRawDev'
]


def _filterPlugin(plugin):
    for filter in PLUGINS_FILTER:
        if filter in plugin:
            return True
    return False


def load_all_plugins():
    """ Scan all of Nuke's plugin load paths and attempt to load any .dylib, .so, or .dll
    files as a plugin, skipping any files listed in PLUGINS_FILTER.
    """
    tried = 0
    failed = 0
    p = nuke.plugins(nuke.ALL, '*.'+nuke.PLUGIN_EXT)
    for i in p:
        if _filterPlugin(i):
            continue

        tried += 1
        print(i)
        try:
            try_load = nuke.load(i)
        except:
            print(i, 'failed to load.')
            failed += 1
    if failed > 0:
        print(failed, 'of', tried, 'plugin(s) total did not load')
    else:
        print('All available binary plugins (', tried, ') successfully loaded')
