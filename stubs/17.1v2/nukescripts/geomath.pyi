# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any

def get_prim_world_rotation_zxy(prim: Any, time: Any) -> list:
    """Get xyz rotation angles in radians for the prim in world space
    assuming zxy rotation order
    """

def get_world_point_on_bbox(prim: Any, position: str, time: Any) -> Any:
    """Return points inside or on the bounding box of a prim in world space"""

def plane_rotation(tri: Any, norm: Any = ...) -> Any:
    """Calculate the rotations around the X, Y and Z axes in radians that will align a plane
    perpendicular to the Z axis with the given triangle.

    @param tri: A list or tuple of 3 _nukemath.Vector3 objects. The 3 points must
    describe the plane (i.e. they must not be collinear).
    @return: A _nukemath.Vector3 object where the x coordinate is the angle of
    rotation around the x axis and so on in radians.
    @raise ValueError: if the three points are collinear.
    """

def rotate_matrix_xyz(rotations: Any) -> Any:
    """Generates a rotation XYZ matrix from the input vector.

    @type rotations:  _nukemath.Vector3
    @param rotations: Vector that will be used generate the rotate matrix.
    @return:          The rotate matrix.
    """

def rotate_matrix_zxy(rotations: Any) -> Any:
    """Generates a rotation ZXY matrix from the input vector.

    @type rotations:  _nukemath.Vector3
    @param rotations: Vector that will be used generate the rotate matrix.
    @return:          The rotate matrix.
    """

def scaling_matrix(scalings: Any) -> Any:
    """Generates a scaling matrix from the input vector.

    @type scalings:  _nukemath.Vector3
    @param scalings: Vector that will be used generate the scaling matrix.
    @return:         The scaling matrix.
    """

def translate_matrix(translations: Any) -> Any:
    """Generates a translation matrix from the input vector.

    @type translations:   _nukemath.Vector3
    @param translations:  Vector that will be used generate the translation
    matrix.
    @return:              The translate matrix.
    """

def transpose_matrix3(m: Any) -> None:
    """Transpose Matrix3 in place"""
