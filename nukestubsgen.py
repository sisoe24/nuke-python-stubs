import os
import re
import inspect
import logging
import pathlib
from shutil import copytree
from typing import Match, Tuple, Union, Optional
from textwrap import dedent, indent

import nuke
import hiero

PATH = pathlib.Path(__file__).parent / 'nuke-python-stubs'

STUBS_PATH = PATH / 'stubs'
STUBS_PATH.mkdir(exist_ok=True)


class Options:
    module = None
    path = ''
    class_path = None
    guess_type = True


MANUAL_CHANGES = {
    '__init__': {
        'headers': [
            {
                'original_header': 'def createNode(node:str, args:list=None, inpanel:bool=None):',
                'new_header': 'def createNode(node:str, args:str=None, inpanel:bool=None):'
            },
            {
                'original_header': "def tprint(value, sep=' ', end='\\', file=sys.stdout):",
                'new_header': "def tprint(value, sep=' ', end='\\n', file=sys.stdout):"
            },
            {
                'original_header': "def executeBackgroundNuke(exe_path:str, nodes:list, frameRange, views:list, limits:dict, continueOnError = False, flipbookToRun = \", flipbookOptions = {}):",
                'new_header': "def executeBackgroundNuke(exe_path:str, nodes:list, frameRange, views:list, limits:dict, continueOnError = False, flipbookToRun = '', flipbookOptions = {}):"
            }
        ],
        'returns': [
            {
                'function_name': 'getNodeClassName',
                'original_return': 'return None',
                'new_return': 'return str()'
            },
            {
                'function_name': 'allNodes',
                'original_return': 'return list()',
                'new_return': 'return [Node]'
            },
            {
                'function_name': 'formats',
                'original_return': 'return list()',
                'new_return': 'return [Format]'
            },
            {
                'function_name': 'layers',
                'original_return': 'return list()',
                'new_return': 'return [str]'
            },
            {
                'function_name': 'selectedNodes',
                'original_return': 'return list()',
                'new_return': 'return [Node]'
            }
        ]
    },
    'Node': {
        'headers': [
            {
                'original_header': 'def knob(self, p:int, follow_link=None):',
                'new_header': 'def knob(self, p:Union[str, int], follow_link=None):'
            },
            {
                'original_header': 'def dependencies(self, what):',
                'new_header': 'def dependencies(self, what=None):'
            },
            {
                'original_header': 'def dependent(self, what, forceEvaluate:bool):',
                'new_header': 'def dependent(self, what=None, forceEvaluate:bool=None):'
            }
        ],
        'returns': [
            {
                'function_name': 'dependencies',
                'original_return': 'return list()',
                'new_return': 'return [Node]'
            },
            {
                'function_name': 'dependent',
                'original_return': 'return list()',
                'new_return': 'return [Node]'
            }
        ]
    }
}


def manual_mods(filename, func_header, func_return):
    """Make manual modifications to header and returns.

    Certain headers and returns are wrong, because of the docs or because the
    parser failed. Instead of writing a condition for each case, the file
    `manual_changes.json` can be used to create a list of modifications to make
    at each function generated.

    Args:
        filename (str): the filename to check for modifications
        func_header (str): the function header.
        func_return (str): the function return.

    Returns:
        (str): the function header.
        (str): the function return.
    """
    def _debug(old, new):
        logging.debug('Modifying: %s -> %s', old, new)

    def header_mod(func_header, headers):
        """Modify the header of the function.

        Args:
            func_header (str): the current function header.
            headers (list): the list of modification to make.

        Returns:
            str: the header function
        """
        for header in headers:
            if func_header == header['original_header']:

                new_header = header['new_header']
                _debug(func_header, new_header)
                func_header = new_header

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
            # I am checking `in` because some functions could be indented so
            # `x` does not match `    x`.
            if (_return['function_name'] in func_header and
                    _return['original_return'] in func_return):

                new_return = _return['new_return']
                _debug(func_return, new_return)
                func_return = indent(new_return, ' ' * 4)

        return func_return

    for file, modifications in MANUAL_CHANGES.items():
        if filename == file:
            func_header = header_mod(func_header, modifications['headers'])
            func_return = return_mod(func_header, func_return,
                                     modifications['returns'])

    return func_header, func_return


def get_included_modules():
    """Get included modules inside plugins path.

    - nukescripts
    - nuke_internal
    - ocionuke
    """
    def clean_nukescripts():
        """Import the correct module for nukescripts."""
        nukescripts_path = Options.path / 'nukescripts'
        for file in nukescripts_path.glob('*.py'):
            with open(file, 'r+', encoding='utf-8') as f:
                content = f.read()
                sub = re.sub('import nuke_internal as nuke',
                             'import nuke', content)
                f.seek(0)
                f.write(sub)
                f.truncate()

    def clean_init():
        """Clean nuke_internal __init__."""
        nuke_internal_init = os.path.join(
            Options.path, 'nuke_internal', '__init__.py')

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
                print(f'Internal module copied: {module}')
                destination = Options.path / module if module == 'nuke_internal' else STUBS_PATH / module
                copytree(src, str(destination), dirs_exist_ok=True)

    clean_init()
    clean_nukescripts()


def log_unguessed(name, arg, guarg):
    pass

    # print("➡ name :", name, arg, guarg)


def indented_docs(obj: object) -> str:
    """Return the indent version of the docs."""
    return indent(f'"""\n{get_docs(obj)}\n"""', ' ' * 4)


def get_docs(obj: object) -> str:
    """Return object docs or empty string if there are none"""
    return inspect.getdoc(obj) or ''


def is_valid_object(obj):
    """Check if is a valid object.

    At first method will try to check if object is callbale, if it fails will
    try to evaluate  if is simple object.
    """
    try:
        # check if return could be a callable object eg. a class
        callable(getattr(Options.module, obj))
    except AttributeError as err:
        # if is not then check if is a valid object
        try:
            eval(obj)
        except (NameError, SyntaxError) as err:
            # some returns are descriptions, so return Any

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
        'int': r'\b(int|integer|index|i\'th|\d)\b',
        'str': r'\b(str|string|class|prompt|message|name|label|tooltip|text|file(\w+)?|path|code|script|shortcut|title)\b',
        'bool': r'bool|true|false',
        'dict': r'dict',
        'Iterable': r'sequence|(\(|\[)\w+, \w+(\)|\])',
        'Number': r'min|max|coordinate|range|number|frame|time|position|height|width|scale',
        'float': r'float',
        'Any': r'value',
        'Node': r'^(?:(a|the)\s)?node',
        'Knob': r'^(?:(a|the)\s)?knob',
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
        for _type, pattern in self.types_match.items():
            if exclude and _type in exclude:
                continue

            match = self._re_search(pattern)
            if match:

                if _type == 'union':
                    return self.is_union(match)

                if _type == 'optional':
                    return self.is_optional(match)

                return _type

        return None

    def is_type(self, _type: str) -> Union[str, None]:
        """Check if string matches argument.

        Args:
            _type (str): type to check for.
        """
        return self._re_search(self.types_match[_type])

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

    def is_optional(self, match: re.Match) -> str:
        guess_type = self.auto_guess(exclude=['optional'])
        if guess_type:
            # Using Optional from types seems to produce the same result
            # return f'Optional[{guess_type}]=""'
            return f'{guess_type}=None'

        log_unguessed('Optionals', match.group(), guess_type)
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
            r'\[.+\]': '*args',                # list args
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

    @staticmethod
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
                    log_unguessed('Args', arg, docs_args[arg])
                    continue

                index = args.index(arg)
                arg = self._annotation_syntax(guessed_type)

                # remove and replace the argument with the guessed one
                args.insert(index, f'{args.pop(index)}{arg}')

        return ', '.join(args)


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

    @property
    def obj(self) -> object:
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
        return get_docs(self.obj)

    @property
    def docs_arguments(self) -> Union[dict, None]:
        docs_args = re.findall(
            r'(?<=(?:@|:)param(?:\s|:))(?:\s?)(\w+)(?:\:|\s)(.+)',
            self.docs)
        return dict(docs_args) or None

    @property
    def return_argument(self) -> Union[re.Match, None]:
        try:
            return re.search(r'(?<=(?:@|:)return:)(.+)', self.docs).group()
        except AttributeError:
            return None

    @property
    def header(self):
        fn_header = FnHeaderExtractor(self).extract()

        args_parser = ArgsParser(fn_header, self.docs_arguments)
        args_parser.fix_args()

        if not Options.guess_type:
            return args_parser.fn_header

        return args_parser.guess_data_type()

    @property
    def return_(self):
        return ReturnExtractor(self).extract()


class FnHeaderExtractor:
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

    def __init__(self, header_obj: FunctionObject):
        self.header_obj = header_obj

        self.obj = header_obj.obj
        self.obj_name = self.obj.__name__

        self.obj_docs = header_obj.docs
        self.is_class = header_obj.is_class

        self.header = None

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
        try:
            # Built in methods will always fail
            return f'def {self.obj_name}{inspect.signature(self.obj)}:'
        except ValueError:
            return self._regex_extractor()
        except TypeError as err:

            # properties will not be callable from inspect.signature
            # so fallback on simple header
            if inspect.isdatadescriptor(self.obj):
                return f'@property\ndef {self.obj_name}(self) -> Any:'

            # the only warning is a staticmethod descriptor but I dont
            # want to bother making conditions to not add the self arg
            if inspect.ismethoddescriptor(self.obj):
                return self.simple_header()

            return self._unknown_header(err)

        except Exception as err:
            return self._unknown_header(err)

    def _unknown_header(self, err: Optional[Exception] = '') -> str:
        # most likely to be some dunder methods that can be safely ignored
        logging.warning(
            'Failed to extract func header for: %s. '
            'Fallback on object name. Traceback: %s', self.obj_name, err
        )
        return self.simple_header()


class ReturnExtractor:
    def __init__(self, header_obj: FunctionObject):
        self.header_obj = header_obj

    @staticmethod
    def _guess_type(_return):
        return GuessType(_return).auto_guess(exclude='optional')

    def get_return(self) -> str:
        """Parse the return value from the docs if any."""
        try:
            # search for everything after `->` if any
            _return = re.search(r'(?<=> ).+', self.header_obj.docs).group()

            # clean the extra last dot
            _return = re.sub(r'\.$', '',  _return)
        except AttributeError:
            # doc had no -> return annotation so try guessing based on doc arg
            _return = self.header_obj.return_argument
            if _return:
                return self._guess_type(_return)
            return 'None'

        # a list of object that should not be valid even if nuke this that are
        not_valid = ['name']

        if is_valid_object(_return) and _return not in not_valid:
            return _return

        if not Options.guess_type:
            return 'Any'

        guessed_type = self._guess_type(_return)

        if guessed_type:
            return guessed_type

        log_unguessed('Returns', self.header_obj.obj.__name__, _return)
        return 'Any'

    @staticmethod
    def _is_return_callable(_return: str) -> str:
        """Check if return is not Any, None, True, or has a ].

        If return match is made then the return will have a parenthesis: type()
        """
        if re.search(r'(Any|None|True|])', _return):
            return _return
        return f'{_return}()'

    def extract(self) -> str:
        """Extract function return from documentation."""
        _return = self._is_return_callable(self.get_return())
        return indent(f'return {_return}', ' ' * 4)


def func_constructor(header_obj: FunctionObject, _id) -> str:
    """Construct the function body.

    Args:
        header_obj (FunctionObject): FunctionObject data type

    Returns:
        [type]: string representation of the function body.
    """

    func_header = header_obj.header
    func_doc = indented_docs(header_obj.obj)
    func_return = header_obj.return_

    func_header, func_return = manual_mods(_id, func_header, func_return)

    return f'{func_header}\n{func_doc}\n{func_return}\n\n'


class ClassExtractor:
    def __init__(self, obj):
        self.obj = obj
        self.class_name = self.obj.__name__
        self.class_parent = self.obj.__base__.__name__

        self.class_file = None

    def init(self):
        self._setup_class_file()
        self._write_class_file()

    def _write_class_file(self):
        """Create class file"""
        with open(Options.path / 'classes' / f'{self.class_name}.py', 'w') as file:
            file.write(self.class_file)

    def _setup_class_file(self):
        self.class_file = dedent("""
        from numbers import Number
        from typing import *

        import nuke
        from . import *

        {}
        """).format(self._setup_class_content()).strip()

    def _setup_class_content(self) -> str:
        """Setup class file text content: header, docs and body."""
        class_header = f'class {self.class_name}({self.class_parent}):'
        class_doc = indented_docs(self.obj)
        class_body = self._get_class_methods()

        return f'{class_header}\n{class_doc}\n{class_body}'

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
            # logging.debug('\t%s', member)

            # check for simple type class attributes
            if type(obj) in (float, int, str, list, tuple, set, dict, bool, frozenset):
                class_body += f'{member} = {obj}\n'
                continue

            class_body += func_constructor(FunctionObject(
                obj=obj, fallback_name=member, is_class=True), self.class_name
            )

        return indent(class_body, ' ' * 4)


def parse_modules():
    """Parse the nuke object from Nuke python interpret."""
    def write_init(constants: str, builtin: str):
        """Create a init file will all the constants and built in methods."""

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
        """).format(constants, builtin).strip()
        print('Generating __init__.py')
        with open(Options.path / '__init__.py', 'w') as file:
            file.write(init_file)

    def write_class_imports(class_imports):
        """Create a init file with all the classes imports."""
        print('Generating class imports.')
        with open(Options.path / 'classes' / '__init__.py', 'w') as file:
            file.write(class_imports)

    builtin = ''
    constants = ''
    class_imports = ''

    print('Start extraction...')
    for attr in dir(Options.module):
        obj = getattr(Options.module, attr)

        if inspect.isclass(obj):
            class_imports += f'from .{attr} import {attr}\n'
            ClassExtractor(obj).init()
            print('Class:', attr)

        elif inspect.isbuiltin(obj):
            builtin += func_constructor(FunctionObject(obj, attr, False),
                                        '__init__')
            print('Built-in method:', attr)

        elif attr.isupper():
            print('Constants:', attr)
            constants += f'{attr} = {repr(obj)}\n'

        elif attr == 'env':
            constants += f"env = {repr({k: '' for k, _ in obj.items()})}"

    write_init(constants, builtin)
    write_class_imports(class_imports)
    print('Extraction completed.')


def generate_nuke_stubs():
    path = STUBS_PATH / 'nuke'

    Options.module = nuke
    Options.path = path
    os.makedirs(path / 'classes', exist_ok=True)

    parse_modules()
    get_included_modules()


def get_hiero():
    # Hack: add Hiero api
    import PySide2
    site_packages = pathlib.Path(PySide2.__file__).parent.parent
    hiero = site_packages / 'hiero'
    if hiero.exists():
        print('Hiero module copied')
        copytree(str(hiero), str(Options.path.parent), dirs_exist_ok=True)


def todo_generate_hiero_stubs():
    # TODO: Not ready yet
    path = STUBS_PATH / 'hiero' / 'core'

    Options.module = hiero.core
    Options.path = path
    os.makedirs(path / 'classes', exist_ok=True)

    get_hiero()
    parse_modules()


generate_nuke_stubs()
# todo_generate_hiero_stubs()
