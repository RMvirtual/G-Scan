import wx

from maths import Vector2D


class Camera:
    def __init__(
        self,
        position: Vector2D | None = None,
        dimensions: Vector2D | None = None,
        zoom: float = 1.0,
    ) -> None:
        self.position = (
            position if position is not None else Vector2D(0.0, 0.0)
        )

        self.dimensions = (
            dimensions if dimensions is not None else Vector2D(0.0, 0.0)
        )

        self.zoom = zoom

    def rect(self) -> wx.Rect:
        rectangle = wx.Rect2D(
            self.position.x,
            self.position.y,
            self.dimensions.x,
            self.dimensions.y,
        )

        rectangle.Scale(1 / self.zoom)

        result = wx.Rect(
            int(rectangle.Left),
            int(rectangle.Top),
            int(rectangle.GetSize().Width),
            int(rectangle.GetSize().Height),
        )

        return result
