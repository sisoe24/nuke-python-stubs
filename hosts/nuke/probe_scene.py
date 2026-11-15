"""The scene the probe runs against. Runs inside Nuke: standard library and nuke only.

An empty script makes `allNodes()` return an empty list and every getter
return None, so the probe needs nodes that are wired, selected and animated.
"""
import sys

import nuke

# One of each common kind: generators, filters, merges, 3D, IO, groups, annotations.
NODE_CLASSES = (
    'Constant', 'CheckerBoard2', 'Read', 'Blur', 'Grade', 'ColorCorrect', 'Transform', 'Crop',
    'Reformat', 'Shuffle2', 'Keyer', 'Expression', 'TimeOffset', 'FrameHold', 'Merge2', 'Switch',
    'Roto', 'Camera3', 'Axis3', 'Card2', 'Scene', 'ScanlineRender', 'NoOp', 'Dot', 'Group',
    'BackdropNode', 'StickyNote', 'Write', 'Viewer',
)

# Found by running: constructing one of these ends the session.
CRASHING_KNOBS = ('Gsv_Knob',)

# probe.py stores this in probe.json. build() appends what it created.
DESCRIPTION = []


def _attempt(label, create):
    """Create one scene object. A class missing in this version is noted, not fatal."""
    # Written first, so the log names the step if it takes the host down.
    sys.stderr.write('scene: {}\n'.format(label))
    sys.stderr.flush()

    try:
        created = create()
    except Exception as error:
        DESCRIPTION.append('{}: not created ({})'.format(label, type(error).__name__))
        return []

    DESCRIPTION.append(label)
    return created if isinstance(created, list) else [created]


def build():
    objects = [nuke.root()]

    nodes = []
    for node_class in NODE_CLASSES:
        # Each new node connects to the selected one, so the nodes form a chain.
        nodes += _attempt('node ' + node_class, lambda: nuke.createNode(node_class, inpanel=False))
    objects += nodes

    blur = nuke.toNode('Blur1')
    if blur is not None:
        size = blur['size']
        size.setAnimated()
        size.setValueAt(2, 1)
        size.setValueAt(8, 20)
        curves = _attempt('animation curve on Blur1.size', lambda: list(size.animations()))
        objects += curves
        for curve in curves:
            objects += _attempt('animation keys', lambda: list(curve.keys()))
        blur.setSelected(True)

    # Knob classes that no built-in node above uses, as user knobs on one node.
    holder = nuke.toNode('NoOp1')
    knob_classes = sorted(
        name for name in dir(nuke) if name.endswith('_Knob') and name not in CRASHING_KNOBS
    )
    for name in knob_classes:
        created = _attempt('user knob ' + name, lambda: getattr(nuke, name)('probe_' + name))
        if created and holder is not None:
            _attempt('add ' + name, lambda: holder.addKnob(created[0]) or [])

    for node in nodes:
        objects += [node.knob(index) for index in range(node.numKnobs())]
    DESCRIPTION.append('every knob of every node')

    objects += _attempt('formats', lambda: nuke.formats()[:2])
    objects += _attempt('FrameRange 1-10', lambda: nuke.FrameRange('1-10'))
    objects += _attempt('FrameRanges 1-10 20-30', lambda: nuke.FrameRanges('1-10 20-30'))
    objects += _attempt('Box 0 0 10 10', lambda: nuke.Box(0, 0, 10, 10))
    objects += _attempt('Hash', lambda: nuke.Hash())
    objects += _attempt('Layer rgba', lambda: nuke.Layer('rgba'))

    return objects


def candidates():
    """Values the parameter probe offers to each argument position, most common first."""
    blur = nuke.toNode('Blur1')
    return [
        'hoststubs_probe', 1, 0.5, True, None, [], (), {},
        blur, blur['size'], nuke.root().format(), nuke.FrameRange('1-10'),
        _callback,
    ]


def _callback(*args, **kwargs):
    return None
