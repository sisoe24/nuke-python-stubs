"""Turn probe observations into candidates.

`type(result)` is one return, on one object, in one scene state. These rules
keep an observation from claiming more than it saw:

- None is discarded: it means nothing was set, not that the function returns None.
- A container counts only with its element types. Empty, or elements with no
  common class, gives a bare `list`, which ranks below every other evidence.
- Every receiver must agree. Classes that differ resolve to their common base
  in the dump; anything else gives no candidate.
"""
from __future__ import annotations

import json
from pathlib import Path

from hoststubs.names import Names
from hoststubs.resolve import Candidate

SCHEMA = 1
NONE_TYPE = 'builtins.NoneType'
SEQUENCES = ('builtins.list', 'builtins.tuple', 'builtins.set', 'builtins.frozenset')
DICT = 'builtins.dict'


def _common(raw_types: set[str], names: Names) -> str | None:
    """One type for a set of runtime type names, or None when they do not agree."""
    accepted = [names.accept(raw) for raw in sorted(raw_types)]
    if not accepted or None in accepted:
        return None

    unique = list(dict.fromkeys(accepted))
    if len(unique) == 1:
        return unique[0]
    return names.common_base(unique)


def _candidate(observations: list[dict], names: Names) -> Candidate | None:
    seen = [
        observation for observation in observations
        if 'error' not in observation and observation['type'] != NONE_TYPE
    ]
    kinds = {observation['type'] for observation in seen}
    if not seen:
        return None

    if len(kinds) == 1 and kinds <= set(SEQUENCES):
        [container] = kinds
        elements = {element for observation in seen for element in observation['elements']}
        element = _common(elements, names)
        if element is None:
            return Candidate(container, 'probe_weak')
        suffix = ', ...' if container == 'builtins.tuple' else ''
        return Candidate(f'{container}[{element}{suffix}]', 'probe')

    if kinds == {DICT}:
        key = _common({key for observation in seen for key in observation['keys']}, names)
        value = _common({value for observation in seen for value in observation['values']}, names)
        if key is None or value is None:
            return Candidate(DICT, 'probe_weak')
        return Candidate(f'{DICT}[{key}, {value}]', 'probe')

    if kinds & (set(SEQUENCES) | {DICT}):
        # A container on one receiver and something else on another.
        return None

    found = _common(kinds, names)
    return Candidate(found, 'probe') if found else None


def load_observations(path: Path, names: Names) -> dict[str, Candidate]:
    """Map each probed path to the candidate its observations support."""
    raw = json.loads(path.read_text(encoding='utf-8'))
    if raw.get('schema') != SCHEMA:
        raise ValueError(f'{path}: schema {raw.get("schema")!r}, expected {SCHEMA}')

    candidates = {}
    for target, observations in raw['observations'].items():
        candidate = _candidate(observations, names)
        if candidate:
            candidates[target] = candidate
    return candidates
