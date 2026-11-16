# Type stubs for nuke 17.1v2. Generated; do not edit.

from typing import Any
from typing import final
from typing import overload
from typing_extensions import Self
import PySide6.QtCore as _PySide6_QtCore
import PySide6.QtGui as _PySide6_QtGui
import builtins as _builtins
import enum as _enum
import hiero.core.FnExportRegistry as _hiero_core_FnExportRegistry
import hiero.core.find_items as _hiero_core_find_items
import hiero.core.nuke.Script as _hiero_core_nuke_Script
import nuke as _nuke
import types as _types
from . import FnAddClipToSequence as FnAddClipToSequence
from . import FnCompSourceInfo as FnCompSourceInfo
from . import FnEffectHelpers as FnEffectHelpers
from . import FnExportRegistry as FnExportRegistry
from . import FnExportStructure as FnExportStructure
from . import FnExporterBase as FnExporterBase
from . import FnFloatRange as FnFloatRange
from . import FnNukeHelpers as FnNukeHelpers
from . import FnNukeHelpersV2 as FnNukeHelpersV2
from . import FnOnProjectLoad as FnOnProjectLoad
from . import FnOtioMarkerColorMapping as FnOtioMarkerColorMapping
from . import FnPostEffectCreation as FnPostEffectCreation
from . import FnProcessor as FnProcessor
from . import FnResolveTable as FnResolveTable
from . import FnSequenceFormatHandler as FnSequenceFormatHandler
from . import FnVersionScanner as FnVersionScanner
from . import deprecated as deprecated
from . import events as events
from . import find_items as find_items
from . import find_plugins as find_plugins
from . import find_startup_projects as find_startup_projects
from . import localisation_helpers as localisation_helpers
from . import log as log
from . import nuke as nuke
from . import util as util
from hiero.FnRedirect import getPluginPath as getPluginPath
from hiero.FnRedirect import pluginPath as pluginPath
from hiero.core.FnEffectHelpers import effectInputSourceCoods as effectInputSourceCoods
from hiero.core.FnEffectHelpers import executeEffectNode as executeEffectNode
from hiero.core.FnExportRegistry import TaskRegistry as TaskRegistry
from hiero.core.FnExportStructure import ExportStructure2 as ExportStructure2
from hiero.core.FnExportStructure import ExportStructureElement as ExportStructureElement
from hiero.core.FnExporterBase import FolderTask as FolderTask
from hiero.core.FnExporterBase import FolderTaskPreset as FolderTaskPreset
from hiero.core.FnExporterBase import RenderTaskPreset as RenderTaskPreset
from hiero.core.FnExporterBase import TaskBase as TaskBase
from hiero.core.FnExporterBase import TaskData as TaskData
from hiero.core.FnExporterBase import TaskGroup as TaskGroup
from hiero.core.FnExporterBase import TaskPreset as TaskPreset
from hiero.core.FnExporterBase import TaskPresetBase as TaskPresetBase
from hiero.core.FnPostEffectCreation import afterEffectCreated as afterEffectCreated
from hiero.core.FnPostEffectCreation import overrideKnobDefaults as overrideKnobDefaults
from hiero.core.FnProcessor import ProcessorBase as ProcessorBase
from hiero.core.FnProcessor import ProcessorPreset as ProcessorPreset
from hiero.core.FnResolveTable import ResolveTable as ResolveTable
from hiero.core.FnVersionScanner import VersionScanner as VersionScanner
from hiero.core.find_items import findItemByGuid as findItemByGuid
from hiero.core.find_items import findItemsByGuid as findItemsByGuid
from hiero.core.find_items import findItemsInBin as findItemsInBin
from hiero.core.find_items import findItemsInProject as findItemsInProject
from hiero.core.find_items import findProjectTags as findProjectTags
from hiero.core.localisation_helpers import setLocalisationForAllVersionsInProject as setLocalisationForAllVersionsInProject
from hiero.core.localisation_helpers import setLocalisationPolicyOnBin as setLocalisationPolicyOnBin
from hiero.core.localisation_helpers import setLocalisationPolicyOnClip as setLocalisationPolicyOnClip
from hiero.core.localisation_helpers import setLocalisationPolicyOnSequence as setLocalisationPolicyOnSequence
from hiero.core.localisation_helpers import setLocalisationPolicyOnTrack as setLocalisationPolicyOnTrack
from hiero.core.localisation_helpers import setLocalisationPolicyOnTrackItem as setLocalisationPolicyOnTrackItem
from hiero.core.nuke.Script import getBundledNukePath as getBundledNukePath
from hiero.core.nuke.Script import getBundledPythonPath as getBundledPythonPath

AnnotationCommentKeys: _types.SimpleNamespace
GUI: bool
NonZeroStartFrameMovieFileExtensions: list
QuickTimeExtensions: list
VideoFileExtensions: list
env: dict
kMaxTime: int
kMaxTimeDuration: int
kNoTimeSet: int
rawArgs: list
taskRegistry: _hiero_core_FnExportRegistry.TaskRegistry

class AnnotationElement:
    """Base class for types of elements that may be added to an Annotation.
    This class should not be used directly and AnnotationElement objects should not be created.
    """
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def color(self) -> Any:
        """self.color() -> returns a tuple containing the color for this annotation element in the form (red, green, blue, alpha),
        with the components represented as floating point values in the range [0, 1].

        @return: tuple of (red, green, blue, alpha)
        """
    def deserialize(self, data: Any) -> None:
        """self.deserialize(data) -> None

        Deserializes the paint object from a string.

        @param data: The string data to deserialize from.
        """
    def isNull(self, *args: Any, **kwargs: Any) -> Any: ...
    def serialize(self) -> str:
        """self.serialize() -> string

        Serializes the paint object to a string.

        @return: A string representation of the paint object.
        """
    def setColor(self) -> None:
        """self.setColor() -> None

        Sets the color and alpha of the element.
        Each component must be a floating point value in the range [0, 1].

        @param red: The new red component.
        @param green: The new green component.
        @param blue: The new blue component.
        @param alpha: The new alpha component.
        """
    def toString(self) -> str:
        """self.toString() -> string

        Returns a description of the object. Equivalent to str(object).

        @return: A string describing the object.
        """

class AnnotationStroke(AnnotationElement):
    """A class, derived from AnnotationElement, storing a set of 2d points to represent a single stroke
    within an annotation.
    """
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def brushSettings(self) -> Any:
        """Deprecated. Use paintProperties() instead."""
    def isNull(self, *args: Any, **kwargs: Any) -> Any: ...
    def paintProperties(self, *args: Any, **kwargs: Any) -> PaintProperties:
        """self.paintProperties -> Get a copy of the paint properties for this stroke.

        @return: PaintProperties
        """
    def points(self, *args: Any, **kwargs: Any) -> Any:
        """self.points -> Returns a list of AnnotationStrokePoints representing the 2D line points.

        @return: list of AnnotationStrokePoint objects
        """
    def setBrushSettings(self, settings: Any) -> Any:
        """Deprecated. Use setPaintProperties() instead."""
    def setPaintProperties(self, *args: Any, **kwargs: Any) -> Any:
        """self.setPaintProperties -> Set the paint properties for this stroke.

        To change the properties, modify the object returned from self.paintProperties() and call this method. For example:

            properties = stroke.paintProperties()
            properties.setBlendMode(PaintBlendMode.Plus)
            stroke.setPaintProperties(properties)
        """
    def setPoints(self, *args: Any, **kwargs: Any) -> Any:
        """self.setPoints -> Sets the points that make up this stroke, replacing any points the stroke already had.
        The points must be specified as a list of AnnotationStrokePoint objects.
        """
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """

class AnimatedAnnotationStroke(AnnotationStroke):
    """A class representing an animated paint stroke (vanishing brush)."""
    class AnimationState(_enum.IntEnum):
        Animating: AnimatedAnnotationStroke.AnimationState
        Completed: AnimatedAnnotationStroke.AnimationState
        NotStarted: AnimatedAnnotationStroke.AnimationState
        PendingStart: AnimatedAnnotationStroke.AnimationState
        def __new__(cls, value: Any) -> Self: ...
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def animationState(self) -> Any:
        """self.animationState() -> Returns the animation state.
        Returns AnimationState enum: NotStarted, PendingStart, Animating, or Completed
        """
    def easingCurve(self) -> Any:
        """self.easingCurve() -> Returns the easing curve type for the animation."""
    def initialDelay(self) -> Any:
        """self.initialDelay() -> Returns the initial delay before the animation starts, in seconds."""
    def markReadyToAnimate(self) -> Any:
        """self.markReadyToAnimate() -> Marks the stroke as ready to start animating (fading out)."""
    def setEasingCurve(self) -> Any:
        """self.setEasingCurve() -> Sets the easing curve type for the animation."""
    def setInitialDelay(self) -> Any:
        """self.setInitialDelay() -> Sets the initial delay before the animation starts, in seconds."""

class Annotation:
    """Class for objects that can hold multiple stroke and/or text elements to provide annotation functionality. Annotations should be created by calling SequenceBase.addAnnotation(). Strokes and/or text can be added to an annotation by creating AnnotationStroke and/or AnnotationText objects and using addElement()."""
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def addElement(self) -> Any:
        """self.addElement() -> Adds the specified AnnotationElement, which should be an instance of an AnnotationElement sub-class, i.e. either
        an AnnotationStroke or an AnnotationText object.

        @return: If there was no error, returns the added element.
        """
    def addElementFromData(self, data: Any) -> Any:
        """self.addElementFromData(data) -> Deserializes an AnnotationElement from its XML data and adds it to the annotation.

        The element type is determined from the serialized data.

        @param data: A string produced by AnnotationElement.serialize().
        @return: The added element, or null if the data could not be deserialized.
        """
    def addNote(self, text: Any) -> AnnotationComment:
        """self.addNote(text) -> add a note to the annotation

        @param text: text to set on the created note

        @return: AnnotationComment
        """
    def comment(self) -> AnnotationComment:
        """self.comment() -> get the comment for this annotation

        @return: AnnotationComment
        """
    def deserialize(self) -> Any:
        """self.deserialize() -> restore the annotation from XML data"""
    def elements(self) -> Any:
        """self.elements() -> returns a tuple with all of the elements contained in this annotation.

        @return: tuple of hiero.core.Element sub-class objects
        """
    def guid(self, *args: Any, **kwargs: Any) -> Any: ...
    def isLocked(self) -> bool:
        """self.isLocked() -> Check if the annotation is locked (read-only)

        @return: bool
        """
    def isNull(self, *args: Any, **kwargs: Any) -> Any: ...
    def notes(self) -> Any:
        """self.notes() -> get the list of notes added to the annotation

        @return: List[AnnotationComment]
        """
    def parentSequence(self) -> Sequence | Clip:
        """self.parentSequence() -> returns the sequence the annotation belongs to.

        @return: hiero.core.Sequence | hiero.core.Clip
        """
    def removeElement(self, element: Any) -> Any:
        """self.removeElement(element) -> Removes the specified AnnotationElement from the annotation.

        @param element: The element to remove.
        """
    def removeNote(self) -> Any:
        """self.removeNote() -> remove a note from the annotation

        @param note: the note to remove
        """
    def serialize(self) -> Any:
        """self.serialize() -> serialize the annotation object to XML"""
    def setLocked(self, locked: Any) -> Any:
        """self.setLocked(locked) -> Set the annotation's locked state

        @param locked: True to lock the annotation, False to unlock it
        """
    def setTimeRange(self, *args: Any, **kwargs: Any) -> Any:
        """self.timeRange() -> set the annotation's time range.

        @param start: start time
        @param: end : end time@raise RuntimeError: 
        """
    def timeRange(self) -> Any:
        """self.timeRange() -> get the annotation's time range, if set.

        @return: (Time, Time)
        @raise RuntimeError: if the annotation has no time range set
        """
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """

class AnnotationArrow(AnnotationElement):
    """A class, derived from AnnotationElement, representing an arrow shape element.

    An arrow is defined by a start point and an end point.

    Example usage:

        arrow = AnnotationArrow(0, 0, 100, 50)  # start (0,0), end (100,50)
        arrow = AnnotationArrow(QPointF(0, 0), QPointF(100, 50))  # using QPointF
        props = arrow.paintProperties()
        props.setColor(QColor(255, 0, 0))
        arrow.setPaintProperties(props)
        annotation.addElement(arrow)
    """
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def copy(self) -> AnnotationArrow:
        """self.copy() -> Return a deep copy of this arrow shape.

        @return: AnnotationArrow
        """
    def endPoint(self) -> Any:
        """self.endPoint() -> Returns the end point (arrowhead) of the arrow as a QPointF.

        @return: QPointF
        """
    def isNull(self, *args: Any, **kwargs: Any) -> Any: ...
    def paintProperties(self) -> PaintProperties:
        """self.paintProperties() -> Get a copy of the paint properties for AnnotationArrow.

        @return: PaintProperties
        """
    @overload
    def setEndPoint(self, x: Any, y: Any) -> Any:
        """self.setEndPoint(x, y) -> Sets the end point (arrowhead) of the arrow.
        self.setEndPoint(point) -> Sets the end point (arrowhead) of the arrow.

        @param x: float x-coordinate
        @param y: float y-coordinate
        @param point: QPointF end point
        """
    @overload
    def setEndPoint(self, point: Any) -> Any:
        """self.setEndPoint(x, y) -> Sets the end point (arrowhead) of the arrow.
        self.setEndPoint(point) -> Sets the end point (arrowhead) of the arrow.

        @param x: float x-coordinate
        @param y: float y-coordinate
        @param point: QPointF end point
        """
    def setPaintProperties(self, properties: Any) -> Any:
        """self.setPaintProperties(properties) -> Set the paint properties for AnnotationArrow.

        To change the properties, modify the object returned from self.paintProperties() and call this method. For example:

            properties = shape.paintProperties()
            properties.setColor(QColor(255, 0, 0))
            shape.setPaintProperties(properties)
        """
    @overload
    def setStartPoint(self, x: Any, y: Any) -> Any:
        """self.setStartPoint(x, y) -> Sets the start point of the arrow.
        self.setStartPoint(point) -> Sets the start point of the arrow.

        @param x: float x-coordinate
        @param y: float y-coordinate
        @param point: QPointF start point
        """
    @overload
    def setStartPoint(self, point: Any) -> Any:
        """self.setStartPoint(x, y) -> Sets the start point of the arrow.
        self.setStartPoint(point) -> Sets the start point of the arrow.

        @param x: float x-coordinate
        @param y: float y-coordinate
        @param point: QPointF start point
        """
    def startPoint(self) -> Any:
        """self.startPoint() -> Returns the start point of the arrow as a QPointF.

        @return: QPointF
        """
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """

class AnnotationComment:
    """Class representing a comment or note on an Annotation object.

    Should not be created directly, use the relevant Annotation methods to create and access. For example, notes can be created with Annotation.addNote().

    Predefined metadata keys:
      - hiero.core.AnnotationCommentKeys.kUsername: Username of the person who created the comment
    """
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def color(self) -> _PySide6_QtGui.QColor:
        """self.color() -> get the color for the comment

        @return: PySide6.QtGui.QColor
        """
    def createdTime(self) -> _PySide6_QtCore.QDateTime:
        """self.createdTime() -> get the comment creation time

        @return: PySide6.QtCore.QDateTime
        """
    def imagePath(self) -> str:
        """self.imagePath() -> get the image path for the comment

        @return: str
        """
    def isNull(self) -> bool:
        """self.isNull() -> returns True if this is a invalid or uninitialized item, or False otherwise

        @return: True or False
        """
    def metadata(self) -> DataCollection:
        """self.metadata() -> returns a collection of metadata for the comment

        @return: hiero.core.DataCollection object
        """
    def modifiedTime(self) -> _PySide6_QtCore.QDateTime:
        """self.modifiedTime() -> get the comment modified time

        @return: PySide6.QtCore.QDateTime
        """
    def setColor(self) -> Any:
        """self.setColor() -> set the color for the comment. Setting an invalid QColor clears the color.

        @param color: the color as a PySide6.QtGui.QColor
        """
    def setCreatedTime(self) -> Any:
        """self.setCreatedTime() -> set the created time for the comment

        @param time: the time as a PySide6.QtCore.QDateTime
        """
    def setImagePath(self, path: str) -> Any:
        """self.setImagePath(path: str) -> set the image path for the comment

        @param path: the string path to set
        @raises RuntimeError: if path does not exist or file is not a valid image
        """
    def setModifiedTime(self) -> Any:
        """self.setModifiedTime() -> set the modified time for the comment

        @param time: the time as a PySide6.QtCore.QDateTime
        """
    def setText(self) -> Any:
        """self.setText() -> set the text on the comment

        @param text: the string to set
        """
    def text(self) -> str:
        """self.text() -> get the text on the comment

        @return: str
        """

class AnnotationRectangle(AnnotationElement):
    """A class, derived from AnnotationElement, representing a rectangle shape element.

    A rectangle is defined by its top-left corner and dimensions. Example usage:

        rect = AnnotationRectangle(10, 10, 200, 150)  # x, y, width, height
        props = rect.paintProperties()
        props.setFillEnabled(True)
        props.setFillColor(QColor(0, 128, 255, 128))
        rect.setPaintProperties(props)
        annotation.addElement(rect)
    """
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def copy(self) -> AnnotationRectangle:
        """self.copy() -> Return a deep copy of this rectangle shape.

        @return: AnnotationRectangle
        """
    def isNull(self, *args: Any, **kwargs: Any) -> Any: ...
    def paintProperties(self) -> PaintProperties:
        """self.paintProperties() -> Get a copy of the paint properties for AnnotationRectangle.

        @return: PaintProperties
        """
    def rect(self) -> Any:
        """self.rect() -> Returns the bounding rectangle as a QRectF.

        @return: QRectF
        """
    def rotation(self) -> float:
        """self.rotation() -> Returns the rotation angle of the rectangle in degrees.

        @return: float
        """
    def setPaintProperties(self, properties: Any) -> Any:
        """self.setPaintProperties(properties) -> Set the paint properties for AnnotationRectangle.

        To change the properties, modify the object returned from self.paintProperties() and call this method. For example:

            properties = shape.paintProperties()
            properties.setColor(QColor(255, 0, 0))
            shape.setPaintProperties(properties)
        """
    @overload
    def setRect(self, x: Any, y: Any, width: Any, height: Any) -> Any:
        """self.setRect(x, y, width, height) -> Sets the bounding rectangle.
        self.setRect(rect) -> Sets the bounding rectangle from a QRectF.

        @param x: float x-coordinate of the top-left corner
        @param y: float y-coordinate of the top-left corner
        @param width: float width of the rectangle
        @param height: float height of the rectangle
        @param rect: QRectF bounding rectangle
        """
    @overload
    def setRect(self, rect: Any) -> Any:
        """self.setRect(x, y, width, height) -> Sets the bounding rectangle.
        self.setRect(rect) -> Sets the bounding rectangle from a QRectF.

        @param x: float x-coordinate of the top-left corner
        @param y: float y-coordinate of the top-left corner
        @param width: float width of the rectangle
        @param height: float height of the rectangle
        @param rect: QRectF bounding rectangle
        """
    def setRotation(self, degrees: Any) -> Any:
        """self.setRotation(degrees) -> Sets the rotation angle of the rectangle.

        @param degrees: float rotation angle in degrees
        """
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """

class AnnotationStrokePoint:
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    penPressure: Any
    x: Any
    y: Any

class AnnotationText(AnnotationElement):
    """A class, derived from AnnotationElement, storing a single item of text within an annotation."""
    class HorizontalJustification(_enum.IntEnum):
        eHCenter: AnnotationText.HorizontalJustification
        eHJustify: AnnotationText.HorizontalJustification
        eHLeft: AnnotationText.HorizontalJustification
        eHRight: AnnotationText.HorizontalJustification
        def __new__(cls, value: Any) -> Self: ...
    class VerticalJustification(_enum.IntEnum):
        eVBaseline: AnnotationText.VerticalJustification
        eVBottom: AnnotationText.VerticalJustification
        eVCenter: AnnotationText.VerticalJustification
        eVTop: AnnotationText.VerticalJustification
        def __new__(cls, value: Any) -> Self: ...
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def backgroundColor(self) -> Any:
        """self.backgroundColor() -> QColor

        Returns the background color of the annotation text.

        @return: The QColor object for the text background color.
        """
    def box(self, *args: Any, **kwargs: Any) -> Any:
        """self.box -> Returns a tuple containing the position and size of the text box, as floating point values.

        The position is that of the box's lower left corner.

        @return: The text box position and size in the form (x, y, width, height)
        """
    def fontFamily(self) -> str:
        """self.fontFamily() -> string

        Returns the current font family name for this annotation text object.

        @return: A string containing the current font family name.
        """
    def fontSize(self, *args: Any, **kwargs: Any) -> Any: ...
    def horizontalJustification(self, *args: Any, **kwargs: Any) -> Any:
        """self.horizontalJustification

        Returns the horizontal justification of the text.

        @return: One of eHLeft, eHCenter, eHRight, eHJustify.
        """
    def isBackgroundEnabled(self) -> bool:
        """self.isBackgroundEnabled() -> bool

        Returns whether the background of the text will be rendered.

        @return: True if text background rendering is enabled, False otherwise.
        """
    def isNull(self, *args: Any, **kwargs: Any) -> Any: ...
    def rect(self) -> Any:
        """self.rect() -> QRectF

        Returns the text box as a QRectF.

        @return: QRectF
        """
    def rotation(self, *args: Any, **kwargs: Any) -> float:
        """self.rotation -> float

        Returns the rotation angle of the text, as a floating point value in degrees.

        @return: The text's rotation angle.
        """
    def setBackgroundColor(self, color: Any) -> None:
        """self.setBackgroundColor(color) -> None

        Sets the background color for the annotation text.

        @param color: QColor object.
        """
    def setBox(self, x: Any, y: Any, width: Any, height: Any) -> None:
        """self.setBox(x, y, width, height) -> None

        Deprecated. Use setRect() instead.

        @param x: The new x-component of the bottom left corner of the text box, before any rotation.
        @param y: The new y-component of the bottom left corner of the text box, before any rotation.
        @param width: The new width of the text box.
        @param height: The new height of the text box.
        """
    def setFontFamily(self) -> None:
        """self.setFontFamily() -> None

        Sets the family name of the font for use with this annotation text object.
        """
    def setFontSize(self, *args: Any, **kwargs: Any) -> Any: ...
    def setHorizontalJustification(self, *args: Any, **kwargs: Any) -> None:
        """self.setHorizontalJustification -> None

        Set the horizontal justification of the text.

        @param justify: One of eHLeft, eHCenter, eHRight, eHJustify.
        """
    @overload
    def setRect(self, x: Any, y: Any, width: Any, height: Any) -> Any:
        """self.setRect(x, y, width, height) -> Sets the text box rectangle.
        self.setRect(rect) -> Sets the text box rectangle from QRectF
        @param x: The x-coordinate of the top-left corner of the text box.
        @param y: The y-coordinate of the top-left corner of the text box.
        @param width: The width of the text box.
        @param height: The height of the text box.
        @param rect: A QRectF defining the text box.
        """
    @overload
    def setRect(self, rect: Any) -> Any:
        """self.setRect(x, y, width, height) -> Sets the text box rectangle.
        self.setRect(rect) -> Sets the text box rectangle from QRectF
        @param x: The x-coordinate of the top-left corner of the text box.
        @param y: The y-coordinate of the top-left corner of the text box.
        @param width: The width of the text box.
        @param height: The height of the text box.
        @param rect: A QRectF defining the text box.
        """
    def setRotation(self, *args: Any, **kwargs: Any) -> None:
        """self.setRotation -> None

        Sets the rotation angle of the text, with a floating point value, replacing the previous angle.

        @param rotation: The new rotation angle, in degrees.
        """
    def setText(self) -> None:
        """self.setText() -> None

        Sets the text for this annotation text object.

        @param text: The new text string.
        """
    def setVerticalJustification(self, *args: Any, **kwargs: Any) -> None:
        """self.setVerticalJustification -> None

        Set the vertical justificaiton of the text.

        @param justify: One of eVBaseline, eVTop, eVCenter, eVBottom.
        """
    def setWrapText(self, wrap: Any) -> None:
        """self.setWrapText(wrap) -> None

        Sets whether the text should wrap within the text box.

        @param wrap: True to enable text wrapping, False to disable it.
        """
    def text(self) -> str:
        """self.text() -> string

        @return: A string containing the current text for this annotation text object.
        """
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
    def verticalJustification(self, *args: Any, **kwargs: Any) -> Any:
        """self.verticalJustification

        Returns the vertical justification of the text.

        @return: One of eVBaseline, eVTop, eVCenter, eVBottom.
        """
    def wrapText(self) -> bool:
        """self.wrapText() -> bool

        Returns whether the text is set to wrap within the text box.

        @return: True if text wrapping is enabled, False otherwise.
        """

class ApplicationSettings:
    """Helper object to set and get application settings."""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @overload
    def boolValue(self, key: Any, defaultValue: Any) -> str:
        """self.boolValue(key, defaultValue) -> returns the previously stored value as True or False, named by the key parameter, or the defaultValue parameter
        self.boolValue(key) ->  returns the previously stored value as True or False, named by the key parameter, or the default value as configured (if configured) by the Hiero code. Use this method if you're looking up a value used by Hiero internally.
        Note: use self.value(key, defaultValue) if you just want to retrieve a string setting

        @param key: string name of the value to retrieve
        @param defaultValue: the value to return if this setting hasn't been saved before. Does not save the value to the default.
        @return: string
        """
    @overload
    def boolValue(self, key: Any) -> str:
        """self.boolValue(key, defaultValue) -> returns the previously stored value as True or False, named by the key parameter, or the defaultValue parameter
        self.boolValue(key) ->  returns the previously stored value as True or False, named by the key parameter, or the default value as configured (if configured) by the Hiero code. Use this method if you're looking up a value used by Hiero internally.
        Note: use self.value(key, defaultValue) if you just want to retrieve a string setting

        @param key: string name of the value to retrieve
        @param defaultValue: the value to return if this setting hasn't been saved before. Does not save the value to the default.
        @return: string
        """
    def setBoolValue(self, key: Any, value: Any) -> Any:
        """self.setBoolValue(key, value) -> saves the value as True or False with the application's settings using the key

        @param key: string name of the value to retrieve
        @param value: the bool (True or False) value to save.
        """
    def setValue(self, name: Any, value: Any) -> Any:
        """self.setValue(key, value) -> saves the value with the application's settings using the key

        @param key: string name of the value to save

        @param value: the value to store
        """
    def value(self, name: Any, defaultValue: Any = ...) -> str:
        """self.value(key, defaultValue=None) -> returns the previously stored string value named by the key parameter, or the defaultValue parameter

        @param key: string name of the value to retrieve
        @param defaultValue: the value to return if this setting hasn't been saved before. Does not save the value to the default
        @return: string, unless the defaultValue is set, in which case, the return value will be the same type as the defaultValue (string, int or bool)
        """

class TrackBase:
    """Base class for VideoTrack and AudioTrack objects. This class should never be used directly.

    Flags for controlling behavior when removing items, these can be combined with bitwise or:
     TrackBase.eRemoveLinkedItems: removing an item will also remove any items it is linked to
     TrackBase.eDontRemoveLinkedItems: removing an item will not remove linked items
     TrackBase.eDontCollapseSubTracks: removing a sub-track item will not cause empty sub-tracks to be removed
    """
    class RemoveItemOptions(_enum.IntEnum):
        eDontCollapseSubTracks: TrackBase.RemoveItemOptions
        eDontRemoveLinkedItems: TrackBase.RemoveItemOptions
        eRemoveLinkedItems: TrackBase.RemoveItemOptions
        def __new__(cls, value: Any) -> Self: ...
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def addItem(self, item: Any) -> TrackItem:
        """self.addItem(item) -> deprecated; use addTrackItem instead. Adds a track item to this track. Throws an exception if the item overlaps any existing items on the track.

        @param item: the hiero.core.TrackItem to add to this track
        @return: hiero.core.TrackItem object
        """
    def addTag(self, tag: Any) -> Tag:
        """self.addTag(tag) -> adds the specified tag to the Track.

        @param tag: Tag object to apply to the track
        @return: a hiero.core.Tag object
        """
    def addTagToRange(self, tag: Any, inTime: Any, outTime: Any) -> Tag:
        """self.addTagToRange(tag, inTime, outTime) -> adds the tag to the specified range of the Track.

        @param tag: Tag object to apply to the track
        @param inTime: start time of the tag
        @param outTime: end time of the tag
        @return: a hiero.core.Tag object
        """
    def addTransition(self, transition: Any) -> Transition:
        """self.addTransition(transition) -> adds a transition to the timeline for the track.  Can only be called when the track has been added to a Sequence.

        Note that a transition can only be added to a single track. Calling this function with a Transition object which already belongs to a Track will result in an error. 
        Transition items can be reomoved from a track using the removeTransition function. 

        @param transition: the hiero.core.Transition to add to this track
        @return: a hiero.core.Transition object
        """
    def clearRange(self, start: Any, end: Any, ripple: Any) -> Any:
        """self.clearRange(start, end, ripple) -> Clears a time range out of the track; effectively a razor on any clips straddling the start and end, and a delete of everything else.

        @param start: the start of the range to clear
        @param end: the end of the range to clear
        @param ripple: set to True to shift the remaining track items to the left
        """
    def guid(self) -> str: ...
    def isEmpty(self) -> bool:
        """self.isEmpty() -> returns True if the Track contains no items.

        @return: True or False
        """
    def isEnabled(self) -> bool:
        """self.isEnabled() -> returns True if the Track object is enabled.

        @return: True or False
        """
    def isLocked(self) -> bool:
        """self.isLocked() -> returns True if the Track object is locked.

        @return: True or False
        """
    def isNull(self) -> bool:
        """self.isNull() -> returns True if the Track object is invalid.

        @return: True or False
        """
    def metadata(self) -> DataCollection:
        """self.metadata() -> returns the metadata for this Track.

        @return: hiero.core.DataCollection object
        """
    def name(self) -> str:
        """self.name() -> returns the name of the track. Identical to calling trackName().

        @return: string
        """
    def numItems(self) -> int:
        """self.numItems() -> returns the number of items in this track.

        @return: int
        """
    def numTransitions(self) -> int:
        """self.numTransitions() -> returns the number of transitions in this track.

        @return: int
        """
    def project(self) -> Project:
        """self.project() -> returns the Project object that this item is attached to or None if the object is not attached to a project.

        @return: hiero.core.Project object
        """
    def razorAt(self, time: Any) -> Any:
        """self.razorAt(time) -> Creates razor cuts on a track for the parameter time(s).

        @param time: if a single (integer) value, indicates the razor cut time; if a tuple or list of integer values, then the times to create multiple cuts at
        """
    def removeItem(self, trackItem: Any, option: Any = ...) -> Any:
        """self.removeItem(trackItem, option=eRemoveLinkedItems) -> removes a track item from this track.

        @param trackItem: the hiero.core.TrackItem to remove from this track
        @param option: options controlling the remove behavior. By default linked items are also removed. Note that if linked effects are not removed, this will put them in an invalid state.
        """
    def removeTag(self, tag: Any) -> Any:
        """self.removeTag(tag) -> removes the tag from the track.

        @param tag: tag object
        """
    def removeTransition(self, transition: Any) -> Any:
        """self.removeTransition(transition) -> removes a transition from the timeline of this track.

        @param transition: the hiero.core.Transition to remove from this track's timeline
        """
    def setEnabled(self) -> Any:
        """self.setEnabled() -> enables or disables the Track."""
    def setLocked(self) -> bool:
        """self.setLocked() -> locks or unlocks the Track.

        @return: True or False
        """
    def setName(self) -> Any:
        """self.setName() -> Sets the name of a track.

        @param: string
        """
    def tags(self) -> tuple:
        """self.tags() -> returns a tuple of all of the tags applied to this object.

        @return: tuple of hiero.core.Tag objects
        """
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
    def trackIndex(self) -> int: ...
    def trackName(self) -> str:
        """self.trackName() -> returns the name of the track. Identical to calling name().

        @return: string
        """
    def transitions(self) -> tuple:
        """self.transitions() -> returns a tuple of all of the transitions applied to this track object.

        @return: tuple of hiero.core.Transition objects
        """

class AudioTrack(TrackBase):
    """Object for manipulating audio tracks."""
    class Channel(_enum.IntEnum):
        kCentre: AudioTrack.Channel
        kFrontLeft: AudioTrack.Channel
        kFrontRight: AudioTrack.Channel
        kMono: AudioTrack.Channel
        kRearLeft: AudioTrack.Channel
        kRearRight: AudioTrack.Channel
        kSideLeft: AudioTrack.Channel
        kSideRight: AudioTrack.Channel
        kSub: AudioTrack.Channel
        kUnknown: AudioTrack.Channel
        def __new__(cls, value: Any) -> Self: ...
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def addTrackItem(self, clip: Any, audioChannel: int = ..., position: int = ...) -> TrackItem:
        """self.addTrackItem(clip, audioChannel, position) -> if the first parameter is a Clip object, the second and third parameters must be specified and this method creates a new track item with the specified audio channel and adds it to this audio track at the given position.
        If the first parameter is a TrackItem, then this method just adds the track item specified.
        This method will cut or delete track items that overlap with the one being added.
        This method can only be called if the track has already been added to a Sequence.

        @param clip: a hiero.core.Clip object or a hiero.core.TrackItem object, to add to this audio track.
        @param audioChannel: int; audio channel that will be associated with the track item. Do not specify if clip is a TrackItem.
        @param position: int; insert position. Do not specify if clip is a TrackItem.
        @return: hiero.core.TrackItem object
        """
    def channel(self) -> AudioTrack.Channel:
        """self.channel() -> returns the channel of the audio track.

        @return: String
        """
    def clone(*args, **kwargs: Any) -> AudioTrack:
        """self.clone() -> returns a deep copy of this object.

        @return: hiero.core.AudioTrack object

        WARNING - DEPRECATED ( clone ): This method is deprecated and will not be present in future versions of the Python API.
        This method has been replaced by copy().
        """
    def copy(self) -> AudioTrack:
        """self.copy() -> returns a deep copy of this object.

        @return: hiero.core.AudioTrack object
        """
    def createTrackItem(self, name: Any) -> TrackItem:
        """self.createTrackItem(name) -> creates a new track item.

        @param name: the name of the new track item
        @return: hiero.core.TrackItem object
        """
    def items(self) -> tuple:
        """self.items() -> returns a tuple with all of the track items contained by this track.

        @return: tuple of hiero.core.TrackItem objects
        """
    def parent(self) -> Sequence:
        """self.parent() -> returns the sequence that contains this track.

        @return: hiero.core.Sequence object
        """
    def setChannel(self) -> Any:
        """self.setChannel() -> Sets the channel of an audio track.

        @param: channel to set
        """
    def setVolume(self) -> Any:
        """self.setVolume() -> Sets the volume of an audio track (0 - 1).

        @param: volume to set
        """
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
    def trackIndex(self) -> int: ...
    def volume(self) -> float:
        """self.volume() -> returns the volume of the audio track.

        @return: double
        """

class BackgroundRenderObserver:
    """Observer of background renders."""
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def isNull(self, *args: Any, **kwargs: Any) -> Any: ...
    def onFrameRenderCancelled(self, *args: Any, **kwargs: Any) -> Any: ...
    def onFrameRenderError(self, *args: Any, **kwargs: Any) -> Any: ...
    def onFrameRenderInProgress(self, *args: Any, **kwargs: Any) -> Any: ...
    def onFrameRenderQueued(self, *args: Any, **kwargs: Any) -> Any: ...
    def onFrameRendered(self, *args: Any, **kwargs: Any) -> Any: ...
    def onRenderQueued(self, *args: Any, **kwargs: Any) -> Any: ...

class Bin:
    """Container object for hiero.core.BinItem objects (wrapping hiero.core.Clip and hiero.core.Sequence objects) and other hiero.core.Bin objects."""
    class ItemType(_enum.IntEnum):
        kBin: Bin.ItemType
        kClip: Bin.ItemType
        kNone: Bin.ItemType
        kSequence: Bin.ItemType
        kTag: Bin.ItemType
        def __new__(cls, value: Any) -> Self: ...
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __contains__(self, key: Any, /) -> bool:
        """Return key in self."""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def addItem(self, object: Bin) -> Any:
        """self.addItem(object) -> adds the item to the bin object.

        @param object: hiero.core.Bin, hiero.core.BinItem, or hiero.core.Tag object, to be added as a sub item of the bin object
        @return: Added object
        """
    def bins(self) -> tuple:
        """self.bins() -> returns a tuple with all of the sub bins contained by this object.

        @return: tuple of hiero.core.Bin objects
        """
    def clips(self) -> tuple[BinItem, ...]:
        """self.clips() -> returns a tuple with all of the BinItem's containing clips contained by this bin.

        @return: tuple of hiero.core.BinItem objects
        """
    def color(self) -> _PySide6_QtGui.QColor:
        """self.color() -> Get the bin display color, or an invalid QColor if not set.

        @return: PySide6.QtGui.QColor
        """
    def createClip(self, path: Any, **knobs: Any) -> Any:
        """self.createClip(path, **knobs) -> Construct a clip from a path and optional knob values, and add it to the bin.

        @param path: path to use, may contain expressions
        @param knobs: keyword args for specifying additional knobs to set
        @return: the created Clip
        """
    def deserializeChildItem(self, arg1: Any, arg2: Any, /) -> Any: ...
    def displayColor(self) -> _PySide6_QtGui.QColor:
        """self.displayColor() -> Returns the bin's color if one is set, otherwise returns the preference color associated with this bin.

        @return: PySide6.QtGui.QColor
        """
    def guid(self) -> str: ...
    def importFolder(self, path: Any) -> Bin:
        """self.importFolder(path) -> imports the media in the path into this bin (needs a project).

        @param path: path to the media to import
        @return Bin: returns the bin created for imported media
        """
    def importSequence(self, filename: str, timeBase: TimeBase = ..., frameRate: float = ..., dropFrame: bool = ...) -> Sequence:
        """self.importSequence(filename, timeBase=None, frameRate=None, dropFrame=False) -> imports the sequence stored in filename into this bin (needs a project).  If the timebase/frame rate for the sequence isnot specified, the project defaults will be used.

        @param filename: path to the file to import the sequence from
        @param timeBase: optional argument of type hiero.core.TimeBase specifying the timebase for the created sequence
        @param frameRate: optional float argument specifying the frame rate for the created sequence
        @return: hiero.core.Sequence the created sequence
        """
    def isNull(self) -> bool:
        """self.isNull() -> returns True if the object is invalid.

        @return: True or False
        """
    def items(self, typeFilter: Any = ...) -> Any:
        """self.items(typeFilter) -> returns a tuple with all of the objects contained by this bin, filtered by the typeFilter argument, if supplied.

        @param typeFilter: combination of hiero.core.Bin.ItemType flags
        @return: tuple of hiero.core.BinItem objects
        """
    def moveItem(self, arg1: Any, arg2: Any, /) -> Any: ...
    def name(self) -> str:
        """self.name() -> returns the name of the bin.

        @return: True or False
        """
    def numChildren(self) -> int:
        """self.numChildren() -> returns the number of child objects contained by this bin.

        @return: int
        """
    def parentBin(self) -> Bin | Project:
        """self.parentBin() -> returns the bin that contains this object.

        @return: hiero.core.Bin object
        """
    def project(self) -> Project:
        """self.project() -> returns the Project object that this is attached to, or None if the object is not attached to a project.

        @return: hiero.core.Project object
        """
    def reconnectMedia(self, path: Any) -> Any:
        """self.reconnectMedia(path) -> For any Clips or Sequences in the bin, reconnects media found in the specified path.

        @param path: path containing media to reconnect to
        """
    def removeItem(self, object: Bin) -> Any:
        """self.removeItem(object) -> removes the item from the bin object. If the object is not a child item of the bin object, throws an exception.

        @param object: hiero.core.Bin, hiero.core.BinItem, or hiero.core.Tag object to be removed as a sub item of the bin object
        """
    def sequences(self) -> tuple[BinItem, ...]:
        """self.sequences() -> returns a tuple with all of the BinItem's containing sequences contained by this bin.

        @return: tuple of hiero.core.BinItem objects
        """
    def serialize(self) -> str: ...
    def setColor(self, color: Any) -> Any:
        """self.setColor(color) -> Set the bin display color.

        @param color: the color to set, as a PySide6.QtGui.QColor, a string (e.g. '#ff0000') or an integer containing the RGB components (e.g. 0x11aa33).
        """
    def setName(self, name: Any) -> Any:
        """self.setName(name) -> set the name of the bin."""
    def syncName(self, name: Any) -> Any:
        """self.syncName(name) -> set the name of the bin without sending additional notifications."""
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """

class BinItem:
    """Generic object wrapper with shared functionality for sequences and clips."""
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def activeItem(self) -> Clip | Sequence:
        """self.activeItem() -> returns the item contained by this bin item.

        @return: hiero.core.Clip or hiero.core.Sequence object
        """
    def activeVersion(self) -> Version:
        """self.activeVersion() -> gets the currently active Version object of the bin item.

        @return: hiero.core.Version object
        """
    @overload
    def addSnapshot(self, comment: Any) -> Snapshot:
        """self.addSnapshot(comment) -> adds a new snapshot for the object, with a comment.
        self.addSnapshot(sequence, comment) -> adds a new snapshot for the object, using the sequence as the new snapshot, setting the comment.

        @param comment: a comment string to set on the snapshot
        @param sequence: a hiero.core.Sequence object to create the Snapshot from
        @return: hiero.core.Snapshot object
        """
    @overload
    def addSnapshot(self, sequence: Any, comment: Any) -> Snapshot:
        """self.addSnapshot(comment) -> adds a new snapshot for the object, with a comment.
        self.addSnapshot(sequence, comment) -> adds a new snapshot for the object, using the sequence as the new snapshot, setting the comment.

        @param comment: a comment string to set on the snapshot
        @param sequence: a hiero.core.Sequence object to create the Snapshot from
        @return: hiero.core.Snapshot object
        """
    def addVersion(self, version: Any) -> Version:
        """self.addVersion(version) -> adds the version parameter to the bin item.

        @param version: hiero.core.Version object for the new version
        @param position: position at which the new Version must be inserted, if -1 then insert at end
        @return: hiero.core.Version object
        """
    def clone(*args, **kwargs: Any) -> BinItem:
        """self.clone() -> returns a deep copy of this object.

        @return: hiero.core.BinItem object

        WARNING - DEPRECATED ( clone ): This method is deprecated and will not be present in future versions of the Python API.
        This method has been replaced by copy().
        """
    def color(self) -> _PySide6_QtGui.QColor:
        """self.color() -> Get the bin item display color, or an invalid QColor if not set.

        @return: PySide6.QtGui.QColor
        """
    def copy(self) -> BinItem:
        """self.copy() -> returns a deep copy of this object.

        @return: hiero.core.BinItem object
        """
    def createClipVersion(self, position: Any, path: Any, **knobs: Any) -> Any:
        """self.createClipVersion(position, path, **knobs) -> Construct a clip from a path and optional knob values, and add it as a new version. Raises RuntimeError if creating the clip fails or the path already exists as a version.

        @param position: position at which the new Version must be inserted, if -1 then insert at end
        @param path: path to use, may contain expressions
        @param knobs: keyword args for specifying additional knobs to set
        @return: the created Version
        """
    def deserializeChildItem(self, arg1: Any, arg2: Any, /) -> Any: ...
    def displayColor(self) -> _PySide6_QtGui.QColor:
        """self.displayColor() -> Returns the item's color if one is set, otherwise returns the preference color associated with this item type.

        @return: PySide6.QtGui.QColor
        """
    def guid(self) -> str: ...
    def hasVersion(self, index: Any) -> bool:
        """self.hasVersion(index) -> checks if a given version exists and is valid.

        @param index: index of the version to check for
        @return: True or False
        """
    def isClipVersion(self, index: Any) -> bool:
        """self.isClipVersion(index) -> checks if a given clip belongs to this BinItem as a version.

        @param clip: Clip to look for
        @return: True or False
        """
    def isNull(self) -> bool:
        """self.isNull() -> returns True if the object contains a invalid hiero.core.Sequence or hiero.core.Clip object.

        @return: True or False
        """
    def items(self) -> tuple[Version, ...]:
        """self.items() -> returns a tuple containing all of the different versions of this object.

        @return: tuple of hiero.core.Version objects
        """
    def maxVersion(self) -> Version:
        """self.maxVersion() -> finds the maximum (last) version and sets it as the active version on this bin item and any linked TrackItems. Offline versions and hidden versions will be ignored during the search.

        @return: hiero.core.Version object
        """
    def minVersion(self) -> Version:
        """self.minVersion() -> finds the minimum (first) version and sets it as the active version on this bin item and any linked TrackItems. Offline versions and hidden versions will be ignored during the search.

        @return: hiero.core.Version object
        """
    def name(self) -> str:
        """self.name() -> returns the name of the item.

        @return: string
        """
    def nextVersion(self) -> Version:
        """self.nextVersion() -> finds the next version and sets it as the active version on this bin item and any linked TrackItems. Offline versions and hidden versions will be ignored during the search.

        @return: hiero.core.Version object
        """
    def numSnapshots(self) -> int:
        """self.numSnapshots() -> returns the number of snapshots that this bin item has.

        @return: int
        """
    def numVersions(self) -> int:
        """self.numVersions() -> returns the number of versions for this bin item.

        @return: int
        """
    def parentBin(self) -> Bin:
        """self.parentBin() -> returns the bin object that contains this bin item.

        @return: hiero.core.Bin object
        """
    def prevVersion(self) -> Version:
        """self.prevVersion() -> finds the previous version and sets it as the active version on this bin item and any linked TrackItems. Offline versions and hidden versions will be ignored during the search.

        @return: hiero.core.Version object
        """
    def project(self) -> Project:
        """self.project() -> returns the Project object that this object is attached to, or None if the object is not attached to a project.

        @return: heiro.core.Project object
        """
    def removeVersion(self, version: Any) -> Any:
        """self.removeVersion(version) -> remove a version from the BinItem. The version must not currently be in use in the project.

        @param version: hiero.core.Version object to be removed
        """
    def restoreToSnapshot(self, index: Any) -> Any:
        """self.restoreToSnapshot(index) -> adds a new snapshot for the object, with a comment.

        @param index: index of the Snapshot to restore from. Generates an exception if the index is out of range
        """
    def serialize(self) -> str: ...
    def setActiveVersion(self, version: Any) -> Version:
        """self.setActiveVersion(version) -> sets the active version to the version parameter.
        @return: hiero.core.Version object
        """
    def setActiveVersionIndex(self, version: Any) -> Version:
        """self.setActiveVersionIndex(version) -> sets the currently active version by index.

        @param index: index of the version to make active
        @return: hiero.core.Version object

        WARNING - DEPRECATED ( setActiveVersionIndex ): This method is deprecated and will not be present in future versions of the Python API.
        Version indices are no longer unique identifiers and should not be used as such. Please use BinItem.setActiveVersion() instead.
        """
    def setColor(self, color: Any) -> Any:
        """self.setColor(color) -> Set the bin item display color.

        @param color: the color to set, as a PySide6.QtGui.QColor, a string (e.g. '#ff0000') or an integer containing the RGB components (e.g. 0x11aa33).
        """
    def setName(self, name: Any) -> Any:
        """self.setName(name) -> set the name of the item."""
    def snapshots(self) -> tuple:
        """self.snapshots() -> returns a tuple of all of the snapshots contained by this object.

        @return: tuple of hiero.core.Snapshot objects
        """
    def syncName(self, name: Any) -> Any:
        """self.syncName(name) -> set the name of the item without sending additional notifications."""
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
    def version(self, index: Any) -> Version:
        """self.version(index) -> gets a Version object for the version of the bin item specified by the index.

        @param index: index of the version to get
        @return: hiero.core.Version object
        """
    def versionDown(*args, **kwargs: Any) -> Version:
        """self.versionDown() -> decrements the current/active version and returns the newly active Version object of the bin item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionDown ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from BinItem. To find new versions, please use hiero.core.VersionScanner. To obtain the next version, please use BinItem.prevVersion().
        """
    def versionMaxAvailable(*args, **kwargs: Any) -> Version:
        """self.versionMaxAvailable() -> finds the highest version that is currently loaded and does not have missing or offline media and sets it as the active version on this bin item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionMaxAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from BinItem. This method has been replaced by BinItem.maxVersion().
        """
    def versionMinAvailable(*args, **kwargs: Any) -> Version:
        """self.versionMinAvailable() -> finds the lowest version that is currently loaded and does not have missing or offline media and sets it as the active version on this bin item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionMinAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from BinItem. This method has been replaced by BinItem.minVersion().
        """
    def versionNextAvailable(*args, **kwargs: Any) -> Version:
        """self.versionNextAvailable() -> finds the next (higher) version that is currently loaded and does not have missing or offline media and sets it as the active version on this bin item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionNextAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from BinItem. This method has been replaced by BinItem.nextVersion().
        """
    def versionPrevAvailable(*args, **kwargs: Any) -> Version:
        """self.versionPrevAvailable() -> finds the prev (lower) version that is currently loaded and does not have missing or offline media and sets it as the active version on this bin item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionPrevAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from BinItem. This method has been replaced by BinItem.prevVersion().
        """
    def versionUp(*args, **kwargs: Any) -> Version:
        """self.versionUp() -> increments the current/active version and returns the newly active Version object of the bin item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionUp ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from BinItem. To find new versions, please use hiero.core.VersionScanner. To obtain the next version, please use BinItem.nextVersion().
        """

class SequenceBase:
    """Base class for Sequence and Clip objects. Has some methods common to both of those objects. Most likely never used directly."""
    class PlayheadState(_enum.IntEnum):
        ePlayheadActive: SequenceBase.PlayheadState
        ePlayheadDisabled: SequenceBase.PlayheadState
        ePlayheadEnabled: SequenceBase.PlayheadState
        ePlayheadInvalid: SequenceBase.PlayheadState
        def __new__(cls, value: Any) -> Self: ...
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def activePlayhead(self) -> int:
        """activePlayhead() -> Returns the index of the active playhead."""
    def addAnnotation(self, arg1: Any = ..., arg2: Any = ..., /) -> Annotation:
        """Create an annotation on the sequence with an optional frame range. If not given, the range will default to frame 0.

        @param start: optional start time
        @param end: optional end time
        @return: Annotation
        """
    def addTag(self, tag: Any) -> Tag:
        """self.addTag(tag) -> adds a hiero.core.Tag object to the Clip or Sequence.

        @param tag: the tag object to add
        @return: hiero.core.Tag object
        """
    def addTagToRange(self, tag: Any, inTime: Any, outTime: Any) -> Tag:
        """self.addTagToRange(tag, inTime, outTime) -> adds a hiero.core.Tag object to the specified range of the Clip or Sequence.

        @param tag: the tag object to add
        @param inTime: the first time at which the tag is valid
        @param outTime: the last time at which the tag is valid
        @return: hiero.core.Tag object
        """
    def annotations(self) -> list[Annotation]:
        """Get a list of annotations on the sequence.

        @return: List[Annotation]
        """
    def autoDiskCacheMode(self) -> SequenceAutoDiskCacheMode:
        """self.autoDiskCacheMode() -> returns the auto disk cache mode of the Sequence or Clip.

        @return: hiero.core.SequenceAutoDiskCacheMode
        """
    def binItem(self) -> BinItem:
        """self.binItem() -> returns the parent BinItem this Sequence or Clip belongs to, if any.

        @return: BinItem
        """
    def clearInTime(self, t: Any) -> None:
        """self.clearInTime(t) -> clear the 'in' point for the clip to Time t.

        @return: None
        """
    def clearOutTime(self, *args: Any, **kwargs: Any) -> None:
        """self.clearInTime(t) -> clear the 'out' point for the clip to Time t.

        @return: None
        """
    def clearPlayheadInTime(self, index: Any) -> None:
        """clearPlayheadInTime(index) -> Clear the in marker time position for the given playhead index.
        @param index: The index of the playhead to be changed.
        @return: None
        """
    def clearPlayheadOutTime(self, index: Any) -> None:
        """clearPlayheadOutTime(index) -> Clear the out marker time position for the given playhead index.
        @param index: The index of the playhead to be changed.
        @return: None
        """
    def clearRange(self, start: Any, end: Any, ripple: Any) -> Any:
        """self.clearRange(start, end, ripple) -> Clears a time range out of the sequence; effectively a razor on any clips straddling the start and end, and a delete of everything else.

        @param start: the start of the range to clear
        @param end: the end of the range to clear
        @param ripple: set to True to shift the remaining track items to the left
        """
    def disableSoftTrims(self) -> Any:
        """self.disableSoftTrims() -> disables soft trims on the object."""
    def dropFrame(self) -> bool:
        """self.dropFrame() -> get whether sequence timecode is displayed in drop frame format"""
    def duration(self) -> int:
        """self.duration() -> returns the duration of the Clip or Sequence.

        @return: int time value
        """
    def editFinished(self, trackItems: Any = ...) -> Any:
        """self.editFinished(trackItems) -> this should be called after finishing editing the sequence to ensure that its internal state is updated properly and to send a signal to all objects listening to changes in this object (e.g. UI views).This function optionally takes a list of track items that is used to selectively rebuild only those sections of the timeline.This allows a faster update when the edited track items are known.

        @param trackItems: optional, the track items to be updated
        """
    def enableSoftTrims(self, inTime: Any, outTime: Any) -> Any:
        """self.enableSoftTrims(inTime, outTime) -> enables soft trims on the object.

        @param inTime: Time - soft trim in time
        @param outTime: Time - soft trim out time
        """
    def format(self) -> Format:
        """self.format() -> returns the output Format object for this Sequence or Clip.

        @return: hiero.core.Format object
        """
    def framerate(self) -> TimeBase:
        """self.framerate() -> returns the framerate of the Sequence or Clip.

        @return: hiero.core.TimeBase object
        """
    def inOutEnabled(self) -> bool:
        """self.inOutEnabled() -> Checks if the 'in' and 'out' points are enabled in the Sequence or Clip.

        @return: bool
        """
    def inTime(self) -> Any:
        """self.inTime() -> returns the 'in' point set on the clip.

        @return: frame
        """
    def isNull(self) -> bool:
        """self.isNull() -> returns False if this is a valid Sequence or Clip object, True otherwise.

        @return: True or False
        """
    def layers(self) -> list[str]:
        """self.layers() -> returns a list of layer names present within the Sequence or Clip.
        @return: list of layer names.
        """
    def metadata(self) -> DataCollection:
        """self.metadata() -> returns a collection of metadata for the object.

        @return: hiero.core.DataCollection object
        """
    def name(self) -> str:
        """self.name() -> returns the name of the object.

        @return: string
        """
    def outTime(self) -> Any:
        """self.outTime() -> returns the 'out' point set on the clip.

        @return: frame
        """
    def playheadCount(self, index: Any = ...) -> Any:
        """playheadCount(index) -> Returns the number of playheads in the sequence."""
    def playheadInTime(self, index: Any) -> Any:
        """playheadInTime(index) -> Returns the in marker time position of the playhead in the sequence.
        @param index: The index of the playhead.
        """
    def playheadOutTime(self, index: Any) -> Any:
        """playheadOutTime(index) -> Returns the out marker time position of the playhead in the sequence.
        @param index: The index of the playhead.
        """
    def playheadState(self, index: Any) -> Any:
        """playheadState(index) -> The state of the given playhead index.
        The available states are:  ePlayheadActive : is the active playhead
          ePlayheadEnabled : is not the active playhead but is editable
          ePlayheadDisabled : has been removed.
          ePlayheadInvalid : index does not reference a valid playhead.@param index: The index of the playhead to be queried.
        """
    def playheadTime(self, index: Any) -> Any:
        """playheadTime(index) -> Returns the time position of the playhead in the sequence.
        @param index: The index of the playhead.
        """
    def posterFrame(self) -> int:
        """self.posterFrame() -> get the frame in the sequence used for thumbnails"""
    def project(self) -> Project:
        """self.project() -> returns the Project object that this is attached to, or None if the object is not attached to a project.

        @return: hiero.core.Project object
        """
    def rawView(self) -> str:
        """self.rawView() -> returns a string representing the raw view of this sequence or clip.

        @return: string
        """
    def razorAt(self, time: Any) -> Any:
        """self.razorAt(time) -> Creates razor cuts on all of the unlocked tracks for the parameter time(s).

        @param time: if a single (integer) value, indicates the razor cut time; if a tuple or list of integer values, then the times to create multiple cuts at
        """
    def refreshInOutEnabled(self) -> None:
        """self.refreshInOutEnabled() -> Automatically set the sequence in/out enabled based on the current in/out values.

        @return: None
        """
    def removeAnnotation(self, *args: Any, **kwargs: Any) -> Any:
        """Remove an annotation from the sequence"""
    def removeTag(self, tag: Tag) -> Any:
        """self.removeTag(tag) -> removes the tag from the track.

        @param tag: hiero.core.Tag object
        """
    def setActivePlayhead(self, index: Any) -> Any:
        """setActivePlayhead(index) -> The given playhead index is made active.
        There can only be one active playhead, the previous playhead will be made inactive.
        @param index: The index of the playhead to be made active.
        """
    def setAutoDiskCacheMode(self, autoDiskCacheMode: Any) -> Any:
        """self.setAutoDiskCacheMode(autoDiskCacheMode) -> set the auto disk cache mode of the Sequence or Clip.

        @param autoDiskCacheMode: the selected hiero.core.SequenceAutoDiskCacheMode
        """
    def setDropFrame(self, drop: Any) -> Any:
        """self.setDropFrame(drop) -> set whether sequence timecode is displayed in drop frame format"""
    def setFormat(self, format: Any) -> Any:
        """self.setFormat(format) -> set the format of the Sequence or Clip.

        @param format: a hiero.core.Format object to set for the Clip or Sequence.

        Example: myClipSequence.setFormat( hiero.core.Format(2048, 400, 2.37, 'MyFormat') )
        """
    def setFramerate(self, framerate: Any) -> Any:
        """self.setFramerate(framerate) -> set the framerate of the Sequence or Clip.

        @param framerate: framerate value to set
        """
    def setInOutEnabled(self, enable: Any) -> None:
        """self.setInOutEnabled(enable) -> Enable/Disable the 'in' and 'out' points.

        @return: None
        """
    def setInTime(self, t: Any) -> None:
        """self.setInTime(t) -> set the 'in' point for the clip to Time t.
        This will also enable the In/Out lock.

        @return: None
        """
    def setName(self) -> Any:
        """self.setName() -> set the name of the object.

        @param: string new name
        """
    def setOutTime(self, t: Any) -> None:
        """self.setOutTime(t) -> set the 'out' point for the clip to Time t.
        This will also enable the In/Out lock.

        @return: None
        """
    def setPlayheadEnabled(self, index: Any, enabled: bool) -> Any:
        """setPlayheadEnabled(index, enabled) -> Put the given playhead into the enabled state. The playheadis not active but is visible and editable in the UI. Otherwise the playhead will be disabled, which means thatit will not be visible in the UI.
        The current active playhead cannot be changed by this function.
        @param index: The index of the playhead to be changed.
        @param enabled: True if the playhead is enabled.
        """
    def setPlayheadInTime(self, index: Any, time: Any) -> Any:
        """setPlayheadInTime(index, time) -> Set the in marker time position for the given playhead index.
        @param index: The index of the playhead to be changed.
        @param time: The new in time position to be set.
        """
    def setPlayheadOutTime(self, index: Any, time: Any) -> Any:
        """setPlayheadOutTime(index, time) -> Set the out marker time position for the given playhead index.
        @param index: The index of the playhead to be changed.
        @param time: The new in time position to be set.
        """
    def setPlayheadTime(self, index: Any, time: Any) -> Any:
        """setPlayheadTime(index, time) -> Set the time position for the given playhead index.
        @param index: The index of the playhead to be changed.
        @param time: The new time position to be set.
        """
    def setPosterFrame(self, frame: Any) -> Any:
        """self.setPosterFrame(frame) -> set the frame in the sequence used for thumbnails"""
    def setSoftTrimsInTime(self, inTime: Any) -> Any:
        """self.setSoftTrimsInTime(inTime) -> sets the in time for the soft trims. Note: this method does not enable soft trims if they are disabled.

        @param inTime: in frame value for the soft trims
        """
    def setSoftTrimsOutTime(self, outTime: Any) -> Any:
        """self.setSoftTrimsOutTime(outTime) -> sets the out time for the soft trims. Note: this method does not enable soft trims if they are disabled.

        @param outTime: out frame value for the soft trims
        """
    @overload
    def setTimecodeStart(self, time: Any) -> Any:
        """self.setTimecodeStart(time) -> sets the value of the start timecode by frame. To convert times to frame values, use TimeCode.HMSFToFrames or TimeCode.stringToTime.
        self.setTimecodeStart(timecodeValue, hasDropFrames) -> sets the value of the start timecode by formatted string, using the framerate of the Sequence or Clip as the time base. If just passing in a framerate, pass it in as an integer.

        @param time: frame value to set the time code to
        @param timecodeValue: string of the format "hh:mm:ss:ff"
        @param hasDropFrames: True if the timecode includes drop frames, False otherwise
        """
    @overload
    def setTimecodeStart(self, timecodeValue: Any, hasDropFrames: bool) -> Any:
        """self.setTimecodeStart(time) -> sets the value of the start timecode by frame. To convert times to frame values, use TimeCode.HMSFToFrames or TimeCode.stringToTime.
        self.setTimecodeStart(timecodeValue, hasDropFrames) -> sets the value of the start timecode by formatted string, using the framerate of the Sequence or Clip as the time base. If just passing in a framerate, pass it in as an integer.

        @param time: frame value to set the time code to
        @param timecodeValue: string of the format "hh:mm:ss:ff"
        @param hasDropFrames: True if the timecode includes drop frames, False otherwise
        """
    def softTrimsEnabled(self) -> bool:
        """self.softTrimsEnabled() -> returns True if soft trims are enabled, False otherwise.

        @return: True or False
        """
    def softTrimsInTime(self) -> Any:
        """self.softTrimsInTime() -> returns the in time set for the soft trims.

        @return: frame
        """
    def softTrimsOutTime(self) -> Any:
        """self.softTrimsOutTime() -> returns the out time set for the soft trims.

        @return: frame
        """
    def tags(self) -> tuple:
        """self.tags() -> returns a tuple of all of the tags applied to this object.

        @return: tuple of hiero.core.Tag objects
        """
    def thumbnail(self, frame: Any = ..., layer: Any = ...) -> _PySide6_QtGui.QImage:
        """self.thumbnail(frame, layer) -> returns a thumbnail of the frame specified as a QImage object.

        @param frame: the frame to get the thumbnail for (defaults to 0)
        @param layer: the layer to get the thumbnail for (defaults to rgb)
        @return: QImage object
        """
    def timecodeStart(self) -> int:
        """self.timecodeStart() -> returns the frame value of the start timecode. To convert this to a time code string, use TimeCode.timeToString.

        @return: frame
        """
    def timelineOffset(self) -> int:
        """self.timelineOffset() -> returns the timeline offset value.

        @return: frame
        """
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
    def writeAudioToFile(self) -> Any:
        """self.writeAudioToFile() -> Bounce down audio tracks and write to wav file at specified location. File will be created or overwritten.

        @param filepath: the filepath of file to be written
        @param inTime: in point of the timeline to write
        @param outTime: out point of the timeline to write
        @param numChannels: number of audio channels
        @param sampleRate: the sample rate to export to
        @param bitDepth: sample bit depth (PCM only)
        @param bitRate: audio bitrate in bits (compressed formats only)
        """

class Clip(SequenceBase):
    """Object representing a clip.

    Initialisation:
      * Clip(mediaSource)
      * Clip(mediaSource, first, last)

    mediaSource may be a MediaSource object or a string containing the media path.  If first and last are given, the Clip only plays frames within this range.
    """
    class LocalizationPolicy(_enum.IntEnum):
        kAlwaysLocalize: Clip.LocalizationPolicy
        kAutoLocalize: Clip.LocalizationPolicy
        kNeverLocalize: Clip.LocalizationPolicy
        kOffLocalize: Clip.LocalizationPolicy
        kOnDemandLocalize: Clip.LocalizationPolicy
        kOnLocalize: Clip.LocalizationPolicy
        def __new__(cls, value: Any) -> Self: ...
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def addTag(self) -> Tag:
        """self.addTag() -> adds the tag to the set of tags attached to the Clip.

        @param tag: the tag object to add
        @return: hiero.core.Tag object
        """
    def addTagToRange(self, tag: Any, inTime: Any, outTime: Any) -> Tag:
        """self.addTagToRange(tag, inTime, outTime) -> adds the tag to the specified range of the Clip.

        @param tag: the tag object to add
        @param inTime: from - time to add tag
        @param outTime: to - time to add tag
        @return: hiero.core.Tag object
        """
    def addToNukeScript(self, script: _hiero_core_nuke_Script.ScriptWriter, additionalNodes: Any = ..., additionalNodesCallback: Any = ..., firstFrame: Any = ..., trimmed: bool = ..., trimStart: Any = ..., trimEnd: Any = ..., colourTransform: Any = ..., metadataNode: Any = ..., includeMetadataNode: bool = ..., nodeLabel: Any = ..., enabled: bool = ..., includeEffects: bool = ..., beforeBehaviour: Any = ..., afterBehaviour: Any = ..., project: Any = ..., readNodes: Any = ..., addEffectsLifetime: bool = ...) -> Any:
        """addToNukeScript(self, script, trimmed=True, trimStart=None, trimEnd=None)

        Add a Read node to the Nuke script for each media sequence/file used in this clip. If there is no media, nothing is added.

        @param script: Nuke script object to add nodes
        @param additionalNodes: List of nodes to be added post read
        @param additionalNodesCallback: callback to allow custom additional node per item function([Clip|TrackItem|Track|Sequence])
        @param firstFrame: Custom offset to move start frame of clip
        @param trimmed: If True, a TimeClip node will be added to trim the range output by the Read node. The range defaults to the clip's soft trim range. If soft trims are not enabled on the clip, the range defaults to the clip range. The range can be overridden by passing trimStart and/or trimEnd values.
        @param trimStart: Override the trim range start with this value.
        @param trimEnd: Override the trim range end with this value.
        @param colourTransform: if specified, is set as the color transform for the clip
        @param metadataNode: node containing metadata to be inserted into the script
        @param includeMetadataNode: specifies whether a metadata node should be added to the script
        @param nodeLabel: optional label for the Read node
        @param enabled: enabled status of the read node. True by default
        @param includeEffects: if True, soft effects in the clip are included
        @param beforeBehaviour: What to do for frames before the first ([hold|loop|bounce|black])
        @param afterBehaviour: What to do for frames after the last ([hold|loop|bounce|black])
        """
    def clone(*args, **kwargs: Any) -> Clip:
        """self.clone() -> returns a deep copy of this object.

        @return: hiero.core.Clip object

        WARNING - DEPRECATED ( clone ): This method is deprecated and will not be present in future versions of the Python API.
        This method has been replaced by copy().
        """
    def copy(self) -> Clip:
        """self.copy() -> returns a deep copy of this object.

        @return: hiero.core.Clip object
        """
    def createEffect(self, effectType: Any) -> Any:
        """self.createEffect(effectType) -> adds an effect to the clip

        @param effectType: The node type of create a soft effect for
        @return: The created EffectTrackItem
        """
    def effects(self) -> list:
        """self.effects() -> get the list of effects present on the clip.

        return: list(EffectTrackItem)
        """
    def entityReference(self) -> str:
        """self.entityReference() -> returns this clip's asset management system entity reference.

        @return: string
        """
    def getAvailableOcioColourTransforms(self) -> list[str]:
        """self.getAvailableOcioColourTransforms() -> returns colour transform for the source media.

        @return: string
        """
    def getReadInfo(self, firstFrame: Any = ...) -> Any:
        """Get information (filename and start at value) for any Read Node in this clip.

        @param firstFrame: Custom offset to move start frame of clip
        """
    def getVersionedName(self) -> str:
        """self.getVersionedName() -> returns the versioned display name of this clip,
        in the format 'clipName > vXXX' (or just 'clipName' if no version is
        present).

        @return: str
        """
    def guid(self) -> str: ...
    def hasError(self) -> bool:
        """self.hasError() -> check if the clip is in error state"""
    def hasMultipleViews(self) -> bool:
        """self.hasMultipleViews() -> returns true if the Clip has multiple views available for display given the current settings of the project it belongs to.

        @return: bool
        """
    def isLocalizationOutdated(self) -> bool:
        """self.isLocalizationOutdated() -> Returns whether the source media has changed.

        @return: bool
        """
    def isLocalized(self) -> bool:
        """self.isLocalized() -> returns whether the clip is completely localized.

        @return: bool
        """
    def isNull(self) -> bool:
        """self.isNull() -> returns False if this is a valid Clip object, True otherwise.

        @return: True or False
        """
    def localizationPolicy(self) -> Clip.LocalizationPolicy:
        """self.localizationPolicy() -> returns the localization policy of the clip.

        @return: LocalizationPolicy
        """
    def localizationPriority(self) -> int:
        """self.localizationPriority() -> returns localization priority value which determines the order in which files are localized

        @return: int
        """
    def localizationProgress(self) -> float:
        """self.localizationProgress() -> returns the localization progress of the clip, where 0 is totally non-localized and 1 is completely localized.

        @return: double
        """
    def mediaSource(self) -> MediaSource:
        """self.mediaSource() -> returns the clip's media source.

        @return: hiero.core.MediaSource object
        """
    def metadata(self) -> DataCollection:
        """self.isNull() -> returns a *copy* of the clip's metadata.

        @return: hiero.core.Metadata object
        """
    def numAudioTracks(self) -> int:
        """self.numAudioTracks() -> returns number of audio tracks contained by this clip.

        @return: int
        """
    def numVideoTracks(self) -> int:
        """self.numVideoTracks() -> returns number of video tracks contained by this clip.

        @return: int
        """
    def readNode(self) -> _nuke.Node:
        """self.readNode() -> returns the Read node representing the Clip's media

        @return: nuke.Node
        """
    def reconnectMedia(self, path: Any) -> Any:
        """self.reconnectMedia(path) -> Reconnect the Clip with media found in the specified path.

        @param path: path containing media to reconnect to
        """
    def refresh(self) -> Any:
        """self.refresh() -> updates the clip if the source media has changed."""
    def removeEffect(self, effect: Any) -> Any:
        """self.removeEffect(effect) -> removes the given effect from the clip"""
    def removeTag(self, tag: Tag) -> Any:
        """self.removeTag(tag) -> removes the tag from the clip.

        @param tag: hiero.core.Tag object
        """
    def rescan(self) -> Any:
        """self.rescan() -> updates the clip and rescan the frame range if the source media has changed."""
    def setCameraColourTransform(self, colourTransform: Any) -> Any:
        """self.setCameraColourTransform(colourTransform) -> sets the camera colour transform for the source media.

        @param colourTransform: Colour transform name
        """
    def setEntityReference(self, location: Any) -> Any:
        """self.setEntityReference(location) -> set this clip's (asset management system) entity reference.

        @param location: Asset management system's string identifier for the entity.
        """
    def setFrameRange(self) -> Any:
        """self.setFrameRange() -> Sets the clip frame range to the specified values."""
    def setLocalizationPolicy(self, policy: Any) -> Any:
        """self.setLocalizationPolicy( policy ) -> sets the localization policy to the clip.

        @param policy: localization policy to apply to the clip
        """
    def setLocalizationPriority(self, priority: Any) -> Any:
        """self.setLocalizationPriority( priority ) -> sets localization priority value which determines the order in which files are localized

        @param: priority int
        """
    def setSourceMediaColourTransform(self, colourTransform: Any) -> Any:
        """self.setSourceMediaColourTransform(colourTransform) -> sets the input colour transform for the source media.

        @param colourTransform: Colour transform name
        """
    def sourceIn(self) -> int:
        """self.sourceIn() -> returns the source in value for the clip.

        @return: frame
        """
    def sourceMediaColourTransform(self) -> str:
        """self.sourceMediaColourTransform() -> returns colour transform for the source media.

        @return: string
        """
    def sourceOut(self) -> int:
        """self.sourceOut() -> returns the source out value for the clip.

        @return: frame
        """
    def subTrackItems(self) -> tuple[tuple, ...]: ...
    def views(self) -> list:
        """self.views() -> get the list of views available for the clip. If it uses a path with %v/%V, this will return all the views for which media exists. If the source media contains multiple named views, it will return those (note this does not work for mov files). Otherwise returns an empty list.

        return: list(str)
        """

class ConformRule:
    """Represents a conform rule used by Hiero to make decisions when conforming. Can be derived from in order to make new conform rules."""
    class Type(_enum.IntEnum):
        kConform: ConformRule.Type
        kConformAndReconnect: ConformRule.Type
        kReconnect: ConformRule.Type
        def __new__(cls, value: Any) -> Self: ...
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def activate(self) -> Any:
        """self.activate() -> adds this conform rule to the list of conform rules. Conform operations done after this call will use the rule."""
    def appliesToTrackItems(self) -> bool:
        """self.appliesToTrackItems() -> should return True if this conform rule applies to track items.

        @return: True or False; default implementation returns True
        """
    def compare(self, media: Any, candidateMedia: Any) -> Any:
        """self.compare(media, candidateMedia) -> should compare media against candidateMedia, and return True if they match, according to this conform rule.

        The metadata contains the following keys which can be used for creating matching rules:
          Conformer.kUmid == 'umid'
          Conformer.kName == 'name'
          Conformer.kTapeName == 'tapeName'
          Conformer.kUrl == 'url'
          Conformer.kAudioChannels == 'audioChannels'
          Conformer.kDuration == 'duration'
          Conformer.kFramerate == 'framerate'
          Conformer.kFramerateIsNtsc == 'framerateIsNtsc'
          Conformer.kSamplerate == 'samplerate'
          Conformer.kMediaType == 'mediaType'
          Conformer.kMasterMediaType == 'masterMediaType'
          Conformer.kStartTime == 'startTime'
          Conformer.kTimecode == 'timecode'
          Conformer.kWidth == 'width'
          Conformer.kHeight == 'height'

        @return: True for a match, False otherwise; default implementation returns False
        """
    def conformType(self) -> Any:
        """self.conformType() -> Get the conform types for which this rule can be used.  The default is kConform.

        @return: one of the constants kConform, kReconnect, kConformAndReconnect
        """
    def deactivate(self) -> Any:
        """self.deactivate() -> removes this conform rule from the list of conform rules. Conform operations done after this call will not use the rule."""
    def isNull(self, *args: Any, **kwargs: Any) -> Any:
        """self.name() -> should return True if the conform rule is invalid.

        @return: True for invalid, False otherwise
        """
    def name(self) -> str:
        """self.name() -> returns the name of the conform rule (which was passed to the object in it's initializer).

        @return: string
        """
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """

class Conformer:
    """Provides and interface for querying and setting the conform options, such as file pattern filters and active rules.
    These options mirror those found in the conforming dialog box in the UI.
    """
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def excludeNonOverlappingTimecode(self) -> bool:
        """self.excludeNonOverlappingTimecode() -> returns the state of the exclude non-overlapping timecode flag.

        @return: True when media which does not have timecode overlapping track items is excluded from matching.
        """
    def excludePatterns(self) -> Any:
        """self.excludePatterns() -> returns the list of file patterns that are excluded from source media searches.
        By default this is empty.

        @return: A list containing the file patterns excluded from source media searches.
        """
    def includeAlreadyMatched(self) -> bool:
        """self.includeAlreadyMatched() -> returns the state of re-conform media flag.

        @return: True when the tracks that already have media attached will be re-conformed.
        """
    def includePatterns(self) -> Any:
        """self.includePatterns() -> returns the list of file patterns that are included in source media searches.
        By default this is '*', which includes all file types.

        @return: A list containing the file patterns included in source media searches.
        """
    def nativeRuleFiltering(self) -> Any:
        """self.nativeRuleFiltering() -> returns a dictionary with the names of the native conforming rules and whether they are enabled for conforming.
        By changing the state of the flags for the rules and submitting the dictionary back to the Conformer the rules can be filterd out.

        @return: A dictionary containing the enabled flag for each native rule, keyed by the rule name.
        """
    def nativeRuleNames(self) -> Any:
        """self.nativeRuleNames() -> returns the list of names for the native rules.
        This can be used to set rule filtering.

        @return: A list containing the names for all of the conform rules built-in to Hiero.
        """
    def pythonRuleFiltering(self) -> Any:
        """self.pythonRuleFiltering() -> returns a dictionary with the names of the Python conforming rules and whether they are enabled for conforming.
        By changing the state of the flags for the rules and submitting the dictionary back to the Conformer the rules can be filterd out.

        @return: A dictionary containing the enabled flag for each Python rule, keyed by the rule name.
        """
    def pythonRuleNames(self) -> Any:
        """self.pythonRuleNames() -> returns the list of names for the registered Python rules.
        This can be used to set rule filtering.

        @return: A list containing the names for all of the conform rules that have been added through the Python API.
        """
    def setExcludeNonOverlappingTimecode(self, flag: Any) -> Any:
        """self.setExcludeNonOverlappingTimecode( flag ) -> controls whether matching is done on media which does not have timecode which overlaps the track item."""
    def setExcludePatterns(self, filepatterns: Any) -> Any:
        """self.setExcludePatterns( filepatterns ) -> sets the list of file patterns to exclude from source media searches."""
    def setIncludeAlreadyMatched(self, flag: Any) -> Any:
        """self.setIncludeAlreadyMatched( flag ) -> controls whether to re-connect tracks that already have media matched to them."""
    def setIncludePatterns(self, filepatterns: Any) -> Any:
        """self.setIncludePatterns( filepatterns ) -> sets the list of file patterns to include in source media searches."""
    def setNativeRuleFiltering(self, ruleFiltering: Any) -> Any:
        """self.setNativeRuleFiltering( ruleFiltering ) -> uses a dictionary keyed on the names of the native conforming rules to set whether each rule is enabled for conforming."""
    def setPythonRuleFiltering(self, ruleFiltering: Any) -> Any:
        """self.setPythonRuleFiltering( ruleFiltering ) -> uses a dictionary keyed on the names of the Python conforming rules to set whether each rule is enabled for conforming."""
    def setUseBestTimecodeMatch(self, flag: Any) -> Any:
        """self.setUseBestTimecodeMatch( flag ) -> controls whether to accept the best timecode match if no rules match."""
    def useBestTimecodeMatch(self) -> bool:
        """self.useBestTimecodeMatch() -> returns the state of the use best timecode match flag.

        @return: True when the best timecode match will be accepted if no rules match.
        """

class DataCollection:
    """Storage objects for key/value pairs. Generally used to store metadata."""
    def __contains__(self, key: Any, /) -> bool:
        """Return key in self."""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def dict(self) -> _builtins.dict:
        """self.dict() -> returns a dictionary of key/value pairs. Can be used to iterate over the items in this collection.

        @return: dict
        """
    def hasKey(self, key: Any) -> bool:
        """self.hasKey(key) -> returns True if the collection has a value for the key.

        @param key: the key to look up
        @return: True or False
        """
    def keys(self) -> Any:
        """self.keys() -> returns keys in the collection.

        @return: list of strings which are keys in the collection
        """
    def readOnly(self, key: Any) -> bool:
        """self.readOnly(key) -> returns True if the collection can be modified.

        @return: True or False
        """
    def setValue(self, key: Any) -> Any:
        """self.setValue(key) -> sets the value of the key stored in this collection.

        @param key: the key to look up
        @param value: value to assign to key
        """
    def toString(self) -> str:
        """self.toString() -> returns a formatted list of the key/value pairs currently set on this object. Equivalent to str(object).

        @return: string
        """
    def value(self, key: Any) -> str:
        """self.value(key) -> returns the value of the key stored in this collection. Throws an exception if the key does not exist.

        @param key: the key to look up
        @return: string
        """

class TrackItemBase:
    """Base class for objects which can exist on a timeline track which provides some common methods.  Not to be used directly."""
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def clone(*args, **kwargs: Any) -> Any:
        """self.clone() -> returns a deep copy of this object.



        WARNING - DEPRECATED ( clone ): This method is deprecated and will not be present in future versions of the Python API.
        This method has been replaced by copy().
        """
    def copy(self) -> Any:
        """self.copy() -> returns a deep copy of this object."""
    def duration(self) -> int:
        """self.duration() -> returns the timeline duration value for the item.

        @return: frames
        """
    def guid(self) -> str: ...
    def isEnabled(self) -> bool:
        """self.isEnabled() -> returns True if the track item is enabled.

        @return: True or False
        """
    def isNull(self) -> bool:
        """self.isNull() -> returns True if the track item is invalid.

        @return: True or False
        """
    def linkedItems(self) -> tuple:
        """self.linkedItems() -> returns a tuple of track item objects linked to this one.

        @return: tuple of linked items
        """
    def move(self, time: Any) -> Any:
        """self.move(time) -> moves the item in the sequence. This will keep the duration.

        @param time: frame value. If positive, the item moves right. If negative, the item moves left.
        """
    @staticmethod
    def moveTrackItems(trackItems: Any, time: Any) -> Any:
        """TrackItem.moveTrackItems(trackItems, time) -> moves a group of track items in the sequence.

        @param trackItems: sequence of track items to move
        @param time: frame value. If positive, the trackitems move right. If negative, the trackitems move left.
        """
    def parent(self) -> AudioTrack | VideoTrack:
        """self.parent() -> returns the AudioTrack or VideoTrack that contains this item.

        @return: hiero.core.AudioTrack or hiero.core.VideoTrack object
        """
    def parentSequence(self) -> Sequence | Clip:
        """self.parentSequence() -> returns the sequence for the current track item as a Python object, or None if no track or sequence is found.

        @return: hiero.core.Sequence | hiero.core.Clip
        """
    def parentTrack(self) -> TrackBase: ...
    def project(self) -> Project:
        """self.project() -> returns the Project object that this is attached to, or None if the object is not attached to a project.

        @return: hiero.core.Project object
        """
    def sequence(self) -> Sequence | Clip:
        """self.sequence() -> deprecated; use parentSequence() instead. Returns the sequence for the current track item as a Python object, or None if no track or sequence is found.

        @return: hiero.core.Sequence | hiero.core.Clip
        """
    def setEnabled(self, enabled: Any) -> Any:
        """self.setEnabled(enabled) -> enables or disables the track item.

        @param enabled: Enabled state
        """
    def setTimelineIn(self, inTime: Any) -> Any:
        """self.setTimelineIn(inTime) -> sets the timeline in value. Shrinks or grows the timeline duration, as appropriate.

        @param inTime: frame value
        """
    def setTimelineOut(self, outTime: Any) -> Any:
        """self.setTimelineOut(outTime) -> sets the timeline out value. Shrinks or grows the timeline duration, as appropriate.

        @param outTime: frame value
        """
    def timelineIn(self) -> int:
        """self.timelineIn() -> returns the timeline in value for the track item.

        @return: frames
        """
    def timelineOut(self) -> int:
        """self.timelineOut() -> returns the timeline out value for the track item.

        @return: frames
        """
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
    def trimIn(self, time: Any) -> Any:
        """self.trimIn(time) -> trims the left end of the item. This will grow or shrink the duration and the sourceDuration, but keep the playback speed.

        @param time: frame value. If positive, the item duration shrinks. If negative, the item duration grows.
        """
    def trimOut(self, time: Any) -> Any:
        """self.trimOut(time) -> trims the right end of the item. This will grow or shrink the duration and the sourceDuration, but keep the playback speed.

        @param time: frame value. If positive, the item duration shrinks. If negative, the item duration grows.
        """

class SubTrackItem(TrackItemBase):
    """Base class for items that exist in sub-tracks, e.g. Annotation objects. This class should never be used directly."""
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def descString(self, *args: Any, **kwargs: Any) -> Any: ...
    def setTimelineIn(self, inTime: Any) -> Any:
        """self.setTimelineIn(inTime) -> sets the in point for this SubTrackItem. Note that this trims the duration of the SubTrackItem.

        @param inTime: frame for the new in point
        """
    def setTimelineOut(self, outTime: Any) -> Any:
        """self.setTimelineOut(outTime) -> sets the out point for this SubTrackItem. Note that this trims the duration of the SubTrackItem.

        @param outTime: frame for the new out point
        """
    def subTrackIndex(self) -> Any:
        """self.subTrackIndex() -> get the index of the item's parent sub-track.

        @return: int index, -1 if the item has not been added to a track
        """
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """

class EffectTrackItem(SubTrackItem):
    """Class representing an effect on a sequence.  EffectTrackItem is derived from SubTrackItem and thus EffectTrackItem objects can be placed and trimmed on VideoTrack subtracks.
    The effect's node can be accessed with effect.node(), which can then be manipulated through the nuke Node API.To create effects, it is recommended you use the hiero.core.VideoTrack.createEffect() method.

    Usage:
    EffectTrackItem(effectType)
    EffectTrackItem(effectType, timelineIn, timelineOut)
    """
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addToNukeScript(self, script: _hiero_core_nuke_Script.ScriptWriter, offset: Any = ..., inputs: Any = ..., startHandle: Any = ..., endHandle: Any = ..., addLifetime: bool = ...) -> Any: ...
    def clone(self) -> Any:
        """self.clone() -> returns a deep copy of this object but, unlike copy(), this clones the underlying Nuke node so that the knobs are shared."""
    def copy(self, *args: Any, **kwargs: Any) -> Any: ...
    def declone(self) -> Any:
        """self.declone() -> Declones the effect item. Has no effect if the item is not a clone."""
    def executeNode(self, frames: Any) -> Any:
        """self.executeNode(frames) -> execute the effect item's node

        @param frames: a sequence of frame numbers to execute
        """
    def isRetimeEffect(self) -> bool:
        """Check if an EffectTrackItem applies a retime.  Currently this only applies to TimeWarp effects. """
    def isValid(self) -> Any:
        """self.isValid() -> Returns true if the effect item is in a valid state and position and false otherwise."""
    def name(self) -> str:
        """self.name() -> Get the name of the effect's node.

        @return: string
        """
    def node(self) -> Any:
        """self.node() -> Node

        Get the node used to apply the effect.

        @return: The effect node.
        """
    def nodeHasError(self) -> Any:
        """self.nodeHasError() -> Returns True if the node is in error.

        Note that an error on a node may not appear if it has not been rendered e.g. by the viewer, because, it may have not been validated.
        """
    def setName(self, name: str) -> None:
        """self.setName() -> Set the name of the effect's node."""
    def toString(self, *args: Any, **kwargs: Any) -> Any: ...

class FlipbookManager:
    """Object for Flipbook manager"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def createClip(self, filepath: Any) -> Clip:
        """self.createClip(filepath) -> creates and return a flipbook clip for the defined filepath.

        @param filepath: The file path of the source media for which to create the clip
        @param knobsScript: Optional string containing one or more pairs of Read node knob names and values,
          which can be used to configure the Clip beyond default the behaviour.
          The name/value pairs should be separated by newlines (\\n), as in the output from Node.writeKnobs().  The path specified by filepath takes precedence over the possible presence of 'file' in knobsScript.
          Defaults to an empty string.
        @return: hiero.core.Clip
        """
    def createEffectItem(self, effectType: Any, timelineIn: Any, timelineOut: Any) -> EffectTrackItem:
        """self.createEffectItem(effectType, timelineIn, timelineOut) -> creates and return a flipbook Soft Effect with defiend effectType,
        covering the specified timeline in and out range.

        @return: hiero.core.EffectTrackItem
        """
    def createSequence(self, framerate: Any, outputformat: Any) -> Sequence:
        """self.createSequence(framerate, outputformat) -> creates and returns a flipbook sequence with the defined framerate and ouput formar.

        @return: hiero.core.Sequence
        """
    def setWorkingSpace(self, workingSpace: Any) -> None:
        """self.setWorkingSpace(workingSpace) -> sets the colorspace to use as the working space.

        @return: None
        """
    def updateOCIOConfig(self, ocioConfigPath: Any) -> None:
        """self.updateOCIOConfig(ocioConfigPath) -> updates the flipbook OCIO setting with the defined ocio config filename.

        @return: None
        """

class Format:
    """Object containing width, height, pixel aspect, and name of a Clip/Sequence format.

    Initialisation:
    Format(width, height, pixel_aspect, name)

    Format(formatStr)

    @param: width - the format's width in pixels (integer)
    @param: height - the format's height in pixels (integer)
    @param: pixel_aspect - the format's pixel aspect ratio (float)
    @param: name - the display name of the format (string)

    @param: formatStr - the string representation of the format in the form returned by str(format)

    Examples: F = hiero.core.Format(2048, 400, 2.37, 'MyFormat'), F = hiero.core.Format('2048 400 0 0 2048 400 2.37 MyFormat')
    """
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def addToNukeScript(self, script: Any = ..., resize: str = ..., black_outside: bool = ...) -> Any:
        """self.addToNukeScript(self, script, to_type) -> adds a Reformat node matching this Format to the specified script and returns the nuke node object.         @param script: Nuke script object to add nodes to, or None to just generate and return the node.     @param resize: Type of resize (use constants from nuke.ReformatNode, default is kResizeWidth).     @parm black_outside: Value for the black_outside knob.     @return: hiero.core.nuke.ReformatNode object
    
        """
    def aspect(self) -> float:
        """self.aspect() -> returns the aspect ratio of this format.

        @return: float
        """
    def cleanAperture(self) -> tuple[int, ...]:
        """self.cleanAperture() -> returns a 4 element tuple with the rectangle (x1, y1, x2, y2) of the clean aperture.

        @return: tuple
        """
    def height(self) -> int:
        """self.height() -> returns the height of this format.

        @return: int
        """
    def isValid(self) -> bool:
        """self.isValid() -> returns whether or not this format object has valid data.

        @return: True or False
        """
    def name(self) -> str:
        """self.name() -> returns the name of this format.

        @return: string
        """
    def pixelAspect(self) -> float:
        """self.pixelAspect() -> returns the pixel aspect ratio of this format.

        @return: float
        """
    def productionAperture(self) -> tuple[int, ...]:
        """self.productionAperture() -> returns a 4 element tuple with the rectangle (x1, y1, x2, y2) of the production aperture.

        @return: tuple
        """
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
    def width(self) -> int:
        """self.width() -> returns the width of this format

        @return: int
        """

class IExportStructure:
    """Base class to be derived from in order to populate an ExportStructureViewer widget, such as the one used in the Export dialog box. IExportStructure objects provides access to a root node, which has to be an object derived from IExportStructureElement, which the ExportStructureViewer widget then uses to determine the tree structure to display to the user. For an example of how to derive from this class, see Plugins/site-packages/hiero/core/FnExportStructure.py. For an example use of a derived IExportStructure object, see Plugins/site-packages/hiero/exporters/FnShotProcessor.py. It will often be more than sufficient to just use an ExportStructure2 object, instead of subclassing IExportStructure directly."""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def childElement(self, path: Any) -> Any:
        """self.childElement(path) -> should return an object derived from IExportStructureElement, representing a child with the path specified.

        @param path: the path to the new (or existing) child element
        @return: IExportStructureElement derived object
        """
    def exportRootPath(self) -> str:
        """self.exportRootPath() -> retrieves the root path for the export structure.

        @return: string
        """
    def rootElement(self) -> Any:
        """self.rootElement() -> should return a IExportStructureElement super class object, representing the root of the export file structure.

        @return: IExportStructureElement derived object
        """
    def setExportRootPath(self, path: Any) -> Any:
        """self.setExportRootPath(path) -> called when the user has modified the export root path, to inform the object of the new path.

        @param path: the new user supplied path to export to.
        """

class IExportStructureElement:
    """Base class to be derived from and used in conjunction with a custom implementation of IExportStructure. For an example of how to derive from this class, see Plugins/site-packages/hiero/core/FnExportStructure.py."""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addChild(self, newChild: IExportStructureElement) -> Any:
        """self.addChild(newChild) -> should append the new child item to this node's children, and set the parent on the child to this node.

        @param newChild: hiero.core.IExportStructureElement object
        """
    def child(self, index: Any) -> IExportStructureElement:
        """self.child(index) -> should return the child of this node, based on the index.

        @param index: int index of the child to return
        @return: hiero.core.IExportStructureElement object
        """
    def childCount(self) -> int:
        """self.childCount() -> should return the number of child nodes on this item.

        @return: int
        """
    def childIndex(self, exportElementChild: IExportStructureElement) -> int:
        """self.childIndex(exportElementChild) -> if the parameter is a child of this node, then this method should return the index of that child amongst the node's other children.

        @param exportElementChild: hiero.core.IExportStructureElement object
        @return: int
        """
    def clearChildren(self) -> Any:
        """self.clearChildren() -> clears all of the children nodes from this node."""
    def createChildFolder(self, path: Any) -> IExportStructureElement:
        """self.createChildFolder(path) -> create a child folder, including any needed intermediate folders, for the given path. If the named folder already exists, returns it.

        @param path: the path to the new folder
        @return: hiero.core.IExportStructureElement object
        """
    def createChildTask(self, path: Any) -> IExportStructureElement:
        """self.createChildTask(path) -> create a child task, including any needed intermediate folders, for the given path.

        @param path: the path to the new element
        @return: hiero.core.IExportStructureElement object
        """
    def fromXml(self, xmlText: Any) -> Any:
        """self.fromXml(xmlText) -> should reinitialize the node from the xml text, and recreate the preset and all child nodes as well. If initialized using taskRegistry._savePresetElement, taskRegistry._loadPresetElement can be used to get data back out.

        @param xmlText: xml formatted text, as a result of a call in the past to the toXml method
        """
    def isLeaf(self) -> bool:
        """self.isLeaf() -> should return True if this is a node with no children, otherwise it should return False.

        @return: True or False
        """
    def name(self) -> str:
        """self.name() -> should return the name of this element.

        @return: string
        """
    def parent(self) -> IExportStructureElement:
        """self.parent() -> should return the parent node of this object.

        @return: hiero.core.IExportStructureElement object
        """
    def path(self) -> str:
        """self.path() -> should return the full path to this node, including the path of any parents of this node.

        @return: string
        """
    def preset(self) -> Any:
        """self.preset() -> should return an object derived from TaskPreset, representing the task associated with this element of the export structure.

        @return: hiero.core.TaskPreset derived object
        """
    def removeChild(self, child: Any) -> Any:
        """self.removeChild(child) -> should remove the child from the node's list of children

        @param child: hiero.core.IExportStructureElement child object to remove
        """
    def setName(self, name: str) -> Any:
        """self.setName(name) -> called to tell the node it's name.

        @param name: string
        """
    def setPreset(self, preset: Any) -> Any:
        """self.setPreset(preset) -> tells the object that the user has selected a new preset for this particular export element.

        @param preset: a hiero.core.TaskPreset derived object, which can be used to create a task to process later on during an export.
        """
    def setPresetType(self, presetType: Any) -> Any:
        """self.setPresetType(presetType) -> called to tell the object to set the task preset type by name. The taskRegistry can be used with this 'type' to create the preset to store.

        @param presetType: the name of the task preset to create/use.
        """
    def toXml(self) -> str:
        """self.toXml() -> should return a string of formatted xml which can be sent to the fromXml method later to read it back. The xml should include the preset data for this node, as well as the children, and should be in proper xml format. This can be done easily with xml.etree.ElementTree, especially because the taskRegistry has methods to write out xml for presets and other objects (taskRegistry._savePresetElement)

        @return: string
        """

class IExporterRegistry:
    """IExporterRegistry provides a simple interface for our C++ Application to access python instance of hiero.core.TaskRegistry.

    This class should not be used directly; use hiero.core.TaskRegistry instead.
    """
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def assignPresetToProject(self, *args: Any, **kwargs: Any) -> Any:
        """self.assignPresetToProject(hiero.core.TaskPreset, hiero.core.Project) -> Called by the C++ application to assign a TaskPreset to .
        a null hiero.core.Project will remove the project assignment and revernt the preset to local ownership.

        @param: hiero.core.TaskPreset
        @param: hiero.core.Project
        """
    def copyAndAddProcessorPreset(self) -> Any:
        """self.copyAndAddProcessorPreset() -> Called by the C++ application to duplicate a preset.

        @param: hiero.core.TaskPreset instance for duplication
        @return: new hiero.core.TaskPreset instance
        """
    def copyAndAddProjectPreset(self) -> Any:
        """copyAndAddProjectPreset() -> Called by the C++ application to duplicate a preset and assign it to a new project.

        @param: hiero.core.TaskPreset instance for duplication
        @param: hiero.core.Project to which cloned preset should be assigned
        @return: new hiero.core.TaskPreset instance
        """
    def createAndAddProcessorPreset(self, *args: Any, **kwargs: Any) -> Any:
        """self.createAndAddProcessorPreset(string, hiero.core.TaskPreset) -> Called by the C++ application to create a new preset, using typetemplate as a template.

        @param: string - Preset name
        @return: hiero.core.TaskPreset instance as type template
        """
    def createAndExecuteProcessor(self, *args: Any, **kwargs: Any) -> Any:
        """self.createAndExecuteProcessor(hiero.core.TaskPreset, [hiero.core.ItemWrapper], string) -> Called by the C++ application to instantiate the Processor associated with specified preset and execute on the selected items.

        @param: hiero.core.TaskPreset
        @param: list of items for export
        @param: name of submission object used for dispatching job to renderfarm
        """
    def discardPresetChanges(self, *args: Any, **kwargs: Any) -> Any:
        """self.startPresetChanges(hiero.core.Project) -> Discard any changes to the presets since startPresetChanges() was called.

        @param: hiero.core.Project)
        """
    def loadPresets(self, string: Any) -> Any:
        """self.loadPresets(string) -> Called by the C++ application to load presets from a specified path.

        @param: path as string
        """
    def localPresets(self, *args: Any, **kwargs: Any) -> Any:
        """self.projectPresets() -> Returns a list of local presets assigned to the specified Project.

        @return: list of TaskPreset instances
        """
    def localPresetsChanged(self) -> Any:
        """self.localPresetsChanged() -> Called by the C++ application to check whether local presets have changed since last save.

        @return: bool changed state
        """
    def nukeShotExportPresets(self, *args: Any, **kwargs: Any) -> Any:
        """self.nukeShotExportPresets(hiero.core.Project) -> Get a list of presets which are contain Nuke shot exports.

        @return: list of TaskPreset instances
        """
    def presetFromXml(self, string: Any) -> Any:
        """self.presetFromXml(string) -> Called by the C++ application to ask the TaskRegistry to deserialize a Task preset from xml.

        @param: string - Preset XML
        @return: hiero.core.TaskPreset instance
        """
    def presetToPrettyXml(self, *args: Any, **kwargs: Any) -> str:
        """self.presetToPrettyXml(hiero.core.TaskPreset) -> Called by the C++ application to ask the TaskRegistry to serialize a Task preset to human friendly formatted xml.

        @param: hiero.core.TaskPreset instance
        @return: string - Preset XML
        """
    def presetToXml(self, *args: Any, **kwargs: Any) -> str:
        """self.presetToXml(hiero.core.TaskPreset) -> Called by the C++ application to ask the TaskRegistry to serialize a Task preset to xml.

        @param: hiero.core.TaskPreset instance
        @return: string - Preset XML
        """
    def presetsSubDirectory(self) -> Any:
        """self.presetsSubDirectory() -> Get the sub-directory in the plugin paths to search for presets."""
    def projectDuplicated(self, *args: Any, **kwargs: Any) -> Any:
        """projectDuplicated(hiero.core.Project, hiero.core.Project) -> Called by the C++ application to notify the TaskRegistry that a project has been duplicated and its associated Presets should be duplicated and assigned to the new project.

        @param: hiero.core.Project - original project
        @param: hiero.core.Project - new project
        """
    def projectExportHistoryXml(self, *args: Any, **kwargs: Any) -> Any:
        """self.projectExportHistoryXml(hiero.core.Project) -> Returns a list of XML fragments containing the project export history.

        @param hiero.core.Project: project
        @return: list of strings
        """
    def projectPresets(self, *args: Any, **kwargs: Any) -> Any:
        """self.projectPresets(hiero.core.Project) -> Returns a list of project presets assigned to the specified Project.

        @param: hiero.core.Project
        @return: list of TaskPreset instances
        """
    def projectPresetsChanged(self, *args: Any, **kwargs: Any) -> Any:
        """self.projectPresetsChanged(hiero.core.Project) -> Called by the C++ application to check whether project presets have changed since project last save.

        @param: hiero.core.Project
        """
    def projectUnloaded(self, *args: Any, **kwargs: Any) -> Any:
        """self.projectUnloaded(hiero.core.Project) -> Called by the C++ application to notify the TaskRegistry that a project has been unloaded and its associated Presets should be released.

        @param: hiero.core.Project
        """
    def registerme(self) -> Any:
        """self.registerme() -> Called from python implimentation of TaskRegistry to register instance as the Application Task Registry."""
    def removeProcessorPreset(self, *args: Any, **kwargs: Any) -> Any:
        """self.removeProcessorPreset(hiero.core.TaskPreset) -> Called by the C++ application to remove a preset from the registry.

        @param: hiero.core.TaskPreset
        """
    def renameProcessorPreset(self, *args: Any, **kwargs: Any) -> Any:
        """self.renameProcessorPreset(hiero.core.TaskPreset, string) -> Called by the C++ application to rename a preset in the registry.

        @param: hiero.core.TaskPreset
        """
    def restoreProjectExportHistoryXml(self, *args: Any, **kwargs: Any) -> Any:
        """self.restoreProjectExportHistoryXml(hiero.core.Project, list) -> Restore the export history for a project.

        @param hiero.core.Project: project
        @param list: list of strings containing export history
        """
    def revertDefaultPresets(self, string: Any) -> Any:
        """self.revertDefaultPresets(string) -> Called by the C++ application reconstruct the default presets.

        @param: path as string
        """
    def savePresets(self, string: Any) -> Any:
        """self.savePresets(string) -> Called by the C++ application to save presets to a specified path.

        @param: path as string
        """
    def startPresetChanges(self, *args: Any, **kwargs: Any) -> Any:
        """self.startPresetChanges(hiero.core.Project) -> Called when the user might start editing the presets, so the changes can be reverted if necessary.

        @param: hiero.core.Project)
        """
    def submissionChanged(self, *args: Any, **kwargs: Any) -> Any:
        """self.submissionChanged(string, hiero.core.Project) -> Called by the C++ application when the submission choice changes in the Export Dialog.

        @param: submission name as a string
        """
    def submissionNames(self) -> Any:
        """self.submissionNames() -> Called by the C++ application to get a list of the available Submission objects. Submission objects are used to manage render farm renders.

        @return: list of name strings
        """
    def validateExport(self, *args: Any, **kwargs: Any) -> Any:
        """self.validateExport(hiero.core.TaskPreset, [hiero.core.ItemWrapper]) -> Called by the C++ application to determinate if preset and selected items have valid resolution according the application mode.
        A warning message will be shown in case of any invalid output resolution.

        @param: hiero.core.TaskPreset
        @param: list of items for export
        @return: An error string if disallowed, otherwise an empty string.
        """

class ITask:
    """ITask provides a simple interface for our C++ Application to access Python instances of TaskBase.

    This class should not be used directly; use hiero.core.TaskBase instead.
    """
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addToQueue(self) -> Any:
        """self.addToQueue() -> adds this task into the task queue."""
    def children(self) -> Any:
        """self.children() -> get a list of child tasks.  Note that this list should not change after addToQueue() has been called."""
    def clearError(self) -> Any:
        """self.clearError() -> clears the error or warning string for this task."""
    def destinationDescription(self) -> Any:
        """self.destinationDescription() -> Get the destination description."""
    def error(self) -> Any:
        """self.error() -> Get the error string if one has been set."""
    def finishTask(self) -> Any:
        """self.finishTask() -> called by Hiero to tell the Task to that it's finished. Subclasses should finish processing in their override of this method (close files, clean up)."""
    def forcedAbort(self) -> Any:
        """self.forcedAbort() -> called by Hiero when the user presses the Abort button. Subclasses should do any clean up in their override of this method."""
    def formatDescription(self) -> Any:
        """self.formatDescription() -> Get a description of the format that this task writes to."""
    def getExportDuration(self) -> Any:
        """self.getExportDuration() -> Return the time this task took to export in milliseconds. Will return 0 until the task has finished exporting."""
    def ident(self) -> Any:
        """self.ident() -> called by Hiero to get a unique identifier for this task."""
    def progress(self) -> Any:
        """self.progress() -> called by Hiero to find out from the task what it's progress is, between 0.0 and 1.0."""
    def runOnMainThread(self) -> Any:
        """self.runOnMainThread() -> check if the task needs to be run on the main thread. Tasks which require this should override this method. If True is returned, taskStep() will always be called from the main thread."""
    def setDestinationDescription(self, desc: str) -> Any:
        """self.setDestinationDescription(desc) -> 

        @param desc: string
        """
    def setDuplicate(self) -> Any:
        """self.setDuplicate() -> Sets the flag cancelling this task and marking as duplicate."""
    def setError(self, desc: Any) -> Any:
        """self.setError(desc) -> sets the error string displayed to the user in the task dialog. Error strings display in red.

        @param desc: the text to display
        """
    def setExportDuration(self, *args: Any, **kwargs: Any) -> Any:
        """For internal use only. Do not use."""
    def setFormatDescription(self, desc: Any) -> Any:
        """self.setFormatDescription(desc) -> tells Hiero a description of the format that this task writes to.

        @param desc: description of the format that this task outputs
        """
    def setSynchronous(self) -> Any:
        """self.setSynchronous() -> Flags this task as synchronous. When added to the queue, this task will be executed imediately on the current thread. The Flag must be set prior to adding to queue"""
    def setTaskDescription(self, description: Any) -> Any:
        """self.setTaskDescription(description) -> tells Hiero a descriptive string for the task that it can use to show the user through the user interface and/or store it for reference. Helpful when debugging.

        @param desc: description of the task
        """
    def setWarning(self, desc: Any) -> Any:
        """self.setWarning(desc) -> sets the warning string displayed to the user in the task dialog. Warning strings display in orange.

        @param desc: the text to display
        """
    def startTask(self) -> Any:
        """self.startTask() -> called by Hiero to tell the Task to start. Subclasses should start processing in their override of this method."""
    def synchronous(self) -> Any:
        """self.synchronous() -> Returns the state of the Synchronous flag. If True, wheb added to the queue, this task will be executed imediately on the current thread."""
    def taskDescription(self) -> Any:
        """self.taskDescription() -> Get a description of the task."""
    def taskStep(self) -> Any:
        """self.taskStep() -> called by Hiero repeatedly until the progress method returns 1.0 or greater. Step based processing should occur in this method by subclasses of Task."""

class ITaskPreset:
    """ITaskPreset provides a simple interface for our C++ Application to access Python instances of TaskPreset.

    This class should not be used directly; use hiero.core.TaskPresetBase instead.
    """
    class ItemTypes(_enum.IntEnum):
        kAllItems: ITaskPreset.ItemTypes
        kAudioTrackItem: ITaskPreset.ItemTypes
        kClip: ITaskPreset.ItemTypes
        kSequence: ITaskPreset.ItemTypes
        kTrackItem: ITaskPreset.ItemTypes
        def __new__(cls, value: Any) -> Self: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def getResolveEntryCount(self) -> Any:
        """self.getResolveEntryCount() -> called by Hiero to get the number of resolve tokens available on this TaskPreset."""
    def ident(self) -> Any:
        """self.ident() -> called by Hiero to get a unique identifier for the Task related to this TaskPreset."""
    def isDeprecated(self) -> bool:
        """self.isDeprecated() -> returns whether or not this task preset is using a deprecated configuration.

        @return: True or False
        """
    def markedForDeletion(self) -> Any:
        """self.markedForDeletion() -> called by Hiero to check if the preset is marked for deletion."""
    def name(self) -> Any:
        """self.name() -> called by Hiero to get the preset name."""
    def project(self) -> Any:
        """self.project() -> called by Hiero to discover which Project (if any), this preset is assigned to"""
    def readOnly(self) -> Any:
        """self.readOnly() -> called by Hiero to discover if this preset is marked ReadOnly."""
    def resolveEntryDescription(self) -> Any:
        """self.resolveEntryDescription() -> called by Hiero to get a resolve token description by index."""
    def resolveEntryName(self) -> Any:
        """self.resolveEntryName() -> called by Hiero to get a resolve token ({shot}) by index."""
    def setMarkedForDeletion(self) -> Any:
        """self.setMarkedForDeletion() -> called by Hiero to mark this preset for deletion. The delete is not performed until presets are saved."""
    def setProject(self) -> Any:
        """self.setProject() -> called by Hiero to assign a preset to a Project."""
    def setReadOnly(self) -> Any:
        """self.setReadOnly() -> called by Hiero to mark this preset as ReadOnly."""
    def summary(self) -> Any:
        """self.summary() -> called by Hiero to get the preset description."""
    def supportedItems(self) -> Any:
        """self.supportedItems() -> called by Hiero to establish what types of object this export task operates on (Clips, Sequences, TrackItems)."""
    def supportsAudio(self) -> bool:
        """self.supportsAudio() -> returns whether or not this task preset supports audio.

        @return: True or False
        """

class ItemWrapper:
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def bin(self) -> Bin:
        """self.bin() -> converts this ItemWrapper to a hiero.core.Bin object. If the item wrapper isn't wrapping a Bin object, it will return a non-functioning (isNull returns True) TrackItem object (meaning that it has all of the methods of a Bin object, but the methods don't do anything)

        @return: hiero.core.Bin object
        """
    def binItem(self) -> BinItem:
        """self.binItem() -> converts this ItemWrapper to a hiero.core.BinItem object. If the item wrapper isn't wrapping a BinItem object, it will return a non-functioning (isNull returns True) TrackItem object (meaning that it has all of the methods of a BinItem object, but the methods don't do anything)

        @return: hiero.core.BinItem object
        """
    def clip(self) -> Clip:
        """self.clip() -> converts this ItemWrapper to a hiero.core.Clip object. If the item wrapper isn't wrapping a Clip object, it will return a non-functioning (isNull returns True) Clip object (meaning that it has all of the methods of a Clip object, but the methods don't do anything)

        @return: hiero.core.Clip object
        """
    def ignore(self, *args: Any, **kwargs: Any) -> Any: ...
    def isNull(self) -> bool:
        """self.isNull() -> returns True if this is a invalid or uninitialized item, or False otherwise

        @return: True or False
        """
    def item(self) -> Sequence | Clip | TrackItemBase | BinItem:
        """self.item() -> Return the item contained within this wrapper. 

        @return: hiero.core.Sequence | hiero.core.Clip | hiero.core.TrackItemBase | hiero.core.BinItem
        """
    def name(self) -> str:
        """self.name() -> Returns item name.

        @return: string
        """
    def root(self) -> Bin:
        """self.root() -> the root is the highest level in the bin selected for export, Root may be null. 

        @return: hiero.core.Bin object
        """
    def sequence(self) -> Sequence:
        """self.sequence() -> converts this ItemWrapper to a hiero.core.Sequence object. If the item wrapper isn't wrapping a Sequence object, it will return a non-functioning (isNull returns True) Sequence object (meaning that it has all of the methods of a Sequence object, but the methods don't do anything)

        @return: hiero.core.Sequence object
        """
    def setTrackItemsForViews(self, *args: Any, **kwargs: Any) -> Any: ...
    def trackItem(self) -> TrackItem:
        """self.trackItem() -> converts this ItemWrapper to a hiero.core.TrackItemBase object. If the item wrapper isn't wrapping a TrackItem object, it will return a non-functioning (isNull returns True) TrackItem object (meaning that it has all of the methods of a TrackItem object, but the methods don't do anything)

        @return: hiero.core.TrackItem object
        """
    def trackItemsForViews(self, *args: Any, **kwargs: Any) -> Any: ...

class Keys:
    kAssetEntityReference: str
    kClipComment: str
    kColorSpace: str
    kDDImageRootNodeName: str
    kEdlComments: str
    kEdlEditNumber: str
    kEdlEditString: str
    kEdlEffect: str
    kEdlMode: str
    kEdlName: str
    kEdlRetime: str
    kEdlSourceReel: str
    kEdlSrcIn: str
    kEdlSrcOut: str
    kEdlSrcTimecode: str
    kEdlTimelineIn: str
    kEdlTimelineOut: str
    kMXFPreferredTransfer: str
    kMediaAudioChannels: str
    kMediaDuration: str
    kMediaForceTimecode: str
    kMediaFramerate: str
    kMediaFramerateIsNtsc: str
    kMediaHeight: str
    kMediaIsStillFrame: str
    kMediaMasterMediaType: str
    kMediaMediaType: str
    kMediaName: str
    kMediaSamplerate: str
    kMediaStartTime: str
    kMediaTapeName: str
    kMediaTimecode: str
    kMediaUmid: str
    kMediaUrl: str
    kMediaWidth: str
    kNukePixelEncodingMatrix: str
    kPlayerTrack: str
    kQuickTimeColourspace: str
    kQuickTimeGamma: str
    kQuickTimePixelEncoding: str
    kQuickTimePreferredMatrix: str
    kQuickTimePreferredTransfer: str
    kReadParams: str
    kSourceAudioBitDepth: str
    kSourceBitmapSize: str
    kSourceDuration: str
    kSourceFormat: str
    kSourceFramerate: str
    kSourceGamma: str
    kSourceHasDefaultView: str
    kSourceHeight: str
    kSourceInputColourTransform: str
    kSourceLayers: str
    kSourceNumAudioChannels: str
    kSourceNumSamples: str
    kSourceOriginalSamplerate: str
    kSourcePixelAspectRatio: str
    kSourceReelId: str
    kSourceSamplerate: str
    kSourceShootTime: str
    kSourceShortFileName: str
    kSourceSize: str
    kSourceStartTime: str
    kSourceTimecode: str
    kSourceTimecodeDropFrame: str
    kSourceUmid: str
    kSourceViewUnspecifiedPostfix: str
    kSourceViewUnspecifiedPrefix: str
    kSourceViews: str
    kSourceViewsDelimiter: str
    kSourceWidth: str
    kTimelineAudioSynced: str
    kTimelineAutoDiskCacheMode: str
    kTimelineDuration: str
    kTimelineFramerate: str
    kTimelineIn: str
    kTimelineName: str
    kTimelineOut: str
    kTimelineOutputFormat: str
    kTimelineOverrideOutputFormat: str
    kTimelinePoster: str
    kTimelinePosterLayer: str
    kTimelineSamplerate: str
    kTrackBlendEnabled: str
    kTrackBlendMode: str
    kTrackDuration: str
    kTrackEnabled: str
    kTrackLocked: str
    kTrackMaskBlendEnabled: str
    kTrackVolume: str
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""

class MediaFileInfo:
    """Object representing a single set of media files on disk. """
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def endFrame(self) -> Any:
        """self.endFrame() -> returns the last frame of the media source contained by this object. Note that for video formats (mov, r3d), this will always be the media's (duration - 1).

        @return: integer frame
        """
    def filename(self) -> str:
        """self.filename() -> returns a path to a media source on disk. May represent multiple files, as with image sequences. The form will be one of the following, depending on the file extension of the media:
        * /somepath/file.mov
        * /somepath/imagesequence.######.dpx (1-40)

        In the case of the image sequence above, the numbers between the brackets represent the first and last frame of the sequence.

        @return: string
        """
    def startFrame(self) -> Any:
        """self.startFrame() -> returns the first frame of the media source contained by this object. Note that for video formats (mov, r3d), this will always be 0.

        @return: integer frame
        """

class MediaSource:
    """Represents a media source."""
    class MediaType(_enum.IntEnum):
        kAudio: MediaSource.MediaType
        kVideo: MediaSource.MediaType
        def __new__(cls, value: Any) -> Self: ...
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def associatedFilePaths(self) -> list:
        """self.associatedFilePaths() -> Return a list of file paths associated with the 'main' file, this is used with r3d clips where there are multiple r3ds in sequence, or rmd files.

        @return: list of path strings
        """
    @staticmethod
    def createOfflineVideoMediaSource() -> Any:
        """MediaSource.createOfflineVideoMediaSource() -> returns a media source that might be an offline video file. Use this to explicitly set what you expect the start, duration and framerate of the video source to be, once it becomes available.
        Raises a RuntimeError if the source path exists but could not be read by Hiero.

        @param path: path to where the media will eventually be
        @param start: start of the media, in frames
        @param duration: duration of the media, in frames
        @param frameRate: TimeBase representing the frame rate of the media source
        @param startTimecode: start timecode of the media
        @return: Created MediaSource
        """
    def duration(self) -> int:
        """self.duration() -> returns the duration, in frames.

        @return: frames
        """
    def fileinfos(self) -> list[MediaFileInfo]:
        """self.fileinfos() -> returns a tuple of hiero.core.MediaFileInfo objects, which can be used to retrieve all of the file fragments that are used by this MediaSource.

        @return: tuple of hiero.core.MediaFileInfo objects
        """
    def filename(self) -> str:
        """self.filename() -> returns the file name (and just the file name) of the first file used for the MediaSource.

        Deprecated; Please use the fileinfos() method instead.

        @return: string
        """
    def filenameHead(self) -> str:
        """self.filenameHead() -> returns the portion of filename before the frame index for an image sequence.

        @return: string
        """
    def filenamePadding(self) -> int:
        """self.filenameHead() -> returns the number characters used for frame index. -1 if not an image sequence.

        @return: int
        """
    def firstpath(self) -> str:
        """self.firstpath() -> returns the full path of the first file used for the MediaSource.
        Deprecated; Please use the fileinfos() method instead.

        @return: string
        """
    def fragmentFilename(self, fragmentIndex: Any) -> str:
        """self.fragmentFilename(fragmentIndex) -> returns the file name (and just the file name) for the fragment of the MediaSource, specified by the fragmentIndex.
        Deprecated; Please use the fileinfos() method instead

        @param fragmentIndex: index of the fragment to retrieve
        @return: string
        """
    def fragmentPath(self, fragmentIndex: Any) -> str:
        """self.fragmentPath(fragmentIndex) -> returns the full path for the fragment of the MediaSource, specified by the fragmentIndex.
        Deprecated; Please use the fileinfos() method instead.

        @param fragmentIndex: index of the fragment to retrieve
        @return: string
        """
    def hasAudio(self) -> bool:
        """self.hasAudio() -> True if the source has audio.

        @return: True or False
        """
    def hasVideo(self) -> bool:
        """self.hasVideo() -> True if the source has video.

        @return: True or False
        """
    def height(self) -> int:
        """self.height() -> returns the height of the media.

        @return: int
        """
    def isMediaPresent(self) -> bool:
        """self.isMediaPresent() -> returns True if the media is present.

        @return: True or False
        """
    def isNull(self) -> bool:
        """self.isNull() -> True if the object points to an invalid source, False otherwise.

        @return: True or False
        """
    def isOffline(self) -> bool:
        """self.isOffline() -> returns True if the media is missing or unavailable for any reason.

        @return: True or False
        """
    def metadata(self) -> DataCollection:
        """self.metadata() -> returns a hiero.core.Metadata object with metadata for the MediaSource.

        @return: hiero.core.Metadata object
        """
    def numChannels(self, arg1: Any, /) -> Any: ...
    def numFragments(self) -> int:
        """self.numFragments() -> returns the number of files used by this MediaSource, or -1 for invalid media. For instance, for mov files, this will return 1; for exr sequences this method will return the number of exr files in the sequence.
        Deprecated; Please use the fileinfos() method instead.

        @return: int
        """
    def pixelAspect(self) -> float:
        """self.pixelAspect() -> returns the pixel aspect ratio of the media.

        @return: float
        """
    def refresh(self) -> Any:
        """self.refresh() -> updates source info for latest changes in underlying files but doesn't update the frame range"""
    def singleFile(self) -> bool:
        """self.singleFile() -> returns True if this MediaSource is comprised of only a single file regardless of how many frames it contains (like a .mov or .r3d).

        @return: True or False
        """
    def startTime(self) -> int:
        """self.startTime() -> returns the start time of the media.

        @return: int
        """
    def timecodeStart(self) -> int: ...
    def toString(self, includeMetadata: bool = ...) -> str:
        """self.toString(includeMetadata=False) -> returns a string with info for the MediaSource. str(object) is equivalent to object.toString().

        @param includeMetadata: True adds metadata to the string, False does not
        @return: string
        """
    def width(self) -> int:
        """self.width() -> returns the width of the media.

        @return: int
        """

class NamingScheme:
    """Utility object for extracting names for clips, versions and objects out of clip objects"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def clipName(clip: Any) -> str:
        """self.clipName(clip) -> extracts name from clip that will be used for displaying the clip object, based on the underlying file(s).
        Redefine this method if desired for customized naming schema. Use default_clipName for default functionality if needed.

        @param clip: a clip to extract the name from
        @return: string
        """
    @staticmethod
    def default_clipName(clip: Any) -> str:
        """self.default_clipName(clip) -> extracts name from clip that will be used for displaying the clip object, based on the underlying file(s).
        Do not redefine this method. It preserves accessibility to default functionality when redefining clipName.

        @param clip: a clip to extract the name from
        @return: string
        """
    @staticmethod
    def default_rootName(clip: Any) -> str:
        """self.default_rootName(clip) -> extracts name from clip that will be used for displaying the bin item object, based on the underlying file(s).
        Do not redefine this method. It preserves accessibility to default functionality when redefining rootName.

        @param clip: a clip to extract the name from
        @return: string
        """
    @staticmethod
    def default_trackItemName(clip: Any) -> str:
        """self.default_trackItemName(clip) -> extracts name from clip that will be used for naming track items when added to a sequence.
        Do not redefine this method. It preserves accessibility to default functionality when redefining trackItemName.

        @param clip: a clip to extract the name from
        @return: string
        """
    @staticmethod
    def default_versionName(clip: Any) -> str:
        """self.default_versionName(clip) -> extracts name from clip that will be used for displaying the version object, based on the underlying file(s).
        Do not redefine this method. It preserves accessibility to default functionality when redefining versionName.

        @param clip: a clip to extract the name from
        @return: string
        """
    @staticmethod
    def rootName(clip: Any) -> str:
        """self.rootName(clip) -> extracts name from clip that will be used for displaying the bin item object, based on the underlying file(s).
        Redefine this method if desired for customized naming schema. Use default_rootName for default functionality if needed.

        @param clip: a clip to extract the name from
        @return: string
        """
    @staticmethod
    def trackItemName(clip: Any) -> str:
        """self.trackItemName(clip) -> extracts name from clip that will be used for naming track items when added to a sequence.
        Redefine this method if desired for customized naming schema. Use default_trackItemName for default functionality if needed.

        @param clip: a clip to extract the name from
        @return: string
        """
    @staticmethod
    def versionName(clip: Any) -> str:
        """self.versionName(clip) -> extracts name from clip that will be used for displaying the version object, based on the underlying file(s).
        Redefine this method if desired for customized naming schema. Use default_versionName for default functionality if needed.

        @param clip: a clip to extract the name from
        @return: string
        """

class PaintBlendMode(_enum.IntEnum):
    ColorBurn: PaintBlendMode
    ColorDodge: PaintBlendMode
    Difference: PaintBlendMode
    Exclusion: PaintBlendMode
    From: PaintBlendMode
    HardLight: PaintBlendMode
    LinearBurn: PaintBlendMode
    LinearDodge: PaintBlendMode
    Max: PaintBlendMode
    Min: PaintBlendMode
    Minus: PaintBlendMode
    Multiply: PaintBlendMode
    Over: PaintBlendMode
    Overlay: PaintBlendMode
    Plus: PaintBlendMode
    Screen: PaintBlendMode
    SoftLight: PaintBlendMode
    def __new__(cls, value: Any) -> Self: ...

class PaintObjectType(_enum.IntEnum):
    Burn: PaintObjectType
    Clone: PaintObjectType
    Dodge: PaintObjectType
    Eraser: PaintObjectType
    Paint: PaintObjectType
    ShapeArrow: PaintObjectType
    ShapeRectangle: PaintObjectType
    Text: PaintObjectType
    VanishingBrush: PaintObjectType
    def __new__(cls, value: Any) -> Self: ...

class PaintProperties:
    """Paint properties for annotation paint objects. Initialized with a PaintObjectType value, for example:

        eraserProperties = PaintProperties(PaintObjectType.Eraser)

    Depending on the paint object type some properties may not be supported, e.g. the Eraser does not support a color.
    Trying to set invalid properties or types will cause an exception to be raised.
    """
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def blendMode(self) -> PaintBlendMode:
        """self.blendMode() -> Get the blend mode for the brush

        @return: PaintBlendMode
        """
    def borderEnabled(self, *args: Any, **kwargs: Any) -> Any: ...
    def brushType(self) -> Any:
        """Deprecated. Use paintObjectType() instead."""
    def color(self) -> Any:
        """self.color() -> Get the color for the brush

        @return PySide6.QtGui.QColor
        """
    def fillColor(self, *args: Any, **kwargs: Any) -> Any: ...
    def fillEnabled(self, *args: Any, **kwargs: Any) -> Any: ...
    def get(self, property: Any) -> Any:
        """self.get(property) -> Get the value for a PaintProperty"""
    def hash(self, *args: Any, **kwargs: Any) -> Any: ...
    def isReadOnly(self, property: Any) -> Any:
        """self.isReadOnly(property) -> Check if a PaintProperty is supported and is read only for the current paint object type"""
    def isWritable(self, property: Any) -> Any:
        """self.isWritable(property) -> Check if a PaintProperty is supported and can be updated for the current paint object type"""
    def lineHardness(self) -> float:
        """self.lineHardness() -> Get the line hardness for the brush

        @return: float
        """
    def lineOpacity(self) -> float:
        """self.lineOpacity() -> Get the line opacity for the brush

        @return: float
        """
    def lineWidth(self) -> float:
        """self.lineWidth() -> Get the line width for the brush

        @return: float
        """
    def paintObjectType(self) -> PaintObjectType:
        """self.paintObjectType() -> Get the brush type

        @return: PaintObjectType
        """
    def pressureAffectsLineHardness(self) -> bool:
        """self.pressureAffectsLineHardness() -> Get whether pen pressure affects the line hardness of the brush

        @return: boolean
        """
    def pressureAffectsLineOpacity(self) -> bool:
        """self.pressureAffectsLineOpacity() -> Get whether pen pressure affects the opacity of the brush

        @return: boolean
        """
    def pressureAffectsLineWidth(self) -> bool:
        """self.pressureAffectsLineWidth() -> Get whether pen pressure affects the line width of the brush

        @return: boolean
        """
    def set(self, property: Any, value: Any) -> Any:
        """self.set(property, value) -> Set a PaintProperty to a given value. The allowed types for value depend on the property"""
    def setBlendMode(self, blendMode: Any) -> Any:
        """self.setBlendMode(blendMode) -> Set the PaintBlendMode for the brush"""
    def setBorderEnabled(self, *args: Any, **kwargs: Any) -> Any: ...
    def setColor(self, color: Any) -> Any:
        """self.setColor(color) -> Set the PySide6.QtGui.QColor for the brush"""
    def setFillColor(self, *args: Any, **kwargs: Any) -> Any: ...
    def setFillEnabled(self, *args: Any, **kwargs: Any) -> Any: ...
    def setLineHardness(self, hardness: Any) -> Any:
        """self.setLineHardness(hardness) -> Set the line hardness for the brush. Value must be in the range 0-1"""
    def setLineOpacity(self, opacity: Any) -> Any:
        """self.setLineOpacity(opacity) -> Set the line opacity for the brush. Value must be in the range 0-1"""
    def setLineWidth(self, width: Any) -> Any:
        """self.setLineWidth(width) -> Set the line width for the brush. Value must be > 1"""
    def setPressureAffectsLineHardness(self, on: Any) -> Any:
        """self.setPressureAffectsLineHardness(on) -> Set whether pen pressure affects the line hardness of the brush"""
    def setPressureAffectsLineOpacity(self, on: Any) -> Any:
        """self.setPressureAffectsLineOpacity(on) -> Set whether pen pressure affects the opacity of the brush"""
    def setPressureAffectsLineWidth(self, on: Any) -> Any:
        """self.setPressureAffectsLineWidth(on) -> Set whether pen pressure affects the line width of the brush"""
    def setSource(self, source: Any) -> Any:
        """self.setSource(source) -> Set the PaintSource"""
    def setSourceOffset(self, *args: Any, **kwargs: Any) -> Any: ...
    def source(self) -> PaintSource:
        """self.source() -> Get the source for the brush

        @return: PaintSource
        """
    def sourceOffset(self, *args: Any, **kwargs: Any) -> Any: ...
    def supports(self, property: Any) -> Any:
        """self.supports(property) -> Check if a PaintProperty is supported by the current paint object type. PaintProperty may be ReadOnly or ReadWrite, use isReadOnly and isWritable to check."""

class PaintProperty(_enum.IntEnum):
    BlendMode: PaintProperty
    BorderEnabled: PaintProperty
    Color: PaintProperty
    FillColor: PaintProperty
    FillEnabled: PaintProperty
    LineHardness: PaintProperty
    LineOpacity: PaintProperty
    LineWidth: PaintProperty
    PressureAffectsLineHardness: PaintProperty
    PressureAffectsLineOpacity: PaintProperty
    PressureAffectsLineWidth: PaintProperty
    Source: PaintProperty
    SourceOffset: PaintProperty
    def __new__(cls, value: Any) -> Self: ...

class PaintSource(_enum.IntEnum):
    Background: PaintSource
    Color: PaintSource
    Foreground: PaintSource
    def __new__(cls, value: Any) -> Self: ...

class Project:
    """Object for manipulating projects. Can be created using hiero.core.newProject() or by the following code:
    hiero.core.openProject(projectPath)
    project = hiero.core.projects()[-1]
    """
    class OpenFlags(_enum.IntEnum):
        kProjectOpenDontAddToRecent: Project.OpenFlags
        kProjectOpenNoFlags: Project.OpenFlags
        kProjectOpenShowDialogs: Project.OpenFlags
        kProjectOpenStartup: Project.OpenFlags
        def __new__(cls, value: Any) -> Self: ...
    class PosterFrameSetting(_enum.IntEnum):
        eCustom: Project.PosterFrameSetting
        eFirst: Project.PosterFrameSetting
        eLast: Project.PosterFrameSetting
        eMiddle: Project.PosterFrameSetting
        def __new__(cls, value: Any) -> Self: ...
    class SaveFlags(_enum.IntEnum):
        kProjectSaveAsShowFileDialog: Project.SaveFlags
        kProjectSaveDontAddToRecent: Project.SaveFlags
        kProjectSaveDontChangeProjectPath: Project.SaveFlags
        kProjectSaveKeepName: Project.SaveFlags
        kProjectSaveNoFlags: Project.SaveFlags
        def __new__(cls, value: Any) -> Self: ...
    kAllProjects: int
    kStartupProjects: int
    kUserProjects: int
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def addView(self, name: str, color: Any = ...) -> bool:
        """addView(name, color) -> Appends a view to this project's list of views. Returns False if name is empty or a view already exists with the same name.

        @param name: string
        @param color: optional; string in the format #RGB, #RRGGBB, #RRRGGGBBB, #RRRRGGGGBBBB or a name from the list of colors defined in the list of SVG color keyword names
        @return: True or False
        """
    def audioTrackItems(self, partialName: str | None = ...) -> list[TrackItem]:
        """self.audioTrackItems(partialName) -> returns all audio track items in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.TrackItem objects.

        Example: finds all audio track items in a project with 30Sec in the name:

        trackItems = myProject.audioTrackItems('30Sec')
        """
    def audioTracks(self, partialName: str | None = ...) -> list[AudioTrack]:
        """self.audioTracks(partialName) -> returns all audio tracks in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.AudioTrack objects.

        Example: finds all audio tracks in a project with 30Sec in the name:

        tracks = myProject.audioTracks('30Sec')
        """
    def autosave(self) -> Any:
        """self.autosave() -> if the project has been modified create an autosave file"""
    def beginUndo(self, name: Any) -> UndoGroup:
        """self.beginUndo(name) -> starts a new undo action, which will group all other undo actions until self.endUndo() is called. Be aware that this method only works on the main thread, and will throw an exception otherwise.
        Note that for operations inside the undo to work Project.endUndo() must be called.  It is recommended that you use this in a with block to ensure that this happens.  For example:
          with project.beginUndo('My Undo'):
            // Undoable edits

        @return: UndoGroup object
        """
    def bins(self, partialName: str | None = ...) -> list[Bin]:
        """self.bins(partialName) -> returns all bins in a project. Searches recursively, so will return bins within other bins in the list.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.Bin objects.

        Example: finds all bins in a project with MyBin in the name:

        bins = myProject.bins('MyBin')
        """
    def buildTrackName(self) -> str:
        """buildTrackName() -> get default track name used when building vfx trackthis can be configured in the project settings dialog"""
    def cancelUndo(self) -> Any:
        """self.cancelUndo() -> cancels an undo action started previously by a call to self.beginUndo()."""
    def clearUnusedLocalFiles(self) -> Any:
        """clearUnusedLocalFiles() -> clear all localised files that are not in any currently open project. This requires localisation to be enabled"""
    def clips(self, partialName: str | None = ...) -> list[Clip]:
        """self.clips(partialName) -> returns all clips in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.Clip objects.

        Example: finds all clips in a project with 30Sec in the name:

        clips = myProject.clips('30Sec')
        """
    def clipsBin(self) -> Bin:
        """self.clipsBin() -> returns the bin object containing the top level clips, sequences and bins for this project.

        @return: hiero.core.Bin object
        """
    def close(self) -> Any:
        """self.close() -> closes the project. Be aware that this method will not save the project, even if changes have been made since the last save of the project."""
    def createExportWriteNode(self, *args: Any, **kwargs: Any) -> Any: ...
    def customExportDirectory(self) -> str:
        """self.customExportDirectory() -> Get the custom directory used for exports if useCustomExportDirectory() is set to True.

        @return: string
        """
    def deletable(self) -> bool:
        """self.deletable() -> returns True if the project can be deleted.

        @return: True or False
        """
    def deleteView(self, name: str) -> bool:
        """deleteView(name) -> Removes the view with the matching name from this project's list of views. Returns False if no matching view is found or if the view to be deleted is the only view in the project.
        @param name: string
        @return: True or False
        """
    def editable(self) -> bool:
        """self.editable() -> returns True if the project can be edited.

        @return: True or False
        """
    def endUndo(self) -> Any:
        """self.endUndo() -> ends an undo action started previously by a call to self.beginUndo(). This will put a new item into the Edit > Undo/Redo menu items."""
    def exportRootDirectory(self) -> str:
        """self.exportRootDirectory() -> The root directory to use for exports. This will return either self.projectDirectory(True) or self.customExportDirectory() depending on the self.useCustomExportDirectory() setting.

        @return: string
        """
    def extractSettings(self) -> dict[str, str | bool]:
        """self.extractSettings() -> returns a dict of the project's settings.         @return: dict
    
        """
    def framerate(self) -> TimeBase:
        """framerate() -> project's default framerate for new sequences

        @return: TimeBase
        """
    def guid(self) -> str: ...
    def heroView(self) -> str:
        """heroView() -> Get the name of the hero view set on the project
        @return: str
        """
    def isLocalisationEnabled(self) -> bool:
        """isLocalisationEnabled() -> return whether localisation is enabled

        @return: whether localisation is enabled
        """
    def isNull(self) -> bool:
        """self.isNull() -> returns False if this is a valid Project object, True otherwise.

        @return: True or False
        """
    def isRestricted(self) -> bool:
        """self.isRestricted() -> returns whether or not access to the project is restricted.

        @return: True or False
        """
    def lutSetting16Bit(self) -> str:
        """self.lutSetting16Bit() -> returns the project's 16 bit lut setting name.

        @return: string
        """
    def lutSetting8Bit(self) -> str:
        """self.lutSetting8Bit() -> returns the project's 8 bit lut setting name.

        @return: string
        """
    def lutSettingFloat(self) -> str:
        """self.lutSettingFloat() -> returns the project's float lut setting name.

        @return: string
        """
    def lutSettingLog(self) -> str:
        """self.lutSettingLog() -> returns the project's log lut setting name.

        @return: string
        """
    def lutSettingMonitorOut(self) -> str:
        """self.lutSettingMonitorOut() -> returns the project's Monitor Out lut setting name.

        @return: string
        """
    def lutSettingThumbnail(self) -> str:
        """self.lutSettingThumbnail() -> returns the project's Thumbnail lut setting name.

        @return: string
        """
    def lutSettingViewer(self) -> str:
        """self.lutSettingsViewer() -> returns the project's viewer lut setting name.

        @return: string
        """
    def lutSettingWorkingSpace(self) -> str:
        """self.lutSettingWorkingSpace() -> returns the project's Working Space lut setting name.

        @return: string
        """
    def lutUseOCIOForExport(self) -> bool:
        """self.lutUseOCIOForExport() -> returns the project setting for using OCIO in nuke script export.

        @return: bool
        """
    def modifiedSinceLastSave(self) -> Any:
        """self.modifiedSinceLastSave() -> Check if the project has been modified since it was last saved"""
    def name(self) -> str:
        """self.name() -> returns the name of the project.

        @return: string
        """
    def ocioConfigName(self) -> str:
        """self.ocioConfigName() -> returns the ocio config name loaded by NukeStudio. When using a custom ocio config an empty string is returned.

        @return: string
        """
    def ocioConfigPath(self) -> str:
        """self.ocioConfigPath() -> returns the project settings for the ocio config path.

        @return: string
        """
    def outputFormat(self) -> Format:
        """outputFormat() -> gets project's default outputFormat for new sequences.

        @return: Format
        """
    def path(self) -> str:
        """self.path() -> returns the path to the project.

        @return: string
        """
    def posterFrameSettings(self) -> tuple:
        """posterFrameSettings() -> Get the poster frame settings used for clips added to the project.
        @return: tuple of poster frame setting and custom frame number
        """
    def projectDirectory(self) -> str:
        """self.projectDirectory() -> Get the project directory used for resolving relative paths and the exportRootDirectory() (if useCustomExportDirectory() is False).

        @param expanded: whether expressions in the path are expanded
        @return: string
        """
    def redo(self) -> Any:
        """self.redo() -> triggers a redo of the next item in the redo stack. Only works on the main thread. If called from any other thread, throws an exception."""
    def redoItemText(self) -> str:
        """self.redoItemText() -> returns the text of the next item on the redo stack. Only works on the main thread. Can be useful for testing that undo/redo works.

        @return: string
        """
    def save(self) -> Any:
        """self.save() -> saves a previously saved project to disk."""
    def saveAs(self, filename: Any) -> Any:
        """self.saveAs(filename) -> saves the project to the path specified by the filename parameter. Throws an exception if the project couldn't be saved for any reason.

        @param filename: path to save the project to
        """
    def sequences(self, partialName: str | None = ...) -> list[Sequence]:
        """self.sequences(partialName) -> returns all sequences in a project. User can filter by by partial name.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.
        @return: an array of hiero.core.Sequence objects.

        Example: finds all sequences in a project with 30Sec in the name:

        sequences = myProject.sequences('30Sec')
        """
    def setCustomExportDirectory(self) -> Any:
        """self.setCustomExportDirectory() -> Set the custom directory used for exports if useCustomExportDirectory() is set to True.

        @param path: path
        """
    def setDeletable(self, deletable: bool) -> Any:
        """self.setDeletable(deletable) -> sets whether or not a project can be deleted.

        @param deletable: True or False
        """
    def setEditable(self, editable: bool) -> Any:
        """self.setEditable(editable) -> sets whether or not a project can be edited.

        @param editable: True or False
        """
    def setFramerate(self, TimeBase: Any) -> Any:
        """setFramerate(TimeBase) -> sets project's default framerate for new sequences.This will persist when the application is restarted

        @param: TimeBase
        """
    def setHasMigratedSequenceProperties(self) -> Any:
        """setHasMigratedSequenceProperties() -> Mark the project as having had deprecated sequence properties converted into soft effects."""
    def setLocalisationEnabled(self) -> Any:
        """setLocalisationEnabled() -> set whether localisation is enabled. This will persist when the application is restarted.

        @param isEnabled: whether localisation should be enabled
        """
    def setModified(self) -> Any:
        """self.setModified() -> Set the project as modified even if just saved or loaded"""
    def setOcioConfigPath(self, path: Any) -> Any:
        """self.setOcioConfigPath(path) -> set the ocio config for the project"""
    @overload
    def setOutputFormat(self, format: Format) -> None:
        """setOutputFormat(Format) -> sets project's default output format for new sequences.
        setOutputFormat(width, height, pixelAspect, name) -> sets project's default output format for new sequences. This will persist when the application is restarted

        @param width: width for the output format
        @param height: height for the output format
        @param pixelAspect: float for pixel aspect ratio
        @param name: string for the format name
        """
    @overload
    def setOutputFormat(self, width: Any, height: Any, pixelAspect: Any, name: Any) -> None:
        """setOutputFormat(Format) -> sets project's default output format for new sequences.
        setOutputFormat(width, height, pixelAspect, name) -> sets project's default output format for new sequences. This will persist when the application is restarted

        @param width: width for the output format
        @param height: height for the output format
        @param pixelAspect: float for pixel aspect ratio
        @param name: string for the format name
        """
    def setPath(self, path: Any) -> Any:
        """self.setPath(path) -> set the path a project saves to without saving it"""
    def setPosterFrameSettings(self) -> Any:
        """setPosterFrameSettings() -> Set the poster frame settings used for clips added to the project.
        @param setting: the mode for setting poster frames
        @param customFrame: the frame number if mode is set to ePosterFrameCustom
        """
    def setProjectDirectory(self, string: Any) -> Any:
        """self.setProjectDirectory(string) -> Set the project directory used for resolving relative paths and the exportRootDirectory() (if useCustomExportDirectory() is False).

        @param path: the path or expression to set
        """
    def setShotPresetName(self) -> Any:
        """self.setShotPresetName() -> set the name of Shot Preset which is usedwhen sending to nuke or creating a comp.

        @param name:
        """
    def setShowViewColors(self) -> Any:
        """setShowViewColors() -> Set if colors set for views are shown in the UI."""
    def setStartTimecode(self, Time: Any) -> Any:
        """setStartTimecode(Time) -> sets project's default start timecode for new sequences. This will persist when the application is restarted

        @param startTime: TimeBase start timecode for sequence 
        """
    def setTimeDisplayFormat(self) -> Any:
        """setTimeDisplayFormat() -> sets project's default displayType for new sequences.  This will persist when the application is restarted

        @param displayType: DisplayType to use 
        """
    def setTrackItemReformatState(self) -> Any:
        """setTrackItemReformatState() -> Set the default ReformatState for new TrackItems created in this project"""
    def setTrackItemVersionsLinkedToBin(self, linked: Any) -> Any:
        """setTrackItemVersionsLinkedToBin(linked) -> Set whether track item versions are linked by default"""
    def setUseCustomExportDirectory(self) -> Any:
        """self.setUseCustomExportDirectory() -> Set if the export root directory should be a custom directory, or use the project directory.

        @param custom:
        """
    def setViews(self, views: Any) -> Any:
        """setViews(views) -> Set the project's views.
        @param views: this can be either a list of view names, or a list of tuples with (name, color)
        """
    def setViewsForStereo(self) -> Any:
        """setViewsForStereo() -> Replaces the project's views with two views named "left" and "right"."""
    def shotPresetName(self) -> str:
        """self.shotPresetName() -> get the name of Shot Preset which is usedwhen sending to nuke or creating a comp.

        @return: string
        """
    def showViewColors(self) -> Any:
        """showViewColors() -> Get if colors set for views are shown in the UI."""
    def startTimecode(self) -> int:
        """startTimecode() -> gets project's default start frame for new sequences.

        @return: Time
        """
    def tagsBin(self) -> Bin:
        """self.tagsBin() -> returns the bin object containing the top level tags for this project.

        @return: hiero.core.Bin object
        """
    def timeDisplayFormat(self) -> Timecode.DisplayType:
        """timeDisplayFormat() -> gets project's default displayType for new sequences. @return: DisplayType"""
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
    def trackItemReformatState(self) -> ReformatState:
        """trackItemReformatState() -> Get default ReformatState for new TrackItems created in this project"""
    def trackItemVersionsLinkedToBin(self) -> bool:
        """trackItemVersionsLinkedToBin() -> Get whether track item versions are linked by default"""
    def trackItems(self, partialName: str | None = ...) -> list[TrackItem]:
        """self.trackItems(partialName) -> returns all track items in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.TrackItem objects.

        Example: finds all track items in a project with 30Sec in the name:

        trackItems = myProject.trackItems('30Sec')
        """
    def tracks(self, partialName: str | None = ...) -> list[VideoTrack | AudioTrack]:
        """self.tracks(partialName) -> returns all tracks in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.VideoTrack and hiero.core.AudioTrack objects.

        Example: finds all tracks in a project with 30Sec in the name:

        tracks = myProject.tracks('30Sec')
        """
    def undo(self) -> Any:
        """self.undo() -> triggers an undo on the last item previously added to the undo stack. Only works on the main thread. If called from any other thread, throws an exception."""
    def undoItemText(self) -> str:
        """self.undoItemText() -> returns the text of the last item on the undo stack. Only works on the main thread. Can be useful for testing that undo/redo works.

        @return: string
        """
    def useCustomExportDirectory(self) -> bool:
        """self.useCustomExportDirectory() -> Get if the export root directory should be a custom directory, or use the project directory.

        @return: bool
        """
    @staticmethod
    def useOCIOEnvironmentOverride() -> bool:
        """self.useOCIOEnvironmentOverride() -> returns whether the OCIO config has been overriden in the environment.

        @return: bool
        """
    def videoTrackItems(self, partialName: str | None = ...) -> list[TrackItem]:
        """self.videoTrackItems(partialName) -> returns all video track items in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.TrackItem objects.

        Example: finds all video track items in a project with 30Sec in the name:

        trackItems = myProject.videoTrackItems('30Sec')
        """
    def videoTracks(self, partialName: str | None = ...) -> list[VideoTrack]:
        """self.videoTracks(partialName) -> returns all video tracks in a project.
        @param partialName: optional string with partial name to match against. Will match if this string is anywhere in the name.

        @return: an array of hiero.core.VideoTrack objects.

        Example: finds all video tracks in a project with 30Sec in the name:

        tracks = myProject.videoTracks('30Sec')
        """
    def views(self) -> list[str]:
        """views() -> Returns a list of this project's views.
        @return: list of strings
        """
    def viewsAndColors(self) -> list[tuple]:
        """viewsAndColors() -> Returns a list of this project's views and corresponding colors.
        @return: list of (str, PySide6.QtGui.QColor) tuples
        """

@final
class QIntList:
    def __delitem__(self, key: Any, /) -> None:
        """Delete self[key]."""
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __setitem__(self, key: Any, value: Any, /) -> None:
        """Set self[key] to value."""
    def append(self, *args: Any, **kwargs: Any) -> Any:
        """append"""
    def capacity(self, *args: Any, **kwargs: Any) -> Any:
        """capacity"""
    def clear(self, *args: Any, **kwargs: Any) -> Any:
        """clear"""
    def constData(self, *args: Any, **kwargs: Any) -> Any:
        """constData"""
    def data(self, *args: Any, **kwargs: Any) -> Any:
        """data"""
    def pop_back(self, *args: Any, **kwargs: Any) -> Any:
        """pop_back"""
    def pop_front(self, *args: Any, **kwargs: Any) -> Any:
        """pop_front"""
    def prepend(self, *args: Any, **kwargs: Any) -> Any:
        """prepend"""
    def push_back(self, *args: Any, **kwargs: Any) -> Any:
        """push_back"""
    def push_front(self, *args: Any, **kwargs: Any) -> Any:
        """push_front"""
    def removeFirst(self, *args: Any, **kwargs: Any) -> Any:
        """removeFirst"""
    def removeLast(self, *args: Any, **kwargs: Any) -> Any:
        """removeLast"""
    def reserve(self, *args: Any, **kwargs: Any) -> Any:
        """reserve"""

class ReformatState:
    """Object representing a the reformatting settings for a track item.  This corresponds to the Nuke 'Reformat' node."""
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def boxForceShape(self) -> bool:
        """self.boxForceShape() -> returns the box 'force shape' flag.

        @return: bool
        """
    def boxPAR(self) -> float:
        """self.boxPAR() -> returns the box pixel aspect ratio.

        @return: double
        """
    def boxSize(self) -> Any:
        """self.boxSize() -> returns the box size.

        @return: QSize
        """
    def copyFrom(self) -> Any:
        """self.copyFrom() -> Copy the properties from another ReformatState.

        @param: ReformatState
        """
    def isNull(self, *args: Any, **kwargs: Any) -> Any: ...
    def originalResizeFlip(self) -> bool:
        """self.originalResizeFlip() -> returns the original resize flip flag, which may be a deprecated value if it was loaded from an old project.

        @return: bool
        """
    def originalResizeFlop(self) -> bool:
        """self.originalResizeFlop() -> returns the original resize flop flag, which may be a deprecated value if it was loaded from an old project.

        @return: bool
        """
    def originalResizeTurn(self) -> bool:
        """self.originalResizeTurn() -> returns the original resize turn flag, which may be a deprecated value if it was loaded from an old project.

        @return: bool
        """
    def originalType(self) -> str:
        """self.originalType() -> returns the original reformat type of the state, which may be a deprecated value if it was loaded from an old project.

        @return: string
        """
    def resizeCenter(self) -> bool:
        """self.resizeCenter() -> returns the resize center flag.

        @return: bool
        """
    def resizeFlip(self) -> bool:
        """self.resizeFlip() -> returns the resize flip flag. Note: the flip option has been removed, this method should not be called.

        @return: bool
        """
    def resizeFlop(self) -> bool:
        """self.resizeFlop() -> returns the resize flop flag. Note: the flop option has been removed, this method should not be called.

        @return: bool
        """
    def resizeTurn(self) -> bool:
        """self.resizeTurn() -> returns the resize turn flag. Note: the turn option has been removed, this method should not be called.

        @return: bool
        """
    def resizeType(self) -> str:
        """self.resizeType() -> returns the resize type.

        @return: string
        """
    def scale(self) -> float:
        """self.scale() -> returns the scaling factor. Note: the scale option has been removed, this method should not be called.

        @return: double
        """
    def setBoxForceShape(self) -> Any:
        """self.setBoxForceShape() -> sets the box 'force shape' flag if the reformat type is set to 'to box'.

        @param setBoxForceShape: bool
        """
    def setBoxPAR(self) -> Any:
        """self.setBoxPAR() -> sets the box pixel aspect ratio if the reformat type is set to 'to box'.

        @param PAR: double
        """
    def setBoxSize(self) -> Any:
        """self.setBoxSize() -> sets the box size if the reformat type is set to 'to box'.

        @param size: QSize
        """
    def setResizeCenter(self) -> Any:
        """self.setResizeCenter() -> sets the resize center flag on the track item.

        @param center: bool
        """
    def setResizeFlip(self) -> Any:
        """self.setResizeFlip() -> the flip option has been removed, this method exists only for compatibility reasons"""
    def setResizeFlop(self) -> Any:
        """self.setResizeFlop() -> the flop option has been removed, this method exists only for compatibility reasons"""
    def setResizeTurn(self) -> Any:
        """self.setResizeTurn() -> the turn option has been removed, this method exists only for compatibility reasons"""
    def setResizeType(self) -> Any:
        """self.setResizeType() -> sets the resize type of the state.

        @param newResizeType: string
        """
    def setScale(self) -> Any:
        """self.setScale() -> the scale option has been removed, this method exists only for compatibility reasons"""
    def setType(self) -> Any:
        """self.setType() -> sets the reformat type of the state. Valid types are: 'Disabled' and 'To Format'.

        @param newType: string
        """
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
    def type(self) -> str:
        """self.type() -> returns the reformat type of the state.

        @return: string
        """

class RenderProgressObserver:
    """Observer for tracking the progress of renders on the frame server."""
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def isNull(self, *args: Any, **kwargs: Any) -> Any: ...
    def updateProgress(self) -> Any:
        """RenderProgressObserver.updateProgress() -> called on progress of frame renders
        @param progressList: list of lists containing [filePath, frame, progress]
        """

class Sequence(SequenceBase):
    """Object for Sequences."""
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def addClip(self, clip: Clip, time: float, videoTrackIndex: int = ..., audioTrackIndex: int = ...) -> list[TrackItem]:
        """Add a clip to a sequence, creating a TrackItem for each video/audio channel in the clip,
        adding them to the appropriate tracks and linking them together.  This has the same effect
        as dragging a clip from the Bin View to the Timeline View in the Hiero UI.

        @param clip: the clip to add
        @param time: the in time for created track items
        @param videoTrackIndex: index of the video track to add items to if the clip has video
        @param audioTrackIndex: index of the audio track to start adding items to if the clip has audio
        @return: list of created hiero.core.TrackItems
        """
    def addToNukeScript(self, script: _hiero_core_nuke_Script.ScriptWriter = ..., additionalNodes: Any = ..., additionalNodesCallback: Any = ..., includeRetimes: bool = ..., retimeMethod: Any = ..., offset: Any = ..., skipOffline: bool = ..., mediaToSkip: Any = ..., disconnected: bool = ..., masterTrackItem: Any = ..., includeEffects: bool = ..., outputToFormat: Any = ...) -> None:
        """addToNukeScript(self, script)
        @param script: Nuke script object to add nodes to.
        @param includeRetimes: True/False include retimes
        @param retimeMethod: "Motion", "Blend", "Frame" - Knob setting for OFlow retime method
        @param additionalNodesCallback: callback to allow custom additional node per item function([Clip|TrackItem|Track|Sequence])
        @param offset: Optional, Global frame offset applied across whole script
        @param skipOffline: If True, offline clips are not included in the export
        @param mediaToSkip: List of MediaSources which should be excluded from the export
        @param disconnected: If True, tracks other than that containing the masterTrackItem are not connected to any inputs
        @param masterTrackItem: Used for controlling the script output if disconnected is specified
        @param includeEffects: If True, soft effects are included in the exported script
        @param outputToFormat: Format to use for output.  If not specified, the sequence's own format is used.
        @return: None

        Add nodes representing this Sequence to the specified script.
        If there are no clips in the Sequence, nothing is added.
        """
    def addTrack(self, track: Any) -> Any:
        """self.addTrack(track) -> adds a video or audio track to the Sequence.

        @param track: video or audio track to add
        """
    def audioTrack(self, index: Any) -> AudioTrack:
        """self.audioTrack(index) -> returns the audio track for the specified index.

        @param index: index of the audio track to return
        @return: hiero.core.AudioTrack
        """
    def audioTracks(self) -> tuple[TrackBase, ...]:
        """self.audioTracks() -> returns a tuple with all of the audio tracks.

        @return: tuple of hiero.core.AudioTrack objects
        """
    def changeFramerateKeepFrames(self, toTimebase: Any) -> Any:
        """self.changeFramerateKeepFrames(toTimebase) -> changes the timebase of the sequence, keeping frames of track items the same

        @param toTimebase: timebase to change to
        """
    def changeFramerateKeepTimecodes(self, toTimebase: Any, roundingMode: Any) -> Any:
        """self.changeFramerateKeepTimecodes(toTimebase, roundingMode) -> changes the timebase of the sequence, keeping timecodes of track items the same, according to the specified rounding mode

        @param toTimebase: timebase to change to
        @param roundingMode: rounding mode to use when converting timebases (hiero.core.TimeBase.kRoundNearest, hiero.core.TimeBase.kRound32Pulldown)
        """
    def clone(*args, **kwargs: Any) -> Sequence:
        """self.clone() -> returns a deep copy of this object.

        @return: hiero.core.Sequence object

        WARNING - DEPRECATED ( clone ): This method is deprecated and will not be present in future versions of the Python API.
        This method has been replaced by copy().
        """
    def copy(self) -> Sequence:
        """self.copy() -> returns a deep copy of this object.

        @return: hiero.core.Sequence object
        """
    def deserialize(self) -> Any:
        """self.deserialize() -> restore the sequence state from XML data

        @param rangeMin: The beginning of the timeline range effected by this change
        @param rangeMax: The end of the timeline range effected by this change
        """
    def guid(self) -> str: ...
    def importTracks(self, filePath: Any) -> Any:
        """self.importTracks(filePath) -> imports all of the tracks from the file specified by the filePath argument.

        @param filePath: path to the file to import tracks from
        @return tracks: tuple of created tracks
        """
    def importTracksFromTimeBaseKeepFrames(self, filePath: Any, srcTimebase: Any) -> Any:
        """self.importTracksFromTimeBaseKeepFrames(filePath, srcTimebase) -> imports all of the tracks from the file specified by the filePath argument using the specified timebase.

        @param filePath: path to the file to import tracks from
        @param srcTimebase: timebase to use when reading the source file
        @return tracks: tuple of created tracks
        """
    def importTracksFromTimeBaseKeepTimecodes(self, filePath: Any, srcTimebase: Any, roundingMode: Any) -> Any:
        """self.importTracksFromTimeBaseKeepTimecodes(filePath, srcTimebase, roundingMode) -> imports all of the tracks from the file specified by the filePath argument using the specified timebase.

        @param filePath: path to the file to import tracks from
        @param srcTimebase: timebase to use when reading the source file
        @param roundingMode: rounding mode to use when converting timebases (hiero.core.TimeBase.kRoundNearest, hiero.core.TimeBase.kRound32Pulldown)
        @return tracks: tuple of created tracks
        """
    def items(self) -> tuple[VideoTrack | AudioTrack, ...]:
        """self.items() -> returns a tuple with all of the video tracks concatenated with all of the audio tracks. Can iterate over the video tracks first by using self.numVideoTracks. The audio tracks follow the video tracks in the tuple returned from this method.

        @return: tuple of hiero.core.VideoTrack and hiero.core.AudioTrack objects
        """
    def matchMedia(self, path: Any) -> Any:
        """self.matchMedia(path) -> match media using the current rule configuration in hiero.core.conformer().

        @param path: path to the folder with the media to connect
        """
    def numAudioTracks(self) -> int:
        """self.numAudioTracks() -> returns number of audio tracks contained by this sequence.

        @return: int
        """
    def numVideoTracks(self) -> int:
        """self.numVideoTracks() -> returns number of video tracks contained by this sequence.

        @return: int
        """
    def reconnectMedia(self, path: Any) -> Any:
        """self.reconnectMedia(path) -> For each of the Clips used by this Sequence, reconnects media found in the specified path.

        @param path: path containing media to reconnect to
        """
    def removeTrack(self, track: Any) -> Any:
        """self.removeTrack(track) -> removes the track from the Sequence.

        @param track: track to remove (hiero.core.AudioTrack or VideoTrack object)
        """
    def replaceClips(self, path: Any) -> Any:
        """self.replaceClips(path) -> For each of the TrackItems in this sequence, replace it's Clip with media found in the specified path.

        @param path: path containing media to replace with
        """
    def serialize(self) -> str:
        """self.serialize() -> serialize the sequence object to XML"""
    def trackItemAt(self, time: Any) -> TrackItem:
        """self.trackItemAt(time) -> returns the top-most video track item for the specified time that is enabled and has media.

        @param time: frame to get the trackitem for
        @return: hiero.core.TrackItem
        """
    def trackItemsAt(self, time: Any, mediaType: TrackItem = ...) -> Any:
        """self.trackItemsAt(time, mediaType) -> finds enabled track items for the specified time, ordered from top-track to bottom-track (or for audio, min channel to max channel).

        @param time: frame to get the trackitems for
        @param mediaType: TrackItem.MediaType value specifying the media type of the track items to look for (defaults to kVideo)
        @return: tuple of hiero.core.TrackItem objects
        """
    def videoTrack(self, index: Any) -> VideoTrack:
        """self.videoTrack(index) -> returns the video track for the specified index.

        @param index: index of the video track to return
        @return: hiero.core.VideoTrack
        """
    def videoTracks(self) -> tuple[VideoTrack, ...]:
        """self.videoTracks() -> returns a tuple with all of the video tracks.

        @return: tuple of hiero.core.VideoTrack objects
        """

class SequenceAutoDiskCacheMode(_enum.IntEnum):
    eAuto: SequenceAutoDiskCacheMode
    eDefault: SequenceAutoDiskCacheMode
    eManual: SequenceAutoDiskCacheMode
    eUnknown: SequenceAutoDiskCacheMode
    def __new__(cls, value: Any) -> Self: ...

class Snapshot:
    """Object representing a snapshot of a sequence or clip. Can be created with a Clip or a Sequence object."""
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def comment(self) -> str:
        """self.comment() -> returns the comment set on this snapshot object.

        @return: string
        """
    def isNull(self) -> bool:
        """self.isNull() -> returns True if the object is invalid, False otherwise.

        @return: True or False
        """
    def item(self) -> Clip | Sequence:
        """self.item() -> returns the clip or sequence stored with this snapshot.

        @return: hiero.core.Clip or hiero.core.Sequence object
        """
    def name(self) -> str:
        """self.name() -> returns the name of this snapshot.

        @return: string
        """
    def setComment(self, comment: Any) -> str:
        """self.setComment(comment) -> sets the comment on this snapshot object.

        @param comment: string to set the comment to
        @return: string
        """
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """

class Tag:
    """Object representing a tag in Hiero.
    Can be created with a string name, an optional path to an icon and an optional editable (in gui) boolean parameter
    """
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def copy(self, *args: Any, **kwargs: Any) -> Any: ...
    def guid(self) -> str:
        """self.guid() -> Return the Tag guid.

        @return: object guid as string
        """
    def icon(self) -> str:
        """self.icon() -> returns the tags icon path.
        If the file doesn't exist, it will search for it in the plugin paths and the project folder and return the located file.

        @return: string
        """
    def inTime(self) -> int:
        """self.inTime() -> returns the in time of the tag.

        @return: frame
        """
    def isNull(self) -> bool:
        """self.isNull() -> returns True if the tag is invalid, False otherwise.

        @return: True or False
        """
    def metadata(self) -> DataCollection:
        """self.metadata() -> returns the tag's metadata.

        @return: hiero.core.DataCollection object
        """
    def name(self) -> str:
        """self.name() -> returns the label of the tag.

        @return: string
        """
    def note(self) -> str:
        """self.note() -> returns the note on the tag.

        @return: string
        """
    def outTime(self) -> int:
        """self.outTime() -> returns the out time of the tag.

        @return: frame
        """
    def parentBin(self, *args: Any, **kwargs: Any) -> Any: ...
    def project(self) -> Project:
        """self.project() -> returns the Project object that this is attached to, or None if the object is not attached to a project.

        @return: hiero.core.Project object
        """
    def serialize(self) -> str: ...
    def setIcon(self) -> Any:
        """self.setIcon() -> sets the icon on the tag.

        @param note: path to icon file
        """
    def setInTime(self, time: Any) -> Any:
        """self.setInTime(time) -> set the in time of the tag.

        @param time: the in time
        """
    def setName(self) -> Any:
        """self.setName() -> sets the name label of the tag.

        @param name: name to assign to tag
        """
    def setNote(self) -> Any:
        """self.setNote() -> sets the note on the tag.

        @param note: string note to assign to tag
        """
    def setOutTime(self, time: Any) -> Any:
        """self.setOutTime(time) -> set the out time of the tag.

        @param time: the out time
        """
    def setVisible(self) -> Any:
        """self.setVisible() -> sets the visibility of the tag.

        @param visible: visibility state
        """
    def syncName(self, name: Any) -> Any:
        """self.syncName(name) -> set the name of the tag without sending additional notifications."""
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
    def visible(self) -> bool:
        """self.visible() -> gets the visibility state of the tag.

        @return: bool
        """

class TimeBase:
    """Helper object that wraps up time bases (or frame rates). Stores values internally as integer ratios, as opposed to floating point values.

    Can be initialised with an int, float, or str.  In addition, you can construct a TimeBase using TimeBase.fromRational(numerator, denominator), or use the predefined TimeBase values, for example TimeBase.k30NTSC.
    """
    class RoundingMode(_enum.IntEnum):
        kRound32Pulldown: TimeBase.RoundingMode
        kRoundNearest: TimeBase.RoundingMode
        def __new__(cls, value: Any) -> Self: ...
    k24: TimeBase
    k24NTSC: TimeBase
    k25: TimeBase
    k30: TimeBase
    k30NTSC: TimeBase
    k50: TimeBase
    k60: TimeBase
    k60NTSC: TimeBase
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    @staticmethod
    def convert(arg1: Any, arg2: Any, arg3: Any, /) -> int:
        """self.convert(t, from, to) -> returns the time specified by the first parameter converted from from parameter's time base into the to parameter's time base.
        If either of the time bases is invalid, this method returns the t parameter unchanged.

        @param t: the time (frame) to convert from one rate to another
        @param from: the time base to convert from
        @param to: the time base to convert to
        @return: integer
        """
    def convertTime(self, t: Any, toRate: Any) -> int:
        """self.convertTime(t, toRate) -> returns the time specified by the first parameter converted from this object's time base into the second parameter's time base.
        If either of the time bases is invalid, this method returns the t parameter unchanged.

        @param t: the time (frame) to convert from one rate to another
        @param toRate: the new time time to convert to
        @return: integer
        """
    def denominator(self) -> int:
        """self.denominator() -> gets the denominator of the time base.
        @return: int
        """
    @staticmethod
    def fromRational(numerator: Any, denominator: Any) -> Any:
        """self.fromRational(numerator, denominator) -> creates a new TimeBase object from the given parameters.
        For example:
          newTimeBase = TimeBase.fromRational(25, 1)
          newTimeBase = TimeBase.fromRational(30000, 1001)
        """
    @staticmethod
    def fromString(str: Any) -> TimeBase:
        """TimeBase.fromString(str) -> deprecated; a TimeBase can now be constructed directly from a str, e.g. TimeBase('30').  Construct a TimeBase object using a str as input.
        For example:
          newTimeBase = TimeBase.fromString('25')
          newTimeBase = TimeBase.fromString('30000 / 1001')

        @return: TimeBase
        """
    def isNTSC(self) -> bool:
        """self.isNTSC() -> returns True if the time base is NTSC (24*1000/1001, 30*1000/1001, or 60*1000/1001).

        @return: True or False
        """
    def isValid(self) -> bool:
        """self.isValid() -> returns True if the denominator of the time base is non-zero.

        @return: True or False
        """
    def numerator(self) -> int:
        """self.numerator() -> gets the numerator of the time base.
        @return: int
        """
    def supportsDropFrames(self) -> bool:
        """self.supportsDropFrames() -> returns True if the time base supports drop frames (only true for 30 or 60 fps NTSC currently).

        @return: True or False
        """
    def toFloat(self) -> float:
        """self.toFloat() -> returns the time base value expressed as a floating point value.

        @return: float
        """
    def toInt(self) -> int:
        """self.toInt() -> returns the time base value, rounded to the nearest integer.

        @return: int
        """
    def toRational(self) -> tuple[int, ...]:
        """self.toRational() -> returns a tuple of the numerator and the denominator of the time base.

        @return: tuple of integers
        """
    def toRationalString(self) -> str:
        """self.toRationalString() -> returns a string containing the time base expressed as a ratio, for example '30000/1001'.

        @return: string
        """
    def toString(self) -> str:
        """self.toString() -> returns a string containing the time base as a floating point number. Equivalent to str(object).

        @return: string
        """

class Timecode:
    """Helper module to convert back and forth between (frames and time bases) and time code values."""
    class DisplayType(_enum.IntEnum):
        kDisplayDropFrameTimecode: Timecode.DisplayType
        kDisplayFrames: Timecode.DisplayType
        kDisplayTimecode: Timecode.DisplayType
        def __new__(cls, value: Any) -> Self: ...
    @staticmethod
    def HMSFToFrames(timeBase: Any, dropFrame: Any, h: Any, m: Any, s: Any, f: Any) -> Any:
        """self.HMSFToFrames(timeBase, dropFrame, h, m, s, f) -> takes a timebase, whether or not it's got drop frames, an hour, minute, second and frame, and returns a time value.

        @param timeBase: the time base to use
        @param dropFrames: True if you want drop frames taken into account
        @param h: hour to use
        @param m: minute to use
        @param s: second to use
        @param f: frame to use
        @return: frame
        """
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    @staticmethod
    def displayTypeFromString(s: Any) -> Timecode:
        """self.displayTypeFromString(s) -> guesses the display type from a timecode string. This can be inferred from separators (though not guaranteed) or if no separators than just display as frames.
        Example:
        displayType = Timecode.displayTypeFromString('01:00:00:00')
        print( displayType ) # prints out hiero.core.Timecode.kDisplayTimecode

        displayType = Timecode.displayTypeFromString('01:00:00;00')
        print( displayType ) # prints out hiero.core.Timecode.kDisplayDropFrameTimecode, because of the semi-colon (;)


        @param s: string to detect time code format from
        @return: hiero.core.Timecode.DisplayType enumeration
        """
    @staticmethod
    def framesFromBCD(arg1: Any, arg2: Any, /) -> Any: ...
    @staticmethod
    def framesFromTimecode(arg1: Any, arg2: Any, /) -> Any: ...
    @staticmethod
    def framesToHMSF(time: Any, timeBase: Any, dropFrames: bool) -> Any:
        """self.framesToHMSF(time, timeBase, dropFrames) -> takes a time, timebase and whether or not it's got drop frames, and returns a tuple of the hour, minute, second and frame.
        Example:
        hour, minute, second, frame = Timecode.framesToHMSF(0, timeBase, True)

        @param time: the frame you want to get the time code for
        @param timeBase: the time base to use
        @param dropFrames: True if you want drop frames taken into account
        @return: tuple of hour, minute, second, frame
        """
    @staticmethod
    def readTimecode(arg1: Any, /) -> Any: ...
    @staticmethod
    def samplesToString(arg1: Any, arg2: Any, arg3: Any, arg4: Any, /) -> Any: ...
    @staticmethod
    def stringToTime(s: Any, timeBase: Any, displayType: Any, timecodeOffset: Any) -> tuple:
        """self.stringToTime(s, timeBase, displayType, timecodeOffset) -> returns a tuple of integer values containing the frame described by a timecode string and the number of time fields in the string that was passed in.

        @param s: the string to convert
        @param timeBase: the time base to use
        @param displayType: how the string was formatted; can be (Timecode.kDisplayTimecode, Timecode.kDisplayDropFrameTimecode, or Time.kDisplayFrames)
        @param timecodeOffset: an offset to apply before converting to a time code string
        @return: tuple
        """
    @staticmethod
    def timeToString(time: Any, timeBase: Any, displayType: Any, includeSign: Any, timecodeOffset: Any) -> str:
        """self.timeToString(time, timeBase, displayType, includeSign, timecodeOffset) -> returns a string formatted as a time code.

        @param time: the frame to use
        @param timeBase: the time base to use
        @param displayType: how to format the returned string (Timecode.kDisplayTimecode, Timecode.kDisplayDropFrameTimecode, or Time.kDisplayFrames)
        @param includeSign: if True, a '+' will be put in front of positive time codes
        @param timecodeOffset: an offset to apply before converting to a time code string
        @return: string
        """

class TimelineDirectExport:
    """Provides an interface for exporting a sequence through Quick Export"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def exportSequence(self, sequence: Any, dstFileName: Any, settings: Any) -> Any:
        """self.exportSequence(sequence, dstFileName, settings) -> exports a sequence into a mov output file based on the settings passed.

        @param sequence: hiero.core.Sequence object to be exported
        @param dstFileName: path of the output mov file to be created
        @param settings: dictionary containing the settings for the export
        """

class TrackItem(TrackItemBase):
    """Represents a specific item on a Track. Can also be created using the createTrackItem method on VideoTrack and AudioTrack objects. Can be converted to a MediaSource object if isSource() returns True, or a Sequence object if isSequence() returns True.
    Note that the version functions don't cause a scan of any directories for other versions of media and will only skip to versions that have already been discovered. For an example of how to do that, see Plugins/site-packages/hiero/ui/ScanForVersions.py.
    For an example of how to implement custom versioning scheme, see Plugins/site-packages/hiero/core/versioning_example.py.
    """
    class MediaType(_enum.IntEnum):
        kAudio: TrackItem.MediaType
        kUnknown: TrackItem.MediaType
        kVideo: TrackItem.MediaType
        def __new__(cls, value: Any) -> Self: ...
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def addTag(self, tag: Any) -> Tag:
        """self.addTag(tag) -> adds a new tag to the track item.

        @param tag: tag object
        @return: a hiero.core.Tag object
        """
    def addTagToRange(self, tag: Any) -> Tag:
        """self.addTagToRange(tag) -> adds a new tag to the specified range of the track item.

        @param inTime: start time of the tag, relative to the source media start time
        @param outTime: end time of the tag, relative to the source media start time
        @param tag: tag object
        @return: a hiero.core.Tag object
        """
    def addToNukeScript(self, script: _hiero_core_nuke_Script.ScriptWriter = ..., firstFrame: Any = ..., additionalNodes: Any = ..., additionalNodesCallback: Any = ..., includeRetimes: bool = ..., retimeMethod: Any = ..., startHandle: Any = ..., endHandle: Any = ..., colourTransform: Any = ..., offset: Any = ..., nodeLabel: Any = ..., includeEffects: bool = ..., outputToSequenceFormat: bool = ...) -> Any:
        """This is a variation on the Clip.addToNukeScript() method that remaps the
        Read frame range to the range of the this TrackItem rather than the Clip's
        range. TrackItem retimes and reverses are applied via Retime and OFlow nodes
        if needed. The additionalNodes parameter takes a list of nodes to add before
        the source material is shifted to the TrackItem timeline time and trimmed to
        black outside of the cut. This means timing can be set in the original
        source range and adding channels, etc won't affect frames outside the cut
        length.

        @param retimeMethod: "Motion", "Blend", "Frame" - Knob setting for OFlow retime method
        @param offset: Optional, Global frame offset applied across whole script
        """
    def currentVersion(self) -> Version:
        """self.currentVersion() -> returns a version object for the current version set on this track item.

        @return: hiero.core.Version object
        """
    def eventNumber(self) -> int:
        """self.eventNumber() -> Get the event number of this track item on it's Sequence.

        @return: integer event number
        """
    def getAvailableOcioColourTransforms(self) -> list[str]:
        """self.    getAvailableOcioColourTransforms() -> returns colour transform for the media source.

        @return: string
        """
    def handleInLength(self) -> int:
        """self.handleInLength() -> returns the length of the track item's in handle.

        @return: frames
        """
    def handleInTime(self) -> int:
        """self.handleInTime() -> returns the track item's in handle time.

        @return: frames
        """
    def handleOutLength(self) -> int:
        """self.handleOutLength() -> returns the length of the track item's out handle.

        @return: frames
        """
    def handleOutTime(self) -> int:
        """self.handleOutTime() -> returns the track item's out handle time.

        @return: frames
        """
    def inTransition(self) -> Transition:
        """self.inTransition() -> returns the in transition for this track item.

        @return: hiero.core.Transition object
        """
    def isLinked(self, trackItem: Any) -> Any:
        """self.isLinked(trackItem) -> Tests if this track item is linked to the given track item.

        @param trackItem: track item to test if this track item is linked to
        @return True if items are linked, False otherwise
        """
    def isMediaPresent(self) -> bool:
        """self.isMediaPreset() -> returns True if the track item represent a media source and if the media source is currently available in Hiero (and not offline). Returns False otherwise.

        @return: True or False
        """
    def layers(self) -> list[str]:
        """self.layers() -> returns a list of layer names present within the TrackItem.
        @return: list of layer names.
        """
    def link(self, trackItem: Any) -> Any:
        """self.link(trackItem) -> Links track item with another track item. Both track items must point to the same source.

        @param trackItem: track item to link to
        """
    def mapSourceToTimeline(self, arg1: Any, /) -> Any:
        """self.mapTimelineToSource(time) -> Map from the track item's source time to timeline time.

        @param time: time to map
        @return: mapped time
        """
    def mapTimelineToSource(self, time: Any) -> Any:
        """self.mapTimelineToSource(time) -> Map from timeline time to the track item's source time.

        @param time: time to map
        @return: mapped time
        """
    def maxVersion(self) -> Version:
        """self.maxVersion() -> sets the highest available version on this TrackItem. If versionLinkedToBin() is set, changes the version on all linked objects.

        @return: hiero.core.Version object
        """
    def mediaType(self) -> TrackItem.MediaType:
        """self.mediaType() -> returns media type for the track item.

        @return: MediaType object
        """
    def metadata(self) -> DataCollection:
        """self.metadata() -> returns the metadata for the track item.

        @return: hiero.core.DataCollection object
        """
    def minVersion(self) -> Version:
        """self.minVersion() -> sets the lowest available version on this TrackItem. If versionLinkedToBin() is set, changes the version on all linked objects.

        @return: hiero.core.Version object
        """
    def name(self) -> str:
        """self.name() -> returns the track item's name.

        @return: string
        """
    def nextVersion(self) -> Version:
        """self.nextVersion() -> sets the next available version on this TrackItem. If versionLinkedToBin() is set, changes the version on all linked objects.

        @return: hiero.core.Version object
        """
    def numVersions(self) -> int:
        """self.numVersions() -> returns the total number of versions on this track item currently (nothing to do with the maximum or minimum version number).

        @return: int
        """
    def outTransition(self) -> Transition:
        """self.outTransition() -> returns the out transition for this track item.

        @return: hiero.core.Transition object
        """
    def playbackSpeed(self) -> float:
        """self.playbackSpeed() -> returns the playback speed of this track item.

        @return: double
        """
    def prevVersion(self) -> Version:
        """self.prevVersion() -> sets the next available version on this TrackItem. If versionLinkedToBin() is set, changes the version on all linked objects.

        @return: hiero.core.Version object
        """
    def reconnectMedia(self, path: Any) -> Any:
        """self.reconnectMedia(path) -> Reconnects media for the Clip used by the TrackItem, using the specified path.

        @param path: path containing media to reconnect to
        """
    def reformatState(self) -> ReformatState:
        """self.reformatState() -> returns the reformat state for the track item.

        @return: hiero.core.ReformatState object
        """
    def removeTag(self, tag: Tag) -> Any:
        """self.removeTag(tag) -> removes the tag from the track item.

        @param tag: hiero.core.Tag object
        """
    def replaceClips(self, path: Any) -> Any:
        """self.replaceClips(path) -> Find a new Clip from the specified path, and replace the TrackItem's existing Clip with it.

        @param path: path containing media to replace with
        """
    def setCameraColourTransform(self, colourTransform: Any) -> Any:
        """self.setCameraColourTransform(colourTransform) -> sets the camera colour transform for the source media.

        @param colourTransform: Colour transform name
        """
    def setCurrentVersion(self, version: Version) -> Any:
        """self.setCurrentVersion(version) -> sets the current version (by object) on this track item. Note that this method doesn't check that the versioned media source exists on disk.

        @param version: hiero.core.Version object
        """
    def setCurrentVersionIndex(self, index: Any) -> Version:
        """self.setCurrentVersionIndex(index) -> sets the current version on this track item and returns the new version object. Creates a new version if there wasn't one before, but doesn't check that the versioned media source exists on disk.

        @param index: the integer index to set the current version on this track item to
        @return: hiero.core.Version object

        WARNING - DEPRECATED ( setCurrentVersionIndex ): This method is deprecated and will not be present in future versions of the Python API.
        Version indices are no longer unique identifiers and should not be used as such. Please use TrackItem.setActiveVersion() instead.
        """
    def setName(self, name: Any) -> Any:
        """self.setName(name) -> sets the name of the track item.

        @param name: the value to set the track name to
        """
    def setPlaybackSpeed(self, newSpeed: float) -> Any:
        """self.setPlaybackSpeed(newSpeed) -> sets the playback speed of this track item.

        @param newSpeed: double
        """
    def setSource(self, clip: Any, trackIndex: Any = ...) -> Any:
        """self.setSource(clip, trackIndex=0) -> sets the source Clip for this TrackItem.
        If the TrackItem is not already in a Track, the duration will be set to the Clip's duration.

        @param clip: the hiero.core.Clip object to set as the source for this track item
        @param trackIndex: optional track index, for instance if you are adding an audio Clip and want to use its second audio track
        @return: the hiero.core.Clip object passed in
        """
    def setSourceIn(self, time: Any) -> Any:
        """self.setSourceIn(time) -> sets the source in for the track item. This will shrink or grow the duration.

        @param time: frame value
        """
    def setSourceMediaColourTransform(self, colourTransform: Any) -> Any:
        """self.setSourceMediaColourTransform(colourTransform) -> sets the input colour transform for the source media.

        @param colourTransform: Colour transform name
        """
    def setSourceOut(self, time: Any) -> Any:
        """self.setSourceOut(time) -> sets the source out for the track item. This will shrink or grow the duration.

        Note that this value depends on speed. For exact editing, edit speed instead in order to avoid rounding errors.

        @param time: frame value
        """
    def setTimelineIn(self, inTime: Any) -> Any:
        """self.setTimelineIn(inTime) -> sets the timeline in value. Shrinks or grows the timeline duration, as appropriate.

        @param inTime: frame value
        """
    def setTimelineOut(self, outTime: Any) -> Any:
        """self.setTimelineOut(outTime) -> sets the timeline out value. Shrinks or grows the timeline duration, as appropriate.

        @param outTime: frame value
        """
    def setTimes(self, timelineIn: Any, timelineOut: Any, sourceIn: Any, sourceOut: Any) -> Any:
        """self.setTimes(timelineIn, timelineOut, sourceIn, sourceOut) -> sets the timeline and source times for the track item.

        @param timelineIn: timeline in frame
        @param timelineOut: timeline out frame
        @param sourceIn: source in frame
        @param sourceOut: source out frame
        """
    def setVersionLinkedToBin(self, linked: Any) -> Any:
        """self.setVersionLinkedToBin(linked) -> link the TrackItem's version to that of it's associated BinItem. If updateVersion is false, the TrackItem's version will not be updated immediately, this will happen next time a version is set on the BinItem or any linked TrackItems.

        @param linked: The linked state to be set on the TrackItem
        @param updatedVersion: Whether or not the TrackItems version will be updated
        """
    def setVolume(self) -> Any:
        """self.setVolume() -> sets the volume of an audio TrackItem.

        @param volume: value to set (0.0 - 1.0)
        """
    def source(self) -> Clip | Sequence | MediaSource:
        """self.source() -> depending on the underlying type of the track item, returns a hiero.core.Clip object, a hiero.core.Sequence object or a hiero.core.MediaSource object.

        @return: a hiero.core.Clip object, a hiero.core.Sequence object or a hiero.core.MediaSource object
        """
    def sourceDuration(self) -> float:
        """self.sourceDuration() -> returns the source duration value for the track item.

        Note that this value depends on speed, and may not be an integer value.

        @return: frames
        """
    def sourceIn(self) -> float:
        """self.sourceIn() -> returns the source in value for the track item.

        Note that after a combination of a retime and editing, this value may not be an integer.

        @return: frame
        """
    def sourceMediaColourTransform(self) -> str:
        """self.setSourceMediaColourTransform() -> returns colour transform for the media source.

        @return: string
        """
    def sourceOut(self) -> float:
        """self.sourceOut() -> returns the source out value for the track item.

        Note that this value depends on speed, and may not be an integer value.

        @return: frame
        """
    def tags(self) -> tuple:
        """self.tags() -> returns a tuple of all of the tags applied to this object.

        @return: tuple of hiero.core.Tag objects
        """
    def thumbnail(self, frame: int = ..., layer: str = ...) -> _PySide6_QtGui.QImage:
        """self.thumbnail(frame, layer) -> returns a thumbnail of the frame specified as a QImage object.

        @param frame: the frame to get the thumbnail for (defaults to 0)
        @param layer: the layer to get the thumbnail for (defaults to rgb)
        @return: QImage object
        """
    def toString(self) -> str: ...
    def unlink(self) -> Any:
        """self.unlink() -> Unlinks this track item from its link group."""
    def unlinkAll(self) -> Any:
        """self.unlinkAll() -> Unlink all track items that are linked to this one."""
    def versionDown(*args, **kwargs: Any) -> Version:
        """self.versionDown() -> decrements the current version on this track item and returns the new version object. Creates a new version if there wasn't one before, but doesn't check that the versioned media source exists on disk.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionDown ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from TrackItem. To find new versions, please use hiero.core.VersionScanner. To obtain the next version, please use TrackItem.prevVersion().
        """
    def versionLinkedToBin(self) -> bool:
        """self.versionLinkedToBin() -> get if the TrackItem's version is linked to the associated BinItem

        @return: bool
        """
    def versionMaxAvailable(*args, **kwargs: Any) -> Version:
        """self.versionMaxAvailable() -> returns the highest discovered version on this track item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionMaxAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from TrackItem. This method has been replaced by TrackItem.maxVersion().
        """
    def versionMinAvailable(*args, **kwargs: Any) -> Version:
        """self.versionMinAvailable() -> returns the lowest discovered version on this track item.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionMinAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from TrackItem. This method has been replaced by TrackItem.minVersion().
        """
    def versionNextAvailable(*args, **kwargs: Any) -> Version:
        """self.versionNextAvailable() -> returns the next highest available version on this track item that the application has discovered.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionNextAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from TrackItem. This method has been replaced by TrackItem.nextVersion().
        """
    def versionPrevAvailable(*args, **kwargs: Any) -> Version:
        """self.versionPrevAvailable() -> returns the next lowest version on this track item that the application has discovered.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionPrevAvailable ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from TrackItem. This method has been replaced by TrackItem.prevVersion().
        """
    def versionUp(*args, **kwargs: Any) -> Version:
        """self.versionUp() -> increments the current version on this track item and returns the new version object. Creates a new version if there wasn't one before, but doesn't check that the versioned media source exists on disk.

        @return: hiero.core.Version object

        WARNING - DEPRECATED ( versionUp ): This method is deprecated and will not be present in future versions of the Python API.
        Only available versions can now be obtained from TrackItem. To find new versions, please use hiero.core.VersionScanner. To obtain the next version, please use TrackItem.nextVersion().
        """
    def volume(self) -> float:
        """self.volume() -> returns the volume of the track item."""

class Transition(TrackItemBase):
    """Object representing a transition between two clips."""
    class Alignments(_enum.IntEnum):
        kDissolve: Transition.Alignments
        kFadeIn: Transition.Alignments
        kFadeOut: Transition.Alignments
        kUnknown: Transition.Alignments
        def __new__(cls, value: Any) -> Self: ...
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def alignment(self) -> Any:
        """self.alignment() -> returns the alignment mode of this transition. Either kFadeIn, kDissolve, kFadeOut or kUnknown.

        @return: alignment type (hiero.core.Transition.Alignments)
        """
    @staticmethod
    def createAudioCrossfadeTransition(trackItem1: Any, trackItem2: Any, duration1: Any, duration2: Any) -> Transition:
        """self.createAudioCrossfadeTransition(trackItem1, trackItem2, duration1, duration2) -> creates a new audio crossfade (kDissolve) Transition between two adjacent track items.
        The effect will start at duration frames from the end of the trackItem1 and end at duration frames from the start of trackItem2.

        @param trackItem1: the earlier hiero.core.TrackItem object to dissolve from. Must be an Audio TrackItem.
        @param trackItem2: the later hiero.core.TrackItem object to crossfade to. Must be an Audio TrackItem.
        @param duration1: frames for the crossfade from
        @param duration2: frames for the crossfade to
        @return: hiero.core.Transition object
        @seealso: createDissolveTransition for Video equivalent
        """
    @staticmethod
    def createAudioFadeInTransition(trackItem: Any, duration: Any) -> Transition:
        """self.createAudioFadeInTransition(trackItem, duration) -> creates a new fade in (kFadeIn) Transition with the timelineIn of the trackItem and the duration specified.

        @param trackItem: hiero.core.TrackItem object to use the timelineIn value from. Must be an Audio TrackItem.
        @param duration: frames
        @return: hiero.core.Transition object
        @seealso: createFadeInTransition for Video equivalent
        """
    @staticmethod
    def createAudioFadeOutTransition(trackItem: Any, duration: Any) -> Transition:
        """self.createAudioFadeOutTransition(trackItem, duration) -> creates a new fade out (kFadeOut) Transition. The in point will be the timelineOut of trackItem, minus the duration specified.

        @param trackItem: hiero.core.TrackItem object to use the timelineOut value from. Must be an Audio TrackItem.
        @param duration: frames
        @return: hiero.core.Transition object
        @seealso: createFadeOutTransition for Video equivalent
        """
    @staticmethod
    def createDissolveTransition(trackItem1: Any, trackItem2: Any, duration1: Any, duration2: Any) -> Transition:
        """self.createDissolveTransition(trackItem1, trackItem2, duration1, duration2) -> creates a new dissolve (kDissolve) Transition between two adjacent track items.
        The effect will start at duration frames from the end of the trackItem1 and end at duration frames from the start of trackItem2.

        @param trackItem1: the earlier hiero.core.TrackItem object to dissolve from. Must be a Video TrackItem.
        @param trackItem2: the later hiero.core.TrackItem object to dissolve to. Must be a Video TrackItem.
        @param duration1: frames for the dissolve from
        @param duration2: frames for the dissolve to
        @return: hiero.core.Transition object
        @seealso: createAudioCrossTransition for Audio equivalent
        """
    @staticmethod
    def createFadeInTransition(trackItem: Any, duration: Any) -> Transition:
        """self.createFadeInTransition(trackItem, duration) -> creates a new fade in (kFadeIn) Transition with the timelineIn of the trackItem and the duration specified.

        @param trackItem: hiero.core.TrackItem object to use the timelineIn value from. Must be a Video TrackItem.
        @param duration: frames
        @return: hiero.core.Transition object
        @seealso: createAudioFadeInTransition for Audio equivalent
        """
    @staticmethod
    def createFadeOutTransition(trackItem: Any, duration: Any) -> Transition:
        """self.createFadeOutTransition(trackItem, duration) -> creates a new fade out (kFadeOut) Transition. The in point will be the timelineOut of trackItem, minus the duration specified.

        @param trackItem: hiero.core.TrackItem object to use the timelineOut value from. Must be a Video TrackItem.
        @param duration: frames
        @return: hiero.core.Transition object
        @seealso: createAudioFadeOutTransition for Audio equivalent
        """
    def dissolveNode(self) -> _nuke.Node:
        """self.dissolveNode() -> Returns the Dissolve node which controls the transition curve.

        @return: nuke.Node
        """
    def guid(self, *args: Any, **kwargs: Any) -> Any: ...
    def inTrackItem(self) -> Any:
        """self.inTrackItem() -> Get the in track item for this transition.

        return: hiero.core.TrackItem
        """
    def multiplyNode(self) -> _nuke.Node:
        """self.multiplyNode() -> Returns the Multiply node which controls the transition curve. For internal use only.

        @return: nuke.Node
        """
    def outTrackItem(self) -> Any:
        """self.outTrackItem() -> Get the out track item for this transition.

        return: hiero.core.TrackItem
        """
    def parent(self) -> AudioTrack | VideoTrack:
        """self.parent() -> returns the AudioTrack or VideoTrack that contains this transition.

        @return: hiero.core.AudioTrack or hiero.core.VideoTrack object
        """
    def project(self, *args: Any, **kwargs: Any) -> Any: ...
    def setAlignment(self, alignment: Any) -> Any:
        """self.setAlignment(alignment) -> sets the alignment mode on this transition.

        @param alignment: alignment type (hiero.core.Transition.Alignments), either kFadeIn, kDissolve, or kFadeOut
        """
    def setTimelineIn(self, inTime: Any) -> Any:
        """self.setTimelineIn(inTime) -> sets the in point for this transition. Note that this trims the duration of the transition.

        @param inTime: frame for the new in point
        """
    def setTimelineOut(self, outTime: Any) -> Any:
        """self.setTimelineOut(outTime) -> sets the out point for this transition. Note that this trims the duration of the transition.

        @param outTime: frame for the new out point
        """
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """

class UndoGroup:
    """Helper class for beginning and ending undo on a project. Recommended usage is to create with hiero.core.Project.beginUndo(name), using a with block for exception safety to ensure Project.endUndo() is called.

    For example:
        with project.beginUndo('My Undo'):
        // Undoable edits
    """
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __enter__(self) -> Any:
        """self.__enter__() -> Allows usage in a with block to automatically end the undo."""
    def __exit__(self) -> Any:
        """self.__exit__() -> Calls self.endUndo().  This allows usage in a with block to automatically end the undo."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def beginUndo(self) -> Any:
        """self.beginUndo() -> starts a new undo action on the project with the initialised name.  See hiero.core.Project.beginUndo()"""
    def endUndo(self) -> Any:
        """self.endUndo() -> ends the undo action on the project"""
    def isNull(self, *args: Any, **kwargs: Any) -> Any: ...

class Version:
    """Object representing a version of a clip or sequence. Can be created with a Clip or Sequence object."""
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, value: Any, /) -> bool:
        """Return self==value."""
    def __ge__(self, value: Any, /) -> bool:
        """Return self>=value."""
    def __gt__(self, value: Any, /) -> bool:
        """Return self>value."""
    def __hash__(self, /) -> int:
        """Return hash(self)."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __le__(self, value: Any, /) -> bool:
        """Return self<=value."""
    def __lt__(self, value: Any, /) -> bool:
        """Return self<value."""
    def __ne__(self, value: Any, /) -> bool:
        """Return self!=value."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def color(self) -> _PySide6_QtGui.QColor:
        """self.color() -> Get the version display color, or an invalid QColor if not set.

        @return: PySide6.QtGui.QColor
        """
    def guid(self) -> str: ...
    def isHidden(self) -> bool: ...
    def isNull(self) -> bool:
        """self.isNull() -> returns True if the object is invalid, False otherwise.

        @return: True or False
        """
    def item(self) -> Clip | Sequence:
        """self.item() -> returns the clip or sequence stored with this version.

        @return: hiero.core.Clip or hiero.core.Sequence object
        """
    def name(self) -> str:
        """self.name() -> returns the name of this version.

        @return: string
        """
    def parent(self) -> BinItem:
        """self.parent() -> returns the bin item that contains this version.

        @return: hiero.core.BinItem object
        """
    def serialize(self) -> str: ...
    def setColor(self, color: Any) -> Any:
        """self.setColor(color) -> Set the version display color.

        @param color: the color to set, as a PySide6.QtGui.QColor, a string (e.g. '#ff0000') or an integer containing the RGB components (e.g. 0x11aa33).
        """
    def setHidden(self, arg1: Any, /) -> Any: ...
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
    def versionIndex(*args, **kwargs: Any) -> str:
        """self.versionIndex() -> returns a string containing the version's index.

        @return: string

        WARNING - DEPRECATED ( versionIndex ): This method is deprecated and will not be present in future versions of the Python API.
        Version indices are no longer unique identifiers and should not be used as such.
        """

class VideoTrack(TrackBase):
    """Object for manipulating video tracks."""
    def __bool__(self, /) -> bool:
        """True if self else False"""
    def __copy__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __getitem__(self, key: Any, /) -> Any:
        """Return self[key]."""
    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def __len__(self, /) -> int:
        """Return len(self)."""
    def __repr__(self, /) -> str:
        """Return repr(self)."""
    def addSubTrackItem(self, subTrackItem: Any, subTrackIndex: Any) -> Any:
        """self.addSubTrackItem(subTrackItem, subTrackIndex) -> Add a subtrack item to the track on the given sub-track index.
        This method will cut or delete sub-track items that overlap with the one being added.

        @param subTrackItem: a hiero.core.SubTrackItem object to add.
        @param subTrackIndex: the index of the sub-track to add to.
        @return: the added item
        """
    def addToNukeScript(self, script: _hiero_core_nuke_Script.ScriptWriter = ..., additionalNodes: Any = ..., additionalNodesCallback: Any = ..., includeRetimes: bool = ..., retimeMethod: Any = ..., offset: Any = ..., skipOffline: bool = ..., mediaToSkip: Any = ..., disconnected: bool = ..., includeEffects: bool = ...) -> Any:
        """Add a Read node for each track item to the script with Merge or Dissolve nodes
        to join them in a sequence. TimeClip nodes are added to pad any gaps between clips.

        @param script: Nuke script object to add nodes to.
        @param additionalNodes: List of nodes to be added post read, passed on to track items
        @param additionalNodesCallback: callback to allow custom additional node per item function([Clip|TrackItem|Track|Sequence])
        @param includeRetimes: True/False include retimes
        @param retimeMethod: "Motion", "Blend", "Frame" - Knob setting for OFlow retime method
        @param offset: Optional, Global frame offset applied across whole script
        @param skipOffline: If True, offline clips are not included in the export
        @param mediaToSkip: List of MediaSources which should be excluded from the export
        @param disconnected: If True, items on the track are not connected and no constant nodes are added to fill gaps
        @param includeEffects: If True, clip-level soft effects will be included in the output
        """
    @overload
    def addTrackItem(self, clip: Clip, position: int) -> TrackItem:
        """self.addTrackItem(clip, position) -> if the first parameter is a Clip object, the second parameter must be specified and this method creates a new track item and adds it to this video track at the given position.
        If the first parameter is a TrackItem, then this method just adds the track item specified.
        This method will cut or delete track items that overlap with the one being added.
        This method can only be called if the track has already been added to a Sequence.

        @param clip: a hiero.core.Clip object or a hiero.core.TrackItem object, to add to this video track.
        @param position: int; insert position. Do not specify if clip is a TrackItem.
        @return: hiero.core.TrackItem object
        """
    @overload
    def addTrackItem(self, trackItem: TrackItem) -> TrackItem:
        """self.addTrackItem(clip, position) -> if the first parameter is a Clip object, the second parameter must be specified and this method creates a new track item and adds it to this video track at the given position.
        If the first parameter is a TrackItem, then this method just adds the track item specified.
        This method will cut or delete track items that overlap with the one being added.
        This method can only be called if the track has already been added to a Sequence.

        @param clip: a hiero.core.Clip object or a hiero.core.TrackItem object, to add to this video track.
        @param position: int; insert position. Do not specify if clip is a TrackItem.
        @return: hiero.core.TrackItem object
        """
    def blendMode(self) -> str:
        """self.blendMode() -> returns a string representing the blend-mode as it appears in the Nuke Merge Node, if the VideoTrack object has blending enabled.

        @return: String containing the blend-mode
        """
    def clone(*args, **kwargs: Any) -> VideoTrack:
        """self.clone() -> returns a deep copy of this object.

        @return: hiero.core.VideoTrack object

        WARNING - DEPRECATED ( clone ): This method is deprecated and will not be present in future versions of the Python API.
        This method has been replaced by copy().
        """
    def copy(self) -> VideoTrack:
        """self.copy() -> returns a deep copy of this object.

        @return: hiero.core.VideoTrack object
        """
    def createEffect(self, effectType: Any = ..., cloneFrom: Any = ..., copyFrom: Any = ..., trackItem: Any = ..., timelineIn: Any = ..., timelineOut: Any = ..., subTrackIndex: Any = ...) -> Any:
        """self.createEffect(trackItem=None, timelineIn=None, timelineOut=None, subTrackIndex=None) -> Create an effect item and add it to the track.

        The effect's node will be of type effectType or if cloneFrom is given, will be a clone of that.  It will use timing either based on trackItem if given or timelineIn and timelineOut.  If none of these are specified,
        the effect will cover the full duration of the track's parent sequence.

        @param effectType: the node type to create a soft effect for

        @param cloneFrom: if given, the new effect item will be cloned from this

        @param copyFrom: if given, the new effect item will be copied from this

        @param trackItem: if specified, the effect will be linked to the track item and use the same timing

        @param timelineIn: the effect start time

        @param timelineOut: the effect end time

        @param subTrackIndex: if specified, will be placed on the appropriate sub-track, otherwise will be placed on a new sub-track

        @return: the created EffectTrackItem object
        """
    def createTrackItem(self, name: Any) -> TrackItem:
        """self.createTrackItem(name) -> creates a new track item.

        @param name: the name of the new track item
        @return: hiero.core.TrackItem object
        """
    def isBlendEnabled(self) -> bool:
        """self.isBlendEnabled() -> returns True if the VideoTrack object has blending enabled.

        @return: True or False
        """
    def isBlendMaskEnabled(self) -> bool:
        """self.isBlendMaskEnabled() -> returns True if the VideoTrack object has blend-masking enabled.

        @return: True or False
        """
    def items(self) -> tuple[TrackItem, ...]:
        """self.items() -> returns a tuple with all of the track items contained by this track.

        @return: tuple of hiero.core.TrackItem objects
        """
    def parent(self) -> Sequence:
        """self.parent() -> returns the sequence that contains this track.

        @return: hiero.core.Sequence object
        """
    def removeSubTrackItem(self, subTrackItem: Any, option: Any = ...) -> Any:
        """self.removeSubTrackItem(subTrackItem, option=eRemoveLinkedItems) -> removes a sub-track item from this track.

        @param subTrackItem: the hiero.core.SubTrackItem to remove from this track
        @param option: options controlling the remove behavior. By default linked items are also removed.
        """
    def setAllViews(self) -> Any:
        """self.setAllViews() -> assigns all views to a VideoTrack in the form of an empty string since that represents all views.
        An error is raised if the track doesn't have a project with multiple views.
        """
    def setBlendEnabled(self) -> Any:
        """self.setBlendEnabled() -> enables or disables blending on the VideoTrack, if it is not locked or restricted.
        An error is raised if the track is locked or restricted.
        """
    def setBlendMaskEnabled(self) -> Any:
        """self.setBlendMaskEnabled() -> sets whether blend-masking is enabled or not, if it is not locked or restricted.
        An error is raised if the track is locked or restricted.
        """
    def setBlendMode(self) -> Any:
        """self.setBlendMode() -> sets the blend mode to be used, if it is not locked or restricted. Expected strings are NUKE Merge Node operations.
        An error is raised if the track is locked or restricted.
        """
    def setView(self) -> Any:
        """self.setView() -> assigns a view on a VideoTrack.
        An error is raised if the track doesn't have a project with multiple views, or the specified view is invalid.
        """
    def splitViewsToTracks(self) -> Any:
        """self.splitViewsToTracks() -> split the views to separate tracks on the Timeline.
        An error is raised if the track doesn't have a project with multiple views.
        """
    def subTrackItems(self) -> tuple:
        """self.subTrackItems() -> returns a tuple with an entry for each sub track in this track, each entry being a tuple of items
        on the corresponding sub track.

        @return: tuple of hiero.core.SubTrackItem sub-class objects
        """
    def toString(self) -> str:
        """self.toString() -> returns a description of the object. Equivalent to str(object).

        @return: string
        """
    def trackIndex(self) -> int: ...
    def view(self) -> str:
        """self.view() -> returns a string representing the view assigned to the VideoTrack. An empty string is returned if the track has multiple views assigned.

        @return: String containing the view name
        """

def LUTGroup(arg1: Any, arg2: Any = ..., /) -> Any: ...

def LUTs(arg1: Any = ..., arg2: Any = ...) -> tuple[str, ...]:
    """hiero.core.LUTs() -> returns a tuple with the names of all of the available luts.

    @return: tuple of strings
    """

def PaintBlendModeName(arg1: Any, /) -> Any: ...

def SequenceAutoDiskCacheModeFromString(arg1: Any, /) -> Any: ...

def SequenceAutoDiskCacheModeToString(arg1: Any, /) -> Any: ...

def ViewerProcessNameFromDisplayTransformName(arg1: Any, /) -> Any: ...

def addPathRemap(windowsPathPrefix: str, osxPathPrefix: str, linuxPathPrefix: str) -> None:
    """hiero.core.addPathRemap(windowsPathPrefix, osxPathPrefix, linuxPathPrefix) -> adds to the table of file path remapping prefixes that Hiero maintains. Pairs of path prefixes added to this table will be used to convert paths between Windows, OSX and Linux. When on Windows, Hiero will replace any Linux or OSX prefixes found with the corresponding Windows prefix. On OSX, Hiero will search for the Windows and Linux path prefixes and replace them with the corresponding OSX prefix. The same applies for OSX/Windows prefixes being replaced on Linux. These can also be configured through the user interface in the General tab of the Preferences dialog.

    @param windowsPathPrefix: string
    @param osxPathPrefix: string
    @param linuxPathPrefix: string

    @return: None
    """

@overload
def addPluginPath(pluginPath: Any) -> Any:
    """hiero.core.addPluginPath(pluginPath) -> adds a new path to the list of plugin paths searched for Python plugins (in Python/Startup and Python/StartupUI folders). The user's .nuke folder will be the first in this list.
    hiero.core.addPluginPath(pluginPath, index) -> the same as above, except that the index specifies which item in the list of paths to place the new one before.

    @param pluginPath: the new path to add
    @param index: optional; if not specified or negative, the new path will be added to the end of the list
    """
@overload
def addPluginPath(pluginPath: Any, index: Any = ...) -> Any:
    """hiero.core.addPluginPath(pluginPath) -> adds a new path to the list of plugin paths searched for Python plugins (in Python/Startup and Python/StartupUI folders). The user's .nuke folder will be the first in this list.
    hiero.core.addPluginPath(pluginPath, index) -> the same as above, except that the index specifies which item in the list of paths to place the new one before.

    @param pluginPath: the new path to add
    @param index: optional; if not specified or negative, the new path will be added to the end of the list
    """

def closeAllProjects(*args: Any, **kwargs: Any) -> Any:
    """hiero.core.closeProject() -> closes all of the existing projects without saving.
    hiero.core.closeProject(bool dontSave) -> same as above, but if the parameter is set to false, unsaved projects will cause Hiero to popup a dialog for each unsaved project, asking the user if they'd like to save.

    @param dontSave: True or False
    """

def conformer() -> Conformer:
    """hiero.core.conformer() -> returns an interface for setting the conforming options.

    @return: a hiero.core.Conformer object
    """

def defaultFrameRates() -> tuple[float, float, float, float, float, float, float, float, float, float, float, float, float]:
    """hiero.core.defaultFrameRates() -> returns the list of frame rates displayed in Hiero's user interface.

    @return: tuple of floats
    """

def executeInMainThread(call: Any, *args: Any, **kwargs: Any) -> None:
    """Execute the callable 'call' with optional arguments 'args' and named arguments 'kwargs' in
    the main thread and return immediately.
    Note that this method expects a single item for args or a tuple, and a dictionary for kwargs.
    It will not accept anything else.

    Examples of how to use this method (that work):

    def someMethod(firstParameter, kwArg0=None, kwArg1=None)
      print( firstParameter )

    executeInMainThread(someMethod, "First positional parameter")
    executeInMainThread(someMethod, "First positional parameter", {'kwArg0': "arg0"})
    executeInMainThread(someMethod, ("First positional parameter", "kwArg0 passed as positional parameter"))
    executeInMainThread(someMethod, ("First positional parameter", "kwArg0 passed as positional parameter"), {'kwArg1': "arg1 as well"})
    executeInMainThread(someMethod, "First positional parameter", {'kwArg1': "arg1"})

    An example of what won't work:

    executeInMainThread(someMethod, "First positional parameter", "Second positional parameter")

    The above fails because the second parameter to executeInMainThread must be a dictionary.
    """

def executeInMainThreadWithResult(call: Any, *args: Any, **kwargs: Any) -> Any:
    """Execute the callable 'call' with optional arguments 'args' and named arguments 'kwargs' in
    the main thread and wait for the result.
    Note that this method expects a single item for args or a tuple, and a dictionary for kwargs.
    It will not accept anything else.

    Examples of how to use this method (that work):

    def someMethod(firstParameter, kwArg0=None, kwArg1=None)
      print( firstParameter )
      return kwArg1

    result = executeInMainThreadWithResult(someMethod, "First positional parameter")
    result = executeInMainThreadWithResult(someMethod, "First positional parameter", {'kwArg0': "arg0"})
    result = executeInMainThreadWithResult(someMethod, ("First positional parameter", "kwArg0 passed as positional parameter"))
    result = executeInMainThreadWithResult(someMethod, ("First positional parameter", "kwArg0 passed as positional parameter"), {'kwArg1': "arg1 as well"})
    result = executeInMainThreadWithResult(someMethod, "First positional parameter", {'kwArg1': "arg1"})

    An example of what won't work:

    result = executeInMainThreadWithResult(someMethod, "First positional parameter", "Second positional parameter")

    The above fails because the second parameter to executeInMainThread must be a dictionary.
    """

def filenameList(directory: Any, splitSequences: bool = ..., returnDirectories: bool = ..., returnHiddenFiles: bool = ...) -> Any:
    """hiero.core.filenameList(directory, splitSequences, returnDirectories, returnHiddenFiles) -> Returns a list of strings representing the items found in the specified directory, putting image sequences together as one element.

    @param directory: path to the directory to query

    @param splitSequences: optional, defaults to False. If set to True, then splits broken image sequences up. Otherwise, broken sequences create only one entry in the returned list

    @param returnDirectories: optional, defaults to True. If set to True, sub directories will be included in the returned list

    @param returnHiddenFiles: optional, defaults to True. If set to True, hidden/system files will be returned in the list

    For a directory with the following items:
    item1.txt
    item2.txt
    quicktime.mov
    highres1.dpx

    You'd get a tuple with the same list of items (txt files are recognized as not being image sequences).

    With a directory with the following items:
      * quicktime.mov
      * highres1.dpx
      * highres2.dpx
      * highres3.dpx
      * highres4.dpx
      * highres5.dpx

    You'd get a tuple with:
    ("quicktime.mov", "highres#.dpx 1-4")

    If you had the following in a directory:
      * highres1.dpx
      * highres2.dpx

      * highres4.dpx
      * highres5.dpx

    Note the missing 3 in the above list.
    If you set splitSequences to False, you'd get:
    ("highres#.dpx 1-5")

    If instead you set splitSequences to True, you'd get:
    ("highres#.dpx 1-3", "highres#.dpx 4-5")

    If you had a directory with this:
      * highres001.dpx
      * highres002.dpx
      * highres003.dpx
      * highres004.dpx
      * highres005.dpx

    You'd get a tuple like this:
    ("highres###.dpx 1-5")

    If you had a directory with this:
      * highres99.dpx
      * highres100.dpx

    You'd get this:
    ("highres#.dpx 99-100")

    In the above example, the sequence number crosses over from 2 digits to 3, so it is treated as one and the number of hashes (#) is put to 1, which means the number is wild.

    If instead you had a directory with this:
      * highres099.dpx
      * highres100.dpx

    You'd get this:
    ("highres###.dpx 99-100")

    Note that in this last example, the 99 is prefixed with 0.
    """

def formats() -> tuple[Format, ...]:
    """hiero.core.formats() -> returns a tuple with all of the formats currently available.

    @return: tuple of hiero.core.Format objects
    """

def getFilenameList(arg1: Any, arg2: Any, arg3: Any, arg4: Any, arg5: Any, /) -> Any:
    """Deprecated. Do not use. Use hiero.core.filenameList() instead"""

def getLibraryDirectory(subdirectory: Any) -> Any:
    """hiero.core.getLibraryDirectory(subdirectory) -> deprecated; use hiero.core.libraryDirectory() instead."""

def getRoleColorspace(arg1: Any, arg2: Any = ..., /) -> Any: ...

def isHieroPlayer() -> bool: ...

def isIndie() -> bool: ...

def isNC() -> bool: ...

def isQuickTimeFileExtension(fileExtension: Any) -> bool:
    """Returns True if the fileExtension is a recognised QuickTime extension, False otherwise."""

def isVideoFileExtension(fileExtension: Any) -> bool:
    """Returns True if the fileExtension is a recognised video format extension, i.e not an image Sequence (QuickTime/MXF/R3D media)"""

def libraryDirectory(subdirectory: Any) -> str:
    """hiero.core.libraryDirectory(subdirectory) -> returns the input appended to the location of the user's .nuke directory.

    @param subdirectory: path to append to the .nuke directory
    @return: string
    """

def newProject(name: Any = ...) -> Project:
    """hiero.core.newProject(name=None) -> creates and returns a new Project object. A name can optionally be given for the project.

    @return: hiero.core.Project object
    """

def openProject(path: Any) -> Any:
    """hiero.core.openProject(path)

    Opens the project found at the specified path. Must be called on the main thread. Throws an exception on failure.
    @param path: Path to the project file (\\*.hrox).
    @return: Opened project.
    """

def overrideApplicationSettingsSetValue() -> None: ...

def pathRemappings() -> list:
    """hiero.core.pathRemappings() -> returns the path remappings specified in the application preferences, or added through addPathRemap().

    @return: a list of path remappings each containing the mapping for (windows, osx, linux)
    """

def presetProjects() -> tuple[Any] | tuple[()]:
    """hiero.core.projects() -> returns a tuple of all of the currently loaded preset projects.


    @deprecated: Use hiero.core.projects(Project.kStartupProjects) instead

    @return: tuple of hiero.core.Project objects
    """

def project(name: str) -> Project | None:
    """hiero.core.project(name) -> returns the Project with the specified name, if it can be found, or None.

    @return: hiero.core.Project object
    """

@overload
def projects() -> tuple[Project, ...]:
    """hiero.core.projects() -> returns a tuple of currently loaded projects which are user projects (not startup). Same effect as calling the method below passing Project.kUserProjects.
    hiero.core.projects(projectTypes) -> returns a tuple of currently loaded projects, filtered according to projectTypes. Use hiero.core.projects()[-1] to get the last loaded project.
    @param projectTypes: optional; one of Project.kAllProjects, Project.kUserProjects, Project.kStartupProjects

    @return: tuple of hiero.core.Project objects
    """
@overload
def projects(projectTypes: Any) -> tuple[Project, ...]:
    """hiero.core.projects() -> returns a tuple of currently loaded projects which are user projects (not startup). Same effect as calling the method below passing Project.kUserProjects.
    hiero.core.projects(projectTypes) -> returns a tuple of currently loaded projects, filtered according to projectTypes. Use hiero.core.projects()[-1] to get the last loaded project.
    @param projectTypes: optional; one of Project.kAllProjects, Project.kUserProjects, Project.kStartupProjects

    @return: tuple of hiero.core.Project objects
    """

def quit() -> Any:
    """hiero.core.quit() -> shuts down Hiero, without saving any existing projects. Safer than calling sys.exit(), which doesn't always clean up properly and can cause Hiero to crash. This version sets the exit code of the Hiero process to 0.

    Note that this must be the last line in a script.
    hiero.core.quit(exitCode) -> same as the first version of this method, except that this one sets the exit code of the process to the exitCode variable.

    @param exitCode: optional; integer value to set the process's exit code to
    """

def redo() -> Any: ...

def redoSize() -> int: ...

def remapPath(path: Any) -> str:
    """hiero.core.remapPath(path) -> uses the platform specific path remapping rules from the user's preferences and applies them to the input path.

    @param path: string path to apply the path remapping rules to
    @return: string
    """

def stopScriptAndQuit(*args: Any, **kwargs: Any) -> Any: ...

def undo() -> Any: ...

def undoSize() -> int: ...

findItems = _hiero_core_find_items.findItemsInProject
