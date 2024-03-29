"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import nuke
import PySide2
from PySide2.QtWidgets import *

from . import *


class AnimationKey(object):
    """
    A control point for an animation curve.
    @var x
    The horizontal position of the point
    @var y
    The vertical position of the point
    @var lslope
    The derivative to the left of the point. If interpolation does not have
    USER_SET_SLOPE then this may not be correct until after evaluate() has been
    called.
    @var rslope
    The derivative to the right of the point. If interpolation does not have
    USER_SET_SLOPE then this may not be correct until after evaluate() has been
    called.
    @var la
    The left 'bicubic' value. This represents the horizontal
    position of the left bezier handle end, where 1.0 means 1/3 of the
    distance to the previous point. If both handles for a span are 1.0
    then the horizontal interpolation is linear and thus the vertical
    interpolation a cubic function.  The legal values are 0 to
    3. Setting outside of this range will produce undefined results.
    @var ra
    The right 'bicubic' value, again the legal range is 0 to 3.
    @var interpolation
    Used to calculate all the slopes except for the left slope of the first key
    and the right slope of the last key.
    Legal values are:
    - USER_SET_SLOPE: If this bit is on, the slopes are fixed by
                      the user and interpolation and extrapolation are ignored.
    - CONSTANT: The value of the curve is equal to the y of the
                point to the left.
    - LINEAR: slopes point directly at the next key.
    - SMOOTH: same as CATMULL_ROM but the slopes are clamped so that the
              convex-hull property is preserved (meaning no part of the curve
              extends vertically outside the range of the keys on each side of
              it). This is the default.
    - CATMULL_ROM: the slope at key n is set to the slope between the control
                   points n-1 and n+1. This is used by lots of software.
    - cubic: the slope is calculated to the only cubic interpolation which makes
             the first and second derivatives continuous. This type of
             interpolation was very popular in older animation software.  A
             different cubic interpolation is figured out for each set of adjacent
             points with the CUBIC type.
    - for the smooth, CATMULL_ROM, and CUBIC interpolations, the first and last
      key have slopes calculated so that the second derivative is zero at them.
    @var extrapolation
    controls how to set the left slope of the first point and the right slope of
    the last point. Notice that this can be set differently on the first and last
    points, and is also remembered on all internal points so if end points are
    deleted old behavior is restored).
    - constant: the left slope of the first point, and the right slope of the last
                point, are set to zero.
    - linear: (and all other values): The left slope of the first point is set
              equal to it's right slope (calculated by the interpolation).
    the right slope of the last point is set equal to it's left slope.
    if there is only one point both slopes are set to zero.
    @var selected
    True if the point is selected in the curve editor.
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def __hash__(self, ) -> None:
        """
        Return hash(self).
        """
        ...

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...

    @property
    def x(self) -> typing.Any:
        """
        The horizontal position of the point
        """
        ...

    @property
    def y(self) -> typing.Any:
        """
        The vertical position of the point
        """
        ...

    @property
    def lslope(self) -> typing.Any:
        """
        The derivative to the left of the point
        """
        ...

    @property
    def rslope(self) -> typing.Any:
        """
        The derivative to the right of the point
        """
        ...

    @property
    def la(self) -> typing.Any:
        """
        The left 'bicubic' value
        """
        ...

    @property
    def ra(self) -> typing.Any:
        """
        The right 'bicubic' value
        """
        ...

    @property
    def interpolation(self) -> typing.Any:
        """
        Used to calculate all the slopes except for the left slope of the first key and the right slope of the last key
        """
        ...

    @property
    def extrapolation(self) -> typing.Any:
        """
        Controls how to set the left slope of the first point and the right slope of the last point
        """
        ...

    @property
    def selected(self) -> typing.Any:
        """
        True if the point is selected in the curve editor
        """
        ...
