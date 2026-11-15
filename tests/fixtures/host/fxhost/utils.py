from __future__ import annotations

__all__ = ['frame_range']


def frame_range(first: int, last: int, step=1) -> list[int]:
    """Frames from first to last, inclusive."""
    return list(range(first, last + 1, step))
