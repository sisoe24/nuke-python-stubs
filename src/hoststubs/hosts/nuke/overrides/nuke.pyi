# Corrections for the nuke module. Format: src/hoststubs/overrides.py.
#
# Ported from NUKE_POST_FIXES and NUKE_POST_INJECT in the old nukestubsgen.py,
# then checked against a Nuke 15.2v9 session where a call could show the type.
# "verified" below means observed there.

# verified: type(nuke.root()) is Root.
# src: manual
def root() -> Root: ...

# verified: returns None for a name that does not exist.
# src: manual
def toNode(s: str) -> Node | None: ...

# verified: `group` must be a node ("expecting a Nuke node type"), not a name.
# src: manual
def allNodes(filter: str = ..., group: Node = ..., recurseGroups: bool = ...) -> list[Node]: ...

# verified: several values are accepted.
# src: manual
def tprint(*value: Any, sep: str = ..., end: str = ..., file: Any = ...) -> None: ...

# The docstring line says None; its text says the task id, an integer.
# `views` are view names (docstring: "A list of view names").
# src: manual
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

# src: manual
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

# Docstring: "ranges is a sequence of range lists", each of first, last, incr.
# src: manual
def executeMultiple(
    nodes: Sequence[Node],
    ranges: Sequence[Sequence[int]] = ...,
    views: list[str] = ...,
    continueOnError: bool = ...,
) -> None: ...


class Node:
    # verified: returns None for a knob that does not exist.
    # src: manual
    def knob(self, p: str | int, follow_link: bool = ...) -> Knob | None: ...

    # verified: raises NameError for a knob that does not exist, so never None.
    # src: manual
    def __getitem__(self, key: str, /) -> Knob: ...

    # verified
    # src: manual
    def dependent(self, what: int = ..., forceEvaluate: bool = ...) -> list[Node]: ...


class Menu:
    # `command` is a script string or a callable. Parameter names follow the docstring.
    # src: manual
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
    # src: manual
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
