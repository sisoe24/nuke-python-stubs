# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any
from nukescripts import panels as panels
from nukescripts.execute import execute_panel as execute_panel

class TableDelegate:
    staticMetaObject: Any
    def initStyleOption(self, option: Any, index: Any) -> None: ...

class UDIMErrorDialog:
    staticMetaObject: Any
    def __init__(self, parent: Any = ..., error_msg: str = ..., udim_label: str = ...) -> None: ...

class UDIMFile:
    def __init__(self, udim: Any, uv: Any, filename: Any) -> None: ...

class UDIMOptionsDialog:
    staticMetaObject: Any
    def __init__(self, parent: Any = ..., parsing_func: Any = ..., udim_label: str = ...) -> None: ...
    def addUdimFile(self, udim_file: Any) -> None: ...
    def cellChanged(self, row: Any, column: Any) -> None: ...
    def importUdimFiles(self) -> None: ...
    def updateTableWidget(self) -> None: ...

def allign_nodes(nodes: Any, base: Any) -> None: ...

def checkUdimValue(udim: Any) -> bool: ...

def findNextName(name: Any) -> Any: ...

def parseUdimFile(f: Any) -> int | None:
    """Parsing a filename string in search of the udim number.
    The function returns the udim number, and None if it is not able to decode the udim value.

    The udim value is a unique number that defines the tile coordinate.
    If u,v are the real tile coordinates the equivalent udim number is calculated with the following formula:
    udim = 1001 + u + 10 * v    (Note: u >=0 && u < 10 && udim > 1000 && udim < 2000)

    Redefine this function if the parsing function is not appropriate with your filename syntax.
    """

def splitInSequence(f: Any) -> list[Any]: ...

def udimStr(s: Any, label: Any) -> Any: ...

def udim_group(nodes: Any) -> Any: ...

def udim_import(udim_parsing_func: Any = ..., udim_column_label: str = ...) -> None:
    """Imports a sequence of UDIM files and creates the node material tree needed.
        This function simplifies the process of importing textures. It generates a tree of nodes which
        adjusts the texture coordinates at rendering time for a model containing multiple texture tiles.
        In general a tile texture coordinate can be expressed with a single value(UDIM) or with a tuple(ST or UV).
        The udim_import function can decode a UDIM number from a filename.
        To determine the tile coordinate encoding for a generic filename convention, the udim_import script can use an
        external parsing function.

        The redefined parsing function needs to decode a filename string and return the udim or the u,v tile coordinate
        as an integer or tuple of integers. It should return None if the tile coordinate id can not be determined.

    @param udim_parsing_func:   The parsing function. This parses a filename string and returns a tile id.
    @param udim_column_label:   The name of the column in the dialog box used to show the tile id.
    @return:                    None
    """

def uv2udim(uv: Any) -> Any: ...
