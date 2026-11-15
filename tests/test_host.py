from __future__ import annotations

from hoststubs.host import load_host, dump_arguments


def test_nuke_dump_arguments() -> None:
    """The Nuke config produces the full dump.py argument list."""
    assert dump_arguments(load_host('nuke'), 'dumps/nuke.json') == [
        'dumps/nuke.json', 'host=nuke', 'version=nuke.NUKE_VERSION_STRING',
        'skip=hiero.examples', 'skip=nukescripts.pyQtExamples', 'private=core:hiero.core', 'private=ui:hiero.ui',
        'nuke', 'nuke_internal', 'nukescripts', 'ocionuke', 'hiero',
    ]
