from __future__ import annotations

import os
import sys
import json
import subprocess
from pathlib import Path

from hoststubs.host import DUMP_SCRIPT

FIXTURES = Path(__file__).parent / 'fixtures'
GOLDEN = FIXTURES / 'dump.golden.json'

# Regenerate the golden file with the command in docs/dump-schema.md.
DUMP_ARGS = [
    'host=fxhost', 'version=fxhost.VERSION', 'skip=fxscripts.examples',
    'private=fxcore:fxhost', 'fxhost', 'fxscripts',
]


def _without_interpreter(dump: dict) -> dict:
    return {key: value for key, value in dump.items() if key not in ('python', 'platform')}


def test_dump_matches_golden(tmp_path: Path) -> None:
    """Dumping the fixture host reproduces the golden file."""
    out = tmp_path / 'dump.json'
    env = {**os.environ, 'PYTHONPATH': str(FIXTURES / 'host')}

    subprocess.run([sys.executable, str(DUMP_SCRIPT), str(out), *DUMP_ARGS], env=env, check=True)

    dumped = json.loads(out.read_text(encoding='utf-8'))
    golden = json.loads(GOLDEN.read_text(encoding='utf-8'))
    assert _without_interpreter(dumped) == _without_interpreter(golden)
