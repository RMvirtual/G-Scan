import wx

from maths import Vector2D


class MouseState:
    def __init__(self) -> None:
        self.position: Vector2D | None = None
        self.last_dragged: Vector2D | None = None
        self.is_down: bool = False

    def click_down(self, event: wx.MouseEvent) -> None:
        self.is_down = True
        self.position = Vector2D.fromPoint(event.Position)

    def click_release(self, event: wx.MouseEvent) -> None:
        self.last_dragged = None
        self.is_down = False

    def motion(self, event: wx.MouseEvent) -> None:
        if self.is_down:
            self.last_dragged = self.position

        self.position = Vector2D.fromPoint(event.Position)

    def drag_distance(self) -> Vector2D:
        if None in (self.position, self.last_dragged):
            return Vector2D(0, 0)

        return self.position - self.last_dragged
