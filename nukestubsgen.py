import os
import re
import pprint
import inspect
import pathlib
from shutil import copytree
from typing import Match, Union, Optional
from textwrap import dedent, indent
from collections import namedtuple

import nuke
from hiero import ui, core

StubsData = namedtuple('StubsData', ['builtin', 'constants', 'classes'])


class StubsRuntimeSettings:
    stubs_path = None
    nuke_extras = None
    guess = True
    log = False
    log_to_file = False
    lo_file = None

    def __new__(cls, module, path: str, class_imports_header: str, post_fixes: dict):
        cls.path = path
        cls.module = module
        cls.post_fixes = post_fixes
        cls.class_imports_header = class_imports_header

        os.makedirs(os.path.join(path, 'classes'), exist_ok=True)


def get_classes_names():
    files = []
    for path in StubsRuntimeSettings.stubs_path.glob('**/classes'):
        files.extend(file.name.replace('.py', '') for file in path.glob('[!__]*.py'))
    return files


# post fix dict structore
# file:                 file name
#    header:            change the header of a function
#       initial:        original header
#       new:            modified header
#   returns:            change a return of a function
#       function:       name of the function
#       initial:        original return
#       new:            modified return
# }

NUKE_POST_FIXES = {
    '__init__': {
        'headers': [
            {
                'initial': 'def createNode(node:str, args:list=None, inpanel:bool=None):',
                'new': 'def createNode(node:str, args:str=None, inpanel:bool=None):'
            },
            {
                'initial': "def tprint(value, sep=' ', end='\\', file=sys.stdout):",
                'new': "def tprint(value, sep=' ', end='\\n', file=sys.stdout):"
            },
            {
                'initial': "def executeBackgroundNuke(exe_path:str, nodes:list, frameRange, views:list, limits:dict, continueOnError = False, flipbookToRun = \", flipbookOptions = {}):",
                'new': "def executeBackgroundNuke(exe_path:str, nodes:list, frameRange, views:list, limits:dict, continueOnError = False, flipbookToRun = '', flipbookOptions = {}):"
            }
        ],
        'returns': [
            {
                'function': 'getNodeClassName',
                'initial': 'return None',
                'new': 'return str()'
            },
            {
                'function': 'allNodes',
                'initial': 'return list()',
                'new': 'return [Node]'
            },
            {
                'function': 'formats',
                'initial': 'return list()',
                'new': 'return [Format]'
            },
            {
                'function': 'layers',
                'initial': 'return list()',
                'new': 'return [str]'
            },
            {
                'function': 'selectedNodes',
                'initial': 'return list()',
                'new': 'return [Node]'
            }
        ]
    },
    'Node': {
        'headers': [
            {
                'initial': 'def knob(self, p:int, follow_link=None):',
                'new': 'def knob(self, p:Union[str, int], follow_link=None):'
            },
            {
                'initial': 'def dependencies(self, what:Any):',
                'new': 'def dependencies(self, what: Any=None):'
            },
            {
                'initial': 'def dependent(self, what:Any, forceEvaluate:bool):',
                'new': 'def dependent(self, what: Any=None, forceEvaluate:bool=None):'
            }
        ],
        'returns': [
            {
                'function': 'dependencies',
                'initial': 'return list()',
                'new': 'return [Node]'
            },
            {
                'function': 'dependent',
                'initial': 'return list()',
                'new': 'return [Node]'
            }
        ]
    }
}

HIERO_CORE_POST_FIX = {
    'Bin': {
        'returns': [
            {
                'function': 'importSequence',
                'initial': 'return Iterable()',
                'new': 'return core.Sequence'
            },
        ],
    },
    'Project': {
        'headers': [
            {
                'initial': 'def _Project_extractSettings(self):',
                'new': 'def extractSettings(self):'
            }
        ],
        'returns': [
            {
                'function': 'sequences',
                'initial': 'return list()',
                'new': 'return [core.Sequence]'
            },
            {
                'function': 'bins',
                'initial': 'return list()',
                'new': 'return [core.Bin]'
            },
            {
                'function': 'clips',
                'initial': 'return list()',
                'new': 'return [core.Clip]'
            },
            {
                'function': 'tracks',
                'initial': 'return list()',
                'new': 'return Union[core.VideoTrack, core.AudioTrack]'
            },
            {
                'function': 'videoTracks',
                'initial': 'return list()',
                'new': 'return [core.VideoTrack]'
            },
            {
                'function': 'audioTracks',
                'initial': 'return list()',
                'new': 'return [core.AudioTrack]'
            },
            {
                'function': 'trackItems',
                'initial': 'return list()',
                'new': 'return [core.TrackItem]'
            },
            {
                'function': 'videoTrackItems',
                'initial': 'return list()',
                'new': 'return [core.TrackItem]'
            },
            {
                'function': 'audioTrackItems',
                'initial': 'return list()',
                'new': 'return [core.TrackItem]'
            },
        ]
    }
}

HIERO_UI_POST_FIX = {}


def post_fixes(filename, func_header, func_return):
    """Make manual modifications to header and returns.

    Certain headers and returns are wrong, because of the docs or because the
    parser failed. Instead of writing a condition for each case, we can use
    `MANUAL_CHANGES` dict to create a list of modifications to are applied
    when a function is generated.

    Args:
        filename (str): the filename to check for modifications
        func_header (str): the function header.
        func_return (str): the function return.

    Returns:
        (str): the function header.
        (str): the function return.
    """
    def _debug(old, new):
        log(f'Modifying: {old} -> {new}')

    def header_mod(func_header, headers):
        """Modify the header of the function.

        Args:
            func_header (str): the current function header.
            headers (list): the list of modification to make.

        Returns:
            str: the header function
        """
        for header in headers:
            if func_header == header['initial']:

                new = header['new']
                _debug(func_header, new)
                func_header = new

        return func_header

    def return_mod(func_header, func_return, returns):
        """Modify the return of the function.

        The header is checked before, to be sure that the modification
        is for the right function.

        Args:
            func_header (str): the current function header.
            func_return (str): the current function header.
            returns (list): the list of modification to make.

        Returns:
            str: the header function
        """
        for _return in returns:
            if _return['function'] in func_header and _return['initial'] in func_return:
                new = _return['new']
                _debug(func_return, new)
                func_return = indent(new, ' ' * 4)

        return func_return

    for file, modifications in StubsRuntimeSettings.post_fixes.items():
        if filename == file:
            if modifications.get('headers'):
                func_header = header_mod(func_header, modifications['headers'])
            if modifications.get('returns'):
                func_return = return_mod(func_header, func_return,
                                         modifications['returns'])

    return func_header, func_return


def get_docs(obj: object) -> str:
    """Return the indent version of the docs."""
    return indent(f'"""\n{inspect.getdoc(obj) or ""}\n"""', ' ' * 4)


def is_valid_object(obj):
    """Check if is a valid object.

    At first method will try to check if object is callbale, if it fails will
    try to evaluate  if is simple object.
    """
    try:
        # check if return could be a callable object eg. a class
        callable(getattr(StubsRuntimeSettings.module, obj))
    except AttributeError as err:
        # if is not then check if is a valid object
        try:
            eval(obj)
        except (NameError, SyntaxError) as err:
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
        'Number': r'min|max|coordinate|range|number|time|position|height|width|scale',
        'float': r'float',
        'Node': r'^(?:(a|the)\s)?node',
        'Knob': r'^(?:(a|the)\s)?knob',
        'Callable': 'callable',
        'None': 'None'
    }

    def __init__(self, string):
        self.string = string.strip()

    def _re_search(self, pattern: str) -> Union[Match, None]:
        """Perform and return the re.search operation on pattern for self.string."""
        return re.search(pattern, self.string, re.I)

    def auto_guess(self, exclude=None) -> Union[str, None]:
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
            if exclude and match_type in exclude:
                continue

            match = self._re_search(pattern)
            if match:

                if match_type == 'union':
                    return self.is_union(match)

                if match_type == 'optional':
                    return self.is_optional()

                return match_type

        # do a last check if any type is a class Name else return 'Any'
        return next(
            (x for x in get_classes_names() if re.search(
                r'\b' + x + r'\b', self.string)), None
        )

    def is_union(self, match: re.Match) -> str:
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
            match2 = self.auto_guess(exclude=['union', match1])

        return f'Union[{match1}, {match2}]'

    def is_optional(self) -> str:
        guess_type = self.auto_guess(exclude=['optional'])
        if guess_type:
            # Using Optional from types seems to produce the same result
            # return f'Optional[{guess_type}]=""'
            return f'{guess_type}=None'

        unknown(text=self.string, _type='Optionals')
        return 'None'


class ArgsParser:
    args_regex = re.compile(r'(?<=\().+(?=\))')

    def __init__(self, fn_header: str, docs_arguments):
        self.fn_header = fn_header
        self.docs_arguments = docs_arguments

    def fix_args(self):
        """Fix/Clean some text from the arguments."""
        def is_arg_valid(arg):
            """Check if is valid argument type"""
            return is_valid_object(arg.expand(r'\1')) or 'None'

        def make_arg_title(arg):
            """Make true and false title case"""
            return arg.expand(r'\1').title()

        patterns = {
            r'(false|true)': lambda m: make_arg_title(m),
            r'(?<==)(\w+)(?=[^\.])\b': lambda m: is_arg_valid(m),
            r'\.\.\.,?': '',                   # dots
            r'/,?': '',                        # positional syntax
            r'\[,(.+)\]': r',\1=None',         # optionals
            r'(?<!\w)\[.+\]': '*args',                # list args
            r'=(?=\s+,|\s+\)|,)': '=None',     # empty args
            r'\\(\w)': r'\\\\\1',              # escape chars
        }

        for pattern, sub in patterns.items():
            self.fn_header = re.sub(pattern, sub, self.fn_header)

    def guess_data_type(self):
        """Guessed data type of arguments inside function."""
        try:
            args = self._extract_args()
        except AttributeError:
            # no arguments
            pass
        else:
            guessed_args = self._guess_args(args)
            if guessed_args:
                return self.args_regex.sub(guessed_args, self.fn_header)

        return self.fn_header

    def _extract_args(self) -> str:
        """Check if function header has any arguments and return them.
        if none are found return None.
        """
        args = self.args_regex.search(self.fn_header).group()
        return [_.strip() for _ in args.split(',')]

    @ staticmethod
    def _annotation_syntax(_type: str) -> str:
        """Return type wrapped in proper annotation syntax.

        If _type is optional return `=None` else` :type`
        """
        return f'={_type}' if _type == 'None' else f':{_type}'

    def _guess_args(self, args: list) -> Union[str, None]:
        """Try guessing args data type based on documentation text."""

        docs_args = self.docs_arguments
        if not docs_args:
            return None

        for arg in args:
            if arg in docs_args:

                guessed_type = GuessType(docs_args[arg]).auto_guess()

                if not guessed_type:
                    unknown(_type='Args', args=self._extract_args(),
                            arg=arg, value=docs_args[arg])
                    continue

                index = args.index(arg)
                arg = self._annotation_syntax(guessed_type)

                # remove and replace the argument with the guessed one
                args.insert(index, f'{args.pop(index)}{arg}')

        return ', '.join(args)


class ReturnExtractor:
    def __init__(self, header_obj):
        self.header_obj = header_obj

    @ staticmethod
    def _guess_type(text):
        return GuessType(text).auto_guess(exclude='optional')

    def _get_return(self) -> str:
        """Parse the return value from the docs if any."""
        if not StubsRuntimeSettings.guess:
            return 'Any'

        # 1. search for the return argument inside the docs
        if self.header_obj.return_argument:
            return_value = self._guess_type(self.header_obj.return_argument)
            if return_value:
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
            return 'None'
        else:
            # a list of object that should not be valid even if nuke this that are
            not_valid = ['name']

            if is_valid_object(return_value) and return_value not in not_valid:
                return return_value

            last_check = self._guess_type(return_value)
            if last_check:
                return last_check

            unknown(_type='Returns', function=self.header_obj.obj.__name__, value=return_value)
            return 'Any'

    @ staticmethod
    def _make_callable(text: str) -> str:
        """Make a return callable to propagate the offer auto complete for this obj.

        Values that should not have a parenthesis call like: Any, None,
        True/False and so on are excluded.
        """
        return text if re.search(r'(Any|None|True|])', text) else f'{text}()'

    def extract(self) -> str:
        """Extract function return from documentation."""
        return indent(f'return {self._make_callable(self._get_return())}', ' ' * 4)


class FunctionObject:
    def __init__(self, obj, fallback_name, is_class):
        """Init method of the FunctionObject.

        Args:
            obj (object): the object to be parsed for the header
            fallback_name (str): object name to fallback in case there is no header
            is_class (bool, optional): flag that function is a class method. Defaults to False.
        """
        self._obj = obj
        self._fallback_name = fallback_name
        self._is_class = is_class

    @ property
    def obj(self) -> object:
        # TODO: this fails if object has no __dict__ or __name__
        try:
            self._obj.__name__
        except AttributeError:
            self._obj.__dict__.setdefault('__name__', self._fallback_name)

        return self._obj

    @ property
    def is_class(self) -> bool:
        return self._is_class

    @ property
    def docs(self) -> str:
        return inspect.getdoc(self._obj) or ''

    @ property
    def docs_arguments(self) -> Union[dict, None]:
        docs_args = re.findall(
            r'(?<=(?:@|:)param(?:\s|:))(?:\s?)(\w+)(?:\:|\s)(.+)',
            self.docs)
        return dict(docs_args) or None

    @ property
    def return_argument(self) -> Union[re.Match, None]:
        try:
            return re.search(r'(?<=(?:@|:)return:)(.+)', self.docs).group()
        except AttributeError:
            return None

    @ property
    def header(self):
        fn_header = FnHeaderExtractor(self).extract()

        args_parser = ArgsParser(fn_header, self.docs_arguments)
        args_parser.fix_args()

        return (
            args_parser.guess_data_type()
            if StubsRuntimeSettings.guess else args_parser.fn_header
        )

    @ property
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
        return f'def {self.obj_name}(*args, **kwargs):'

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
                return f'@property\ndef {self.obj_name}(self) -> Any:'

            if inspect.ismethoddescriptor(self.obj):
                return self.simple_header()

            return self._unknown_header(err)

        except Exception as err:
            return self._unknown_header(err)

    def _unknown_header(self, err: Optional[Exception] = '') -> str:
        # most likely some dunder methods that can be safely ignored
        log(
            f'Failed to extract func header for {self.obj_name}. '
            f'Fallback on object name. Traceback: {err}'
        )
        return self.simple_header()


def func_constructor(header_obj: FunctionObject, _id) -> str:
    """Construct the function body.

    Args:
        header_obj (FunctionObject): FunctionObject data type

    Returns:
        [type]: string representation of the function body.
    """

    func_header, func_return = post_fixes(_id, header_obj.header, header_obj.return_)

    return f'{func_header}\n{get_docs(header_obj.obj)}\n{func_return}\n\n'


class ClassExtractor:
    def __init__(self, obj):
        self.obj = obj
        self.class_name = self.obj.__name__
        self.class_parent = self.obj.__base__.__name__

    def write(self):
        with open(StubsRuntimeSettings.path / 'classes' / f'{self.class_name}.py', 'w') as file:
            file.write(self._class_file())

    def _class_file(self):
        return dedent("""
        from numbers import Number
        from typing import *

        {}
        from . import *

        {}
        {}
        {}
        """).format(
            StubsRuntimeSettings.class_imports_header,
            f'class {self.class_name}({self.class_parent}):',
            get_docs(self.obj),
            self._get_class_methods()
        ).strip()

    def _get_class_methods(self) -> str:
        """Extract class methods."""
        def fix_dict(_dict: dict) -> dict:
            """Clean dictionary from certain keys and add __init__ if missing.

            When __init__ is missing, it could create auto complete problems,
            so it must be added.

            Args:
                _dict (dict): the dictionary to clean
            """
            dummy_class = type('dummy', (object,), {})
            _dict.setdefault('__init__', dummy_class.__init__)

            not_include = ['__module__', '__doc__']
            for i in not_include:
                _dict.pop(i, '')
            return _dict

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


def parse_modules():
    """Parse the nuke object from Nuke python interpret."""

    builtin = ''
    constants = ''
    classes = ''

    for attr in dir(StubsRuntimeSettings.module):
        obj = getattr(StubsRuntimeSettings.module, attr)

        if inspect.isclass(obj):
            log('Class:', attr)
            classes += f'from .{attr} import {attr}\n'
            ClassExtractor(obj).write()

        elif inspect.isbuiltin(obj):
            log('Built-in method:', attr)
            builtin += func_constructor(FunctionObject(obj, attr, False),
                                        '__init__')

        elif attr.isupper():
            log('Constants:', attr)
            constants += f'{attr} = {repr(obj)}\n'

        elif attr == 'env':
            constants += f"env = {repr({k: '' for k, _ in obj.items()})}"

    return StubsData(builtin, constants, classes)


def get_nuke_included_modules():
    """Get included modules inside plugins path.

    - nukescripts
    - nuke_internal
    - ocionuke
    """
    def fix_nukescripts():
        """Import the correct module for nukescripts."""
        nukescripts_path = StubsRuntimeSettings.path / 'nukescripts'
        for file in nukescripts_path.glob('*.py'):
            with open(file, 'r+', encoding='utf-8') as f:
                content = f.read()
                sub = re.sub('import nuke_internal as nuke',
                             'import nuke', content)
                f.seek(0)
                f.write(sub)
                f.truncate()

    def fix_init():
        """Clean nuke_internal __init__."""
        nuke_internal_init = os.path.join(
            StubsRuntimeSettings.path, 'nuke_internal', '__init__.py'
        )

        with open(nuke_internal_init, 'r') as file:
            contents = re.finditer(r'(^(from|#).+)', file.read(), re.M)

        with open(nuke_internal_init, 'w') as file:
            file.seek(0)
            for i in contents:
                file.write(i.group(1) + '\n')

    for path in nuke.pluginPath():
        for module in StubsRuntimeSettings.nuke_extras:
            src = os.path.join(path, module)
            if os.path.exists(src):
                print(f'  Internal module copied: {module}')
                destination = (
                    StubsRuntimeSettings.path / module
                    if module == 'nuke_internal' else StubsRuntimeSettings.stubs_path / module
                )
                copytree(src, str(destination), dirs_exist_ok=True)

    fix_init()
    fix_nukescripts()


def generate_nuke_stubs():
    """Generate stubs for the `nuke` module."""
    print('Generate Nuke Stubs...')
    StubsRuntimeSettings(
        module=nuke,
        path=StubsRuntimeSettings.stubs_path / 'nuke',
        class_imports_header='import nuke',
        post_fixes=NUKE_POST_FIXES
    )
    get_nuke_included_modules()

    stubs_data = parse_modules()

    init_file = dedent("""
    '''Stubs generated automatically from Nuke's internal interpreter.'''
    from numbers import Number
    from typing import *

    from .classes import *
    from .nuke_internal import *

    # Constants
    {}

    # Built-in methods
    {}
    """).format(stubs_data.constants, stubs_data.builtin).strip()
    print('  Generating __init__.py')
    with open(StubsRuntimeSettings.path / '__init__.py', 'w') as file:
        file.write(init_file)

    print('  Generating class imports.')
    with open(StubsRuntimeSettings.path / 'classes' / '__init__.py', 'w') as file:
        file.write(stubs_data.classes)


def get_hiero_included_modules(path):
    import PySide2
    site_packages = pathlib.Path(PySide2.__file__).parent.parent
    hiero = site_packages / 'hiero'
    if hiero.exists():
        print('  Internal module copied: hiero')
        copytree(str(hiero), str(path), dirs_exist_ok=True)


def generate_hiero_stubs():
    print('Generate Hiero Stubs...')

    def generate_stubs(module, module_name, post_fixes):
        imports_header = dedent('''
        import ui
        import core
        import typing
        import PySide2
        from PySide2.QtWidgets import *
        from PySide2.QtCore import Signal
        ''')
        StubsRuntimeSettings(
            module=module,
            path=path / module_name,
            post_fixes=post_fixes,
            class_imports_header=imports_header
        )

        builtin, constants, class_imports = parse_modules()

        init_file = dedent("""
        '''Stubs generated automatically from Nuke's internal interpreter.'''
        import ui
        import core
        from typing import *
        from numbers import Number
        from .classes import *

        # Constants
        {}
        # Built-in methods
        {}
        """).format(constants, builtin).strip()
        print(f'  {module_name}: Generating __init__.py')
        with open(StubsRuntimeSettings.path / '__init__.py', 'a') as file:
            file.write(init_file)

        print(f'  {module_name} Generating class imports.')
        with open(StubsRuntimeSettings.path / 'classes' / '__init__.py', 'w') as file:
            file.write(class_imports)

    path = StubsRuntimeSettings.stubs_path / 'hiero'
    get_hiero_included_modules(path)
    generate_stubs(core, 'core', HIERO_CORE_POST_FIX)
    generate_stubs(ui, 'ui', HIERO_UI_POST_FIX)


def unknown(**kwargs):
    log(f'  Unknown type: {pprint.pformat(kwargs, indent=4, width=120)}')


def log(*args, **kwargs):
    if StubsRuntimeSettings.log_to_file:
        with open(StubsRuntimeSettings.log_file, 'a') as log:
            log.write(' '.join(args) + '\n')

    if StubsRuntimeSettings.log:
        print(*args, **kwargs)


def main():
    stubs_path = pathlib.Path(
        os.path.join(os.path.expanduser('~'), '.nuke', 'nuke-python-stubs', 'stubs')
    )
    os.makedirs(stubs_path, exist_ok=True)
    StubsRuntimeSettings.stubs_path = stubs_path

    if StubsRuntimeSettings.log_to_file:
        StubsRuntimeSettings.log_file = stubs_path.parent / 'nukestubsgen.log'
        with open(StubsRuntimeSettings.log_file, 'w') as file:
            file.write('')

    print('Start Extraction')
    generate_nuke_stubs()
    generate_hiero_stubs()
    print(f'Extraction completed in: "{stubs_path}"')


if __name__ == '__main__':
    StubsRuntimeSettings.log = False
    StubsRuntimeSettings.log_to_file = False
    StubsRuntimeSettings.nuke_extras = ('nuke_internal', 'nukescripts', 'ocionuke')
    main()
