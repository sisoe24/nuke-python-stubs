# Nuke python stubs

Type stubs for the Nuke and Hiero Python API. They let your editor autocomplete the `nuke`, `nukescripts`, `nuke_internal`, `ocionuke` and `hiero` modules. The `.pyi` files have signatures, types and the original docstrings. They contain no Foundry source code.

![Alt text](images/auto_complete.gif)

## Use the stubs

With Visual Studio Code, install [NukeTools](https://marketplace.visualstudio.com/items?itemName=virgilsisoe.nuke-tools) and run `Nuke Tools: Add Python Stubs`.

Otherwise, point your editor at the `stubs/` folder of this repository. For VS Code with Pylance, add this to `.vscode/settings.json`:

```json
{
    "python.analysis.extraPaths": ["/path/to/nuke-python-stubs/stubs"]
}
```

`stubs/` is built from Nuke 15.2v9. You can build Nuke 17.1v2 too, see [Regenerate](#regenerate). The build also lays out a `nuke-stubs` pip package in `build/<version>/package/`. It is not published.

## What to expect

On Nuke 15.2v9:

- `nuke` C functions: 82% of return types and 65% of parameters are typed.
- `hiero` C functions: 46% of return types are typed.
- Python modules: 66 to 80% of return types are typed.

A type the generator cannot find is `Any`. Knob values, like `node['size'].value()`, are `Any`. Qt types are `Any` on Nuke 15, because PySide2 has no type information. On Nuke 17 they are PySide6 types.

`mypy stubtest`, run inside Nuke, found no wrong signature. I have not tested this on Windows or Linux.

## Regenerate

The generator is in `src/hoststubs/`. It needs [`uv`](https://docs.astral.sh/uv/). Dumping a new Nuke version also needs Nuke with a licence.

To rebuild the stubs from the committed data:

```bash
uv run python -m hoststubs build data/nuke/15.2v9/dump.json
```

This writes `build/nuke-15.2v9/`, then checks it: every file parses, every name resolves, and the type-check corpus in `tests/corpus` matches its snapshot. For 15.2v9 it also replaces `stubs/`.

To add a Nuke version, run these steps in order. Each page lists the exact commands:

1. Dump the API: [docs/dump-schema.md](docs/dump-schema.md)
2. Infer types for the Python modules: [docs/inference.md](docs/inference.md)
3. Probe return and parameter types: [docs/probe.md](docs/probe.md)
4. Build, as above.

`uv run python -m hoststubs report data/nuke/17.1v2/dump.json` shows how much of the API each step resolved.

## Fix a wrong type

Add an entry to the override file for the module, for example `src/hoststubs/hosts/nuke/overrides/nuke.pyi`. Put `# src: manual` on the line above it:

```python
# verified: returns None for a name that does not exist.
# src: manual
def toNode(s: str) -> Node | None: ...
```

The format is at the top of `src/hoststubs/overrides.py`. The build fails on a type it cannot resolve. Then run `uv run pytest -q` and build again.

## Acknowledgment

The PyCharm stub generator inspired this project.
