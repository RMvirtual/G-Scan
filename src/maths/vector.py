from __future__ import annotations

from typing import Self

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

    def __iadd__(self, other: Vector2D) -> Self:
        self.x += other.x
        self.y += other.y

        return self

    def __sub__(self, other: Vector2D) -> Vector2D:
        return Vector2D(self.x - other.x, self.y - other.y)

    def __isub__(self, other: Vector2D) -> Self:
        self.x -= other.x
        self.y -= other.y

        return self

    def __truediv__(self, scalar: float) -> Vector2D:
        return Vector2D(self.x / scalar, self.y / scalar)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"({self.x},{self.y})"
