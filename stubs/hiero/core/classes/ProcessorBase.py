import typing
from typing import *
from numbers import Number

import ui
import core
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

    def __init__(self, preset, submission, synchronous=False):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def startProcessing(self, exportItems, preview=False):
        """
        Generate export tasks and add them to the export queue. If preview is
        True, the tasks are created and returned, but not scheduled for execution.
        """
        return None

    def skipOffline(self):
        """

        """
        return None

    def processTaskPreQueue(self):
        """
        processTaskPreQueue() Walk Tasks in submission and mark any duplicates.

        """
        return None

    def validItem(self, supportedTypes, item):
        """
        Get if the task is able to run on the item it was initialised with.
        """
        return None

    def _tagCopiedSequence(self, sequence, sequenceCopy):
        """

        """
        return None

    def _addCopyTag(self, copy, original):
        """

        """
        return None

    def errors(self):
        """
        Get an error string from the processor.  Iterates over child tasks and
        adds their error messages to the string.  Returns None if there were no errors.
        """
        return None

    @property
    def __dict__(self) -> Any:
        """
        dictionary for instance variables (if defined)
        """
        return None

    @property
    def __weakref__(self) -> Any:
        """
        list of weak references to the object (if defined)
        """
        return None
