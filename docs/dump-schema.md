# Dump schema (version 1)

`src/hoststubs/inhost/dump.py` writes this file inside the host. `src/hoststubs/ir.py`
loads it offline. The dump records what the runtime reports. It decides
nothing about types.

To make a dump, see [new-version.md](new-version.md).

## Test fixture

Regenerate the test fixture with:

```bash
PYTHONPATH=tests/fixtures/host python src/hoststubs/inhost/dump.py tests/fixtures/dump.golden.json host=fxhost version=fxhost.VERSION skip=fxscripts.examples private=fxcore:fxhost fxhost fxscripts
```

## Top level

| Key | Content |
|---|---|
| `schema` | `1` |
| `host` | `{"name", "version"}`. `version` is the raw host string, for example `15.0v1`. |
| `python`, `platform` | Interpreter version and `sys.platform`. |
| `qt` | `{"binding", "version"}` of the Qt binding the host imported, or `null`. |
| `modules` | Module name to module entry. Each root and every submodule that imports. |
| `foreign` | Top-level package name to count of references that point outside the roots. A host package here means a root or a `private` module is missing from the host config. |
| `errors` | `{"where", "error"}` for each module that failed to import and each member that failed to dump. |

## Module entry

`doc` (every `doc` in the file is passed through `inspect.cleandoc`), `file` (relative to the package parent, never an absolute path),
`all` (only when the module defines `__all__`), and `members`: name to
member. Module dunders are left out.

## Members

Each member has a `kind`:

| `kind` | Fields | Meaning |
|---|---|---|
| `class` | `origin`, `qualname`, `bases`, `doc`, `members`, `final` | `final` exists and is true for a C type that cannot be subclassed. `origin` is `__module__`. `members` come from the class `__dict__` only, so inherited members appear on the base. |
| `function` | `descriptor`, `origin`, `qualname`, `doc`, `signature`, `text_signature`, `binding` | Any callable routine, except Qt signals, which are values. `descriptor` is the runtime type, for example `builtins.method_descriptor`. `binding` exists on class members: `instance`, `static` or `class`. |
| `property` | `descriptor`, `doc`, `settable`, `getter` | Any data descriptor. `settable` and `getter` (a function entry) exist for Python `property` only. |
| `value` | `type`, `repr` | Everything else. `repr` exists for `bool`, `int`, `float` and `None`. String values are left out because they can hold paths of the dumping machine. |
| `alias` | `target` | The object is defined at `target`. |
| `module` | `target` | A reference to a module. |
| `error` | `error` | The member could not be dumped. |

`signature` is `null` when `inspect.signature` fails, which is normal for
C functions. Otherwise it is `{"params", "returns"}`. Each parameter has
`name`, `kind` (the `inspect.Parameter` kind name), `annotation` (a string
or `null`), and `default` (a value entry, with `repr` for strings too)
when the parameter has one.

## Where an object is recorded

An object can be visible from many modules. It is recorded in full once:

1. Its `__module__` is under a root: in that module. Other places get an alias.
2. Its `__module__` is importable, holds the object, and is public or part
   of the standard library (Qt, `os`, `_io`): alias only. Counted in `foreign`.
3. Otherwise: in the first public place that shows
   it, in root order. Later places get an alias to that place. This covers
   a private C module (`_nuke`) and a `__module__` that cannot be imported
   (Nuke classes report `builtins`).
4. Its `__module__` is declared `private` with an owner (`core:hiero.core`):
   in the owner, when the owner holds it. hiero's C modules import as
   top-level `core` and `ui` in a GUI session, and several hiero modules
   re-export their classes; without the owner, the first of them in
   alphabetical order would get the class.

Functions in a class `__dict__` are always recorded in full, under the
attribute name. `qualname` keeps the original name, which is how hiero's
`Clip.addToNukeScript = _Clip_addToNukeScript` stays visible.
