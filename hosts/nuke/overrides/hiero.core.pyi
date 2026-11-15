# Corrections for hiero.core. Format: src/hoststubs/overrides.py.
#
# Ported from HIERO_CORE_POST_FIX in the old nukestubsgen.py, then checked
# against a Nuke Studio 15.2v9 session with one project, one sequence, one
# video track and one audio track. "verified" below means observed there.
#
# The old GLOBAL_POST_FIXES rule that rewrote `core.X` to `hiero.core.X` is
# not here: the dump records hiero classes under hiero.core, and
# tests/test_names.py checks it.

# verified: None for a name that is not loaded.
# src: manual
def project(name: str) -> Project | None: ...

# verified: a tuple.
# src: manual
@overload
def projects() -> tuple[Project, ...]: ...
@overload
def projects(projectTypes: Any) -> tuple[Project, ...]: ...


class Project:
    # verified: a list.
    # src: manual
    def sequences(self, partialName: str | None = ...) -> list[Sequence]: ...

    # verified: a list.
    # src: manual
    def clips(self, partialName: str | None = ...) -> list[Clip]: ...

    # verified: a list.
    # src: manual
    def bins(self, partialName: str | None = ...) -> list[Bin]: ...

    # verified: a list.
    # src: manual
    def tracks(self, partialName: str | None = ...) -> list[VideoTrack | AudioTrack]: ...

    # verified: a list.
    # src: manual
    def videoTracks(self, partialName: str | None = ...) -> list[VideoTrack]: ...

    # verified: a list.
    # src: manual
    def audioTracks(self, partialName: str | None = ...) -> list[AudioTrack]: ...

    # verified: a list.
    # src: manual
    def trackItems(self, partialName: str | None = ...) -> list[TrackItem]: ...

    # verified: a list.
    # src: manual
    def videoTrackItems(self, partialName: str | None = ...) -> list[TrackItem]: ...

    # verified: a list.
    # src: manual
    def audioTrackItems(self, partialName: str | None = ...) -> list[TrackItem]: ...

    # verified: values are str and bool.
    # src: manual
    def extractSettings(self) -> dict[str, str | bool]: ...

    # src: manual
    @overload
    def setOutputFormat(self, format: Format) -> None: ...
    @overload
    def setOutputFormat(self, width: Any, height: Any, pixelAspect: Any, name: Any) -> None: ...


class Sequence:
    # verified: a tuple.
    # src: manual
    def videoTracks(self) -> tuple[VideoTrack, ...]: ...

    # verified: every track, video and audio.
    # src: manual
    def items(self) -> tuple[VideoTrack | AudioTrack, ...]: ...

    # src: manual
    def addClip(
        self, clip: Clip, time: float, videoTrackIndex: int = ..., audioTrackIndex: int = ...,
    ) -> list[TrackItem]: ...


class VideoTrack:
    # verified: a tuple.
    # src: manual
    def items(self) -> tuple[TrackItem, ...]: ...

    # Docstring: a Clip needs a position; a TrackItem is added as it is.
    # src: manual
    @overload
    def addTrackItem(self, clip: Clip, position: int) -> TrackItem: ...
    @overload
    def addTrackItem(self, trackItem: TrackItem) -> TrackItem: ...


class Clip:
    # src: manual
    def addToNukeScript(
        self,
        script: hiero.core.nuke.ScriptWriter,
        additionalNodes: Any = ...,
        additionalNodesCallback: Any = ...,
        firstFrame: Any = ...,
        trimmed: bool = ...,
        trimStart: Any = ...,
        trimEnd: Any = ...,
        colourTransform: Any = ...,
        metadataNode: Any = ...,
        includeMetadataNode: bool = ...,
        nodeLabel: Any = ...,
        enabled: bool = ...,
        includeEffects: bool = ...,
        beforeBehaviour: Any = ...,
        afterBehaviour: Any = ...,
        project: Any = ...,
        readNodes: Any = ...,
        addEffectsLifetime: bool = ...,
    ) -> Any: ...


class EffectTrackItem:
    # src: manual
    def addToNukeScript(
        self,
        script: hiero.core.nuke.ScriptWriter,
        offset: Any = ...,
        inputs: Any = ...,
        startHandle: Any = ...,
        endHandle: Any = ...,
        addLifetime: bool = ...,
    ) -> Any: ...

    # src: manual
    def isRetimeEffect(self) -> bool: ...

    # src: manual
    def setName(self, name: str) -> None: ...


class TrackItem:
    # Docstring: a Clip, a Sequence or a MediaSource, by the kind of track item.
    # src: manual
    def source(self) -> Clip | Sequence | MediaSource: ...

    # Parameter names follow the docstring: thumbnail(frame, layer).
    # src: manual
    def thumbnail(self, frame: int = ..., layer: str = ...) -> QtGui.QImage: ...


class Bin:
    # src: manual
    def importSequence(
        self,
        filename: str,
        timeBase: TimeBase = ...,
        frameRate: float = ...,
        dropFrame: bool = ...,
    ) -> Sequence: ...
