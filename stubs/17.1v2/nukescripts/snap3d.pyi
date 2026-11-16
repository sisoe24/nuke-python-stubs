# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
from typing import Generator
import nuke as _nuke

snapFuncs: list

class VertexInfo:
    def __init__(self, objnum: Any, index: Any, value: Any, position: Any, normal: Any) -> None: ...
    def __lt__(self, other: Any) -> bool:
        """The implementation of the Less Than operator serves the purpose of
        proper sorting of class instances, where the Object ID, followed by
        the Point Index are predominant over the actual position value of
        the selected point.
        This allows keeping the order of sorted points over changing location
        of the points.
        """

class VertexSelection:
    def __init__(self) -> None: ...
    def __iter__(self) -> Generator[Any, Any, None]: ...
    def __len__(self) -> int: ...
    def add(self, vertexInfo: Any) -> None: ...
    def indices(self) -> dict[Any, Any]: ...
    def inverseRotate(self, vector: Any, order: Any) -> None: ...
    def points(self) -> list[Any]: ...
    def scale(self, vector: Any) -> None: ...
    def translate(self, vector: Any) -> None: ...
    def uniquePositionsSorted(self) -> list[Any]: ...

def addSnapFunc(label: Any, func: Any) -> None:
    """addSnapFunc(label, func) -> None
    Add a new snapping function to the list.

    The label parameter is the text that will appear in (eg.) an Enumeration_Knob
    for the function. It cannot be the same as any existing snap function label
    (if it is, the function will abort without changing anything).

    The func parameter is the snapping function. It must be a callable object
    taking a single parameter: the node to perform the snapping on.
    """

def allNodes(node: Any = ...) -> Generator[Any, Any, None]:
    """allNodes() -> iterator
    Return an iterator which yields all nodes in the current script.

    This includes nodes inside groups. They will be returned in top-down,
    depth-first order.
    """

def allNodesWithGeoSelectKnob() -> list[Any]: ...

def anySelectedPoint(selectionThreshold: float = ...) -> None:
    """anySelectedPoint(selectionThreshold) -> _nukemath.Vector3
    Return a selected point from the active viewer or the first viewer with a selection.
    The selectionThreshold parameter is used when working with a soft selection.
    Only points with a selection level >= the selection threshold will be returned by this function.
    """

def anySelectedVertexInfo(selectionThreshold: float = ...) -> VertexInfo:
    """anySelectedVertexInfo(selectionThreshold) -> VertexInfo

    Returns a single VertexInfo for a selected point. If more than one point is
    selected, one of them will be chosen arbitrarily.

    The selectionThreshold parameter is used when working with a soft selection.
    Only points with a selection level >= the selection threshold will be
    returned by this function.
    """

def averageNormal(vertexSelection: Any) -> None:
    """averageNormal(selectionThreshold -> _nukemath.Vector3
    Return a _nukemath.Vector3 which is the average of the normals of all selected points
    """

def calcAveragePosition(vertexSelection: Any) -> None:
    """Calculate the average position of all points.

    @param points: An iterable sequence of _nukemath.Vector3 objects.
    @return: A _nukemath.Vector3 containing the average of all the points.
    """

def calcBounds(vertexSelection: Any) -> Any: ...

def calcRotationVector(vertexSelection: Any, norm: Any) -> None: ...

def callSnapFunc(nodeToSnap: Any = ...) -> None:
    """callSnapFunc(nodeToSnap) -> None
    Call the snapping function on a node.

    The nodeToSnap parameter is optional. If it's not specified, or is None, we
    use the result of nuke.thisNode() instead.

    The node must have an Enumeration_Knob called "snapFunc" which selects the
    snapping function to call.
    """

def cameraProjectionMatrix(cameraNode: Any) -> Any:
    """Calculate the projection matrix for the camera based on its knob values."""

def checkAllPointCollinear(points: Any) -> bool:
    """Iterates through the points the point and checks if all of them are collinear.
    The points must contain more than two points.

    @type nodeToSnap:   Iterable of Vector3
    @param nodeToSnap:  Points to check
    """

def degrees(vector: Any) -> list: ...

def fuzzyIsZero(value: Any) -> bool:
    """Returns true if a value is very close to zero."""

def fuzzyVector3Add(v1: Any, v2: Any) -> Any:
    """Adds two vectors ensuring the coordinates are actually 0.0 if they are 0.0001
    of zero.
    """

def getAxisKnobPrefix() -> str:
    """Determine the correct knob name prefix for the Axis knob names
    by checking the originating knob that triggered the snap menu action.
    """

def getSelection(selectionThreshold: float = ...) -> VertexSelection: ...

def leastSignificantAxis(vector: Any) -> int:
    """Given a Vector3, returns the least significant axis position, being x, y and
    z 0, 1 and 2 respectively.
    @type vector: _nukemath.Vector3
    @param vector: a Vector3
    @return the position of the least significant component of the vector.
    """

def planeRotation(tri: Any, norm: Any = ...) -> Any:
    """Calculate the rotations around the X, Y and Z axes that will align a plane
    perpendicular to the Z axis with the given triangle.

    @param tri: A list or tuple of 3 _nukemath.Vector3 objects. The 3 points must
     describe the plane (i.e. they must not be collinear).
    @return: A _nukemath.Vector3 object where the x coordinate is the angle of
     rotation around the x axis and so on.
    @raise ValueError: if the three points are collinear.
    """

def projectPoint(camera: Any = ..., point: Any = ...) -> Any:
    """projectPoint(camera, point) -> nuke.math.Vector2

    Project the given 3D point through the camera to get 2D pixel coordinates.

    @param camera: The Camera node or name of the Camera node to use for projecting
                   the point.
    @param point: A nuke.math.Vector3 or of list/tuple of three float values
                  representing the 3D point.
    @raise ValueError: If camera or point is invalid.
    """

def projectPoints(camera: Any = ..., points: Any = ...) -> Generator[Any, Any, None]:
    """projectPoint(camera, points) -> list of nuke.math.Vector2

    Project the given 3D point through the camera to get 2D pixel coordinates.

    @param camera: The Camera node or name of the Camera node to use for projecting
                   the point.
    @param points: A list or tuple of either nuke.math.Vector3 or of list/tuples of
                   three float values representing the 3D points.
    @raise ValueError: If camera or point is invalid.
    """

def projectSelectedPoints(cameraName: str = ...) -> Generator[Any, Any, None]:
    """projectSelectedPoints(cameraName='Camera1') -> iterator yielding nuke.math.Vector2

    Using the specified camera, project all of the selected points into 2D pixel
    coordinates and return their locations.

    @param cameraName: Optional name of the Camera node to use for projecting the
                       points. If omitted, will look for a node called Camera1.
    """

def radians(vector: Any) -> list: ...

def rotateMatrixXYZ(rotations: Any) -> Any:
    """Generates a rotation XYZ matrix from the input vector.

    @type rotations:  _nukemath.Vector3
    @param rotations: Vector that will be used generate the rotate matrix.
    @return:          The rotate matrix.
    """

def rotateMatrixZXY(rotations: Any) -> Any:
    """Generates a rotation ZXY matrix from the input vector.

    @type rotations:  _nukemath.Vector3
    @param rotations: Vector that will be used generate the rotate matrix.
    @return:          The rotate matrix.
    """

def rotatePivotSelectionToPoints(nodeToSnap: Any, vertexSelection: Any) -> None: ...

def rotatePivotToPoints(nodeToSnap: _nuke.Node) -> None:
    """Rotate the specified node's Pivot Point to the average of the current vertex
    selection normals in the active viewer. The nodeToSnap must contain
    'translate', 'rotate', 'pivot_translate' and 'pivot_rotate' knobs, the
    transform order must be 'SRT' and the rotation order must be 'ZXY'.

    @type nodeToSnap:   nuke.Node
    @param nodeToSnap:  Node to translate its Pivot Point
    """

def rotatePivotToPointsVerified(nodeToSnap: Any, vertexSelection: Any) -> None: ...

def rotateToPointsVerified(nodeToSnap: Any, vertexSelection: Any) -> None: ...

def scaleToPointsVerified(nodeToScale: Any, vertexSelection: Any) -> None: ...

def scalingMatrix(scalings: Any) -> Any:
    """Generates a scaling matrix from the input vector.

    @type scalings:  _nukemath.Vector3
    @param scalings: Vector that will be used generate the scaling matrix.
    @return:         The scaling matrix.
    """

def selectedPoints(selectionThreshold: float = ...) -> Generator[Any, Any, None]:
    """selectedPoints(selectionThreshold) -> iterator

    Return an iterator which yields the position of every point currently
    selected in the Viewer in turn.

    The selectionThreshold parameter is used when working with a soft selection.
    Only points with a selection level >= the selection threshold will be
    returned by this function.
    """

def selectedVertexInfos(selectionThreshold: float = ...) -> Generator[VertexInfo, Any, None]:
    """selectedVertexInfos(selectionThreshold) -> iterator

    Return an iterator which yields a tuple of the index and position of each
    point currently selected in the Viewer in turn.

    The selectionThreshold parameter is used when working with a soft selection.
    Only points with a selection level >= the selection threshold will be
    returned by this function.
    """

def transformMatrix(nodeToSnap: _nuke.Node) -> Any:
    """Generates the transformation matrix for a given node based on its knob
    values.

    @type nodeToSnap:  nuke.Node
    @param nodeToSnap: Node from which the data will be extracted to generate
                       its transformation matrix.
    @return:           The matrix containg all node transformations.
    """

def translateMatrix(translations: Any) -> Any:
    """Generates a translation matrix from the input vector.

    @type translations:   _nukemath.Vector3
    @param translations:  Vector that will be used generate the translation
    matrix.
    @return:              The translate matrix.
    """

def translatePivotSelectionToPoints(nodeToSnap: Any, vertexSelection: Any) -> None: ...

def translatePivotToPoints(nodeToSnap: _nuke.Node) -> None:
    """Translate the specified node's Pivot Point to the average position of the
    current vertex selection in the active viewer. The nodeToSnap must contain
    'translate', 'rotate' and 'pivot_translate' knobs, the transform order must
    be 'SRT' and the rotation order must be 'ZXY'.

    @type nodeToSnap:   nuke.Node
    @param nodeToSnap:  Node to translate its Pivot Point
    """

def translatePivotToPointsVerified(nodeToSnap: Any, vertexSelection: Any) -> None: ...

def translateRotatePivot(nodeToSnap: _nuke.Node, translate: Any, rotate: Any) -> tuple:
    """Pivot translation and rotation must keep the object stationary and in
    order to do that compensation values must be placed in the geometry translate
    and rotate.

    @type nodeToSnap:   nuke.Node
    @param nodeToSnap:  Node to translate and rotate
    @type translate:    _nukemath.Vector3
    @param translate:   Target position for the pivot point.
    @type rotate:       _nukemath.Vector3
    @param rotate:      Target rotation for the pivot point.
    @return:            A tuple with the new geometry translation and rotation
                        respectively (_nukemath.Vector3, _nukemath.Vector3).
    """

def translateRotatePivotSelectionToPoints(nodeToSnap: Any, vertexSelection: Any) -> None: ...

def translateRotatePivotToPoints(nodeToSnap: _nuke.Node) -> None:
    """Translate the specified node's Pivot Point to the average position of the
    current vertex selection and rotate the pivot to align Z to match the average
    normals in the active viewer. The nodeToSnap must contain 'translate',
    'rotate', 'pivot_translate', 'pivot_rotate' and 'pivot_translate' knobs,
    the transform order must be 'SRT' and the rotation order must be 'ZXY'.

    @type nodeToSnap:   nuke.Node
    @param nodeToSnap:  Node to translate its Pivot Point
    """

def translateRotatePivotToPointsVerified(nodeToSnap: Any, vertexSelection: Any) -> None: ...

def translateRotateScaleSelectionToPoints(nodeToSnap: Any, vertexSelection: Any) -> None: ...

def translateRotateScaleThisNodeToPoints() -> None: ...

def translateRotateScaleToPoints(nodeToSnap: _nuke.Node) -> None:
    """Translate the specified node to the average position of the current vertex selection in the active viewer,
    rotate to the orientation of the (mean squares) best fit plane for the selection
    and scale to the extents of the selection.
    The nodeToSnap must contain 'translate', 'rotate' and 'scale' knobs, the transform order must be 'SRT' and
    the rotation order must be 'ZXY'.

    @type nodeToSnap:   nuke.Node
    @param nodeToSnap:  Node to translate, rotate and scale
    """

def translateRotateScaleToPointsVerified(nodeToSnap: Any, vertexSelection: Any) -> None: ...

def translateRotateSelectionToPoints(nodeToSnap: Any, vertexSelection: Any) -> None: ...

def translateRotateThisNodeToPoints() -> None: ...

def translateRotateToPoints(nodeToSnap: _nuke.Node) -> None:
    """Translate the specified node to the average position of the current vertex selection in the active viewer
    and rotate to the orientation of the (mean squares) best fit plane for the selection.
    The nodeToSnap must contain 'translate' and 'rotate' knobs, the transform order must be 'SRT' and the
    rotation order must be 'ZXY'.

    @type nodeToSnap:   nuke.Node
    @param nodeToSnap:  Node to translate and rotate
    """

def translateRotateToPointsVerified(nodeToSnap: Any, vertexSelection: Any) -> None: ...

def translateSelectionToPoints(nodeToSnap: Any, vertexSelection: Any) -> None: ...

def translateThisNodeToPoints() -> None: ...

def translateToPoints(nodeToSnap: _nuke.Node) -> None:
    """Translate the specified node to the average position of the current vertex selection in the active viewer.
    The nodeToSnap must contain a 'translate' knob and the transform order must be 'SRT'.

    @type nodeToSnap:   nuke.Node
    @param nodeToSnap:  Node to translate
    """

def translateToPointsVerified(nodeToSnap: Any, vertexSelection: Any) -> None: ...

def transpose(m: Any) -> None: ...

def verifyNodeOrder(node: Any, knobName: Any, orderName: Any) -> None: ...

def verifyNodeToSnap(nodeToSnap: Any, knobList: Any) -> None: ...

def verifyVertexSelection(vertexSelection: Any, minLen: Any) -> None: ...
