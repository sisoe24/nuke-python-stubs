from hoststubs.report import is_private


def test_private_names_are_counted_apart() -> None:
    assert is_private('nuke_internal.callbacks._addCallback')
    assert is_private('hiero.core._Clip.addToNukeScript')
    assert is_private('nuke_internal.__filterNames')
    assert not is_private('hiero.core.Clip.__init__')
    assert not is_private('nuke.toNode')
