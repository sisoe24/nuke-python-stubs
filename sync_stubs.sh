#!/usr/bin/env bash

vscode_stubs="$HOME/.vscode/extensions/virgilsisoe.nuke-tools-*/assets/nuke-python-stubs"

for stub in $vscode_stubs; do
	if [ -d "$stub" ]; then
		echo "Copy stubs in $stub"
		rsync -a --delete "$PWD/stubs/" "$stub"
	fi
done
