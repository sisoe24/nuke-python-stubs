# Nuke python stubs

Type stubs for Nuke and Hiero Python. The `.pyi` files carry signatures, types and the original docstrings, so your editor can autocomplete the `nuke`, `nukescripts`, `nuke_internal`, `ocionuke` and `hiero` modules. They contain no Foundry source code.

![Alt text](images/auto_complete.gif)

## Use the stubs

With Visual Studio Code, install [NukeTools](https://marketplace.visualstudio.com/items?itemName=virgilsisoe.nuke-tools) and run the command `Nuke Tools: Add Python Stubs`.

Manually, point your editor at the `stubs/` directory of this repository. For VS Code with Pylance, add it to `.vscode/settings.json`:

```json
{
    "python.analysis.extraPaths": ["/path/to/nuke-python-stubs/stubs"]
}
```

The committed `stubs/` tree is built from Nuke 15.2v9. A tree for Nuke 17.1v2 can be built too, see [Regenerate](#regenerate).

A pip-installable package layout named `nuke-stubs` is also produced under `build/<version>/package/`. It is not published yet.

## What to expect

Numbers for Nuke 15.2v9:

- `nuke` C functions: 82% of return types and 65% of parameters are typed.
- `hiero` C functions: 46% of return types are typed.
- Python modules (`nukescripts`, `hiero`): 66 to 80% of return types are typed.

Anything unknown is `Any`, never a guess. Knob values (`node['size'].value()`) are `Any`. On Nuke 15 Qt types are `Any`, because PySide2 ships no type information. On Nuke 17 they are PySide6 types.

## How types are found

- A dump of the live API: every module, class, function and constant that Nuke reports.
- The docstrings: signature lines and fields such as `Returns` and `Parameters`.
- Pyright inference on the Python modules that ship with Nuke.
- Runtime probes inside Nuke: the type of what a call returns, and parameter types read from the errors of the argument parser.
- Hand-written overrides in `src/hoststubs/hosts/nuke/overrides/`.

## Regenerate

You need [`uv`](https://docs.astral.sh/uv/). To dump and probe you also need a Nuke install with a licence. Building from the committed data in `data/` needs neither.

Rebuild the stubs from the committed data:

```bash
uv run python -m hoststubs build data/nuke/15.2v9/dump.json
```

This writes `build/nuke-15.2v9/stubs/` (the plain stub tree) and `build/nuke-15.2v9/package/`, then runs a gate: the stubs must parse, every name must resolve, and the type-checking corpus in `tests/corpus` must match its snapshot. Building 15.2v9 also replaces `stubs/`.

To capture a new Nuke version, set `NUKE` to its executable (here Nuke 17.1v2) and run these from the repository root:

```bash
NUKE=/Applications/Nuke17.1v2/Nuke17.1v2.app/Contents/MacOS/Nuke17.1

# 1. Dump the API (opens Nuke Studio, dumps, quits)
NUKE_PATH="$PWD/src/hoststubs/hosts/nuke/studio:$NUKE_PATH" HOSTSTUBS_INHOST="$PWD/src/hoststubs/inhost" HOSTSTUBS_RUN=dump HOSTSTUBS_ARGS="$(uv run python -m hoststubs dump-arguments nuke "$PWD/data/nuke/17.1v2/dump.json")" $NUKE --studio

# 2. Infer types for the Python modules (needs the install files only)
uv run python -m hoststubs infer data/nuke/17.1v2/dump.json /Applications/Nuke17.1v2/Nuke17.1v2.app/Contents/MacOS/plugins /Applications/Nuke17.1v2/Nuke17.1v2.app/Contents/Resources/pythonextensions/site-packages

# 3. Probe return types, then parameter types
scripts/probe.sh 17.1v2 $NUKE nuke
scripts/probe.sh 17.1v2 $NUKE hiero
scripts/probe.sh 17.1v2 $NUKE nuke params

# 4. Build
uv run python -m hoststubs build data/nuke/17.1v2/dump.json
```

`uv run python -m hoststubs report data/nuke/17.1v2/dump.json` prints how much of the API each source resolved.

Details: [dump format and how to dump](docs/dump-schema.md), [inference](docs/inference.md), [probes](docs/probe.md).

## Fix a wrong type

Add an entry to the override file of that module, for example `src/hoststubs/hosts/nuke/overrides/nuke.pyi` for `nuke`. Each entry needs a `# src: manual` line above it:

```python
# verified: returns None for a name that does not exist.
# src: manual
def toNode(s: str) -> Node | None: ...
```

The format is described at the top of `src/hoststubs/overrides.py`. The build fails on a type it cannot resolve. Then run `uv run pytest -q` and the build.

## Acknowledgment

Pycharm Stub generator inspired the creation of this project.
