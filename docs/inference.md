# Inference for the Python modules

`hiero`, `nukescripts`, `nuke_internal` and `ocionuke` are Python source
with real bodies and few annotations. Pyright infers their return types.

## Run pyright

Needs the host install on disk (the files, not a licence). Run once per
host version, from the repository root:

```bash
uv run python -m hoststubs infer data/nuke/17.1v2/dump.json /Applications/Nuke17.1v2/Nuke17.1v2.app/Contents/MacOS/plugins /Applications/Nuke17.1v2/Nuke17.1v2.app/Contents/Resources/pythonextensions/site-packages
```

It writes `data/<host>/<version>/inference/`:

- pyright's draft stubs (`pyright --createstub`, version pinned in
  `pyproject.toml`): signatures, docstrings and inferred return types as
  `# -> T:` comments. No function bodies.
- `empty_bodies.json`: functions whose body is only a docstring, `pass`,
  `...` or `raise`.

Both are committed. Everything after this step runs without the host.

## Read the result

`hoststubs.inference.load_inference` reads that directory into candidates
keyed by `module.qualname`, which is the `origin` and `qualname` of a
function in the dump. Types are fully qualified (`builtins.list[nuke.Node]`).

Rules, each with a test in `tests/test_inference.py`:

| Pyright wrote | Candidate | Why |
|---|---|---|
| `Literal[False]`, `LiteralString` | `bool`, `str` | A literal is one observed value. |
| A name the module namespace does not hold | none | Pyright prints short names. A short name is not looked up across the dump: that would be a guess. |
| A union that contains `Any` | none | It says no more than `Any`. |
| `list[Any]` | `list[Any]` | The container is known. |
| A Qt class, host on PySide2 | none | PySide2 ships no types, so no consumer could resolve the name. |
| `None` for a function in `empty_bodies.json` | none | A hook that subclasses override. `__init__` is exempt. |
| A type that is not Python, such as `(x) -> None` | none | |

Names are resolved through the dump: the module's runtime namespace says
what a name means. `hoststubs.names.Names.accept` is the acceptance rule
every source of types uses.

## Limits

- Pyright omits private functions. Functions that hiero attaches to C
  classes under a public name (`Clip.addToNukeScript` is
  `_Clip_addToNukeScript`) get no candidate.
- Pyright does not infer parameter types. Only source annotations pass
  through.
- Pyright runs without stubs for `nuke`, so a return value that comes from
  a `nuke` call is unknown. Rerunning with the emitted stubs on the path is
  possible.
