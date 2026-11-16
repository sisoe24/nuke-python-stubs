# Type stubs for nuke 17.1v2. Generated; do not edit.

"""Memory module containing functionality for querying and controlling
Nuke's Memory API, currently the module is named memory2 for
backwards compatibility with the old nuke.memory(cmd, value)
function which is now deprecated. Once removed this module will be
deprecated and it will be renamed to nuke.memory. To avoid future
conflicts it is recommended to import like so:

from nuke import memory2 as memory
"""

def allocatorInfo() -> dict[str, dict]:
    """allocatorInfo() -> dict

    Creates a dictionary of allocators mapped by their name to another dictionary containing various metadata information about the allocator.

    :return: dict
    """

def clearUsage() -> bool:
    """clearUsage() -> bool

    Attempts to clear all memory, setUsage(0) and clearUsage() are effectively the same.
    :return: bool True if anything was freed
    """

def info() -> dict[str, list]:
    """info() -> dict

    Creates a dictionary of Node names mapped to a list of memory information for that node.
    Each entry is a dictionary containing various key value pairs of memory information gathered.

    :return: dict
    """

def maxUsage() -> int:
    """maxUsage() -> int

    Reports the maximum memory usage Nuke will aim to use.
    :return: int bytes maximum usage
    """

def setMaxUsage(int: int) -> None:
    """setMaxUsage(int) -> None

    Set the maximum memory usage Nuke will aim to use.
    :param amount: number of bytes to restrict to
    :return: None
    """

def setUsage(int: int) -> bool:
    """setUsage(int) -> bool

    If the value given is less than the current usage, free memory to the new usage.
    :param amount: number of bytes to reduce current usage to
    :return: bool True if anything was freed
    """

def totalRAM() -> int:
    """totalRAM() -> int

    Reports the total RAM detected by Nuke.

    :return: int bytes total RAM
    """

def totalVM() -> int:
    """totalVM() -> int

    Reports the total virtual memory (VM) detected by Nuke.

    :return: int bytes total VM
    """

def usage() -> int:
    """usage() -> int

    Reports the current memory usage allocated.

    :return: int bytes usage
    """
