# Type stubs for nuke 15.2v9. Generated; do not edit.

PLUGINS_FILTER: list

def load_all_plugins() -> None:
    """Scan all of Nuke's plugin load paths and attempt to load any .dylib, .so, or .dll
    files as a plugin, skipping any files listed in PLUGINS_FILTER.
    """
