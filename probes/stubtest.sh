#!/usr/bin/env bash
# Compare the built stubs with the live modules, inside Nuke.
#
#   probes/stubtest.sh 15.2v9 /Applications/Nuke15.2v9/Nuke15.2v9.app/Contents/MacOS/Nuke15.2 3.10
#
# The third argument is the Python version of that Nuke (see `python` in the dump).
# An optional fourth is the platform Nuke was built for, as uv names it; the
# default is Apple silicon. mypy's one compiled dependency must match it.
# Runs in terminal mode, so hiero and the GUI-only nukescripts panels are not checked.
set -u
version=$1
nuke=$2
python=$3
platform=${4:-aarch64-apple-darwin}

work=$PWD/probes/work
mypy=$work/mypy-$python
out=$work/stubtest-$version.txt
mkdir -p "$work"

if [ ! -d "$mypy" ]; then
    uv pip install -q --target "$mypy" --python-version "$python" --python-platform "$platform" \
        --no-binary mypy mypy
fi

# The host API itself breaks substitutability (Boolean_Knob.value against
# Array_Knob.value), and mypy refuses to run stubtest on such stubs.
# The PySide6 inside Nuke has no stubs; the one from PyPI, which users install, has.
printf '[mypy]\ndisable_error_code = override\nignore_missing_imports = True\n' > "$work/mypy.ini"

MYPYPATH=$PWD/build/nuke-$version/stubs "$nuke" -t -i --safe inhost/run_stubtest.py "$mypy" \
    nuke nuke_internal nukescripts ocionuke --concise --mypy-config-file "$work/mypy.ini" > "$out" 2>&1

if ! grep -q '^stubtest exit code' "$out"; then
    echo "stubtest did not run; last lines of $out:"
    tail -3 "$out"
    exit 1
fi

# Not expressible in a stub, or not reachable in terminal mode:
#   disjoint base      a typing feature too new for the checkers users run
#   metaclass differs  pybind11 and Shiboken metaclasses are private
#   failed to import   panels that exist only with the GUI
grep -E '^(nuke|nuke_internal|nukescripts|ocionuke)[A-Za-z0-9_.]* ' "$out" \
    | grep -v -e 'disjoint base' -e 'metaclass differs' -e 'failed to import' > "$out.findings"

echo "all findings: $(grep -c -E '^(nuke|nuke_internal|nukescripts|ocionuke)[A-Za-z0-9_.]* ' "$out")"
echo "findings to fix: $(wc -l < "$out.findings" | tr -d ' ')  ($out.findings)"
