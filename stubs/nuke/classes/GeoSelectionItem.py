"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class GeoSelectionItem(pybind11_object):
    """

    """

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    def getPath(self: _nuke.GeoSelectionItem) -> str:
        """
        getPath(self: _nuke.GeoSelectionItem) -> usg::Path
        """
        ...

    def getObject(self: _nuke.GeoSelectionItem) -> bool:
        """
        getObject(self: _nuke.GeoSelectionItem) -> bool
        """
        ...

    def getVertices(self: _nuke.GeoSelectionItem) -> List[float]:
        """
        getVertices(self: _nuke.GeoSelectionItem) -> List[float]
        """
        ...

    def getVertexWeights(self: _nuke.GeoSelectionItem) -> List[float]:
        """
        getVertexWeights(self: _nuke.GeoSelectionItem) -> List[float]
        """
        ...

    def getFaces(self: _nuke.GeoSelectionItem) -> List[float]:
        """
        getFaces(self: _nuke.GeoSelectionItem) -> List[float]
        """
        ...

    def getFaceWeights(self: _nuke.GeoSelectionItem) -> List[float]:
        """
        getFaceWeights(self: _nuke.GeoSelectionItem) -> List[float]
        """
        ...

    def getWorldPoints(self: _nuke.GeoSelectionItem, stage: usg: : Stage, time: float = nan) -> list:
        """
        getWorldPoints(self: _nuke.GeoSelectionItem, stage: usg::Stage, time: float = nan) -> usg::Array<fdk::Vec3<float> >
        """
        ...

    def getWorldNormals(self: _nuke.GeoSelectionItem, stage: usg: : Stage, time: float = nan) -> list:
        """
        getWorldNormals(self: _nuke.GeoSelectionItem, stage: usg::Stage, time: float = nan) -> usg::Array<fdk::Vec3<float> >
        """
        ...
