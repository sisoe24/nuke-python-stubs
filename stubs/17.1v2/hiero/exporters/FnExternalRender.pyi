# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import hiero.core.FnExporterBase as _hiero_core_FnExporterBase
import hiero.exporters.FnShotExporter as _hiero_exporters_FnShotExporter
from hiero.core import FnExporterBase as FnExporterBase
from hiero.core import FnNukeHelpers as FnNukeHelpers
from hiero.core import log as log
from hiero.core import nuke as nuke
from hiero.core.FnFloatRange import CustomList as CustomList
from hiero.core.FnFloatRange import Default as Default
from hiero.exporters import FnShotExporter as FnShotExporter
from hiero.exporters.FnExportUtil import OutputTransformKnobs as OutputTransformKnobs
import hiero as hiero
import ocionuke as ocionuke

kDisabled: str
kPerSequence: str
kPerShot: str
kPerTrack: str
kUnconnected: str

class ExternalRenderPreset(_hiero_core_FnExporterBase.TaskPresetBase):
    def __init__(self, name: Any, properties: Any) -> None:
        """Initialise presets to default values"""
    def supportedItems(self) -> Any: ...

class ExternalRenderTask(_hiero_exporters_FnShotExporter.ShotTask):
    """ExternalRenderTask doesn't do anything, it's just a marker to go into the template
    so that other tasks can find the location of external renders.
    """
    def __init__(self, initDict: Any) -> None:
        """Initialize"""
    def taskStep(self) -> bool: ...

class NukeRenderPreset(_hiero_core_FnExporterBase.RenderTaskPreset):
    def __init__(self, name: Any, properties: Any) -> None:
        """Initialise presets to default values"""
    def supportedItems(self) -> Any: ...

class NukeRenderTask(ExternalRenderTask):
    """NukeRenderTask holds settings for a Nuke Write node so that shot exports can create
    the node set up to write to the requested location.
    """
    burninKeys: tuple
    burninNodeData: str
    burninPropertyData: tuple
    def __init__(self, initDict: Any) -> None:
        """Initialize"""
    def addBurninNodes(self, script: Any = ...) -> Any:
        """If Burnin enabled in preset, add NukeRenderTask.burninNodeData to the
        script and modify knob values according to preset data
        """
    def nukeWriteNode(self, framerate: Any = ..., project: Any = ...) -> Any:
        """Return a Nuke Write node for this tasks's export path."""
    def taskStep(self) -> bool: ...
    def validate(self) -> None: ...
    def views(self) -> Any: ...
    def viewsFromPreset(self) -> Any:
        """Get the views configured on the preset. """
    def viewsFromSource(self) -> Any:
        """Get the views available from the source sequence/clip/trackitem. By default
        returns all the views in the project.
        """

def createAdditionalNodes(entrypoint: Any, additionalNodeData: Any, item: Any) -> list[Any]:
    """Return list of nodes to be added to the script at specified entrypoint based on item tags"""

def createWriteNode(ctx: Any, path: Any, preset: Any, nodeName: Any = ..., inputNode: Any = ..., framerate: Any = ..., project: Any = ...) -> Any:
    """Return a Nuke Write node based on a path and a preset."""

def getColorspaceAndRoleSplit(lutValue: Any) -> tuple[Any, Any] | tuple[Any, None]:
    """Returns the colorspace and role if the string contains both, otherwise returns
    the provided lutValue as the colorspace and None as the role
    """

def getColorspaceFromPropertyWithRole(lutValue: Any) -> Any:
    """Get just the colorspace name from a string containing the colorspace +
    the role in parentheses.
    """

def getRoleFromPropertyWithRole(lutValue: Any) -> Any:
    """Get just the role name from a string containing the colorspace +
    the role in parentheses.
    """

def isColorspaceValid(project: Any, colorspace: Any, role: Any) -> bool: ...
