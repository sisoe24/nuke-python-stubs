# Type stubs for nuke 15.2v9. Generated; do not edit.

"""The Python interface for used by SplineWarp and RotoPaint2

Use help('_curveknob') to get detailed help on the classes exposed here.
"""

from typing import Any
from typing import final
from typing import overload
import nuke as _nuke

@final
class AnimAttributes:
    """A collection of named attributes.

    Each attribute is represented as a curve, parameterised over time. Convenience methods for managing the curves (adding and removing keys, etc.) are provided, as well as methods for managing the list of available attributes.

    Attributes can be accessed by index or by name. This class defines constants for standard names in use by Nuke.
    """
    kAlphaAttribute: str
    kAlphaOverlayAttribute: str
    kBlendingModeAttribute: str
    kBlueAttribute: str
    kBlueOverlayAttribute: str
    kBrushSizeAttribute: str
    kBrushSpacingAttribute: str
    kBrushTypeAttribute: str
    kBuildUpAttribute: str
    kDynamicHardnessAttribute: str
    kDynamicSizeAttribute: str
    kDynamicTransparencyAttribute: str
    kEffectParameter1Attribute: str
    kEffectParameter2Attribute: str
    kEffectParameter3Attribute: str
    kFeatherFallOffAttribute: str
    kFeatherOnAttribute: str
    kFeatherTypeAttribute: str
    kFeatherXAttribute: str
    kFeatherYAttribute: str
    kGreenAttribute: str
    kGreenOverlayAttribute: str
    kHardnessAttribute: str
    kInvertedAttribute: str
    kLifeTimeMAttribute: str
    kLifeTimeNAttribute: str
    kLifeTimeTypeAttribute: str
    kMotionBlurAttribute: str
    kMotionBlurOnAttribute: str
    kMotionBlurShutterAttribute: str
    kMotionBlurShutterOffsetAttribute: str
    kMotionBlurShutterOffsetTypeAttribute: str
    kNumberOfViewsAttribute: str
    kOpacityAttribute: str
    kPlanarTrackLayerAttribute: str
    kRedAttribute: str
    kRedOverlayAttribute: str
    kSourceAttribute: str
    kSourcePivotPointXAttribute: str
    kSourcePivotPointYAttribute: str
    kSourceRotateAttribute: str
    kSourceScaleXAttribute: str
    kSourceScaleYAttribute: str
    kSourceSkewOrderAttribute: str
    kSourceSkewXAttribute: str
    kSourceSkewYAttribute: str
    kSourceTimeOffsetAttribute: str
    kSourceTimeOffsetTypeAttribute: str
    kSourceTranslateRoundAttribute: str
    kSourceTranslateXAttribute: str
    kSourceTranslateYAttribute: str
    kTensionAttribute: str
    kViewAttribute: str
    kVisibleAttribute: str
    kWriteOnEndAttribute: str
    kWriteOnStartAttribute: str
    def __contains__(self, key: Any, /) -> bool:
        """Return key in self."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def add(self, name: Any, value: Any) -> None:
        """self.add(name, value) -> None
        Add a new attribute. The name parameter is the name for the attribute and value is the initial int or float value to assign to it.
        """
    @overload
    def addKey(self, time: Any, name: Any, value: Any, view: Any) -> None:
        """self.addKey(time, name, value, view) -> None
        self.addKey(time, view) -> None
        When a name and value is specified, this method adds a new key to an existing attribute at the given time. When the name and value are omitted, a new key is added to all attributes at the specified time. The view parameter is optional in either case.
        """
    @overload
    def addKey(self, time: Any, view: Any) -> None:
        """self.addKey(time, name, value, view) -> None
        self.addKey(time, view) -> None
        When a name and value is specified, this method adds a new key to an existing attribute at the given time. When the name and value are omitted, a new key is added to all attributes at the specified time. The view parameter is optional in either case.
        """
    def getCurve(self, attr: Any, view: Any) -> AnimCurve:
        """self.getCurve(attr, view) -> AnimCurve
        Gets the AnimCurve object for a particular attribute. The attr parameter can be the index or name of the attribute. The view parameter is optional.
        """
    def getKeyTime(self, index: Any, keyIndexOrHash: Any, view: Any = ...) -> float:
        """self.getKeyTime(index, keyIndexOrHash, view) -> float
        Gets the time a particular key is set at. The index parameter is the index of the attribute; keyIndexOrHash is either the index of the key in the attributes AnimCurve, or its associated Hash; and view is the optional view name. 
        """
    def getName(self, index: Any) -> str:
        """self.getName(index) -> str
        Get the name of an attribute when you know its index.
        """
    def getNumberOfKeys(self, attr: Any, view: Any) -> int:
        """self.getNumberOfKeys(attr, view) -> int
        Returns the number of keys in the curve for a particular attribute. The attr parameter can be the index or name of the attribute. The view parameter is optional.
        """
    def getValue(self, time: Any, indexOrName: Any, view: Any = ...) -> float:
        """self.getValue(time, indexOrName, view) -> float
        Evaluates the anim curve of an attribute at a particular time and returns the value.
        time is the time for which to evaluate the attribute; indexOrName is either the index of the attribute to evaluate, or its name; and view is the optional view name.
        """
    def remove(self, attributeIndexOrName: Any) -> None:
        """self.remove(attributeIndexOrName) -> None
        Remove an attribute. You can give the name or index of the attribute.
        """
    def removeAll(self) -> None:
        """self.removeAll() -> None
        Remove all attributes.
        """
    def removeKey(self, time: Any, attributeIndex: Any, view: Any) -> None:
        """self.removeKey(time, attributeIndex, view) -> None
        Remove a particular key from an attribute. The view parameter is optional.
        """
    def removeKeys(self, attributeIndex: Any, view: Any) -> None:
        """self.removeKeys(attributeIndex, view) -> None
        Remove all keys from an attribute. The view parameter is optional.
        """
    def reset(self) -> None:
        """self.reset() -> None
        Reset the object to have no attributes.
        """
    def set(self, time: Any, attributeIndexOrName: Any, value: Any, view: Any) -> None:
        """self.set(time, attributeIndexOrName, value, view) -> None
        Set the value of an attribute. The time parameter is optional: if it's present, a new key is created at that time with the specified value; if it's not present, a constant value is set for the attribute. The attribute to set may be identified by its name or index. The view parameter is optional.
        """
    def setCurve(self, index: Any, curve: Any) -> None:
        """self.setCurve(index, curve) -> None
        Replace the current anim curve for an attribute with a new one. The index parameter is the index of the attribute; and curve is an AnimCurve instance.
        """
    def setKey(self, time: Any, attributeIndex: Any, hash: Any, value: Any, view: Any) -> None:
        """self.setKey(time, attributeIndex, hash, value, view) -> None
        Set a key for an attribute. The time parameter is when the new key will be created for; the attributeIndex says which attribute to set the key for; the
        """
    def setName(self, attributeIndex: Any, newName: Any) -> None:
        """self.setName(attributeIndex, newName) -> None
        Change the name of an existing attribute.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> AnimAttributes: ...

@final
class AnimCTransform:
    """An animated transform, where each part of the transform is represented as a curve over time."""
    def addPivotPointKey(self, time: Any, x: Any, y: Any, pressure: Any, view: str = ...) -> None:
        """self.addPivotPointKey(time, x, y, pressure, view='default') -> None"""
    def addRotationKey(self, time: Any, x: Any, y: Any, pressure: Any, view: str = ...) -> None:
        """self.addRotationKey(time, x, y, pressure, view='default') -> None"""
    def addScaleKey(self, time: Any, x: Any, y: Any, pressure: Any, view: str = ...) -> None:
        """self.addScaleKey(time, x, y, pressure, view='default') -> None"""
    def addSkewXKey(self, time: Any, x: Any, y: Any, pressure: Any, view: str = ...) -> None:
        """self.addSkewXKey(time, x, y, pressure, view='default') -> None"""
    def addTransformKey(self, time: Any, view: Any) -> None:
        """self.addTransformKey(time, view) -> None"""
    def addTranslationKey(self, time: Any, x: Any, y: Any, pressure: Any, view: str = ...) -> None:
        """self.addTranslationKey(time, x, y, pressure, view='default') -> None"""
    def evaluate(self, time: Any, view: Any) -> None:
        """self.evaluate(time, view) -> None"""
    def getExtraMatrixAnimCurve(self, i: Any, j: Any, view: Any) -> AnimCurve:
        """self.getExtraMatrixAnimCurve(i, j, view) -> AnimCurve
        Returns the AnimCurve object for the 4i+j element in the transform's extra matrix.The view parameter is optional.
        """
    def getNumberOfPivotPointKeys(self, view: Any) -> int:
        """self.getNumberOfPivotPointKeys(view) -> int
        Get the number of keys for the pivotPoint attribute. The view parameter is optional.
        """
    def getNumberOfRotationKeys(self, view: Any) -> int:
        """self.getNumberOfRotationKeys(view) -> int
        Get the number of keys for the rotation attribute. The view parameter is optional.
        """
    def getNumberOfScaleKeys(self, view: Any) -> int:
        """self.getNumberOfScaleKeys(view) -> int
        Get the number of keys for the scale attribute. The view parameter is optional.
        """
    def getNumberOfSkewXKeys(self, view: Any) -> int:
        """self.getNumberOfSkewXKeys(view) -> int
        Get the number of keys for the skewX attribute. The view parameter is optional.
        """
    def getNumberOfTransformKeys(self, view: Any) -> int:
        """self.getNumberOfTransformKeys(view) -> int
        Get the number of keys for all attributes of this transform. The view parameter is optional.
        """
    def getNumberOfTranslationKeys(self, view: Any) -> int:
        """self.getNumberOfTranslationKeys(view) -> int
        Get the number of keys for the translation attribute. The view parameter is optional.
        """
    def getPivotPointAnimCurve(self, index: Any, view: Any) -> AnimCurve:
        """self.getPivotPointAnimCurve(index, view) -> AnimCurve"""
    def getPivotPointKeyTime(self, index: Any, view: Any) -> float:
        """self.getPivotPointKeyTime(index, view) -> float
        Get the time for a specific key on the pivotPoint attribute. index is the index of the key. The view parameter is optional.
        """
    def getPivotPointKeyTimes(self, view: Any) -> Any:
        """self.getPivotPointKeyTimes(view) -> list of floats
        Get the times for all keys on the pivotPoint attribute. The view parameter is optional.
        """
    def getRotationAnimCurve(self, index: Any, view: Any) -> AnimCurve:
        """self.getRotationAnimCurve(index, view) -> AnimCurve"""
    def getRotationKeyTime(self, index: Any, view: Any) -> float:
        """self.getRotationKeyTime(index, view) -> float
        Get the time for a specific key on the rotation attribute. index is the index of the key. The view parameter is optional.
        """
    def getRotationKeyTimes(self, view: Any) -> Any:
        """self.getRotationKeyTimes(view) -> list of floats
        Get the times for all keys on the rotation attribute.The view parameter is optional.
        """
    def getScaleAnimCurve(self, index: Any, view: Any) -> AnimCurve:
        """self.getScaleAnimCurve(index, view) -> AnimCurve"""
    def getScaleKeyTime(self, index: Any, view: Any) -> float:
        """self.getScaleKeyTime(index, view) -> float
        Get the time for a specific key on the scale attribute. index is the index of the key. The view parameter is optional.
        """
    def getScaleKeyTimes(self, view: Any) -> Any:
        """self.getScaleKeyTimes(view) -> list of floats
        Get the times for all keys on the scale attribute. The view parameter is optional.
        """
    def getSkewXAnimCurve(self, index: Any, view: Any) -> AnimCurve:
        """self.getSkewXAnimCurve(index, view) -> AnimCurve"""
    def getSkewXKeyTime(self, index: Any, view: Any) -> float:
        """self.getSkewXKeyTime(index, view) -> float
        Get the time for a specific key on the skewX attribute. index is the index of the key. The view parameter is optional.
        """
    def getSkewXKeyTimes(self, view: Any) -> Any:
        """self.getSkewXKeyTimes(view) -> list of floats
        Get the times for all keys on the skewX attribute. The view parameter is optional.
        """
    def getTransformKeyTime(self, index: Any, view: Any) -> float:
        """self.getTransformKeyTime(index, view) -> float
        Get the time for a specific key. The view parameter is optional.
        """
    def getTransformKeyTimes(self, view: Any) -> Any:
        """self.getTransformKeyTimes(view) -> list of floats
        Get the times for all keys, across all attributes of this transform. The view parameter is optional.
        """
    def getTranslationAnimCurve(self, index: Any, view: Any) -> AnimCurve:
        """self.getTranslationAnimCurve(index, view) -> AnimCurve"""
    def getTranslationKeyTime(self, index: Any, view: Any) -> float:
        """self.getTranslationKeyTime(index, view) -> float
        Get the time for a specific key on the translation attribute. index is the index of the key. The view parameter is optional.
        """
    def getTranslationKeyTimes(self, view: Any) -> Any:
        """self.getTranslationKeyTimes(view) -> list of floats
        Get the times for all keys on the translation attribute. The view parameter is optional.
        """
    def isDefault(self) -> bool:
        """self.isDefault() -> bool
        Check whether this transform has been modified away from the default values.
        """
    name: Any
    def removePivotPointKey(self, time: Any, view: Any) -> None:
        """self.removePivotPointKey(time, view) -> None"""
    def removeRotationKey(self, time: Any, view: Any) -> None:
        """self.removeRotationKey(time, view) -> None"""
    def removeScaleKey(self, time: Any, view: Any) -> None:
        """self.removeScaleKey(time, view) -> None"""
    def removeSkewXKey(self, time: Any, view: Any) -> None:
        """self.removeSkewXKey(time, view) -> None"""
    def removeTransformKey(self, time: Any, view: Any) -> None:
        """self.removeTransformKey(time, view) -> None"""
    def removeTranslationKey(self, time: Any, view: Any) -> None:
        """self.removeTranslationKey(time, view) -> None"""
    def reset(self) -> None:
        """self.reset() -> None"""
    rotationOrder: Any
    def setExtraMatrixAnimCurve(self, i: Any, j: Any, animcurve: Any, view: Any) -> None:
        """self.setExtraMatrixAnimCurve(i, j, animcurve, view) -> None
        Sets the AnimCurve object for the '4i+j'-th element of the extra matrix.The view parameter is optional
        """
    def setIdentity(self, view: str = ...) -> None:
        """self.setIdentity(view='default') -> None"""
    def setPivotPointAnimCurve(self, index: Any, animCurve: Any, view: Any) -> None:
        """self.setPivotPointAnimCurve(index, animCurve, view) -> None
        Set the anim curve for the pivot point attribute of this transform. The index parameter should be 0 for the x values, 1 for the y values. The view parameter is optional.
        """
    def setRotationAnimCurve(self, index: Any, animCurve: Any, view: Any) -> None:
        """self.setRotationAnimCurve(index, animCurve, view) -> None
        Set the anim curve for the rotation attribute of this transform. The index parameter should be 0 for the x values, 1 for the y values. The view parameter is optional.
        """
    def setScaleAnimCurve(self, index: Any, animCurve: Any, view: Any) -> None:
        """self.setScaleAnimCurve(index, animCurve, view) -> None
        Set the anim curve for the scale attribute of this transform. The index parameter should be 0 for the x values, 1 for the y values. The view parameter is optional.
        """
    def setSkewXAnimCurve(self, index: Any, animCurve: Any, view: Any) -> None:
        """self.setSkewXAnimCurve(index, animCurve, view) -> None
        Set the anim curve for the skewX attribute of this transform. The index parameter should be 0 for the x values, 1 for the y values. The view parameter is optional.
        """
    def setTranslationAnimCurve(self, index: Any, animCurve: Any, view: Any) -> None:
        """self.setTranslationAnimCurve(index, animCurve, view) -> None
        Set the anim curve for the translation attribute of this transform. The index parameter should be 0 for the x values, 1 for the y values. The view parameter is optional.
        """
    transformOrder: Any
    def __new__(cls, *args: Any, **kwargs: Any) -> AnimCTransform: ...

class Flag:
    """A base class for objects which have a set of flags that can be set.

    You should never be instantiating this class directly - it only exists for other classes to inherit from.
    """
    def getFlag(self, flag: Any) -> bool:
        """getFlag(flag) -> bool
        Gets the specified flag. The parameter should be one of the FlagType constants.
        """
    def setFlag(self, flag: Any, value: Any) -> None:
        """setFlag(flag, value) -> None
        Set or clear the specified flag. The flag parameter should be one of the FlagType constants and value should be True or False.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> Flag: ...

@final
class AnimControlPoint(Flag):
    """An animated control point.

    These are used directly by Stroke objects to store the control point locations. Shape objects use a collection of up to 6 of them to represent each control point (see the ShapeControlPoint class for details).

    It is advisable to call changed() on the 'curves' knob after making modifications to curves. This forces the knob to re-cache the state of its curves.

    The 'view' argument to the object's methods can be omitted and the default view 'main' will be used.
    """
    def addControlPoint(self, controlPoint: Any) -> None:
        """self.addControlPoint(controlPoint) -> None"""
    def addKey(self, time: Any, controlPointOrDim: Any, view: Any) -> None:
        """self.addKey(time, controlPointOrDim, view) -> None"""
    def addPositionKey(self, time: Any, positionOrDim: Any, view: Any) -> None:
        """self.addPositionKey(time, positionOrDim, view) -> None
        Adds a new key to the control point's timeline. positionOrDim can either be a vector or a single scalar that specifies which component (xyzw) to add a key for.
        """
    dim: Any
    def evaluate(self, time: Any, view: Any) -> ControlPoint:
        """self.evaluate(time, view) -> ControlPoint
        Evaluates the animated control point's position at the specific time.
        """
    def getControlPointKeyTimes(self, view: Any) -> Any:
        """self.getControlPointKeyTimes(view) -> list of floats
        Get the list of times at which this control point has a key. The view parameter is optional.
        """
    def getPosition(self, time: Any, view: Any = ...) -> CVec3:
        """self.getPosition(time, view) -> CVec3
        Get the position of this control point at a particular time. The time parameter is a float specifying which time to calculate the position for; the view parameter is the optional view name.
        """
    def getPositionAnimCurve(self, index: Any, view: Any) -> AnimCurve:
        """self.getPositionAnimCurve(index, view) -> AnimCurve
        Returns the AnimCurve object containing the time line for the control point.
        """
    def getPositionKeyTime(self, index: Any, keyIndex: Any, view: Any) -> float:
        """self.getPositionKeyTime(index, keyIndex, view) -> float
        Get the time of a particular key for this control point. index is 0 for the X coordinate, 1 for Y or 2 for Z. keyIndex is the index of the relevant key. The view parameter is optional.
        """
    hash: Any
    name: Any
    def removeAllKeys(self, view: Any) -> None:
        """self.removeAllKeys(view) -> None"""
    def removeKey(self, time: Any, view: Any) -> None:
        """self.removeKey(time, view) -> None"""
    def removePositionKey(self, time: Any, view: Any) -> None:
        """self.removePositionKey(time, view) -> None"""
    def reset(self) -> None:
        """self.reset() -> None
        Resets the control point back to an initial empty state.
        """
    def setPosition(self, position: Any, view: Any) -> None:
        """self.setPosition(position, view) -> None
        Sets the control point's 'constant' position (the position used when there are no keys - see AnimCurve for further info). Calling this method when the control point has keys will have no effect.
        """
    def setPositionAnimCurve(self, index: Any, animCurve: Any, view: Any) -> None:
        """self.setPositionAnimCurve(index, animCurve, view) -> None
        Set the point's AnimCurve object (its time line).
        """
    def setPositionKey(self, time: Any, index: Any, value: Any, id: Any, view: Any) -> None:
        """self.setPositionKey(time, index, value, id, view) -> None
        Sets an individual dimension (index) of a key to a specific value. The key to modify is identified by hash (id). The method fails if there is no key at the specified time.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> AnimControlPoint: ...

class BaseCurve(Flag):
    """A base class for animated curves.

    You shouldn't be using this class directly, it only exists for other classes in this module to inherit from.
    """
    kDefaultCurveFlag: int
    kDefaultCurveTension: float
    kDefaultCurveType: int
    curveTension: Any
    curveType: Any
    name: Any
    def __new__(cls, *args: Any, **kwargs: Any) -> BaseCurve: ...

@final
class AnimCurve(BaseCurve):
    """An animated curve. The curve is described as a series of key values (instances of the AnimCurveKey class) which say what value it should have a particular time. For any time in between keys, the neighbouring key values are interpolated based on a curve type and interpolation settings specified at each key.

    Each curve can only represent a single floating point value over time.
    """
    kDefaultConstantValue: float
    @overload
    def addKey(self, time: Any, value: Any) -> None:
        """self.addKey(time, value) -> None
        self.addKey(keyObj) -> None
        Add a new key to this curve. You can pass in either a time and value pair (the value parameter is optional), or an AnimCurveKey object you've created yourself. In the former case, a new AnimCurveKey object will be created and added to the curve; in the latter case, the key you pass in will be added directly.
        """
    @overload
    def addKey(self, keyObj: Any) -> None:
        """self.addKey(time, value) -> None
        self.addKey(keyObj) -> None
        Add a new key to this curve. You can pass in either a time and value pair (the value parameter is optional), or an AnimCurveKey object you've created yourself. In the former case, a new AnimCurveKey object will be created and added to the curve; in the latter case, the key you pass in will be added directly.
        """
    constantValue: Any
    def evaluate(self, time: Any) -> float:
        """self.evaluate(time) -> float
        Calculate the value of the curve at a specific time, the pass that in to the expression for the curve. The return value is the result of the expression.
        """
    def evaluateY(self, time: Any) -> float:
        """self.evaluateY(time) -> float
        Calculates the value of the curve at a specific time.
        """
    expressionString: Any
    def getKey(self, index: Any) -> AnimCurveKey:
        """self.getKey(index) -> AnimCurveKey
        Returns one of the keys on this curve.
        """
    def getNumberOfKeys(self) -> int:
        """self.getNumberOfKeys() -> int
        Returns the number of keys along this curve.
        """
    def isDefault(self) -> bool:
        """self.isDefault() -> bool
        Check whether this curve has been modified away from its default values.
        """
    def removeAllKeys(self) -> None:
        """self.removeAllKeys() -> None
        Removes all keys from this curve.
        """
    def removeKey(self, timeOrHash: Any) -> None:
        """self.removeKey(timeOrHash) -> None
        Remove an existing key from this curve. The key is identified by either the time it occurs at, or its hash (as returned by the key's getHash() method.
        """
    def reset(self) -> None:
        """self.reset() -> None
        Reset this object to its default values.
        """
    useExpression: Any
    def __new__(cls, *args: Any, **kwargs: Any) -> AnimCurve: ...

@final
class AnimCurveKey(Flag):
    """A key value in a parametric curve represented as a value at a particular time."""
    kDefaultAnimCurveKeyInterpolation: int
    kDefaultAnimCurveKeyTime: float
    kDefaultAnimCurveKeyValue: float
    interpolationType: Any
    la: Any
    lslope: Any
    ra: Any
    def reset(self) -> None:
        """self.reset() -> None
        Reset this key to its default values.
        """
    rslope: Any
    time: Any
    value: Any
    def __new__(cls, *args: Any, **kwargs: Any) -> AnimCurveKey: ...

@final
class AnimCurveViews:
    kDefaultViewName: str
    def getNumberOfViews(self) -> int:
        """self.getNumberOfViews() -> int
        Get the number of views.
        """
    def getViewIndex(self, name: Any) -> int:
        """self.getViewIndex(name) -> int
        Get the index of a view when you know its name.
        """
    def getViewName(self, index: Any) -> str:
        """self.getViewName(index) -> str
        Get the name of a particular view when you know its index.
        """
    def getViewNames(self) -> Any:
        """self.getViewNames() -> list of strings
        Get the list of all view names.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> AnimCurveViews: ...

@final
class CMatrix4:
    """A 4x4 matrix with methods for affine transformations."""
    def __add__(self, value: Any, /) -> Any:
        """Return self+value."""
    def __delitem__(self, key: Any, /) -> None:
        """Delete self[key]."""
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __iadd__(self, value: Any, /) -> Any:
        """Return self+=value."""
    def __imul__(self, value: Any, /) -> Any:
        """Return self*=value."""
    def __isub__(self, value: Any, /) -> Any:
        """Return self-=value."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __mul__(self, value: Any, /) -> Any:
        """Return self*value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __radd__(self, value: Any, /) -> Any:
        """Return value+self."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __rmul__(self, value: Any, /) -> Any:
        """Return value*self."""
    def __rsub__(self, value: Any, /) -> Any:
        """Return value-self."""
    def __setitem__(self, key: Any, value: Any, /) -> None:
        """Set self[key] to value."""
    def __sub__(self, value: Any, /) -> Any:
        """Return self-value."""
    def makeIdentity(self) -> None:
        """self.makeIdentity() -> None
        Set this matrix to be the identity matrix.
        """
    def rotateX(self, angleInRadians: Any) -> None:
        """self.rotateX(angleInRadians) -> None
        Post-multiply this matrix by a rotation around the X axis.
        """
    def rotateY(self, angleInRadians: Any) -> None:
        """self.rotateY(angleInRadians) -> None
        Post-multiply this matrix by a rotation around the Y axis.
        """
    def rotateZ(self, *args: Any, **kwargs: Any) -> Any:
        """self.rotateY(angleInRadians) -> None
        Post-multiply this matrix by a rotation around the Z axis.
        """
    def scale(self, x: Any, y: Any, z: Any) -> None:
        """self.scale(x, y, z) -> None
        Post-multiply this matrix by a scale transformation. The y and z parameters
        may be left out; if so the scale is uniform along all three axes.
        """
    def skew(self, x: Any, y: Any, z: Any) -> None:
        """self.skew(x, y, z) -> None
        Post-multiply this matrix with a skew transformation. The y and z parameters
        may be left out; if so, the skew is in the X direction only.
        """
    def translate(self, x: Any, y: Any, z: Any) -> None:
        """self.translate(x, y, z) -> None
        Post-multiply this matrix by a translation matrix.
        """
    def translation(self, x: Any, y: Any, z: Any) -> None:
        """self.translation(x, y, z) -> None
        Set this matrix to be a translation matrix, replacing any existing values.

        This is different from other methods in this class as it replaces, rather than multiplying by, the existing values in the matrix.
        """
    def transpose(self) -> None:
        """self.transpose() -> None
        Transpose the matrix in-place.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> CMatrix4: ...

@final
class CTransform:
    """A transform at a single point in time.

    This is the result of evaluating an AnimTransform for a particular time.
    """
    def getInverseMatrix(self) -> CMatrix4:
        """self.getInverseMatrix() -> CMatrix4
        Gets the inverse transform matrix, which can be used for undoing the effects of this transform.
        """
    def getMatrix(self) -> CMatrix4:
        """self.getMatrix() -> CMatrix4
        Get the matrix which represents the combination of the translation, scale, rotation, skew and pivotPoint settings for this transform.
        """
    def getTransposeMatrix(self) -> CMatrix4:
        """self.getTransposeMatrix() -> CMatrix4
        Returns a transposed copy of the matrix representing this transform.
        """
    def isDefault(self) -> bool:
        """self.isDefault() -> bool
        Returns True if this transform matches the default settings, False if not.
        """
    name: Any
    pivotPoint: Any
    def reset(self) -> None:
        """self.reset() -> None
        Return this transform to its default settings.
        """
    rotation: Any
    rotationOrder: Any
    scale: Any
    def setIdentity(self) -> None:
        """self.setIdentity() -> None
        Set this transform to the identity transform (the transform which doesn't change the object at all).
        """
    skew: Any
    transformOrder: Any
    translation: Any
    def __new__(cls, *args: Any, **kwargs: Any) -> CTransform: ...

@final
class CVec2:
    """A 2-component vector."""
    def __add__(self, value: Any, /) -> Any:
        """Return self+value."""
    def __delitem__(self, key: Any, /) -> None:
        """Delete self[key]."""
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __iadd__(self, value: Any, /) -> Any:
        """Return self+=value."""
    def __isub__(self, value: Any, /) -> Any:
        """Return self-=value."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __mul__(self, value: Any, /) -> Any:
        """Return self*value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __neg__(self, /) -> Any:
        """-self"""
    def __radd__(self, value: Any, /) -> Any:
        """Return value+self."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __rmul__(self, value: Any, /) -> Any:
        """Return value*self."""
    def __rsub__(self, value: Any, /) -> Any:
        """Return value-self."""
    def __setitem__(self, key: Any, value: Any, /) -> None:
        """Set self[key] to value."""
    def __sub__(self, value: Any, /) -> Any:
        """Return self-value."""
    x: Any
    y: Any
    def __new__(cls, *args: Any, **kwargs: Any) -> CVec2: ...

@final
class CVec3:
    """A 3-component vector."""
    def __add__(self, value: Any, /) -> Any:
        """Return self+value."""
    def __delitem__(self, key: Any, /) -> None:
        """Delete self[key]."""
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __iadd__(self, value: Any, /) -> Any:
        """Return self+=value."""
    def __isub__(self, value: Any, /) -> Any:
        """Return self-=value."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __mul__(self, value: Any, /) -> Any:
        """Return self*value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __neg__(self, /) -> Any:
        """-self"""
    def __radd__(self, value: Any, /) -> Any:
        """Return value+self."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __rmul__(self, value: Any, /) -> Any:
        """Return value*self."""
    def __rsub__(self, value: Any, /) -> Any:
        """Return value-self."""
    def __setitem__(self, key: Any, value: Any, /) -> None:
        """Set self[key] to value."""
    def __sub__(self, value: Any, /) -> Any:
        """Return self-value."""
    x: Any
    y: Any
    z: Any
    def __new__(cls, *args: Any, **kwargs: Any) -> CVec3: ...

@final
class CVec4:
    """A 4-component vector."""
    def __add__(self, value: Any, /) -> Any:
        """Return self+value."""
    def __delitem__(self, key: Any, /) -> None:
        """Delete self[key]."""
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __iadd__(self, value: Any, /) -> Any:
        """Return self+=value."""
    def __isub__(self, value: Any, /) -> Any:
        """Return self-=value."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __mul__(self, value: Any, /) -> Any:
        """Return self*value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __neg__(self, /) -> Any:
        """-self"""
    def __radd__(self, value: Any, /) -> Any:
        """Return value+self."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def __rmul__(self, value: Any, /) -> Any:
        """Return value*self."""
    def __rsub__(self, value: Any, /) -> Any:
        """Return value-self."""
    def __setitem__(self, key: Any, value: Any, /) -> None:
        """Set self[key] to value."""
    def __sub__(self, value: Any, /) -> Any:
        """Return self-value."""
    w: Any
    x: Any
    y: Any
    z: Any
    def __new__(cls, *args: Any, **kwargs: Any) -> CVec4: ...

@final
class ControlPoint:
    """A control point at a particular point in time.

    This is the result of evaluating an AnimControlPoint for a particular time value.
    """
    dim: Any
    hash: Any
    name: Any
    position: Any
    def reset(self) -> Any:
        """self.reset() -> NoneReset this control point to its default values."""
    def __new__(cls, *args: Any, **kwargs: Any) -> ControlPoint: ...

@final
class CubicCurve:
    """A baked out curve for a specific frame and view.

    Use the getPoint function to get positions along the curve.

    Note that some curves, such as the feather curve for a roto shape, are stored as offsets relative to another curve rather than absolute positions.
    """
    def getPoint(self, t: Any) -> CVec4:
        """self.getPoint(t) -> CVec4
        @param t: The parameter value to evaluate the curve with. 0.0 is the start of the curve and 1.0 is the end. A value outside this range will throw a ValueError.
        @return: A CVec4 containing the evalution result. If the curve has less than 4 dimension, the extra dimensions will be filled with default values.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> CubicCurve: ...

class CurveKnob(_nuke.Knob):
    """The knob which holds the tree of paint elements (Layers, Shapes and Strokes).

    Most operations are performed on the tree itself, or its elements, rather than through the knob. You can get the root of the tree through the knob's rootLayer property, or you can get straight to a specific element using the toElement() method.

    A common usage scenario is as follows:

    >>> knob = nuke.toNode('RotoPaint1')['curves']
    >>> root = knob.rootLayer
    >>> # perform operations on the root layer.

    Creating any new shapes, strokes or layers will require you to pass in a reference to the knob, so it's worth storing the reference in a variable.
    """
    def changed(self) -> None:
        """self.changed() -> None
        Call this after performing updates on the tree, to tell it that it's been updated. For many operations this is called automatically, but you can call it manually for those cases where it isn't.
        """
    curveWidget: Any
    def getSelected(self) -> list:
        """self.getSelected() -> [selectedObjects]
        Returns list of all selected items in a curve knob
        As an example, say you have a Bezier curve selected,the following will return 'Bezier1'
        >>> curveKnob = nuke.toNode('RotoPaint1)['curves']
        >>> selected = curveKnob.getSelected()
        >>> selected[0].name
        """
    rootLayer: Element
    def toElement(self, path: str) -> Element:
        """self.toElement(path) -> Element
        Takes a path which identifies a particular element in the curve tree and returns the corresponding Layer, Stroke or Shape object. 
        The path is a slash separated string and is always resolved relative to the root layer. So if, for example, you have a RotoPaint node with a layer called 'Layer1' which contains a shape called 'Shape1', the path to the shape would be 'Layer1/Shape1'.
        >>> knob = nuke.toNode('RotoPaint1)['curves']
        >>> shape = knob.toElement('Layer1/Shape1')
        >>> shape.name
        'Shape1'
        """

@final
class CurveType:
    """Constants for use in parameters which require a curve type."""
    eBSplineCurveType: int
    eBezierCurveType: int
    eCardinalCurveType: int
    eCatmullRomCurveType: int
    eHermiteCurveType: int
    eNurbsCurveType: int
    eUndefineCurveType: int

class Element:
    """The base class for the different types of elements you can create in the RotoPaint node."""
    def clone(self) -> Any:
        """self.clone() -> elementCreate clone of element"""
    def getVisible(self, time: Any) -> bool:
        """self.getVisible(time) -> bool
        Get the value of the visible attribute at a particular time.
        """
    locked: Any
    name: Any
    def serialise(self) -> str:
        """self.serialise() -> string
        Returns a string representation of the given element.
        """
    def setVisible(self, time: Any, value: Any) -> None:
        """self.setVisible(time, value) -> None
        Set the value of the visible attribute at a particular time. value must be a bool.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> Element: ...

@final
class ExtrapolationType:
    """Constants for use in parameters which require an extrapolation type."""
    eConstantExtrapolationType: int
    eCycleExtrapolationType: int
    eLinearExtrapolationType: int
    eUndefineExtrapolationType: int

@final
class FlagType:
    """Constants for use in parameters which require a flag type."""
    eActiveFlag: int
    eBreakFlag: int
    eKeySelectedFlag: int
    eLeftTangentSelectedFlag: int
    eLockedFlag: int
    eMaxFlag: int
    eNukeAnimCurveEvalFlag: int
    eOpenFlag: int
    ePressureInZFlag: int
    eRelativeTangentFlag: int
    eRenderableFlag: int
    eRightTangentSelectedFlag: int
    eSelectedFlag: int
    eTangentLengthLockFlag: int
    eUndefineFlag: int
    eVisibleFlag: int

@final
class InterpolationType:
    """Constants for use in parameters which require an interpolation type."""
    eCubicInterpolationType: int
    eLinearInterpolationType: int
    eStepInterpolationType: int
    eUndefineInterpolationType: int

@final
class Layer(Element):
    """A layer, used to group other elements in the paint tree.

    Layers can contain shapes, strokes and other layers. They can be transformed, which has the effect of transforming all contained objects by the same amount (in addition to any individual transforms on the contained objects).

    Layers are represented as a sequence of Element objects. You can find out how many items the layer contains using the len() function, as for any python sequence. Likewise you can access the contained elements using python's array-style syntax (e.g. layer[0] will return the first element inside the layer, layer[-1] will return the last element, etc.).
    """
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def append(self, element: Any) -> None:
        """self.append(element) -> None
        Add a new element inside this layer. The element must be an instance of either the Shape, Stroke or Layer classes. Note that an element cannot be in more than one place in the tree, so if you try to add an element that is already in the tree somewhere else, it'll be removed from its old location first.
        """
    def getAttributes(self) -> AnimAttributes:
        """self.getAttributes() -> AnimAttributes
        Gets the collection of attributes for this stroke.
        """
    def getFlag(self, flag: Any) -> bool:
        """self.getFlag(flag) -> bool
        Check whether a particular flag is set or not. The flag parameter should be one of the constants from the FlagType class. The return value will be True if the flag is set, False if it isn't.
        """
    def getTransform(self) -> AnimCTransform:
        """self.getTransform() -> AnimCTransform
        Gets the transform for this shape.
        """
    def insert(self, index: Any, element: Any) -> None:
        """self.insert(index, element) -> None
        Insert a new element inside this layer at the given index. The element must be an instance of either the Shape, Stroke or Layer classes. Note that an element cannot be in more than one place in the tree, so if you try to add an element that is already in the tree somewhere else, it'll be removed from its old location first.
        """
    def remove(self, index: Any) -> None:
        """self.remove(index) -> None
        Remove the element at the given index from this layer. If the index is out of bounds, an IndexError will be raised.
        """
    def removeAll(self) -> None:
        """self.removeAll() -> None
        Remove all elements from this layer.
        """
    def setFlag(self, flag: Any, value: Any) -> None:
        """self.setFlag(flag, value) -> None
        Set a particular flag. The flag parameter specifies which flag to set and should be one of the constants from the FlagType class. The value parameter is a boolean value; True will set the flag, False will clear it.
        """
    def setTransform(self, transform: Any) -> None:
        """self.setTransform(transform) -> None
        Replace the existing transform for this shape with a new one. The transform parameter must be an instance of the AnimTransform class.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> Layer: ...

@final
class RotationOrder:
    """Constants for use in parameters which require a rotation order."""
    eUndefineRotationOrder: int
    eXYZRotationOrder: int
    eXZYRotationOrder: int
    eYXZRotationOrder: int
    eYZXRotationOrder: int
    eZXYRotationOrder: int
    eZYXRotationOrder: int

@final
class Shape(Element):
    """A Roto or SplineWarp shape, which may be animated.

    Shapes are represented as a sequence of ShapeControlPoint objects, which group together a 'center' control point along with tangent locations and feather offsets. Python's built-in len() function can be used to get the number of shape control points; and array-style access can be used to get individual shape control points (e.g. shape[0] returns the first shape control point, shape[-1] returns the last shape control point, etc.).
    You can create a new shape as follows:

    >>>import _curveknob
    >>>rotoNode = nuke.toNode('RotoPaint1')
    >>>curveKnob = rotoNode['curves']
    >>>emptyShape = _curveknob.Shape( curveKnob )
    >>>twoPointShape = _curveknob.Shape( curveKnob, *((0,0), (10,10)) )
    >>> # perform operations on the shape(s).

    NOTE: this object was designed to work for Roto shapes, which have feather
          curves. Please report any problems with this type to
          support@thefoundry.co.uk
    """
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def append(self, shapeControlPoint: Any) -> None:
        """self.append(shapeControlPoint) -> None
        Add a new control point to the shape. The shapeControlPoint parameter must be either an instance of the ShapeControlPoint class, or something we can convert to a ShapeControlPoint. This includes a sequence of 2, 3 or 4 floats; a CVec2, CVec3 or CVec4 object; or an AnimControlPoint object.
        """
    def evaluate(self, curveNum: Any, time: Any, viewName: str = ...) -> CubicCurve:
        """self.evaluate(curveNum, time, viewName='default') -> CubicCurve
        Bake out a curve for the outline of this shape at the specified time.

        Note that the feather curve is represented as an offset from the main curve. If you want to get the screen position of a point along the feather curve, you'll need to add it to the corresponding position on the main curve. For example:
          >>> frameNum = 10.0
          >>> t = 0.5
          >>> rotoknob = nuke.toNode('RotoPaint1')['curves']
          >>> shape = rotoknob.toElement('Bezier1')
          >>> mainCurve = shape.evaluate(0, frameNum)
          >>> featherCurve = shape.evaluate(1, frameNum)
          >>> pointOnMainCurve = mainCurve.getPoint(t)
          >>> featherOffset = featherCurve.getPoint(t)
          >>> pointOnFeatherCurve = pointOnMainCurve + featherOffset

        @param curveNum: 0 for the main curve, 1 for the feather curve.
        @param time: The (floating point) frame number to bake the curve from.
        @param viewName: Optional parameter specifying which view to bake the curve from. If omitted, the default view will be used.
        """
    def getAttributes(self) -> AnimAttributes:
        """self.getAttributes() -> AnimAttributes
        Gets the collection of attributes for this shape.
        """
    def getFlag(self, flag: Any) -> bool:
        """self.getFlag(flag) -> bool
        Check whether a particular flag is set or not. The flag parameter should be one of the constants from the FlagType class. The return value will be True if the flag is set, False if it isn't.
        """
    def getTransform(self) -> AnimCTransform:
        """self.getTransform() -> AnimCTransform
        Gets the transform for this shape.
        """
    def insert(self, index: Any, shapeControlPoint: Any) -> None:
        """self.insert(index, shapeControlPoint) -> None
        Insert a new control point in the shape before the given index. The shapeControlPoint parameter must be either an instance of the ShapeControlPoint class, or something we can convert to a ShapeControlPoint. This includes a sequence of 2, 3 or 4 floats; a CVec2, CVec3 or CVec4 object; or an AnimControlPoint object.
        """
    def remove(self, index: Any) -> None:
        """self.remove(index) -> None
        Remove the control point at the given index. This removes any associated tangent and feather point data as well. If the index is out of bounds, an IndexError will be raised.
        """
    def setFlag(self, flag: Any, value: Any) -> None:
        """self.setFlag(flag, value) -> None
        Set a particular flag. The flag parameter specifies which flag to set and should be one of the constants from the FlagType class. The value parameter is a boolean value; True will set the flag, False will clear it.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> Shape: ...

@final
class ShapeControlPoint:
    """A control point in a roto shape.

    The control point groups together a 'center' location, along with tangents and feather offsets.
    """
    center: Any
    featherCenter: Any
    featherLeftTangent: Any
    featherRightTangent: Any
    leftTangent: Any
    rightTangent: Any
    def __new__(cls, *args: Any, **kwargs: Any) -> ShapeControlPoint: ...

@final
class Stroke(Element):
    """A paint stroke, which may be animated.

    A paint stroke is represented as a sequence of AnimControlPoint objects. You can find out how many control points there are in the stroke using python's built-in len() function; and you can access individual control points using the array-style syntax (e.g. stroke[0] returns the first control point, stroke[-1] returns the last control point, etc.).
    """
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def append(self, controlPoint: Any) -> None:
        """self.append(controlPoint) -> None
        Add a new control point to the stroke. The controlPoint parameter must be either an instance of the AnimControlPoint class, or something we can convert to an AnimControlPoint. This includes a sequence of 2, 3 or 4 floats; or a CVec2, CVec3 or CVec4 object.
        """
    def evaluate(self, time: Any, viewName: str = ...) -> CubicCurve:
        """self.evaluate(time, viewName='default') -> CubicCurve
        Bake out a curve for the path of this stroke at the specified time.
        @param time: The (floating point) frame number to bake the curve from.
        @param viewName: Optional parameter specifying which view to bake the curve from. If omitted, the default view will be used.
        """
    def getAttributes(self) -> AnimAttributes:
        """self.getAttributes() -> AnimAttributes
        Gets the collection of attributes for this stroke.
        """
    def getFlag(self, flag: Any) -> bool:
        """self.getFlag(flag) -> bool
        Check whether a particular flag is set or not. The flag parameter should be one of the constants from the FlagType class. The return value will be True if the flag is set, False if it isn't.
        """
    def getTransform(self) -> AnimCTransform:
        """self.getTransform() -> AnimCTransform
        Gets the transform for this shape.
        """
    def insert(self, index: Any, controlPoint: Any) -> None:
        """self.insert(index, controlPoint) -> None
        Insert a new control point in the stroke before the given index. The controlPoint parameter must be either an instance of the AnimControlPoint class, or something we can convert to an AnimControlPoint. This includes a sequence of 2, 3 or 4 floats; or a CVec2, CVec3 or CVec4 object.
        """
    def remove(self, index: Any) -> None:
        """self.remove(index) -> None
        Remove the control point at the given index. If the index is out of bounds, an IndexError will be raised.
        """
    def setFlag(self, flag: Any, value: Any) -> None:
        """self.setFlag(flag, value) -> None
        Set a particular flag. The flag parameter specifies which flag to set and should be one of the constants from the FlagType class. The value parameter is a boolean value; True will set the flag, False will clear it.
        """
    def __new__(cls, *args: Any, **kwargs: Any) -> Stroke: ...

@final
class TransformOrder:
    """Constants for use in parameters which require a transform order."""
    eRSTTransformOrder: int
    eRTSTransformOrder: int
    eSRTTransformOrder: int
    eSTRTransformOrder: int
    eTRSTransformOrder: int
    eTSRTransformOrder: int
    eUndefineTransformOrder: int
