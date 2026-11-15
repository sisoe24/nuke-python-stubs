#!/usr/bin/env bash
# Probe one Nuke version. Restarts with `resume` after each crash; the
# journal names the call that caused it.
#
#   probes/run.sh 15.2v9 /Applications/Nuke15.2v9/Nuke15.2v9.app/Contents/MacOS/Nuke15.2 nuke
#   probes/run.sh 15.2v9 /Applications/Nuke15.2v9/Nuke15.2v9.app/Contents/MacOS/Nuke15.2 hiero
#
# `nuke` runs in terminal mode with --safe. `hiero` needs a Nuke Studio GUI
# session, which loads the plugins in ~/.nuke.
set -u
version=$1
nuke=$2
kind=$3

work=probes/work
mkdir -p "$work"
targets=$PWD/$work/nuke-$version.$kind.targets.json
log=$work/nuke-$version.$kind.log

if [ "$kind" = hiero ]; then
    out=$PWD/probes/nuke-$version.hiero.json
    scene=$PWD/hosts/nuke/probe_scene_hiero.py
    modules="hiero"
else
    out=$PWD/probes/nuke-$version.json
    scene=$PWD/hosts/nuke/probe_scene.py
    modules="nuke nuke_internal"
fi

uv run -q python -m hoststubs probe-targets "dumps/nuke-$version.json" "$targets" $modules
rm -f "$out" "$out.journal"

run_once() {
    local arguments="$out targets=$targets scene=$scene $1"
    if [ "$kind" = hiero ]; then
        NUKE_PATH="$PWD/hosts/nuke/studio:${NUKE_PATH:-}" HOSTSTUBS_INHOST="$PWD/inhost" \
            HOSTSTUBS_RUN=probe HOSTSTUBS_ARGS="$arguments" "$nuke" --studio > "$log" 2>&1 &
    else
        "$nuke" -t -i --safe inhost/probe.py $arguments > "$log" 2>&1 &
    fi

    # The probe ends a stuck call itself; this ends a session that is stuck elsewhere.
    local pid=$!
    for _ in $(seq 1 150); do
        kill -0 $pid 2>/dev/null || break
        sleep 2
    done
    kill -0 $pid 2>/dev/null && kill -9 $pid
    wait $pid 2>/dev/null
}

resume=""
journalled=-1
for attempt in $(seq 1 40); do
    run_once "$resume"
    echo "attempt $attempt: exit $?, last call: $(grep '^> ' "$out.journal" 2>/dev/null | tail -1)"
    [ -f "$out" ] && break

    # No new journal line means the crash is in the scene, not in a probed call.
    now=$(grep -c '^> ' "$out.journal" 2>/dev/null || echo 0)
    if [ "$now" = "$journalled" ]; then
        echo "no progress; last scene step: $(grep '^scene: ' "$log" | tail -1)"
        exit 1
    fi
    journalled=$now
    resume=resume
done
