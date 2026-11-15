#!/usr/bin/env bash
# Probe one Nuke version in terminal mode. Restarts with `resume` after each
# crash; the journal names the call that caused it.
#   probes/run.sh 15.2v9 /Applications/Nuke15.2v9/Nuke15.2v9.app/Contents/MacOS/Nuke15.2
set -u
version=$1
nuke=$2
out=probes/nuke-$version.json

uv run -q python -m hoststubs probe-targets "dumps/nuke-$version.json" "probes/nuke-$version.targets.json" nuke nuke_internal
rm -f "$out" "$out.journal"

resume=""
journalled=-1
for attempt in $(seq 1 40); do
    "$nuke" -t -i --safe inhost/probe.py "$out" "targets=probes/nuke-$version.targets.json" scene=hosts/nuke/probe_scene.py $resume > "probes/nuke-$version.log" 2>&1
    echo "attempt $attempt: exit $?, last call: $(grep '^> ' "$out.journal" | tail -1)"
    [ -f "$out" ] && break

    # No new journal line means the crash is in the scene, not in a probed call.
    now=$(grep -c '^> ' "$out.journal" 2>/dev/null || echo 0)
    if [ "$now" = "$journalled" ]; then
        echo "no progress; last scene step: $(grep '^scene: ' "probes/nuke-$version.log" | tail -1)"
        exit 1
    fi
    journalled=$now
    resume=resume
done
