# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from hiero.core import ItemWrapper as ItemWrapper
from hiero.core.FnCompSourceInfo import CompSourceInfo as CompSourceInfo
from hiero.core.FnVersionScanner import VersionScanner as VersionScanner
import hiero as hiero

eventListener: ReExportEventListener

class ReExportAction:
    """Action for re-exporting track items. """
    staticMetaObject: Any
    def __init__(self, reExportItemsTags: Any, text: str = ..., parent: Any = ...) -> None: ...
    def onTriggered(self) -> None: ...
    def postProcess(self, postProcessScripts: Any) -> None:
        """After re-exporting tagged track items, finish by performing
        post processing for items that are comps. 
        """
    def postProcessScripts(self, nkScriptPaths: Any) -> None:
        """Post process each nkScript path. """
    def reExportItem(self, item: Any, tag: Any, newVersionIndex: Any, allTrackItems: Any, enableAnnotations: Any) -> None: ...

class ReExportAnnotationsAction:
    """Action for re-exporting annotations.  This works a bit differently, as it re-exports from
    the track item created with 'Build Track' rather than the original item.  Any track items under the
    main one are also included and collated into the script. 
    """
    staticMetaObject: Any
    def __init__(self, reExportItemsTags: Any, text: str = ..., parent: Any = ...) -> None: ...
    def onTriggered(self) -> None: ...
    def reExportAnnotations(self, item: Any, tag: Any, newVersionIndex: Any) -> bool: ...

class ReExportEventListener:
    """Listen for context menu events in the timeline, and add ReExportActions to it if appropriate depending on the selection. """
    def __init__(self) -> None: ...
    def onContextMenuEvent(self, event: Any) -> None:
        """Context menu event handler.  Check for items which are valid for re-export and if any are found,
        add entries to the menu. 
        """

def compScriptPath(item: Any) -> None:
    """If the item is a comp, return the script path else return None. """

def findItemReExportTag(item: Any) -> None:
    """Helper function to find the export tag to be used for re-export.  Returns the most recent tag
    if there is more than one. 
    """

def findNewVersionIndex(path: Any) -> int:
    """Scan for versioned files in the given path and return the first unused version index.  If the path
    contains no versioning, the user is asked if they wish to overwrite the existing files. 
    """

def findOriginalTrackItemAndTag(trackItem: Any) -> tuple[Any, Any] | tuple[None, None]:
    """Given a track item which has been created using 'Build Track', find the tag
    which links back to the original item, and return both the original item and its export tag. 
    """

def findTrackItemByUID(sequence: Any, uid: Any) -> None:
    """Try to find an item with the given uid on the sequence. """

def findTrackItemsIntersecting(intersectTrackItem: Any, excludeTracks: Any = ...) -> list[Any]:
    """Find items intersecting the given track item. """

def setEnabledTasks(preset: Any, enableShots: Any, enableAnnotations: Any) -> None:
    """Set tasks in the preset enabled or disabled depending on whether shots or annotations
    are being exported. 
    """

def setPresetTasksProperty(preset: Any, name: Any, value: Any) -> None:
    """Iterate over the task presets and if they have the given property, set its value. """
