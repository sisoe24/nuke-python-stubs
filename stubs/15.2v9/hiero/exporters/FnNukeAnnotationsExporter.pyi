# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero.exporters.FnNukeShotExporter as _hiero_exporters_FnNukeShotExporter
from hiero.core import nuke as nuke
from hiero.core.FnNukeHelpers import getConnectedDisconnectedTracks as getConnectedDisconnectedTracks
from hiero.exporters.FnNukeShotExporter import NukeShotExporter as NukeShotExporter
from hiero.exporters.FnNukeShotExporter import NukeShotPreset as NukeShotPreset
import hiero as hiero

class NukeAnnotationsExporter(_hiero_exporters_FnNukeShotExporter.NukeShotExporter):
    def __init__(self, initDict: Any) -> None: ...
    def getAnnotationKeyFramesForTrackItem(self, trackItem: Any, offset: Any, toSequenceTime: Any) -> set[Any]:
        """Get the annotation key frames for the track item's clip.  This is modified by offset and
        mapped to sequence time if required. 
        """
    def getAnnotationsKeyFrames(self) -> list[Any]:
        """Get the list of annotations keyframes for the current export. """
    def getSequenceAnnotationsKeyFrames(self) -> set[Any]:
        """If a sequence is being exported, returns keyframes for annotations on tracks which will be connected. """
    def getTrackItemAnnotationsKeyFrames(self) -> set[Any]:
        """If a single track item is being exported, returns keyframes for the annotations on the item's clip,
        plus any above it on the sequence which are being included. 
        """
    def updateItem(self, originalItem: Any, localtime: Any) -> None: ...

class NukeAnnotationsPreset(_hiero_exporters_FnNukeShotExporter.NukeShotPreset):
    def __init__(self, name: Any, properties: Any) -> None: ...
