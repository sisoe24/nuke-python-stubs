# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import hiero.importers.FnEdlDefinitions as _hiero_importers_FnEdlDefinitions
import hiero.importers.yeanpypa as _hiero_importers_yeanpypa
from hiero.core.log import debug as debug
from hiero.core.log import info as info
from hiero.importers.FnEdlDefinitions import AsyncGeneratorType as AsyncGeneratorType
from hiero.importers.FnEdlDefinitions import Aud34Action as Aud34Action
from hiero.importers.FnEdlDefinitions import AudioRangeAction as AudioRangeAction
from hiero.importers.FnEdlDefinitions import BuiltinFunctionType as BuiltinFunctionType
from hiero.importers.FnEdlDefinitions import CellType as CellType
from hiero.importers.FnEdlDefinitions import ClassMethodDescriptorType as ClassMethodDescriptorType
from hiero.importers.FnEdlDefinitions import CodeType as CodeType
from hiero.importers.FnEdlDefinitions import CoroutineType as CoroutineType
from hiero.importers.FnEdlDefinitions import EllipsisType as EllipsisType
from hiero.importers.FnEdlDefinitions import FrameType as FrameType
from hiero.importers.FnEdlDefinitions import FunctionType as FunctionType
from hiero.importers.FnEdlDefinitions import GeneratorType as GeneratorType
from hiero.importers.FnEdlDefinitions import GetSetDescriptorType as GetSetDescriptorType
from hiero.importers.FnEdlDefinitions import IndexedSourceElementAction as IndexedSourceElementAction
from hiero.importers.FnEdlDefinitions import MappingProxyType as MappingProxyType
from hiero.importers.FnEdlDefinitions import MemberDescriptorType as MemberDescriptorType
from hiero.importers.FnEdlDefinitions import MethodDescriptorType as MethodDescriptorType
from hiero.importers.FnEdlDefinitions import MethodType as MethodType
from hiero.importers.FnEdlDefinitions import MethodWrapperType as MethodWrapperType
from hiero.importers.FnEdlDefinitions import ModuleType as ModuleType
from hiero.importers.FnEdlDefinitions import MultipleEffectFieldAction as MultipleEffectFieldAction
from hiero.importers.FnEdlDefinitions import NamedElementAction as NamedElementAction
from hiero.importers.FnEdlDefinitions import NoneType as NoneType
from hiero.importers.FnEdlDefinitions import NotImplementedType as NotImplementedType
from hiero.importers.FnEdlDefinitions import ParseEDL as ParseEDL
from hiero.importers.FnEdlDefinitions import RetimeElementAction as RetimeElementAction
from hiero.importers.FnEdlDefinitions import SingleEffectFieldAction as SingleEffectFieldAction
from hiero.importers.FnEdlDefinitions import SourceElementAction as SourceElementAction
from hiero.importers.FnEdlDefinitions import SourceModeFieldAction as SourceModeFieldAction
from hiero.importers.FnEdlDefinitions import TimeCodeSpecifierAction as TimeCodeSpecifierAction
from hiero.importers.FnEdlDefinitions import TimeCodeSubFieldSpecifierAction as TimeCodeSubFieldSpecifierAction
from hiero.importers.FnEdlDefinitions import WipeEffectFieldAction as WipeEffectFieldAction
from hiero.importers.FnEdlDefinitions import WrapperDescriptorType as WrapperDescriptorType
from hiero.importers.FnEdlDefinitions import dump as dump
from hiero.importers.FnEdlDefinitions import flatten as flatten
from hiero.importers.FnEdlStructures import EditDecision as EditDecision
from hiero.importers.FnEdlStructures import EffectField as EffectField
from hiero.importers.FnEdlStructures import ModeField as ModeField
from hiero.importers.FnEdlStructures import NamedElement as NamedElement
from hiero.importers.FnEdlStructures import RetimeElement as RetimeElement
from hiero.importers.FnEdlStructures import TimeCode as TimeCode
from hiero.importers.yeanpypa import AndRule as AndRule
from hiero.importers.yeanpypa import AnyOf as AnyOf
from hiero.importers.yeanpypa import CallbackParser as CallbackParser
from hiero.importers.yeanpypa import Combine as Combine
from hiero.importers.yeanpypa import EmptyStackException as EmptyStackException
from hiero.importers.yeanpypa import EndOfStringException as EndOfStringException
from hiero.importers.yeanpypa import ErrorRule as ErrorRule
from hiero.importers.yeanpypa import Group as Group
from hiero.importers.yeanpypa import IgnoreWhite as IgnoreWhite
from hiero.importers.yeanpypa import InputReader as InputReader
from hiero.importers.yeanpypa import Literal as Literal
from hiero.importers.yeanpypa import MatchWhite as MatchWhite
from hiero.importers.yeanpypa import NoneOf as NoneOf
from hiero.importers.yeanpypa import OneOrMore as OneOrMore
from hiero.importers.yeanpypa import Optional as Optional
from hiero.importers.yeanpypa import OrRule as OrRule
from hiero.importers.yeanpypa import ParseException as ParseException
from hiero.importers.yeanpypa import ParseResult as ParseResult
from hiero.importers.yeanpypa import Rule as Rule
from hiero.importers.yeanpypa import Word as Word
from hiero.importers.yeanpypa import ZeroOrMore as ZeroOrMore
from hiero.importers.yeanpypa import parse as parse
from nukescripts import TracebackType as TracebackType
import hiero as hiero

ACTUAL_SEPARATOR: _hiero_importers_yeanpypa.OrRule
ALPHA: _hiero_importers_yeanpypa.CallbackParser
AUDIO1: int
AUDIO2: int
AUDIO3: int
AUDIO4: int
AUDIO_RANGE: _hiero_importers_yeanpypa.AndRule
AUDIO_TRACK_NUMBER: _hiero_importers_yeanpypa.Combine
AUD_ELEMENT: _hiero_importers_yeanpypa.AndRule
COMMENT_ELEMENT: _hiero_importers_yeanpypa.AndRule
CRLF: str
DIGIT: _hiero_importers_yeanpypa.CallbackParser
DLEDL_EDIT_ELEMENT: _hiero_importers_yeanpypa.AndRule
DLEDL_EDIT_FILENAME_ELEMENT: _hiero_importers_yeanpypa.AndRule
DLEDL_EDIT_FRAME_ELEMENT: _hiero_importers_yeanpypa.AndRule
DLEDL_EDIT_RESOLUTION_ELEMENT: _hiero_importers_yeanpypa.AndRule
DLEDL_ELEMENT: _hiero_importers_yeanpypa.AndRule
DLEDL_PATH_ELEMENT: _hiero_importers_yeanpypa.AndRule
DLEDL_START_ELEMENT: _hiero_importers_yeanpypa.AndRule
EDIT_ELEMENT: _hiero_importers_yeanpypa.OrRule
EDIT_LIST: _hiero_importers_yeanpypa.OrRule
EDIT_NUMBER: _hiero_importers_yeanpypa.Combine
EDIT_NUMBER_SUBFIELD: _hiero_importers_yeanpypa.Combine
EDIT_SUB_ELEMENT: _hiero_importers_yeanpypa.OneOrMore
EDL: _hiero_importers_yeanpypa.ZeroOrMore
EFFECT_FIELD: _hiero_importers_yeanpypa.OrRule
EFFECT_PARAMETER_FIELD: _hiero_importers_yeanpypa.Combine
FCP_ELEMENT: _hiero_importers_yeanpypa.AndRule
FILENAME: _hiero_importers_yeanpypa.AndRule
FROMCLIPNAME: str
FROMCLIP_ELEMENT: _hiero_importers_yeanpypa.AndRule
HEXADECIMAL_DIGIT: _hiero_importers_yeanpypa.AnyOf
HEXADECIMAL_NUMBER: _hiero_importers_yeanpypa.AndRule
IDENTIFIER: _hiero_importers_yeanpypa.Combine
INDEXED_EDIT_ELEMENT: _hiero_importers_yeanpypa.OrRule
INDEXED_SOURCE_ELEMENT: _hiero_importers_yeanpypa.AndRule
INFORMATIONAL_DIRECTIVE: _hiero_importers_yeanpypa.Combine
INTEGER: _hiero_importers_yeanpypa.Combine
KEYCLIPNAME: str
KEYCLIP_ELEMENT: _hiero_importers_yeanpypa.AndRule
LEADING_RADIX_NUMBER: _hiero_importers_yeanpypa.OrRule
LOWER_ALPHA: _hiero_importers_yeanpypa.AnyOf
MODE_AUDIO_SUBFIELD: _hiero_importers_yeanpypa.OrRule
MODE_FIELD: _hiero_importers_yeanpypa.OrRule
MULTIPLE_SOURCE_EFFECT: _hiero_importers_yeanpypa.AndRule
NON_ZERO_DIGIT: _hiero_importers_yeanpypa.AnyOf
NUMBER: _hiero_importers_yeanpypa.Combine
PRINTABLE_CHARACTER: _hiero_importers_yeanpypa.OrRule
PRINTABLE_STRING: _hiero_importers_yeanpypa.Combine
RADIX_NUMBER: _hiero_importers_yeanpypa.Combine
REAL_NUMBER: _hiero_importers_yeanpypa.Combine
RETIME_DIRECTIVE: _hiero_importers_yeanpypa.AndRule
SEPARATOR: _hiero_importers_yeanpypa.OneOrMore
SIGNED_NUMBER: _hiero_importers_yeanpypa.Combine
SINGLE_SOURCE_EFFECT: _hiero_importers_yeanpypa.OrRule
SOURCEFILE_ELEMENT: _hiero_importers_yeanpypa.AndRule
SOURCE_ELEMENT: _hiero_importers_yeanpypa.AndRule
SOURCE_ENTRY_FIELD: _hiero_importers_yeanpypa.OrRule
SOURCE_EXIT_FIELD: _hiero_importers_yeanpypa.OrRule
SOURCE_IDENTIFICATION_FIELD: _hiero_importers_yeanpypa.Combine
SPACE: _hiero_importers_yeanpypa.Literal
STARTTC: str
SUB_FRAME_SPECIFIER: _hiero_importers_yeanpypa.AndRule
SYNC_ENTRY_FIELD: _hiero_importers_yeanpypa.OrRule
SYNC_EXIT_FIELD: _hiero_importers_yeanpypa.OrRule
SYSTEM_DIRECTIVE: _hiero_importers_yeanpypa.AndRule
TERMINATOR: _hiero_importers_yeanpypa.OrRule
TIME_CODE: _hiero_importers_yeanpypa.OrRule
TIME_CODE_FIELD_SPECIFIER: _hiero_importers_yeanpypa.OrRule
TIME_CODE_SEPARATOR: _hiero_importers_yeanpypa.OrRule
TIME_CODE_SUB_FIELD_SPECIFIER: _hiero_importers_yeanpypa.AndRule
TOCLIPNAME: str
TOCLIP_ELEMENT: _hiero_importers_yeanpypa.AndRule
UPPER_ALPHA: _hiero_importers_yeanpypa.AnyOf
USER_ELEMENT: _hiero_importers_yeanpypa.AndRule
VIDEO1: int
VIDEO2: int
WIPE_EFFECT: _hiero_importers_yeanpypa.AndRule
alpha: _hiero_importers_yeanpypa.CallbackParser
digit: _hiero_importers_yeanpypa.CallbackParser
error: _hiero_importers_yeanpypa.ErrorRule
hexdigit: _hiero_importers_yeanpypa.AnyOf
integer: _hiero_importers_yeanpypa.Combine

class EdlImporter:
    def __init__(self) -> None:
        """Initialize"""
    def createClipAndMedia(self, element: Any, mediaDict: Any, trackDict: Any) -> None: ...
    def createTransition(self, prevelement: Any, element: Any, clipDict: Any) -> None: ...
    def displayName(self) -> str: ...
    def extractFilenamesAndClipName(self, element: Any) -> tuple[list[Any], Any]: ...
    def getClipData(self, name: Any, edlElement: Any, speed: Any, mediaType: Any, startTC: Any) -> dict[Any, Any]: ...
    def getMediaData(self, filename: Any, edlElement: Any, duration: Any, startTC: Any) -> dict[Any, Any]: ...
    def getTrackItemSpeedAndDuration(self, edlElement: Any) -> tuple[Any, Any]: ...
    def getWarningMessages(self) -> list[Any]: ...
    def importFile(self, fileName: Any) -> Any:
        """Return true if file is succesfully parsed"""
    def isOptionRequired(self, option: Any) -> bool: ...
    def isValidFile(self, fileName: Any) -> bool:
        """Return true if file is of correct type"""
    def prepass(self, edl: Any) -> None: ...
    @staticmethod
    def prepassCheckKeyEvent(element: Any, eventElements: Any) -> None:
        """Handle Key events.  For example:

        006  001      V     C        00:01:08:22 00:01:09:18 00:00:03:23 00:00:04:19
        006  001      V     K B      00:01:09:18 00:01:10:07 00:00:04:19 00:00:05:08
        006  001      V     K    000 00:01:08:22 00:01:09:11 00:00:04:19 00:00:05:08
        * FROM CLIP NAME: C003_007_3010_04.mov
        * KEY CLIP NAME: C003_007_3010_04.mov

        The initial Cut line is optional.  The second line is the Key Background.  Third line is
        the Key In element, which places a clip on a second track.

        We need to a) move FROMCLIPNAME from the Key In element to the background and cut elements,
        b) rename KEYCLIPNAME to FROMCLIPNAME for the Key In element.
        """

class track:
    def __init__(self, trackId: Any, trackType: Any, timelineId: Any, name: Any, filename: Any) -> None: ...
    def getTrackId(self) -> Any: ...
    def getTrackType(self) -> Any: ...

def cleanupFileName(fileName: Any) -> Any: ...

def fixLineEndings(text: Any) -> str: ...

def isAbsPath(path: Any) -> bool: ...

def isFileName(name: Any) -> bool: ...

BuiltinMethodType = _hiero_importers_FnEdlDefinitions.BuiltinFunctionType
LambdaType = _hiero_importers_FnEdlDefinitions.FunctionType
