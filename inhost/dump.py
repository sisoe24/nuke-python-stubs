"""Dump a host application's Python API to JSON.

Runs inside the host interpreter: standard library only, Python 3.7 syntax.
It records what the runtime reports and decides nothing about types.

Usage:
    <host python> dump.py OUT.json host=NAME version=MODULE.ATTR
        [skip=MODULE ...] [private=MODULE ...] ROOT [ROOT ...]

`private` names a C module that is importable but that users reach only through
a root, such as hiero's `core`. Its objects are recorded under that root.

Arguments have no leading dashes because hosts such as Nuke consume dashed flags.
From a script editor, call `main([...])` with the same arguments.

The output format is described in docs/dump-schema.md.
"""
from __future__ import annotations

import sys
import json
import inspect
import logging
import pkgutil
import importlib
from pathlib import Path
from collections import Counter

SCHEMA = 1

QT_BINDINGS = ('PySide6', 'PySide2', 'PyQt6', 'PyQt5')

# A string constant can hold a path on the dumping machine, so its value stays out.
CONSTANT_TYPES = (bool, int, float, type(None))
DEFAULT_TYPES = CONSTANT_TYPES + (str,)
MAX_REPR = 80

CLASS_NOISE = frozenset([
    '__dict__', '__weakref__', '__module__', '__doc__', '__qualname__',
    '__annotations__', '__firstlineno__', '__static_attributes__',
])

LOGGER = logging.getLogger('dump')


def type_name(tp):
    module = getattr(tp, '__module__', None)
    name = getattr(tp, '__qualname__', None) or getattr(tp, '__name__', None) or repr(tp)
    return '{}.{}'.format(module, name) if isinstance(module, str) else name


def doc_of(obj):
    # Python 3.13 strips docstring indentation at compile time; older versions do not.
    doc = getattr(obj, '__doc__', None)
    return inspect.cleandoc(doc) if isinstance(doc, str) else None


def dump_value(value, repr_types):
    entry = {'kind': 'value', 'type': type_name(type(value))}
    if type(value) in repr_types:
        text = repr(value)
        if len(text) <= MAX_REPR:
            entry['repr'] = text
    return entry


def dump_annotation(annotation):
    if annotation is inspect.Signature.empty:
        return None
    if isinstance(annotation, str):
        return annotation
    if inspect.isclass(annotation):
        return type_name(annotation)
    return repr(annotation)


def dump_signature(func):
    try:
        signature = inspect.signature(func)
    except (TypeError, ValueError):
        # C functions without __text_signature__ have no signature.
        return None

    params = []
    for param in signature.parameters.values():
        entry = {
            'name': param.name,
            'kind': param.kind.name,
            'annotation': dump_annotation(param.annotation),
        }
        if param.default is not inspect.Parameter.empty:
            entry['default'] = dump_value(param.default, DEFAULT_TYPES)
        params.append(entry)

    return {'params': params, 'returns': dump_annotation(signature.return_annotation)}


def dump_function(func, binding=None):
    entry = {
        'kind': 'function',
        'descriptor': type_name(type(func)),
        'origin': getattr(func, '__module__', None),
        'qualname': getattr(func, '__qualname__', None),
        'doc': doc_of(func),
        'signature': dump_signature(func),
        'text_signature': getattr(func, '__text_signature__', None),
    }
    if binding:
        entry['binding'] = binding
    return entry


def dump_property(descriptor):
    entry = {
        'kind': 'property',
        'descriptor': type_name(type(descriptor)),
        'doc': doc_of(descriptor),
    }
    if isinstance(descriptor, property):
        entry['settable'] = descriptor.fset is not None
        if descriptor.fget is not None:
            entry['getter'] = dump_function(descriptor.fget)
    return entry


def is_function(obj):
    # A Qt signal in a class body is a callable method descriptor, but an attribute.
    if str(type(obj).__module__).split('.')[0] in QT_BINDINGS:
        return False
    return inspect.isroutine(obj) and callable(obj)


def relative_file(module, name):
    file = getattr(module, '__file__', None)
    if not file:
        return None

    top = sys.modules.get(name.split('.')[0])
    top_file = getattr(top, '__file__', None)
    if not top_file:
        return Path(file).name

    base = Path(top_file).parent
    if Path(top_file).stem == '__init__':
        base = base.parent

    try:
        return Path(file).relative_to(base).as_posix()
    except ValueError:
        return Path(file).name


def resolve(dotted):
    """Import the longest module prefix of `dotted` and follow the rest as attributes."""
    parts = dotted.split('.')
    for split in range(len(parts), 0, -1):
        try:
            obj = importlib.import_module('.'.join(parts[:split]))
        except ImportError:
            continue
        for attribute in parts[split:]:
            obj = getattr(obj, attribute)
        return obj
    raise ImportError('cannot resolve {!r}'.format(dotted))


class Dumper:
    def __init__(self, roots, skip, private):
        self.roots = tuple(roots)
        self.skip = tuple(skip)
        self.private = tuple(private)

        self.modules = {}
        self.errors = []
        self.foreign = Counter()

        # id -> (path, object). Holding the object keeps its id from being reused.
        self._owned = {}

    # === PRIVATE === #

    def _under(self, name, prefixes):
        return any(name == prefix or name.startswith(prefix + '.') for prefix in prefixes)

    def _is_public_elsewhere(self, obj, origin, qualname):
        if any(part.startswith('_') for part in origin.split('.')):
            return False
        if self._under(origin, self.private):
            return False

        found = sys.modules.get(origin)
        if found is None:
            return False

        for attribute in qualname.split('.'):
            found = getattr(found, attribute, None)
        return found is obj

    def _alias_target(self, obj, here):
        """Return where `obj` is defined, or None when it must be recorded at `here`."""
        origin = getattr(obj, '__module__', None)
        qualname = getattr(obj, '__qualname__', None)

        if isinstance(origin, str) and qualname and '<locals>' not in qualname:
            target = '{}.{}'.format(origin, qualname)
            if target == here:
                return None
            if self._under(origin, self.roots):
                return target
            if self._is_public_elsewhere(obj, origin, qualname):
                self.foreign[origin.split('.')[0]] += 1
                return target

        # The origin is private or not importable (a C extension behind a public
        # package), so the first public place that shows the object owns it.
        first = self._owned.setdefault(id(obj), (here, obj))[0]
        return None if first == here else first

    def _guarded(self, dump, obj, here):
        try:
            return dump(obj, here)
        except Exception as error:
            message = '{}: {}'.format(type(error).__name__, error)
            self.errors.append({'where': here, 'error': message})
            return {'kind': 'error', 'error': message}

    def _dump_class(self, cls, here):
        members = {}
        for name, raw in sorted(vars(cls).items()):
            if name not in CLASS_NOISE:
                members[name] = self._guarded(self._dump_class_member, raw, here + '.' + name)

        return {
            'kind': 'class',
            'origin': getattr(cls, '__module__', None),
            'qualname': cls.__qualname__,
            'bases': [type_name(base) for base in cls.__bases__],
            'doc': doc_of(cls),
            'members': members,
        }

    def _dump_class_or_alias(self, cls, here):
        target = self._alias_target(cls, here)
        if target:
            return {'kind': 'alias', 'target': target}
        return self._dump_class(cls, here)

    def _dump_class_member(self, raw, here):
        if isinstance(raw, staticmethod):
            return dump_function(raw.__func__, 'static')
        if isinstance(raw, classmethod):
            return dump_function(raw.__func__, 'class')
        if inspect.isclass(raw):
            return self._dump_class_or_alias(raw, here)
        if is_function(raw):
            is_class_method = type(raw).__name__ == 'classmethod_descriptor'
            return dump_function(raw, 'class' if is_class_method else 'instance')
        if inspect.isdatadescriptor(raw):
            return dump_property(raw)
        return dump_value(raw, CONSTANT_TYPES)

    def _dump_module_member(self, obj, here):
        if inspect.ismodule(obj):
            return {'kind': 'module', 'target': obj.__name__}
        if inspect.isclass(obj):
            return self._dump_class_or_alias(obj, here)
        if is_function(obj):
            target = self._alias_target(obj, here)
            if target:
                return {'kind': 'alias', 'target': target}
            return dump_function(obj)
        return dump_value(obj, CONSTANT_TYPES)

    def _dump_module(self, module, name):
        members = {}
        for key, obj in sorted(vars(module).items()):
            is_dunder = key.startswith('__') and key.endswith('__')
            if not is_dunder:
                members[key] = self._guarded(self._dump_module_member, obj, name + '.' + key)

        entry = {
            'doc': doc_of(module),
            'file': relative_file(module, name),
            'members': members,
        }

        exported = vars(module).get('__all__')
        if isinstance(exported, (list, tuple)):
            entry['all'] = [item for item in exported if isinstance(item, str)]

        self.modules[name] = entry

    def _walk(self, name):
        if self._under(name, self.skip):
            return

        try:
            module = importlib.import_module(name)
        except Exception as error:
            message = '{}: {}'.format(type(error).__name__, error)
            self.errors.append({'where': name, 'error': message})
            return

        self._dump_module(module, name)

        search_path = getattr(module, '__path__', None)
        if search_path is None:
            return

        children = sorted(info.name for info in pkgutil.iter_modules(search_path, name + '.'))
        for child in children:
            self._walk(child)

    # === PUBLIC === #

    def run(self):
        for root in self.roots:
            self._walk(root)


def detect_qt():
    for binding in QT_BINDINGS:
        module = sys.modules.get(binding)
        if module is not None:
            return {'binding': binding, 'version': getattr(module, '__version__', None)}
    return None


def parse_args(argv):
    options = {'host': None, 'version': None, 'skip': [], 'private': []}
    positional = []

    for argument in argv:
        key, separator, value = argument.partition('=')
        if separator and key in ('skip', 'private'):
            options[key].append(value)
        elif separator and key in options:
            options[key] = value
        else:
            positional.append(argument)

    if len(positional) < 2 or not options['host'] or not options['version']:
        raise SystemExit(__doc__)

    return positional[0], positional[1:], options


def main(argv):
    out, roots, options = parse_args(argv)

    dumper = Dumper(roots, options['skip'], options['private'])
    dumper.run()

    dump = {
        'schema': SCHEMA,
        'host': {'name': options['host'], 'version': str(resolve(options['version']))},
        'python': '.'.join(str(part) for part in sys.version_info[:3]),
        'platform': sys.platform,
        'qt': detect_qt(),
        'modules': dumper.modules,
        'foreign': dict(dumper.foreign),
        'errors': dumper.errors,
    }

    with open(out, 'w', encoding='utf-8') as file:
        json.dump(dump, file, indent=1, sort_keys=True)
        file.write('\n')

    LOGGER.info('Wrote %s: %d modules, %d errors.', out, len(dumper.modules), len(dumper.errors))
    for error in dumper.errors:
        LOGGER.warning('%s: %s', error['where'], error['error'])
    LOGGER.info('References to modules outside the roots: %s', dict(dumper.foreign))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(levelname)s %(message)s')
    main(sys.argv[1:])
