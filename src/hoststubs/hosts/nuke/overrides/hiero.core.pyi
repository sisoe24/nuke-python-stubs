def project(name: str) -> Project | None: ...

@overload
def projects() -> tuple[Project, ...]: ...
@overload
def projects(projectTypes: Any) -> tuple[Project, ...]: ...


class Project:
    def sequences(self, partialName: str | None = ...) -> list[Sequence]: ...

    def clips(self, partialName: str | None = ...) -> list[Clip]: ...

    def bins(self, partialName: str | None = ...) -> list[Bin]: ...

    def tracks(self, partialName: str | None = ...) -> list[VideoTrack | AudioTrack]: ...

    def videoTracks(self, partialName: str | None = ...) -> list[VideoTrack]: ...

    def audioTracks(self, partialName: str | None = ...) -> list[AudioTrack]: ...

    def trackItems(self, partialName: str | None = ...) -> list[TrackItem]: ...

    def videoTrackItems(self, partialName: str | None = ...) -> list[TrackItem]: ...

    def audioTrackItems(self, partialName: str | None = ...) -> list[TrackItem]: ...

    def extractSettings(self) -> dict[str, str | bool]: ...

    @overload
    def setOutputFormat(self, format: Format) -> None: ...
    @overload
    def setOutputFormat(self, width: Any, height: Any, pixelAspect: Any, name: Any) -> None: ...


class Sequence:
    def videoTracks(self) -> tuple[VideoTrack, ...]: ...

    def items(self) -> tuple[VideoTrack | AudioTrack, ...]: ...

    def addClip(
        self, clip: Clip, time: float, videoTrackIndex: int = ..., audioTrackIndex: int = ...,
    ) -> list[TrackItem]: ...


class VideoTrack:
    def items(self) -> tuple[TrackItem, ...]: ...

    @overload
    def addTrackItem(self, clip: Clip, position: int) -> TrackItem: ...
    @overload
    def addTrackItem(self, trackItem: TrackItem) -> TrackItem: ...


class Clip:
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
    def addToNukeScript(
        self,
        script: hiero.core.nuke.ScriptWriter,
        offset: Any = ...,
        inputs: Any = ...,
        startHandle: Any = ...,
        endHandle: Any = ...,
        addLifetime: bool = ...,
    ) -> Any: ...

    def isRetimeEffect(self) -> bool: ...

    def setName(self, name: str) -> None: ...


class TrackItem:
    def source(self) -> Clip | Sequence | MediaSource: ...

    def thumbnail(self, frame: int = ..., layer: str = ...) -> QtGui.QImage: ...


class Bin:
    def importSequence(
        self,
        filename: str,
        timeBase: TimeBase = ...,
        frameRate: float = ...,
        dropFrame: bool = ...,
    ) -> Sequence: ...
