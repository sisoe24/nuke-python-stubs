from __future__ import annotations

import os
import re
import pprint
import random
import inspect
import logging
import pathlib
from types import ModuleType
from shutil import copytree
from typing import (Any, Dict, List, Type, Match, Union, Callable, Iterable,
                    Optional, NamedTuple)
from textwrap import dedent, indent

import nuke
from hiero import ui, core


class StubsData(NamedTuple):
    builtin: str
    constants: str
    classes: str


STUBS_PATH = pathlib.Path().home() / '.nuke' / 'nuke-python-stubs' / 'stubs'
STUBS_PATH.mkdir(parents=True, exist_ok=True)

LOG_FILE = STUBS_PATH.parent / 'nukestubsgen.log'
LOG_FILE.write_text('')

PostFixes = Dict[str, List[Dict[str, str]]]


def _setup_logger():

    logger = logging.getLogger(__name__ + str(random.randint(0, 100000)))
    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    def console_handler():
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
        return handler

    def file_handler():
        handler = logging.FileHandler(LOG_FILE)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
        return handler

    logger.addHandler(console_handler())
    logger.addHandler(file_handler())

    return logger


def _log_unknown_type(**kwargs: Any):
    """Log unknown types."""
    LOGGER.debug('  Unknown type: %s', {pprint.pformat(kwargs, indent=4, width=120)})


LOGGER = _setup_logger()


class RuntimeSettings:
    guess: bool = True

    def __new__(
        cls,
        module: ModuleType,
        path: pathlib.Path,
        class_imports_header: str,
        post_fixes: PostFixes
    ):
        cls.path = path
        cls.module = module
        cls.post_fixes = post_fixes
        cls.class_imports_header = class_imports_header

        os.makedirs(os.path.join(path, 'classes'), exist_ok=True)


def get_classes_names() -> list[str]:
    files: List[str] = []
    for path in STUBS_PATH.glob('**/classes'):
        files.extend(file.name.replace('.py', '') for file in path.glob('[!__]*.py'))
    return files


NUKE_POST_FIXES = {
    '__init__': [
        {
            'old': r'def createNode\(.+',
            'new': 'def createNode(node:str, args:Optional[str] = None, inpanel:Optional[bool] = None) -> Node:'
        },
        {
            'old': r'def tprint\(.+',
            'new': "def tprint(value, sep=' ', end='\\n', file=sys.stdout) -> None:"
        },
        {
            'old': r'def executeBackgroundNuke\(.+',
            'new': "def executeBackgroundNuke(exe_path:str, nodes:list, frameRange, views:list, limits:dict, continueOnError = False, flipbookToRun = '', flipbookOptions = {}) -> int:"
        },
        {
            'old': r'def allNodes\(.+',
            'new': 'def allNodes(filter: Optional[str] = None, group: Optional[str] = None) -> list[Node]:'
        },
        {
            'old': r'def formats\(.+',
            'new': 'def format() -> list[Format]:'
        },
        {
            'old': r'def layers\(.+',
            'new': 'def layers(node: Optional[Any] = None) -> list[str]:'
        },
        {
            'old': r'def selectedNodes\(.+',
            'new': 'def selectedNodes(filter:Optional[str] = None) -> list[Node]:'
        }
    ],
    'Node': [
        {
            'old': r'def knob\(.+',
            'new': 'def knob(self, p:Union[str, int], follow_link=None):'
        },
        {
            'old': r'def dependencies\(.+',
            'new': 'def dependencies(self, what: Any=None) -> list[Node]:'
        },
        {
            'old': r'def dependent\(.+',
            'new': 'def dependent(self, what: Any=None, forceEvaluate:bool=None) -> list[Node]:'
        },
        {
            'old': r'def rootNode\(.+',
            'new': 'def rootNode(self) -> Node:'
        },
        {
            'old': r'def allKnobs\(.+',
            'new': 'def allKnobs(self) -> list[Knob]:'
        },
        {
            'old': r'def knobs\(.+',
            'new': 'def knobs(self) -> dict[str, Knob]:'
        }
    ]
}

HIERO_CORE_POST_FIX = {
    '__init__': [
        {
            'old': r'def conformer\(.+',
            'new': 'def conformer() -> Conformer:'
        },
        {
            'old': r'def project\(.+',
            'new': 'def project(arg__1: str) -> Project:'
        },
        {
            'old': r'def projects\(.+',
            'new': 'def projects(*args, **kwargs) -> Tuple[Project, ...]:'
        },
        {
            'old': r'def activeSequence\(.+',
            'new': 'def activeSequence() -> hiero.core.Sequence:'
        }
    ],
    'VideoTrack': [
        {
            'old': r'def _VideoTrack_addToNukeScript\(.+',
            'new': 'def addToNukeScript(self, script: hiero.core.nuke.ScriptWriter, additionalNodes=list, disconnected=False, includeAnnotations=False, includeEffects=True):'
        },
        {
            'old': r'def items\(.+',
            'new': 'def items(self) -> Tuple[hiero.core.TrackItem, ...]:'
        },
        {
            'old': r'def addTrackItem\(.+',
            'new': 'def addTrackItem(self, clip: hiero.core.Clip, position: Optional[int] = None) -> hiero.core.TrackItem:'
        }
    ],
    'Sequence': [
        {
            'old': r'def _Sequence_addToNukeScript\(.+',
            'new': 'def addToNukeScript(self, script: hiero.core.nuke.ScriptWriter, additionalNodes=list, disconnected=False, masterTrackItem=None, includeAnnotations=False, includeEffects=True, outputToFormat=None):'
        },
        {
            'old': r'def _addClip\(.+',
            'new': 'def addClip(self, clip: Clip, time: int|float, videoTrackIndex=0, audioTrackIndex=-1) -> list[core.TrackItem]:'
        },
        {
            'old': r'def videoTracks\(.+',
            'new': 'def videoTracks(self) -> Tuple[core.VideoTrack, ...]:'
        },
        {
            'old': r'def items\(.+',
            'new': 'def items(self) -> tuple[hiero.core.VideoTrack, hiero.core.AudioTrack]:',
        }
    ],
    'Clip': [
        {
            'old': r'def _Clip_addAnnotationsToNukeScript\(.+',
            'new': 'def addAnnotationsToNukeScript(self, script, firstFrame, trimmed, trimStart=None, trimEnd=None):'
        },
        {
            'old': r'def _Clip_getReadInfo\(.+',
            'new': 'def getReadInfo(self, firstFrame=None):'
        },
        {
            'old': r'def _Clip_addToNukeScript\(.+',
            'new': 'def addToNukeScript(self, script: hiero.core.nuke.ScriptWriter, additionalNodes=list, additionalNodesCallback=None, firstFrame=None, trimmed=True, trimStart=None, trimEnd=None, colourTransform=None, metadataNode=None, includeMetadataNode=True, nodeLabel=None, enabled=True, includeEffects=True, beforeBehaviour=None, afterBehaviour=None, project=None, readNodes={}, addEffectsLifetime=True):'
        }
    ],
    'EffectTrackItem': [
        {
            'old': r'def _EffectTrackItem_addToNukeScript\(.+',
            'new': 'def addToNukeScript(self, script: hiero.core.nuke.ScriptWriter, offset=0, inputs=1, startHandle=0, endHandle=0, addLifetime=True):'
        },
        {
            'old': r'def _EffectTrackItem_isRetimeEffect\(.+',
            'new': 'def isRetimeEffect(self) -> bool:'
        },
        {
            'old': r'def __EffectTrackItem_name\(.+',
            'new': 'def name(self) -> str:'
        },
        {
            'old': r'def __EffectTrackItem_setName\(.+',
            'new': 'def setName(self, name: str):'
        }
    ],
    'TrackItem': [
        {
            'old': r'def source\(.+',
            'new': 'def source(self) -> Clip | Sequence | MediaSource: '
        },
        {
            'old': r'def __TrackItem_unlinkAll\(.+',
            'new': 'def unlinkAll(self):'
        },
        {
            'old': r'def _TrackItem_addToNukeScript\(.+',
            'new': 'def addToNukeScript(self, script: hiero.core.nuke.ScriptWriter, firstFrame=None, additionalNodes=[], additionalNodesCallback=None, includeRetimes=False, retimeMethod=None, startHandle=None, endHandle=None, colourTransform=None, offset=0, nodeLabel=None, includeAnnotations=False, includeEffects=True, outputToSequenceFormat=False):'
        },
        {
            'old': r'def thumbnail\(.+',
            'new': 'def thumbnail(self, index: int = 0, layer: str = None) -> PySide2.QtGui.QImage:'
        }
    ],
    'Bin': [
        {
            'old': r'def importSequence\(.+',
            'new': 'def importSequence(self, filename: str, timeBase: core.TimeBase, frameRate: float = 0.0, dropFrame: bool = False) -> core.Sequence: '
        },
    ],
    'Project': [
        {
            'old': r'def _Project_extractSettings\(.+',
            'new': 'def extractSettings(self) -> dict[str, str]:'
        },
        {
            'old': r'def setOutputFormat\(.+',
            'new': 'def setOutputFormat(self, format: hiero.core.Format) -> None:'
        },
        {
            'old': r'def sequences\(.+',
            'new': 'def sequences(self, partialNam: Optional[str]=None) -> list[core.Sequence]:'
        },
        {
            'old': r'def clips\(.+',
            'new': 'def clips(self, partialName: Optional[str]=None) -> list[core.Clip]:'
        },
        {
            'old': r'def bins\(.+',
            'new': 'def bins(self, partialName: Optional[str]=None) -> list[core.Bin]:'
        },
        {
            'old': r'def tracks\(.+',
            'new': 'def tracks(self, partialName: Optional[str]=None) -> list[core.Track]:'
        },
        {
            'old': r'def videoTracks\(.+',
            'new': 'def videoTracks(self, partialName: Optional[str]=None) -> list[core.VideoTrack]:'
        },
        {
            'old': r'def audioTracks\(.+',
            'new': 'def audioTracks(self, partialName: Optional[str]=None) -> list[core.AudioTrack]:'
        },
        {
            'old': r'def trackItems\(.+',
            'new': 'def trackItems(self, partialName: Optional[str]=None) -> list[core.TrackItem]:'
        },
        {
            'old': r'def videoTrackItems\(.+',
            'new': 'def videoTrackItems(self, partialName: Optional[str] = None) -> list[core.TrackItem]:'
        },
        {
            'old': r'def audioTrackItems\(.+',
            'new': 'def audioTrackItems(self, partialName: Optional[str] = None) -> list[core.TrackItem]:'
        }
    ],
}

HIERO_UI_POST_FIX = {
    '__init__': [
        {
            'old': r'def activeSequence\(.+',
            'new': 'def activeSequence() -> hiero.core.Sequence:'
        },
        {
            'old': r'def getTimelineEditor\(.+',
            'new': 'def getTimelineEditor(sequence: hiero.core.Sequence, creationFlag: Optional[hiero.ui.TimelineEditorCreationFlag] = None) -> hiero.ui.TimelineEditor:'
        }
    ],
}

GLOBAL_POST_FIXES = [
    {
        'old': r'\(Object\):',
        'new': ':',
    },
]


def post_fixes(filename: str, old_header: str):
    """Make manual modifications to header and returns.

    Certain headers and returns are wrong, because of the docs or because the
    parser failed. Instead of writing a condition for each case, we can use
    `MANUAL_CHANGES` dict to create a list of modifications to are applied
    when a function is generated.

    Args:
        filename (str): the filename to check for modifications
        func_header (str): the function header to check for modifications

    """

    def header_mod(func_header: str, mods: List[dict[str, Union[str, str]]]):
        """Modify the header of the function.

        Args:
            func_header (str): the current function header.
            headers (list): the list of modification to make.

        Returns:
            str: the header function
        """
        for mod in mods:

            if re.search(mod['old'], func_header):
                new = mod['new']
                LOGGER.debug('    Post-Mod: %s -> %s', func_header, new)
                func_header = new

        return func_header

    for file, modifications in RuntimeSettings.post_fixes.items():
        if filename == file and modifications:
            old_header = header_mod(old_header, modifications)

    return old_header


def global_post_fixes():
    for file in STUBS_PATH.glob('**/*.py'):
        with open(file, 'r') as f:
            content = f.read()

        for fix in GLOBAL_POST_FIXES:
            content = re.sub(fix['old'], fix['new'], content)

        with open(file, 'w') as f:
            f.write(content)


def get_docs(obj: object) -> str:
    """Return the indent version of the docs."""
    docs = inspect.getdoc(obj) or ''
    return indent(f'"""\n{docs}\n"""', ' ' * 4)


def is_valid_object(obj: str) -> Optional[str]:
    """Check if is a valid object.

    At first method will try to check if object is callbale, if it fails will
    try to evaluate  if is simple object.
    """
    LOGGER.debug('      Trying to validate object: %s', obj)
    try:
        # check if return could be a callable object eg. a class
        callable(getattr(RuntimeSettings.module, obj))
    except AttributeError as err:
        # if is not then check if is a valid object
        LOGGER.debug('        Invalid object: %s', err)

        try:
            eval(obj)
        except (NameError, SyntaxError) as err:
            LOGGER.debug('        Second check (eval) failed: %s', err)
            # some returns are descriptions, so return None
            return None

    return obj


class GuessType:
    """Guess data type based on regex match.

    This method is obviously not precise and it depends on the order of calls but
    is good enough for the job.
    """
    types_match = {
        'optional': r'optional.+',
        'union': r'^(\w+) or (\w+)',
        'list': r'list|array',
        'tuple': r'tuple',
        'int': r'\b(int|integer|index|frame|i\'th|\d)\b',
        'str': r'\b(str|string|class|prompt|clipboard|message|name|label|tooltip|text|file(\w+)?|path|code|script|shortcut|title)\b',
        'bool': r'bool|true|false',
        'dict': r'dict',
        'Iterable': r'sequence|(\(|\[)\w+, \w+(\)|\])',
        'int|float': r'min|max|coordinate|range|number|time|position|height|width|scale',
        'float': r'float',
        'Node': r'^(?:(a|the)\s)?node',
        'Knob': r'^(?:(a|the)\s)?knob',
        'Callable': 'callable',
        'None': 'None'
    }

    def __init__(self, string: str):
        self.string = string.strip()

    def _re_search(self, pattern: str) -> Union[Match[str], None]:
        """Perform and return the re.search operation on pattern for self.string."""
        return re.search(pattern, self.string, re.I)

    def auto_guess(self, exclude: Optional[Iterable[str]] = None) -> Union[str, None]:
        """Auto guess type based on all of the regex pattern inside `types_match`.

        Args:
            exclude (list): Optional list to exclude matches.
        """

        # XXX: running match classes BEFORE guess, produces slightly better results on hiero
        # but worst on nuke.
        # for x in get_classes_names():
        #     if re.search(r'\b' + x + r'\b', self.string):
        #         return x

        for match_type, pattern in self.types_match.items():

            LOGGER.debug('      Checking: %s', match_type)

            if exclude and match_type in exclude:
                continue

            match = self._re_search(pattern)
            if match:

                if match_type == 'union':
                    LOGGER.debug('      Checking union: %s', self.string)
                    return self.is_union(match)

                if match_type == 'optional':
                    LOGGER.debug('      Checking optional: %s', self.string)
                    return self.is_optional()

                LOGGER.debug('       * Guessed: %s', match_type)

                return match_type

        # do a last check if any type is a class Name else return 'Any'
        return next(
            (x for x in get_classes_names() if re.search(
                r'\b' + x + r'\b', self.string)), None
        )

    def is_union(self, match: re.Match[str]) -> str:
        """Deal with Union arguments; int or str.

        Method will try to check if is a valid object. If that will fail will try
        guessing with the internal method.
        """
        match1 = is_valid_object(match[1])
        match2 = is_valid_object(match[2])

        # try second guess
        if not match1:
            match1 = self.auto_guess(exclude=['union'])

        if not match2:
            # must add match1 to exclude to avoid matching the same type twice
            match2 = self.auto_guess(exclude=['union', match1 or ''])

        return f'Union[{match1}, {match2}]'

    def is_optional(self) -> str:
        guess_type = self.auto_guess(exclude=['optional'])
        if guess_type:
            return f'Optional[{guess_type}] = None'

        _log_unknown_type(text=self.string, _type='Optionals')
        return 'None'


class ArgsParser:
    args_regex = re.compile(r'(?<=\().+(?=\))')

    def __init__(self, fn_header: str, docs_arguments: Optional[Dict[str, str]] = None):
        self.fn_header = fn_header
        self.docs_arguments = docs_arguments

    def fix_args(self):
        """Fix/Clean some text from the arguments."""
        patterns: Dict[str, Union[str, Callable[[Match[str]], str]]] = {
            r'(false|true)': lambda m: m.expand(r'\1').title(),
            r'(?<==)(\w+)(?=[^\.])\b': lambda m: is_valid_object(m.expand(r'\1')) or 'None',
            r'\.\.\.,?': '',                   # dots
            r'/,?': '',                        # positional syntax
            r'\[,(.+)\]': r',\1=None',         # optionals
            r'(?<!\w)\[.+\]': '*args',         # list args
            r'=(?=\s+,|\s+\)|,)': '=None',     # empty args
            r'\\(\w)': r'\\\\\1',              # escape chars
        }

        for pattern, sub in patterns.items():
            self.fn_header = re.sub(pattern, sub, self.fn_header)

    def guess_data_type(self):
        """Guessed data type of arguments inside function."""
        LOGGER.debug('    Guessing type for header: %s', self.fn_header)
        try:
            args = self._extract_args()
            LOGGER.debug('      Args found: %s', args)
        except AttributeError as err:
            LOGGER.debug('      No args found: %s', err)
        else:
            guessed_args = self._guess_args(args)
            if guessed_args:
                return self.args_regex.sub(guessed_args, self.fn_header)

        LOGGER.debug('      Cannot guess.')

        return self.fn_header

    def _extract_args(self) -> List[str]:
        """Check if function header has any arguments and return them.
        if none are found return None.
        """
        m = self.args_regex.search(self.fn_header)

        if not m:
            LOGGER.debug('      No arguments found in: %s', self.fn_header)
            return []

        return [_.strip() for _ in m.group().split(',')]

    @staticmethod
    def _annotation_syntax(_type: str) -> str:
        """Return type wrapped in proper annotation syntax.

        If _type is optional return `=None` else` :type`
        """
        return f'={_type}' if _type == 'None' else f':{_type}'

    def _guess_args(self, args: List[str]) -> Union[str, None]:
        """Try guessing args data type based on documentation text."""

        docs_args = self.docs_arguments
        if not docs_args:
            return None

        for arg in args:
            LOGGER.debug('    Guessing for: %s', arg)
            if arg in docs_args:
                LOGGER.debug('      Parsing doc: %s', docs_args[arg])

                guessed_type = GuessType(docs_args[arg]).auto_guess()

                if not guessed_type:
                    _log_unknown_type(_type='Args', args=self._extract_args(),
                                      arg=arg, value=docs_args[arg])
                    LOGGER.debug('      No guess found for: %s', arg)
                    continue

                index = args.index(arg)
                arg = self._annotation_syntax(guessed_type)

                # remove and replace the argument with the guessed one
                args.insert(index, f'{args.pop(index)}{arg}')

                LOGGER.debug('      Guessed types: %s', args)
                continue

            LOGGER.debug('      No guess found for: %s', arg)

        return ', '.join(args)


class ReturnExtractor:
    def __init__(self, header_obj: FunctionObject):
        self.header_obj = header_obj

    @staticmethod
    def _guess_type(text: str) -> Optional[str]:
        return GuessType(text).auto_guess(exclude='optional')

    def extract(self) -> str:
        """Parse the return value from the docs if any."""
        LOGGER.debug('    Guessing return value for: %s', self.header_obj.obj.__name__)
        if not RuntimeSettings.guess:
            return 'Any'

        # 1. search for the return argument inside the docs
        if self.header_obj.return_argument:

            # if is_valid_object(self.header_obj.return_argument):
            #     LOGGER.debug('      Found return value: %s', return_value)
            #     return self.header_obj.return_argument

            return_value = self._guess_type(self.header_obj.return_argument)
            if return_value:
                LOGGER.debug('    Guessed return value: %s', return_value)
                return return_value

        # 2. search for return value inside the function signature
        try:
            return_value = str(inspect.signature(self.header_obj.obj))
        except (TypeError, ValueError):
            return_value = None
        else:
            # skip when value is object to give it another chance of guessing
            if 'object' in return_value:
                return_value = None

        # 3. use the return value signature or search for it inside the docs
        try:
            # search for everything after `->` if any
            return_value = re.search(
                r'(?<=> ).+', return_value or self.header_obj.docs).group()

            # clean the extra last dot
            return_value = re.sub(r'\.$', '',  return_value)
        except AttributeError:
            LOGGER.debug('      No return value found for: %s',
                         self.header_obj.obj.__name__)
            return 'None'
        else:
            # a list of object that should not be valid even if nuke this that are
            not_valid = ['name']

            if is_valid_object(return_value) and return_value not in not_valid:
                LOGGER.debug('      Found return value: %s', return_value)
                return return_value

            last_check = self._guess_type(return_value)
            if last_check:
                LOGGER.debug('      Guessed return value: %s', last_check)
                return last_check

            _log_unknown_type(_type='Returns',
                              function=self.header_obj.obj.__name__, value=return_value)
            LOGGER.debug('      No return value found for: %s',
                         self.header_obj.obj.__name__)
            return 'Any'


class FunctionObject:
    def __init__(self, obj: object, fallback_name: str, is_class: bool = False):
        """Init method of the FunctionObject.

        Args:
            obj (object): the object to be parsed for the header
            fallback_name (str): object name to fallback in case there is no header
            is_class (bool, optional): flag that function is a class method. Defaults to False.
        """
        self._obj = obj
        self._fallback_name = fallback_name
        self._is_class = is_class

    @property
    def obj(self) -> object:
        # TODO: this fails if object has no __dict__ or __name__
        try:
            self._obj.__name__
        except AttributeError:
            self._obj.__dict__.setdefault('__name__', self._fallback_name)

        return self._obj

    @property
    def is_class(self) -> bool:
        return self._is_class

    @property
    def docs(self) -> str:
        return inspect.getdoc(self._obj) or ''

    @property
    def docs_arguments(self) -> Union[Dict[str, str], None]:
        docs_args = re.findall(r'(?<=[@:]param[\s:])\s?(\w+)[\s:](.+)', self.docs)
        return dict(docs_args) or None

    @property
    def return_argument(self) -> Union[str, None]:
        try:
            return re.search(r'(?<=[@:]return:)(.+)', self.docs).group()
        except AttributeError:
            return None

    @property
    def header(self):
        fn_header = FnHeaderExtractor(self).extract()

        args_parser = ArgsParser(fn_header, self.docs_arguments)
        args_parser.fix_args()

        guessing_header = args_parser.guess_data_type()
        LOGGER.debug('    Guessing header: %s', guessing_header)
        if re.search(r'\):', guessing_header):
            guessing_header = guessing_header.replace('):', f') -> {self.return_}:')

        return (
            guessing_header
            if RuntimeSettings.guess else args_parser.fn_header
        )

    @property
    def return_(self):
        return ReturnExtractor(self).extract()


class FnHeaderExtractor:

    def __init__(self, header_obj: FunctionObject):
        self.header_obj = header_obj

        self.obj = header_obj.obj
        self.obj_name = self.obj.__name__

        self.obj_docs = header_obj.docs
        self.is_class = header_obj.is_class

    def extract(self) -> str:
        """Extract function header from initial object."""
        header = self._header_constructor()

        if self.is_class:
            header = re.sub(r'(?<=\()(?!self)', 'self,', header)

        return header

    def simple_header(self) -> str:
        return f'def {self.obj_name}(*args: typing.Any, **kwargs: typing.Any):'

    def _regex_extractor(self) -> str:
        """Extract function header with regex pattern. if fails fallback on simple header.
        """
        extractor = re.compile(r'''
                ^(?:.+?\.)?            # match: `self.abc` or `abc`
                (                      # start group
                \b\w+\(                # match: `word(`
                (.+(?=\s->)|(.+)??\))  # match: everything till ` ->` or `)`
                )                      # end group
                ''', re.X)
        try:
            return f'def {extractor.search(self.obj_docs).group(1)}:'
        except AttributeError:
            # if there are no parenthesis, then return a simple header
            return self.simple_header()

    def _header_constructor(self):
        """Extract the function header.

        The method will try to get the function signature by calling inspect.
        If it fails will fallback on parsing the documentation for a line `xyz()`.
        If it fails again will create a simple function header msg(*args, **kwargs).

        If `is_class` is True, then will insert the argument `self`.

        Args:
            obj (object): object to be parsed from the inspect module.

        Returns:
            str: stringified function definition header: "def xyz():"
        """
        try:
            # Built in methods will always fail
            return f'def {self.obj_name}{inspect.signature(self.obj)}:'
        except ValueError:
            return self._regex_extractor()
        except TypeError as err:

            # properties will not be callable from inspect.signature
            # so fallback on simple header
            # XXX: this is wrong on some occasions but it shouldnt be a problem.
            if inspect.isdatadescriptor(self.obj):
                return f'@property\ndef {self.obj_name}(self) -> typing.Any:'

            if inspect.ismethoddescriptor(self.obj):
                return self.simple_header()

            return self._unknown_header(err)

        except Exception as err:
            return self._unknown_header(err)

    def _unknown_header(self, err: Optional[Exception] = '') -> str:
        # most likely some dunder methods that can be safely ignored
        LOGGER.debug('    Failed to extract func header for %s. %s', self.obj_name, err)
        return self.simple_header()


def func_constructor(header_obj: FunctionObject, file_name: str) -> str:
    """Construct the function body.

    Args:
        header_obj (FunctionObject): FunctionObject data type
        file_name (str): the file name to check for modifications

    Returns:
        [type]: string representation of the function body.
    """

    func_header = post_fixes(file_name, header_obj.header)

    dots = indent('...', ' ' * 4)
    return f'{func_header}\n{get_docs(header_obj.obj)}\n{dots}\n\n'


class ClassExtractor:
    def __init__(self, obj: Type[object]):
        self.obj = obj
        self.class_name: str = self.obj.__name__
        self.class_parent: str = self.obj.__base__.__name__

    def write(self):
        with open(RuntimeSettings.path / 'classes' / f'{self.class_name}.py', 'w') as file:
            file.write(self._class_file())

    def _class_file(self):
        return dedent("""
        {}
        from . import *

        {}
        {}
        {}
        """).format(
            RuntimeSettings.class_imports_header,
            f'class {self.class_name}({self.class_parent}):',
            get_docs(self.obj),
            self._get_class_methods()
        ).strip()

    def _get_class_methods(self) -> str:
        """Extract class methods."""

        def fix_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
            """Clean dictionary from certain keys and add __init__ if missing.

            When __init__ is missing, it could create auto complete problems,
            so it must be added.

            Args:
                _dict (dict): the dictionary to clean
            """
            dummy_class = type('dummy', (object,), {})
            d.setdefault('__init__', dummy_class.__init__)

            dont_include = ('__module__', '__doc__')
            for i in dont_include:
                d.pop(i, '')
            return d

        class_dict = fix_dict(dict(self.obj.__dict__))

        class_body = ''

        for member, obj in class_dict.items():

            # check for simple type class attributes
            if type(obj) in (float, int, str, list, tuple, set, dict, bool, frozenset):
                # TODO: obj sometimes is a string or with broken syntax
                class_body += f'{member} = {repr(obj)}\n'

            elif obj.__class__.__name__ == 'Signal':
                class_body += f'{member} = Signal()\n'
            elif (
                inspect.ismethoddescriptor(obj)
                or inspect.isfunction(obj)
                or inspect.isbuiltin(obj)
                or inspect.isgetsetdescriptor(obj)
            ):
                class_body += func_constructor(
                    FunctionObject(obj=obj, fallback_name=member, is_class=True),
                    self.class_name
                )
            else:
                class_body += f'{member}: Any = None\n'

        return indent(class_body, ' ' * 4)


def parse_modules() -> StubsData:
    """Parse the nuke object from Nuke python interpret."""

    builtin = ''
    constants = ''
    classes = ''

    for attr in dir(RuntimeSettings.module):
        obj = getattr(RuntimeSettings.module, attr)

        if inspect.isclass(obj):
            LOGGER.debug('  Class: %s', attr)
            classes += f'from .{attr} import {attr}\n'
            ClassExtractor(obj).write()

        elif inspect.isbuiltin(obj):
            LOGGER.debug('  Built-in method: %s', attr)
            builtin += func_constructor(FunctionObject(obj, attr, False), '__init__')

        elif attr.isupper():
            LOGGER.debug('  Constant: %s - %s', attr, obj)
            constants += f'{attr} = {repr(obj)}\n'

        elif attr == 'env':
            constants += f"env = {repr({k: '' for k, _ in obj.items()})}"
            LOGGER.debug('  Constant: env - %s', obj)

    return StubsData(builtin, constants, classes)


def generate_nuke_stubs():
    """Generate stubs for the `nuke` module."""
    LOGGER.info('Generate Nuke Stubs...')

    def get_nuke_included_modules():
        """Get included modules inside plugins path.
        - nukescripts
        - nuke_internal
        - ocionuke
        """
        def fix_nukescripts():
            """Import the correct module for nukescripts."""
            nukescripts_path = RuntimeSettings.path / 'nukescripts'
            for file in nukescripts_path.glob('*.py'):
                with open(file, 'r+', encoding='utf-8') as f:
                    content = f.read()
                    content = content.replace(
                        'import nuke_internal as nuke', 'import nuke')
                    f.seek(0)
                    f.write(content)
                    f.truncate()

        def fix_init():
            """Clean nuke_internal __init__."""
            nuke_internal_init = os.path.join(
                RuntimeSettings.path, 'nuke_internal', '__init__.py'
            )

            with open(nuke_internal_init, 'r') as file:
                contents = re.finditer(r'(^(from|#).+)', file.read(), re.M)

            with open(nuke_internal_init, 'w') as file:
                file.seek(0)
                for i in contents:
                    file.write(i.group(1) + '\n')

        for path in nuke.pluginPath():
            for module in ('nuke_internal', 'nukescripts', 'ocionuke'):
                src = os.path.join(path, module)
                if os.path.exists(src):
                    print(f'  Internal module copied: {module}')
                    destination = (
                        RuntimeSettings.path / module
                        if module == 'nuke_internal' else STUBS_PATH / module
                    )
                    copytree(src, str(destination), dirs_exist_ok=True)

        fix_init()
        fix_nukescripts()

    imports_header = dedent('''
    """Stubs generated automatically from Nuke's internal interpreter."""
    import nuke
    import typing
    import PySide2
    from typing import *
    from PySide2.QtWidgets import *
    ''').strip()

    RuntimeSettings(
        module=nuke,
        path=STUBS_PATH / 'nuke',
        class_imports_header=imports_header,
        post_fixes=NUKE_POST_FIXES
    )
    get_nuke_included_modules()

    stubs_data = parse_modules()

    init_file = dedent("""
    '''Stubs generated automatically from Nuke's internal interpreter.'''
    import typing
    from typing import *

    from .classes import *
    from .nuke_internal import *

    # Constants
    {}

    # Built-in methods
    {}
    """).format(stubs_data.constants, stubs_data.builtin).strip()

    LOGGER.info('  Generating __init__.py')
    with open(RuntimeSettings.path / '__init__.py', 'w') as file:
        file.write(init_file)

    LOGGER.info('  Generating class imports.')
    with open(RuntimeSettings.path / 'classes' / '__init__.py', 'w') as file:
        file.write(stubs_data.classes)


def generate_hiero_stubs():
    LOGGER.info('  Generate Hiero Stubs...')

    def get_hiero_included_modules():
        """Copy the internal hiero module to the stubs path."""
        import PySide2

        site_packages = pathlib.Path(PySide2.__file__).parent.parent
        hiero = site_packages / 'hiero'
        if hiero.exists():
            LOGGER.info('  Internal module copied: hiero')
            copytree(str(hiero), str(STUBS_PATH / 'hiero'), dirs_exist_ok=True)

    def generate_stubs(module: ModuleType, module_name: str, post_fixes: PostFixes):
        imports_header = dedent('''
        """Stubs generated automatically from Nuke's internal interpreter."""
        import ui
        import core
        import hiero
        import typing
        import PySide2
        from typing import *
        from PySide2.QtWidgets import *
        from PySide2.QtCore import Signal
        ''').strip()

        RuntimeSettings(
            module=module,
            path=STUBS_PATH / 'hiero' / module_name,
            post_fixes=post_fixes,
            class_imports_header=imports_header
        )

        builtin, constants, class_imports = parse_modules()

        init_file = dedent("""
        '''Stubs generated automatically from Nuke's internal interpreter.'''
        import ui
        import core
        import hiero
        import typing
        import PySide2

        from . import nuke
        from .classes import *
        from typing import *

        # Constants
        {}
        # Built-in methods
        {}
        """).format(constants, builtin).strip()

        LOGGER.info('  %s: Generating __init__.py', module_name)
        with open(RuntimeSettings.path / '__init__.py', 'a') as file:
            file.write(init_file)

        LOGGER.info('  %s: Generating class imports.', module_name)
        with open(RuntimeSettings.path / 'classes' / '__init__.py', 'w') as file:
            file.write(class_imports)

    get_hiero_included_modules()

    generate_stubs(core, 'core', HIERO_CORE_POST_FIX)
    generate_stubs(ui, 'ui', HIERO_UI_POST_FIX)


def nukestubsgen():

    LOGGER.info('Starting Stub Generation...')

    generate_nuke_stubs()
    generate_hiero_stubs()
    global_post_fixes()

    LOGGER.info(f'Generation completed: "{STUBS_PATH}"')


if __name__ == '__main__':
    nukestubsgen()
