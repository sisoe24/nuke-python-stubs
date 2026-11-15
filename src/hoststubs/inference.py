"""Track A, offline step: read pyright's draft stubs into type candidates."""
from __future__ import annotations

import re
import ast
import json
from pathlib import Path
from dataclasses import dataclass

from hoststubs.infer import EMPTY_BODIES
from hoststubs.names import Names

ANY = 'typing.Any'

# Pyright writes an inferred return type as a comment: `def f(x): # -> list[Any]:`
INFERRED_RETURN = re.compile(r'# -> (.+):\s*$')

ACCESSOR_DECORATORS = ('setter', 'deleter')


@dataclass(frozen=True)
class Inferred:
    """Types for one function. None and a missing parameter mean no evidence."""
    returns: str | None
    params: dict[str, str]


class _Normalizer:
    """Turn an annotation as written in one module into fully qualified, accepted names."""

    def __init__(self, names: Names, module: str) -> None:
        self._names = names
        self._module = module

    # === PRIVATE === #

    def _literal(self, node: ast.expr) -> str | None:
        """Widen one `Literal[...]` element to its type."""
        if isinstance(node, ast.Constant):
            return 'None' if node.value is None else f'builtins.{type(node.value).__name__}'
        if isinstance(node, ast.UnaryOp) and isinstance(node.operand, ast.Constant):
            return f'builtins.{type(node.operand.value).__name__}'
        if isinstance(node, ast.Attribute):
            # An enum member: the type is the enum class.
            return self._names.resolve(ast.unparse(node.value), self._module)
        return None

    def _union(self, members: list[str | None]) -> str | None:
        if None in members or ANY in members:
            return None
        return ' | '.join(dict.fromkeys(members))

    def _argument(self, node: ast.expr) -> str:
        if isinstance(node, ast.Constant) and node.value is Ellipsis:
            return '...'
        if isinstance(node, ast.List):
            return '[' + ', '.join(self._argument(item) for item in node.elts) + ']'
        return self.normalize(node) or ANY

    def _subscript(self, node: ast.Subscript) -> str | None:
        arguments = node.slice.elts if isinstance(node.slice, ast.Tuple) else [node.slice]

        if ast.unparse(node.value) == 'Literal':
            return self._union([self._literal(argument) for argument in arguments])

        container = self.normalize(node.value)
        if container is None:
            return None
        return f'{container}[{", ".join(self._argument(argument) for argument in arguments)}]'

    def _union_members(self, node: ast.expr) -> list[ast.expr]:
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
            return self._union_members(node.left) + self._union_members(node.right)
        return [node]

    # === PUBLIC === #

    def normalize(self, node: ast.expr) -> str | None:
        if isinstance(node, ast.Constant) and node.value is None:
            return 'None'
        if isinstance(node, (ast.Name, ast.Attribute)):
            dotted = ast.unparse(node)
            if dotted == 'LiteralString':
                return 'builtins.str'
            return self._names.resolve(dotted, self._module)
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
            return self._union([self.normalize(member) for member in self._union_members(node)])
        if isinstance(node, ast.Subscript):
            return self._subscript(node)
        return None


def normalize(annotation: str, names: Names, module: str) -> str | None:
    """Return the accepted, fully qualified form of `annotation`, or None for no evidence."""
    try:
        tree = ast.parse(annotation.strip(), mode='eval')
    except SyntaxError:
        # Pyright prints some types that are not Python, such as `(x) -> None`.
        return None

    result = _Normalizer(names, module).normalize(tree.body)
    return None if result == ANY else result


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
