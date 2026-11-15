from __future__ import annotations

from hoststubs.host import HostConfig

HOST = HostConfig(
    name='nuke',
    version_attribute='nuke.NUKE_VERSION_STRING',
    roots=('nuke', 'nuke_internal', 'nukescripts', 'ocionuke', 'hiero'),
    # Examples are not API: hiero's register UI at import, nukescripts' need sip.
    skip=('hiero.examples', 'nukescripts.pyQtExamples'),
    # hiero's C modules are importable as top-level `core` and `ui` in a GUI session.
    private=('core', 'ui'),
    type_names={
        'string': 'builtins.str',
        'String': 'builtins.str',
        'Bool': 'builtins.bool',
        'Boolean': 'builtins.bool',
        'boolean': 'builtins.bool',
        'true': 'builtins.bool',
        'integer': 'builtins.int',
        'Integer': 'builtins.int',
        'Float': 'builtins.float',
        'double': 'builtins.float',
        'List': 'builtins.list',
        'Dict': 'builtins.dict',
        'Tuple': 'builtins.tuple',
    },
    probe_skip_words=frozenset({
        # Seed list: ends the session or the scene.
        'exit', 'quit', 'close', 'delete', 'clear', 'save', 'load', 'execute', 'render',
        # Can reach the disk, the network or another process.
        'remove', 'destroy', 'kill', 'fork', 'crash', 'abort', 'write', 'sync', 'send',
        'connect', 'install', 'uninstall', 'import', 'export', 'open', 'new', 'restore',
        'reload', 'spawn', 'launch', 'flush', 'purge', 'upload', 'download', 'submit',
        'publish', 'register', 'unregister',
    }),
    probe_skip=frozenset({
        # Writes a toolset file under ~/.nuke.
        'nuke.createToolset',
        # Found by running: each of these ends a terminal session of Nuke 15.2v9.
        'nuke.Knob.makeWidget',
        'nuke.Node.error',
        'nuke.Node.hasError',
        'nuke.Node.treeHasError',
        'nuke.duplicateSelectedNodes',
        'nuke.getColor',
        'nuke.hotkeys',
        'nuke.licenseInfo',
        'nuke.selectPattern',
        'nuke.waitForThreadsToFinish',
        # The same, on Nuke 17.1v2.
        'nuke.expandSelectedGroup',
        'nuke.makeGroup',
    }),
    stub_revisions={},
)
