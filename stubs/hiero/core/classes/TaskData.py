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

    def __init__(self, preset: typing.Any, item: typing.Any, exportRoot: typing.Any, shotPath: typing.Any, version: typing.Any, exportTemplate: typing.Any, project: typing.Any, cutHandles: typing.Optional[typing.Any] = None, resolver: typing.Optional[typing.Any] = None, retime: bool = False, startFrame: typing.Optional[typing.Union[int, str]] = None, startFrameSource: typing.Optional[typing.Any] = None, submission: typing.Optional[typing.Any] = None, skipOffline: bool = True, presetId: typing.Optional[typing.Any] = None, shotNameIndex: str = '', mediaToSkip: typing.List[typing.Any] = []) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    @property
    def __dict__(self) -> typing.Dict[str, typing.Any]:
        """
        dictionary for instance variables (if defined)
        """
        ...

    @property
    def __weakref__(self) -> typing.List[typing.Any]:
        """
        list of weak references to the object (if defined)
        """
        ...
