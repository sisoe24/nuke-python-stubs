# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import hiero.core as _hiero_core
from hiero.core import projects as projects
import hiero as hiero

def convertToType(type: Any) -> Any: ...

def findItemByGuid(guid: Any, *_args: Any, **kwargs: Any) -> None:
    """Find an item matching a guid. This searches all open projects. The other
    arguments are passed as keyword arguments.
    """

def findItemsByGuid(guids: Any, *args: Any, **kwargs: Any) -> list[Any]:
    """Find all items matching a list of guids. This searches all open projects.
    The other arguments are the same as those to findItemsInProject.
    """

def findItemsInAllProjects(**kwargs: Any) -> list[Any]:
    """Search for items across all open projects. See findItemsInProject() for arguments.
    
    """

def findItemsInBin(rootBin: _hiero_core.Bin, filter: Any = ..., partialName: Any = ..., verbose: Any = ...) -> list[Any]:
    """findItemsInBin(rootBin, filter=None, partialName=None, verbose=0) -> Returns all items recursively in a Bin, found in rootBin.
    @param rootBin: hiero.core.Bin object, to find the items on.
    @param filter: optional. Used to filter the returned list. Can be None, a case insensitive single string or type, or a list of case insensitive strings and types.
    @param partialName: optional string. If specified, objects will only be returned if their name contains this string.
    @param verbose: optional value. If not None/False/0, findItems will print out information as it searches.
    @return: list of objects.

    Example uses:
    myBin = hiero.core.projects()[0].clipsBin()[0] # A hiero.core.Bin object
    allItemsInMyBin = findItemsInBin(myBin)
    allClipsAndSequencesInMyBin = findItemsInBin(myBin, filter = [hiero.core.Sequence, hiero.core.Clip])
    allClipsWithPartialName = findItems(myProj, 'clips', 'C00')
    allSubBinsOnly = findItems(myProj, hiero.core.Bin)
    """

def findItemsInProject(proj: _hiero_core.Project | None = ..., filter: Any = ..., partialName: Any = ..., verbose: Any = ...) -> list[Any]:
    """findItemsInProject -> Returns all items in a Project's clipsBin.
    User can filter by a specific type(s) or by partial name, and optionally print a verbose log to the output window.
    Takes up to 4 keyword arguments : Project object, a string, a type or an array of strings for filter type, partial name of item, and a bool to enable/disable verbose mode
    Returns an array of items. Note: to find Tags in a Project, use the findProjectTags method.

    @param proj: hiero.core.Project object, to find the items on. If None, then the last project in the currently loaded projects will be used.
    @param filter: optional. Used to filter the returned list. Can be None, a case insensitive single string or type, or a list of case insensitive strings and types.
    @param partialName: optional string. If specified, objects will only be returned if their name contains this string.
    @param verbose: optional value. If not None/False/0, findItems will print out information as it searches.
    @return: list of objects.

    Example uses:

    allItems = findItemsInProject(myProj)
    allSeqsAndTracksWith30SecInName = findItemsInProject(myProj, ['sequences', 'Tracks'], '30Sec', 1)
    allTracks = findItemsInProject(myProj, "Track")
    videoTracks = findItemsInProject(myProj, "VideoTrack")
    sequences = findItemsInProject(myProj, "Sequence") # Can also use plural: 'Sequences'
    sequences = findItemsInProject(myProj, hiero.core.Sequence)
    sequencesAndClips = findItemsInProject(myProj, [hiero.core.Sequence, hiero.core.Clip])
    binsOnly = findItemsInProject(myProj, hiero.core.Bin)

    hiero.core.findItems is deprecated. Please use hiero.core.findItemsInProject instead.
    """

def findProjectTags(proj: _hiero_core.Project | None = ..., tagName: Any = ..., iconName: Any = ..., verbose: Any = ...) -> list[Any]:
    """findProjectTags -> Returns all Tags in a project. User can filter by tag name, icon name, and optionally print a verbose log to the output window.
    Takes up to 4 arguments : Project object, partial name of Tag, partial icon name, and a bool to enable/disable verbose mode
    Returns a list of Tag objects.

    @param proj: hiero.core.Project object, to find the items on. If None, then the last project in the currently loaded projects will be used.
    @param tagName: optional string. If specified, Tags will only be returned if their name contains this string.
    @param iconName: optional string. If specified, Tags will only be returned if their icon path contains this string.
    @param verbose: optional value. If not None/False/0, findProjectTags will print out information as it searches.
    @return: list of Tag objects.

    Example uses:

    allTags = findItems(myProj)
    allTagsWithNameLens = findItems(myProj, tagName = 'Lens')
    allTagsWithIconPath = findItems(myProj, iconName = 'lens.png')
    """

def typeName(type: Any) -> Any: ...

findItems = findItemsInProject
