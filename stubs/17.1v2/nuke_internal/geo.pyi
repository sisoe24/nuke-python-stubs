# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
from typing import final

@final
class AttrGroup:
    """The available attribute groups. Use these in conjunction with the Attribute and AttribContext methods."""
    Group_Attributes: int
    Group_Last: int
    Group_Matrix: int
    Group_None: int
    Group_Object: int
    Group_Points: int
    Group_Primitives: int
    Group_Vertices: int

@final
class AttrType:
    """The available attribute types. Used by the Attribute and AttribContext classes. Note that we don't support pointer attributes in python, although we do report their type."""
    eFloatAttrib: int
    eIntAttrib: int
    eInvalidAttrib: int
    eMatrix3Attrib: int
    eMatrix4Attrib: int
    eNormalAttrib: int
    ePointerAttrib: int
    eStringAttrib: int
    eVector2Attrib: int
    eVector3Attrib: int
    eVector4Attrib: int

@final
class AttribContext:
    """A set of selected items on a single of 3d object."""
    attribute: Any
    channel: Any
    def empty(self) -> bool:
        """self.empty() -> bool
        Whether this attribute is empty, i.e. contains no values, or not.
        """
    group: Any
    name: Any
    recursive: Any
    type: Any
    varying: Any

@final
class Attribute:
    """An attribute on a 3d object."""
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def invalid(self) -> bool:
        """self.invalid() -> bool
        Check whether the type for this attribute is valid (i.e. one of the known and supported types). This is equivalent to 'not self.valid()'
        """
    name: Any
    type: Any
    def valid(self) -> bool:
        """self.valid() -> bool
        Check whether the type for this attribute is valid (i.e. one of the known and supported types).
        """

@final
class GeoInfo:
    """A 3D object consisting of vertices and primitives built out of them."""
    def attribContext(self, name: Any, group: Any, type: Any) -> AttribContext:
        """self.attribContext(name, group, type) -> AttribContext
        Gets an attribute context for the named attribute of this object. If the attribute doesn't exist, returns None.

        The group and type parameters are both optional. The group specifies what the attribute applies to; it can be any of:
          0  primitives
          1  vertices
          2  points
          3  object
          4  matrix

        The type parameter specifies the expected type of the object. It can be any of:
          0  float
          1  Vector2
          2  Vector3
          3  Vector4
          4  a normal vector (stored as a Vector3)
          5  int
          6  string
          7  std::string
          8  pointer
          9  Matrix3
          10 Matrix4
        """
    def constructNormals(self) -> Any:
        """self.constructNormals() -> list of (x,y,z) tuples
        Computes the list of vertex normals for this object from its primitives.
        """
    def normals(self) -> Any:
        """self.normals() -> list of (x,y,z) tuples
        Gets the list of vertex normals for this object.
        """
    def points(self) -> PointList:
        """self.points() -> PointList
        Gets the point list for this object.
        """
    def primitives(self) -> Any:
        """self.primitives() -> list of point index lists
        Gets the list of primitives which make up this object.
        """
    def transform(self) -> Any:
        """self.transform() -> 4x4 tuple of floats
        Gets the transform matrix from the objects local coordinate system to world coordinates.
        """

@final
class GeometryList:
    """A list of GeoInfo objects."""
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __len__(self, /) -> int:
        """Return len(self)."""

@final
class PointList:
    """A list of points.

    Each point is represented as an (x,y,z) tuple of floats.
    """
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __len__(self, /) -> int:
        """Return len(self)."""

@final
class Primitive:
    """The base class for geometric primitives in Nuke."""
    def averageCenter(self, pointlist: Any) -> Any:
        """self.averageCenter(pointlist) -> (x, y, z)
        Get the average x,y,z location of all points in this primitive. The pointlist parameter should be the result of the points() method on the GeoInfo object which owns this primitive.
        """
    def faceAverageCenter(self, faceIndex: Any, pointlist: Any) -> Any:
        """self.faceAverageCenter(faceIndex, pointlist) -> (x, y, z)
        Get the average x,y,z location of all points in a particular face. The faceIndex parameter specifies which face to process. The pointlist parameter should be the result of the points() method on the GeoInfo object which owns this primitive.
        """
    def faceVertices(self, faceIndex: Any) -> Any:
        """self.faceVertices(faceIndex) -> list of int
        Get the list of point indexes for a particular face. The faceIndex parameter specifies which face to process.
        """
    def faces(self) -> int:
        """self.faces() -> int
        Get the number of sub-faces this primitive generates.
        """
    def normal(self) -> Any:
        """self.normal() -> (x, y, z)
        Get the normal for this primitive.
        """
    def points(self) -> Any:
        """self.points() -> list of int
        Get the list of point indexes for this primitive. The indexes refer to the position of the point in the point list of the GeoInfo object which owns this primitive.
        """

def bestFitPlane(*points: Any) -> tuple:
    """bestFitPlane(*points) -> (_nukemath.Vector3, _nukemath.Vector3, _nukemath.Vector3)

    Find the plane of best fit through a set of 3D points.

    :param points: The points to fit the plane through. Each point must be a
     _nukemath.Vector3 object.
    :return: 3 non-collinear points on the plane, in a tuple.
    """
