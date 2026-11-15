"""Nuke usage that the stubs must type. Checked by `python -m hoststubs build`.

Each reveal_type is compared with tests/corpus/snapshots/<host>-<version>.json.
"""
from typing_extensions import reveal_type

import nuke
import nukescripts

# Seeds: the calls most scripts make.
node = nuke.createNode('Blur')
reveal_type(node)
reveal_type(nuke.createNode)
reveal_type(nuke.allNodes())
reveal_type(nuke.allNodes)
reveal_type(nuke.root())
reveal_type(nuke.formats())
reveal_type(nuke.execute)
reveal_type(node.knob('size'))
reveal_type(node['size'])
reveal_type(nuke.Node.knob)

# Every override in hosts/nuke/overrides/nuke.pyi.
reveal_type(nuke.toNode)
reveal_type(nuke.selectedNodes)
reveal_type(nuke.layers)
reveal_type(nuke.recentFile)
reveal_type(nuke.stripFrameRange)
reveal_type(nuke.tprint)
reveal_type(nuke.executeBackgroundNuke)
reveal_type(nuke.executeMultiple)
reveal_type(nuke.Node.knobs)
reveal_type(nuke.Node.allKnobs)
reveal_type(nuke.Node.dependencies)
reveal_type(nuke.Node.dependent)
reveal_type(nuke.Node.rootNode)
reveal_type(nuke.Menu.addCommand)
reveal_type(nuke.MenuBar.addCommand)

# Docstring signature line: `self.name() -> str`, `-> bool.`, `-> None`.
reveal_type(node.name())
reveal_type(nuke.Node.setInput)
reveal_type(nuke.message)

# Docstring fields: `:type knobs: str, optional`, `:rtype: nuke.Node`.
reveal_type(nuke.createNode)

# Dunder table.
reveal_type(len(node))
reveal_type(node == node)

# Return probe: observed in a live session.
reveal_type(nuke.views())
reveal_type(node.pixelAspect())
reveal_type(nuke.nodeTypes())
# The docstring says Node and the probe saw a Root: the docstring stands.
reveal_type(nuke.thisNode())
reveal_type(nuke.Group.selectedNode)

# Parameter probe: types from the argument parser's errors.
reveal_type(nuke.Node.setXYpos)
reveal_type(nuke.Node.input)
reveal_type(nuke.Node.setName)
reveal_type(nuke.Node.metadata)
reveal_type(nuke.Format.scaled)

# Constants and module-level instances.
reveal_type(nuke.ADD_VIEWS)
reveal_type(nuke.nodes)
reveal_type(nuke.env)

# Re-exports: defined in nuke_internal, used as nuke.X.
reveal_type(nuke.addOnCreate)
reveal_type(nuke.scriptExit)
reveal_type(nuke.rotopaint)

# Pure-Python modules: pyright inference on Foundry's source.
reveal_type(nukescripts.PythonPanel)
reveal_type(nukescripts.toolsets.addToolsetsPanel)
reveal_type(nukescripts.clear_selection_recursive)

# Wrong on purpose. Each line must be reported.
nuke.allNodes(group='Group1')
nuke.createNode('Blur', args='size 3')
node.nope()
node.setXYpos('left', 10)
node['size'].nope()
