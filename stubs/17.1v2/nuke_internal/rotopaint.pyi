# Type stubs for nuke 17.1v2. Generated; do not edit.

"""The Python interface for RotoPaint

Use help('_rotopaint') to get detailed help on the classes exposed here.
"""

from typing import Any
from nuke import Hash as Hash
from nuke_internal.curveknob import AnimAttributes as AnimAttributes
from nuke_internal.curveknob import AnimCTransform as AnimCTransform
from nuke_internal.curveknob import AnimControlPoint as AnimControlPoint
from nuke_internal.curveknob import AnimCurve as AnimCurve
from nuke_internal.curveknob import AnimCurveKey as AnimCurveKey
from nuke_internal.curveknob import AnimCurveViews as AnimCurveViews
from nuke_internal.curveknob import BaseCurve as BaseCurve
from nuke_internal.curveknob import CMatrix4 as CMatrix4
from nuke_internal.curveknob import CTransform as CTransform
from nuke_internal.curveknob import CVec2 as CVec2
from nuke_internal.curveknob import CVec3 as CVec3
from nuke_internal.curveknob import CVec4 as CVec4
from nuke_internal.curveknob import ControlPoint as ControlPoint
from nuke_internal.curveknob import CubicCurve as CubicCurve
from nuke_internal.curveknob import CurveKnob as CurveKnob
from nuke_internal.curveknob import CurveType as CurveType
from nuke_internal.curveknob import Element as Element
from nuke_internal.curveknob import ExtrapolationType as ExtrapolationType
from nuke_internal.curveknob import Flag as Flag
from nuke_internal.curveknob import FlagType as FlagType
from nuke_internal.curveknob import InterpolationType as InterpolationType
from nuke_internal.curveknob import Layer as Layer
from nuke_internal.curveknob import RotationOrder as RotationOrder
from nuke_internal.curveknob import Shape as Shape
from nuke_internal.curveknob import ShapeControlPoint as ShapeControlPoint
from nuke_internal.curveknob import Stroke as Stroke
from nuke_internal.curveknob import TransformOrder as TransformOrder

def convertDirectoryToNuke6(fromDir: Any, toDir: Any, matchPattern: str = ..., overwrite: bool = ...) -> None:
    """Convert a directory containing NUKE 7 roto scripts in one containing the old format.
    Note that the pattern is a regular expression.
    """

def convertDirectoryToNuke7(fromDir: Any, toDir: Any, matchPattern: str = ..., overwrite: bool = ...) -> None:
    """Convert a directory containing NUKE 6 roto scripts in one containing the new format.
    Note that the pattern is a regular expression.
    """

def convertToNuke6(fromScript: Any, toScript: Any, overwrite: bool = ...) -> None:
    """Convert a script containing NUKE 7 roto in one containing the old format."""

def convertToNuke7(fromScript: Any, toScript: Any, overwrite: bool = ...) -> None:
    """Convert a script containing NUKE 6 roto in one containing the new format."""
