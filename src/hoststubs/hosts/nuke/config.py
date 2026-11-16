from __future__ import annotations

from hoststubs.host import HostConfig

HOST = HostConfig(
    name='nuke',
    # `types-nuke` belongs to an unrelated project.
    package_name='nuke-stubs',
    version_attribute='nuke.NUKE_VERSION_STRING',
    roots=('nuke', 'nuke_internal', 'nukescripts', 'ocionuke', 'hiero'),
    # Examples are not API: hiero's register UI at import, nukescripts' need sip.
    skip=('hiero.examples', 'nukescripts.pyQtExamples'),
    # hiero's C modules are importable as top-level `core` and `ui` in a GUI session.
    private={'core': 'hiero.core', 'ui': 'hiero.ui'},
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
    probe_messages=(
        (r'expecting a Nuke node type', 'nuke.Node'),
        (r'expecting a sequence', 'typing.Sequence[typing.Any]'),
        (r'expecting either a string/integer/view', 'builtins.str | builtins.int | nuke.View'),
        (r'expecting (?:either )?a string(?:/| or )number', 'builtins.str | builtins.float'),
        (r'expecting OutputContext or None', 'nuke.OutputContext | None'),
    ),
    probe_skip_words=frozenset({
        # Seed list: ends the session or the scene.
        'exit', 'quit', 'close', 'delete', 'clear', 'save', 'load', 'execute', 'render',
        # Can reach the disk, the network or another process.
        'remove', 'destroy', 'kill', 'fork', 'crash', 'abort', 'write', 'sync', 'send',
        'connect', 'install', 'uninstall', 'import', 'export', 'open', 'new', 'restore',
        'reload', 'spawn', 'launch', 'flush', 'purge', 'upload', 'download', 'submit',
        'publish', 'register', 'unregister', 'reset', 'revert', 'trash', 'localise', 'localize',
        'transcode',
        # Opens a modal dialog in a GUI session, which blocks until someone answers.
        'show', 'ask', 'choose', 'browse', 'dialog', 'prompt', 'popup', 'message', 'picker',
        'chooser', 'exec',
        # Changes the user's clipboard.
        'copy', 'cut', 'paste',
    }),
    probe_skip=frozenset({
        # Sync review opens network sessions.
        'hiero.syncreview',
        # Sets up the hiero UI; calling it again in a running session is not a query.
        'hiero.ui.Initialise',
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
        'nuke.AnimationCurve.changeInterpolation',
        'nuke.Node.forceValidate',
        'nuke_internal.geo.bestFitPlane',
        # The same, in a Nuke Studio 15.2v9 GUI session.
        'hiero.core.Project.cancelUndo',
        'hiero.ui.Viewer.toggleFullScreen',
        # The same, on Nuke 17.1v2.
        'hiero.ui.Viewer.enterFullScreen',
        'hiero.ui.Viewer.image',
        'hiero.ui.Viewer.toggleFullScreen1_1',
        'nuke.expandSelectedGroup',
        'nuke.makeGroup',
    }),
    stub_revisions={'15.2v9': 0, '17.1v2': 0},
)
