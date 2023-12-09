import typing
from typing import *
from numbers import Number

import ui
import core
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class Conformer(Object):
    """
    Provides and interface for querying and setting the conform options, such as file pattern filters and active rules.
    These options mirror those found in the conforming dialog box in the UI.
    """

    def __setattr__(self, name, value, ) -> None:
        """
        Implement setattr(self, name, value).
        """
        ...

    def __delattr__(self, name, ) -> None:
        """
        Implement delattr(self, name).
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def excludeNonOverlappingTimecode(self) -> bool:
        """
        self.excludeNonOverlappingTimecode() -> returns the state of the exclude non-overlapping timecode flag.

        @return: True when media which does not have timecode overlapping track items is excluded from matching.
        """
        ...

    def excludePatterns(self) -> typing.List[str]:
        """
        self.excludePatterns() -> returns the list of file patterns that are excluded from source media searches.
        By default this is empty.

        @return: A list containing the file patterns excluded from source media searches.
        """
        ...

    def includeAlreadyMatched(self) -> bool:
        """
        self.includeAlreadyMatched() -> returns the state of re-conform media flag.

        @return: True when the tracks that already have media attached will be re-conformed.
        """
        ...

    def includePatterns(self) -> typing.List[str]:
        """
        self.includePatterns() -> returns the list of file patterns that are included in source media searches.
        By default this is '*', which includes all file types.

        @return: A list containing the file patterns included in source media searches.
        """
        ...

    def nativeRuleFiltering(self) -> typing.Dict[str, bool]:
        """
        self.nativeRuleFiltering() -> returns a dictionary with the names of the native conforming rules and whether they are enabled for conforming.
        By changing the state of the flags for the rules and submitting the dictionary back to the Conformer the rules can be filterd out.

        @return: A dictionary containing the enabled flag for each native rule, keyed by the rule name.
        """
        ...

    def nativeRuleNames(self) -> typing.List[str]:
        """
        self.nativeRuleNames() -> returns the list of names for the native rules.
        This can be used to set rule filtering.

        @return: A list containing the names for all of the conform rules built-in to Hiero.
        """
        ...

    def pythonRuleFiltering(self) -> typing.Dict[str, bool]:
        """
        self.pythonRuleFiltering() -> returns a dictionary with the names of the Python conforming rules and whether they are enabled for conforming.
        By changing the state of the flags for the rules and submitting the dictionary back to the Conformer the rules can be filterd out.

        @return: A dictionary containing the enabled flag for each Python rule, keyed by the rule name.
        """
        ...

    def pythonRuleNames(self) -> typing.List[str]:
        """
        self.pythonRuleNames() -> returns the list of names for the registered Python rules.
        This can be used to set rule filtering.

        @return: A list containing the names for all of the conform rules that have been added through the Python API.
        """
        ...

    def setExcludeNonOverlappingTimecode(self, exclude: bool) -> None:
        """
        self.setExcludeNonOverlappingTimecode( flag ) -> controls whether matching is done on media which does not have timecode which overlaps the track item.
        """
        ...

    def setExcludePatterns(self, excludePatterns: typing.List[str]) -> None:
        """
        self.setExcludePatterns( filepatterns ) -> sets the list of file patterns to exclude from source media searches.
        """
        ...

    def setIncludeAlreadyMatched(self, val: bool) -> None:
        """
        self.setIncludeAlreadyMatched( flag ) -> controls whether to re-connect tracks that already have media matched to them.
        """
        ...

    def setIncludePatterns(self, includePatterns: typing.List[str]) -> None:
        """
        self.setIncludePatterns( filepatterns ) -> sets the list of file patterns to include in source media searches.
        """
        ...

    def setNativeRuleFiltering(self, ruleFiltering: typing.Dict[str, bool]) -> None:
        """
        self.setNativeRuleFiltering( ruleFiltering ) -> uses a dictionary keyed on the names of the native conforming rules to set whether each rule is enabled for conforming.
        """
        ...

    def setPythonRuleFiltering(self, ruleFiltering: typing.Dict[str, bool]) -> None:
        """
        self.setPythonRuleFiltering( ruleFiltering ) -> uses a dictionary keyed on the names of the Python conforming rules to set whether each rule is enabled for conforming.
        """
        ...

    def setUseBestTimecodeMatch(self, val: bool) -> None:
        """
        self.setUseBestTimecodeMatch( flag ) -> controls whether to accept the best timecode match if no rules match.
        """
        ...

    def useBestTimecodeMatch(self) -> bool:
        """
        self.useBestTimecodeMatch() -> returns the state of the use best timecode match flag.

        @return: True when the best timecode match will be accepted if no rules match.
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...
