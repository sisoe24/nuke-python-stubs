# Add a Nuke version

The pipeline: dump the API from Nuke, infer the Python modules with Pyright, probe the C functions inside Nuke, then build the stubs and check them. The dump and the probes need a licence. Everything after them runs offline.

Run the steps in order, from the repository root. In the commands:

- `<version>` is the Nuke version, for example `17.1v2`.
- `<app>` is the install, for example `/Applications/Nuke17.1v2/Nuke17.1v2.app`.
- `<nuke>` is the executable, for example `<app>/Contents/MacOS/Nuke17.1`.

> [!WARNING]
> The repository path must not contain spaces.

1. **Prepare `~/.nuke`.** The dump and the hiero probes run in a Nuke Studio window, and plugins in `~/.nuke` load there. A plugin that adds names to `nuke` or `hiero` ends up in the committed data. Move plugins out first.

2. **Register the version.** Add it to `stub_revisions` in `src/hoststubs/hosts/nuke/config.py`, with revision `0`. Without it, the build raises `KeyError: No stub revision for ...`.

3. **Dump the API.** Nuke Studio runs `src/hoststubs/hosts/nuke/studio/Python/StartupUI/run_inhost.py` at startup, dumps, and quits. Terminal mode cannot reach `hiero` or the `nukescripts` panels, so it uses the GUI.

   ```bash
   NUKE_PATH="$PWD/src/hoststubs/hosts/nuke/studio:$NUKE_PATH" HOSTSTUBS_INHOST="$PWD/src/hoststubs/inhost" HOSTSTUBS_RUN=dump HOSTSTUBS_ARGS="$(uv run python -m hoststubs dump-arguments nuke "$PWD/data/nuke/<version>/dump.json")" "<nuke>" --studio
   ```

   Check: `data/nuke/<version>/dump.json` exists. Read its `errors` and `foreign` keys. The format is in [dump-schema.md](dump-schema.md).

4. **Infer the Python modules.** It needs the files of the install, not the licence.

   ```bash
   uv run python -m hoststubs infer data/nuke/<version>/dump.json "<app>/Contents/MacOS/plugins" "<app>/Contents/Resources/pythonextensions/site-packages"
   ```

   Check: `data/nuke/<version>/inference/empty_bodies.json` exists.

5. **Probe.** The usage is in the header of `scripts/probe.sh`. Run all four:

   ```bash
   scripts/probe.sh <version> "<nuke>" nuke
   scripts/probe.sh <version> "<nuke>" hiero
   scripts/probe.sh <version> "<nuke>" nuke params
   scripts/probe.sh <version> "<nuke>" hiero params
   ```

   `nuke` runs in terminal mode with `--safe`. `hiero` opens a Nuke Studio window and loads the plugins in `~/.nuke`.

   Check: `probe-nuke.json`, `probe-hiero.json`, `params-nuke.json` and `params-hiero.json` exist in `data/nuke/<version>/`.

   A call can end the Nuke session. The script restarts with `resume`, and the output lists the unfinished calls as `crashed`. Add each crashing path to `probe_skip` in the host config and run again. A new version usually has a few: 17.1v2 added five.

6. **Record the corpus snapshot.** The build checks the stubs against `tests/corpus/snapshots/nuke-<version>.json`. A new version has none, and without it the build and CI fail with `no snapshot for this version`.

   ```bash
   uv run python -m hoststubs build data/nuke/<version>/dump.json --update-snapshot
   ```

   The snapshot records what Pyright reveals for the corpus, so it also records a symbol that is missing in this version, or one that fell back to `Any`. Read it before you commit it. Compare it with the snapshot of the closest version.

   > [!IMPORTANT]
   > Never update a snapshot to make a failing build pass.

7. **Build.**

   ```bash
   uv run python -m hoststubs build data/nuke/<version>/dump.json
   ```

   Check: `build/nuke-python-stubs-<version>.zip` exists.

8. **Look at the coverage and run the tests.**

   ```bash
   uv run python -m hoststubs report data/nuke/<version>/dump.json
   uv run pytest -q
   ```

9. **Optional: run `stubtest`.** The usage is in the header of `scripts/stubtest.sh`. It needs a licence. The findings that stay on purpose are in [decisions.md](decisions.md#stubtest-findings-that-stay).

10. **Commit `data/nuke/<version>/` and the config change.** CI builds a zip for every `data/nuke/*/dump.json`, so the commit is what makes the release.
