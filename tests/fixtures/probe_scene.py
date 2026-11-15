"""Scene for the probe test: two nodes and a format with one slot set."""
import fxhost

DESCRIPTION = []


def build():
    fmt = fxhost.Format()
    fmt.width = 1920
    DESCRIPTION.append('two nodes, one format with width set')
    return [fxhost.Node(), fxhost.Node(), fmt]


def candidates():
    return ['text', 1, 0.5, True, None, [], (), {}, fxhost.Node()]
