#!/usr/bin/env bash
# Syncs stubs to NukeTools
# This script is meant to be run from the root of the repo
#
#   ./sync_stubs.sh 17.1v2      (default: 15.2v9)
#
# It will remove the existing stubs directory and replace it with a symlink to the stubs directory in the repo
# This is useful for development, as you can edit the stubs in the repo and have them automatically update in NukeTools

CURRENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
NUKE="$HOME/.nuke/NukeTools"
VERSION="${1:-15.2v9}"

echo "Syncing stubs to $NUKE"
echo "Current dir: $CURRENT_DIR"

(
	cd $NUKE || exit 1
	rm -rf $NUKE/stubs
	ln -s $CURRENT_DIR/stubs/$VERSION $NUKE/stubs
)
