# Decisions

Choices that the code does not explain by itself, and the reason for each. When one place in the code owns a choice, the reason is a comment there and not here.

## Types from Pyright

The inference step reads Pyright's draft stubs for `hiero`, `nukescripts`, `nuke_internal` and `ocionuke`. Each row is one rule, and `tests/test_inference.py` has a test for each.

| Pyright wrote | Result | Reason |
|---|---|---|
| `Literal[False]`, `LiteralString` | `bool`, `str` | A literal is one observed value. |
| A name the module namespace does not hold | none | Pyright prints short names. A short name is not looked up across the dump, because that would be a guess. |
| A union that contains `Any` | none | It says no more than `Any`. |
| `list[Any]` | `list[Any]` | The container is known. |
| A Qt class, host on PySide2 | none | PySide2 ships no types, so no consumer could resolve the name. |
| `None` for a function in `empty_bodies.json` | none | The function is a hook that subclasses override. `__init__` is exempt. |
| A type that is not Python, such as `(x) -> None` | none | |

A name is resolved through the dump: the runtime namespace of the module says what the name means. `Names.accept` is the rule that every source of types uses.

## Stubtest findings that stay

`scripts/stubtest.sh` compares the built stubs with the live modules. These findings stay on purpose:

| Finding | Reason |
|---|---|
| `is a disjoint base`, `metaclass differs` | A stub cannot express them in a form that current checkers read. |
| `failed to import` | These are panels that exist only with the GUI. |
| `nuke_internal.os is not present in stub` and similar | The module's own imports, not API. |
| `nukescripts.pyQtExamples failed to find stubs` | The host config skips it: examples, not API. |
| `cannot be subclassed at runtime, but isn't marked with @final` | C code derives from that class, so `@final` would be wrong for its subclasses. |

## Known limits

- Pyright omits private functions. A function that hiero attaches to a C class under a public name gets no candidate. `Clip.addToNukeScript` is `_Clip_addToNukeScript`.
- Pyright does not infer parameter types. Only source annotations pass through.
- Pyright runs without stubs for `nuke`, so a return value that comes from a `nuke` call is unknown. Running it again with the emitted stubs on the path is possible.
- hiero's C functions report `Invalid arguments to core.TrackItem.setTimelineIn`. The parameter probe gets counts from that text and no types.
- Python functions check no arguments, so the parameter probe does not call them.
