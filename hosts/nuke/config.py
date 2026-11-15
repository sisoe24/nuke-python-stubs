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
    stub_revisions={},
)
