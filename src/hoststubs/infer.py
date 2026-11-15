"""Track A, machine step: infer types for the host's pure-Python modules.

Needs the host's Python source on disk, so it runs where the host is
installed. It writes pyright's draft stubs (signatures and docstrings, no
bodies) and a list of functions with an empty body. Both are committed, so
the rest of the build needs no host install.
"""
from __future__ import annotations

import ast
import sys
import json
import shutil
import logging
import tempfile
import subprocess
from pathlib import Path

from hoststubs import ir

LOGGER = logging.getLogger(__name__)

INFERENCE = Path(__file__).parents[2] / 'inference'
EMPTY_BODIES = 'empty_bodies.json'


def inference_dir(dump: ir.Dump) -> Path:
    return INFERENCE / f'{dump.host}-{dump.host_version}'


def _source_packages(dump: ir.Dump, search: list[Path]) -> dict[str, Path]:
    """Top-level Python packages of the dump, mapped to the search directory that holds them."""
    names = sorted({
        name.split('.')[0]
        for name, module in dump.modules.items()
        if module.file and module.file.endswith('.py')
    })

    packages = {}
    for name in names:
        holder = next((directory for directory in search if (directory / name).is_dir()), None)
        if holder is None:
            LOGGER.warning('No source directory for %s in %s', name, [str(d) for d in search])
            continue
        packages[name] = holder
    return packages


def _is_empty_body(function: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    """True when the body says nothing about the return value.

    A docstring, `pass`, `...` or a bare `raise` marks a hook that subclasses
    override, so pyright's inferred `None` (or `NoReturn`) is not evidence.
    """
    for statement in function.body:
        is_constant = isinstance(statement, ast.Expr) and isinstance(statement.value, ast.Constant)
        if not is_constant and not isinstance(statement, (ast.Pass, ast.Raise)):
            return False
    return True


def _empty_bodies(tree: ast.AST, prefix: str) -> list[str]:
    found = []
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.ClassDef):
            found += _empty_bodies(node, f'{prefix}.{node.name}')
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and _is_empty_body(node):
            found.append(f'{prefix}.{node.name}')
    return found


def _module_name(path: Path, root: Path) -> str:
    parts = path.relative_to(root).with_suffix('').parts
    if parts[-1] == '__init__':
        parts = parts[:-1]
    return '.'.join(parts)


def find_empty_bodies(packages: dict[str, Path]) -> list[str]:
    found = []
    for name, holder in packages.items():
        for path in sorted((holder / name).rglob('*.py')):
            try:
                tree = ast.parse(path.read_text(encoding='utf-8', errors='replace'))
            except SyntaxError as error:
                LOGGER.warning('Cannot parse %s: %s', path, error)
                continue
            found += _empty_bodies(tree, _module_name(path, holder))
    return sorted(found)


def create_stubs(packages: dict[str, Path], python: str, out: Path) -> None:
    with tempfile.TemporaryDirectory() as project:
        config = {
            'extraPaths': sorted({str(holder) for holder in packages.values()}),
            'pythonVersion': '.'.join(python.split('.')[:2]),
        }
        (Path(project) / 'pyrightconfig.json').write_text(json.dumps(config), encoding='utf-8')

        for name in packages:
            subprocess.run(
                [sys.executable, '-m', 'pyright', '--createstub', name], cwd=project, check=True,
            )
            shutil.move(Path(project) / 'typings' / name, out / name)


def infer(dump_path: Path, search: list[Path]) -> Path:
    dump = ir.load(dump_path)
    # Pyright runs in a temporary directory, so relative paths would not resolve.
    packages = _source_packages(dump, [directory.resolve() for directory in search])

    out = inference_dir(dump)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    create_stubs(packages, dump.python, out)

    empty = find_empty_bodies(packages)
    (out / EMPTY_BODIES).write_text(json.dumps(empty, indent=1) + '\n', encoding='utf-8')

    LOGGER.info('Wrote %s: %d packages, %d empty bodies.', out, len(packages), len(empty))
    return out
