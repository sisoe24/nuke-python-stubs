"""Create Nuke python file stubs to aid auto complete in text editors.

This method is inspired by PyCharm stub generator albeit less sophisticated but
a tiny bit more accurate on certain elements.

Unless specified otherwise, the stubs will be generated in the current working directory
inside a folder named 'nuke_stubs'. From there just add the path inside your text editor.
option for extra paths (eg: `python.analysis.extraPaths` for vscode).

Note: you should never find yourself in the same directory as the folder `nuke`
inside `nuke_stubs`, otherwise python will import that one instead of the real Nuke,
unless you mess with sys.path.

This has been tested only on MacOS under Python3 with Nuke13.

Usage:
    >>> alias nukepy='path/to/nuke/interpreter'
    >>> nukepy nuke_stubs_generator.py
    >>> nukepy nuke_stubs_generator.py -e
    >>> nukepy nuke_stubs_generator.py -o path/to/dir

Author:
    Virgil Sisoe - virgilsisoe@gmail.com - 09.27.2021
"""
import argparse
import inspect
import json
import logging
import os
import pathlib
import re
from distutils.dir_util import copy_tree
from textwrap import dedent, indent
from typing import Match, Optional, Union

# XXX: module nuke is imported inside main function


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
        callable(getattr(nuke, obj))
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
        'Knob': r'^(?:(a|the)\s)?knob'
    }

    def __init__(self, string):
        self.string = string

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
        match1 = is_valid_object(match.group(1))
        match2 = is_valid_object(match.group(2))

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
            r'(?<=@param\s)(\w+)(?:\s|:\s)(.+)', self.docs)
        return dict(docs_args) or None

    @property
    def return_argument(self) -> Union[re.Match, None]:
        try:
            return re.search(r'(?<=@return:)(.+)', self.docs).group()
        except AttributeError:
            return None

    @property
    def header(self):
        fn_header = FnHeaderExtractor(self).extract()

        args_parser = ArgsParser(fn_header, self.docs_arguments)
        args_parser.fix_args()

        if ARGS.no_type_guess:
            return args_parser.fn_header

        return args_parser.guess_data_type()

    @property
    def return_(self):
        return ReturnExtractor(self).extract()


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
        LOGGER.warning(
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

        if ARGS.no_type_guess:
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
        LOGGER.info('Modifying: %s -> %s', old, new)

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

    try:
        with open('manual_changes.json') as file:
            contents = json.load(file)
    except FileNotFoundError:
        LOGGER.warning(
            'No manual_changes.json file. Please download the example from the git repo.')
    else:
        for file, modifications in contents.items():
            if filename == file:
                func_header = header_mod(func_header, modifications['headers'])
                func_return = return_mod(func_header, func_return,
                                         modifications['returns'])

    return func_header, func_return


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
        path = PATH / 'nuke_classes' / f'{self.class_name}.py'
        with open(path, 'w') as file:
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
            LOGGER.debug('\t%s', member)

            # check for simple type class attributes
            if type(obj) in (float, int, str, list, tuple, set, dict):
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

        # BUG: string gets broken when using dedent + f string
        init_file = dedent("""
        '''Stubs generated automatically from Nuke's internal interpreter.'''
        from numbers import Number
        from typing import *

        from .nuke_classes import *
        from .nuke_internal import *

        # Constants
        {}

        # Built-in methods
        {}
        """).format(constants, builtin).strip()
        LOGGER.info('Generating __init__.py')

        path = PATH / '__init__.py'
        with open(path, 'w') as file:
            file.write(init_file)

    def write_class_imports(class_imports):
        """Create a init file with all the classes imports."""
        LOGGER.info('Generating class imports..')

        path = PATH / 'nuke_classes' / '__init__.py'
        with open(path, 'w') as file:
            file.write(class_imports)

    builtin = ''
    constants = ''
    class_imports = ''

    LOGGER.info('Start extraction...')
    for attr in dir(nuke):
        obj = getattr(nuke, attr)

        if inspect.isclass(obj):
            class_imports += f'from .{attr} import {attr}\n'
            ClassExtractor(obj).init()

        elif inspect.isbuiltin(obj):
            builtin += func_constructor(FunctionObject(obj, attr, False),
                                        '__init__')
            LOGGER.debug('Built-in method: %s', attr)

        elif attr.isupper():
            LOGGER.debug('Constants: %s', attr)
            constants += f'{attr} = {repr(obj)}\n'

        elif attr == 'env':
            constants += f"env = {repr({k: '' for k, _ in obj.items()})}"

    write_init(constants, builtin)
    write_class_imports(class_imports)
    LOGGER.info('Extraction completed.')


def get_included_modules():
    """Get included modules inside plugins path.

    If user has declared a package named with the same internal modules names,
    although they will be copied at first, they will be overwritten when the loop
    goes to the last plugins path that are usually the one from the system.
    """
    def _clean_nukescripts():
        """Import the correct module for nukescripts."""
        path = PATH.parent.joinpath('nukescripts')

        for file in path.glob('*.py'):
            with open(file, 'r+') as f:
                content = f.read()
                sub = re.sub('import nuke_internal as nuke',
                             'import nuke', content)
                f.seek(0)
                f.write(sub)
                f.truncate()

    def _clean_init():
        """Clean nuke_internal __init__."""
        nuke_internal_init = os.path.join(PATH, 'nuke_internal', '__init__.py')

        with open(nuke_internal_init, 'r') as file:
            contents = re.finditer(r'(^(from|#).+)', file.read(), re.M)

        with open(nuke_internal_init, 'w') as file:
            file.seek(0)
            for i in contents:
                file.write(i.group(1) + '\n')

    plugins_path = nuke.pluginPath()

    for path in plugins_path:
        for module in ('nuke_internal', 'nuke', 'nukescripts'):
            src = os.path.join(path, module)
            if os.path.exists(src):
                LOGGER.info('Internal module copied: %s', module)

                _path = PATH.parent if module == 'nukescripts' else PATH
                copy_tree(src, str(_path / module))

    _clean_init()
    _clean_nukescripts()


def get_hiero():
    # Hack: add Hiero api
    import PySide2
    site_packages = pathlib.Path(PySide2.__file__).parent.parent
    hiero = site_packages / 'hiero'
    if hiero.exists():
        LOGGER.info('Hiero module copied')
        copy_tree(str(hiero), str(PATH.parent / 'hiero'))


def setup_argparser():
    """Command line arguments setup function."""
    parser = argparse.ArgumentParser(description='Create Nuke Python Stubs')
    parser.add_argument('-v', '--verbosity', action='store_true',
                        help='Increase output verbosity')
    parser.add_argument('--exclude-internals', action='store_true',
                        help='Exclude internal modules: nukescripts, nuke_internal')
    parser.add_argument('-x', '--no-type-guess', action='store_true',
                        help='Compile stubs without guessing some of the types.')
    parser.add_argument('-o', '--output', action='store', type=str,
                        help='Output to specific directory')
    return parser.parse_args()


def setup_logger(name,  log_file, _format='%(levelname)s :: %(message)s'):
    os.makedirs('log', exist_ok=True)
    logger = logging.getLogger(name)

    logger.parent = None
    logger.setLevel(logging.DEBUG)

    logging_format = logging.Formatter(_format)

    path = os.path.join('log', log_file)
    file_handler = logging.FileHandler(path, 'w')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging_format)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging_format)
    logger.addHandler(console_handler)

    return logger


def log_unguessed(_type, obj, result):
    msg = '[ {:>9} ] {: ^85} :: {}'.format(_type, obj, result)
    LOG_UNGUESSED.debug(msg)


def main():
    """Main start up function"""

    # BUG: importing nuke at top module seems create some undefined behavior
    # when dealing with argparser module, order resolution calls and more ?
    import nuke

    # create folders if missing
    for modules in ['nuke_classes', 'nuke_internal']:
        os.makedirs(PATH / modules, exist_ok=True)

    nukescripts_path = PATH.parent / 'nukescripts'
    os.makedirs(nukescripts_path, exist_ok=True)

    parse_modules()
    if not ARGS.exclude_internals:
        get_included_modules()
        get_hiero()

    manual_mods()
    logging.info('Done')


LOGGER = setup_logger('main', 'log.log')
LOG_UNGUESSED = setup_logger('unguessed', 'unguessed.log', '')

ARGS = setup_argparser()
PATH = ARGS.output or pathlib.Path(__file__).parent / 'nuke_stubs' / 'nuke'

main()
