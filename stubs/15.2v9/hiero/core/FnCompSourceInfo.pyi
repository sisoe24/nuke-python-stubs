# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from hiero.core import Clip as Clip
from hiero.core import MediaSource as MediaSource
from hiero.core import TrackItem as TrackItem
from hiero.core import remapPath as remapPath

class CompSourceInfo:
    """Helper class for getting render information from a comp MediaSource.
    Raises an exception if the expected metadata can't be found.
    Sets the following attributes:
      writePath - The path being rendered to. For multi-view comps which render to %v
                  paths, this will be formatted with the first view name
      unexpandedWritePath - For multi-view comps this will contain the render path
                            including any %v placeholders
      firstFrame - the first frame rendered
      lastFrame - the last frame rendered
    """
    kNkFirstFrameKey: str
    kNkLastFrameKey: str
    kNkUnexpandedWritePathKey: str
    kNkWritePathKey: str
    def __init__(self, comp: Any) -> None: ...
    def __str__(self) -> str: ...
    def isComp(self) -> bool:
        """Get if the source is actually a comp. """

def isNukeScript(filename: Any) -> Any:
    """Returns True if filename ends with .nk (.nk / .nknc for NC)
    (or .nk / .nkind for Nuke Indie)
    """
