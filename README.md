# Nuke python stubs

Type stubs for the Nuke and Hiero Python API. They let your editor autocomplete the `nuke`, `nukescripts`, `nuke_internal`, `ocionuke` and `hiero` modules. The `.pyi` files have signatures, types and the original docstrings.

The docstrings of Nuke's C functions are short, sometimes wrong, and often have no types. The generator also runs the functions inside Nuke and records what they return. To find the parameter types, it calls a function with an argument that cannot be valid and reads the error message.

![Alt text](images/auto_complete.gif)

## Use the stubs

Install the `nuke-stubs` package from PyPI into the environment your editor or type checker uses. Pin the version to your Nuke version:

```bash
pip install "nuke-stubs==15.2.*"
```

The package version is the Nuke version followed by a stub revision: `15.2.9.0` is Nuke 15.2v9, revision 0. With `==15.2.*`, pip installs the newest stubs for Nuke 15.2. If there are no stubs for your Nuke version, use the closest one. For example, `"nuke-stubs>=15,<16"` installs the newest stubs for Nuke 15. Do not install without a pin: pip then installs the stubs for the newest Nuke.

One environment holds stubs for one Nuke version. Do not install `types-nuke` in the same environment, because both packages write the `nuke-stubs` folder.

With Visual Studio Code, you can also install [NukeTools](https://marketplace.visualstudio.com/items?itemName=virgilsisoe.nuke-tools) and run `Nuke Tools: Add Python Stubs`.

You can also download the zip for your Nuke version from [Releases](https://github.com/sisoe24/nuke-python-stubs/releases), unzip it, and point your editor at the folder. For VS Code with Pylance, add this to `.vscode/settings.json`:

```json
{
    "python.analysis.extraPaths": ["/path/to/nuke-python-stubs-15.2v9"]
}
```

There is one zip per Nuke version. Use the closest to your Nuke. The stubs were tested on macOS only.

## Where types come from

Nuke ships no type information. The generator takes each type from one of these places:

- The docstring of a function, when it names a type.
- A call inside Nuke. The return type is what the function returned in a test scene. For the parameters, the function is called with an argument that cannot be valid, and the error message names the type it wanted.
- Pyright, for `hiero`, `nukescripts`, `nuke_internal` and `ocionuke`, which are Python code.
- The override files, for a type that is still wrong.

The type `Any` means the generator found no type, not that any type is valid. Knob values, like `node['size'].value()`, are `Any`. Qt types are `Any` on Nuke 15, because PySide2 has no type information. On Nuke 17 they are PySide6 types. Parameters are `Any` more often than return types, most of all in `hiero` and the Python modules.

> [!IMPORTANT]
> A type can be wrong. See [Fix a wrong type](#fix-a-wrong-type).

## Build

The generator is in `src/hoststubs/`. It needs [`uv`](https://docs.astral.sh/uv/). Dumping a new Nuke version also needs Nuke with a licence.

To rebuild the stubs from the committed data:

```bash
uv run python -m hoststubs build data/nuke/15.2v9/dump.json
```

This writes `build/nuke-15.2v9/`, then checks it: every file parses, every name resolves, and the type-check corpus in `tests/corpus` matches its snapshot. It also writes `build/nuke-python-stubs-15.2v9.zip`, the file attached to a release.

To add a Nuke version, follow [docs/new-version.md](docs/new-version.md).

## Fix a wrong type

Add an entry to the override file for the module, for example `src/hoststubs/hosts/nuke/overrides/nuke.pyi`. It is a normal stub line:

```python
def toNode(s: str) -> Node | None: ...
```

The format is at the top of `src/hoststubs/overrides.py`. The build fails on a type it cannot resolve. Then run `uv run pytest -q` and build again.

## Older versions

Releases up to [v0.3.1](https://github.com/sisoe24/nuke-python-stubs/releases/tag/v0.3.1) are `.py` stubs from the previous generator, which read the types from the docstrings. Use them if the current stubs do not work for you. All releases are on the [Releases](https://github.com/sisoe24/nuke-python-stubs/releases) page.

## Acknowledgment

The PyCharm stub generator inspired this project.
