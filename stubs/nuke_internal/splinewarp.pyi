# Type stubs for nuke 15.2v9. Generated; do not edit.

"""The Python interface for used by SplineWarp

Use help('_splinewarp') to get detailed help on the classes exposed here.
"""

from typing import Any
from typing import final
import nuke_internal.curveknob as _nuke_internal_curveknob
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

@final
class SplineKnob(_nuke_internal_curveknob.CurveKnob):
    def defaultJoin(self, AShape: Any, BShape: Any) -> Any:
        """self.defaultJoin(AShape, BShape) -> CorrespondencePoints
        Joins the two given SplineWarp elements.
        Does not create an undo nor call knob.changed on the spline knob
        """
    def getAB(self, shapeObj: Any) -> Any:
        """self.getAB(shapeObj, ) -> ["A"|"B"|"UNDEFINED"]
        Returns a string denoting the channel the given shape is in.
        A utility function wrapping the attribute getter for the ABAttribute
        """
    def getCorrespondencePoints(self, *args: Any, **kwargs: Any) -> Any:
        """self.getCorrespondencePoints('path/to/element') -> CorrespondencePoints
        Gets the collection of correspondence point collection for the element
        specified by the path.
        """
    def setAB(self, *args: Any, **kwargs: Any) -> None:
        """self.setAB(shapeObj, ["A"|"B"]) -> None
        Puts the given shape into the 'A' or the 'B' channel.
        A utility function wrapping the attribute setter for the ABAttribute
        Does not create an undo nor call knob.changed on the spline knob
        """
