"""Pure-Python host scripts: real bodies, few annotations."""
from __future__ import annotations

import os

import fxhost
from PySide2 import QtCore
from PySide2.QtCore import QObject


def node_names(nodes=None, upper=False, prefix=''):
    nodes = nodes or fxhost.allNodes()
    names = [prefix + node.name() for node in nodes]
    return [name.upper() for name in names] if upper else names


def script_directory(path: str | None = None) -> str:
    return os.path.dirname(path or '')


def make_node():
    return fxhost.Node()


def find_panel(name):
    for panel in _panels():
        if panel.name == name:
            return panel
    return None


def _panels():
    return [Panel('main')]


select = node_names


class Panel(QObject):
    """A panel with every member kind."""

    title = 'Panel'
    width = 320
    closed = QtCore.Signal()

    def __init__(self, name, parent=None):
        self._name = name

    @property
    def name(self) -> str:
        """The panel name."""
        return self._name

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @staticmethod
    def default_size():
        return (320, 240)

    @classmethod
    def create(cls, name):
        return cls(name)

    def show(self, modal=False):
        return True

    def on_close(self):
        """Called when the panel closes. Subclasses return False to veto."""
        pass

    class Options:
        compact = False
