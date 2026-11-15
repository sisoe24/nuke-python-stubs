from __future__ import annotations

import os
import ast
import sys
import json
import subprocess
from pathlib import Path

from hoststubs.host import DUMP_SCRIPT

FIXTURES = Path(__file__).parent / 'fixtures'
GOLDEN = FIXTURES / 'dump.golden.json'

# Regenerate the golden file with the command in docs/dump-schema.md.
DUMP_ARGS = [
    'host=fxhost', 'version=fxhost.VERSION', 'skip=fxscripts.examples', 'fxhost', 'fxscripts',
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


def test_dump_parses_as_python37() -> None:
    """The dump script uses only syntax that Python 3.7 accepts."""
    ast.parse(DUMP_SCRIPT.read_text(encoding='utf-8'), feature_version=(3, 7))


def test_dump_imports_only_stdlib() -> None:
    """The dump script must run in a host that has no extra packages."""
    tree = ast.parse(DUMP_SCRIPT.read_text(encoding='utf-8'))

    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split('.')[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.add(node.module.split('.')[0])

    assert imported <= sys.stdlib_module_names
