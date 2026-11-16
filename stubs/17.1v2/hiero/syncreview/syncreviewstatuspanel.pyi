# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
import PySide6.QtCore as _PySide6_QtCore
import PySide6.QtGui as _PySide6_QtGui
import PySide6.QtWidgets as _PySide6_QtWidgets
from hiero.syncreview import config as config
from hiero.syncreview.connectionmanager import ConnectionManager as ConnectionManager
from hiero.syncreview.connectionstate import ConnectionState as ConnectionState
import hiero as hiero

class SyncStatusPanel(_PySide6_QtWidgets.QWidget):
    """Shows the current status of the participants of a sync review session. """
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, connectionManager: Any) -> None: ...
    def getSortedColumn(self) -> int:
        """Column that is currently being sorted. Holds a negative value if the table is currently not sorted. """
    def getSortedOrder(self) -> Any:
        """Current sort order. If getSortedColumn is negative, it will return None. """

class _Columns:
    """Columns present in the table model. """
    color: int
    participant: int
    size: int
    status: int

class _Participant:
    """Holds the data of a participant in the table model. """
    def __init__(self, clientId: Any, name: Any, color: Any, status: Any) -> None: ...

class _SyncReviewStatusModel(_PySide6_QtCore.QAbstractTableModel):
    """Data model for the data of the participants in the current sync review session. """
    staticMetaObject: _PySide6_QtCore.QMetaObject
    def __init__(self, view: Any) -> None: ...
    def columnCount(self, parent: Any) -> int: ...
    def data(self, index: Any, role: Any) -> _PySide6_QtGui.QColor | str | None: ...
    def enterSession(self, clientDataProvider: Any) -> None: ...
    def headerData(self, section: Any, orientation: Any, role: Any) -> _PySide6_QtGui.QIcon | str | None: ...
    def leaveSession(self) -> None: ...
    def rowCount(self, parent: Any) -> int: ...

def initialise(connectionManager: Any) -> None:
    """Initialize the global instance of the sync review status panel. """

def openStatusPanelIfClosed() -> None:
    """Opens the status panel in a floating window if it's closed and the user preference is to open
    it on session startup
    """
