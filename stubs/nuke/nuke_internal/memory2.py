#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Memory module containing functionality for querying and controlling
Nuke's Memory API, currently the module is named memory2 for
backwards compatibility with the old nuke.memory(cmd, value)
function which is now deprecated. Once removed this module will be
deprecated and it will be renamed to nuke.memory. To avoid future
conflicts it is recommended to import like so:

from nuke import memory2 as memory
"""

from _memory import *
