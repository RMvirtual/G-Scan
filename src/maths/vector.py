from __future__ import annotations

import wx


class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    @staticmethod
    def fromPoint(point: wx.Point) -> Vector2D:
        return Vector2D(point.x, point.y)

    def __add__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x - other.x, self.y - other.y)
