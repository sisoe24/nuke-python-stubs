# Copyright (c) 2010 The Foundry Visionmongers Ltd.  All Rights Reserved.
import re
import sys
import _thread
import os.path
import platform
import subprocess

import nuke
import nukescripts
import nukescripts.flipbooking as flipbooking

################################################################################
# README
#
# This is an example script that demonstrated how to subimplement for RV.
# You need to modify this to get it to work!
#
# To include this in nuke please add this to somewhere in the python search path
# and add the following line to __init__.py (or menu.py):
# from rv import *
################################################################################


class ExampleRVFlipbook(flipbooking.FlipbookApplication):
    """This is an example implementation of how to deal with implementing a
       flipbook application other than FrameCycler for Nuke. This script needs
       to be modified in several places before it can work, so please read all
       of the notes marked with TODO and modify them where necessary."""

    def __init__(self):
        # TODO: Please put your own path in here or add RV path discovery.
        self._rvPath = '/Applications/RV64.app/Contents/MacOS/RV64'

    def name(self):
        return 'RV'

    def path(self):
        return self._rvPath

    def cacheDir(self):
        return os.environ['NUKE_TEMP_DIR']

    def run(self, filename, frameRanges, views, options):
        # TODO: You probably want more involved handling of frame ranges!
        sequence_interval = str(frameRanges.minFrame())+'-'+str(frameRanges.maxFrame())

        os.path.normpath(filename)

        args = []
        if nuke.env['WIN32']:
            args.append("\"" + self.path() + "\"")
            filename = filename.replace('/', '\\')
            filename = "\"" + filename + "\""
        else:
            args.append(self.path())

        roi = options.get('roi', None)
        if roi != None and not (roi['x'] == 0.0 and roi['y'] == 0.0 and roi['w'] == 0.0 and roi['h'] == 0.0):
            args.append('-c '+str(int(roi['x'])))
            args.append(str(int(roi['y'])))
            args.append(str(int(roi['w'])))
            args.append(str(int(roi['h'])))

        lut = options.get('lut', '')
        if lut == 'linear-sRGB':
            args.append('-sRGB')
        elif lut == 'linear-rec709':
            args.append('-rec709')

        args.append(filename)

        if sequence_interval:
            args.append(sequence_interval)

        # print args
        os.spawnv(os.P_NOWAITO, self.path(), args)

    def capabilities(self):
        return {
            'proxyScale': False,
            'crop': True,
            'canPreLaunch': False,
            'supportsArbitraryChannels': True,
            'maximumViews': 2,
            # TODO: This list is compiled from running rv with the following:
            # RV64 -formats | grep 'format "' | awk '{print $2}' | tr '[:space:]' ','; echo
            # This may differ for your platform!
            'fileTypes': ['j2k', 'jpt', 'jp2', 'dpx', 'cin', 'cineon', 'jpeg', 'jpg', 'rla', 'rpf', 'yuv', 'exr', 'openexr', 'sxr', 'tif', 'tiff', 'sm', 'tex', 'tx', 'tdl', 'shd', 'targa', 'tga', 'tpic', 'rgbe', 'hdr', 'iff', 'png', 'z', 'zfile', 'sgi', 'bw', 'rgb', 'rgba', '*mraysubfile*', 'movieproc', 'stdinfb', 'aiff', 'aif', 'aifc', 'wav', 'snd', 'au', 'mov', 'avi', 'mp4', 'm4v', 'dv']

        }


flipbooking.register(ExampleRVFlipbook())
