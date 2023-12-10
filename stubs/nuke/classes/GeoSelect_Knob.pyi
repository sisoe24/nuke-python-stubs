from typing import *
from numbers import Number

import nuke

from . import *

class GeoSelect_Knob(Knob):
    """
    A knob which allows selection of parts of a 3D object.
    """
    def __getattribute__(self, name, ) -> None:
        """
        Return getattr(self, name).
        """
        ...

    def __setattr__(self, name, value, ) -> None:
        """
        Implement setattr(self, name, value).
        """
        ...

    def __delattr__(self, name, ) -> None:
        """
        Implement delattr(self, name).
        """
        ...

    def getGeometry(self,) -> list:
        """
        self.getGeometry() -> _geo.GeometryList
        Get the geometry which this knob can select from.
        """
        ...

    def getSelection(self,) -> list:
        """
        self.getSelection() -> list of lists of floats
        Returns the selection for each vertex as a float. If you access the result as selection[obj][pt], then obj is the index of the object in the input geometry and pt is the index of the point in that object.
        """
        ...

    def getSelectionWeights(self,) -> list:
        """
        self.getSelectionWeights() -> list of lists of floats
        Returns the selection weights for each vertex as a float. If you access the result as selection[obj][pt], then obj is the index of the object in the input geometry and pt is the index of the point in that object. LALA
        """
        ...

    def getSelectedFaces(self,) -> list:
        """
        self.getSelectedFaces() -> list of lists of floats
        Returns the selection for each face as a float. If you access the result as selection[obj][fc], then obj is the index of the object in the input geometry and fc is the index of the face in that object.
        """
        ...

    def getFaceWeights(self,) -> list:
        """
        self.getFaceWeights() -> list of lists of floats
        Returns the selection weight for each face as a float. If you access the result as selection[obj][fc], then obj is the index of the object in the input geometry and fc is the index of the face in that object.
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
