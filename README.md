# Nuke python stubs

Type stubs for the Nuke and Hiero Python API. They let your editor autocomplete the `nuke`, `nukescripts`, `nuke_internal`, `ocionuke` and `hiero` modules. The `.pyi` files have signatures, types and the original docstrings.

The docstrings of Nuke's C functions are short, sometimes wrong, and often have no types. The generator also runs the functions inside Nuke and records what they return. To find the parameter types, it calls a function with an argument that cannot be valid and reads the error message.

![Alt text](images/auto_complete.gif)

## Use the stubs

With Visual Studio Code, install [NukeTools](https://marketplace.visualstudio.com/items?itemName=virgilsisoe.nuke-tools) and run `Nuke Tools: Add Python Stubs`.

Otherwise, download the zip for your Nuke version from [Releases](https://github.com/sisoe24/nuke-python-stubs/releases), unzip it, and point your editor at the folder. For VS Code with Pylance, add this to `.vscode/settings.json`:

```json
{
    "python.analysis.extraPaths": ["/path/to/nuke-python-stubs-15.2v9"]
}
```

There is one zip per Nuke version: 15.2v9 and 17.1v2. Use the closest to your Nuke. The build also lays out a `nuke-stubs` pip package in `build/<version>/package/`.

## Type guess

Nuke ships no type information, so the generator guesses. A type comes from one of these places:

- The docstring of a function, when it names a type.
- A call inside Nuke. The return type is what the function returned in a test scene. For the parameters, the function is called with an argument that cannot be valid, and the error message names the type it wanted.
- Pyright, for `hiero`, `nukescripts`, `nuke_internal` and `ocionuke`, which are Python code.
- The override files, for a type that is still wrong.

The type `Any` means the generator found no type, not that any type is valid. Knob values, like `node['size'].value()`, are `Any`. Qt types are `Any` on Nuke 15, because PySide2 has no type information. On Nuke 17 they are PySide6 types.

> [!IMPORTANT]
> A guess can be wrong. See [Fix a wrong type](#fix-a-wrong-type).

## Not done

- I have not tested this on Windows or Linux.
- `hiero` C functions get parameter counts but no parameter types. Their error messages do not say.
- Python functions are not probed for parameters, because they check nothing.
- `stubtest` does not cover `hiero` or the GUI-only `nukescripts` panels.
- The `nuke-stubs` pip package is built but not published.

## Regenerate

The generator is in `src/hoststubs/`. It needs [`uv`](https://docs.astral.sh/uv/). Dumping a new Nuke version also needs Nuke with a licence.

To rebuild the stubs from the committed data:

```bash
uv run python -m hoststubs build data/nuke/15.2v9/dump.json
```

This writes `build/nuke-15.2v9/`, then checks it: every file parses, every name resolves, and the type-check corpus in `tests/corpus` matches its snapshot. It also writes `build/nuke-python-stubs-15.2v9.zip`, the file attached to a release.

To add a Nuke version, run these steps in order. Each page lists the exact commands:

1. Dump the API: [docs/dump-schema.md](docs/dump-schema.md)
2. Infer types for the Python modules: [docs/inference.md](docs/inference.md)
3. Probe return and parameter types: [docs/probe.md](docs/probe.md)
4. Build, as above.

`uv run python -m hoststubs report data/nuke/17.1v2/dump.json` shows how much of the API each step resolved.

## Fix a wrong type

Add an entry to the override file for the module, for example `src/hoststubs/hosts/nuke/overrides/nuke.pyi`. It is a normal stub line:

```python
def toNode(s: str) -> Node | None: ...
```

The format is at the top of `src/hoststubs/overrides.py`. The build fails on a type it cannot resolve. Then run `uv run pytest -q` and build again.

## Acknowledgment

The PyCharm stub generator inspired this project.
