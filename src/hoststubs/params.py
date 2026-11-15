"""Read the parameter probe's raw outcomes into argument counts and types.

Two kinds of evidence per position. The error a poison object gets says
what the parser wanted (`argument 1 must be str, not HostStubsPoison`).
Where that text is missing or unknown, the candidates that got past the
position say what it accepts.
"""
from __future__ import annotations

import re
import json
from pathlib import Path

from hoststubs.names import Names
from hoststubs.resolve import ProbedParams
from hoststubs.annotations import split_generic, split_top_level

SCHEMA = 1
POISON = 'HostStubsPoison'
NONE_TYPE = 'builtins.NoneType'
ANY_SEQUENCE = 'typing.Sequence[typing.Any]'
ANY_CALLABLE = 'typing.Callable[..., typing.Any]'

ARGUMENT_NUMBER = re.compile(r'argument (\d+)')
COUNT_ERROR = re.compile(r'takes (?:exactly|at least|at most|no) |missing required argument')

# What CPython's own argument converters say, in any host.
MUST_BE = re.compile(r'must be (?:an? )?([\w.]+?)(?P<or_none> or None)?,? not ')
PYTHON_MESSAGES = (
    (re.compile(r'cannot be interpreted as an integer|an integer is required'), 'builtins.int'),
    (re.compile(r'must be real number|a float is required'), 'builtins.float'),
    (re.compile(r'must be callable|expected callable'), ANY_CALLABLE),
)
MUST_BE_NAMES = {
    'str': 'builtins.str', 'string': 'builtins.str', 'int': 'builtins.int',
    'integer': 'builtins.int', 'bool': 'builtins.bool', 'float': 'builtins.float',
    'dict': 'builtins.dict', 'list': 'builtins.list', 'tuple': 'builtins.tuple',
    'bytes': 'builtins.bytes',
}

# A position that lets nearly every candidate through takes any object.
MAX_UNION = 3


def _blames_poison(outcome: dict) -> bool:
    return outcome.get('error') == 'TypeError' and POISON in outcome.get('message', '')


class _Reader:
    def __init__(
        self, names: Names, messages: tuple[tuple[str, str], ...], candidates: int,
    ) -> None:
        self._names = names
        self._messages = [(re.compile(pattern), type_) for pattern, type_ in messages]
        self._candidates = candidates

    # === PRIVATE === #

    def _from_message(self, outcome: dict, index: int, module: str) -> str | None:
        """The type the error text asks for, when the error is about this position."""
        if outcome.get('error') != 'TypeError':
            return None

        message = outcome['message']
        if COUNT_ERROR.search(message):
            return None
        number = ARGUMENT_NUMBER.search(message)
        if number and int(number.group(1)) != index + 1:
            return None

        for pattern, type_ in self._messages:
            if pattern.search(message):
                # A class the config names may not exist in this host version.
                is_known = all(
                    member == 'None' or self._names.accept(split_generic(member)[0])
                    for member in split_top_level(type_, ' | ')
                )
                return type_ if is_known else None
        for pattern, type_ in PYTHON_MESSAGES:
            if pattern.search(message):
                return type_

        must_be = MUST_BE.search(message)
        if must_be is None:
            return None
        wanted = must_be.group(1)
        found = MUST_BE_NAMES.get(wanted) or self._names.resolve(wanted, module)
        if found and must_be.group('or_none'):
            return f'{found} | None'
        return found

    def _from_candidates(self, outcomes: dict[str, dict]) -> str | None:
        """One type for the set of candidates that got past this position."""
        accepted = {label for label, outcome in outcomes.items() if _blames_poison(outcome)}
        if not accepted or len(accepted) >= self._candidates - 1:
            return None

        allows_none = NONE_TYPE in accepted
        accepted.discard(NONE_TYPE)

        # The parser converts: a float position takes int, an int position takes bool.
        if 'builtins.float' in accepted:
            accepted -= {'builtins.int', 'builtins.bool'}
        elif 'builtins.int' in accepted:
            accepted.discard('builtins.bool')

        types = []
        if {'builtins.list', 'builtins.tuple'} <= accepted:
            accepted -= {'builtins.list', 'builtins.tuple'}
            types.append(ANY_SEQUENCE)
        if 'builtins.function' in accepted:
            accepted.discard('builtins.function')
            types.append(ANY_CALLABLE)

        for label in sorted(accepted):
            public = self._names.accept(label)
            if public is None:
                return None
            # The candidate was one instance; the position takes its base class.
            types.append(self._names.ancestors(public)[-1])

        if not types or len(types) > MAX_UNION:
            return None
        if allows_none:
            types.append('None')
        return ' | '.join(dict.fromkeys(types))

    # === PUBLIC === #

    def read(self, record: dict, module: str) -> ProbedParams:
        types = []
        for index, position in enumerate(record['positions']):
            found = self._from_message(position['poison'], index, module)
            types.append(found or self._from_candidates(position['candidates']))
        return ProbedParams(record['minimum'], record['maximum'], tuple(types))


def _reached_parser(record: dict) -> bool:
    none = record['none']
    return 'returned' in none or none.get('error') == 'TypeError'


def _merge(readings: list[ProbedParams]) -> ProbedParams | None:
    """Receivers must agree on the counts; a type they disagree on is dropped."""
    first = readings[0]
    if any((other.minimum, other.maximum) != (first.minimum, first.maximum) for other in readings):
        return None

    types = []
    for index, type_ in enumerate(first.types):
        same = all(index < len(other.types) and other.types[index] == type_ for other in readings)
        types.append(type_ if same else None)
    return ProbedParams(first.minimum, first.maximum, tuple(types))


def load_params(
    path: Path, names: Names, messages: tuple[tuple[str, str], ...],
) -> dict[str, ProbedParams]:
    """Map each probed function path to what its argument parser accepts."""
    raw = json.loads(path.read_text(encoding='utf-8'))
    if raw.get('schema') != SCHEMA:
        raise ValueError(f'{path}: schema {raw.get("schema")!r}, expected {SCHEMA}')

    reader = _Reader(names, messages, len(raw['candidates']))

    probed = {}
    for function, records in raw['functions'].items():
        # A receiver that refuses the call for its own reasons (Root has no inputs
        # and answers 'invalid') says nothing about the arguments.
        usable = [record for record in records if _reached_parser(record)]
        if not usable:
            continue
        module, _ = names.split_module(function)
        merged = _merge([reader.read(record, module) for record in usable])
        if merged:
            probed[function] = merged
    return probed
