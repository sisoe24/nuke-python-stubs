# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from typing import Callable
from hiero.core import AudioTrack as AudioTrack
from hiero.core import BinItem as BinItem
from hiero.core import Clip as Clip
from hiero.core import Sequence as Sequence
from hiero.core import TrackItem as TrackItem
from hiero.core import TrackItemBase as TrackItemBase
from hiero.core import Version as Version
from hiero.core import VideoTrack as VideoTrack

def deprecated(f: Any, msg: Any = ..., funcName: Any = ..., deprecatedWarningMsg: Any = ...) -> Callable[..., Any]:
    """defines a new method and prints a message warning that the function is deprecated.
    @param f: method
    @param msg: Optional. Warning message to print.
    @param funcName: Optional. method name to appear in the warning message. If None f.__name__ will be used.
    @param deprecatedWarningMsg: Optional. Message that will appear after 'WARNING - DEPRECATED ( funcName ): '
    """

def markDeprecated() -> None: ...
