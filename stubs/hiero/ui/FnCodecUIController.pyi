# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from hiero.ui.FnTaskUIFormLayout import TaskUIFormLayout as TaskUIFormLayout
from hiero.ui.FnUIProperty import UIPropertyFactory as UIPropertyFactory

kCodecTooltips: dict
kEXRTooltips: dict

class CodecUIController:
    """CodecUIController is the base class used to control the widgets for specific Codecs.
    This allows to customize layout of the widgets and signals and slots
    """
    propertyChanged: Any
    staticMetaObject: Any
    def __init__(self, file_type: Any, propertyDictionaries: Any, presetDictionary: Any) -> None: ...
    def connectProperty(self, propertyWidget: Any) -> None:
        """reimplement this to allow setup custom signals and slots"""
    def getLabelAndProperty(self, propertyKey: Any) -> tuple[Any, Any]: ...
    def getTooltip(self, label: Any, propertyKey: Any) -> Any: ...
    def initializeUI(self, propertyDictionaries: Any, presetDictionary: Any) -> None:
        """Creates all the properties from the propertyDictionaries"""

class EXRCodecUIController(CodecUIController):
    kCompression: str
    kCompressionLevel: str
    kDataType: str
    kFullLayerNames: str
    kInterleave: str
    kLayerNameFormat: str
    kMetadata: str
    kPrefix: str
    kTruncateChannelNames: str
    kWriteACESCompliantEXR: str
    staticMetaObject: Any
    def __init__(self, file_type: Any, propertyDictionaries: Any, presetDictionary: Any) -> None: ...
    def compressionChanged(self) -> None: ...
    def connectProperty(self, propertyWidget: Any) -> None: ...
    def createProperty(self, properties: Any, propertyKey: Any, presetDictionary: Any) -> None: ...
    def initializeUI(self, propertyDictionaries: Any, presetDictionary: Any) -> None:
        """Creates all the properties from the propertyDictionaries"""
    def interleaveChanged(self) -> None: ...
    def metadataChanged(self) -> None: ...
