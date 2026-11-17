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
from hoststubs.resolve import Candidate, Observed

SCHEMA = 1
NONE_TYPE = 'builtins.NoneType'
SEQUENCES = ('builtins.list', 'builtins.tuple', 'builtins.set', 'builtins.frozenset')
DICT = 'builtins.dict'


def _accepted(raw_types: set[str], names: Names) -> list[str] | None:
    """Public names for a set of runtime type names, or None when one is unknown."""
    accepted = [names.accept(raw) for raw in sorted(raw_types)]
    if not accepted or None in accepted:
        return None
    return list(dict.fromkeys(accepted))


def _common(accepted: list[str] | None, names: Names) -> str | None:
    """One type for several, or None when they do not agree."""
    if not accepted:
        return None
    return accepted[0] if len(accepted) == 1 else names.common_base(accepted)


def _observed(observations: list[dict], names: Names) -> Observed | None:
    seen = [
        observation for observation in observations
        if 'error' not in observation and observation['type'] != NONE_TYPE
    ]
    kinds = {observation['type'] for observation in seen}
    if not seen:
        return None

    if len(kinds) == 1 and kinds <= set(SEQUENCES):
        [container] = kinds
        elements = _accepted(
            {element for observation in seen for element in observation['elements']}, names,
        )
        element = _common(elements, names)
        if element is None:
            return Observed(Candidate(container, 'probe_weak'), ())

        suffix = ', ...' if container == 'builtins.tuple' else ''
        each = tuple(f'{container}[{one}{suffix}]' for one in elements)
        return Observed(Candidate(f'{container}[{element}{suffix}]', 'probe'), each)

    if kinds == {DICT}:
        keys = _accepted({key for observation in seen for key in observation['keys']}, names)
        values = _accepted(
            {value for observation in seen for value in observation['values']}, names,
        )
        key = _common(keys, names)
        value = _common(values, names)
        if key is None or value is None:
            return Observed(Candidate(DICT, 'probe_weak'), ())

        each = tuple(f'{DICT}[{one_key}, {one}]' for one_key in keys for one in values)
        return Observed(Candidate(f'{DICT}[{key}, {value}]', 'probe'), each)

    if kinds & (set(SEQUENCES) | {DICT}):
        # A container on one receiver and something else on another.
        return None

    accepted = _accepted(kinds, names)
    found = _common(accepted, names)
    return Observed(Candidate(found, 'probe'), tuple(accepted)) if found else None


def load_observations(path: Path, names: Names) -> dict[str, Observed]:
    """Map each probed path to what its observations support."""
    raw = json.loads(path.read_text(encoding='utf-8'))
    if raw.get('schema') != SCHEMA:
        raise ValueError(f'{path}: schema {raw.get("schema")!r}, expected {SCHEMA}')

    candidates = {}
    for target, observations in raw['observations'].items():
        observed = _observed(observations, names)
        if observed:
            candidates[target] = observed
    return candidates
