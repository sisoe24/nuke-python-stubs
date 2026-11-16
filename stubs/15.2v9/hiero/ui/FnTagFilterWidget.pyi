# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
import hiero as hiero

class TagFilterWidget:
    kCheckbox: int
    kIcon: int
    kName: int
    staticMetaObject: Any
    tagSelectionChanged: Any
    def __init__(self, alltags: Any, include_subset: Any, exclude_subset: Any, showhidden: bool = ..., parent: Any = ...) -> None: ...
    def all_tags(self) -> list[Any]:
        """Return entire set of tags"""
    def exclude_subset(self) -> Any:
        """Return subset of tags marked to be exclusion"""
    def include_subset(self) -> Any:
        """Return subset for tags marked to be included"""
    def init_ui(self) -> None: ...
