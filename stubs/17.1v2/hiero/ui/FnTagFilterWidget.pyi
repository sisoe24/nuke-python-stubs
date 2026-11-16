# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import PySide6.QtWidgets as _PySide6_QtWidgets
import hiero as hiero

class TagFilterWidget(_PySide6_QtWidgets.QTableView):
    kCheckbox: int
    kIcon: int
    kName: int
    staticMetaObject: _PySide6_QtCore.QMetaObject
    tagSelectionChanged: _PySide6_QtCore.Signal
    def __init__(self, alltags: Any, include_subset: Any, exclude_subset: Any, showhidden: bool = ..., parent: Any = ...) -> None: ...
    def all_tags(self) -> list[Any]:
        """Return entire set of tags"""
    def exclude_subset(self) -> Any:
        """Return subset of tags marked to be exclusion"""
    def include_subset(self) -> Any:
        """Return subset for tags marked to be included"""
    def init_ui(self) -> None: ...
