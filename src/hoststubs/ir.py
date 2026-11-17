"""Typed view of a dump file. See docs/dump-schema.md."""
from __future__ import annotations

import json
from typing import Any
from pathlib import Path
from dataclasses import dataclass

SCHEMA = 1


@dataclass(frozen=True)
class Value:
    type: str
    repr: str | None


@dataclass(frozen=True)
class Param:
    name: str
    kind: str
    annotation: str | None
    default: Value | None


@dataclass(frozen=True)
class Signature:
    params: tuple[Param, ...]
    returns: str | None


@dataclass(frozen=True)
class Function:
    descriptor: str
    origin: str | None
    qualname: str | None
    doc: str | None
    signature: Signature | None
    text_signature: str | None
    binding: str | None


@dataclass(frozen=True)
class Property:
    descriptor: str
    doc: str | None
    settable: bool | None
    getter: Function | None


@dataclass(frozen=True)
class Alias:
    target: str
    is_module: bool


@dataclass(frozen=True)
class Failed:
    error: str


@dataclass(frozen=True)
class Class:
    origin: str | None
    qualname: str
    bases: tuple[str, ...]
    doc: str | None
    members: dict[str, Member]
    # True for a C type that cannot be subclassed.
    final: bool


Member = Class | Function | Property | Value | Alias | Failed


@dataclass(frozen=True)
class Module:
    doc: str | None
    file: str | None
    exported: tuple[str, ...] | None
    members: dict[str, Member]


@dataclass(frozen=True)
class Qt:
    binding: str
    version: str | None


@dataclass(frozen=True)
class Dump:
    host: str
    host_version: str
    python: str
    platform: str
    qt: Qt | None
    modules: dict[str, Module]
    foreign: dict[str, int]
    errors: tuple[dict[str, str], ...]


def _value(raw: dict[str, Any]) -> Value:
    return Value(type=raw['type'], repr=raw.get('repr'))


def _signature(raw: dict[str, Any] | None) -> Signature | None:
    if raw is None:
        return None

    params = tuple(
        Param(
            name=param['name'],
            kind=param['kind'],
            annotation=param['annotation'],
            default=_value(param['default']) if 'default' in param else None,
        )
        for param in raw['params']
    )
    return Signature(params=params, returns=raw['returns'])


def _function(raw: dict[str, Any]) -> Function:
    return Function(
        descriptor=raw['descriptor'],
        origin=raw['origin'],
        qualname=raw['qualname'],
        doc=raw['doc'],
        signature=_signature(raw['signature']),
        text_signature=raw['text_signature'],
        binding=raw.get('binding'),
    )


def _property(raw: dict[str, Any]) -> Property:
    return Property(
        descriptor=raw['descriptor'],
        doc=raw['doc'],
        settable=raw.get('settable'),
        getter=_function(raw['getter']) if 'getter' in raw else None,
    )


def _class(raw: dict[str, Any]) -> Class:
    return Class(
        origin=raw['origin'],
        qualname=raw['qualname'],
        bases=tuple(raw['bases']),
        doc=raw['doc'],
        members=_members(raw['members']),
        final=raw.get('final', False),
    )


def _member(raw: dict[str, Any]) -> Member:
    kind = raw['kind']
    if kind == 'class':
        return _class(raw)
    if kind == 'function':
        return _function(raw)
    if kind == 'property':
        return _property(raw)
    if kind == 'value':
        return _value(raw)
    if kind in ('alias', 'module'):
        return Alias(target=raw['target'], is_module=kind == 'module')
    if kind == 'error':
        return Failed(error=raw['error'])
    raise ValueError(f'Unknown member kind: {kind!r}')


def _members(raw: dict[str, dict[str, Any]]) -> dict[str, Member]:
    return {name: _member(member) for name, member in raw.items()}


def _module(raw: dict[str, Any]) -> Module:
    exported = raw.get('all')
    return Module(
        doc=raw['doc'],
        file=raw['file'],
        exported=tuple(exported) if exported is not None else None,
        members=_members(raw['members']),
    )


def load(path: Path) -> Dump:
    raw = json.loads(path.read_text(encoding='utf-8'))

    if raw.get('schema') != SCHEMA:
        raise ValueError(f'{path}: schema {raw.get("schema")!r}, expected {SCHEMA}')

    qt = raw['qt']
    return Dump(
        host=raw['host']['name'],
        host_version=raw['host']['version'],
        python=raw['python'],
        platform=raw['platform'],
        qt=Qt(binding=qt['binding'], version=qt['version']) if qt else None,
        modules={name: _module(module) for name, module in raw['modules'].items()},
        foreign=raw['foreign'],
        errors=tuple(raw['errors']),
    )
