# Add a Nuke version

Run the steps in order, from the repository root. Each linked page has the exact commands. Replace the version in those commands with yours.

You need the Nuke install and a licence. The inference step needs only the files on disk.

1. **Prepare `~/.nuke`.** The dump and the hiero probes run in a Nuke Studio GUI session, and plugins in `~/.nuke` load there. A plugin that adds names to `nuke` or `hiero` ends up in the committed data. Move plugins out first.

2. **Register the version.** Add it to `stub_revisions` in `src/hoststubs/hosts/nuke/config.py`, with revision `0`. Without it, the build raises `KeyError: No stub revision for ...`.

3. **Dump the API.** [dump-schema.md](dump-schema.md).
   Check: `data/nuke/<version>/dump.json` exists. Read its `errors` and `foreign` keys.

4. **Infer the Python modules.** [inference.md](inference.md).
   Check: `data/nuke/<version>/inference/empty_bodies.json` exists.

5. **Probe.** [probe.md](probe.md). Four runs: `nuke`, `hiero`, `nuke params`, `hiero params`.
   Check: `probe-nuke.json`, `probe-hiero.json`, `params-nuke.json` and `params-hiero.json` exist in `data/nuke/<version>/`.

   A call can end the Nuke session. The script restarts with `resume`, and the output lists the unfinished calls as `crashed`. Add each crashing path to `probe_skip` in the host config and run again. A new version usually has a few: 17.1v2 added five.

6. **Build.**

   ```bash
   uv run python -m hoststubs build data/nuke/<version>/dump.json
   ```

   Check: `build/nuke-python-stubs-<version>.zip` exists.

7. **Look at the coverage and run the tests.**

   ```bash
   uv run python -m hoststubs report data/nuke/<version>/dump.json
   uv run pytest -q
   ```

8. **Optional: run `stubtest`.** [probe.md](probe.md#stubtest). It needs a licence.

9. **Commit `data/nuke/<version>/` and the config change.** CI builds a zip for every `data/nuke/*/dump.json`, so the commit is what makes the release.
