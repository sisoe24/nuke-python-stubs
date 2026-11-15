# Probe: observed return types

Many C functions take no arguments and say nothing usable in their
docstring. The probe calls them inside the host and records the type of
each result.

## Run

One command per version, from the repository root. It needs a licence.

```bash
probes/run.sh 17.1v2 /Applications/Nuke17.1v2/Nuke17.1v2.app/Contents/MacOS/Nuke17.1
```

The script writes the target list, starts Nuke in terminal mode with
`--safe` (no `~/.nuke` plugins), and restarts with `resume` after each
crash. Output: `probes/nuke-<version>.json`, which is committed.

Only `nuke` and `nuke_internal` are probed. hiero exists only in a GUI
session and has no probe scene yet.

## What is called

`python -m hoststubs probe-targets` picks, from the dump:

- C functions and methods that the docstring shows as callable without
  arguments, or whose parameters are unknown (a call that needs arguments
  fails with `TypeError` before it does anything);
- C properties, which are read, not called.

Not called: Python functions, dunders, any name that contains a word in
`probe_skip_words` (`scriptSaveAs` contains `save`), and the paths in
`probe_skip`. Both lists are in `hosts/nuke/config.py`. The paths were
found by running: each one ends the session.

Methods run first, on the scene as built. Module functions run after,
because some of them change the scene.

## Scene

`hosts/nuke/probe_scene.py` builds it: one node of each common class in a
chain, an animated knob, one user knob of each knob class, formats, frame
ranges. The list of what was created is stored in the output as `scene`.

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
| Contradicts or refines the docstring type | The observed type |
| A subclass, with no docstring type | Its topmost base in the dump |

The last three rows are stricter than "the probe wins". An observation is
one object in one scene: it showed `Root` for `nuke.thisNode()` and a
single `Node` where the docstring says `Node | None`.
