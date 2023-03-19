'''
Module for accessing OCIO configs.
'''

import os
import platform
from typing import List
from pathlib import Path

import nuke_internal as nuke
import PyOpenColorIO


def list_rindex(l: List, value) -> int:
    return len(l) - l[-1::-1].index(value)


def getOCIOConfigDirs():
    '''
    Get the list of directories where OCIO configs are stored.
    '''
    ocioConfigPaths = nuke.pluginPath()
    if platform.system() == 'Darwin':
        mod_path = Path(nuke.__file__)
        mod_path_parts = list(mod_path.parts)
        root_index = list_rindex(mod_path_parts, 'Contents')
        resource_path = Path(*mod_path_parts[:root_index]) / 'Resources'
        ocioConfigPaths.append(str(resource_path))

    return ocioConfigPaths


def getOCIOConfig():
    '''
    Get the current OCIO config, as specified by the root node.
    '''
    rootNode = nuke.root()
    ocioConfigKnob = rootNode.knob('OCIO_config')

    ocioConfigSelection = ocioConfigKnob.value()

    if (ocioConfigSelection == 'custom'):
        # Just use the config specified by the custom path
        customOCIOConfigPathKnob = rootNode.knob('customOCIOConfigPath')
        customOCIOConfigPath = customOCIOConfigPathKnob.getValue()

        if (customOCIOConfigPath != ''):
            return loadConfig(customOCIOConfigPath)
        else:
            raise IOError('Custom config is selected but path is not specified.')
    else:
        # Construct the config path from the specific option.
        # Look for configs in the nuke path
        for p in getOCIOConfigDirs():
            configPath = os.path.join(p, 'OCIOConfigs', 'configs', ocioConfigSelection)
            if os.path.exists(configPath) and os.path.isdir(configPath):
                return loadConfig(os.path.join(configPath, 'config.ocio'))

            # Checks that the selected config is an ocio file only,
            # which is the case for ACES 1.3 configs.
            configFile = configPath + '.ocio'
            if os.path.exists(configFile):
                return loadConfig(configFile)

        # If we got here, the config couldn't be found in any Nuke path
        raise IOError("Config '%s' doesn't exist" % ocioConfigSelection)

    return None


def loadConfig(configPath):
    '''
    Load the OCIO Config from the given path
    '''
    if not os.path.exists(configPath):
        raise IOError("Config '%s' doesn't exist" % configPath)

    # FIXME This might have performance problems. In which case either
    # the configs need to be cached in Python, or add a OCIO dependency on
    # the Nuke lib and cache the config object on the root node.
    return PyOpenColorIO.Config.CreateFromFile(configPath)
