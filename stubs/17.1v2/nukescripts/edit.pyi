# Type stubs for nuke 17.1v2. Generated; do not edit.

def branch() -> None: ...

def cut_paste_file() -> str: ...

def extract() -> None:
    """Disconnect all arrows between selected and unselected nodes, and move selected nodes to the right.
    This function is maintained only for compatibility.  Please use nuke.extractSelected() instead.
    """

def node_copypaste() -> None: ...

def remove_inputs() -> None: ...
