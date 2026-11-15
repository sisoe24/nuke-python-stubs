from __future__ import annotations


class Signal:
    """Like the real one: a descriptor in the class body that is not callable."""

    def __get__(self, instance, owner):
        return self


class QObject:
    pass
