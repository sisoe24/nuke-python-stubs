"""Track A, offline step: read pyright's draft stubs into type candidates."""
from __future__ import annotations

import re
import ast
import json
from pathlib import Path
from dataclasses import dataclass

from hoststubs.infer import EMPTY_BODIES
from hoststubs.names import Names
from hoststubs.annotations import normalize

# Pyright writes an inferred return type as a comment: `def f(x): # -> list[Any]:`
INFERRED_RETURN = re.compile(r'# -> (.+):\s*$')

ACCESSOR_DECORATORS = ('setter', 'deleter')


@dataclass(frozen=True)
class Inferred:
    """Types for one function. None and a missing parameter mean no evidence."""
    returns: str | None
    params: dict[str, str]


def _is_accessor(function: ast.FunctionDef | ast.AsyncFunctionDef) -> bool:
    return any(
        isinstance(decorator, ast.Attribute) and decorator.attr in ACCESSOR_DECORATORS
        for decorator in function.decorator_list
    )


def _return_annotation(function: ast.FunctionDef, lines: list[str]) -> str | None:
    if function.returns is not None:
        return ast.unparse(function.returns)

    match = INFERRED_RETURN.search(lines[function.lineno - 1])
    return match.group(1) if match else None


def _load_module(
    path: Path, module: str, names: Names, empty: frozenset[str],
) -> dict[str, Inferred]:
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    found: dict[str, Inferred] = {}

    def visit(scope: ast.AST, prefix: str) -> None:
        for node in ast.iter_child_nodes(scope):
            if isinstance(node, ast.ClassDef):
                visit(node, f'{prefix}.{node.name}')
                continue
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) or _is_accessor(node):
                continue

            key = f'{prefix}.{node.name}'
            if key in found:
                continue

            returns = None
            written = _return_annotation(node, lines)
            is_hook = key in empty and node.name != '__init__'
            if written and not is_hook:
                returns = normalize(written, names, module)

            params = {}
            arguments = node.args
            for argument in arguments.posonlyargs + arguments.args + arguments.kwonlyargs:
                if argument.annotation is not None:
                    accepted = normalize(ast.unparse(argument.annotation), names, module)
                    if accepted:
                        params[argument.arg] = accepted

            found[key] = Inferred(returns=returns, params=params)

    visit(ast.parse(text), module)
    return found


def load_inference(directory: Path, names: Names) -> dict[str, Inferred]:
    """Map `module.qualname` to the types pyright inferred for it."""
    empty = frozenset(json.loads((directory / EMPTY_BODIES).read_text(encoding='utf-8')))

    found: dict[str, Inferred] = {}
    for path in sorted(directory.rglob('*.pyi')):
        parts = path.relative_to(directory).with_suffix('').parts
        if parts[-1] == '__init__':
            parts = parts[:-1]
        found.update(_load_module(path, '.'.join(parts), names, empty))
    return found
