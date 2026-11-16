# Type stubs for nuke 15.2v9. Generated; do not edit.

"""Module for accessing OCIO configs."""

from typing import Any
import typing as _typing

List: Any

def getOCIOConfig() -> Any:
    """Get the current OCIO config, as specified by the root node."""

def getOCIOConfigDirs() -> Any:
    """Get the list of directories where OCIO configs are stored."""

def list_rindex(l: _typing.List, value: Any) -> int: ...

def loadConfig(configPath: Any) -> Any:
    """Load the OCIO Config from the given path"""
