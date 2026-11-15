from __future__ import annotations

from hoststubs.host import HostConfig

HOST = HostConfig(
    name='nuke',
    version_attribute='nuke.NUKE_VERSION_STRING',
    roots=('nuke', 'nukescripts', 'ocionuke', 'hiero'),
    # The examples register UI at import and are not API.
    skip=('hiero.examples',),
    launchers={
        'nuke': ('Nuke', '-t'),
        'studio': ('Nuke', '--studio', '-t'),
    },
    stub_revisions={},
)
