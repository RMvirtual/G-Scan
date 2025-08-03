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
        scaled_dimensions = self.dimensions * (1.0 / self.zoom)
        top_left = self.position - scaled_dimensions / 2

        result = wx.Rect(
            int(top_left.x),
            int(top_left.y),
            int(scaled_dimensions.x),
            int(scaled_dimensions.y),
        )

        return result
