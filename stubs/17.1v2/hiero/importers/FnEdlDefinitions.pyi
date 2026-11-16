# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
from typing import final
from typing import overload
import hiero.importers.FnEdlStructures as _hiero_importers_FnEdlStructures
import hiero.importers.yeanpypa as _hiero_importers_yeanpypa
from hiero.core.log import info as info
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
FROMCLIP_ELEMENT: _hiero_importers_yeanpypa.AndRule
HEXADECIMAL_DIGIT: _hiero_importers_yeanpypa.AnyOf
HEXADECIMAL_NUMBER: _hiero_importers_yeanpypa.AndRule
IDENTIFIER: _hiero_importers_yeanpypa.Combine
INDEXED_EDIT_ELEMENT: _hiero_importers_yeanpypa.OrRule
INDEXED_SOURCE_ELEMENT: _hiero_importers_yeanpypa.AndRule
INFORMATIONAL_DIRECTIVE: _hiero_importers_yeanpypa.Combine
INTEGER: _hiero_importers_yeanpypa.Combine
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
SUB_FRAME_SPECIFIER: _hiero_importers_yeanpypa.AndRule
SYNC_ENTRY_FIELD: _hiero_importers_yeanpypa.OrRule
SYNC_EXIT_FIELD: _hiero_importers_yeanpypa.OrRule
SYSTEM_DIRECTIVE: _hiero_importers_yeanpypa.AndRule
TERMINATOR: _hiero_importers_yeanpypa.OrRule
TIME_CODE: _hiero_importers_yeanpypa.OrRule
TIME_CODE_FIELD_SPECIFIER: _hiero_importers_yeanpypa.OrRule
TIME_CODE_SEPARATOR: _hiero_importers_yeanpypa.OrRule
TIME_CODE_SUB_FIELD_SPECIFIER: _hiero_importers_yeanpypa.AndRule
TOCLIP_ELEMENT: _hiero_importers_yeanpypa.AndRule
UPPER_ALPHA: _hiero_importers_yeanpypa.AnyOf
USER_ELEMENT: _hiero_importers_yeanpypa.AndRule
WIPE_EFFECT: _hiero_importers_yeanpypa.AndRule
alpha: _hiero_importers_yeanpypa.CallbackParser
digit: _hiero_importers_yeanpypa.CallbackParser
error: _hiero_importers_yeanpypa.ErrorRule
hexdigit: _hiero_importers_yeanpypa.AnyOf
integer: _hiero_importers_yeanpypa.Combine

@final
class AsyncGeneratorType:
    def __aiter__(self, /) -> Any:
        """Return an awaitable, that resolves in asynchronous iterator."""
    def __anext__(self, /) -> Any:
        """Return a value or raise StopAsyncIteration."""
    def __del__(self, *args: Any, **kwargs: Any) -> Any: ...
    __name__: Any
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def aclose(self) -> Any:
        """aclose() -> raise GeneratorExit inside generator."""
    ag_await: Any
    ag_code: Any
    ag_frame: Any
    ag_running: Any
    def asend(self, v: Any) -> Any:
        """asend(v) -> send 'v' in generator."""
    def athrow(self, typ: Any, val: Any = ..., tb: Any = ...) -> Any:
        """athrow(typ[,val[,tb]]) -> raise exception in generator."""

@final
class BuiltinFunctionType:
    def __call__(self, /, *args: Any, **kwargs: Any) -> Any:
        """Call self as a function."""
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    __name__: Any
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    __self__: Any
    __text_signature__: Any

@final
class CellType:
    """Create a new cell object.

     contents
       the contents of the cell. If not specified, the cell will be empty,
       and 
    further attempts to access its cell_contents attribute will
       raise a ValueError.
    """
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    cell_contents: Any
    def __new__(cls, *args: Any, **kwargs: Any) -> CellType: ...

@final
class ClassMethodDescriptorType:
    def __call__(self, /, *args: Any, **kwargs: Any) -> Any:
        """Call self as a function."""
    def __get__(self, instance: Any, owner: Any = ..., /) -> Any:
        """Return an attribute of instance, which is of type owner."""
    __name__: Any
    __objclass__: Any
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    __text_signature__: Any

@final
class CodeType:
    """Create a code object.  Not for the faint of heart."""
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    co_argcount: Any
    co_cellvars: Any
    co_code: Any
    co_consts: Any
    co_exceptiontable: Any
    co_filename: Any
    co_firstlineno: Any
    co_flags: Any
    co_freevars: Any
    co_kwonlyargcount: Any
    def co_lines(self, *args: Any, **kwargs: Any) -> Any: ...
    co_linetable: Any
    co_lnotab: Any
    co_name: Any
    co_names: Any
    co_nlocals: Any
    def co_positions(self, *args: Any, **kwargs: Any) -> Any: ...
    co_posonlyargcount: Any
    co_qualname: Any
    co_stacksize: Any
    co_varnames: Any
    def replace(self, /, **changes: Any) -> Any:
        """Return a copy of the code object with new values for the specified fields."""
    def __new__(cls, *args: Any, **kwargs: Any) -> CodeType: ...

@final
class CoroutineType:
    def __await__(self, /) -> Any:
        """Return an iterator to be used in await expression."""
    def __del__(self, *args: Any, **kwargs: Any) -> Any: ...
    __name__: Any
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def close(self) -> Any:
        """close() -> raise GeneratorExit inside coroutine."""
    cr_await: Any
    cr_code: Any
    cr_frame: Any
    cr_origin: Any
    cr_running: Any
    cr_suspended: Any
    def send(self, arg: Any) -> Any:
        """send(arg) -> send 'arg' into coroutine,
        return next iterated value or raise StopIteration.
        """
    @overload
    def throw(self, value: Any) -> Any:
        """throw(value)
        throw(type[,value[,traceback]])

        Raise exception in coroutine, return next iterated value or raise
        StopIteration.
        """
    @overload
    def throw(self, type: Any, value: Any = ..., traceback: Any = ...) -> Any:
        """throw(value)
        throw(type[,value[,traceback]])

        Raise exception in coroutine, return next iterated value or raise
        StopIteration.
        """

@final
class EllipsisType:
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __new__(cls, *args: Any, **kwargs: Any) -> EllipsisType: ...

@final
class FrameType:
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def clear(self, *args: Any, **kwargs: Any) -> Any:
        """F.clear(): clear most references held by the frame"""
    f_back: Any
    f_builtins: Any
    f_code: Any
    f_globals: Any
    f_lasti: Any
    f_lineno: Any
    f_locals: Any
    f_trace: Any
    f_trace_lines: Any
    f_trace_opcodes: Any

@final
class FunctionType:
    """Create a function object.

    code
      a code object
    globals
      the globals dictionary
    name
      a string that overrides the name from the code object
    argdefs
      a tuple that specifies the default argument values
    closure
      a tuple that supplies the bindings for free variables
    """
    __builtins__: Any
    def __call__(self, /, *args: Any, **kwargs: Any) -> Any:
        """Call self as a function."""
    __closure__: Any
    __code__: Any
    __defaults__: Any
    def __get__(self, instance: Any, owner: Any = ..., /) -> Any:
        """Return an attribute of instance, which is of type owner."""
    __globals__: Any
    __kwdefaults__: Any
    __name__: Any
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __new__(cls, *args: Any, **kwargs: Any) -> FunctionType: ...

@final
class GeneratorType:
    def __del__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __iter__(self, /) -> Any:
        """Implement iter(self)."""
    __name__: Any
    def __next__(self, /) -> Any:
        """Implement next(self)."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def close(self) -> Any:
        """close() -> raise GeneratorExit inside generator."""
    gi_code: Any
    gi_frame: Any
    gi_running: Any
    gi_suspended: Any
    gi_yieldfrom: Any
    def send(self, arg: Any) -> Any:
        """send(arg) -> send 'arg' into generator,
        return next yielded value or raise StopIteration.
        """
    @overload
    def throw(self, value: Any) -> Any:
        """throw(value)
        throw(type[,value[,tb]])

        Raise exception in generator, return next yielded value or raise
        StopIteration.
        """
    @overload
    def throw(self, type: Any, value: Any = ..., tb: Any = ...) -> Any:
        """throw(value)
        throw(type[,value[,tb]])

        Raise exception in generator, return next yielded value or raise
        StopIteration.
        """

@final
class GetSetDescriptorType:
    def __delete__(self, instance: Any, /) -> Any:
        """Delete an attribute of instance."""
    def __get__(self, instance: Any, owner: Any = ..., /) -> Any:
        """Return an attribute of instance, which is of type owner."""
    __name__: Any
    __objclass__: Any
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __set__(self, instance: Any, value: Any, /) -> Any:
        """Set an attribute of instance to value."""

@final
class MappingProxyType:
    def __contains__(self, key: Any, /) -> bool:
        """Return key in self."""
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __ior__(self, value: Any, /) -> Any:
        """Return self|=value."""
    def __iter__(self, /) -> Any:
        """Implement iter(self)."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __or__(self, value: Any, /) -> Any:
        """Return self|value."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __reversed__(self) -> Any:
        """D.__reversed__() -> reverse iterator"""
    def __ror__(self, value: Any, /) -> Any:
        """Return value|self."""
    def __str__(self, /) -> str:
        """Return str(self)."""
    def copy(self) -> Any:
        """D.copy() -> a shallow copy of D"""
    def get(self, k: Any, d: Any = ...) -> Any:
        """D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None."""
    def items(self) -> Any:
        """D.items() -> a set-like object providing a view on D's items"""
    def keys(self) -> Any:
        """D.keys() -> a set-like object providing a view on D's keys"""
    def values(self) -> Any:
        """D.values() -> an object providing a view on D's values"""
    def __new__(cls, *args: Any, **kwargs: Any) -> MappingProxyType: ...

@final
class MemberDescriptorType:
    def __delete__(self, instance: Any, /) -> Any:
        """Delete an attribute of instance."""
    def __get__(self, instance: Any, owner: Any = ..., /) -> Any:
        """Return an attribute of instance, which is of type owner."""
    __name__: Any
    __objclass__: Any
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __set__(self, instance: Any, value: Any, /) -> Any:
        """Set an attribute of instance to value."""

@final
class MethodDescriptorType:
    def __call__(self, /, *args: Any, **kwargs: Any) -> Any:
        """Call self as a function."""
    def __get__(self, instance: Any, owner: Any = ..., /) -> Any:
        """Return an attribute of instance, which is of type owner."""
    __name__: Any
    __objclass__: Any
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    __text_signature__: Any

@final
class MethodType:
    """Create a bound instance method object."""
    def __call__(self, /, *args: Any, **kwargs: Any) -> Any:
        """Call self as a function."""
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    __func__: Any
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    __self__: Any
    def __new__(cls, *args: Any, **kwargs: Any) -> MethodType: ...

@final
class MethodWrapperType:
    def __call__(self, /, *args: Any, **kwargs: Any) -> Any:
        """Call self as a function."""
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    __name__: Any
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    __objclass__: Any
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    __self__: Any
    __text_signature__: Any

class ModuleType:
    """Create a module object.

    The name must be a string; the optional doc argument can have any type.
    """
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""

@final
class NoneType:
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __new__(cls, *args: Any, **kwargs: Any) -> NoneType: ...

@final
class NotImplementedType:
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __new__(cls, *args: Any, **kwargs: Any) -> NotImplementedType: ...

@final
class WrapperDescriptorType:
    def __call__(self, /, *args: Any, **kwargs: Any) -> Any:
        """Call self as a function."""
    def __get__(self, instance: Any, owner: Any = ..., /) -> Any:
        """Return an attribute of instance, which is of type owner."""
    __name__: Any
    __objclass__: Any
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    __text_signature__: Any

def Aud34Action(x: Any) -> _hiero_importers_FnEdlStructures.NamedElement: ...

def AudioRangeAction(x: Any) -> list[int]: ...

def IndexedSourceElementAction(x: Any) -> list[Any]: ...

def MultipleEffectFieldAction(x: Any) -> _hiero_importers_FnEdlStructures.EffectField: ...

def NamedElementAction(x: Any) -> _hiero_importers_FnEdlStructures.NamedElement: ...

def ParseEDL(filename: Any) -> list[Any]: ...

def RetimeElementAction(x: Any) -> _hiero_importers_FnEdlStructures.RetimeElement: ...

def SingleEffectFieldAction(x: Any) -> _hiero_importers_FnEdlStructures.EffectField: ...

def SourceElementAction(x: Any) -> list[Any]: ...

def SourceModeFieldAction(x: Any) -> _hiero_importers_FnEdlStructures.ModeField: ...

def TimeCodeSpecifierAction(x: Any) -> _hiero_importers_FnEdlStructures.TimeCode: ...

def TimeCodeSubFieldSpecifierAction(x: Any) -> _hiero_importers_FnEdlStructures.TimeCode: ...

def WipeEffectFieldAction(x: Any) -> _hiero_importers_FnEdlStructures.EffectField: ...

def dump(p: Any) -> None: ...

def flatten(q: Any) -> list[Any]:
    """a recursive function that flattens a nested list q"""

BuiltinMethodType = BuiltinFunctionType
LambdaType = FunctionType
