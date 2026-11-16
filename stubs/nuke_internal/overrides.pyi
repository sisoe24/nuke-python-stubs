# Type stubs for nuke 15.2v9. Generated; do not edit.

from typing import Any

def dependencies(nodes: Any, what: Any = ...) -> list[Any]:
    """List all nodes referred to by the nodes argument. 'what' is an optional integer (see below).
      You can use the following constants or'ed together to select the types of dependencies that are looked for:
             nuke.EXPRESSIONS = expressions
             nuke.LINKINPUTS = link knob inputs
             nuke.LINKNODE_INPUTS = link nodes
             nuke.INPUTS = visible input pipes
             nuke.HIDDEN_INPUTS = hidden input pipes.
      The default is to look for all types of connections.
  
    Example:
      n1 = nuke.nodes.Blur()
      n2 = nuke.nodes.Merge()
      n2.setInput(0, n1)
      deps = nuke.dependencies([n2], nuke.INPUTS | nuke.HIDDEN_INPUTS | nuke.EXPRESSIONS)
    """

def dependentNodes(what: Any = ..., nodes: Any = ..., evaluateAll: bool = ...) -> list[Any]:
    """List all nodes referred to by the nodes argument. 'what' is an optional integer (see below).
      You can use the following constants or'ed together to select what types of dependent nodes are looked for:
             nuke.EXPRESSIONS = expressions
             nuke.LINKINPUTS = link knob inputs
             nuke.LINKNODE_INPUTS = link nodes
             nuke.INPUTS = visible input pipes
             nuke.HIDDEN_INPUTS = hidden input pipes.
      The default is to look for all types of connections.

      evaluateAll is an optional boolean defaulting to True. When this parameter is true, it forces a re-evaluation of the entire tree.
      This can be expensive, but otherwise could give incorrect results if nodes are expression-linked.

  
    Example:
      n1 = nuke.nodes.Blur()
      n2 = nuke.nodes.Merge()
      n2.setInput(0, n1)
      ndeps = nuke.dependentNodes(nuke.INPUTS | nuke.HIDDEN_INPUTS | nuke.EXPRESSIONS, [n1])

      @param what: Or'ed constant of nuke.EXPRESSIONS, nuke.LINKINPUTS, nuke.LINKNODE_INPUTS, nuke.INPUTS and nuke.HIDDEN_INPUTS to select the types of dependent nodes. The default is to look for all types of connections.
      @param evaluateAll: Specifies whether a full tree evaluation will take place. Defaults to True.
      @return: List of nodes. 
    """

def pluginAddPath(args: Any, addToSysPath: bool = ...) -> None:
    """Adds all the paths to the beginning of the Nuke plugin path.
    If the path already exists in the list of plugin paths, it is moved
    to the start. If this command is executed inside an init.py then
    the init.py in the path will be executed.
    It also adds the paths to the sys.path, if addToSysPath is True.
    """

def pluginAppendPath(args: Any, addToSysPath: bool = ...) -> None:
    """Add a filepath to the end of the Nuke plugin path.  If the path
    already exists in the list of plugin paths, it will remain at its
    current position.
    It also appends the paths to the sys.path, if addToSysPath is True.
    """

def selectConnectedNodes() -> None:
    """Selects all nodes in the tree of the selected nodes. """
