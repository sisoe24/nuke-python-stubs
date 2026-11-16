# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
from typing import Generator
import collections.abc as _collections_abc
import nuke as _nuke
from nukescripts.geomath import get_prim_world_rotation_zxy as get_prim_world_rotation_zxy
from nukescripts.geomath import get_world_point_on_bbox as get_world_point_on_bbox
from nukescripts.geomath import plane_rotation as plane_rotation
from nukescripts.geomath import rotate_matrix_xyz as rotate_matrix_xyz
from nukescripts.geomath import rotate_matrix_zxy as rotate_matrix_zxy
from nukescripts.geomath import scaling_matrix as scaling_matrix
from nukescripts.geomath import translate_matrix as translate_matrix
from nukescripts.geomath import transpose_matrix3 as transpose_matrix3

class GeoVertexInfo:
    """Information on a single vertex in the selection"""
    def __init__(self, objnum: Any, index: Any, value: Any, position: Any, normal: Any) -> None: ...
    def __lt__(self, other: Any) -> bool:
        """The implementation of the Less Than operator serves the purpose of
        proper sorting of class instances, where the Object ID, followed by
        the Point Index are predominant over the actual position value of
        the selected point.
        This allows keeping the order of sorted points over changing location
        of the points.
        """

class GeoVertexSelection:
    """Selection container"""
    def __init__(self) -> None: ...
    def __iter__(self) -> Generator[Any, Any, None]: ...
    def __len__(self) -> int: ...
    def add(self, vertex_info: Any) -> None: ...
    def indices(self) -> dict[Any, Any]: ...
    def inverse_rotate(self, vector: Any, order: Any) -> None: ...
    def points(self) -> list[Any]: ...
    def scale(self, vector: Any) -> None: ...
    def translate(self, vector: Any) -> None: ...
    def unique_positions_sorted(self) -> list[Any]: ...

def average_normal(vertex_selection: GeoVertexSelection) -> Any:
    """Return a _nukemath.Vector3 which is the average of the normals of all selected points"""

def calc_average_position(vertex_selection: GeoVertexSelection) -> None:
    """Calculate the average position of all points.

    @param points: An iterable sequence of _nukemath.Vector3 objects.
    @return: A _nukemath.Vector3 containing the average of all the points.
    """

def calc_bounds(vertex_selection: GeoVertexSelection) -> Any:
    """Get the size of the bounding box of all the selected points
    Avoid zero size to allow inverse scaling (1/scale)
    """

def calc_rotation_vector(vertex_selection: GeoVertexSelection, norm: Any) -> Any:
    """Get the rotation vector"""

def check_all_point_collinear(points: Any) -> bool:
    """Iterates through the points the point and checks if all of them are collinear.
    The points must contain more than two points.
    @param points:  Points to check
    """

def copy_stage(stage: Any) -> Any:
    """Returns a copy of the given stage. This can be expensive so should be avoided where possible."""

def degrees(vector: Any) -> list:
    """Return a list of all radians values in argument converted to degrees"""

def ensure_frame_range(frames: Any) -> list[Any] | _collections_abc.Iterable[Any]:
    """If frames is not iterable (i.e it's a single number) we create an array with the single frame"""

def fuzzy_is_zero(value: Any) -> bool:
    """Returns true if a value is very close to zero."""

def fuzzy_vector3_add(v1: Any, v2: Any) -> Any:
    """Adds two vectors ensuring the coordinates are actually 0.0 if they are 0.0001
    of zero.
    """

def geo_to_selection(node_to_snap: _nuke.Node, frames: Any, translate_enabled: bool, rotate_enabled: bool, scale_enabled: bool, animate_single_frame: bool = ..., stage: Any = ..., task: _nuke.ProgressTask | None = ...) -> bool:
    """Translate/rotate/scale the specified node to the average position of the current vertex
    selection on the stage.

    @type node_to_snap:             nuke.Node
    @param node_to_snap:            Node to translate/rotate/scale
    @type frames:                   int or int array
    @param frames:                  The frame or array of frames to affect
    @type translate_enabled:        boolean
    @param translate_enabled:       Whether to apply the translation to the node
    @type rotate_enabled:           boolean
    @param rotate_enabled:          Whether to apply the rotation to the node
    @type scale_enabled:            boolean
    @param scale_enabled:           Whether to apply the scale to the node
    @type animate_single_frame:     boolean
    @param animate_single_frame:    If true, will set key for animation if affecting 1 frame.
                                    Always will set keys for animation if affecting multiple frames
    @type stage:                    pxr.Usd.Stage
    @param stage:                   The stage to get the selected vertex info from. If None, this
                                    method will attempt to get the stage from the active viewer.
    @type task:                     nuke.ProgressTask
    @param task:                    An optional progress task that will update as frames are processed.
    @return:                        True if this method was successful, False otherwise.
    """

def get_axis_pivot_rotate_knob(node_to_snap: Any) -> Any:
    """Get the axis pivot_rotate knob"""

def get_axis_pivot_translate_knob(node_to_snap: Any) -> Any:
    """Get the axis pivot_translate knob"""

def get_axis_rotate_knob(node_to_snap: Any) -> Any:
    """Get the axis rotate knob"""

def get_axis_scaling_knob(node_to_snap: Any) -> Any:
    """Get the axis scaling knob"""

def get_axis_translate_knob(node_to_snap: Any) -> Any:
    """Get the axis translate knob"""

def get_axis_uniform_scaling_knob(node_to_snap: Any) -> Any:
    """Get the axis uniform_scale knob"""

def get_node_transform_matrix(node_to_snap: _nuke.Node, current_frame: Any) -> Any:
    """Generates the transformation matrix for a given node based on its knob
    values.

    @type node_to_snap:  nuke.Node
    @param node_to_snap: Node from which the data will be extracted to generate
                      its transformation matrix.
    @return:           The matrix containg all node transformations.
    """

def get_rotate_enabled(node: Any, knob_name_prefix: Any) -> Any:
    """Get whether rotation is enabled by the snap knob with the given prefix"""

def get_scale_enabled(node: Any, knob_name_prefix: Any) -> Any:
    """Get whether scale is enabled by the snap knob with the given prefix"""

def get_selected_prim_path(geo_selection: Any) -> None:
    """Get the currently selected prim"""

def get_stage_from_active_viewer(frame_range: Any) -> None:
    """Gets the stage from the active viewer with the specified frame range."""

def get_translate_enabled(node: Any, knob_name_prefix: Any) -> Any:
    """Get whether translation is enabled by the snap knob with the given prefix"""

def get_vertex_selection(stage: Any, current_frame: Any, selection_threshold: float = ...) -> GeoVertexSelection:
    """Build a GeoVertexSelection from GeoVertexInfos"""

def least_significant_axis(vector: Any) -> int:
    """Given a Vector3, returns the least significant axis position, being x, y and
    z 0, 1 and 2 respectively.
    @type vector: _nukemath.Vector3
    @param vector: a Vector3
    @return the position of the least significant component of the vector.
    """

def need_stage_copy(frame_range: Any, task: Any = ...) -> bool:
    """This method will either return true if a copy of the stage is needed, false otherwise.
    Currently, updating the task progress can cause recomposition of the stage from the viewer if changes
    have been made. We need a copy of the stage to ensure this wont change during the calculation.
    """

def on_snap_knob(origin_knob: _nuke.Knob, command: str) -> None:
    """Called by the snap knobs to perform a pivot_to_selection/pivot_to_bbox/geo_to_selection operation.

    @type origin_knob:  nuke.Knob
    @param origin_knob: Knob that was used to start this operation. This is used to determine
                        the operation to perform as well as finding the parameters for the
                        operation from other related snap knobs on the node.
    @type command:      str
    @param command:     An additional command string currently used by the pivot_to_bbox operation
                        specifying the side of the bounding box to snap to. This must be one of:
                        Center/Top/Bottom/Left/Right/Front/Back if pivot_to_bbox operation, otherwise
                        this parameter is ignored.
    """

def pivot_to_bbox(node_to_snap: _nuke.Node, frames: Any, rotate_enabled: bool, command: str, animate_single_frame: bool = ..., stage: Any = ..., task: _nuke.ProgressTask | None = ...) -> bool:
    """Translate and optionally rotate the specified node's Pivot Point to a chosen point on the
    currently selected prim's bounding box.

    @type node_to_snap:             nuke.Node
    @param node_to_snap:            Node to translate and optionally rotate
    @type frames:                   int or int array
    @param frames:                  The frame or array of frames to affect
    @type rotate_enabled:           boolean
    @param rotate_enabled:          Whether to apply the rotation to the node
    @type command:                  str
    @param command:                 The side of the bounding box to snap to. This must be one of:
                                    Center/Top/Bottom/Left/Right/Front/Back
    @type animate_single_frame:     boolean
    @param animate_single_frame:    If true, will set key for animation if affecting 1 frame.
                                    Always will set keys for animation if affecting multiple frames
    @type stage:                    pxr.Usd.Stage
    @param stage:                   The stage to get the selected prim from. If None, this
                                    method will attempt to get the stage from the active viewer.
    @type task:                     nuke.ProgressTask
    @param task:                    An optional progress task that will update as frames are processed.
    @return:                        True if this method was successful, False otherwise.
    """

def pivot_to_selection(node_to_snap: _nuke.Node, frames: Any, translate_enabled: bool, rotate_enabled: bool, animate_single_frame: bool = ..., stage: Any = ..., task: _nuke.ProgressTask | None = ...) -> bool:
    """Translate and/or rotate the specified node's Pivot Point to the average position/rotation of the
    current vertex selection on the stage.

    @type node_to_snap:             nuke.Node
    @param node_to_snap:            Node to translate/rotate
    @type frames:                   int or int array
    @param frames:                  The frame or array of frames to affect
    @type translate_enabled:        boolean
    @param translate_enabled:       Whether to apply the translation to the node
    @type rotate_enabled:           boolean
    @param rotate_enabled:          Whether to apply the rotation to the node
    @type animate_single_frame:     boolean
    @param animate_single_frame:    If true, will set key for animation if affecting 1 frame.
                                    Always will set keys for animation if affecting multiple frames
    @type stage:                    pxr.Usd.Stage
    @param stage:                   The stage to get the selected vertex info from. If None, this
                                    method will attempt to get the stage from the active viewer.
    @type task:                     nuke.ProgressTask
    @param task:                    An optional progress task that will update as frames are processed.
    @return:                        True if this method was successful, False otherwise.
    """

def radians(vector: Any) -> list:
    """Return a list of all degree values in argument converted to radians"""

def rotate_geo_to_points_verified(node_to_snap: Any, vertex_selection: GeoVertexSelection, adjust_selection_only: Any, animate_enabled: bool = ..., current_frame: Any = ...) -> None:
    """Rotate the geometry to the vertex selection (does not check for required conditions)"""

def rotate_pivot_to_angles_verified(node_to_snap: Any, pivot_rotate: Any, animate_enabled: Any, current_frame: Any) -> None:
    """Rotate the pivot to rotation angles without affecting the geometry's position"""

def rotate_pivot_to_points_verified(node_to_snap: Any, vertex_selection: GeoVertexSelection, animate_enabled: Any, current_frame: Any) -> None:
    """Rotate the pivot to the vertex selection without affecting the geometry's position"""

def scale_geo_to_points_verified(node_to_snap: Any, vertex_selection: GeoVertexSelection, animate_enabled: bool = ..., current_frame: Any = ...) -> None:
    """Scale the geometry to the vertex selection (does not check for required conditions)"""

def selected_vertex_infos(stage: Any, current_frame: Any, selection_threshold: float = ...) -> Generator[GeoVertexInfo, Any, None]:
    """selectedVertexInfos(selectionThreshold) -> iterator

    Return an iterator which yields a tuple of the index and position of each
    point currently selected in the Viewer in turn.

    The selectionThreshold parameter is used when working with a soft selection.
    Only points with a selection level >= the selection threshold will be
    returned by this function.
    """

def should_animate(num_of_frames_to_affect: Any, animate_single_frame: Any) -> bool:
    """Returns whether we need to animate the knob by checking how many frames we are going to affect and
    whether we want to animate even if only a single frame will be affected.
    """

def translate_geo_to_points_verified(node_to_snap: Any, vertex_selection: GeoVertexSelection, adjust_selection_only: Any, animate_enabled: bool = ..., current_frame: Any = ...) -> None:
    """Translate the geometry to the vertex selection (does not check for required conditions)"""

def translate_pivot_to_points_verified(node_to_snap: Any, vertex_selection: GeoVertexSelection, animate_enabled: Any, current_frame: Any) -> None:
    """Translate the pivot to the vertex selection without affecting the geometry's position"""

def translate_pivot_to_world_pos_verified(node_to_snap: Any, world_position: Any, animate_enabled: Any, current_frame: Any) -> None:
    """Translate the pivot to world position without affecting the geometry's position"""

def translate_rotate_pivot(node_to_snap: _nuke.Node, translate: Any, rotate: Any, current_frame: Any) -> tuple:
    """Pivot translation and rotation must keep the object stationary and in
    order to do that compensation values must be placed in the geometry translate
    and rotate.

    @type node_to_snap:   nuke.Node
    @param node_to_snap:  Node to translate and rotate
    @type translate:    _nukemath.Vector3
    @param translate:   Target position for the pivot point.
    @type rotate:       _nukemath.Vector3
    @param rotate:      Target rotation for the pivot point.
    @return:            A tuple with the new geometry translation and rotation
                        respectively (_nukemath.Vector3, _nukemath.Vector3).
    """

def verify_node_order(node: Any, knob_name: Any, order_name: Any) -> None:
    """Verify the transform/rotation order"""

def verify_node_to_snap(node_to_snap: Any, knob_list: Any) -> None:
    """Check knobs exist and current transform/rotation order is supported"""

def verify_vertex_selection_for_rotation(vertex_selection: GeoVertexSelection) -> None:
    """GeoSelection should have at least 3 selected vertices for rotation"""

def verify_vertex_selection_not_empty(vertex_selection: GeoVertexSelection) -> None:
    """GeoSelection should have at least 1 selected vertex."""
