"""The Python interface for used by SplineWarp and RotoPaint2

Use help('_curveknob') to get detailed help on the classes exposed here.
"""

import _curveknob
from _curveknob import (Layer, Shape, Stroke, Element, CurveKnob,
                        ShapeControlPoint)

from .curvelib import *
