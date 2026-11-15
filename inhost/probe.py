"""Call the host's zero-argument functions and record the type of each result.

Runs inside the host interpreter: standard library only, Python 3.7 syntax.
It is separate from dump.py because it calls host code, which can hang or
crash the host.

Usage:
    <host python> probe.py OUT.json targets=TARGETS.json scene=SCENE.py [resume]

TARGETS.json lists what to call; `python -m hoststubs probe-targets` writes it.
SCENE.py is host-specific: `build()` creates a known scene and returns the
objects whose methods are probed.

Before each call the target path is written to OUT.json.journal and flushed,
so after a hang or a crash the last line names the call that did it. Run
again with `resume` to skip everything already journalled. A call that
runs longer than TIMEOUT seconds kills the process, for the same reason.
"""
from __future__ import annotations

import os
import sys
import json
import signal
import logging
import importlib
import importlib.util

SCHEMA = 1
TIMEOUT = 30

# A method of a base class must be seen on every subclass before its result
# means anything: one receiver of each type, then more up to this many.
MIN_INSTANCES = 12
MAX_ELEMENTS = 500
CONTAINERS = (list, tuple, set, frozenset)

LOGGER = logging.getLogger('probe')


def type_name(tp):
    module = getattr(tp, '__module__', None)
    name = getattr(tp, '__qualname__', None) or getattr(tp, '__name__', None) or repr(tp)
    return '{}.{}'.format(module, name) if isinstance(module, str) else name


def element_types(values):
    return sorted({type_name(type(value)) for value in list(values)[:MAX_ELEMENTS]})


def observe(value):
    """Describe a result by its type, never by its value or repr."""
    observation = {'type': type_name(type(value))}
    if isinstance(value, CONTAINERS):
        observation['length'] = len(value)
        observation['elements'] = element_types(value)
    elif isinstance(value, dict):
        observation['length'] = len(value)
        observation['keys'] = element_types(value.keys())
        observation['values'] = element_types(value.values())
    return observation


def resolve(path):
    parts = path.split('.')
    for split in range(len(parts), 0, -1):
        try:
            found = importlib.import_module('.'.join(parts[:split]))
        except ImportError:
            continue
        for attribute in parts[split:]:
            found = getattr(found, attribute)
        return found
    raise ImportError('cannot resolve {!r}'.format(path))


def load_scene(path):
    spec = importlib.util.spec_from_file_location('probe_scene', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def receivers(target, instances):
    """Objects to call the target on: the module or class itself, or scene instances."""
    try:
        owner = resolve(target['owner'])
    except Exception:
        # A module that exists only in another session kind, such as hiero outside the GUI.
        return []
    if target['on'] == 'owner':
        return [owner]

    by_type = {}
    for instance in instances:
        if isinstance(instance, owner):
            by_type.setdefault(type(instance), []).append(instance)

    picked = []
    rounds = max([len(group) for group in by_type.values()] or [0])
    for index in range(rounds):
        if index and len(picked) >= MIN_INSTANCES:
            break
        picked += [group[index] for group in by_type.values() if index < len(group)]
    return picked


def call(target, receiver):
    try:
        attribute = getattr(receiver, target['name'])
        value = attribute if target['kind'] == 'property' else attribute()
    except Exception as error:
        return {'error': type(error).__name__, 'message': str(error)[:120]}
    return observe(value)


class Journal:
    """Append-only record: '> path' before a call, '< path json' after it."""

    def __init__(self, path, resume):
        self.started = set()
        self.results = {}

        if resume and os.path.exists(path):
            self._read(path)
        self._file = open(path, 'a' if resume else 'w', encoding='utf-8')

    def _read(self, path):
        with open(path, encoding='utf-8') as file:
            for line in file:
                marker, _, rest = line.rstrip('\n').partition(' ')
                target, _, payload = rest.partition(' ')
                if marker == '>':
                    self.started.add(target)
                elif marker == '<':
                    self.results[target] = json.loads(payload)

    def _write(self, line):
        self._file.write(line + '\n')
        self._file.flush()
        os.fsync(self._file.fileno())

    def start(self, target):
        self._write('> ' + target)
        self.started.add(target)

    def finish(self, target, observations):
        self._write('< {} {}'.format(target, json.dumps(observations, sort_keys=True)))
        self.results[target] = observations

    def unfinished(self):
        return sorted(self.started - set(self.results))


def main(argv):
    options = dict(argument.split('=', 1) for argument in argv if '=' in argument)
    positional = [argument for argument in argv if '=' not in argument]
    if not positional or 'targets' not in options or 'scene' not in options:
        raise SystemExit(__doc__)

    out = positional[0]
    journal = Journal(out + '.journal', resume='resume' in positional)

    with open(options['targets'], encoding='utf-8') as file:
        targets = json.load(file)['targets']

    scene = load_scene(options['scene'])
    instances = scene.build()

    for target in targets:
        path = target['path']
        if path in journal.started:
            continue

        journal.start(path)
        if hasattr(signal, 'alarm'):
            # No handler: a call stuck in C code cannot be interrupted, only killed.
            signal.alarm(TIMEOUT)

        observations = []
        for receiver in receivers(target, instances):
            observation = call(target, receiver)
            observation['receiver'] = type_name(type(receiver))
            observations.append(observation)

        if hasattr(signal, 'alarm'):
            signal.alarm(0)
        journal.finish(path, observations)

    if hasattr(scene, 'teardown'):
        scene.teardown()

    probe = {
        'schema': SCHEMA,
        'scene': scene.DESCRIPTION,
        'observations': journal.results,
        # Journalled but never finished: the calls that hung or crashed the host.
        'crashed': journal.unfinished(),
    }
    with open(out, 'w', encoding='utf-8') as file:
        json.dump(probe, file, indent=1, sort_keys=True)
        file.write('\n')

    crashed = len(probe['crashed'])
    LOGGER.info('Wrote %s: %d targets, %d crashed.', out, len(journal.results), crashed)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(levelname)s %(message)s')
    main(sys.argv[1:])
