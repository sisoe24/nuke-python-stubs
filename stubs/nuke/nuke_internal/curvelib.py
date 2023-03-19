"""The Python interface for Nuke's curve library (as used by
Roto, RotoPaint, SplineWarp).

Use help('_curvelib') to get detailed help on the classes exposed here.

This module provides the public interface to the curvelib module and will
remain stable. It uses an underlying native module called _curvelib to
provide this interface. While there is nothing stopping you from using the
_curvelib module directly, it may change in a future release and break your
scripts.
"""

import _curvelib
# enums
from _curvelib import (Flag, CVec2, CVec3, CVec4, CMatrix4, FlagType,
                       AnimCurve, BaseCurve, CurveType, CTransform, CubicCurve,
                       AnimCurveKey, ControlPoint, RotationOrder,
                       AnimAttributes, AnimCTransform, AnimCurveViews,
                       TransformOrder, AnimControlPoint, ExtrapolationType,
                       InterpolationType)
