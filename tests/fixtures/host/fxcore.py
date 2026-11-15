"""Stand-in for a C module that is importable under a public top-level name.

hiero's `core` and `ui` are like this in a GUI session: users reach them
only through `hiero.core` and `hiero.ui`.
"""
from __future__ import annotations


class Track:
    def items(self):
        """self.items() -> tuple of the items on this track."""
