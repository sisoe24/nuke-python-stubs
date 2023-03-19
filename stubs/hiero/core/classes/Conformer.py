import typing
from typing import *
from numbers import Number

import core
import PySide2

from . import *


class Conformer(Object):
    """
    Provides and interface for querying and setting the conform options, such as file pattern filters and active rules.
    These options mirror those found in the conforming dialog box in the UI.
    """

    def __setattr__(self, name, value, ):
        """
        Implement setattr(self, name, value).
        """
        return None

    def __delattr__(self, name, ):
        """
        Implement delattr(self, name).
        """
        return None

    def __init__(self,  *args, **kwargs):
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        return None

    def __new__(self, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        return None

    def excludeNonOverlappingTimecode(self) -> bool:
        """
        self.excludeNonOverlappingTimecode() -> returns the state of the exclude non-overlapping timecode flag.

        @return: True when media which does not have timecode overlapping track items is excluded from matching.
        """
        return bool()

    def excludePatterns(self) -> typing.List*args:
        """
        self.excludePatterns() -> returns the list of file patterns that are excluded from source media searches.
        By default this is empty.

        @return: A list containing the file patterns excluded from source media searches.
        """
        return list()

    def includeAlreadyMatched(self) -> bool:
        """
        self.includeAlreadyMatched() -> returns the state of re-conform media flag.

        @return: True when the tracks that already have media attached will be re-conformed.
        """
        return bool()

    def includePatterns(self) -> typing.List*args:
        """
        self.includePatterns() -> returns the list of file patterns that are included in source media searches.
        By default this is '*', which includes all file types.

        @return: A list containing the file patterns included in source media searches.
        """
        return list()

    def nativeRuleFiltering(self) -> typing.Dict*args:
        """
        self.nativeRuleFiltering() -> returns a dictionary with the names of the native conforming rules and whether they are enabled for conforming.
        By changing the state of the flags for the rules and submitting the dictionary back to the Conformer the rules can be filterd out.

        @return: A dictionary containing the enabled flag for each native rule, keyed by the rule name.
        """
        return str()

    def nativeRuleNames(self) -> typing.List*args:
        """
        self.nativeRuleNames() -> returns the list of names for the native rules.
        This can be used to set rule filtering.

        @return: A list containing the names for all of the conform rules built-in to Hiero.
        """
        return list()

    def pythonRuleFiltering(self) -> typing.Dict*args:
        """
        self.pythonRuleFiltering() -> returns a dictionary with the names of the Python conforming rules and whether they are enabled for conforming.
        By changing the state of the flags for the rules and submitting the dictionary back to the Conformer the rules can be filterd out.

        @return: A dictionary containing the enabled flag for each Python rule, keyed by the rule name.
        """
        return str()

    def pythonRuleNames(self) -> typing.List*args:
        """
        self.pythonRuleNames() -> returns the list of names for the registered Python rules.
        This can be used to set rule filtering.

        @return: A list containing the names for all of the conform rules that have been added through the Python API.
        """
        return list()

    def setExcludeNonOverlappingTimecode(self, exclude: bool) -> None:
        """
        self.setExcludeNonOverlappingTimecode( flag ) -> controls whether matching is done on media which does not have timecode which overlaps the track item.
        """
        return None

    def setExcludePatterns(self, excludePatterns: typing.List*args) -> None:
        """
        self.setExcludePatterns( filepatterns ) -> sets the list of file patterns to exclude from source media searches.
        """
        return None

    def setIncludeAlreadyMatched(self, val: bool) -> None:
        """
        self.setIncludeAlreadyMatched( flag ) -> controls whether to re-connect tracks that already have media matched to them.
        """
        return None

    def setIncludePatterns(self, includePatterns: typing.List*args) -> None:
        """
        self.setIncludePatterns( filepatterns ) -> sets the list of file patterns to include in source media searches.
        """
        return None

    def setNativeRuleFiltering(self, ruleFiltering: typing.Dict*args) -> None:
        """
        self.setNativeRuleFiltering( ruleFiltering ) -> uses a dictionary keyed on the names of the native conforming rules to set whether each rule is enabled for conforming.
        """
        return None

    def setPythonRuleFiltering(self, ruleFiltering: typing.Dict*args) -> None:
        """
        self.setPythonRuleFiltering( ruleFiltering ) -> uses a dictionary keyed on the names of the Python conforming rules to set whether each rule is enabled for conforming.
        """
        return None

    def setUseBestTimecodeMatch(self, val: bool) -> None:
        """
        self.setUseBestTimecodeMatch( flag ) -> controls whether to accept the best timecode match if no rules match.
        """
        return None

    def useBestTimecodeMatch(self) -> bool:
        """
        self.useBestTimecodeMatch() -> returns the state of the use best timecode match flag.

        @return: True when the best timecode match will be accepted if no rules match.
        """
        return bool()

    def __copy__(self,) -> None:
        """

        """
        return None
