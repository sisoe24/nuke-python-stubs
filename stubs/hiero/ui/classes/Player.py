"""Stubs generated automatically from Nuke's internal interpreter."""
import typing
from typing import *

import ui
import core
import hiero
import PySide2
from PySide2.QtCore import Signal
from PySide2.QtWidgets import *

from . import *


class Player(Object):
    """
    Object representing a video player in Hiero. Players are used by Viewer objects, and can be retrieved using the player() method of Viewer objects.
    """

    def __new__(self, *args, **kwargs) -> None:
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
        ...

    def LUT(self) -> str:
        """
        self.LUT() -> returns the name of the LUT currently in use by the player.

        @return: string
        """
        ...

    def alphaIsTransparent(self) -> bool:
        """
        self.alphaIsTransparent() -> returns whether the player treats the alpha channel as premultiplied transparency (True) or not (False).

        @return: True or False
        """
        ...

    def centerImage(self) -> None:
        """
        self.centerImage() -> centers the player, resetting the pan values.
        """
        ...

    def channels(self) -> ui.Player.Channels:
        """
        self.channels() -> returns channel(s) that the player is currently displaying.

        @return: hiero.ui.Player.Channels object
        """
        ...

    def displayGain(self) -> float:
        """
        self.displayGain() -> returns the current gain of the player. Defaults to 1.0

        @return: float
        """
        ...

    def displayGamma(self) -> float:
        """
        self.displayGamma() -> returns the current gamma of the player. Since the viewer displays pixels in linear space, this value defaults to 1.0.

        @return: float
        """
        ...

    def guideOverlay(self) -> object:
        """
        self.guideOverlay() -> returns the guide overlays displayed in the player.

        @return: sequence of foundry.ui.Drawing
        """
        ...

    def ignorePixelAspectRatio(self) -> bool:
        """
        self.ignorePixelAspectRatio() -> returns whether the player ignores the pixel aspect ratio or not.

        @return: True or False
        """
        ...

    def maskOverlay(self) -> object:
        """
        self.maskOverlay() -> returns the drawing used as the mask overlay in the player.

        @return: foundry.ui.Drawing
        """
        ...

    def maskOverlayStyle(self) -> ui.Player.MaskOverlayStyle:
        """
        self.maskOverlayStyle() -> returns the current drawing style of the mask overlay used by the player.

        @return: hiero.ui.Player.MaskOverlayStyle
        """
        ...

    def pan(self, dx: float, dy: float) -> None:
        """
        self.pan(dx, dy) -> pans the player by (dx, dy).

        @param dx: float value to pan in x by
        @param dy: float value to pan in y by
        """
        ...

    def proxyResolution(self) -> ui.Player.ProxyResolution:
        """
        self.proxyResolution() -> get the current proxy resolution setting for the player

        @return: Player.ProxyResolution
        """
        ...

    def rect(self) -> PySide2.QtCore.QRect:
        """
        self.rect() -> player rectangular area in GL coordinates.

        @return: rectangle
        """
        ...

    def sequence(self, *args: typing.Any, **kwargs: typing.Any) -> Iterable:
        """
        self.sequence() -> returns the object currently being played.

        @return: hiero.core.Clip object or hiero.core.Sequence object, depending on what is currently playing
        """
        ...

    def setAlphaIsTransparent(self, alphaIsTransparent: bool) -> None:
        """
        self.setAlphaIsTransparent( alphaIsTransparent ) -> sets whether the player treats the alpha channel as premultiplied transparency.

        @param alphaIsTransparent: True to have the player treat alpha as premultiplied transparency, False otherwise
        """
        ...

    def setChannels(self, channels: ui.Player.Channels) -> None:
        """
        self.setChannels(channels) -> sets the channels to display in the player. It's currently either one of the channels or red, green and blue.

        @param channels: hiero.ui.Player.Channels object
        """
        ...

    def setDisplayGain(self, gain: float) -> None:
        """
        self.setDisplayGain(gain) -> sets the gain of the player.

        @param gain: float
        """
        ...

    def setDisplayGamma(self, gamma: float) -> None:
        """
        self.setDisplayGamma(gamma) -> sets the gamma of the player.

        @param gamma: float
        """
        ...

    def setGuideOverlay(self, arg__1: object) -> object:
        """
        self.setGuideOverlay(guideOverlays) -> sets the guide overlays to display in the player.

        @param guideOverlays: sequence of foundry.ui.Drawing
        """
        ...

    def setIgnorePixelAspectRatio(self, ignorePixelAspectRatio: bool) -> None:
        """
        self.setIgnorePixelAspectRatio(ignorePixelAspectRatio) -> tells the player whether or not to display in anamorphic mode.

        @param ignorePixelAspectRatio: True to have the player ignore the pixel aspect ratio, False otherwise
        """
        ...

    def setLUT(self, lut: str) -> None:
        """
        self.setLUT(lut) -> sets the LUT to use in the player. If the lut doesn't exist, will raise an exception.

        @param lut: string name of the lut to use
        """
        ...

    def setMaskOverlay(self, arg__1: object) -> object:
        """
        self.setMaskOverlay(aspect) -> sets the drawing to use for the mask overlay.

        @param aspect: foundry.ui.Drawing
        """
        ...

    def setMaskOverlayStyle(self, maskOverlayStyle: ui.Player.MaskOverlayStyle) -> None:
        """
        self.setMaskOverlayStyle(style) -> sets the drawing style of the mask overlay.

        @param style: hiero.ui.Player.MaskOverlayStyle style
        """
        ...

    def setProxyResolution(self, resolution: ui.Player.ProxyResolution) -> None:
        """
        self.setProxyResolution(resolution) -> set the player proxy resolution.

        @param resolution: Player.ProxyResolution
        """
        ...

    def setSequence(self, sequence: core.SequenceBase) -> None:
        """
        self.setSequence(clip) -> deprecated; use Viewer.setSequence instead
        """
        ...

    def setWarningOverlay(self, warningOverlay: ui.Player.WarningOverlay) -> None:
        """
        self.setWarningOverlay(warningOverlay) -> sets the warning overlay.

        @param warningOverlay: One of the following enums: eWarningNone, eWarningExposure, eWarningPAL or eWarningNTSC
        """
        ...

    def setZoomMode(self, mode: ui.Player.ZoomMode) -> None:
        """
        self.setZoomMode(mode) -> Change the current zoom mode. Use zoomAbsolute or zoomRelative for eZoomFixed instead of this method.

        @param mode: Zoom mode
        """
        ...

    def time(self) -> int:
        """
        self.time() -> gets the time of the playhead.

        @return: frame number
        """
        ...

    def translation(self) -> PySide2.QtCore.QPointF:
        """
        self.translation() -> translation applied to the footage in the player.

        @return: float
        """
        ...

    def warningOverlay(self) -> ui.Player.WarningOverlay:
        """
        self.warningOverlay() -> returns player's warningOverlay.

        @return: One of the following enums: eWarningNone, eWarningExposure, eWarningPAL or eWarningNTSC
        """
        ...

    def zoom(self) -> float:
        """
        self.zoomMode() -> current zoom

        @return: float
        """
        ...

    def zoomAbsolute(self, centreX: float, centreY: float, zoom: float) -> None:
        """
        self.zoomAbsolute(centerX, centerY, zoom) -> sets the zoom to a specific centre and zoom level, ignoring previous zoom state.

        @param centerX: new relative center of the zoom
        @param centerY: new relative center of the zoom
        @param zoom: float value scale by
        """
        ...

    def zoomMode(self) -> ui.Player.ZoomMode:
        """
        self.zoomMode() -> current zoom mode.

        @return: ZoomMode
        """
        ...

    def zoomRelative(self, centreX: float, centreY: float, zoomFactor: float) -> None:
        """
        self.zoomRelative(centerX, centerY, zoomFactor) -> scales the image relatively and repositions the image.

        @param centerX: new x center of the image, in image pixels
        @param centerY: new y center of the image, in image pixels
        @param zoom: float value scale by
        """
        ...

    def zoomToActualSize(self) -> None:
        """
        self.zoomToActualSize() -> scales and centers the image to the full size of the image.
        """
        ...

    def zoomToFill(self) -> None:
        """
        self.zoomToFill() -> scales the image so that it fills the player window.
        """
        ...

    def zoomToFit(self) -> None:
        """
        self.zoomToFit() -> scales the image so that it fits in the player window, maintaining the pixel aspect ratio.
        """
        ...

    def zoomToFitHeight(self) -> None:
        """
        self.zoomToFitHeight() -> scales the image so that the height of the image fits in the player window, maintaining the pixel aspect ratio.
        """
        ...

    def zoomToFitWidth(self) -> None:
        """
        self.zoomToFitWidth() -> scales the image so that the width of the image fits in the player window, maintaining the pixel aspect ratio.
        """
        ...

    def zoomToHalfSize(self) -> None:
        """
        self.zoomToActualSize() -> scales and centers the image to half the size of the image.
        """
        ...

    def __copy__(self,) -> None:
        """

        """
        ...

    Channels: Any = None
    eChannelRGB: Any = None
    eChannelR: Any = None
    eChannelG: Any = None
    eChannelB: Any = None
    eChannelA: Any = None
    eChannelLuma: Any = None
    MaskOverlayStyle: Any = None
    eMaskOverlayNone: Any = None
    eMaskOverlayLines: Any = None
    eMaskOverlayHalf: Any = None
    eMaskOverlayFull: Any = None
    WarningOverlay: Any = None
    eWarningNone: Any = None
    eWarningExposure: Any = None
    eWarningPAL: Any = None
    eWarningNTSC: Any = None
    ProxyResolution: Any = None
    eProxyAuto: Any = None
    eProxyFull: Any = None
    eProxy2: Any = None
    eProxy4: Any = None
    eProxy8: Any = None
    eProxy16: Any = None
    eProxy32: Any = None
    ZoomMode: Any = None
    eZoomFixed: Any = None
    eZoomToFit: Any = None
    eZoomToFill: Any = None
    eZoomToFitWidth: Any = None
    eZoomToFitHeight: Any = None

    def __init__(self,  *args, **kwargs) -> None:
        """
        Initialize self.  See help(type(self)) for accurate signature.
        """
        ...
