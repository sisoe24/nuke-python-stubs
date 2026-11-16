# Type stubs for nuke 17.1v2. Generated; do not edit.

"""Functions used by the CameraTracker node"""

from typing import Any
import nukescripts.panels as _nukescripts_panels
from nukescripts import camerapresets as camerapresets
from nukescripts import flags as flags
from nukescripts.panels import PythonPanel as PythonPanel

class LinkableImportPanel(_nukescripts_panels.PythonPanel):
    """Modal dialog for selecting a Linkable node in the script.

    The following class creates a modal dialog with one UI element: an enum of nodes
    that derive from the LinkableI class. (The LinkableI interface allows us to easily query and import
    2D data from a variety of sources, particularly the Tracker node.) The user then selects their source node
    to import the data from. Once Ok'ed, the code below creates a new user track for each LinkableInfo object
    returned in the node.linkableKnobs() function with an XY co-ordinate, and then copies each animation curve
    entry.
    """
    def __init__(self) -> None: ...
    def showModalDialog(self, dstNode: Any) -> None: ...

def cameraClass(solver: Any) -> str:
    """Returns the correct camera class for the 3D system in use."""

def cameratrackerCreateCallback() -> None: ...

def cardClass(solver: Any) -> str:
    """Returns the correct card class for the 3D system in use."""

def classic3D(solver: Any) -> bool:
    """Checks if the node is using the classic 3D system."""

def createCamera(solver: Any) -> Any:
    """Create a camera node based on the projection calculated by the solver."""

def createCameraRig(solver: Any) -> None:
    """Create a multi-view rig with a camera per view."""

def createCameraSet(solver: Any) -> None:
    """Create a set of Cameras, one Camera per solved frame."""

def createCards(solver: Any) -> None: ...

def createEverything(cameraTracker: Any) -> None:
    """Create a Scene with a Camera, PointCloud, ScanlineRender, and LensDistortion (Undistort) node."""

def createLensDistortion(cameraTracker: Any) -> Any: ...

def createPointCloud(cameraTracker: Any) -> None:
    """Create a CameraTrackerPointCloud node."""

def createScene(cameraTracker: Any) -> list[Any]:
    """Create a Scene with a Camera and PointCloud for the camera solve."""

def createUndistortion(cameraTracker: Any) -> Any: ...

def exportTracker(cameraTracker: Any) -> None:
    """Export data from the CameraTracker node into a Tracker node."""

def exportTracks(cameraTracker: Any) -> None:
    """Utility function that collects the filename to be used in exporting tracks from a Shake formatted file."""

def importTracker(cameraTracker: Any) -> None:
    """Import data from a Tracker node into the CameraTracker node."""

def importTracks(cameraTracker: Any) -> None:
    """Utility function that collects the filename to be used in importing tracks from a Shake formatted file."""

def pointCloudClass(solver: Any) -> str:
    """Returns the correct point cloud class for the 3D system in use."""

def populateExportMenu(cameraTracker: Any) -> None:
    """Populate the export menu on a CameraTracker node."""

def populateFilmBackPresets(cameraTracker: Any) -> None:
    """Populate the film back presets menu on a CameraTracker node."""

def scanlineRenderClass(solver: Any) -> str:
    """Returns the correct point cloud class for the 3D system in use."""

def sceneClass(solver: Any) -> str:
    """Returns the correct scene class for the 3D system in use."""

def setKnobToPreset(cameraTracker: Any, selectedPresetIdx: Any) -> None:
    """Finds the index of the preset knob and sets the film back size knob accordingly."""
