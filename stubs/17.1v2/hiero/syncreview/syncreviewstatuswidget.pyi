# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import PySide6.QtWidgets as _PySide6_QtWidgets
from hiero.syncreview.connectionmanager import ConnectionManager as ConnectionManager
from hiero.syncreview.connectionstate import ConnectionState as ConnectionState

class SyncReviewStatusWidget(_PySide6_QtWidgets.QWidget):
    """Widget for editing displaying info about the current sync review state
    
    """
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, connectionManager: Any) -> None: ...
