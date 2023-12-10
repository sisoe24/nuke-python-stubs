from typing import *
from numbers import Number

import nuke

from . import *

class Format(object):
    """
    A format.
    """
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

    def __new__(self,*args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def name(self,) -> str:
        """
        self.name() -> string

        Returns the user-visible name of the format.
        """
        ...

    def setName(self,name) -> None:
        """
        self.setName(name) -> None

        Set name of this format. The name parameter is the new name for the format.
        """
        ...

    def width(self,) -> int:
        """
        self.width() -> int

        Return the width of image file in pixels.
        """
        ...

    def setWidth(self,newWidth) -> None:
        """
        self.setWidth(newWidth) -> None

        Set the width of image file in pixels.newWidth is the new width for the image; it should be a positive integer.
        """
        ...

    def height(self,) -> int:
        """
        self.height() -> int

        Return the height of image file in pixels.
        """
        ...

    def setHeight(self,newHeight) -> None:
        """
        self.setHeight(newHeight) -> None

        Set the height of image file in pixels. newHeight is the new height for the image; it should be a positive integer.
        """
        ...

    def x(self,) -> int:
        """
        self.x() -> int

        Return the left edge of image file in pixels.
        """
        ...

    def setX(self,newX) -> None:
        """
        self.setX(newX) -> None

        Set the left edge of image file in pixels. newX is the new left edge for the  image; it should be a positive integer.
        """
        ...

    def y(self,) -> int:
        """
        self.y() -> int

        Return the bottom edge of image file in pixels.
        """
        ...

    def setY(self,newY) -> None:
        """
        self.setY(newY) -> None

        Set the bottom edge of image file in pixels. newY is the new bottom edge for the image; it should be a positive integer.
        """
        ...

    def r(self,) -> int:
        """
        self.r() -> int

        Return the right edge of image file in pixels.
        """
        ...

    def setR(self,newR) -> None:
        """
        self.setR(newR) -> None

        Set the right edge of image file in pixels. newR is the new right edge for the image; it should be a positive integer.
        """
        ...

    def t(self,) -> int:
        """
        self.t() -> int

        Return the top edge of image file in pixels.
        """
        ...

    def setT(self,newT) -> None:
        """
        self.setT(newT) -> None

        Set the top edge of image file in pixels. newY is the new top edge for the image; it should be a positive integer.
        """
        ...

    def pixelAspect(self,) -> float:
        """
        self.pixelAspect() -> float

        Returns the pixel aspect ratio (pixel width divided by pixel height) for this format.
        """
        ...

    def setPixelAspect(self,aspectRatio) -> None:
        """
        self.setPixelAspect(aspectRatio) -> None

        Set a new pixel aspect ratio for this format. The aspectRatio parameter is the new ratio, found by dividing the desired pixel width by the desired pixel height.
        """
        ...

    def add(self,name) -> None:
        """
        self.add(name) -> None

        Add this instance to a list of "named" formats. The name parameter is the name of the list to add the format to.
        """
        ...

    def fromUV(self, u:Number, v:Number) -> Iterable:
        """
        self.fromUV(u, v) -> [x, y]

        Transform a UV coordinate in the range 0-1 into the format's XY range. Returns a list containing the x and y coordinates.

        @param u: The U coordinate.
        @param v: The V coordinate.
        @return: [x, y]
        """
        ...

    def toUV(self, x:Number, y:Number) -> Iterable:
        """
        self.toUV(x, y) -> (u, v)

        Back-transform an XY coordinate in the format's space into UV space.

        @param x: The X coordinate.
        @param y: The Y coordinate.
        @return: [u, v].
        """
        ...

    def scaled(self, sx:Number, sy, tx, ty) -> Format:
        """
        scaled(sx, sy, tx, ty) -> Format

        Scale and translate this format by sx, sy, tx and ty.

        @param sx: Scale factor in X.@param sy: Scale factor in Y.@param tx: Offset factor in X.@param ty: Offset factor in Y.@return: Format.
        """
        ...
