def root() -> Root: ...

def toNode(s: str) -> Node | None: ...

def allNodes(filter: str = ..., group: Node = ..., recurseGroups: bool = ...) -> list[Node]: ...

def tprint(*value: Any, sep: str = ..., end: str = ..., file: Any = ...) -> None: ...

def executeBackgroundNuke(
    exe_path: str,
    nodes: list[Node],
    frameRange: list[Any],
    views: list[str],
    limits: dict[str, Any],
    continueOnError: bool = ...,
    flipbookToRun: str = ...,
    flipbookOptions: dict[str, Any] = ...,
) -> int: ...

@overload
def execute(
    nameOrNode: Node | str,
    start: int = ...,
    end: int = ...,
    incr: int = ...,
    views: list[str] = ...,
    continueOnError: bool = ...,
) -> None: ...
@overload
def execute(
    nameOrNode: Node | str,
    frameRangeSet: FrameRanges | list[FrameRange],
    views: list[str] = ...,
    continueOnError: bool = ...,
) -> None: ...

def executeMultiple(
    nodes: Sequence[Node],
    ranges: Sequence[Sequence[int]] = ...,
    views: list[str] = ...,
    continueOnError: bool = ...,
) -> None: ...


class Node:
    def knob(self, p: str | int, follow_link: bool = ...) -> Knob | None: ...

    def __getitem__(self, key: str, /) -> Knob: ...

    def dependent(self, what: int = ..., forceEvaluate: bool = ...) -> list[Node]: ...


class Menu:
    def addCommand(
        self,
        name: str,
        command: str | Callable[..., Any] = ...,
        shortcut: str = ...,
        icon: str = ...,
        tooltip: str = ...,
        index: int = ...,
        readonly: bool = ...,
        shortcutContext: int = ...,
        tag: Any = ...,
        tagTarget: Any = ...,
        node: str = ...,
    ) -> Any: ...


class MenuBar:
    def addCommand(
        self,
        name: str,
        command: str | Callable[..., Any] = ...,
        shortcut: str = ...,
        icon: str = ...,
        tooltip: str = ...,
        index: int = ...,
        readonly: bool = ...,
        shortcutContext: int = ...,
        tag: Any = ...,
        tagTarget: Any = ...,
        node: str = ...,
    ) -> Any: ...
