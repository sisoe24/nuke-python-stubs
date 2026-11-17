# nuke-stubs

Type stubs for the Nuke and Hiero Python API. They let your editor and type checker autocomplete and check the `nuke`, `nukescripts`, `nuke_internal`, `ocionuke` and `hiero` modules. The stubs have signatures, types and the original docstrings.

This release is for Nuke {host_version}.

## Install

Install the package into the environment your editor or type checker uses. Without a version, pip installs the stubs for the newest Nuke:

```bash
pip install nuke-stubs
```

For an older Nuke, pin the version:

```bash
pip install "nuke-stubs==15.2.*"
```

The package version is the Nuke version followed by a stub revision: `15.2.9.0` is Nuke 15.2v9, revision 0. The release history lists the Nuke versions that have stubs. If there are no stubs for your Nuke version, use the closest one.

One environment holds stubs for one Nuke version. Do not install `types-nuke` in the same environment, because both packages write the `nuke-stubs` folder.

## Types

Nuke ships no type information. The types come from the docstrings, from calls inside Nuke, from Pyright for the Python modules, and from hand-written overrides. `Any` means that no type was found, not that any type is valid.

A type can be wrong. To report or fix one, see the [repository](https://github.com/sisoe24/nuke-python-stubs).
