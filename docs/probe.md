# Probe: observed return types

Many C functions take no arguments and say nothing usable in their
docstring. The probe calls them inside the host and records the type of
each result.

## Run

Two commands per version, from the repository root. Each needs a licence.

```bash
scripts/probe.sh 17.1v2 /Applications/Nuke17.1v2/Nuke17.1v2.app/Contents/MacOS/Nuke17.1 nuke
```

```bash
scripts/probe.sh 17.1v2 /Applications/Nuke17.1v2/Nuke17.1v2.app/Contents/MacOS/Nuke17.1 hiero
```

`nuke` probes `nuke` and `nuke_internal` in terminal mode with `--safe`
(no `~/.nuke` plugins). `hiero` probes `hiero` in a Nuke Studio GUI
session, because hiero exists only there; that session loads `~/.nuke`
plugins and its window appears on screen. Both restart with `resume` after
each crash. Outputs, both committed: `data/nuke/<version>/probe-nuke.json` and
`data/nuke/<version>/probe-hiero.json`. Work files go to `build/work/`.

## What is called

`python -m hoststubs probe-targets` picks, from the dump:

- C functions and methods that the docstring shows as callable without
  arguments, or whose parameters are unknown (a call that needs arguments
  fails with `TypeError` before it does anything);
- C properties, which are read, not called.

Not called: Python functions, dunders, any name that contains a word in
`probe_skip_words` (`scriptSaveAs` contains `save`), and the paths in
`probe_skip`. Both lists are in `src/hoststubs/hosts/nuke/config.py`. The paths were
found by running: each one ends the session.

Methods run first, on the scene as built. Module functions run after,
because some of them change the scene.

## Scene

`src/hoststubs/hosts/nuke/probe_scene.py` builds the Nuke scene: one node of each common
class in a chain, an animated knob, one user knob of each knob class,
formats, frame ranges. `src/hoststubs/hosts/nuke/probe_scene_hiero.py` builds the hiero
scene: a project, a sequence with a video and an audio track, a bin, a tag,
and a clip from a generated image placed on the video track. The list of
what was created is stored in the output as `scene`.

A method is called on one instance of every type that has it, so a method
of `Knob` is seen on every knob class before its result counts.

## Crashes and hangs

Before each call the target is appended to `<out>.journal` and synced to
disk. After a crash the last `>` line is the call that did it. `resume`
skips every journalled target; the final output lists the unfinished ones
as `crashed`. A call that runs longer than 30 seconds kills the process.
Add each crashing path to `probe_skip`.

## How observations are used

`hoststubs.observations` and `Resolver._with_probe`, with tests in
`tests/test_observations.py`:

| Observation | Result |
|---|---|
| `None` | Discarded. It means nothing was set. |
| List whose elements share a type or a base class | `list[T]` |
| Empty list, or elements with nothing in common | Bare `list`, ranked below all other evidence |
| Receivers disagree, classes with a common base | The base |
| Receivers disagree otherwise (`Knob.value`) | Nothing |
| Agrees with the docstring type (`Root` seen, docstring says `Node`) | The docstring type stays |
| Contradicts the docstring type, both are host classes (`Bin`, saw `Project`) | Both: `Bin \| Project` |
| Contradicts otherwise, or refines a bare container | The observed type |
| A subclass, with no docstring type | Its topmost base in the dump |

The last four rows are stricter than "the probe wins". An observation is
one object in one scene: it showed `Root` for `nuke.thisNode()` and a
single `Node` where the docstring says `Node | None`.

## Parameter probe

`src/hoststubs/inhost/param_probe.py` finds out what arguments a C function accepts,
from the function's own errors. Add `params` to the run command:

```bash
scripts/probe.sh 17.1v2 /Applications/Nuke17.1v2/Nuke17.1v2.app/Contents/MacOS/Nuke17.1 nuke params
```

Outputs: `data/nuke/<version>/params-nuke.json` and
`data/nuke/<version>/params-hiero.json`.

A C function checks its arguments before it does any work, left to right,
and reports the first one it rejects. For each function the script makes:

1. A call with no arguments and one with twelve. The errors give the
   counts: `takes at least 1 argument`, `takes at most 3 arguments`.
2. For each position, one candidate value followed by a poison object:

   ```
   f('text', POISON)   error names the poison  -> position 1 accepts str
   f(12, POISON)       error names the int     -> position 1 rejects int
   ```

   The poison stops the call, so the function body does not run.
3. For the last position, the poison alone. Nothing can follow it, so a
   candidate there would run the function. Its error text often names the
   type: `argument 1 must be str, not HostStubsPoison`.

Candidates come from `candidates()` in the scene file. `hoststubs.params`
reads the outcomes, with tests in `tests/test_param_probe.py`:

| Outcome | Result |
|---|---|
| Error text names a type (`must be str`, `cannot be interpreted as an integer`, `expecting a Nuke node type`) | That type. Host phrases are in `probe_messages` in the host config. |
| No usable text; `int` and `float` got past the position | `float`: the parser converts |
| Nearly every candidate got past | Nothing: the position takes any object |
| Two receivers disagree on the counts (`Knob.setValue` on two knob classes) | Nothing |
| A receiver refuses the call for its own reasons (`Root` has no inputs) | That receiver is ignored |

The resolver uses it as follows (`Resolver._with_probed_params`):

- A type replaces the documented one for that position.
- Counts only relax. A documented required parameter becomes optional when
  the parser accepts fewer arguments; it never becomes required. `Node.knob`
  reports two required arguments and works with one, because it tries
  several argument formats.
- A function with no signature in its docstring gets positional-only
  parameters `arg1`, `arg2` from the counts.
- A function with documented overloads is left alone.

Limits: hiero's C functions say `Invalid arguments to core.TrackItem.setTimelineIn`,
which gives counts but no types. Python functions check nothing and are
not probed.

## stubtest

mypy's `stubtest` imports the real modules and compares them with the
stubs: names, kinds, and the signatures of Python functions. It cannot
check the parameters of C functions; the parameter probe does that.

```bash
scripts/stubtest.sh 17.1v2 /Applications/Nuke17.1v2/Nuke17.1v2.app/Contents/MacOS/Nuke17.1 3.11
```

Build the stubs first (`python -m hoststubs build data/nuke/17.1v2/dump.json`).
The script installs a mypy without compiled modules for that Python
version into `build/work/`, because the compiled build does not load
inside Nuke, and runs in terminal mode with `--safe`. hiero and the
GUI-only `nukescripts` panels are not checked.

Findings that stay, by design:

| Finding | Why |
|---|---|
| `is a disjoint base`, `metaclass differs` | Not expressible in a stub that current checkers read |
| `failed to import` | Panels that exist only with the GUI |
| `nuke_internal.os is not present in stub` and similar | The module's own imports, not API |
| `nukescripts.pyQtExamples failed to find stubs` | Skipped in the host config: examples, not API |
| `cannot be subclassed at runtime, but isn't marked with @final` | C code derives from that class, so `@final` would be wrong for its subclasses |
