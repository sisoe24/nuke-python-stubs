"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class GeoSelection(pybind11_object):
    """

    """

    def __init__(self: _nuke.GeoSelection) -> None:
        """
        __init__(self: _nuke.GeoSelection) -> None
        """
        ...

    def __getitem__(self: _nuke.GeoSelection, arg0: str) -> GeoSelectionItem:
        """
        __getitem__(self: _nuke.GeoSelection, arg0: str) -> Foundry::Python::GeoSelectionItem
        """
        ...

    def __len__(self: _nuke.GeoSelection) -> int:
        """
        __len__(self: _nuke.GeoSelection) -> int
        """
        ...

    def __iter__(self: _nuke.GeoSelection) -> Any:
        """
        __iter__(self: _nuke.GeoSelection) -> Iterator
        """
        ...

    def selectObject(self: _nuke.GeoSelection, arg0: str) -> None:
        """
        selectObject(self: _nuke.GeoSelection, arg0: str) -> None
        """
        ...

    def selectVertices(self: _nuke.GeoSelection, primPath: str, vertices: List[float], vertexWeights: List[float] = []) -> None:
        """
        selectVertices(self: _nuke.GeoSelection, primPath: str, vertices: List[float], vertexWeights: List[float] = []) -> None

        Select vertices, also sets vertex weights if given
        """
        ...

    def selectFaces(self: _nuke.GeoSelection, primPath: str, faces: List[float], faceWeights: List[float] = []) -> None:
        """
        selectFaces(self: _nuke.GeoSelection, primPath: str, faces: List[float], faceWeights: List[float] = []) -> None

        Select faces, also sets face weights if given
        """
        ...
