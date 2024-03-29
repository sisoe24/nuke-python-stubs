"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import ui
import core
import nuke
import hiero
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class TaskData(dict):
    """
    TaskData is used as a seed for creating classes, wrapping up all of
    the parameters and making it simpler to add new ones
    """
    kPreset = 'preset'
    kItem = 'item'
    kExportRoot = 'exportRoot'
    kShotPath = 'shotPath'
    kVersion = 'version'
    kExportTemplate = 'exportTemplate'
    kResolver = 'resolver'
    kCutHandles = 'cutHandles'
    kRetime = 'retime'
    kStartFrameSource = 'startFrameSource'
    kStartFrame = 'startFrame'
    kProject = 'project'
    kSubmission = 'submission'
    kSkipOffline = 'skipOffline'
    kPresetId = 'presetId'
    kShotNameIndex = 'shotNameIndex'
    kMediaToSkip = 'mediaToSkip'

    def __init__(self, preset, item, exportRoot, shotPath, version, exportTemplate, project, cutHandles=None, resolver=None, retime=False, startFrame=None, startFrameSource=None, submission=None, skipOffline=True, presetId=None, shotNameIndex='', mediaToSkip=[]) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    @property
    def __dict__(self) -> typing.Any:
        """
        dictionary for instance variables (if defined)
        """
        ...

    @property
    def __weakref__(self) -> typing.Any:
        """
        list of weak references to the object (if defined)
        """
        ...
