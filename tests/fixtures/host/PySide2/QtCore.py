from __future__ import annotations


class Signal:
    """Like the real one: a callable method descriptor in the class body."""

    def __get__(self, instance, owner):
        return self

    def __call__(self, *args):
        return self


class QObject:
    pass
