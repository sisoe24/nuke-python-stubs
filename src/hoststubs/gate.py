"""Checks that every build must pass. Any finding fails the build.

1. Every stub file parses.
2. No undefined name, no redefinition, no syntax-level error (ruff F821, F811, E9).
3. Pyright, at the pinned version, reveals the same type for every expression
   in `tests/corpus/` as the snapshot for this host version says, and reports
   the same errors on the lines that are wrong on purpose.

The corpus is the accuracy measure. A snapshot holds concrete types, so a
symbol that falls back to Any fails. Never make a failure pass by updating
the snapshot: fix the resolver or add an override.
"""
from __future__ import annotations

import os
import re
import ast
import sys
import json
import tempfile
import subprocess
from pathlib import Path

from hoststubs.host import REPO

CORPUS = REPO / 'tests' / 'corpus'
SNAPSHOTS = CORPUS / 'snapshots'
RUFF_RULES = 'F821,F811,E9'
REVEALED = re.compile(r'^Type of "(?P<expression>.+)" is "(?P<type>.+)"$', re.DOTALL)


def check_syntax(stubs: Path) -> list[str]:
    findings = []
    for path in sorted(stubs.rglob('*.pyi')):
        try:
            ast.parse(path.read_text(encoding='utf-8'))
        except SyntaxError as error:
            findings.append(f'{path}:{error.lineno}: {error.msg}')
    return findings


def check_names(stubs: Path) -> list[str]:
    command = [
        sys.executable, '-m', 'ruff', 'check', '--isolated', '--no-cache',
        '--select', RUFF_RULES, '--output-format', 'concise', str(stubs),
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        return []
    return [line for line in result.stdout.splitlines() if re.match(r'.+:\d+:\d+: ', line)]


def run_corpus(stubs: Path, python: str) -> dict[str, dict[str, dict[str, str]]]:
    """Run pyright over the corpus against `stubs`.

    Returns, per corpus file, the revealed type of each expression and the
    rule of each error keyed by the source line it is on.
    """
    with tempfile.TemporaryDirectory() as project:
        # Pyright ignores an absolute path in `include`.
        config = {
            'include': [os.path.relpath(CORPUS, project)],
            'extraPaths': [str(stubs.resolve())],
            'pythonVersion': '.'.join(python.split('.')[:2]),
        }
        (Path(project) / 'pyrightconfig.json').write_text(json.dumps(config), encoding='utf-8')
        result = subprocess.run(
            [sys.executable, '-m', 'pyright', '--outputjson', '-p', project],
            capture_output=True, text=True,
        )

    report = json.loads(result.stdout)
    found: dict[str, dict[str, dict[str, str]]] = {}
    sources: dict[str, list[str]] = {}

    for diagnostic in report['generalDiagnostics']:
        path = Path(diagnostic['file'])
        entry = found.setdefault(path.name, {'revealed': {}, 'errors': {}})
        revealed = REVEALED.match(diagnostic['message'])

        if diagnostic['severity'] == 'information' and revealed:
            entry['revealed'][revealed.group('expression')] = revealed.group('type')
        elif diagnostic['severity'] == 'error':
            lines = sources.setdefault(path.name, path.read_text(encoding='utf-8').splitlines())
            line = lines[diagnostic['range']['start']['line']].strip()
            entry['errors'][line] = diagnostic.get('rule', diagnostic['message'].splitlines()[0])
    return found


def snapshot_path(host: str, version: str) -> Path:
    return SNAPSHOTS / f'{host}-{version}.json'


def write_snapshot(found: dict, host: str, version: str) -> Path:
    path = snapshot_path(host, version)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(found, indent=1, sort_keys=True) + '\n', encoding='utf-8')
    return path


def check_corpus(found: dict, host: str, version: str) -> list[str]:
    path = snapshot_path(host, version)
    if not path.exists():
        return [f'{path}: no snapshot for this version']
    expected = json.loads(path.read_text(encoding='utf-8'))

    findings = []
    for file in sorted(set(expected) | set(found)):
        for kind in ('revealed', 'errors'):
            want = expected.get(file, {}).get(kind, {})
            got = found.get(file, {}).get(kind, {})
            for key in sorted(set(want) | set(got)):
                if want.get(key) != got.get(key):
                    findings.append(
                        f'{file}: {key}\n    expected {want.get(key)}\n    got      {got.get(key)}',
                    )
    return findings


def gate(stubs: Path, host: str, version: str, python: str) -> list[str]:
    """Run every check and return the findings. An empty list means the build passes."""
    findings = check_syntax(stubs) + check_names(stubs)
    return findings + check_corpus(run_corpus(stubs, python), host, version)
