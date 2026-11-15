# Probe: observed return types

Many C functions take no arguments and say nothing usable in their
docstring. The probe calls them inside the host and records the type of
each result.

## Run

Two commands per version, from the repository root. Each needs a licence.

```bash
probes/run.sh 17.1v2 /Applications/Nuke17.1v2/Nuke17.1v2.app/Contents/MacOS/Nuke17.1 nuke
```

```bash
probes/run.sh 17.1v2 /Applications/Nuke17.1v2/Nuke17.1v2.app/Contents/MacOS/Nuke17.1 hiero
```

`nuke` probes `nuke` and `nuke_internal` in terminal mode with `--safe`
(no `~/.nuke` plugins). `hiero` probes `hiero` in a Nuke Studio GUI
session, because hiero exists only there; that session loads `~/.nuke`
plugins and its window appears on screen. Both restart with `resume` after
each crash. Outputs, both committed: `probes/nuke-<version>.json` and
`probes/nuke-<version>.hiero.json`. Work files go to `probes/work/`.

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

`hosts/nuke/probe_scene.py` builds the Nuke scene: one node of each common
class in a chain, an animated knob, one user knob of each knob class,
formats, frame ranges. `hosts/nuke/probe_scene_hiero.py` builds the hiero
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
