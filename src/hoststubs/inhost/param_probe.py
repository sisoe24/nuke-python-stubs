"""Find out what arguments the host's C functions accept, from their own errors.

Runs inside the host interpreter: standard library only, Python 3.7 syntax.

Usage:
    <host python> param_probe.py OUT.json targets=TARGETS.json scene=SCENE.py [resume]

A C function checks its arguments before it does any work, left to right,
and reports the first one it rejects. So for each position this script
passes one real candidate value followed by a poison object:

    f('text', POISON)   error names the poison  -> position 1 accepts str
    f(12, POISON)       error names the int     -> position 1 rejects int

The function body does not run, because the poison stops the call. The last
position has nothing after it, so only the poison is passed there and the
error text is kept for the offline step to read.

It records outcomes only. Deciding what they mean is the offline step's job.
Journal, resume and timeout work as in probe.py.
"""
from __future__ import annotations

import re
import sys
import json
import signal
import logging

from probe import TIMEOUT, Journal, resolve, type_name, load_scene

SCHEMA = 1
MAX_POSITIONS = 8
MANY = 12
MAX_RECEIVERS = 2
MAX_MESSAGE = 400

NUMBER_WORDS = {'no': 0, 'one': 1, 'two': 2, 'three': 3}
EXACTLY = re.compile(r'takes exactly (\w+) (?:positional )?arguments?')
NO_ARGUMENTS = re.compile(r'takes no arguments')
AT_LEAST = re.compile(r'(?:takes|expected) at least (\d+) (?:positional )?arguments?')
AT_MOST = re.compile(r'(?:takes|expected) at most (\d+) (?:positional )?arguments?')
EXPECTED = re.compile(r'expected (\d+) arguments?, got')

LOGGER = logging.getLogger('param_probe')


class HostStubsPoison:
    """An object no function expects. Its name in an error says which argument failed."""


POISON = HostStubsPoison()


def outcome(function, arguments):
    try:
        result = function(*arguments)
    except Exception as error:
        return {'error': type(error).__name__, 'message': str(error)[:MAX_MESSAGE]}
    return {'returned': type_name(type(result))}


def blames_poison(result):
    return result.get('error') == 'TypeError' and 'HostStubsPoison' in result['message']


def to_number(word):
    return NUMBER_WORDS[word] if word in NUMBER_WORDS else int(word)


def argument_counts(none, many):
    """Read (minimum, maximum) from the errors of a call with no and with too many arguments."""
    minimum = maximum = None

    for result in (none, many):
        message = result.get('message', '') if result.get('error') == 'TypeError' else ''

        exactly = EXACTLY.search(message) or EXPECTED.search(message)
        if exactly:
            try:
                minimum = maximum = to_number(exactly.group(1))
            except ValueError:
                pass
        if NO_ARGUMENTS.search(message):
            minimum = maximum = 0

        at_least = AT_LEAST.search(message)
        if at_least:
            minimum = int(at_least.group(1))
        at_most = AT_MOST.search(message)
        if at_most:
            maximum = int(at_most.group(1))

    if minimum is None and 'returned' in none:
        minimum = 0
    return minimum, maximum


def probe_positions(function, count, candidates):
    """Test each position in turn. Stops at the first one that accepts no candidate."""
    positions = []
    accepted_values = []

    for index in range(count):
        is_last = index + 1 == count
        position = {'poison': outcome(function, accepted_values + [POISON]), 'candidates': {}}
        positions.append(position)
        if is_last:
            # Nothing can follow to stop the call, so a candidate would run the function.
            break

        first_accepted = None
        for label, value in candidates:
            result = outcome(function, accepted_values + [value, POISON])
            position['candidates'][label] = result
            if first_accepted is None and blames_poison(result):
                first_accepted = value

        if first_accepted is None:
            break
        accepted_values.append(first_accepted)

    return positions


def probe_function(function, documented_count, candidates):
    none = outcome(function, [])
    many = outcome(function, [POISON] * MANY)
    minimum, maximum = argument_counts(none, many)

    count = maximum if maximum is not None else documented_count
    record = {'none': none, 'many': many, 'minimum': minimum, 'maximum': maximum, 'positions': []}
    if count:
        record['positions'] = probe_positions(function, min(count, MAX_POSITIONS), candidates)
    return record


def receivers(target, instances):
    owner = resolve(target['owner'])
    if target['on'] == 'owner':
        return [owner]

    by_type = {}
    for instance in instances:
        if isinstance(instance, owner):
            by_type.setdefault(type(instance), instance)
    return list(by_type.values())[:MAX_RECEIVERS]


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
    candidates = [(type_name(type(value)), value) for value in scene.candidates()]

    for target in targets:
        path = target['path']
        if path in journal.started:
            continue

        journal.start(path)
        if hasattr(signal, 'alarm'):
            signal.alarm(TIMEOUT)

        records = []
        try:
            found = receivers(target, instances)
        except Exception:
            found = []
        for receiver in found:
            try:
                function = getattr(receiver, target['name'])
            except Exception:
                continue
            record = probe_function(function, target.get('count'), candidates)
            record['receiver'] = type_name(type(receiver))
            records.append(record)

        if hasattr(signal, 'alarm'):
            signal.alarm(0)
        journal.finish(path, records)

    if hasattr(scene, 'teardown'):
        scene.teardown()

    probe = {
        'schema': SCHEMA,
        'scene': scene.DESCRIPTION,
        'candidates': [label for label, _ in candidates],
        'functions': journal.results,
        'crashed': journal.unfinished(),
    }
    with open(out, 'w', encoding='utf-8') as file:
        json.dump(probe, file, indent=1, sort_keys=True)
        file.write('\n')

    crashed = len(probe['crashed'])
    LOGGER.info('Wrote %s: %d functions, %d crashed.', out, len(journal.results), crashed)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(levelname)s %(message)s')
    main(sys.argv[1:])
