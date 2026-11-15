from __future__ import annotations

from hoststubs.host import HostConfig

HOST = HostConfig(
    name='nuke',
    version_attribute='nuke.NUKE_VERSION_STRING',
    roots=('nuke', 'nuke_internal', 'nukescripts', 'ocionuke', 'hiero'),
    # Examples are not API: hiero's register UI at import, nukescripts' need sip.
    skip=('hiero.examples', 'nukescripts.pyQtExamples'),
    # hiero's C modules are importable as top-level `core` and `ui` in a GUI session.
    private=('core', 'ui'),
    stub_revisions={},
)
