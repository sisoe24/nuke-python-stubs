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


class ProcessorBase(object):
    """
    ProcessorBase is the base class from which all Processors should derive.
    The Processor object is responible for taking the object selection and spawning
    Tasks with the appropriate parameters.
    """

    def __init__(self, preset, submission, synchronous=False) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def startProcessing(self, exportItems, preview=False) -> None:
        """
        Generate export tasks and add them to the export queue. If preview is
        True, the tasks are created and returned, but not scheduled for execution.
        """
        ...

    def skipOffline(self) -> None:
        """

        """
        ...

    def processTaskPreQueue(self) -> None:
        """
        processTaskPreQueue() Walk Tasks in submission and mark any duplicates.

        """
        ...

    def validItem(self, supportedTypes, item) -> None:
        """
        Get if the task is able to run on the item it was initialised with.
        """
        ...

    def _tagCopiedSequence(self, sequence, sequenceCopy) -> None:
        """

        """
        ...

    def _addCopyTag(self, copy, original) -> None:
        """

        """
        ...

    def errors(self) -> None:
        """
        Get an error string from the processor.  Iterates over child tasks and
        adds their error messages to the string.  Returns None if there were no errors.
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
