from __future__ import annotations

from hoststubs.host import DUMP_SCRIPT, load_host, dump_command


def test_nuke_dump_command() -> None:
    """The Nuke config produces the full in-host dump command."""
    command = dump_command(load_host('nuke'), 'studio', 'dumps/nuke.json')

    assert command == [
        'Nuke', '--studio', '-t', str(DUMP_SCRIPT), 'dumps/nuke.json',
        'host=nuke', 'version=nuke.NUKE_VERSION_STRING', 'skip=hiero.examples',
        'nuke', 'nukescripts', 'ocionuke', 'hiero',
    ]
